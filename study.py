"""Operações auditáveis do estudo; somente biblioteca padrão."""
import argparse
import csv
import hashlib
import json
import math
import random
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import NormalDist, mean

CONFIGS = ('A', 'B', 'C', 'Bp', 'L', 'S')
CLASSES = ('direta', 'condicao', 'excecao', 'ambiguidade', 'insuficiencia')


def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def records(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line.strip()]


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Resultados imutáveis: uma nova execução exige outro caminho.
    with path.open('x', encoding='utf-8') as f:
        json.dump(value, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')


def write_records(path, values):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8') as f:
        for value in values:
            f.write(json.dumps(value, ensure_ascii=False, allow_nan=False) + '\n')


def write_csv(path, rows, fields):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def validate_questions(questions, pilot_families=()):
    if not isinstance(questions, list) or not questions:
        raise ValueError('Informe uma lista de perguntas com pelo menos um registro')
    ids = set()
    family_banks = {}
    for q in questions:
        if not isinstance(q, dict):
            raise ValueError('Cada pergunta precisa ser um objeto com os campos indicados no guia')
        for field in ('id', 'bank', 'family', 'class', 'question', 'query_attributes'):
            if field not in q:
                raise ValueError(f'Pergunta sem {field}')
        if not isinstance(q['id'], str) or not re.fullmatch(r'[A-Za-z0-9_-]+', q['id']):
            raise ValueError('ID de pergunta deve conter apenas letras, números, _ e -')
        if q['id'] in ids or q['class'] not in CLASSES:
            raise ValueError('Identificador repetido ou classe inválida')
        ids.add(q['id'])
        if not isinstance(q['bank'], str) or not isinstance(q['family'], str) or not q['bank'] or not q['family']:
            raise ValueError('Banco e família devem ser textos não vazios')
        if q['family'] in pilot_families:
            raise ValueError('Família do piloto presente na amostra final')
        previous = family_banks.setdefault(q['family'], q['bank'])
        if previous != q['bank']:
            raise ValueError('Família precisa ter identificador único, incluindo o banco')
        if not isinstance(q['question'], str) or not q['question'].strip():
            raise ValueError('Escreva o texto da pergunta')
        if not isinstance(q['query_attributes'], dict):
            raise ValueError('Os atributos da pergunta precisam ser um objeto')
        for attr, values in q['query_attributes'].items():
            if attr not in ('product', 'public') or not isinstance(values, list) or not values or any(
                not isinstance(v, str) or not v.strip() or v in ('geral', 'desconhecido') for v in values
            ):
                raise ValueError('Filtro exige atributo explícito e valores em lista')


def compatible(metadata, query_attributes):
    for attr, required in query_attributes.items():
        values = metadata[attr]
        if not values or not isinstance(values, list):
            raise ValueError('Use categorias explícitas: geral ou desconhecido')
        if any(v in ('geral', 'desconhecido') for v in values):
            continue
        if not set(values).intersection(required):
            return False
    return True


def prefix(chunk, metadata, config):
    if config in ('A', 'L', 'S'):
        return ''
    fields = [('Produto', ', '.join(metadata['product'])), ('Público', ', '.join(metadata['public']))]
    if config in ('B', 'C'):
        fields = [('Título', chunk['title']), ('Seção', chunk['section']),
                  ('Tipo', metadata['document_type'])] + fields
    return '\n'.join(f'{name}: {value}' for name, value in fields) + '\n'


def words(text):
    return re.findall(r'\w+', text.lower(), flags=re.UNICODE)


def bm25(query, chunks):
    tokens = [words(c['text']) for c in chunks]
    if not tokens:
        return []
    counts = [Counter(t) for t in tokens]
    frequency = Counter(w for c in counts for w in c)
    average = mean(len(t) for t in tokens) or 1
    scores = []
    for chunk, ts, ct in zip(chunks, tokens, counts):
        score = 0.0
        for term in set(words(query)):
            n = frequency[term]
            idf = math.log(1 + (len(chunks) - n + 0.5) / (n + 0.5))
            tf = ct[term]
            if tf:
                score += idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * len(ts) / average))
        scores.append((score, chunk))
    return sorted(scores, key=lambda item: (-item[0], item[1]['id']))


def covered(retrieved_units, sufficient_sets):
    retrieved_units = set(retrieved_units)
    return any(set(s).issubset(retrieved_units) for s in sufficient_sets if s)


def recall(retrieved_units, reference_units):
    reference_units = set(reference_units)
    return len(set(retrieved_units) & reference_units) / len(reference_units) if reference_units else None


def quantile(values, p):
    values = sorted(values)
    index = (len(values) - 1) * p
    lower = int(index)
    upper = min(lower + 1, len(values) - 1)
    return values[lower] + (index - lower) * (values[upper] - values[lower])


