"""Mutations sur copies du code de la règle (a') de P3-bis (consigne `consigne-code-p3bis-regle-a-v1.md`, `39300056…`, mandat 4).

    python -I mutations_p3bis_regle_a_v1.py ARBRE DOSSIER_NEUF JOURNAL.txt [ID …]

Pour chaque mutation : copie de `src/`, `tests/`, `scripts/` et `pyproject.toml` de l'arbre dans `DOSSIER_NEUF/<id>/`, une
seule modification (texte trouvé **une fois**, sinon arrêt), puis les essais visés joués **dans la copie** :
`python -m pytest -o pythonpath="src tests" -p trace_import_mutation …`, le greffon (hors de la copie, sur `PYTHONPATH`, seul
dossier qui y figure) écrivant au début de la session le fichier réellement importé de chaque module muté (**import
tracé** : il doit être sous la copie). Mutation **tuée** si les essais visés échouent ; **survivante** sinon. Un **témoin**
sans mutation joue les mêmes fichiers (sauf l'essai de fermeture complet, joué à part) et doit passer : il éprouve le harnais
(R5). Chaque copie est effacée par son chemin exact après son passage."""
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

L2 = "src/controle_ia/premier_test_ia/lecture_p3bis_v2.py"
O3 = "src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py"
E3 = "scripts/essai_fermeture_p3bis_v3.py"
P2 = "src/controle_ia/t07/plancher_v2.py"
TL = "tests/test_premier_test_ia_lecture_p3bis_v2.py"
TO = "tests/test_premier_test_ia_ouverture_p3bis_v3.py"
TE = "tests/test_essai_fermeture_p3bis_v3.py"
TN = "tests/test_premier_test_ia_notation_plancher_800_v1.py"
MODULES_TRACES = {L2: "controle_ia.premier_test_ia.lecture_p3bis_v2", O3: "controle_ia.premier_test_ia.ouverture_p3bis_v3",
                  P2: "controle_ia.t07.plancher_v2"}
