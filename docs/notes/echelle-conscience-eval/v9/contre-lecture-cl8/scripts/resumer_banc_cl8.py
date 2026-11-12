import json, sys, collections
lignes = [json.loads(l) for f in sys.argv[1:] for l in open(f, encoding='utf-8') if l.strip()]
par = collections.defaultdict(list)
for x in lignes: par[x['scenario']].append(x)
for nom, xs in par.items():
    c = collections.Counter()
    for x in xs:
        if 'code' in x: c['arrêt'] += 1; continue
        l = x['lecture']
        if l in ('positif', 'inverse', 'nul', 'pas de fuite') or l.startswith('fuite de signe inverse (') and 'non confirmé' not in l:
            lam = any(r.startswith('le λ du') for r in x['reserves_v8']); ctx = any(r.startswith('jeux') for r in x['reserves_v8'])
            l += ' [' + ('λ' if lam else '') + ('+' if lam and ctx else '') + ('ctx' if ctx else '') + ('aucune' if not (lam or ctx) else '') + ']'
        c[l] += 1
    q = [x['q'] for x in xs if 'q' in x]
    qs = ' '.join(f"{a['petit']:.2f}/{a['grand']:.2f}" for a in q)
    tr = [x.get('transfert_ab') for x in xs if 'q' in x]
    print(f"{nom:34s} {dict(c)}  q: {qs}  transfert a→b (p,g) ex.: {tr[0] if tr else ''}")
