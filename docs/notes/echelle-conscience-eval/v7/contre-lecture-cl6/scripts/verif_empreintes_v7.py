"""Vérifie les empreintes citées par le brouillon v7 : outils (fichier, compagnon, objet du commit) et traces (fichier, compagnon)."""
import hashlib, os, re, subprocess, sys
TEXTE = "/home/user/controle-ia-travail/prereg/brouillon-test-echelle-conscience-eval-v7.md"
DEPOT = "/home/user/controle-ia-travail"
WT = "/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1"
COMMIT = "b8b76650d29e213cf5da9b8fccee22cad9ba98c5"
def h(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
def compagnon(p):
    c = p + ".sha256"
    if not os.path.exists(c):
        return None
    return open(c).read().split()[0]
txt = open(TEXTE, encoding="utf-8").read()
lignes = re.findall(r"^\s*\| `([^`]+)` \| `([0-9a-f]{64})` \|", txt, re.M)
ok = ko = 0
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
for chemin, attendu in lignes:
    if chemin.startswith("echelle-v6/"):
        p = os.path.join(WT, chemin)
        f = h(p); c = compagnon(p)
        g = hashlib.sha256(subprocess.run(["git", "-C", WT, "show", f"{COMMIT}:{chemin}"], capture_output=True, env=env, check=True).stdout).hexdigest()
        bon = (f == attendu == c == g)
        print(("OK " if bon else "KO ") + chemin, "fichier" if f == attendu else "FICHIER!", "compagnon" if c == attendu else f"COMPAGNON!({c})", "commit" if g == attendu else "COMMIT!")
    else:
        p = os.path.join(DEPOT, chemin)
        f = h(p); c = compagnon(p)
        bon = (f == attendu and (c is None or c == attendu))
        print(("OK " if bon else "KO ") + chemin, "fichier" if f == attendu else "FICHIER!", "compagnon" if c == attendu else f"COMPAGNON:{c}")
    ok += bon; ko += (not bon)
print(f"{ok} OK, {ko} KO sur {len(lignes)}")
# empreintes abrégées citées dans le texte
abr = re.findall(r"`([^`]+\.(?:md|txt|json|py|jsonl))`, `([0-9a-f]{8})…`", txt)
print("--- empreintes abrégées citées")
for chemin, debut in abr:
    p = os.path.join(DEPOT, chemin)
    if os.path.exists(p):
        f = h(p)
        print(("OK " if f.startswith(debut) else "KO ") + chemin, debut, f[:16])
    else:
        print("ABSENT", chemin, debut)