MUTATIONS = [
    ("m01", "plancher exigé à 799 directions", L2, "N_PLANCHER = 800 ", "N_PLANCHER = 799 ",
     [f"{TL}::test_plancher_de_800_directions_dans_l_ordre_du_tirage"]),
    ("m02", "ancienne règle sur 199 directions", L2, "N_PLANCHER_ANCIEN = 200 ", "N_PLANCHER_ANCIEN = 199 ",
     [f"{TL}::test_lecture_decisive_egale_au_bit_pres_a_l_appel_de_c7"]),
    ("m03", "quantile du plancher 0,90", L2, "QUANTILE_PLANCHER = 0.95", "QUANTILE_PLANCHER = 0.90",
     [f"{TL}::test_lecture_decisive_egale_au_bit_pres_a_l_appel_de_c7"]),
    ("m04", "ancienne règle sur les 200 dernières directions", L2, "plancher_at[:N_PLANCHER_ANCIEN].T",
     "plancher_at[-N_PLANCHER_ANCIEN:].T", [f"{TL}::test_lecture_decisive_egale_au_bit_pres_a_l_appel_de_c7",
                                             f"{TL}::test_ancienne_regle_sur_les_seules_200_premieres_et_reserve_r_r"]),
    ("m05", "prédicteur trivial : « au moins » devient « plus que »", L2,
     'qui = sorted(k for k, x in triv.items() if x["separation"] is not None and x["separation"] >= sep)',
     'qui = sorted(k for k, x in triv.items() if x["separation"] is not None and x["separation"] > sep)',
     [f"{TL}::test_non_interpretable_par_un_predicteur_trivial_de_p3",
      f"{TL}::test_frontiere_au_moins_autant_predicteur_trivial_et_mention"]),       # essai de frontière : après la 1re passe
    ("m06", "mention étendue : « atteint » devient « dépasse »", L2,
     'm["separation"] is not None and m["separation"] >= separation(aire))',
     'm["separation"] is not None and m["separation"] > separation(aire))', [f"{TL}::test_issue_de_chaque_run_jouet",
     f"{TL}::test_frontiere_au_moins_autant_predicteur_trivial_et_mention"]),        # essai de frontière : après la 1re passe
    ("m07", "réserve R-R inversée", L2, 'if anc["issue"] != s["issue_mecanique"]:', 'if anc["issue"] == s["issue_mecanique"]:',
     [f"{TL}::test_issue_de_chaque_run_jouet"]),
    ("m08", "PB-7 lu dans la lecture de P3", L2, 'th = s["jeux_regle_a"]["temoin-honnete"]',
     'th = {"etat": l3["etats_des_jeux"][p].get("temoin-honnete")}',
     [f"{TL}::test_reserve_pb7_suit_la_regle_a_et_non_la_lecture_de_p3"]),
    ("m09", "ordre du tirage non contrôlé", L2, 'any(x != f"{racine}{k}" for k, x in enumerate(pl))', "False",
     [f"{TL}::test_plancher_de_800_directions_dans_l_ordre_du_tirage"]),
    ("m10", "lecture de P3 à un autre nombre de directions admise", L2,
     'if (l3.get("n_plancher") or {}).get(p) != N_PLANCHER:', "if False:", [f"{TL}::test_accords_avec_la_lecture_de_p3"]),
    ("m11", "aire non comparée à la lecture de P3", L2,
     'if "echec" not in d3 and (aire is None or float(d3["aire"]) != aire):', "if False:",
     [f"{TL}::test_accords_avec_la_lecture_de_p3"]),
    ("m12", "prédicteurs triviaux non comparés", L2, "if ligne is not None and any(", "if False and any(",
     [f"{TL}::test_accords_avec_la_lecture_de_p3"]),
    ("m13", "intervalles des deux règles non comparés", L2, 'if "echec" in ra or "echec" in anc:\n        return',
     "if True:\n        return", [f"{TL}::test_meme_intervalle_sous_la_meme_graine"]),
    ("m14", "graine de PB-13 pour la lecture décisive", L2, "g = graine_entiere(graines[CLE_DECISIVE])",
     "g = graine_entiere(graines[CLE_SANS_MENTION])", [f"{TL}::test_lecture_decisive_egale_au_bit_pres_a_l_appel_de_c7"]),
    ("m15", "échec de la règle (a) non rattrapé", L2,
     "QUANTILE_PLANCHER, float(niveau)))\n    except GardeArret as e:", "QUANTILE_PLANCHER, float(niveau)))\n    except ZeroDivisionError as e:",
     [f"{TL}::test_regle_a_echec_sur_tirages_degeneres_et_classe_manquante"]),
    ("m16", "issue tirée de l'ancienne règle", L2, 's["issue_mecanique"] = v1.issue_mecanique(s["etat_decisif"]["E_prime"])',
     's["issue_mecanique"] = v1.issue_mecanique(etat_decisif(anc, c["triviaux"][JEU_DECISIF], m, s["sonde_p"])["E_prime"])',
     [f"{TL}::test_ancienne_regle_sur_les_seules_200_premieres_et_reserve_r_r"]),
    ("m17", "PB-9 : directions neuves non contrôlées", L2, "and set(neuves) == attendues and not (attendues & set(b))",
     "and not (attendues & set(b))", [f"{TL}::test_identite_pb9_par_nom"]),
    ("m18", "sans resume_pour_critere", L2, "return pl2.resume_pour_critere(pl2.comparer_difference_au_plancher(",
     "return (pl2.comparer_difference_au_plancher(", [f"{TL}::test_lecture_decisive_egale_au_bit_pres_a_l_appel_de_c7"]),
    ("m19", "positifs inversés au jeu décisif", L2, "y_at = (cond[m_at] == A).astype(np.int64)\n    sonde_at",
     "y_at = (cond[m_at] == T).astype(np.int64)\n    sonde_at", [f"{TL}::test_issue_de_chaque_run_jouet"]),
    ("m20", "PB-13 sur toutes les actions", L2, "m = sans & ((cond == A) | (cond == T))", "m = (cond == A) | (cond == T)",
     [f"{TL}::test_pb13_aligne_sur_la_regle_a"]),
    ("m21", "A contre H lu à 95 %", L2, "JEUX_DESCRIPTIFS = ((A, H, NIVEAU_A_H)", "JEUX_DESCRIPTIFS = ((A, H, NIVEAU)",
     [f"{TL}::test_jeux_descriptifs_et_pb7_sous_la_regle_a"]),
    ("m22", "la sortie standard porte l'issue", L2,
     "    analyser(Path(\".\"), a.run_source, a.lecture, a.run_lecture, a.prereg, a.entropie)\n    return 0",
     "    print(analyser(Path(\".\"), a.run_source, a.lecture, a.run_lecture, a.prereg, a.entropie)[\"issue_mecanique\"])\n    return 0",
     [f"{TL}::test_analyser_aucune_impression_code_0_et_garde_code_1"]),
    ("m23", "ouverture v3 : lecture complémentaire v1", O3, '"controle_ia.premier_test_ia.lecture_p3bis_v2", "--run-source"',
     '"controle_ia.premier_test_ia.lecture_p3bis_v1", "--run-source"',
     [f"{TO}::test_commandes_des_lectures", f"{TO}::test_v3_egale_a_v2_hors_des_lignes_declarees"]),
    ("m24", "ouverture v3 : une constante changée", O3, "TAILLE_MORCEAU_MAX = 90_000_000", "TAILLE_MORCEAU_MAX = 90_000_001",
     [f"{TO}::test_fonctions_et_classes_de_meme_source_hors_des_deux_changees"]),
    ("m25", "ouverture v3 : une fonction changée hors des deux déclarées", O3, "PRESET_XZ = 6", "PRESET_XZ = 9",
     [f"{TO}::test_fonctions_et_classes_de_meme_source_hors_des_deux_changees", f"{TO}::test_v3_egale_a_v2_hors_des_lignes_declarees"]),
    ("m26", "essai de fermeture v3 à 200 directions", E3, "N_TACHES, T_PAS, N_PLANCHER, L_JETONS, D_SIGNAL = 8, 4, 800, 6, 2.5",
     "N_TACHES, T_PAS, N_PLANCHER, L_JETONS, D_SIGNAL = 8, 4, 200, 6, 2.5",
     [f"{TE}::test_v3_egal_au_script_v2_hors_des_remplacements_declares"]),
    ("m27", "plancher_v2 : lot de 26 directions (fichier de C7 altéré)", P2, "LOT_DIRECTIONS = 25", "LOT_DIRECTIONS = 26",
     [f"{TL}::test_plancher_v2_egal_au_fichier_de_c7"]),
]
GREFFON = '''"""Greffon de trace d'import des mutations : écrit, au début de la session, le fichier de chaque module muté."""
import importlib, json, os

def pytest_sessionstart(session):
    noms = json.loads(os.environ["MODULES_TRACES"])
    trace = {n: importlib.import_module(n).__file__ for n in noms}
    with open(os.environ["TRACE_IMPORT"], "w", encoding="utf-8") as f:
        json.dump(trace, f, ensure_ascii=False)
'''


