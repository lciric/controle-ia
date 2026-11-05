import json, sys, collections
xs = [json.loads(l) for l in open(sys.argv[1], encoding='utf-8')]
print('analyses', len(xs), 'arrêts', sum(1 for x in xs if 'code' in x))
for sc in dict.fromkeys(x['scenario'] for x in xs):
    ys = [x for x in xs if x['scenario'] == sc]
    c = collections.Counter()
    for x in ys:
        lam = any(r.startswith('le λ du') for r in x['reserves']); ctx = any(r.startswith('jeux de force') for r in x['reserves'])
        autres = [r for r in x['reserves'] if not r.startswith(('le λ du', 'jeux de force'))]
        tag = x['lecture']
        if x['lecture'] in ('positif', 'inverse', 'nul'):
            tag += ' [' + ('+'.join([n for n, b in (('λ', lam), ('ctx', ctx), ('autres', bool(autres))) if b]) or 'aucune réserve') + ']'
        c[tag] += 1
    qs = [v for x in ys for v in x['q'].values() if v is not None]
    print(f'{sc} ({len(ys)}) : {dict(c)} ; q de {min(qs):.3f} à {max(qs):.3f}')
    for x in ys:
        if x['lecture'] in ('positif', 'inverse') and not x['reserves']:
            print('   SANS AUCUNE RÉSERVE', x['graine'], x['lecture'], 'e', x['e'], x['e_ic'], 'q', x['q'], 'Δλ', x['dl_ic'], 'λ', x['lambda'], 'spéc', x['spec_ic'], 'cert', x['cert'])
