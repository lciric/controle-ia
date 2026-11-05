import json, re, collections
D = '/home/user/controle-ia-travail/'
sim = json.load(open(D + 'docs/notes/echelle-conscience-eval/v8/atteignabilite-echelle-v8.json', encoding='utf-8'))
texte = open(D + 'prereg/brouillon-test-echelle-conscience-eval-v9.md', encoding='utf-8').read()
V8 = ("le λ du ", "jeux de force de contexte inégale")
# mes cases
noms, cases = [], collections.defaultdict(dict)
for e in sim['detail']:
    nom, tau = e['cas'].rsplit(' ; tau ', 1)
    if nom not in noms: noms.append(nom)
    c = cases[nom].setdefault(tau, {})
    base = re.sub(r" \(\d+ réserve\(s\)\)$", "", e['lecture'])
    n, a, a8 = c.get(base, (0, 0, 0))
    c[base] = (n + 1, a + bool(e['reserves']), a8 + any(r.startswith(V8) for r in e['reserves']))
print(len(noms), 'cas ;', len(sim['detail']), 'analyses')
# tableau du texte
sec = texte.split('| vérité (α au 8B et au 70B) | tau 0,15 | tau 0,4 | tau 0,8 |')[1].split('\n\n')[0]
lignes = [l for l in sec.strip().split('\n')[1:] if l.startswith('|')]
print(len(lignes), 'lignes au tableau du texte')
def parse(cell):
    cell = cell.strip()
    if cell == '—': return {}
    out = {}
    for m in re.finditer(r"(.+?) (\d+)(?: \((\d+)(?: ; v8 (\d+))?\))?(?:, |$)", cell):
        out[m.group(1)] = (int(m.group(2)), int(m.group(3) or 0), int(m.group(4) or 0))
    return out
ecarts = 0
for nom, l in zip(noms, lignes):
    cells = [x for x in l.strip().strip('|').split('|')]
    for tau, cell in zip(('0.15', '0.4', '0.8'), cells[1:]):
        t = parse(cell); m = cases[nom].get(tau, {})
        if t != m:
            ecarts += 1; print('ECART', nom, tau, t, m)
print('écarts de cases :', ecarts)
# totaux
tot = collections.Counter()
for e in sim['detail']:
    tot[re.sub(r" \(\d+ réserve\(s\)\)$", "", e['lecture'])] += 1
print(sum(tot.values()))
