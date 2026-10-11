"""Coleta dirigida de URLs oficiais previamente aprovadas, com instantâneo e hashes."""
import argparse
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, quote, unquote
from urllib.request import Request, HTTPRedirectHandler, build_opener

from study import load, write_records

LIMIT = 20 * 1024 * 1024


def check_url(url, host):
    p = urlsplit(url)
    if p.scheme != 'https' or p.hostname != host or p.username or p.password or p.port not in (None, 443):
        raise ValueError('Somente HTTPS no host oficial aprovado, sem credenciais')


class RobotsRules:
    """Grupos específicos, regras mais longas, curingas e fim de caminho do robots.txt."""
    def __init__(self, text):
        self.groups = []
        agents, rules, delay, rate, started = [], [], None, None, False
        for raw in text.splitlines() + ['User-agent: END-OF-PARSE']:
            line = raw.split('#', 1)[0].strip()
            if ':' not in line:
                continue
            key, value = (x.strip() for x in line.split(':', 1))
            key = key.lower()
            if key == 'user-agent':
                if started:
                    self.groups.append((agents, rules, delay, rate))
                    agents, rules, delay, rate, started = [], [], None, None, False
                agents.append(value.lower())
            elif agents:
                started = True
                if key in ('allow', 'disallow') and value:
                    rules.append((key == 'allow', value))
                elif key == 'crawl-delay':
                    try: delay = float(value)
                    except ValueError: pass
                elif key == 'request-rate':
                    try:
                        requests, seconds = map(float, value.split('/'))
                        if requests > 0 and seconds > 0: rate = seconds / requests
                    except ValueError: pass

    def matching(self, agent):
        token = agent.split('/')[0].split(' ')[0].lower()
        matched = [(max((len(a) if a != '*' else 0 for a in agents if a == '*' or a in token), default=-1),
                    rules, delay, rate) for agents, rules, delay, rate in self.groups]
        longest = max((g[0] for g in matched), default=-1)
        return [g for g in matched if g[0] == longest and longest >= 0]

    @staticmethod
    def normalize(value):
        value = quote(value, safe="/%:$*?&=;,+-_.!~'()@")
        def replace(match):
            byte = unquote(match.group())
            return byte if len(byte) == 1 and byte in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~' else match.group().upper()
        return re.sub(r'%[a-fA-F0-9]{2}', replace, value)

    def can_fetch(self, agent, url):
        parsed = urlsplit(url)
        path = self.normalize((parsed.path or '/') + ('?' + parsed.query if parsed.query else ''))
        matches = []
        for _, rules, _, _ in self.matching(agent):
            for allow, pattern in rules:
                pattern = self.normalize(pattern)
                end = pattern.endswith('$')
                body = pattern[:-1] if end else pattern
                regex = '^' + '.*'.join(re.escape(piece) for piece in body.split('*')) + ('$' if end else '')
                if re.search(regex, path):
                    # Comprimento em octetos, desconsiderando o curinga e o marcador de fim.
                    specificity = len(re.sub(r'%[A-F0-9]{2}', 'x', body.replace('*', '')))
                    matches.append((specificity, allow))
        return max(matches)[1] if matches else True

    def crawl_delay(self, agent):
        return max((g[2] or 0 for g in self.matching(agent)), default=0)

    def request_interval(self, agent):
        return max((g[3] or 0 for g in self.matching(agent)), default=0)


class RedirectPolicy(HTTPRedirectHandler):
    def __init__(self, host, robots=None, agent=None):
        self.host, self.robots, self.agent = host, robots, agent

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl, self.host)
        if self.robots and not self.robots.can_fetch(self.agent, newurl):
            raise ValueError('Redirecionamento bloqueado pelo robots.txt')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url, host, agent, robots=None):
    check_url(url, host)
    opener = build_opener(RedirectPolicy(host, robots, agent))
    req = Request(url, headers={'User-Agent': agent, 'Accept': 'text/html,application/pdf,text/plain'})
    with opener.open(req, timeout=30) as response:
        body = response.read(LIMIT + 1)
        if len(body) > LIMIT:
            raise ValueError('Resposta excede 20 MiB')
        check_url(response.url, host)
        return body, response.url, dict(response.headers), response.status


