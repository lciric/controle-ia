import json, collections, sys
D = '/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v9/contre-lecture-cl8/sorties/'
def lire(f): return [json.loads(l) for l in open(D + f, encoding='utf-8')]
PRON = ('positif', 'inverse', 'nul')
def fam(sc): return sc.split('_')[0]
print('== BDC')
bdc = lire('banc-cl8-BDC.jsonl')
print('analyses', len(bdc), 'codes non nuls', sum(1 for x in bdc if 'code' in x))
par = collections.Counter(); scen = collections.defaultdict(set)
for x in bdc:
    f = fam(x['scenario']); scen[f].add(x['scenario'])
    v8 = x.get('reserves_v8', []); autres = x.get('autres_reserves', [])
    lam = any(r.startswith('le λ du') for r in v8); ctx = any(r.startswith('jeux de force') for r in v8)
    par[(f, x['lecture'], 'λ' if lam else '-', 'ctx' if ctx else '-', 'autres' if autres else '-')] += 1
for f in sorted(scen): print(f, 'scénarios', len(scen[f]), 'analyses', sum(1 for x in bdc if fam(x['scenario']) == f))
for k, v in sorted(par.items()):
    if k[1] in PRON or k[1].startswith('fuite de signe inverse') or k[1] == 'pas de fuite': print(k, v)
print('D : lectures', collections.Counter(x['lecture'] for x in bdc if fam(x['scenario']) == 'D'))
print('C : lectures', collections.Counter(x['lecture'] for x in bdc if fam(x['scenario']) == 'C'))
sans = [x for x in bdc if x['lecture'] in ('positif','inverse') and not x.get('reserves_v8') and not x.get('autres_reserves')]
for x in sans: print('SANS RESERVE', x['scenario'], x['graine'], x['lecture'], x['e'], x['e_ic'], x['q'], x['dl_ab'], x['dl_ba'])
print('== Z et Z2 (famille D sous composante : ZD_ca4_k1.4_s ; variante s2 ; miroir pos)')
z = lire('banc-cl8-Z.jsonl') + lire('banc-cl8-Z2.jsonl')
print('analyses', len(z), 'codes non nuls', sum(1 for x in z if 'code' in x))
for sc in sorted({x['scenario'] for x in z}):
    xs = [x for x in z if x['scenario'] == sc]
    c = collections.Counter()
    for x in xs:
        v8 = x.get('reserves_v8', []); lam = any(r.startswith('le λ du') for r in v8); ctx = any(r.startswith('jeux de force') for r in v8)
        tag = x['lecture'] + (' [' + '+'.join([t for t, b in (('λ', lam), ('ctx', ctx)) if b] or ['aucune v8']) + ']' if x['lecture'] in PRON else '')
        if x['lecture'] in PRON and x.get('autres_reserves'): tag += ' +autres:' + '|'.join(x['autres_reserves'])
        c[tag] += 1
    qs = [v for x in xs for v in x['q'].values() if v is not None]
    print(sc, len(xs), dict(c), 'q min-max', min(qs), max(qs))
    for x in xs:
        if x['lecture'] in ('positif','inverse') and not x.get('reserves_v8') and not x.get('autres_reserves'):
            print('   SANS RESERVE', x['graine'], x['e'], x['e_ic'], x['q'], 'transfert', x.get('transfert_ab'), x.get('transfert_ba'))
print('== Z-n2000')
for x in lire('banc-cl8-Z-n2000.jsonl'):
    print(x['scenario'], x['graine'], x['n_boot'], x['lecture'], 'réserves', x['reserves'])
    print('  e', {k: round(v, 3) for k, v in x['e'].items()}, {k: [round(a, 3) for a in v] for k, v in x['e_ic'].items()})
    print('  q', {k: round(v, 3) for k, v in x['q'].items()}, {k: [round(a, 3) for a in v] for k, v in x['q_ic'].items()})
    print('  λ', x['lambda'], 'Δλ', x['dl'], 'spec', x['spec'])