def kappa(a, b):
    if not a or len(a) != len(b):
        raise ValueError('Pares de anotação ausentes ou incompletos')
    ca, cb = Counter(a), Counter(b)
    agreement = mean(x == y for x, y in zip(a, b))
    chance = sum(ca[v] * cb[v] for v in ca.keys() | cb.keys()) / len(a)**2
    return {'n': len(a), 'agreement': agreement,
            'kappa': (agreement - chance) / (1 - chance) if chance < 1 else None}


def agreement(annotations_path, out, annotators, set_attributes=()):
    """Compara dois anotadores antes da decisão conjunta. Listas usam JSON no CSV."""
    if len(set(annotators)) != 2:
        raise ValueError('Informe dois nomes diferentes de anotadores')
    with Path(annotations_path).open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    paired = defaultdict(dict)
    for row in rows:
        if row['annotator'] not in annotators:
            raise ValueError('Arquivo contém anotador fora do par declarado')
        key = (row['item_id'], row['attribute'])
        if row['annotator'] in paired[key] or not row['value'].strip():
            raise ValueError('Há anotação repetida ou valor vazio')
        value = row['value']
        if row['attribute'] in set_attributes:
            parsed = json.loads(value)
            if not isinstance(parsed, list) or any(not isinstance(v, str) for v in parsed):
                raise ValueError('Conjunto precisa ser uma lista de textos em JSON')
            value = tuple(sorted(set(parsed)))
        paired[key][row['annotator']] = value
    if not paired:
        raise ValueError('Nenhuma anotação disponível')
    groups = defaultdict(list)
    for (item, attribute), values in sorted(paired.items()):
        if set(values) != set(annotators):
            raise ValueError(f'Anotação incompleta: {item}, {attribute}')
        groups[attribute].append((values[annotators[0]], values[annotators[1]]))
    report = {}
    for attribute, values in groups.items():
        result = kappa([a for a,b in values], [b for a,b in values])
        if attribute in set_attributes:
            result['mean_jaccard'] = mean(len(set(a)&set(b))/len(set(a)|set(b))
                if set(a)|set(b) else 1.0 for a,b in values)
        result['annotators'] = annotators
        result['category_frequencies'] = {who: {str(k):n for k,n in Counter(v[i] for v in values).items()}
                                          for i,who in enumerate(annotators)}
        report[attribute] = result
    write(out, report)


def combine(directory, output):
    """Reúne somente uma execução completa de geração, sem repetir respostas."""
    root = Path(directory)
    if not (root / 'retrieval.jsonl').is_file():
        raise ValueError('A execução não terminou: falta retrieval.jsonl')
    paths = sorted(root.glob('*-runs.jsonl'))
    runs = [r for p in paths for r in records(p)]
    if not runs or len({r['run_id'] for r in runs}) != len(runs):
        raise ValueError('Não há respostas ou há respostas repetidas')
    expected = {(r['question_id'], r['config']) for r in records(root/'retrieval.jsonl')}
    actual = [(r['question_id'], r['config']) for r in runs if r['seed'] is None]
    if len(set(actual)) != len(actual) or set(actual) != expected:
        raise ValueError('Faltam respostas principais ou há pares repetidos')
    write_records(output, runs)


def paired_bootstrap(pairs, repetitions=5000, seed=2026):
    if not pairs:
        raise ValueError('Nenhum par elegível')
    banks = defaultdict(lambda: defaultdict(list))
    for bank, family, delta in pairs:
        banks[bank][family].append(delta)
    rng = random.Random(seed)
    samples = []
    for _ in range(repetitions):
        sample = []
        for bank in sorted(banks):
            families = sorted(banks[bank])
            for family in rng.choices(families, k=len(families)):
                sample.extend(banks[bank][family])
        samples.append(mean(sample))
    estimate = mean(p[2] for p in pairs)
    alpha = 0.05 / 3
    return {'pairs': len(pairs), 'families_by_bank': {b: len(v) for b, v in banks.items()},
            'estimate': estimate, 'point_estimate_at_least_10pp': estimate >= 0.10,
            'absolute_point_estimate_at_least_10pp': abs(estimate) >= 0.10,
            'ci95': [quantile(samples, .025), quantile(samples, .975)],
            'ci9833': [quantile(samples, alpha / 2), quantile(samples, 1 - alpha / 2)],
            'bootstrap_repetitions': repetitions, 'bootstrap_seed': seed,
            'interpretation': 'exploratoria; nenhum apoio confirmatorio automatico'}


def stability_sample(questions, fraction=.25):
    groups = defaultdict(list)
    for q in questions:
        groups[(q['bank'], q['class'])].append(q)
    selected = []
    for key in sorted(groups):
        group = sorted(groups[key], key=lambda q: (digest(q['id'] + 'estabilidade-2026'), q['id']))
        # Proposta de arredondamento, a aprovar e registrar antes do estudo.
        n = math.floor(len(group) * fraction + .5)
        selected.extend(q['id'] for q in group[:n])
    return selected


