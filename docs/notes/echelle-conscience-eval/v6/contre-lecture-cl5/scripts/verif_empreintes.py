"""Verifie les empreintes du brouillon v6 : fichiers, compagnons, objets du commit (lecture seule)."""
import hashlib, os, re, subprocess, sys
DEPOT = "/home/user/controle-ia-travail"
WT = "/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1"
COMMIT = "8b4db5a6c8b109695fbf0a5394cc19c880d9041a"
texte = open(os.path.join(DEPOT, "prereg/brouillon-test-echelle-conscience-eval-v6.md"), encoding="utf-8").read()
lignes = re.findall(r"^\s*\| `([^`]+)` \| `([0-9a-f]{64})` \|", texte, re.M)
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
ok = 0; ko = 0
for chemin, empreinte in lignes:
    if chemin.startswith("echelle-v5/"):
        p = os.path.join(WT, chemin)
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()
        comp = open(p + ".sha256").read().split()[0] if os.path.exists(p + ".sha256") else None
        blob = subprocess.run(["git", "-C", WT, "show", f"{COMMIT}:{chemin}"], capture_output=True, env=env).stdout
        hb = hashlib.sha256(blob).hexdigest()
        etat = "OK" if (h == empreinte == comp == hb) else "ECART"
        print(f"{etat} outil {chemin} fichier={h[:12]} texte={empreinte[:12]} compagnon={(comp or 'absent')[:12]} commit={hb[:12]}")
    else:
        p = os.path.join(DEPOT, chemin)
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()
        comp = None
        if os.path.exists(p + ".sha256"):
            comp = open(p + ".sha256").read().split()[0]
        etat = "OK" if h == empreinte and (comp is None or comp == h) else "ECART"
        print(f"{etat} trace {chemin} fichier={h[:12]} texte={empreinte[:12]} compagnon={(comp or 'absent')[:12]}")
    ok += etat == "OK"; ko += etat != "OK"
print(f"total {len(lignes)} ; OK {ok} ; ECART {ko}")
