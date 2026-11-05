import os, pathlib, shutil, subprocess, sys
SRC = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
COLL = str(SRC.parent / "collisionneur-v2.5-banc-jev-travail" / "collisionneur_v2.py")
MUT = [
 ("cl5-01-cacher", "essaim_m3/noyau/bac_a_sable.py",
  '        caches = dossiers_a_cacher([cwd, *gardes])              # CL5-01 : dépôt, code, /home… cachés (vide, lecture seule)',
  '        caches = []  # mutation CL5-01',
  "test_cl5_01_banque_cachee_a_l_organisme"),
 ("cl5-02-balayage", "essaim_m3/noyau/bac_a_sable.py",
  '    for d in dossiers_inscriptibles_par_tous():',
  '    for d in DOSSIERS_TMP_PARTAGES:  # mutation CL5-02',
  "test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous"),
 ("cl5-04-exclues", "essaim_m3/analyse_gradient.py",
  "    if exclues and apres_audit != \"defaut_paires\":\n        raise ValueError(\"exclues n'est permis qu'avec apres_audit='defaut_paires' (une paire n'est coupée par l'audit qu'après un rapport d'audit scellé)\")\n",
  "",
  "test_cl5_04_lire_h_g1_compose_et_refuse_exclues_sans_audit"),
 ("cl5-07-compte", "essaim_m3/analyse_gradient.py",
  "    if _MOTIF_COMPTE.search(s):\n        return True\n",
  "",
  "test_h_g1_couverture_pannes_recoupements_et_trois_niveaux"),
]
OUT.mkdir(exist_ok=True)
for nom, fichier, avant, apres, essai in MUT:
    copie = OUT / nom
    if copie.exists(): shutil.rmtree(copie)
    shutil.copytree(SRC, copie, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    f = copie / fichier; t = f.read_text()
    if t.count(avant) != 1:
        print(f"{nom}: MOTIF {t.count(avant)} fois — non appliquée"); shutil.rmtree(copie); continue
    f.write_text(t.replace(avant, apres))
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x",
                        f"tests/test_noyau.py::{essai}"], cwd=copie, capture_output=True, text=True, timeout=600,
                       env=dict(os.environ, ESSAIM_M3_COLLISIONNEUR=COLL, ESSAIM_M3_ESPACE="/var/lib/essaim-m3",
                                PATH="/usr/bin:/bin", HOME="/tmp", LANG="C.UTF-8"))
    fin = (r.stdout.strip().splitlines() or ["?"])[-1]
    verdict = "ÉCHOUE (attendu)" if r.returncode != 0 else "PASSE (essai aveugle !)"
    if " error" in fin: verdict = "ERREUR DE COLLECTE"
    print(f"{nom}: {verdict} — {fin}")
    shutil.rmtree(copie)