def copier(arbre: Path, d: Path) -> None:
    d.mkdir(parents=True)
    for x in ("src", "tests", "scripts"):
        shutil.copytree(arbre / x, d / x, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"))
    shutil.copy2(arbre / "pyproject.toml", d / "pyproject.toml")


def jouer(d: Path, essais: list[str], greffon: Path, n_cible: str | None) -> dict:
    trace = d / "trace-import.json"
    env = {k: os.environ[k] for k in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR") if k in os.environ}
    env.update(PYTHONPATH=str(greffon), PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1", TRACE_IMPORT=str(trace),
               MODULES_TRACES=json.dumps(sorted(set(MODULES_TRACES.values()))))
    t0 = time.monotonic()
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "--color=no",
                        "-p", "trace_import_mutation", "-o", "pythonpath=src tests", f"--basetemp={d / 'tmp'}", *essais],
                       cwd=str(d), env=env, capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if x.strip()]
    t = json.loads(trace.read_text(encoding="utf-8")) if trace.is_file() else {}
    sous_la_copie = bool(t) and all(str(Path(f).resolve()).startswith(str(d.resolve()) + os.sep) for f in t.values())
    cible = None if n_cible is None else t.get(MODULES_TRACES[n_cible])
    return {"code": r.returncode, "derniere": lignes[-1] if lignes else "", "trace": t, "import_sous_la_copie": sous_la_copie,
            "fichier_mute_importe": cible, "duree_s": round(time.monotonic() - t0, 1)}


