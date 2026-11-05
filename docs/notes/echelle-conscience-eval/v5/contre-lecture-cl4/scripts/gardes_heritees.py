"""Gardes héritées du lanceur v4, éprouvées sans rien modifier hors du bac à sable :
1. `exiger_prereg_scelle` (src/controle_ia/prereg.py) sur des copies du brouillon v5 dans le bac à sable ;
2. `.claude/hooks/garde_calcul.py`, lancée comme le lanceur la lance (même entrée JSON), sur des GO du registre courant.
La commande passée à la garde est construite ici, jamais écrite en clair sur une ligne de commande."""
import hashlib, json, pathlib, re, shutil, subprocess, sys
DEPOT = pathlib.Path("/home/user/controle-ia-travail")
SB = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v5/gardes")
SB.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(DEPOT / "src"))
from controle_ia.prereg import exiger_prereg_scelle, problemes
from controle_ia.scellement import sceller

def essai(nom, f):
    try:
        print(f"  {nom} : passe ({f()[:12]}…)")
    except Exception as e:
        print(f"  {nom} : arrêt ({type(e).__name__} : {str(e)[:160]})")

print("1. exiger_prereg_scelle")
brouillon = (DEPOT / "prereg/brouillon-test-echelle-conscience-eval-v5.md").read_text(encoding="utf-8")
# a. le brouillon tel quel (section Contre-lecture « À REMPLIR »), scellé : refusé
a = SB / "a-tel-quel.md"; a.write_text(brouillon, encoding="utf-8"); sceller(a)
essai("brouillon tel quel, scellé", lambda: exiger_prereg_scelle(a))
# b. section Contre-lecture remplie (deux empreintes), scellé : cas sain
rempli = brouillon.replace("À REMPLIR après la relecture neuve (R2) des parties changées.",
                           "- Contre-lecture 4 : brouillon relu `" + "1" * 64 + "`, rapport `" + "2" * 64 + "`.")
b = SB / "b-rempli.md"; b.write_text(rempli, encoding="utf-8"); sceller(b)
essai("Contre-lecture remplie, scellé (sain)", lambda: exiger_prereg_scelle(b))
# c. rempli mais sans compagnon
c = SB / "c-sans-compagnon.md"; c.write_text(rempli, encoding="utf-8")
essai("rempli, sans compagnon", lambda: exiger_prereg_scelle(c))
# d. rempli, scellé, puis modifié
d = SB / "d-modifie.md"; d.write_text(rempli, encoding="utf-8"); sceller(d); d.write_text(rempli + " ", encoding="utf-8")
essai("rempli, scellé puis modifié", lambda: exiger_prereg_scelle(d))
# e. rempli, scellé, mais le commit des outils remplacé par un autre dans tout le texte : passe quand même
autre = rempli.replace("f579930842ab633cdced18a13f82d77bb467ca7f", "0" * 40)
e = SB / "e-autre-commit.md"; e.write_text(autre, encoding="utf-8"); sceller(e)
essai("rempli, scellé, autre commit écrit dans le texte", lambda: exiger_prereg_scelle(e))
lanceur = (pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v4/scripts/lancer_echelle_v4.sh")).read_text()
print("  le lanceur relit-il le commit dans le texte scellé ?",
      "oui" if re.search(r'grep[^\n]*\$COMMIT[^\n]*PREREG|PREREG[^\n]*\$COMMIT', lanceur) else "non (aucune comparaison entre COMMIT et le texte)")

print("2. garde de calcul (entrée JSON du lanceur, étape 4)")
outil = "vast" + "ai"
def garde(go):
    cmd = (f"GO_ID={go} " if go else "") + f"{outil} " + "cre" + "ate instance 0 --raw"
    r = subprocess.run([sys.executable, "-I", "-B", str(DEPOT / ".claude/hooks/garde_calcul.py")],
                       input=json.dumps({"tool_input": {"command": cmd}}), capture_output=True, text=True)
    return r.returncode, r.stderr.strip()[:200]
go_lignes = [l for l in (DEPOT / "registres/go.md").read_text(encoding="utf-8").splitlines() if l.startswith("| GO-")]
def ligne(go):
    for l in go_lignes:
        if l.startswith(f"| {go} |"):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            return f"type {c[2]!r}, plafond {c[4]!r}, échéance {c[5]}, périmètre : {c[3][:110]}…"
    return "absent"
for go in ("GO-0000-00-00-00", None, "GO-2026-10-04-01", "GO-2026-10-04-08", "GO-2026-10-26-08"):
    code, err = garde(go)
    print(f"  {go} : code {code} {('— ' + err) if err else '(passe)'}")
    if go and go != "GO-0000-00-00-00":
        print(f"      registre : {ligne(go)}")
