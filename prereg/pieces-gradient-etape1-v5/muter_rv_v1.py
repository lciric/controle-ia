import os, pathlib, shutil, subprocess, sys
SRC = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
MUTATIONS = [
 ("m1-cablage-fuite", "essaim_m3/noyau/boucle.py", "empreintes_fuite=self._empreintes_fuite(), empreintes_courtes=self._empreintes_courtes())", "empreintes_courtes=self._empreintes_courtes())", "test_rv12_garde_de_fuite_cablee_de_bout_en_bout"),
 ("m2-attente-fils", "essaim_m3/noyau/serveur.py", "            f.join(timeout=max(0.0, limite - _time.monotonic()))", "            pass", "test_rv08_appels_en_vol_attendus_avant_la_lecture_du_journal"),
 ("m3-vivants", "essaim_m3/noyau/boucle.py", "        if not self.isolation[\"utilisateur\"]:\n            return\n        for d in dossiers:", "        return\n        for d in dossiers:", "test_rv02_dossiers_vivants_rendus_a_root_et_decalage_distinct_en_reel"),
 ("m4-vue-importee", "essaim_m3/noyau/archive.py", "                    if gid is not None:\n                        os.chown(f, 0, gid, follow_symlinks=False)\n                        os.chmod(f, 0o550 if f.is_dir() else 0o440)\n                    else:\n                        os.chmod(f, 0o555 if f.is_dir() else 0o444)\n                except OSError:\n                    pass\n            importees.append(ligne)\n        if gid is not None and", "                    os.chmod(f, 0o555 if f.is_dir() else 0o444)\n                except OSError:\n                    pass\n            importees.append(ligne)\n        if False and", "test_rv03_vue_importee_fermee_aux_autres_lignees_des_l_import"),
 ("m5-reponses-lues", "essaim_m3/analyse_gradient.py", "    f = _dossier_generation(course, lignee, generation) / \"juge\" / \"reponses-lues.json\"\n    if not f.is_file():", "    f = _dossier_generation(course, lignee, generation) / \"juge\" / \"reponses_test.json\"\n    if not f.is_file():", "test_rv01_lecture_h_g1_suit_le_juge_absence_de_reponse_et_marque_d_ordre"),
 ("m6-tmp-prives", "essaim_m3/noyau/bac_a_sable.py", "    for d in DOSSIERS_TMP_PARTAGES:", "    for d in ():", "test_rv04_tmp_prive_a_chaque_execution"),
 ("m7-fisher", "essaim_m3/analyse_gradient.py", "abs(ea - eb) >= ECHECS_ECART_MIN and p < ALPHA_PANNE", "abs(ea - eb) >= ECHECS_ECART_MIN", "test_h_g1_couverture_pannes_recoupements_et_trois_niveaux"),
 ("m8-vivier-un-sens", "essaim_m3/noyau/vivier.py", "max(n / tailles[k] if tailles[k] else 0.0, n / len(propres) if propres else 0.0)", "(n / tailles[k] if tailles[k] else 0.0)", "test_ce403_garde_unicode_deux_sens_et_identifiants_tires"),
 ("m9-statut-lien", "essaim_m3/noyau/bac_a_sable.py", "    donnees_statut, raison_statut = lire_fichier_organisme(dossier_travail / \"statut_execution.json\", 200_000)", "    donnees_statut, raison_statut = ((dossier_travail / \"statut_execution.json\").read_bytes(), None) if (dossier_travail / \"statut_execution.json\").exists() else (None, \"absent\")", "test_rv05_statut_et_erreurs_lus_sans_lien_ni_tube"),
 ("m10-unicode", "essaim_m3/noyau/garde_fuite.py", "_SEPARATEUR = re.compile(r\"[\\W_]+\")", "_SEPARATEUR = re.compile(r\"[^0-9a-zà-ÿ]+\")", "test_ce403_garde_unicode_deux_sens_et_identifiants_tires"),
 ("m11-notices", "essaim_m3/noyau/recherche.py", "        resultats = gardes\n", "        retires = []\n", "test_rv07_notices_qui_recopient_une_tache_de_test_retirees"),
 ("m12-importees-extrait", "essaim_m3/outils/extrait_mecanique.py", "        g[\"importee\"] = str(d.relative_to(racine_archive)) in importees", "        g[\"importee\"] = False", "tests/test_outils.py::test_extrait_mecanique_v2_statuts_des_services_et_rondes_importees"),
]
OUT.mkdir(exist_ok=True)
for nom, fichier, avant, apres, essai in MUTATIONS:
    copie = OUT / nom
    if copie.exists(): shutil.rmtree(copie)
    shutil.copytree(SRC, copie, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    f = copie / fichier; t = f.read_text(encoding="utf-8")
    if t.count(avant) != 1:
        print(f"{nom}: MOTIF {t.count(avant)} fois — non appliquée"); continue
    f.write_text(t.replace(avant, apres), encoding="utf-8")
    cible = essai if "::" in essai else f"tests/test_noyau.py::{essai}"
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", cible], cwd=copie, capture_output=True, text=True, timeout=600,
                       env=dict(os.environ, ESSAIM_M3_COLLISIONNEUR=str(SRC.parent / "collisionneur-v2.5-banc-jev-travail" / "collisionneur_v2.py")))
    fin = (r.stdout.strip().splitlines() or ["?"])[-1]
    if " error" in fin:
        print(f"{nom}: ERREUR DE COLLECTE — {fin}"); shutil.rmtree(copie); continue
    print(f"{nom}: {'ÉCHOUE (attendu)' if r.returncode != 0 else 'PASSE (essai aveugle !)'} — {fin}")
    shutil.rmtree(copie)
