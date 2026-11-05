"""Vérifie les empreintes du tableau d'outils et du tableau des traces du brouillon v5.
Lecture seule : fichiers, compagnons .sha256, objets git du commit (git cat-file, sans écriture)."""
import hashlib, os, re, subprocess, sys
WT = "/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1"
DEPOT = "/home/user/controle-ia-travail"
TEXTE = os.path.join(DEPOT, "prereg/brouillon-test-echelle-conscience-eval-v5.md")
COMMIT = "f579930842ab633cdced18a13f82d77bb467ca7f"
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
def h(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
def compagnon(p):
    c = p + ".sha256"
    if not os.path.exists(c):
        return None
    return open(c).read().split()[0]
def objet(chemin):
    r = subprocess.run(["git", "-C", WT, "show", f"{COMMIT}:{chemin}"], capture_output=True, env=env)
    if r.returncode != 0:
        return None
    return hashlib.sha256(r.stdout).hexdigest()
txt = open(TEXTE, encoding="utf-8").read()
lignes = re.findall(r"\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", txt)
ok = 0; ko = 0
for chemin, attendu in lignes:
    if chemin.startswith("echelle-v4/"):
        p = os.path.join(WT, chemin)
        reel = h(p); comp = compagnon(p); obj = objet(chemin)
        verdict = (reel == attendu) and (comp == attendu) and (obj == attendu)
    else:
        p = os.path.join(DEPOT, chemin)
        if not os.path.exists(p):
            print("ABSENT", chemin); ko += 1; continue
        reel = h(p); comp = compagnon(p); obj = "(dépôt)"
        verdict = (reel == attendu) and (comp in (attendu, None))
    print(("OK  " if verdict else "KO  "), chemin, "| fichier", reel == attendu, "| compagnon", comp == attendu if comp else "absent", "| objet", obj == attendu if obj != "(dépôt)" else obj)
    ok += verdict; ko += (not verdict)
print(f"{ok} conformes, {ko} non conformes, sur {len(lignes)}")
