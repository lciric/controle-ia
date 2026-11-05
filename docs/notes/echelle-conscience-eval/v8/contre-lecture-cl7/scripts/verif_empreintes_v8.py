"""Vérifie les empreintes du brouillon v8 : outils (fichier, compagnon, objet du commit), traces (fichier, compagnon), abrégées."""
import hashlib, re, subprocess, sys, os
DEPOT = "/home/user/controle-ia-travail"
WT = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1"
COMMIT = "b54da1fe41e26360cb5410bfd2fdc0614537de1d"
texte = open(os.path.join(DEPOT, "prereg/brouillon-test-echelle-conscience-eval-v8.md"), encoding="utf-8").read()
def h(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
ok = ko = 0
# outils
for m in re.finditer(r"\| `(echelle-v7/[^`]+)` \| `([0-9a-f]{64})` \|", texte):
    chemin, attendu = m.group(1), m.group(2)
    p = os.path.join(WT, chemin)
    f = h(p)
    comp = open(p + ".sha256").read().split()[0] if os.path.exists(p + ".sha256") else None
    obj = subprocess.run(["git", "-C", WT, "show", f"{COMMIT}:{chemin}"], capture_output=True, env=env).stdout
    o = hashlib.sha256(obj).hexdigest()
    bon = (f == attendu == comp == o)
    ok += bon; ko += (not bon)
    print("OUTIL", "OK " if bon else "KO ", chemin, f[:12], (comp or "-")[:12], o[:12])
# traces
for m in re.finditer(r"\| `((?:docs|prereg)/[^`]+)` \| `([0-9a-f]{64})` \|", texte):
    chemin, attendu = m.group(1), m.group(2)
    p = os.path.join(DEPOT, chemin)
    f = h(p)
    compp = p + ".sha256"
    comp = open(compp).read().split()[0] if os.path.exists(compp) else None
    bon = (f == attendu) and (comp is None or comp == f)
    ok += bon; ko += (not bon)
    print("TRACE", "OK " if bon else "KO ", chemin, f[:12], (comp or "SANS-COMPAGNON")[:14])
# abrégées dans le corps : `xxxxxxxx…`
abr = re.findall(r"`([^`]+)`[^`]{0,6}`([0-9a-f]{8})…`", texte)
print("abrégées (chemin, préfixe) trouvées:", len(abr))
for chemin, pre in abr:
    p = None
    for base in (DEPOT,):
        q = os.path.join(base, chemin)
        if os.path.isfile(q): p = q
    if p is None:
        print("ABR ?", chemin, pre); continue
    f = h(p)
    bon = f.startswith(pre)
    ok += bon; ko += (not bon)
    print("ABR", "OK " if bon else "KO ", chemin, pre, f[:8])
print("TOTAL ok", ok, "ko", ko)
