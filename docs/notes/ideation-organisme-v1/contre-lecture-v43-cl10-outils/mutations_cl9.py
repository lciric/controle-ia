"""Réintroduction de défauts dans la v42 (contre-lecture CL9 ; moteur de CL7 et CL8). Une copie neuve par défaut, remplacement vérifié.

Usage : python3 -B mutations.py ARBRE_V40 DOSSIER_MUTANTS [--complet ID…]
Premier passage : les modules d'essais qui touchent le fichier muté ; « --complet » : la suite entière (découverte)."""
import concurrent.futures
import json
import os
import shutil
import subprocess
import sys
import time

ARBRE, DOSSIER = sys.argv[1], sys.argv[2]
COMPLET = sys.argv[4:] if len(sys.argv) > 3 and sys.argv[3] == "--complet" else None

IDN, LAN, ADA = "pole/ideation.py", "demonstrations/ideation_v1.py", "pole/adaptateurs.py"
PA, PP = "pole/pari_apparie.py", "pole/porte_pace.py"
M_IDN = ["essais.test_adaptateurs", "essais.test_v7_ideation"]
M_PA = ["essais.test_v7_pari_apparie", "essais.test_v7_engagement_apparie", "essais.test_v7_monde_banque_scores",
        "essais.test_v7_duel", "essais.test_v7_demo_pari_apparie", "essais.test_v7_porte_pace"]
M_PP = ["essais.test_v7_porte_pace"]

