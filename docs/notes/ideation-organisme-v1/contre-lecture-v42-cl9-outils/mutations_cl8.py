"""Réintroduction de défauts dans la v41 (contre-lecture CL8 ; moteur de CL7). Une copie neuve par défaut, remplacement vérifié.

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
    # --- les dix survivantes de CL7, réexprimées sur le code de la v41
    ("M07", "CL37-02 « rien envoyé » sans condition de processus", IDN,
     'and (journal["non_lance"] or isinstance(e, CleDansEnvironnement)))', ")", None, M_IDN),
    ("M28", "ex-M15 sceau de la consigne en attente non vérifié", IDN,
     "if not verifier_scelle(chemin_consigne):", "if False:", None, M_IDN),
    ("N03", "CL39-01 lanceur : contrôle du bras à 0 dans verifier_reglages", LAN,
     "budget_controle_bras_usd=budget_controle, nombre_par_proposeur=args.nombre)",
     "budget_controle_bras_usd=0.0, nombre_par_proposeur=args.nombre)", None, M_IDN),
    ("N04", "CL39-02 coût externe des tentatives non imputé à la somme", LAN,
     "cout_controles_externes_prevu_usd=cout_tentatives_externe + ",
     "cout_controles_externes_prevu_usd=0.0 * cout_tentatives_externe + ", None, M_IDN),
    ("N05", "CL39-02 coût Claude des tentatives non imputé à la somme", LAN,
     "cout_controles_prevu_usd=cout_tentatives_claude + ", "cout_controles_prevu_usd=0.0 * cout_tentatives_claude + ",
     None, M_IDN),
    ("N07", "CL39-02 coût externe des tentatives non passé au cœur", LAN,
     "cout_externe_deja_engage_usd=cout_controle_externe + cout_tentatives_externe,",
     "cout_externe_deja_engage_usd=cout_controle_externe,", None, M_IDN),
    ("N08", "CL39-02 coût Claude des tentatives non passé au cœur", LAN,
     "cout_deja_engage_usd=cout_controle + cout_tentatives_claude,", "cout_deja_engage_usd=cout_controle,", None, M_IDN),
    ("N13", "CL39-06 contrôle d'Argon sur les pièces seules", LAN,
     'supplement=verif["texte_controle_externe"]', 'supplement=verif["texte_pieces"]', None, M_IDN),
    ("N14", "CL39-06 / CL40-04 marge d'une seule fiche", IDN,
     "fiches_precedentes=[fiche_maximale()] * nombre_par_proposeur)", "fiches_precedentes=[fiche_maximale()])", None, M_IDN),
    ("N28", "CL39-09 budget e-BH non vérifié", PA, '_exiger_fini(b, f"e-BH : budget de {i!r}")', "pass", None, M_PA),
    # --- défauts neufs, sur ce que la v41 ajoute
    ("V01", "CL40-02 contrôle interrompu compté 0", IDN,
     "cout, inconnu = float(budget_usd), True", "cout, inconnu = 0.0, True", None, M_IDN),
    ("V02", "CL40-02 lectures accumulées non jointes à l'interruption", IDN,
     "                e.lecture = lecture\n", "                pass\n", None, M_IDN),
    ("V03", "CL40-02 interruption convertie en ControleRefuse", IDN,
     "if isinstance(e, Exception) and not isinstance(e, (ControleRefuse, CleDansEnvironnement)):",
     "if not isinstance(e, (ControleRefuse, CleDansEnvironnement)):", None, M_IDN),
    ("V04", "CL40-02 clé dans l'environnement comptée au plafond", IDN,
     'avant_lancement = etape == "avant" or (etape == "envoye" and isinstance(e, CleDansEnvironnement))',
     'avant_lancement = etape == "avant"', None, M_IDN),
    ("V05", "CL40-02 coût compté ignoré (déclaré seul)", IDN,
     'c = lecture_modele.get("cout_compte_usd")', "c = None", None, M_IDN),
    ("V06", "CL40-04 antériorités comptées à une", IDN,
     "NOMBRE_ANTERIORITES_COMPTEES = 12", "NOMBRE_ANTERIORITES_COMPTEES = 1", None, M_IDN),
    ("V07", "CL40-04 contrôle sans matériau", IDN,
     "materiau=materiau_lu or None,", "materiau=None,", None, M_IDN),
    ("V08", "CL40-04 ordre : passe 2 d'Argon après les passes Claude", IDN,
     [("                if seconde_passe:\n                    jouer(etiquette, modele, 2)\n", ""),
      ("                if etiquette not in externes_adapt:\n", "                if etiquette not in externes_adapt or numero == 2:\n")],
     None, None, M_IDN),
    ("V09", "CL40-04 contrôle du bras court", IDN,
     "supplement=consignes[etiquette])[modele]", "supplement=None)[modele]", None, M_IDN),
    ("V10", "CL40-01 lanceur : relancable promis", LAN,
     "relancable=relancable, motifs_relance=motifs, sommes_de_cette_course",
     "relancable=True, motifs_relance=motifs, sommes_de_cette_course", None, M_IDN),
    ("V11", "CL40-01 relancable sans le coût Claude de la tentative", LAN,
     'somme_c = verif["somme_claude"] + cout_claude', 'somme_c = verif["somme_claude"]', None, M_IDN),
    ("V12", "CL40-01 relancable sans le coût externe de la tentative", LAN,
     'somme_e = verif["somme_externe"] + cout_externe', 'somme_e = verif["somme_externe"]', None, M_IDN),
    ("V13", "CL40-01 bras : plafond externe absent du calcul de relancable", IDN,
     'if deja_externe + journal["cout_total_usd"] + besoin > plafond_externe + 1e-9:', "if False:", None, M_IDN),
    ("V14", "CL40-03 bras : contrôle repris à 0,2 au lieu du manifeste", IDN,
     '_exiger_somme("budget_controle_bras_usd (manifeste de départ)", (depart.get(',
     '(lambda *a: 0.2)("x", (depart.get(', None, M_IDN),
    ("V15", "CL40-01 tolérances liées", IDN,
     "return bool(tolerer_somme_plafonds or tolerer_somme_claude), bool(tolerer_somme_plafonds or tolerer_somme_externe)",
     "return (bool(tolerer_somme_plafonds or tolerer_somme_claude or tolerer_somme_externe),) * 2", None, M_IDN),
    ("V16", "CL40-05 tentative de contrôle : sceau non vérifié", LAN,
     "        if not verifier_scelle(chemin):\n", "        if False:\n", None, M_IDN),
    ("V17", "CL40-05 tentative de contrôle : coût négatif accepté", LAN,
     "            if not _fini(v) or v < 0:", "            if not _fini(v):", None, M_IDN),
    ("V18", "CL40-05 dossier de contrôle orphelin non vu", LAN,
     " or any(k not in numeros for k in dossiers + compagnons)", "", None, M_IDN),
    ("V19", "CL40-05 tentative du bras : sceau non vérifié", IDN,
     "if not verifier_scelle(os.path.join(sortie, f)):", "if False:", None, M_IDN),
    ("V20", "CL40-05 tentative du bras : coût non fini accepté", IDN,
     "if not _fini(c) or c < 0:", "if False:", None, M_IDN),
    ("V21", "CL40-08 classement sans bras seulement pour CourseInterrompue", IDN,
     '                classement_sans_bras(journal["arret"])\n',
     '                (classement_sans_bras(journal["arret"]) if isinstance(e, CourseInterrompue) else ecrire_manifeste(erreur=journal["arret"]))\n',
     None, M_IDN),
    ("V22", "CL40-02 bras : interruption avant envoi convertie en CourseInterrompue", IDN,
     "            if not isinstance(e, Exception):  # v41 : une interruption reste une interruption (le lanceur rend 2)\n                raise\n",
     "", None, M_IDN),
    ("V23", "CL40-02 bras : seule ControleRefuse rattrapée au contrôle", IDN,
     "except BaseException as e:  # CL37-02, v41 (CL40-02)", "except ControleRefuse as e:  # CL37-02, v41 (CL40-02)",
     None, M_IDN),
    ("V24", "CL40-05 _exiger_somme accepte un négatif", IDN, "if not _fini(b) or b < 0:", "if not _fini(b):", None, M_IDN),
    ("V25", "CL40-05 cœur : contrôle du bras non vérifié", IDN,
     '("budget_controle_bras_usd", budget_controle_bras_usd)):  # v41 (CL40-05)',
     '("budget_total_usd", budget_total_usd)):  # v41 (CL40-05)', 2, M_IDN),
    ("V26", "CL40-03 lanceur : contrôle du bras non passé au cœur", LAN,
     "budget_controle_bras_usd=budget_controle)", "budget_controle_bras_usd=0.2)", None, M_IDN),
    ("V27", "CL40-03 tentative scellée même après le départ de la course", LAN,
     'if os.path.exists(os.path.join(sortie, "manifeste-depart.json")):', "if False:", None, M_IDN),
    ("V28", "CL40-06 α d'e-BH non vérifié", PA, "if alpha is not None:  # v41 (CL40-06)", "if False:  # v41 (CL40-06)", None, M_PA),
    ("V29", "CL40-06 richesse : valeurs non vérifiées", PA,
     '_exiger_valeur(v, f"richesse, unité {i}")', "pass", None, M_PA),
    ("V30", "CL40-06 part de contraste non vérifiée", PA,
     'r = _exiger_fini(parts[cellule], f"part de {cellule!r}")', "r = parts[cellule]", None, M_PA),
    ("V31", "v41 ponderation_plafonnee admet un booléen", PA,
     "or isinstance(m_t, bool) or isinstance(m_max, bool) ", "", None, M_PA),
    ("V32", "CL40-05 relais : champs non vérifiés", LAN,
     "if v is not None and (not _fini(v) or v < 0):", "if False:", None, M_IDN),
    ("V33", "CL40-02 contrôle réussi compté 0", IDN,
     '"cout_compte_usd": float(r.cout_declare_usd or 0.0),', '"cout_compte_usd": 0.0,', None, M_IDN),
    ("V34", "CL40-01 relais : coût de la tentative ignoré", LAN,
     '- float(relais.get("depense_usd") or 0.0) - cout_claude', '- float(relais.get("depense_usd") or 0.0)', None, M_IDN),
    ("V35", "CL40-02 lecture externe imputée à Claude", LAN,
     'lectures[("externe:" + etiquette_externe.get(m, m)) if c.get("role") == "proposeur_ideation" else m] = c',
     "lectures[m] = c", None, M_IDN),
    ("V36", "CL40-04 questions comptées à une", IDN,
     "NOMBRE_QUESTIONS_COMPTEES = 9", "NOMBRE_QUESTIONS_COMPTEES = 1", None, M_IDN),
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
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    resultats = list(ex.map(jouer, choix))
nom = "mutations-complet.json" if COMPLET else "mutations-premier-passage.json"
with open(os.path.join(DOSSIER, nom), "w", encoding="utf-8") as f:
    json.dump(resultats, f, ensure_ascii=False, indent=1)
for r in resultats:
    print(f"{r['id']:<4} {r['verdict']:<6} {r['duree_s']:>6} s  {r['cible'][:70]:<70} {'; '.join(r['essais_en_echec'][:2])[:120]}")
print("survivantes :", [r["id"] for r in resultats if r["verdict"] == "survit"])