def main(argv) -> int:
    arbre, dossier, journal = Path(argv[0]).resolve(), Path(argv[1]).resolve(), Path(argv[2])
    choisies = set(argv[3:])                     # sous-ensemble rejoué (vide : toutes)
    if choisies - {m[0] for m in MUTATIONS}:
        raise SystemExit(f"mutations inconnues : {sorted(choisies - {m[0] for m in MUTATIONS})}")
    if dossier.exists() or journal.exists():
        raise SystemExit(f"{dossier} ou {journal} existe déjà (R12)")
    dossier.mkdir(parents=True)
    greffon = dossier / "greffon"
    greffon.mkdir()
    (greffon / "trace_import_mutation.py").write_text(GREFFON, encoding="utf-8")
    sortie, tuees, n = [f"Mutations de la règle (a') de P3-bis, v1 — arbre {arbre}, début {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}"], 0, 0
    # témoin : sans mutation, les quatre fichiers d'essais (sauf l'essai de fermeture complet) doivent passer
    d = dossier / "temoin"
    copier(arbre, d)
    r = jouer(d, [TL, TO, TN, f"{TE}::test_v3_egal_au_script_v2_hors_des_remplacements_declares"], greffon, L2)
    temoin_ok = r["code"] == 0 and r["import_sous_la_copie"]
    sortie.append(f"témoin (aucune mutation) : code {r['code']} ; {r['derniere']} ; import sous la copie : {r['import_sous_la_copie']} "
                  f"({r['trace']}) ; {r['duree_s']} s ; {'CONFORME' if temoin_ok else 'NON CONFORME'}")
    shutil.rmtree(d)
    for id_, desc, fichier, ancien, nouveau, essais in [m for m in MUTATIONS if not choisies or m[0] in choisies]:
        d = dossier / id_
        copier(arbre, d)
        p = d / fichier
        texte = p.read_text(encoding="utf-8")
        if texte.count(ancien) != 1:
            raise SystemExit(f"{id_} : texte à muter trouvé {texte.count(ancien)} fois dans {fichier}")
        p.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        r = jouer(d, essais, greffon, fichier if fichier in MODULES_TRACES else None)
        n += 1
        mute_ok = r["fichier_mute_importe"] is None or Path(r["fichier_mute_importe"]).resolve() == p.resolve()
        tuee = r["code"] != 0 and r["import_sous_la_copie"] and mute_ok
        tuees += int(tuee)
        sortie.append(f"{id_} — {desc} ({fichier}) : essais {[e.split('::')[-1] for e in essais]} ; code {r['code']} ; "
                      f"{r['derniere'][:110]} ; import tracé sous la copie : {r['import_sous_la_copie']}, fichier muté importé : "
                      f"{mute_ok} ; {r['duree_s']} s ; {'TUÉE' if tuee else 'SURVIVANTE'}")
        shutil.rmtree(d)
    shutil.rmtree(greffon)
    sortie.append(f"MUTATIONS : {tuees} tuées sur {n} ; témoin sain : {'CONFORME' if temoin_ok else 'NON CONFORME'} ; fin "
                  f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    journal.write_text("\n".join(sortie) + "\n", encoding="utf-8")
    print(sortie[-1])
    return 0 if temoin_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
