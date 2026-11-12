"""Remplacements déclarés des copies du code du plancher v3 de T0.7 (fichier d'appui des essais, non collecté).

Chaque copie de `lecture_v4.py`, `passe_blanc_v2.py` et `repli_etapes_v2.py` est le texte d'une fonction ou d'un module gelé
(`inspect.getsource`), auquel on applique, dans l'ordre, les remplacements ci-dessous, chacun trouvé exactement le nombre de
fois écrit (1 par défaut). L'essai de miroir (`test_t07_plancher_v3_lecture_v1.py`) rejoue ces remplacements sur les sources
gelées et exige l'égalité au caractère près ; le générateur du bac à sable (`generer_lecture_v4_v1.py`) les a appliqués.
"""
from __future__ import annotations


def appliquer(source: str, remplacements) -> str:
    for r in remplacements:
        ancien, nouveau = r[0], r[1]
        n = r[2] if len(r) > 2 else 1
        trouve = source.count(ancien)
        if trouve != n:
            raise AssertionError(f"remplacement trouvé {trouve} fois, {n} attendu(s) : {ancien[:80]!r}")
        source = source.replace(ancien, nouveau)
    return source


# --------------------------------------------------------------------------------------------- lecture_v2.noter → lecture_v4.noter
NOTER = [
    ("def noter(racine: Path, run: str, mesures: dict, sondes: list, planchers_p3: dict, jetons: dict, config: dict, graines: dict,\n"
     "          couples: list, extras: dict | None = None, textes: dict | None = None) -> dict:\n",
     "def noter(racine: Path, run: str, mesures: dict, sondes: list, planchers_p3: dict, jetons: dict, config: dict, graines: dict,\n"
     "          couples: list, extras: dict | None = None, textes: dict | None = None, descriptifs_p3: dict | None = None,\n"
     "          echecs_figees: dict | None = None, sources_planchers: dict | None = None, paliers_figees: dict | None = None) -> dict:\n"),
    ('    """`lecture_v1.noter` (sondes lues',
     '    """v4 : celle de `lecture_v2.noter`, directions de plancher notées par lots (`plancher_v3.scores_plancher_vectorises`, contrôle\n'
     '    en ligne contre la boucle du harnais) ; sondes figées de P3 : plancher neuf de la réextraction (`planchers_p3`,\n'
     '    `sources_planchers`), leurs 200 directions de P3 notées en descriptif (`descriptifs_p3` → `plancher_p3_<k>`), bras arrêté\n'
     '    → « échec » de la sonde, motif écrit, scores et directions de P3 gardés (`echecs_figees`). v2 : `lecture_v1.noter` (sondes lues'),
    ('"n_plancher": int(config["n_plancher"]),\n',
     '"n_plancher": int(config["n_plancher"]),\n             "notation_planchers": pl3.METHODE_NOTATION,\n'),
    ("    extras = extras or {}\n",
     "    extras = extras or {}\n"
     "    descriptifs_p3, echecs_figees, sources_planchers = descriptifs_p3 or {}, echecs_figees or {}, sources_planchers or {}\n"
     "    paliers_figees = paliers_figees or {}\n"),
    ('                                          "empreintes_deux_premieres": [p.empreinte() for p in plancher[:2]]}\n',
     '                                          "empreintes_deux_premieres": [p.empreinte() for p in plancher[:2]]}\n'
     '                    if s.nom in paliers_figees:          # v4 : palier et réserves de la garde d\'identité de la réextraction\n'
     '                        entree["plancher"]["reextraction"] = paliers_figees[s.nom]\n'),
    ('                    entree["essai_egalite"] = essai\n'
     '                    if s.nom in planchers_p3:\n'
     '                        plancher = planchers_p3[s.nom]\n'
     '                        source = ("P3 (sondes-figees-legeres.npz, directions réutilisées, graine de P3)" if s.nom not in jetons\n'
     '                                  else "tiré par ce texte à l\'étape A (plancher_apparie, graine dérivée)")\n',
     '                    entree["essai_egalite"] = essai\n'
     '                    if s.nom in descriptifs_p3:          # v4 : les 200 directions de P3, notées en lecture descriptive\n'
     '                        tableaux[f"scores_{k}"] = pl.noter_actions(sonde, seqs)\n'
     '                        tableaux[f"plancher_p3_{k}"] = pl3.scores_plancher_vectorises(descriptifs_p3[s.nom], seqs).T\n'
     '                        entree["plancher_p3"] = {"n": len(descriptifs_p3[s.nom]), "lecture": "descriptive", "source": SOURCE_P3,\n'
     '                                                 "notation": pl3.METHODE_NOTATION,\n'
     '                                                 "empreintes_deux_premieres": [p.empreinte() for p in descriptifs_p3[s.nom][:2]]}\n'
     '                    if s.nom in echecs_figees:           # v4 : bras du plancher neuf arrêté (R5) ; aucune bascule vers P3\n'
     '                        raise GardeArret(echecs_figees[s.nom])\n'
     '                    if s.nom in planchers_p3:\n'
     '                        plancher = planchers_p3[s.nom]\n'
     '                        source = sources_planchers.get(s.nom, "tiré par ce texte à l\'étape A (plancher_apparie, graine dérivée)")\n'),
    ('                    tableaux[f"plancher_{k}"] = pl.scores_plancher(plancher, seqs).T\n'
     '                    entree["plancher"] = {"n": len(plancher), "source": source,\n',
     '                    tableaux[f"plancher_{k}"] = pl3.scores_plancher_vectorises(plancher, seqs).T\n'
     '                    entree["plancher"] = {"n": len(plancher), "source": source, "notation": pl3.METHODE_NOTATION,\n'),
    ('tableaux[f"plancher_p6_{k}"] = pl.scores_plancher(x["plancher"], seqs).T',
     'tableaux[f"plancher_p6_{k}"] = pl3.scores_plancher_vectorises(x["plancher"], seqs).T'),
    ('tableaux[f"plancher_concept_{k}"] = pl.scores_plancher(d["plancher"], seqs).T',
     'tableaux[f"plancher_concept_{k}"] = pl3.scores_plancher_vectorises(d["plancher"], seqs).T'),
]

