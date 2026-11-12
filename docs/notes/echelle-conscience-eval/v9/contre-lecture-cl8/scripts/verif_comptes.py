import json, re, collections
D = '/home/user/controle-ia-travail/'
sim = json.load(open(D + 'docs/notes/echelle-conscience-eval/v8/atteignabilite-echelle-v8.json', encoding='utf-8'))
V8L, V8C = "le λ du ", "jeux de force de contexte inégale"
def base(e): return re.sub(r" \(\d+ réserve\(s\)\)$", "", e['lecture'])
propres = lambda n: ('signature' not in n and 'jeu a' not in n and 'jeu b' not in n and 'contexte' not in n and 'masqu' not in n)
print('--- vérités sans signature, contextes égaux : cas retenus')
cas = sorted({e['cas'].rsplit(' ; tau ',1)[0] for e in sim['detail'] if propres(e['cas'])})
print(cas)
c = collections.Counter()
for e in sim['detail']:
    if not propres(e['cas']): continue
    b = base(e)
    if b in ('positif', 'inverse', 'nul'):
        c[b] += 1
        r8 = [r for r in e['reserves'] if r.startswith((V8L, V8C))]
        if r8:
            print(b, e['cas'], e['graine'], [r[:60] for r in r8], {k: round(v,3) for k,v in e['rapport_Ec'].items()}, {k:[round(x,3) for x in v] for k,v in e['ecart_sens_ic'].items()})
print(c)
print('--- doubles signatures')
for e in sim['detail']:
    if 'deux jeux' in e['cas'] and 'H1' not in e['cas'] and base(e) in ('positif','inverse'):
        print(base(e), e['cas'], e['graine'], [r[:40] for r in e['reserves']])
print('--- prix cohérence sous H_0 à contextes inégaux')
for e in sim['detail']:
    n = e['cas']
    if n.startswith('H0') and 'contexte' in n and 'jeu a' not in n and 'jeu b +' not in n and 'jeu b −' not in n:
        pass
print('--- tous les positif/inverse/nul sans réserve v8 sous H_0 ou artefacts (vérité α non H_A)')
