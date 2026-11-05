import hashlib, re, subprocess, sys, os
texte = open('/home/user/controle-ia-travail/prereg/brouillon-test-echelle-conscience-eval-v9.md', encoding='utf-8').read()
wt = '/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1'
env = dict(os.environ, GIT_OPTIONAL_LOCKS='0')
lignes = re.findall(r"\| `(echelle-v8/[^`]+)` \| `([0-9a-f]{64})` \|", texte)
print(len(lignes), 'outils au tableau')
ok = 0
for chemin, h in lignes:
    p = os.path.join(wt, chemin)
    hf = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    comp = open(p + '.sha256').read().split()[0]
    blob = subprocess.run(['git', '-C', wt, 'show', '9ccc383c02a08e58928368b23471f4c438e06cda:' + chemin], capture_output=True, env=env).stdout
    hc = hashlib.sha256(blob).hexdigest()
    bon = (h == hf == comp == hc)
    ok += bon
    if not bon:
        print('ECART', chemin, h[:12], hf[:12], comp[:12], hc[:12])
print('conformes', ok, '/', len(lignes))
# fichiers de echelle-v8 non cités
cites = {c for c, _ in lignes}
for racine, ds, fs in os.walk(os.path.join(wt, 'echelle-v8')):
    for f in fs:
        if f.endswith('.sha256'): continue
        rel = os.path.relpath(os.path.join(racine, f), wt)
        if rel not in cites: print('non cité', rel)
