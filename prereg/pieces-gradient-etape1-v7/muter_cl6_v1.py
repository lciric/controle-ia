"""Banc de mutation pour CL6-02 (boucle `prives` de `ABAISSER_SOURCE`, essaim_m3/noyau/bac_a_sable.py).
Usage : python -I -B muter_cl6_v1.py SRC_PACKAGE_DIR SORTIE_TMP COLLISIONNEUR
Témoin : l'essai test_cl6_02 passe sur le code livré. Mutant : on retire le saut errno 2 de la boucle `prives`
(un dossier inscriptible par tous imbriqué sous un temporaire déjà rendu privé fait alors échouer l'exécution) ;
l'essai doit échouer. Modelé sur muter.py (contre-lecture n° 6)."""
import os, pathlib, shutil, subprocess, sys

SRC = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); COLL = sys.argv[3]
ESSAI = "test_cl6_02_dossier_inscriptible_imbrique_sous_un_temporaire"
AVANT = ('            if ctypes.get_errno() == 2:\n'
         '                continue\n'
         '            sys.exit("dossier temporaire prive impossible sur " + d + " (errno " + str(ctypes.get_errno()) + ")")')
APRES = '            sys.exit("dossier temporaire prive impossible sur " + d + " (errno " + str(ctypes.get_errno()) + ")")'
ENV = dict(os.environ, ESSAIM_M3_COLLISIONNEUR=COLL, ESSAIM_M3_ESPACE="/var/lib/essaim-m3",
           PATH="/usr/bin:/bin", LANG="C.UTF-8")

def lancer(cwd):
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x",
                        f"tests/test_noyau.py::{ESSAI}"], cwd=cwd, capture_output=True, text=True, timeout=600,
                       env=dict(ENV, HOME=str(pathlib.Path(cwd) / "_home")))
    (pathlib.Path(cwd) / "_home").mkdir(exist_ok=True)
    return r

OUT.mkdir(parents=True, exist_ok=True)

# Témoin : code livré, non muté
print("=== TÉMOIN (code livré, non muté) ===")
r = lancer(SRC)
fin = (r.stdout.strip().splitlines() or ["?"])[-1]
print(f"cl6-02 témoin : {'PASSE (attendu)' if r.returncode == 0 else 'ÉCHOUE (inattendu !)'} — {fin}")
if r.returncode != 0:
    print(r.stdout[-2000:]); print(r.stderr[-1000:])

# Mutant : saut errno 2 retiré de la boucle prives
print("\n=== MUTANT cl6-02 (saut errno 2 retiré de la boucle prives) ===")
copie = OUT / "cl6-02"
if copie.exists(): shutil.rmtree(copie)
shutil.copytree(SRC, copie, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
f = copie / "essaim_m3" / "noyau" / "bac_a_sable.py"; t = f.read_text()
n = t.count(AVANT)
if n != 1:
    print(f"cl6-02 : MOTIF trouvé {n} fois — mutation non appliquée"); shutil.rmtree(copie); sys.exit(1)
f.write_text(t.replace(AVANT, APRES))
r = lancer(copie)
fin = (r.stdout.strip().splitlines() or ["?"])[-1]
verdict = "ÉCHOUE (attendu — la mutation est détectée)" if r.returncode != 0 else "PASSE (essai aveugle !)"
if " error" in fin: verdict = "ERREUR DE COLLECTE"
print(f"cl6-02 mutant : {verdict} — {fin}")
shutil.rmtree(copie)
print("\n(Une correction est éprouvée si le témoin passe et le mutant échoue.)")