# ------------------------------------------------------------------------------------------ lecture_v2.etape_a → lecture_v4.etape_a
ETAPE_A = [
    ('    """Étape A, v2 (celle de `lecture_v1.etape_a`,',
     '    """Étape A, v4 : celle de `lecture_v2.etape_a`, plus, avant toute autre extraction, la réextraction des jetons\n'
     '    d\'entraînement des sondes figées de P3 et leur plancher neuf (`reextraction_p3_v1.reextraire`, gardes d\'identité, 800\n'
     '    directions, `planchers-figees-t07.npz` et `reextraction-p3-t07.json` scellés ; un échec arrête le seul bras) ; les 200\n'
     '    directions de P3 lues en descriptif ; planchers notés par lots (`noter` de la v4). v2 : (celle de `lecture_v1.etape_a`,'),
    ('    taches = [f"mahalanobis-egalite/{n}" for n in connus] + [f"plancher/{n}" for n in neuves]\n',
     '    taches = [f"mahalanobis-egalite/{n}" for n in connus] + [f"plancher/{n}" for n in connus]   # v4 : figées comprises\n'
     '    taches += [f"{CLE_P3_DESCRIPTIF}/{n}/{j}" for n in connus if concept_de[n] in lv1.CONCEPTS_P3 for j in [cr.JEU_I] + doses]\n'),
    ('                                                                        "fiches_t06": ep["fiches"]})\n'
     '        if complete:\n',
     '                                                                        "fiches_t06": ep["fiches"]})\n'
     '        t0 = time.perf_counter()                 # v4 : réextraction de P3, avant toute autre extraction du processus\n'
     '        figees_lues = {concept_de[s.nom]: s for s in sondes if concept_de.get(s.nom) in lv1.CONCEPTS_P3}\n'
     '        reextraction = rx.reextraire(racine, config, figees_lues, lambda cle: lv1._graine(graines, cle), int(config["n_plancher"]))\n'
     '        durees["reextraction_p3_s"] = round(time.perf_counter() - t0, 2)\n'
     '        fichier_figees = rx.ecrire_planchers(racine_sortie, run_t07, reextraction)\n'
     '        lv1.ecrire_resultat(racine_sortie, chemin_m, "reextraction-p3-t07", {**rx.rapport_serialisable(reextraction),\n'
     '                                                                              "fichier": fichier_figees})\n'
     '        if complete:\n'),
    ('        p3 = lv1.charger_planchers_p3(racine, config, [s for s in principales if concept_de.get(s.nom) in lv1.CONCEPTS_P3])\n'
     '        planchers_p3 = {**p3.get("directions", {}), **planchers_neufs}\n',
     '        p3 = charger_planchers_p3(racine, config, [s for s in principales if concept_de.get(s.nom) in lv1.CONCEPTS_P3])\n'
     '        descriptifs_p3 = p3.get("directions", {})                     # v4 : les 200 directions de P3, en descriptif\n'
     '        planchers_figees = {n: x["directions"] for n, x in reextraction["par_sonde"].items() if x["etat"] == "établi"}\n'
     '        echecs_figees = {n: f"plancher neuf de la sonde figée non établi (réextraction de P3) : {x[\'motif\']}"\n'
     '                         for n, x in reextraction["par_sonde"].items() if x["etat"] != "établi"}\n'
     '        planchers_p3 = {**planchers_figees, **planchers_neufs}\n'),
    ("        notation = noter(racine, run_t06, mesures, principales, planchers_p3, jetons, config, graines, couples, extras, textes)\n",
     "        notation = noter(racine, run_t06, mesures, principales, planchers_p3, jetons, config, graines, couples, extras, textes,\n"
     "                         descriptifs_p3=descriptifs_p3, echecs_figees=echecs_figees,\n"
     "                         sources_planchers={n: SOURCE_FIGEES for n in planchers_figees},\n"
     "                         paliers_figees={n: paliers_de(x) for n, x in reextraction[\"par_sonde\"].items() if x[\"etat\"] == \"établi\"})\n"),
    ('                    "garde_identite": identite, "planchers_p3": p3.get("fichier"), "cles_ignorees": ignorees,\n',
     '                    "garde_identite": identite, "planchers_p3": p3.get("fichier"), "cles_ignorees": ignorees,\n'
     '                    "planchers_figees": {"fichier": fichier_figees, "n_plancher": int(config["n_plancher"]),\n'
     '                                         "etats": {n: x["etat"] for n, x in reextraction["par_sonde"].items()},\n'
     '                                         "paliers": {n: paliers_de(x) for n, x in reextraction["par_sonde"].items()},\n'
     '                                         "reextraction": f"diag/{run_t07}/reextraction-p3-t07.json"},\n'),
]

