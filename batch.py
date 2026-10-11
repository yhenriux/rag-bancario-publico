"""Pré-conferência de acesso e catálogo automático, sem promover permissões ou avaliações humanas."""
import argparse
import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from collect import RobotsRules, check_url, collect, extract, fetch
from study import load, records, write, write_records


def preflight(sources_path, output, agent):
    sources = load(sources_path)
    rows = []
    for source in sources:
        host = source['host']
        row = {'bank': source['bank'], 'host': host, 'checked_at': datetime.now(timezone.utc).isoformat(),
               'collection_permission': source.get('collection_permission', 'pending'),
               'agent': agent, 'urls': [], 'corpus_downloaded': False}
        try:
            robot_url = f'https://{host}/robots.txt'
            body, final, _, status = fetch(robot_url, host, agent)
            rules = RobotsRules(body.decode('utf-8', errors='replace'))
            row.update(robots_url=final, robots_status=status, robots_sha256=hashlib.sha256(body).hexdigest())
            for url in source['urls']:
                check_url(url, host)
                row['urls'].append({'url': url, 'robots_allowed': rules.can_fetch(agent, url)})
        except Exception as error:
            row['error'] = str(error)
        rows.append(row)
    write(output, {'kind': 'technical_access_preflight', 'sources': rows,
                  'warning': 'Robots.txt não autoriza coleta. Conferir termos e registrar decisão separadamente.'})
    return rows


CRITICAL = re.compile(r'\b(?:se|desde que|exceto|salvo|somente|apenas|mínimo|máximo|prazo|isenção|anuidade)\b|R\$|\d', re.I)


def catalog(documents_path, output):
    """Propostas determinísticas com passagens literais; desconhecido fica explícito."""
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    entries, passages, seen = [], [], {}
    for doc in records(documents_path):
        duplicate = seen.get((doc['bank'], doc['sha256']))
        seen.setdefault((doc['bank'], doc['sha256']), doc['document_id'])
        flags = []
        total = 0
        categories = set()
        for section in doc['sections']:
            text = section['text']
            total += len(text.strip())
            if re.search(r'\b(conta|contas)\b', text, re.I): categories.add('conta')
            if re.search(r'\b(cartão|cartões)\b', text, re.I): categories.add('cartao')
            if '\ufffd' in text: flags.append('caractere_de_substituicao')
            for match in re.finditer(r'[^\n]+', text):
                if CRITICAL.search(match.group()):
                    passages.append({'document_id': doc['document_id'], 'source_sha256': doc['sha256'],
                        'location': section['location'], 'char_start': match.start(), 'char_end': match.end(),
                        'text': match.group(), 'kind': 'literal_candidate', 'validation': 'not_human_validated'})
        if total < 100: flags.append('texto_curto')
        entries.append({'document_id': doc['document_id'], 'bank': doc['bank'], 'title': doc['title'],
            'url': doc['final_url'], 'collected_at': doc['collected_at'], 'source_sha256': doc['sha256'],
            'mime': doc['mime'], 'sections': len(doc['sections']), 'characters': total,
            'topic_candidates': sorted(categories), 'product': 'desconhecido', 'public': 'desconhecido',
            'duplicate_of': duplicate, 'flags': sorted(set(flags)), 'extraction_review': doc['extraction_review'],
            'annotation_origin': 'deterministic_rules_v1', 'validation': 'not_human_validated'})
    write_records(out / 'catalog.jsonl', entries)
    write_records(out / 'critical-passages.jsonl', passages)
    with (out / 'catalog.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        fields = ('document_id', 'bank', 'title', 'url', 'mime', 'characters', 'duplicate_of', 'flags', 'validation')
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        # CSV destinado à leitura: impedir que títulos ou endereços sejam tratados como fórmulas.
        for entry in entries:
            safe = {k: ("'" + v if isinstance(v, str) and v.startswith(('=', '+', '-', '@')) else v) for k, v in entry.items()}
            writer.writerow(safe)
    summary = {'documents': len(entries), 'unique_per_bank': sum(e['duplicate_of'] is None for e in entries),
               'critical_candidates': len(passages), 'flagged_documents': sum(bool(e['flags']) for e in entries),
               'human_validated': sum(e['extraction_review'] == 'approved' for e in entries),
               'collection_permission_changed': False}
    write(out / 'summary.json', summary)
    return summary


def run_batch(sources, output, agent):
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    # collect valida todos os cadastros antes do primeiro pedido de documento.
    collect(sources, out / 'snapshot', agent)
    extract(out / 'snapshot', out / 'documents.jsonl')
    return catalog(out / 'documents.jsonl', out / 'catalog')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    s = p.add_subparsers(dest='command', required=True)
    for name in ('preflight', 'run'):
        c = s.add_parser(name)
        c.add_argument('sources'); c.add_argument('output'); c.add_argument('--user-agent', required=True)
    c = s.add_parser('catalog'); c.add_argument('documents'); c.add_argument('output')
    a = p.parse_args()
    if a.command == 'preflight': result = preflight(a.sources, a.output, a.user_agent)
    elif a.command == 'run': result = run_batch(a.sources, a.output, a.user_agent)
    else: result = catalog(a.documents, a.output)
    print(json.dumps(result, ensure_ascii=False))
