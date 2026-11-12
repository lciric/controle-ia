import re, hashlib, os, sys
DEPOT = '/home/user/controle-ia-travail'
texte = open(sys.argv[1], encoding='utf-8').read()
INTERDITS = ['P3-consignes-v1.md', 'textes-actions-', 'items-textes-p1-v1.json', 'prompts-p1-v1.json']
def interdit(p): return any(x in p for x in INTERDITS) or any(x in ('donnees','runs','diag','traces') for x in p.split('/'))
# chaque `abrégé…` : chemin = dernier `...` qui ressemble à un chemin avant lui (sur la même ligne)
n = ok = 0
for ln, ligne in enumerate(texte.splitlines(), 1):
    for m in re.finditer(r'`([0-9a-f]{8,16})…`', ligne):
        av = ligne[:m.start()]
        chemins = re.findall(r'`([^`]+\.(?:md|txt|json|jsonl|py|sh))`', av)
        n += 1
        if not chemins:
            print(f'l.{ln} {m.group(1)} : pas de chemin avant (contexte : {av[-90:]!r})'); continue
        c = chemins[-1]
        cands = [c] if c.startswith(('docs/', 'prereg/', 'src/', 'registres/')) else []
        if not cands:
            # nom court : chercher dans les dossiers cités plus haut sur la ligne
            dossiers = re.findall(r'`(docs/[^`]+/)`', av)
            cands = [d + c for d in dossiers] + [os.path.join(os.path.dirname(x), c) for x in re.findall(r'`(docs/[^`]+\.(?:txt|json|jsonl|py))`', av)]
        trouve = False
        for cc in cands:
            p = os.path.join(DEPOT, cc)
            if interdit(cc) or not os.path.isfile(p): continue
            h = hashlib.sha256(open(p,'rb').read()).hexdigest()
            if h.startswith(m.group(1)):
                ok += 1; trouve = True; break
            else:
                print(f'l.{ln} DIFFERENT {cc} {m.group(1)} ≠ {h[:16]}'); trouve = True; break
        if not trouve:
            print(f'l.{ln} {m.group(1)} : chemin non résolu ({c})')
print('abrégées', n, 'conformes', ok)
