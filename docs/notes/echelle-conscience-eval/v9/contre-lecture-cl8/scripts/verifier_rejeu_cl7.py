import json, collections, hashlib
D = '/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v8/'
def lire(f): return [json.loads(l) for l in open(D + f, encoding='utf-8') if l.strip()]
rp = lire('rejeu-banc-cl7/rejeu-banc-cl7-v8-principal.jsonl'); rn = lire('rejeu-banc-cl7/rejeu-banc-cl7-v8-n2000.jsonl')
bp = lire('contre-lecture-cl7/banc/banc-cl7-principal.jsonl'); bn = lire('contre-lecture-cl7/banc/banc-cl7-n2000.jsonl')
print('entêtes', rp[0]['entete']['bancs'], rn[0]['entete']['bancs'])
for f in ('contre-lecture-cl7/banc/banc-cl7-principal.jsonl', 'contre-lecture-cl7/banc/banc-cl7-n2000.jsonl', 'contre-lecture-cl7/scripts/banc_cl7.py'):
    print(f, hashlib.sha256(open(D + f, 'rb').read()).hexdigest()[:16])
rp, rn = rp[1:], rn[1:]
print('analyses', len(rp), len(rn), '; banc', len(bp), len(bn))
# appariement avec le banc : mêmes (scénario, graine), même lecture v7
cle = lambda x: (x['scenario'], x['graine'], x.get('n_boot', 300))
B = {cle(x): x for x in bp + bn}
manque = [cle(x) for x in rp + rn if cle(x) not in B]
print('lignes du rejeu absentes du banc :', manque)
diff_v7 = [cle(x) for x in rp + rn if x['lecture_v7'] != B[cle(x)]['lecture']]
print('lecture_v7 du rejeu ≠ lecture du banc :', diff_v7)
print('écart max λ ic :', max(x['ecart_max_lambda_ic_au_banc'] for x in rp + rn))
ch = collections.Counter((x['lecture_v7'], x['lecture']) for x in rp + rn if x['lecture_v7'] != x['lecture'])
print('changements', ch)
# e(m) du rejeu contre e(m) du banc
de = max(abs(x['ecart_sens'][m] - B[cle(x)]['ecart_sens'][m]) for x in rp + rn for m in ('petit', 'grand'))
print('écart max e(m) rejeu − banc :', de)
# lectures fausses
def vrai(nom):
    if nom.startswith(('B_H0', 'A_H0', 'D_H0', 'E_H0', 'd256_H0')): return 'H0'
    if nom.startswith(('C_HA', 'd256_HA')): return 'HA'
    return '?'
faux = [x for x in rp + rn if (vrai(x['scenario']) == 'H0' and x['lecture'] in ('positif', 'inverse')) or (vrai(x['scenario']) == 'HA' and x['lecture'] == 'nul')]
L = lambda x: any(r.startswith('le λ du') for r in x['reserves']); C = lambda x: any(r.startswith('jeux de force') for r in x['reserves'])
print('lectures fausses', len(faux), 'λ', sum(map(L, faux)), 'ctx', sum(map(C, faux)), 'aucune', sum(1 for x in faux if not (L(x) or C(x))))
fp = [x for x in faux if x.get('n_boot', 300) == 300]
print('dont banc principal', len(fp), collections.Counter(x['lecture'] for x in fp), 'λ', sum(map(L, fp)), 'ctx', sum(map(C, fp)))
autres = [x for x in rp if x['lecture'] in ('positif', 'inverse', 'nul') and x not in faux]
print('autres prononcées', len(autres), [(x['scenario'], x['graine'], x['lecture'], L(x), C(x)) for x in autres if L(x) or C(x)])
print('témoins à contextes égaux prononcés :', [(x['scenario'], x['lecture'], L(x), C(x)) for x in autres if 'k0' not in x['scenario'] and 'k1' not in x['scenario']])
