import hashlib, re, os
D = '/home/user/controle-ia-travail/'
texte = open(D + 'prereg/brouillon-test-echelle-conscience-eval-v9.md', encoding='utf-8').read()
corps = texte.split('## Traces')[0]
sec = texte.split('## Traces')[1]
tab = dict(re.findall(r"\| `([^`]+)` \| `([0-9a-f]{64})` \|", sec))
for m in re.finditer(r"`([0-9a-f]{8})…`", corps):
    a = m.group(1)
    avant = corps[:m.start()]
    chemins = re.findall(r"`([^`\s]+\.(?:md|txt|json|jsonl|py))`", avant)
    c = chemins[-1] if chemins else None
    # chemin complet
    cand = [k for k in tab if c and (k == c or k.endswith('/' + c))]
    if c and c.startswith('docs/sources'):
        p = D + c
        hf = hashlib.sha256(open(p,'rb').read()).hexdigest()
        comp = open(p + '.sha256').read().split()[0]
        print(a, c, 'OK' if hf.startswith(a) and comp == hf else 'ECART')
        continue
    if len(cand) == 1:
        print(a, cand[0], 'OK' if tab[cand[0]].startswith(a) else 'ECART ' + tab[cand[0]][:8])
    else:
        print(a, c, 'ambigu', cand)