# ------------------------------------------------------------------------------------------ lecture_v3.etape_b → lecture_v4.etape_b
ETAPE_B = [
    ('    """Étape B, v3 : celle de `lecture_v2.etape_b`,',
     '    """Étape B, v4 : celle de `lecture_v3.etape_b` (contrôle de configuration v4), plus la lecture descriptive des 200\n'
     '    directions de P3 des sondes figées (`lecture_planchers_p3`, règle (a) à 95 %, hors jugement). v3 : celle de `lecture_v2.etape_b`,'),
    ('for c in ("intervalle", "descriptif") for n in sondes_lues\n',
     'for c in ("intervalle", "descriptif", CLE_P3_DESCRIPTIF) for n in sondes_lues\n'),
    ("            t, index = lv1.ouvrir_scores(chemin_scores, sondes_lues, refusees)\n",
     "            t, index = lv1.ouvrir_scores(chemin_scores, sondes_lues, refusees)\n"
     "            exiger_nombre_de_directions(t, index, config)        # note 05 (R-2305) : n_plancher directions par plancher décisif\n"),
    ("        jeux, hors, etats_i, etats_ii, motifs, ecarts_base, couples = None, None, [], {}, {}, {}, None\n",
     "        jeux, hors, etats_i, etats_ii, motifs, ecarts_base, couples = None, None, [], {}, {}, {}, None\n"
     "        planchers_p3_lus, index = None, None\n"),
    ("        reserves = list(ep[\"reserves\"]) + (list(derivation[\"reserves\"]) if derivation else [])\n",
     "        reserves = list(ep[\"reserves\"]) + (list(derivation[\"reserves\"]) if derivation else [])\n"
     "        reserves += reserves_plancher_figees(index)            # v4 : palier « carte », principale rapportée\n"),
    ("            couples = lecture_couples(t, index, config, [cr.JEU_I] + ([d for d in cr.DOSES] if oii else []))\n",
     "            couples = lecture_couples(t, index, config, [cr.JEU_I] + ([d for d in cr.DOSES] if oii else []))\n"
     "            planchers_p3_lus = lecture_planchers_p3(t, index, mesures, config, graines,\n"
     "                                                    [cr.JEU_I] + ([d for d in cr.DOSES] if oii else []))\n"),
    ('"couples_figes_descriptif": couples,', '"couples_figes_descriptif": couples, "planchers_p3_descriptif": planchers_p3_lus,'),
]