def blind(run_path, out, seed, judges=1):
    if judges not in (1, 2):
        raise ValueError('Escolha um ou dois julgadores reais')
    runs = records(run_path)
    if not runs:
        raise ValueError('Não há respostas para preparar os formulários')
    if len({r['run_id'] for r in runs}) != len(runs):
        raise ValueError('Execuções duplicadas')
    rng = random.Random(seed)
    rng.shuffle(runs)
    key, rows = [], []
    for i, r in enumerate(runs):
        uid = f'resposta-{i+1:06d}'
        key.append({'blind_id': uid, 'run_id': r['run_id'], 'question_id': r['question_id'],
                    'config': r['config'], 'seed': r['seed']})
        rows.append({'blind_id': uid, 'question': r['question'], 'answer': r['answer'],
                     'evidence': json.dumps(r['evidence'], ensure_ascii=False), 'adequacy': '',
                     'filtered_attributes': '', 'unfiltered_attributes': '', 'completeness': '',
                     'support': '', 'failures': '', 'notes': ''})
    root = Path(out)
    write_records(root / 'private_key.jsonl', key)
    for j in ('J1', 'J2')[:judges]:
        copied = list(rows)
        rng.shuffle(copied)
        write_csv(root / f'{j}.csv', copied, list(rows[0]) if rows else ['blind_id'])


def analyze(questions_path, judgments_path, out):
    questions = records(questions_path)
    validate_questions(questions)
    with Path(judgments_path).open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    values = {}
    question_ids = {q['id'] for q in questions}
    for row in rows:
        key = (row['question_id'], row['config'])
        if row['question_id'] not in question_ids:
            raise ValueError('Julgamento sem pergunta na amostra declarada')
        if key in values or row['adequacy'] not in ('0', '1') or row['config'] not in CONFIGS:
            raise ValueError('Julgamentos principais: um 0/1 por pergunta/configuração')
        values[key] = int(row['adequacy'])
    result = {}
    for name, left, right in [('H1', 'B', 'A'), ('H2', 'C', 'B'), ('H3', 'B', 'Bp')]:
        pairs = []
        for q in questions:
            eligible = bool(q['query_attributes']) if name == 'H2' else q['class'] in ('condicao', 'excecao')
            if not eligible:
                continue
            if (q['id'], left) not in values or (q['id'], right) not in values:
                raise ValueError(f'Par incompleto: {q["id"]} {name}; resolver sem descarte silencioso')
            pairs.append((q['bank'], q['family'], values[q['id'], left] - values[q['id'], right]))
        result[name] = paired_bootstrap(pairs) if pairs else {'status': 'sem perguntas elegiveis'}
    write(out, result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    p = subs.add_parser('check')
    p.add_argument('questions')
    p.add_argument('--pilot-families')
    p = subs.add_parser('blind')
    p.add_argument('runs'); p.add_argument('output'); p.add_argument('--seed', type=int, default=2026)
    p.add_argument('--judges', type=int, choices=(1, 2), default=1)
    p = subs.add_parser('analyze')
    p.add_argument('questions'); p.add_argument('judgments'); p.add_argument('output')
    p = subs.add_parser('combine', help='Reunir respostas de uma execução completa')
    p.add_argument('directory'); p.add_argument('output')
    p = subs.add_parser('agreement', help='Comparar dois anotadores antes da decisão conjunta')
    p.add_argument('annotations'); p.add_argument('output')
    p.add_argument('--annotators', nargs=2, required=True)
    p.add_argument('--set-attributes', nargs='*', default=[])
    p = subs.add_parser('budget')
    p.add_argument('--questions', type=int, default=120)
    p.add_argument('--judges', type=int, choices=(1, 2), default=1)
    a = parser.parse_args()
    if a.command == 'check':
        validate_questions(records(a.questions), load(a.pilot_families) if a.pilot_families else ())
        print('Estrutura das perguntas e exclusão das famílias: OK')
    elif a.command == 'blind':
        blind(a.runs, a.output, a.seed, a.judges)
    elif a.command == 'analyze':
        analyze(a.questions, a.judgments, a.output)
    elif a.command == 'combine':
        combine(a.directory, a.output)
    elif a.command == 'agreement':
        agreement(a.annotations, a.output, a.annotators, a.set_attributes)
    else:
        if a.questions <= 0:
            raise ValueError('Quantidade precisa ser positiva')
        n = a.questions
        z = NormalDist()
        power = (z.inv_cdf(1-.05/6)*math.sqrt(.25)+z.inv_cdf(.8)*math.sqrt(.25-.1**2))**2/.1**2
        print(json.dumps({'questions': n, 'judges': a.judges, 'main_judgments': n*6*a.judges,
              'main_hours_at_3min': n*6*a.judges*3/60, 'illustrative_stability_questions': n*.25,
              'illustrative_total_judgments': n*7.5*a.judges, 'illustrative_total_hours': n*7.5*a.judges*3/60,
              'independent_power_pairs': power, 'precision_pairs': math.ceil(z.inv_cdf(.975)**2*.25/.1**2),
              'warning': 'Estabilidade efetiva depende do arredondamento estratificado; famílias não são perguntas.'}, indent=2))


if __name__ == '__main__':
    main()
