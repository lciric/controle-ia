import json, collections
D = '/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v8/'
s = json.load(open(D + 'atteignabilite-echelle-v8.json', encoding='utf-8'))
d = s['detail']
cas = sorted({e['cas'].rsplit(' ; tau ', 1)[0] for e in d})
for c in cas: print('CAS', c)
def v8(e):
    lam = any(r.startswith('le λ du') for r in e['reserves']); ctx = any(r.startswith('jeux de force') for r in e['reserves'])
    return lam, ctx
print('--- positif vrais sous H_A avec signature d\'un seul jeu')
for e in d:
    if e['lecture'] == 'positif' and e['cas'].startswith(('H1', 'fuite masquée')):
        print(e['cas'], e['graine'], v8(e), [r[:40] for r in e['reserves']])
