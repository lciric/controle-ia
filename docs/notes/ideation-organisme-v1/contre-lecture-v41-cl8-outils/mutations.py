"""Réintroduction de défauts dans la v40 (contre-lecture CL7). Une copie neuve par défaut, remplacement vérifié.

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

# (identifiant, constat visé, fichier, ancien, nouveau, occurrence (None : unique), modules)
MUTATIONS = [
    # --- les 21 survivantes de CL6 (§ 6), reconstituées d'après leur description
    ("M07", "CL37-02 « rien envoyé » sans condition de processus", IDN,
     'and (journal["non_lance"] or isinstance(e, CleDansEnvironnement)))', ")", None, M_IDN),
    ("M09", "CL37-02 coût des tentatives payées non imputé au plafond du bras", IDN,
     'deja_externe = float(fin["journal"].get("cout_externe_usd", 0.0)) + cout_tentatives',
     'deja_externe = float(fin["journal"].get("cout_externe_usd", 0.0))', None, M_IDN),
    ("M12", "CL37-03 somme externe du cœur désarmée", IDN,
     "        if somme_externe > budget_externe_usd + 1e-9:", "        if False:", None, M_IDN),
    ("M13", "CL37-03 somme Claude de verifier_reglages désarmée", IDN,
     "if somme_claude > budget_total_usd + 1e-9:", "if False:", 1, M_IDN),
    ("M14", "CL37-03 somme externe de verifier_reglages désarmée", IDN,
     "if (proposeurs_externes or juges_externes) and somme_externe > budget_externe_usd + 1e-9:", "if False:", None, M_IDN),
    ("M15", "CL37-03 garde du relais désarmée", LAN,
     "if float(plafond_relais) - float(reserve) - depense < budget_total_usd - plus_petit_juge - 1e-9:", "if False:",
     None, M_IDN),
    ("M16", "CL37-04 taille des pièces vérifiée seulement après le contrôle", IDN,
     "pieces_lues = lire_pieces(pieces, liste, taille_max_pieces)",
     "pieces_lues = lire_pieces(pieces, liste, TAILLE_MAX_PIECES_ABSOLUE)", 1, M_IDN),
    ("M17", "CL37-04 totaux non finis acceptés par le cœur", IDN,
     "or not math.isfinite(b) or b < 0:", "or b < 0:", 2, M_IDN),
    ("M18", "CL37-04 défaut de taille 650 000", LAN, "default=750_000", "default=650_000", None, M_IDN),
    ("M19", "CL37-04 plafonds par session non finis acceptés par verifier_reglages", IDN,
     "if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v <= 0:",
     "if isinstance(v, bool) or not isinstance(v, (int, float)) or v <= 0:", 1, M_IDN),
    ("M20", "CL37-07 interruption : kill au lieu de killpg", ADA,
     "os.killpg(p.pid, signal.SIGKILL)", "os.kill(p.pid, signal.SIGKILL)", 2, M_IDN),
    ("M21", "CL37-08 délai de session 1 800", ADA, "DELAI_SESSION_S = 3600", "DELAI_SESSION_S = 1800", None, M_IDN),
    ("M22", "CL37-08 délai de commande 900", ADA, "DELAI_COMMANDE_S = 1800", "DELAI_COMMANDE_S = 900", None, M_IDN),
    ("M26", "ex-M1 délai : kill au lieu de killpg", ADA,
     "os.killpg(p.pid, signal.SIGKILL)", "os.kill(p.pid, signal.SIGKILL)", 1, M_IDN),
    ("M28", "ex-M15 sceau de la consigne en attente non vérifié", IDN,
     "if not verifier_scelle(chemin_consigne):", "if False:", None, M_IDN),
    ("M29", "ex-M6 course réelle sans Argon non refusée d'abord", LAN,
     'if args.moteur == "claude-sdk" and not args.bras_rapporte_differe and not (prop_ext and juges_ext):  # CL36-03, M29',
     "if False:", None, M_IDN),
    ("M30", "ex-M11 défaut du juge Opus 3,0", LAN, '("juge_ideation", "claude-opus-5-5"): 4.0',
     '("juge_ideation", "claude-opus-5-5"): 3.0', None, M_IDN),
    ("M31", "ex-M17 commande externe avec juge externe seul acceptée hors bras", LAN,
     "if args.commande_externe and not (args.bras_rapporte_differe or args.proposeur_externe):",
     "if args.commande_externe and not (args.bras_rapporte_differe or args.proposeur_externe or args.juge_externe):",
     None, M_IDN),
    ("M34", "PACE gain réel non fini accepté", PP,
     "if gain is not None and (not _nombre(gain) or not math.isfinite(gain)):",
     "if gain is not None and not _nombre(gain):", None, M_PP),
    ("M35", "PACE seuil 1/α par candidat au lieu de l'e-BH", PP,
     "retenues = pa.ebh_pondere(log_e, {n: alpha / m for n in log_e}, alpha)",
     "retenues = {n for n in log_e if log_e[n] >= math.log(1 / alpha)}", None, M_PP),
    ("M36", "PACE δ non vérifié", PP,
     "if delta is None or not _nombre(delta) or not math.isfinite(delta) or not 0.0 < delta < 1.0:",
     "if delta is None:", None, M_PP),
    # --- défauts neufs, sur ce que la v40 ajoute
    ("N01", "CL39-01 contrôle du bras omis dans verifier_reglages", IDN,
     "+ budget_controle_bras_usd * len(list(juges_externes))", "+ 0.0", None, M_IDN),
    ("N02", "CL39-01 contrôle du bras omis au cœur", IDN,
     "+ budget_controle_bras_usd * len(juges_externes)  # v40 (CL39-01)", "+ 0.0", None, M_IDN),
    ("N03", "CL39-01 lanceur : contrôle du bras à 0", LAN,
     "budget_controle_bras_usd=args.budget_controle_usd,", "budget_controle_bras_usd=0.0,", None, M_IDN),
    ("N04", "CL39-02 coût externe des tentatives non imputé à la somme", LAN,
     "cout_controles_externes_prevu_usd=cout_tentatives_externe + ",
     "cout_controles_externes_prevu_usd=0.0 * cout_tentatives_externe + ", None, M_IDN),
    ("N05", "CL39-02 coût Claude des tentatives non imputé à la somme", LAN,
     "cout_controles_prevu_usd=cout_tentatives_claude + ", "cout_controles_prevu_usd=0.0 * cout_tentatives_claude + ",
     None, M_IDN),
    ("N06", "CL39-02 borne des tentatives à quatre", LAN,
     "if len(tentatives) >= idn.MAX_TENTATIVES_BRAS:", "if len(tentatives) > idn.MAX_TENTATIVES_BRAS:", None, M_IDN),
    ("N07", "CL39-02 coût externe des tentatives non passé au cœur", LAN,
     "    cout_controle_externe += cout_tentatives_externe", "    pass", None, M_IDN),
    ("N08", "CL39-02 coût Claude des tentatives non passé au cœur", LAN,
     "    cout_controle += cout_tentatives_claude", "    pass", None, M_IDN),
    ("N09", "CL39-02 tentative toujours « relançable »", LAN,
     "relancable=numero_tentative < idn.MAX_TENTATIVES_BRAS))", "relancable=True))", None, M_IDN),
    ("N10", "CL39-02 coût du contrôle refusé imputé au mauvais total", LAN,
     'externe_e = any(c.get("role") == "proposeur_ideation"', 'externe_e = not any(c.get("role") == "proposeur_ideation"',
     None, M_IDN),
    ("N11", "CL39-07 SORTIE existante refusée seulement après le contrôle", LAN,
     "if os.path.exists(sortie):  # v40 (CL39-07) : refus avant tout contrôle", "if False:", None, M_IDN),
    ("N12", "CL39-07 max_tours non vérifié avant le contrôle", IDN,
     "if isinstance(max_tours, bool) or not isinstance(max_tours, int) or not 1 <= max_tours <= MAX_TOURS_IDEATION:",
     "if False:", None, M_IDN),
    ("N13", "CL39-06 contrôle d'Argon sur les pièces seules", LAN,
     'supplement=verif["texte_controle_externe"]', 'supplement=verif["texte_pieces"]', None, M_IDN),
    ("N14", "CL39-06 marge d'une seule fiche", IDN,
     '("x" * marge_fiche_caracteres + "\\n") * nombre_par_proposeur', '("x" * marge_fiche_caracteres + "\\n")', None, M_IDN),
    ("N15", "CL39-05 session interrompue de la course comptée 0", IDN,
     "journal[cle_total] += plafond", "journal[cle_total] += 0.0", None, M_IDN),
    ("N16", "CL39-04 envoi du bras non marqué", IDN,
     'journal["consigne_envoyee"] = etiquette  # v40', 'pass  # v40', None, M_IDN),
    ("N17", "CL39-04 session interrompue du bras comptée 0", IDN,
     'journal["cout_total_usd"] += plafond', 'journal["cout_total_usd"] += 0.0', None, M_IDN),
    ("N18", "CL39-05 gestionnaires SIGTERM/SIGHUP non posés", LAN,
     "signal.signal(sig, interrompre)", "pass", None, M_IDN),
    ("N19", "CL39-05 interruption non rattrapée par le lanceur", LAN,
     "except KeyboardInterrupt as e:", "except ZeroDivisionError as e:", None, M_IDN),
    ("N20", "CL39-08 contrôle simulé reconnu par égalité stricte", LAN,
     "if consigne.startswith(idn.APPEL_DE_CONTROLE_CONSIGNE):", "if consigne == idn.APPEL_DE_CONTROLE_CONSIGNE:",
     None, M_IDN),
    ("N21", "CL39-02 tentatives jamais relues", LAN, 'r"tentative-\\d+\\.json$"', 'r"tentative-\\d+\\.jsonx$"', None, M_IDN),
    ("N22", "CL39-03 dépense du relais ignorée", LAN, "float(reserve) - depense <", "float(reserve) <", None, M_IDN),
    ("N23", "CL39-09 _fini admet les booléens", PA,
     "if not isinstance(x, numbers.Real) or isinstance(x, bool):", "if not isinstance(x, numbers.Real):", None, M_PA),
    ("N24", "CL39-09 constante NaN acceptée par verifier_coefficients", PA,
     '_exiger_fini(constante, "constante du contraste")  # v40', 'pass  # v40', None, M_PA),
    ("N25", "CL39-09 coefficient non vérifié dans contraste", PA,
     '_exiger_fini(a, f"coefficient de {cellule!r}")', "pass", None, M_PA),
    ("N26", "CL39-09 v avant la borne non vérifié", PA, '_exiger_fini(v, "contraste avant la borne")', "pass", None, M_PA),
    ("N27", "CL39-09 log e-valeur non vérifiée (e-BH)", PA, '_exiger_fini(x, f"e-BH : log e-valeur de {i!r}")', "pass",
     None, M_PA),
    ("N28", "CL39-09 budget e-BH non vérifié", PA, '_exiger_fini(b, f"e-BH : budget de {i!r}")', "pass", None, M_PA),
    ("N29", "CL39-09 trajectoire de la course non vérifiée", PA,
     '_exiger_fini(lw, f"fiche {fiche!r} : trajectoire, instant {t + 1}")', "pass", None, M_PA),
    ("N30", "CL39-09 sans remise : borne [−1 ; 1] perdue", PA,
     '_exiger_valeur(v, f"sans remise, unité {i}")', '_exiger_fini(v, f"sans remise, unité {i}")', None, M_PA),
    ("N31", "CL39-09 α de borne_basse non vérifié", PA, "if not _fini(alpha) or not 0.0 < alpha < 1.0:", "if False:", 2,
     M_PA),
    ("N32", "CL39-09 m de evaluer admis dans [0 ; 1[", PA, "if not _fini(m) or m < 1:", "if not _fini(m) or m < 0:", None,
     M_PA),
    ("N33", "CL39-09 α de evaluer non vérifié", PA, "if not _fini(alpha) or not 0.0 < alpha < 1.0:", "if False:", 1, M_PA),
    ("N34", "CL39-09 borne_basse : borne [−1 ; 1] perdue", PA,
     '_exiger_valeur(v, f"borne basse, unité {i}")', '_exiger_fini(v, f"borne basse, unité {i}")', None, M_PA),
    ("N35", "CL39-10 δ sans écarts ignoré en silence", PP, "elif delta is not None:", "elif False:", None, M_PP),
    ("N36", "CL39-10 témoin « honnête » qui triche", PP,
     'exces = fp_tricheur if (regime == "tricheur" and j == temoin) else 0.0',
     "exces = fp_tricheur if j == temoin else 0.0", None, M_PP),
    ("N37", "CL39-10 n_garde ignoré", PP, "n_garde = n_dev if n_garde is None else n_garde", "n_garde = n_dev", None, M_PP),
]


def appliquer(m, cible):
    ident, _, fichier, ancien, nouveau, occ, _ = m
    chemin = os.path.join(cible, fichier)
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
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
    resultats = list(ex.map(jouer, choix))
nom = "mutations-complet.json" if COMPLET else "mutations-premier-passage.json"
with open(os.path.join(DOSSIER, nom), "w", encoding="utf-8") as f:
    json.dump(resultats, f, ensure_ascii=False, indent=1)
for r in resultats:
    print(f"{r['id']:<4} {r['verdict']:<6} {r['duree_s']:>6} s  {r['cible'][:70]:<70} {'; '.join(r['essais_en_echec'][:2])[:120]}")
print("survivantes :", [r["id"] for r in resultats if r["verdict"] == "survit"])
