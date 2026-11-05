import sys, re, hashlib, os
DEPOT = '/home/user/controle-ia-travail'
ARBRE = '/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1'
INTERDITS = ['P3-consignes-v1.md', 'textes-actions-', 'items-textes-p1-v1.json', 'prompts-p1-v1.json']
def interdit(p):
    if any(x in p for x in INTERDITS): return True
    parts = p.split('/')
    return any(x in ('donnees','runs','diag','traces') for x in parts)
def h(p):
    return hashlib.sha256(open(p,'rb').read()).hexdigest()
texte = open(sys.argv[1], encoding='utf-8').read()
lignes = texte.splitlines()
# Tableau des traces et des outils : lignes "| `chemin` | `sha` |"
ok = ko = 0
for i, l in enumerate(lignes, 1):
    m = re.match(r'\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|', l)
    if not m: continue
    chemin, attendu = m.groups()
    if interdit(chemin):
        print('INTERDIT, non lu', chemin); continue
    if chemin.startswith('echelle-v8/'):
        p = os.path.join(ARBRE, chemin)
    else:
        p = os.path.join(DEPOT, chemin)
    if not os.path.exists(p):
        print(f'l.{i} ABSENT {chemin}'); ko += 1; continue
    reel = h(p)
    comp = p + '.sha256'
    compv = open(comp).read().split()[0] if os.path.exists(comp) else None
    etat = 'OK' if reel == attendu else 'DIFFERENT'
    cetat = 'compagnon OK' if compv == attendu else ('compagnon ABSENT' if compv is None else 'compagnon DIFFERENT')
    if reel == attendu and compv == attendu: ok += 1
    else:
        ko += 1
    print(f'l.{i} {etat} {cetat} {chemin}')
print('complets', ok, 'defauts', ko)