# (identifiant, constat visé, fichier, ancien, nouveau, occurrence (None : unique), modules) ; CL8 : « ancien » peut être
# une liste de paires (ancien, nouveau), toutes appliquées (chacune unique)
MUTATIONS = [
    # --- les douze survivants de CL8, réexprimés sur le code de la v42
    ("M28", "ex-M15 sceau de la consigne en attente non vérifié", IDN,
     "if not verifier_scelle(chemin_consigne):", "if False:", None, M_IDN),
    ("N03", "CL39-01 lanceur : contrôle du bras à 0 dans verifier_reglages", LAN,
     "budget_controle_bras_usd=budget_controle, nombre_par_proposeur=args.nombre,",
     "budget_controle_bras_usd=0.0, nombre_par_proposeur=args.nombre,", None, M_IDN),
    ("N04", "CL39-02 coût externe des tentatives non imputé à la somme", LAN,
     "cout_controles_externes_prevu_usd=cout_tentatives_externe + ",
     "cout_controles_externes_prevu_usd=0.0 * cout_tentatives_externe + ", None, M_IDN),
    ("N07", "CL39-02 coût externe des tentatives non passé au cœur", LAN,
     "cout_externe_deja_engage_usd=cout_controle_externe + cout_tentatives_externe,",
     "cout_externe_deja_engage_usd=cout_controle_externe,", None, M_IDN),
    ("N08", "CL39-02 coût Claude des tentatives non passé au cœur", LAN,
     "cout_deja_engage_usd=cout_controle + cout_tentatives_claude,", "cout_deja_engage_usd=cout_controle,", None, M_IDN),
    ("N13", "CL39-06 contrôle d'Argon sur les pièces seules", LAN,
     'supplement=verif["texte_controle_externe"]', 'supplement=verif["texte_pieces"]', None, M_IDN),
    ("N28", "CL39-09 budget e-BH non vérifié", PA, '_exiger_fini(b, f"e-BH : budget de {i!r}")', "pass", None, M_PA),
    ("V12", "CL40-01 relancable sans le coût externe de la tentative", LAN,
     'somme_e = verif["somme_externe"] + cout_externe', 'somme_e = verif["somme_externe"]', None, M_IDN),
    ("V20", "CL40-05 tentative du bras : coût non fini accepté", IDN,
     "if not _fini(c) or c < 0:", "if False:", None, M_IDN),
    ("V27", "CL40-03 tentative scellée même après le départ de la course", LAN,
     'if os.path.exists(os.path.join(sortie, "manifeste-depart.json")):', "if False:", None, M_IDN),
    ("V34", "CL40-01 relais : coût de la tentative ignoré", LAN,
     '- float(relais.get("depense_usd") or 0.0) - cout_claude', '- float(relais.get("depense_usd") or 0.0)', None, M_IDN),
    ("V36", "CL40-04 questions comptées à une (fiche_maximale)", IDN,
     '"questions_servies": ["x" * 80] * MAX_QUESTIONS_SERVIES', '"questions_servies": ["x" * 80] * 1', None, M_IDN),
    # --- défauts neufs, sur ce que la v42 ajoute
    ("W01", "CL41-01 course : garde de taille jamais passée au cœur", LAN,
     "taille_max if prop_ext else None, origine_taille)", "None, origine_taille)", None, M_IDN),
    ("W02", "CL41-01 bras : garde mesurée à 0", IDN,
     'gardes[etiquette] = garde_taille_consigne(f"consigne du juge externe {etiquette!r}", len(consignes[etiquette]),',
     'gardes[etiquette] = garde_taille_consigne(f"consigne du juge externe {etiquette!r}", 0,', None, M_IDN),
    ("W03", "CL41-01 garde : égalité refusée (> devient >=)", IDN,
     "    if taille > taille_max:\n        raise TailleConsigneRefusee(", "    if taille >= taille_max:\n        raise TailleConsigneRefusee(",
     None, M_IDN),
    ("W04", "CL41-01 prix prudent à 3 caractères par jeton", IDN,
     "CARACTERES_PAR_JETON_PRUDENT = 4", "CARACTERES_PAR_JETON_PRUDENT = 3", None, M_IDN),
    ("W05", "CL41-01 défaut de taille sans l'arrondi (999 999)", IDN,
     "/ PRIX_CARACTERE_PRUDENT_USD + 1e-6)", "/ PRIX_CARACTERE_PRUDENT_USD)", None, M_IDN),
    ("W06", "CL41-01 bras : taille donnée à la course ignorée", IDN,
     'elif donnee_course.get("origine") == "option" and _fini(donnee_course.get("valeur")):',
     'elif donnee_course.get("origine") == "opt" and _fini(donnee_course.get("valeur")):', None, M_IDN),
    ("W07", "CL41-01 lanceur : origine de la taille toujours « defaut »", LAN,
     '"origine": "option" if args.taille_max_consigne_externe\n                                               is not None else "defaut"',
     '"origine": "defaut"', None, M_IDN),
    ("W08", "CL41-01 bras : taille donnée au bras ignorée si la course en a une", IDN,
     "        if taille_max_consigne_externe is not None:\n            tmax, origine = taille_max_consigne_externe, \"donnée au bras\"\n        elif",
     "        if False:\n            tmax, origine = taille_max_consigne_externe, \"donnée au bras\"\n        elif", None, M_IDN),
    ("W09", "CL41-01 lanceur : plafond externe jamais transmis au bras", LAN,
     'if getattr(args, "budget_externe_usd_explicite", False) else None)', "if False else None)", None, M_IDN),
    ("W10", "CL41-01 lanceur : plafond externe par défaut (11,6) toujours transmis", LAN,
     'if getattr(args, "budget_externe_usd_explicite", False) else None)', 'if getattr(args, "budget_externe_usd_explicite", True) else None)',
     None, M_IDN),
    ("W11", "CL41-01 bras : tentative payée non relançable sans classement", IDN,
     '            if not relancable:  # v42 (CL41-01) : plus de course sans classement\n                sans_bras_non_relancable(f"tentative {numero} du bras non relançable : " + motif_t)\n',
     "", None, M_IDN),
    ("W12", "CL41-01 bras : tentative non jouée non relançable sans classement", IDN,
     '            if not relancable:  # v42 (CL41-01) : plus de course sans classement\n                sans_bras_non_relancable(f"tentative {numero} du bras non relançable : " + journal["arret"] + suite)\n',
     "", None, M_IDN),
    ("W13", "CL41-01 bras : classement de repli verrouille le bras", IDN,
     "classement_sans_bras(motif, verrouiller=False)", "classement_sans_bras(motif, verrouiller=True)", None, M_IDN),
    ("W14", "CL41-02 questions servies sans borne", IDN,
     "    if len(qs) > MAX_QUESTIONS_SERVIES:", "    if False:", None, M_IDN),
    ("W15", "CL41-02 antériorités sans borne", IDN, "    if len(ant) > MAX_ANTERIORITES:", "    if False:", None, M_IDN),
    ("W16", "CL41-02 fiche sans borne de taille", IDN,
     "    if taille > TAILLE_MAX_FICHE_SERVIE:", "    if False:", None, M_IDN),
    ("W17", "CL41-02 taille servie comptée sans indentation", IDN,
     "return len(json.dumps([vue_servie(fiche)], ensure_ascii=False, indent=1))",
     "return len(json.dumps([vue_servie(fiche)], ensure_ascii=False))", None, M_IDN),
    ("W18", "CL41-02 fiche maximale sans le reste (≈ 11 99x)", IDN,
     "    return _fiche_textes(k, reste)", "    return _fiche_textes(k)", None, M_IDN),
    ("W19", "CL41-03 consigne de contrôle sans la phrase finale", IDN,
     '+ FIN_MATERIAU_CONTROLE + "\\n\\n" + APPEL_DE_CONTROLE_FIN)', '+ FIN_MATERIAU_CONTROLE)', None, M_IDN),
    ("W20", "CL41-03 matériau sans délimiteur de fin", IDN,
     '+ DEBUT_MATERIAU_CONTROLE + "\\n" + supplement + "\\n" + FIN_MATERIAU_CONTROLE + "\\n\\n" + APPEL_DE_CONTROLE_FIN)',
     '+ DEBUT_MATERIAU_CONTROLE + "\\n" + supplement + "\\n\\n" + APPEL_DE_CONTROLE_FIN)', None, M_IDN),
    ("W21", "CL41-07 contrôles Claude avant Argon", LAN,
     [("    try:\n        for e, m in prop_ext:  # CL36-02",
       "    try:\n        controle.update(idn.appel_de_controle(adaptateur, modeles, dossier_tentative, budget_controle, lire_relais,\n                                              exiger_cout=(args.moteur == \"claude-sdk\")))\n        for e, m in prop_ext:  # CL36-02"),
      ("        controle.update(idn.appel_de_controle(adaptateur, modeles, dossier_tentative, budget_controle, lire_relais,\n                                              exiger_cout=(args.moteur == \"claude-sdk\")))\n        cout_controle = ",
       "        cout_controle = ")], None, None, M_IDN),
    ("W22", "CL41-01 bras : contrôle long (retour à la v41)", IDN,
     "exiger_cout=exiger_cout_controle, supplement=None)[modele]",
     "exiger_cout=exiger_cout_controle, supplement=consignes[etiquette])[modele]", None, M_IDN),
    ("W23", "CL41-04 contrôle non court refusé non verrouillé", IDN,
     'if lecture_controle and not lecture_controle.get("consigne_courte", True):',
     'if False and lecture_controle and not lecture_controle.get("consigne_courte", True):', None, M_IDN),
    ("W24", "CL41-04 consigne_courte toujours vrai (chemin normal)", IDN,
     '"consigne_courte": consigne == APPEL_DE_CONTROLE_CONSIGNE,  # v42 (CL41-04)', '"consigne_courte": True,  # v42 (CL41-04)',
     None, M_IDN),
    ("W25", "CL41-05 relais « à neuf » calculé comme gardé", LAN,
     'neuf = float(relais["plafond_usd"]) - float(relais["reserve_par_appel_usd"])\n',
     'neuf = float(relais["plafond_usd"]) - float(relais["reserve_par_appel_usd"]) - float(relais.get("depense_usd") or 0.0) - cout_claude\n',
     None, M_IDN),
    ("W26", "CL41-06 lanceur : SORTIE sans manifeste relançable", LAN,
     "        if os.path.exists(sortie):  # v42 (CL41-06)", "        if False:  # v42 (CL41-06)", None, M_IDN),
    ("W27", "CL41-06 cœur : dossier provisoire laissé sur exception", IDN,
     "        shutil.rmtree(provisoire, ignore_errors=True)", "        pass", None, M_IDN),
    ("W28", "CL41-06 cœur : seconde vérification de SORTIE retirée (course concurrente)", IDN,
     '        if os.path.exists(sortie):\n            raise FileExistsError(errno.EEXIST, "SORTIE existe déjà (jamais écrasée, R12)", sortie)\n        os.rename(provisoire, sortie)',
     "        os.rename(provisoire, sortie)", None, M_IDN),
    ("W29", "CL41-01 bras : refus de taille non scellé", IDN,
     '            ecrire_json_scelle(os.path.join(sortie, f"manifeste-bras-refus-taille-{k}.json"), manifeste(',
     '            (lambda *a: None)(os.path.join(sortie, f"manifeste-bras-refus-taille-{k}.json"), manifeste(', None, M_IDN),
    ("W30", "CL41-01 bras : plafond externe donné non vérifié (NaN admis)", IDN,
     '        _exiger_somme("budget_externe_usd", budget_externe_usd)\n', "        pass\n", None, M_IDN),
    ("W31", "CL41-01 course : garde sur le matériau sans l'enveloppe de contrôle", IDN,
     "    taille_controle = len(consigne_de_controle(texte_controle))", "    taille_controle = len(texte_controle)", None, M_IDN),
    ("W32", "CL41-01 bras : défaut sur le plafond du contrôle (0,2) au lieu du juge", IDN,
     'tmax = taille_max_consigne_par_defaut(budgets[("juge_ideation", modele)])',
     "tmax = taille_max_consigne_par_defaut(budget_controle_usd or 0.2)", None, M_IDN),
    ("W33", "CL41-01 bras non joué non relançable : code 2 au lieu de 5", IDN,
     "            if not relancable and resultat[\"sans_bras\"]:\n                raise SansJugeExterne(\"bras non joué",
     "            if False:\n                raise SansJugeExterne(\"bras non joué", None, M_IDN),
    ("W34", "CL41-02 marge de la passe 2 absente du journal", IDN,
     '"marge_seconde_passe": {"taille_fiche_maximale_servie"', '"marge_seconde_passe_": {"taille_fiche_maximale_servie"', None, M_IDN),
    ("W35", "CL41-02 bornes non dites aux proposeurs", IDN,
     'f"\\n```\\nBornes (une fiche qui les dépasse est refusée) : au plus {MAX_QUESTIONS_SERVIES} questions "',
     'f"\\n```\\nBornes : au plus {MAX_QUESTIONS_SERVIES + 0} questions "', None, M_IDN),
    ("W35b", "CL41-02 borne de 12 000 caractères non dite aux proposeurs", IDN,
     'f"{TAILLE_MAX_FICHE_SERVIE} caractères au plus par fiche (JSON compris).\\n"', '".\\n"', None, M_IDN),
    ("W36", "CL41-01 bras : classement de repli réécrit à chaque tentative", IDN,
     '        if os.path.exists(os.path.join(sortie, "classement-sans-bras.json")):\n            if verrouiller:',
     '        if False:\n            if verrouiller:', None, M_IDN),
]