def collect(sources_path, output, agent):
    sources = load(sources_path)
    if not sources:
        raise ValueError('Nenhuma fonte aprovada; preencher cadastro de fontes')
    if 'contato' in agent.lower() or '@' not in agent:
        raise ValueError('Preencher User-Agent de pesquisa com contato real')
    for source in sources:
        for field in ('bank', 'host', 'urls', 'terms_url', 'terms_checked_at', 'collection_permission',
                      'reviewer', 'permission_evidence', 'redistribution'):
            if not source.get(field):
                raise ValueError(f'Cadastro incompleto: {field}')
        if source['collection_permission'] != 'approved':
            raise ValueError('Fonte pendente ou excluída exige resolução antes da coleta')
        check_url(source['terms_url'], source['host'])
        for url in source['urls']:
            check_url(url, source['host'])
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    (out / 'raw').mkdir()
    manifest, errors = [], []
    for source in sources:
        host = source['host']
        try:
            robot_url = f'https://{host}/robots.txt'
            raw, _, _, _ = fetch(robot_url, host, agent)
            robot_path = out / 'raw' / (hashlib.sha256(host.encode()).hexdigest() + '-robots.txt')
            robot_path.write_bytes(raw)
            robots = RobotsRules(raw.decode('utf-8', errors='replace'))
            delay = max(2, robots.crawl_delay(agent), robots.request_interval(agent))
        except Exception as e:
            errors.append({'bank': source['bank'], 'url': f'https://{host}/robots.txt',
                           'status': 'pending', 'error': str(e)})
            continue
        for url in source['urls']:
            try:
                if not robots.can_fetch(agent, url):
                    raise ValueError('Robots.txt impede a coleta por este agente')
                time.sleep(delay)
                body, final_url, headers, status = fetch(url, host, agent, robots)
                mime = headers.get('Content-Type', headers.get('content-type', '')).split(';')[0].strip()
                if mime not in ('text/html', 'application/pdf', 'text/plain'):
                    raise ValueError(f'Tipo documental não suportado: {mime}')
                sha = hashlib.sha256(body).hexdigest()
                document_id = hashlib.sha256((source['bank'] + '\n' + url + '\n' + sha).encode()).hexdigest()
                suffix = '.pdf' if mime == 'application/pdf' else '.html' if mime == 'text/html' else '.txt'
                path = out / 'raw' / (document_id + suffix)
                path.write_bytes(body)
                manifest.append({'document_id': document_id, 'bank': source['bank'], 'url': url,
                    'final_url': final_url, 'collected_at': datetime.now(timezone.utc).isoformat(),
                    'status': status, 'mime': mime, 'headers': headers, 'sha256': sha,
                    'raw_path': str(path.relative_to(out)), 'source_registry': source,
                    'robots_sha256': hashlib.sha256(raw).hexdigest()})
            except Exception as e:
                errors.append({'bank': source['bank'], 'url': url, 'status': 'pending', 'error': str(e)})
    write_records(out / 'manifest.jsonl', manifest)
    write_records(out / 'errors.jsonl', errors)
    if errors:
        raise SystemExit(f'Coleta incompleta: {len(errors)} pendências registradas; resolver antes de congelar.')


def extract(snapshot, output):
    from bs4 import BeautifulSoup
    from pypdf import PdfReader
    snapshot = Path(snapshot)
    documents = []
    for item in [json.loads(s) for s in (snapshot / 'manifest.jsonl').read_text().splitlines()]:
        path = snapshot / item['raw_path']
        if not path.resolve().is_relative_to(snapshot.resolve()):
            raise ValueError('O arquivo de origem precisa estar dentro da pasta da coleta')
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            raise ValueError('Instantâneo alterado')
        sections = []
        title = item['url']
        if item['mime'] == 'application/pdf':
            for i, page in enumerate(PdfReader(path).pages, 1):
                text = page.extract_text() or ''
                if not text.strip():
                    raise ValueError(f'PDF sem texto na página {i}; requer OCR revisado e registrado')
                sections.append({'section': f'Página {i}', 'location': f'page:{i}', 'text': text})
        elif item['mime'] == 'text/html':
            soup = BeautifulSoup(path.read_bytes(), 'html.parser')
            title = soup.title.get_text(' ', strip=True) if soup.title else title
            for node in soup(['script', 'style', 'noscript']):
                node.decompose()
            root = soup.find('main') or soup.find('article') or soup.body or soup
            # ponytail: extração linear conserva tabelas/notas como texto; auditoria humana decide segmentação final.
            text = root.get_text('\n', strip=True)
            sections.append({'section': 'Corpo do documento', 'location': 'html:body', 'text': text})
        else:
            sections.append({'section': 'Documento', 'location': 'text:body',
                             'text': path.read_text(encoding='utf-8')})
        if not any(s['text'].strip() for s in sections):
            raise ValueError('Documento sem conteúdo extraído')
        documents.append({**item, 'title': title, 'sections': sections,
                          'extraction_review': 'pending', 'notes': 'Conferir números, notas, tabelas e cabeçalhos na fonte.'})
    write_records(output, documents)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    s = p.add_subparsers(dest='command', required=True)
    c = s.add_parser('collect'); c.add_argument('sources'); c.add_argument('output')
    c.add_argument('--user-agent', required=True)
    c = s.add_parser('extract'); c.add_argument('snapshot'); c.add_argument('output')
    a = p.parse_args()
    if a.command == 'collect': collect(a.sources, a.output, a.user_agent)
    else: extract(a.snapshot, a.output)