# --------------------------------------------------------------------------------- passe_blanc_v1.py → passe_blanc_v2.py (module)
PASSE_BLANC = [
    ('"""Passe à blanc de l\'extracteur', '"""v2 (plancher v3 de T0.7) : `passe_blanc_v1.py` à la lettre, sauf la configuration, contrôlée et chargée par\n'
     '`lecture_v4` (n_plancher = 800 admis en mode réel, clé `plancher_figees`), et le nom de la commande\n'
     '(`python -m controle_ia.t07.lecture_v4 passe-blanc`) ; la passe ne lit aucun plancher. v1 : Passe à blanc de l\'extracteur'),
    ('    PYTHONPATH=src python -m controle_ia.t07.lecture_v2 passe-blanc', '    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 passe-blanc'),
    ('COMMANDE = "python -m controle_ia.t07.lecture_v2 passe-blanc"', 'COMMANDE = "python -m controle_ia.t07.lecture_v4 passe-blanc"'),
    ("    from .lecture_v2 import empreinte_canonique, exiger_configuration, extracteur_de_la_course\n",
     "    from .lecture_v2 import empreinte_canonique, extracteur_de_la_course\n"
     "    from .lecture_v4 import exiger_configuration\n"),
    ("    from .lecture_v2 import charger_configuration\n", "    from .lecture_v4 import charger_configuration\n"),
    ('        raise RefusPasse(f"configuration : {e}") from None\n',
     '        raise RefusPasse(f"configuration : {e}") from None\n'
     '    from .reextraction_p3_v1 import controler_avant_ouverture          # CLP3-03 (R-2305) : avant l\'ouverture de l\'étape A\n'
     '    try:\n'
     '        reextraction_p3 = controler_avant_ouverture(racine, config)\n'
     '    except GardeArret as e:\n'
     '        raise RefusPasse(f"réextraction des jetons de P3 non jouable (CLP3-03) : {e}") from None\n'),
    ('        "configuration": {"empreinte_canonique": empreinte_canonique(config), "couches": couches, "registre": str(registre)},\n',
     '        "configuration": {"empreinte_canonique": empreinte_canonique(config), "couches": couches, "registre": str(registre)},\n'
     '        "reextraction_p3": reextraction_p3,\n'),
]

# ------------------------------------------------------------------------------- repli_etapes_v1.py → repli_etapes_v2.py (module)
REPLI = [
    ('"""Repli de l\'étape A (recalcul des activations), **garde d\'ouverture d\'abord**',
     '"""v2 (plancher v3 de T0.7) : `repli_etapes_v1.py` à la lettre, sauf la configuration (contrôle et chargement de\n'
     '`lecture_v4`), l\'étape A appelée après le repli (`lecture_v4.etape_a`) et le nom de la commande\n'
     '(`python -m controle_ia.t07.lecture_v4`). v1 : Repli de l\'étape A (recalcul des activations), **garde d\'ouverture d\'abord**'),
    ("- `repli-recalcul` de `lecture_v2` enchaîne `repli` puis l'étape A (même ordre, même reprise).",
     "- `repli-recalcul` : refusé par `lecture_v4` (code 2, motif écrit) ; jouer `repli-seul`, puis `etape-a-apres-repli`."),
    ("Commandes (par `python -m controle_ia.t07.lecture_v2`)", "Commandes (par `python -m controle_ia.t07.lecture_v4`)"),
    ("    from .lecture_v2 import exiger_configuration, ouvrir\n",
     "    from .lecture_v2 import ouvrir\n    from .lecture_v4 import exiger_configuration\n"),
    ("    from .lecture_v2 import ArretApresManifeste, charger_configuration, etape_a\n",
     "    from .lecture_v4 import ArretApresManifeste, charger_configuration, etape_a\n"),
    ('prog="python -m controle_ia.t07.lecture_v2"', 'prog="python -m controle_ia.t07.lecture_v4"'),
    ("    print(f\"notation scellée, fermée : {r['scores']['chemin']} ; sondes lues {r['index']['sondes_lues']}\")\n",
     "    print(f\"notation scellée, fermée : {r['scores']['chemin']} ; sondes lues {r['index']['sondes_lues']} ; plancher des \"\n"
     "          f\"figées : {r['planchers_figees']['etats']}\")                           # CLP3-10 (R-2305)\n"),
]
