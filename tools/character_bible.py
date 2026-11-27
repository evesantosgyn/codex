#!/usr/bin/env python3
"""Character Bible canônica (HPS 1.0) — validar, gerar leitura e pranchas, conferir cards.

Uso (a partir da raiz do repositório):
  python3 tools/character_bible.py validate  <bible.json>
  python3 tools/character_bible.py render-md <bible.json> <saida.md>
  python3 tools/character_bible.py sheets    <bible.json> <saida.md> [P3 P4 ...]
  python3 tools/character_bible.py approve-sheet <bible.json> <P#> <imagem.png>
  python3 tools/character_bible.py check-cards <pasta_shots> <bible.json> [<bible.json> ...]

O JSON é a fonte canônica; o Markdown e os pacotes de prancha são gerados a partir dele.
"""
import hashlib, json, os, sys
import jsonschema

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = os.path.join(ROOT, 'templates', 'character-bible.schema.json')


def load(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def series_root(bible_path):
    # .../SERIES_xxx/02_CHARACTERS/<NOME>/<arquivo>.json -> .../SERIES_xxx
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(bible_path))))


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def validate(path):
    d = load(path)
    jsonschema.validate(d, load(SCHEMA))
    errs = []
    ids = [e['id'] for e in d['expressions']]
    if len(ids) != len(set(ids)):
        errs.append('IDs de expressão repetidos')
    sr = series_root(path)
    for k, r in d['references'].items():
        f = os.path.join(sr, r['path'])
        if not os.path.exists(f):
            errs.append(f'referência {k} não existe: {r["path"]}')
        elif sha(f) != r['sha256']:
            errs.append(f'referência {k} mudou (SHA-256 diferente): {r["path"]}')
    sheet_ids = {s['id'] for s in d['sheets']}
    for e in d['expressions']:
        if e['sheet'] not in sheet_ids:
            errs.append(f'{e["id"]} aponta para prancha inexistente {e["sheet"]}')
    for s in d['sheets']:
        for pid in s['panels']:
            if pid not in ids:
                errs.append(f'prancha {s["id"]} cita {pid}, que não existe')
    if errs:
        raise SystemExit('ERROS:\n- ' + '\n- '.join(errs))
    print(f'OK: {d["character_id"]} {d["version"]} · {len(ids)} expressões · {len(d["sheets"])} pranchas')
    return d


def identity_block(d):
    im = d['identity_lock']['immutable']
    parts = [f'{k.replace("_", " ")}: {v}' for k, v in im.items() if k != 'hair_seven_years_ago']
    return '; '.join(parts)


def render_md(path, out):
    d = validate(path)
    g = {x['id']: x['name'] for x in d.get('expression_groups', [])}
    L = [f'# {d["name"]} — Catálogo de expressões da Temporada 1 · {d["version"]}', '',
         f'> **Gerado automaticamente** de `{os.path.basename(path)}` (fonte canônica, HPS). Não edite este arquivo: edite o JSON e rode `tools/character_bible.py render-md`.',
         f'> **Status:** {d["status"]} · atualizado em {d.get("updated", "")}', '',
         f'**Regra-mãe:** {d["interpretation_rule"]}', '']
    cur = None
    for e in d['expressions']:
        if e['group'] != cur:
            cur = e['group']
            L += ['', f'### {cur}. {g.get(cur, "")}', '| ID | Expressão | Onde na T1 | Direção (inglês) | Prancha | Referência |', '|---|---|---|---|---|---|']
        ref = f'`{e["reference_image"]["path"]}` painel {e["reference_image"]["panel"]}' if e['reference_image'] else '—'
        L.append(f'| {e["id"]} | **{e["name"]}** | {e["where"]} | *{e["direction"]}* | {e["sheet"]}·{e["panel"]} | {ref} |')
    L += ['', '## Proibidos', '- ' + '\n- '.join(d['forbidden']), '', '## Pranchas', '| Prancha | Painéis | Arquivo | Status |', '|---|---|---|---|']
    for s in d['sheets']:
        L.append(f'| {s["id"]} — {s["name"]} | {", ".join(s["panels"])} | `{s["approved_file"]}` | {s["status"]} |')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')
    print('escrito', out)


