import json, collections, numpy as np
D = '/home/user/controle-ia-travail/'
sim = json.load(open(D + 'docs/notes/echelle-conscience-eval/v8/atteignabilite-echelle-v8.json', encoding='utf-8'))
g = collections.defaultdict(list); q = collections.defaultdict(list)
for e in sim['detail']:
    if 'ecart_sens_ic' not in e: continue
    dim = '256' if 'd 256' in e['cas'] else '64'
    tau = e['cas'].rsplit(' ; tau ', 1)[1]
    for m in ('petit', 'grand'):
        b, h = e['ecart_sens_ic'][m]; g[(dim, tau)].append((h - b) / 2)
        n = e['cas']
        if 'contexte' not in n and 'force' not in n and 'faible' not in n and e['rapport_Ec'][m] is not None:
            q[(dim, tau)].append(np.log(e['rapport_Ec'][m]))
for k in sorted(g):
    v = np.array(g[k]); w = np.array(q[k])
    print(k, 'demi-largeur e(m) : médiane %.3f, 10e %.3f, 90e %.3f, n %d' % (np.median(v), np.percentile(v, 10), np.percentile(v, 90), len(v)),
          '| log q (contextes égaux) : écart type %.3f, |log q|>log 1,15 : %d/%d' % (w.std(), (abs(w) > np.log(1.15)).sum(), len(w)))