def appliquer(m, cible):
    ident, _, fichier, ancien, nouveau, occ, _ = m
    chemin = os.path.join(cible, fichier)
    if isinstance(ancien, list):  # CL8 : plusieurs remplacements, chacun unique
        with open(chemin, encoding="utf-8") as f:
            texte = f.read()
        for a, n_ in ancien:
            if texte.count(a) != 1:
                raise RuntimeError(f"{ident} : « {a[:60]} » trouvé {texte.count(a)} fois (attendu 1)")
            texte = texte.replace(a, n_)
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(texte)
        return
    with open(chemin, encoding="utf-8") as f:
        texte = f.read()
    n = texte.count(ancien)
    if occ is None:
        if n != 1:
            raise RuntimeError(f"{ident} : « {ancien[:60]} » trouvé {n} fois (attendu 1)")
        texte = texte.replace(ancien, nouveau)
    else:
        if n < occ:
            raise RuntimeError(f"{ident} : occurrence {occ} absente ({n})")
        i = -1
        for _ in range(occ):
            i = texte.index(ancien, i + 1)
        texte = texte[:i] + nouveau + texte[i + len(ancien):]
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(texte)


def jouer(m):
    ident = m[0]
    cible = os.path.join(DOSSIER, ident + ("-complet" if COMPLET else ""))
    if os.path.exists(cible):
        shutil.rmtree(cible)
    shutil.copytree(ARBRE, cible, ignore=shutil.ignore_patterns("EMPREINTES-*", "LISEZMOI-*", "__pycache__"))
    appliquer(m, cible)
    env = {"PATH": "/usr/bin:/bin", "HOME": "/tmp", "LANG": "C.UTF-8"}
    cmd = ([sys.executable, "-B", "-m", "unittest", "discover", "-s", "essais", "-t", ".", "-p", "test_*.py"] if COMPLET
           else [sys.executable, "-B", "-m", "unittest", *m[6]])
    debut = time.time()
    try:
        p = subprocess.run(cmd, cwd=cible, env=env, capture_output=True, timeout=1500)
        code, sortie = p.returncode, (p.stdout + p.stderr).decode("utf-8", "replace")
    except subprocess.TimeoutExpired as e:
        code, sortie = "délai", ((e.stdout or b"") + (e.stderr or b"")).decode("utf-8", "replace")
    with open(cible + ".sortie.txt", "w", encoding="utf-8") as f:
        f.write(sortie)
    fin = [l for l in sortie.splitlines() if l.startswith(("Ran ", "OK", "FAILED"))]
    echecs = sorted({l.split("(")[0].replace("FAIL: ", "").replace("ERROR: ", "").strip()
                     for l in sortie.splitlines() if l.startswith(("FAIL:", "ERROR:"))})
    shutil.rmtree(cible)
    return {"id": ident, "cible": m[1], "verdict": "survit" if code == 0 else "tuée", "code": code,
            "duree_s": round(time.time() - debut, 1), "fin": fin[-2:], "essais_en_echec": echecs[:6]}


