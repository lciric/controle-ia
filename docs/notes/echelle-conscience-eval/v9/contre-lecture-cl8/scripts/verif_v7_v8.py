import json, re, collections
D = '/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/'
s7 = json.load(open(D + 'v7/atteignabilite-echelle-v7.json', encoding='utf-8'))['detail']
s8 = json.load(open(D + 'v8/atteignabilite-echelle-v8.json', encoding='utf-8'))['detail']
base = lambda e: re.sub(r" \(\d+ réserve\(s\)\)$", "", e['lecture'])
print(len(s7), len(s8))
d7 = {(e['cas'], e['graine']): e for e in s7}
communs = [(e, d7[(e['cas'], e['graine'])]) for e in s8 if (e['cas'], e['graine']) in d7]
print('communes', len(communs))
ch = collections.Counter((base(b), base(a)) for a, b in communs if base(a) != base(b))
print('changements de lecture', ch)
# intervalles identiques ?
diffe = max(abs(a['ecart_sens'][m] - b['ecart_sens'][m]) for a, b in communs for m in ('petit', 'grand'))
print('écart max e(m) v8 − v7', diffe)
# réserves v7 conservées ?
perdues = sum(1 for a, b in communs if not set(b['reserves']) <= set(a['reserves']))
print('réserves v7 non conservées en v8', perdues)
ajout = collections.Counter()
for a, b in communs:
    n = len([r for r in a['reserves'] if r.startswith(('le λ du', 'jeux de force'))])
    if n: ajout[base(a)] += 1
print('lectures communes avec réserve v8 ajoutée', ajout, sum(ajout.values()))
