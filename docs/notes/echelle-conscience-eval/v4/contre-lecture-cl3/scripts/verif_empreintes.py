"""Vérifie une à une les empreintes du tableau d'outils et du tableau Traces du brouillon v4."""
import hashlib, re, sys, os, subprocess
BROUILLON = "/home/user/controle-ia-travail/prereg/brouillon-test-echelle-conscience-eval-v4.md"
ARBRE = "/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1"
DEPOT = "/home/user/controle-ia-travail"
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()
texte = open(BROUILLON, encoding="utf-8").read()
lignes = re.findall(r"^\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", texte, re.M)
print(len(lignes), "lignes à empreinte complète")
ok = 0
for chemin, attendu in lignes:
    if chemin.startswith("echelle-v3/"):
        p = os.path.join(ARBRE, chemin)
        # aussi contre le commit
        blob = subprocess.run(["git", "-C", ARBRE, "show", "c08a5b21df42aa10f7c7351173ccb75ed5a101ca:" + chemin], capture_output=True).stdout
        sha_commit = hashlib.sha256(blob).hexdigest()
    else:
        p = os.path.join(DEPOT, chemin)
        sha_commit = None
    reel = sha(p) if os.path.exists(p) else "ABSENT"
    comp = p + ".sha256"
    comp_val = open(comp).read().split()[0] if os.path.exists(comp) else "SANS-COMPAGNON"
    etat = "OK" if reel == attendu else "DIFFERENT"
    etat_c = "OK" if comp_val == attendu else comp_val
    etat_commit = "" if sha_commit is None else ("commit OK" if sha_commit == attendu else "commit DIFFERENT " + sha_commit)
    print(f"{etat:9s} compagnon {etat_c:9s} {etat_commit:10s} {chemin}")
    ok += etat == "OK"
print("concordants :", ok, "/", len(lignes))
# empreintes abrégées citées
abr = re.findall(r"`([^`]+)`,\s*`([0-9a-f]{7,8})…`", texte)
print("abrégées:", abr)