def sheets(path, out, only):
    d = validate(path)
    ex = {e['id']: e for e in d['expressions']}
    refs = d['references']
    L = [f'# Pacote ChatGPT — {d["name"]} · pranchas {", ".join(only) if only else "todas"} · {d["version"]}', '',
         f'> **Gerado** de `{os.path.basename(path)}`. Um **chat novo, só com {d["name"].split()[0]}**. Para cada prancha: anexe R1–R3 e cole o bloco da prancha (abaixo da linha dela).', '',
         '| Anexo | Arquivo |', '|---|---|',
         *[f'| R{i} | `{refs[k]["path"]}` |' for i, k in enumerate(d.get('sheet_refs', ['identity_pack', 'look_L7', 'level1_ref']), 1)], '']
    for s in d['sheets']:
        if only and s['id'] not in only:
            continue
        if not only and s['status'] == 'approved':
            continue
        if s.get('custom_prompt'):
            L += ['---', '', f'## {s["id"]} — {s["name"]}', f'**Salvar o aprovado como:** `{s["approved_file"]}`', '', '```', s['custom_prompt'], '```', '']
            continue
        n = len(s['panels'])
        grid = '3×2' if n == 6 else ('2×2' if n == 4 else f'1×{n}')
        L += ['---', '', f'## {s["id"]} — {s["name"]}', f'**Salvar o aprovado como:** `{s["approved_file"]}`', '', '```',
              f'Create a character expression sheet of the SAME woman as R1 ({d["name"]}), 16:9, photorealistic, cinematic, natural skin texture, {n} close-ups in a {grid} grid on a dark neutral background, each with a small caption underneath. Same face in every panel; only the expression changes.',
              '', f'Identity (every panel): {identity_block(d)}. Wardrobe as R2.', '', f'Who she is: {d["interpretation_rule"]}', '']
        for i, pid in enumerate(s['panels'], 1):
            e = ex[pid]
            extra = f' [AGE VARIANT: {e["age_variant"]}]' if e.get('age_variant') else ''
            L.append(f'{i}. {pid} — {e["direction"]}{extra}')
        if d.get('generation_suffix'):
            L += ['', d['generation_suffix']]
        L += ['', 'Captions: ' + ' · '.join(s['panels']) + '. No other text.', '```', '']
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')
    print('escrito', out)


def approve_sheet(path, sid, img):
    d = load(path)
    sr = series_root(path)
    s = next(x for x in d['sheets'] if x['id'] == sid)
    rel = os.path.relpath(os.path.abspath(img), sr)
    h = sha(img)
    s['status'] = 'approved'; s['approved_file'] = rel; s['sha256'] = h
    for i, pid in enumerate(s['panels'], 1):
        for e in d['expressions']:
            if e['id'] == pid:
                e['status'] = 'approved'; e['reference_image'] = {'path': rel, 'sha256': h, 'panel': i}
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print(f'{sid} aprovada: {rel} ({h[:12]}…)')


def check_cards(folder, bibles):
    known = {}
    for b in bibles:
        d = load(b)
        known[d['character_id']] = ({e['id'] for e in d['expressions']}, set(d['looks']))
    bad = 0; n = 0
    for fn in sorted(os.listdir(folder)):
        if not fn.endswith('.json'):
            continue
        c = load(os.path.join(folder, fn)); n += 1
        for ch in c['direction'].get('characters', []):
            cid = ch['character_id']
            if cid not in known:
                continue
            exps, looks = known[cid]
            for x in ch.get('expression_ids', []):
                if x not in exps:
                    print(f'{fn}: {cid} cita {x}, que não existe'); bad += 1
            if ch.get('look_id') and ch['look_id'] not in looks:
                print(f'{fn}: {cid} cita look {ch["look_id"]}, que não existe'); bad += 1
    print(f'{n} cards conferidos, {bad} problemas')
    if bad:
        raise SystemExit(1)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    cmd = a[0]
    if cmd == 'validate':
        validate(a[1])
    elif cmd == 'render-md':
        render_md(a[1], a[2])
    elif cmd == 'sheets':
        sheets(a[1], a[2], a[3:])
    elif cmd == 'approve-sheet':
        approve_sheet(a[1], a[2], a[3])
    elif cmd == 'check-cards':
        check_cards(a[1], a[2:])
    else:
        raise SystemExit(__doc__)
