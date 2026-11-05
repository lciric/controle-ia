import hashlib, re, os
D = '/home/user/controle-ia-travail/'
texte = open(D + 'prereg/brouillon-test-echelle-conscience-eval-v9.md', encoding='utf-8').read()
INTERDIT = ('donnees/', 'runs/', 'diag/', 'traces/', 'P3-consignes', 'textes-actions', 'items-textes-p1', 'prompts-p1')
def h(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
sec = texte.split('## Traces')[1].split('## Contre-lecture')[0]
lignes = re.findall(r"\| `([^`]+)` \| `([0-9a-f]{64})` \|", sec)
print(len(lignes), 'traces')
ok = 0; complet = {}
for c, e in lignes:
    assert not any(x in c for x in INTERDIT), c
    p = D + c
    hf = h(p)
    comp = open(p + '.sha256').read().split()[0] if os.path.exists(p + '.sha256') else None
    complet[c] = hf
    if hf == e and (comp is None or comp == e): ok += 1
    else: print('ECART', c, e[:12], hf[:12], comp and comp[:12])
    if comp is None: print('sans compagnon', c)
print('traces conformes', ok)
# empreintes abrégées du corps
corps = texte.split('## Traces')[0]
abr = re.findall(r"`([0-9a-f]{8})…`", corps)
print(len(abr), 'empreintes abrégées')
connues = {e[:8]: c for c, e in complet.items()}
# ajouter outils
manque = []
for a in sorted(set(abr)):
    if a in connues: continue
    manque.append(a)
print('abrégées non couvertes par le tableau Traces :', manque)
for a in manque:
    i = corps.find(a)
    print(a, '...', corps[max(0, i-200):i+10].replace('\n', ' ')[-220:])
