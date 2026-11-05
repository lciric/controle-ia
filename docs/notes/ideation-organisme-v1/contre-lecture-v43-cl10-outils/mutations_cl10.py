"""CL10 : réintroduction de défauts dans la v43 (moteur de CL7 à CL9 ; moteur de CL7 et CL8). Une copie neuve par défaut, remplacement vérifié.

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
    # --- survivants de CL9 (et de CL8), réexprimés sur la v43
    ("M28", "ex-M15 sceau de la consigne en attente non vérifié", IDN,
     "        if not verifier_scelle(chemin_consigne):", "        if False:", None, M_IDN),
    ("N28", "CL39-09 budget e-BH non vérifié", PA, '_exiger_fini(b, f"e-BH : budget de {i!r}")', "pass", None, M_PA),
    ("V27", "CL40-03 tentative scellée même après le départ de la course", LAN,
     'if os.path.exists(os.path.join(sortie, "manifeste-depart.json")):', "if False:", None, M_IDN),
    ("W03", "CL41-01 garde : égalité refusée (> devient >=)", IDN,
     "    if taille > taille_max:\n        raise TailleConsigneRefusee(", "    if taille >= taille_max:\n        raise TailleConsigneRefusee(",
     None, M_IDN),
    ("W07", "CL41-01 lanceur : origine de la taille toujours « defaut »", LAN,
     '"origine": "option" if args.taille_max_consigne_externe\n                                               is not None else "defaut"',
     '"origine": "defaut"', None, M_IDN),
    ("W28", "CL41-06 cœur : seconde vérification de SORTIE retirée (course concurrente)", IDN,
     '        if os.path.exists(sortie):\n            raise FileExistsError(errno.EEXIST, "SORTIE existe déjà (jamais écrasée, R12)", sortie)\n        os.rename(provisoire, sortie)',
     "        os.rename(provisoire, sortie)", None, M_IDN),
    ("W30", "CL41-01 bras : plafond externe donné non vérifié (NaN admis)", IDN,
     '        _exiger_somme("budget_externe_usd", budget_externe_usd)\n', "        pass\n", None, M_IDN),
    ("W35", "CL41-02 bornes non dites aux proposeurs (phrase « refusée » retirée)", IDN,
     'Bornes (une fiche qui les dépasse est refusée) : au plus', 'Bornes : au plus', None, M_IDN),
    ("W35b", "CL42-04 borne de 12 000 par fiche redite aux proposeurs (retour de la phrase retirée)", IDN,
     '{LONGUEUR_MAX_CHAMP} caractères au plus par texte.\\n"',
     '{LONGUEUR_MAX_CHAMP} caractères au plus par texte, 12000 caractères au plus par fiche (JSON compris).\\n"', None, M_IDN),
    ("W36", "CL41-01 bras : classement de repli réécrit à chaque tentative", IDN,
     '        if os.path.exists(os.path.join(sortie, "classement-sans-bras.json")):\n            if verrouiller:',
     '        if False:\n            if verrouiller:', None, M_IDN),
    # --- défauts neufs sur le code ajouté par la v43
    ("X01", "CL40-01 c : clé de reprise sans l'empreinte de la consigne (fichiers changés : Argon repris)", LAN,
     '{"role": role, "modele": modele, "consigne_sha256": consigne_sha256, "identite": identite}',
     '{"role": role, "modele": modele, "identite": identite}', None, M_IDN),
    ("X02", "CL40-01 c : clé de reprise sans l'identité de la commande", LAN,
     '{"role": role, "modele": modele, "consigne_sha256": consigne_sha256, "identite": identite}',
     '{"role": role, "modele": modele, "consigne_sha256": consigne_sha256}', None, M_IDN),
    ("X03", "CL40-01 c : contrôle « réussi » sans regarder le texte ni les problèmes", LAN,
     '            and not lecture.get("problemes") and not lecture.get("non_lance")\n            and str(lecture.get("texte") or "").upper().strip(".!») ") == "OK")',
     '            )', None, M_IDN),
    ("X04", "CL40-01 c : contrôle non lancé tenu pour réussi", LAN,
     ' and not lecture.get("non_lance")\n', '\n', None, M_IDN),
    ("X06", "CL40-01 c : contrôles Claude toujours rejoués", LAN,
     "    a_jouer_claude = [m for m in modeles if m not in repris]", "    a_jouer_claude = list(modeles)", None, M_IDN),
    ("X07", "CL40-01 c : somme de départ compte aussi les contrôles d'Argon repris", LAN,
     "n_controles_claude=len(a_jouer_claude), n_controles_externes=len(a_jouer_externe))",
     "n_controles_claude=len(a_jouer_claude), n_controles_externes=len(prop_ext))", None, M_IDN),
    ("X08", "CL40-01 c : relancable compte deux fois les contrôles Claude joués", LAN,
     'somme_claude=verif["somme_claude"] + budget_controle * (n_c - len(a_jouer_claude)),',
     'somme_claude=verif["somme_claude"] + budget_controle * n_c,', None, M_IDN),
    ("X09", "CL40-01 c : contrôles repris comptés « à refaire »", LAN,
     "reussis_ici = set(repris) | {k for k, c in lectures.items() if controle_reussi(c)}",
     "reussis_ici = {k for k, c in lectures.items() if controle_reussi(c)}", None, M_IDN),
    ("X10", "CL42-01 garde par défaut de la course sans provision (nombre 0)", LAN,
     'args.budget_controle_externe_usd, [budgets[("proposeur_ideation", m)] for _, m in prop_ext], args.nombre,',
     'args.budget_controle_externe_usd, [budgets[("proposeur_ideation", m)] for _, m in prop_ext], 0,', None, M_IDN),
    ("X11", "CL42-01 garde de la course : plus grand plafond au lieu du plus petit", IDN,
     'retenue = min(sessions, key=lambda s: s["taille_max"])', 'retenue = max(sessions, key=lambda s: s["taille_max"])', None, M_IDN),
    ("X12", "CL42-01 cœur : passes non gardées quand la taille est donnée", IDN,
     '            tmax, prov = taille_max_consigne_externe, 0\n            origine = origine_taille_max or "donnée (--taille-max-consigne-externe)"',
     '            return', None, M_IDN),
    ("X13", "CL42-01 cœur : passe gardée sur son plafond sans provision de sortie", IDN,
     "tmax, prov = taille_max_consigne_par_defaut(plafond, provision_sessions, prix_caractere_usd), provision_sessions",
     "tmax, prov = taille_max_consigne_par_defaut(plafond, 0, prix_caractere_usd), 0", None, M_IDN),
    ("X14", "CL42-01 cœur : passes jamais gardées", IDN,
     "        if ext:  # v43 (CL42-01) : avant tout envoi, sans dépense\n            garder_session_externe(etiquette, modele, numero, consigne)\n",
     "", None, M_IDN),
    ("X15", "CL42-04 b : prix du devis non transmis au cœur (passes au prix prudent)", LAN,
     "prix_caractere_usd=idn.prix_caractere(args.prix_entree_usd_par_million_jetons),\n                                    controles_repris=repris)",
     "controles_repris=repris)", None, M_IDN),
    ("X16", "CL42-04 b : prix du devis non transmis au bras", LAN,
     "taille_max_consigne_externe=args.taille_max_consigne_externe_bras,\n                                            prix_caractere_usd=idn.prix_caractere(args.prix_entree_usd_par_million_jetons))",
     "taille_max_consigne_externe=args.taille_max_consigne_externe_bras)", None, M_IDN),
    ("X17", "CL42-05 bras : refus de taille non compté parmi les trois tentatives", IDN,
     "if len(tentatives_non_jouees) + len(tentatives_payees) + len(tentatives_refus_taille) >= MAX_TENTATIVES_BRAS:",
     "if len(tentatives_non_jouees) + len(tentatives_payees) >= MAX_TENTATIVES_BRAS:", None, M_IDN),
    ("X18", "CL42-05 bras : refus de taille sans classement sans bras", IDN,
     "            lever_non_relancable(motif_r, motif_r, e)\n    if deja_externe", "            raise\n    if deja_externe", None, M_IDN),
    ("X19", "CL42-07 : champ trop long non compté comme refus pour taille", IDN,
     'raise FicheTropLongue(f"champ trop long : {cle} ({len(v)} > {maximum})")',
     'raise FicheIdeationInvalide(f"champ trop long : {cle} ({len(v)} > {maximum})")', None, M_IDN),
    ("X20", "CL42-03 : passe 2 maximale mesurée avec une seule fiche", IDN,
     "fiches_precedentes=[fiche_maximale()] * nombre_par_proposeur) if seconde_passe else None)",
     "fiches_precedentes=[fiche_maximale()] * 1) if seconde_passe else None)", None, M_IDN),
    ("X23", "CL42-06 : échec du repli non scellé", IDN,
     '            ecrire_json_scelle(os.path.join(sortie, nom), manifeste(\n                phase="bras-classement-sans-bras-impossible"',
     '            (lambda *a: None)(os.path.join(sortie, nom), manifeste(\n                phase="bras-classement-sans-bras-impossible"', None, M_IDN),
    ("X25", "CL42-05 : provision du juge sans le rapport de sortie", IDN,
     "return int(round(fiches_servies * PROVISION_SORTIE_PAR_NOTE * RAPPORT_SORTIE_ENTREE_PRUDENT))",
     "return int(round(fiches_servies * PROVISION_SORTIE_PAR_NOTE))", None, M_IDN),
    ("X26", "CL42-01 : provision des passes sans le rapport de sortie", IDN,
     "return int(round(nombre * taille_fiche * RAPPORT_SORTIE_ENTREE_PRUDENT))", "return int(round(nombre * taille_fiche))", None, M_IDN),
    ("X27", "CL40-01 c : clé d'Argon de la tentative sans identité (jamais reprise)", LAN,
     '                                                   c["consigne_sha256"], identite_externe)',
     '                                                   c["consigne_sha256"], None)', None, M_IDN),
    ("X28", "CL40-01 c : reprises absentes du journal du cœur", IDN,
     '"controles_repris": dict(controles_repris or {}),\n', '"controles_repris": {},\n', None, M_IDN),
    ("X29", "CL42-05 : refus de taille au bras marqué non compté", IDN,
     "tentative_comptee=True, numero_tentative=numero, relancable=False", "tentative_comptee=False, numero_tentative=numero, relancable=False",
     None, M_IDN),
    ("X30", "CL42-04 b : prix non fini admis par le cœur", IDN,
     '    if not _fini(prix_caractere_usd) or prix_caractere_usd <= 0:  # v43 (CL42-04 b)\n        raise CourseInterrompue(f"prix_caractere_usd : réel fini > 0 (reçu {prix_caractere_usd!r})")\n    tolere_claude',
     '    tolere_claude', None, M_IDN),
    ("X32", "CL40-01 c : contrôles d'Argon toujours rejoués", LAN,
     '    a_jouer_externe = [(e, m) for e, m in prop_ext if f"externe:{e}" not in repris]', "    a_jouer_externe = list(prop_ext)",
     None, M_IDN),
    ("X34", "CL42-03 : « passerait » toujours vrai à la mesure", LAN, '"passerait": ctrl <= taille,', '"passerait": True,', None, M_IDN),
    ("X35", "CL42-05 : garde du bras par défaut sans provision", IDN,
     "            prov = provision_sortie_juge_caracteres(servies)\n", "            prov = 0\n", None, M_IDN),
    ("X36", "CL42-05 lanceur : taille de la course admise au bras", LAN,
     "    if args.bras_rapporte_differe and args.taille_max_consigne_externe is not None:  # v43 (CL42-05)",
     "    if False:  # v43 (CL42-05)", None, M_IDN),
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
with concurrent.futures.ThreadPoolExecutor(max_workers=int(os.environ.get('CL10_TRAVAILLEURS', '6'))) as ex:
    resultats = list(ex.map(jouer, choix))
nom = "mutations-complet.json" if COMPLET else "mutations-premier-passage.json"
with open(os.path.join(DOSSIER, nom), "w", encoding="utf-8") as f:
    json.dump(resultats, f, ensure_ascii=False, indent=1)
for r in resultats:
    print(f"{r['id']:<4} {r['verdict']:<6} {r['duree_s']:>6} s  {r['cible'][:70]:<70} {'; '.join(r['essais_en_echec'][:2])[:120]}")
print("survivantes :", [r["id"] for r in resultats if r["verdict"] == "survit"])