choix = [m for m in MUTATIONS if COMPLET is None or m[0] in COMPLET]
os.makedirs(DOSSIER, exist_ok=True)
for m in choix:  # vérification préalable de chaque remplacement, sur une copie jetable
    t = os.path.join(DOSSIER, "_verif")
    if os.path.exists(t):
        shutil.rmtree(t)
    os.makedirs(os.path.join(t, "pole"))
    os.makedirs(os.path.join(t, "demonstrations"))
    for fch in (IDN, LAN, ADA, PA, PP):
        shutil.copy(os.path.join(ARBRE, fch), os.path.join(t, fch))
    appliquer(m, t)
    shutil.rmtree(t)
with concurrent.futures.ThreadPoolExecutor(max_workers=int(os.environ.get('CL9_TRAVAILLEURS', '6'))) as ex:
    resultats = list(ex.map(jouer, choix))
nom = "mutations-complet.json" if COMPLET else "mutations-premier-passage.json"
with open(os.path.join(DOSSIER, nom), "w", encoding="utf-8") as f:
    json.dump(resultats, f, ensure_ascii=False, indent=1)
for r in resultats:
    print(f"{r['id']:<4} {r['verdict']:<6} {r['duree_s']:>6} s  {r['cible'][:70]:<70} {'; '.join(r['essais_en_echec'][:2])[:120]}")
print("survivantes :", [r["id"] for r in resultats if r["verdict"] == "survit"])
