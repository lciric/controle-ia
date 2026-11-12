"""Scénarios de la contre-lecture CL7 (v39 → v40), repris et étendus en CL8 (v40 → v41) puis CL9 (v41 → v42, options du
devis v7 sexies : D-*) ; copie, Argon factice local.

Usage : python3 -B scenarios.py ARBRE DOSSIER_SIMULE NOM_SCENARIO
Tout est écrit sous DOSSIER_SIMULE/NOM_SCENARIO. Aucun réseau."""
import json
import os
import signal
import subprocess
import sys
import time

ARBRE, BASE, NOM = sys.argv[1], sys.argv[2], sys.argv[3]
OUTILS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ARBRE)
from pole import ideation as idn  # noqa: E402

D = os.path.join(BASE, NOM)
os.makedirs(D, exist_ok=False)
JOURNAL_ARGON = os.path.join(D, "argon-journal.jsonl")
RAPPORT = {}

FICHE = {"nom": "Sobre fort", "type": "question",
         "enonce": "Le transfert d'un moniteur vers le diffus suit-il une courbe prédite avant le test ?",
         "loi_predictive": {"espace_instances": "familles", "prediction": "rappel décroît", "signe": "-",
                            "metrique": "rappel à 1 % de fausses alertes"},
         "perte_traduction": "pente", "questions_servies": ["Q4"],
         "avantage": {"source": "programme", "texte": "théorie", "incopiable_parce_que": "carte"},
         "originalite": {"niveau": "transposition", "texte": "rupture"},
         "demande_organisme": {"nature": "ajout", "texte": "générateur"},
         "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"},
         "piege": "artefact", "cosmetique_si": "plates",
         "anteriorite": [{"reference": "réf", "statut": "RAPPORTE"}]}


def ecrire(nom, texte):
    p = os.path.join(D, nom)
    with open(p, "w", encoding="utf-8") as f:
        f.write(texte)
    return p


def preparer(taille_piece=2000, taille_materiau=2000, taille_question=None):
    if taille_question is None:
        p = ecrire("piece-a.md", "# Pièce A\n" + ("Texte de contexte. " * (taille_piece // 19 + 1))[:taille_piece])
    else:  # CL9 : tailles exactes (caractères servis)
        p = ecrire("piece-a.md", ("# Pièce A\n" + "Texte de contexte. " * (taille_piece // 19 + 1))[:taille_piece])
    q = ecrire("question.md", "Quelles questions ?" if not taille_question else
               ("Quelles questions ? " + "Précision de la question. " * (taille_question // 26 + 1))[:taille_question])
    m = ecrire("materiau.md", ("# Matériau\n" + ("Tour interne. " * (taille_materiau // 14 + 1)))[:taille_materiau]
               if taille_question is not None else "# Matériau\n" + ("Tour interne. " * (taille_materiau // 14 + 1))[:taille_materiau])
    t = ecrire("temoins.json", json.dumps({"temoins": [
        {"fiche": dict(FICHE), "attendu": "eligible", "classe": "vrai"},
        {"fiche": dict(FICHE, nom="Verbeux vide", enonce="Long " * 50), "attendu": "ineligible",
         "note_max": {"falsifiabilite": 1}, "classe": "faux_falsifiabilite"},
        {"fiche": dict(FICHE, nom="Assuré occupé", originalite={"niveau": "inedite", "texte": "jamais vu"}),
         "attendu": "ineligible", "note_max": {"originalite": 1}, "classe": "faux_anteriorite"},
        {"fiche": dict(FICHE, nom="Jumeau"), "attendu": "eligible", "jumeau_de": "Sobre fort", "classe": "jumeau"}]},
        ensure_ascii=False))
    lb = os.path.join(D, "liste-blanche.json")
    idn.construire_liste_blanche([p, q, m, t], lb)
    att = os.path.join(D, "attestation-materiau.json")
    idn.ecrire_json_scelle(att, {"lecteur": "Lazar (factice CL7)", "lu_le": "2026-10-29",
                                 "materiau_sha256": {"materiau.md": idn.sha256_fichier(m)}})
    return dict(lb=lb, q=q, p=p, m=m, t=t, att=att)


def config_argon(factice="argon_factice.py", **k):
    c = os.path.join(D, f"argon-config-{len(os.listdir(D))}.json")
    with open(c, "w") as f:
        json.dump(k, f)
    return f"{sys.executable} -I {os.path.join(OUTILS, factice)} {JOURNAL_ARGON} {c}"


def args_course(prep, sortie, commande, extra=()):
    return [os.path.join(D, sortie), "--liste-blanche", prep["lb"], "--question", prep["q"], "--piece", prep["p"],
            "--materiau", prep["m"], "--attestation-materiau", prep["att"], "--seconde-passe", "--temoins", prep["t"],
            "--proposeur-externe", "argon=gemini-argon", "--juge-externe", "argon=gemini-argon",
            "--commande-externe", commande, "--horodatage", "2026-10-29T02:30Z", *extra]


def lancer(argv, cout_controle_claude=None, attendre=True, arbre=ARBRE):
    cmd = [sys.executable, "-B", os.path.join(OUTILS, "lanceur_pire.py"), arbre]
    if cout_controle_claude is not None:
        cmd += ["--cout-controle-claude", str(cout_controle_claude)]
    cmd += ["--", *argv]
    env = {k: v for k, v in os.environ.items() if k in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR")}
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    if not attendre:
        return p
    out, err = p.communicate(timeout=600)
    return p.returncode, out.decode(), err.decode()


def claude_appels(err):
    return [json.loads(l[7:]) for l in err.splitlines() if l.startswith("CLAUDE ")]


def argon_appels():
    if not os.path.exists(JOURNAL_ARGON):
        return []
    with open(JOURNAL_ARGON) as f:
        return [json.loads(l) for l in f]


def resume(code, out, err, etiquette):
    ca = claude_appels(err)
    RAPPORT[etiquette] = {"code": code, "sortie": out[-1500:], "erreur": "\n".join(l for l in err.splitlines()
                                                                               if not l.startswith("CLAUDE "))[-1500:],
                          "claude_appels": len(ca), "claude_cout": round(sum(a["cout"] for a in ca), 4),
                          "argon_appels_cumules": len(argon_appels()),
                          "argon_cout_cumule": round(sum(a["cout_rendu"] for a in argon_appels()), 4)}


def lire_scelle(chemin):
    with open(chemin) as f:
        return json.load(f)


def attester_bras(sortie, etiquette="argon"):
    consigne = os.path.join(sortie, "juges-bras-rapporte", f"traces-{etiquette}", "consigne-en-attente.md")
    att = os.path.join(D, f"att-bras-{os.path.basename(sortie)}.json")
    idn.ecrire_json_scelle(att, {"lecteur": "Lazar (factice CL7)", "lu_le": "2026-10-29",
                                 "fiches_validees_sha256": idn.sha256_fichier(os.path.join(sortie, "fiches-validees.json")),
                                 "consignes_en_attente_sha256": {etiquette: idn.sha256_fichier(consigne)}})
    return att


def args_bras(sortie, att, commande, extra=()):
    return [os.path.join(D, sortie), "--bras-rapporte-differe", "--juge-externe", "argon=gemini-argon",
            "--attestation-lecture-humaine", att, "--commande-externe", commande, *extra]


def vivant(pid):
    try:
        with open(f"/proc/{pid}/status") as f:
            return not any(l.startswith("State:") and "Z" in l for l in f)
    except OSError:
        return False


# ---------------------------------------------------------------------------------------------------------------------
if NOM == "S1-devis-pire-cas":
    # Réglages du devis v7 quinquies (défauts du lanceur) ; tout au plafond, Claude et Argon ; course puis bras.
    prep = preparer()
    cmd = config_argon(cout="plafond")
    code, out, err = lancer(args_course(prep, "course", cmd))
    resume(code, out, err, "course")
    s = os.path.join(D, "course")
    fin = lire_scelle(os.path.join(s, "manifeste-fin.json"))["reglages"]["journal"]
    dep = lire_scelle(os.path.join(s, "manifeste-depart.json"))["reglages"]
    RAPPORT["course_journal"] = {k: fin[k] for k in ("cout_total_usd", "cout_externe_usd", "cout_appels_de_controle_usd",
                                                     "cout_appels_de_controle_externes_usd")}
    RAPPORT["somme_des_plafonds"] = dep["somme_des_plafonds"]
    att = attester_bras(s)
    code, out, err = lancer(args_bras("course", att, cmd))
    resume(code, out, err, "bras")
    jb = lire_scelle(os.path.join(s, "manifeste-bras-rapporte.json"))["reglages"]["journal"]
    RAPPORT["bras_journal"] = {k: jb[k] for k in ("cout_total_usd", "cout_externe_deja_compte_course_usd",
                                                  "plafond_externe_usd", "arret")}
    RAPPORT["argon_total_reel"] = round(sum(a["cout_rendu"] for a in argon_appels()), 6)
    RAPPORT["argon_par_appel"] = [(a["role"], a["controle"], a.get("passe"), a["plafond"], a["taille"]) for a in argon_appels()]
    RAPPORT["classement_ecrit"] = sorted(f for f in os.listdir(s) if f.startswith("classement"))
    RAPPORT["sommes_v41"] = dep["somme_des_plafonds"]

elif NOM == "S2-relance-apres-controle-argon-paye":
    # Contrôle d'Argon refusé (« KO ») à 0,15, contrôles Claude au plafond (0,2) puis réels faibles (0,01) ; relances.
    prep = preparer()
    for cc in (0.2, 0.01, 0.0):
        cmd = config_argon(casse_controle=True, cout=0.15)
        sortie = f"course-cc{cc}"
        res = []
        for i in range(4):
            code, out, err = lancer(args_course(prep, sortie, cmd), cout_controle_claude=cc)
            resume(code, out, err, f"{sortie}-essai{i + 1}")
            res.append(code)
        ctl = os.path.join(D, sortie + "-controle")
        RAPPORT[f"{sortie}-tentatives"] = sorted(f for f in os.listdir(ctl) if f.endswith(".json"))
        for f in RAPPORT[f"{sortie}-tentatives"]:
            r_ = lire_scelle(os.path.join(ctl, f))["reglages"]
            RAPPORT[f"{sortie}-{f}"] = {k: r_.get(k) for k in ("cout_claude_usd", "cout_externe_usd", "relancable",
                                                                 "motifs_relance")}
    # Contrôle d'Argon qui casse sans coût lisible : plafond 2,5 compté ; relance
    cmd = config_argon(casse_au_dela=10)
    for i in range(2):
        code, out, err = lancer(args_course(prep, "course-plafond", cmd), cout_controle_claude=0.01)
        resume(code, out, err, f"course-plafond-essai{i + 1}")
    t1 = os.path.join(D, "course-plafond-controle", "tentative-1.json")
    RAPPORT["tentative-plafond"] = {k: v for k, v in lire_scelle(t1)["reglages"].items() if k.startswith("cout") or k == "relancable"}

elif NOM == "S3-sigterm-pendant-controle-argon":
    prep = preparer()
    pidf = os.path.join(D, "pids.txt")
    cmd = config_argon(dormir_controle_s=60, pid_fichier=pidf)
    p = lancer(args_course(prep, "course", cmd), cout_controle_claude=0.01, attendre=False)
    for _ in range(200):
        if os.path.exists(pidf) and open(pidf).read().strip():
            break
        time.sleep(0.1)
    pids = [int(x) for x in open(pidf).read().split()]
    p.send_signal(signal.SIGTERM)
    out, err = p.communicate(timeout=60)
    resume(p.returncode, out.decode(), err.decode(), "course")
    time.sleep(0.5)
    RAPPORT["vivants_apres"] = {pid: vivant(pid) for pid in pids}
    for pid in pids:
        if vivant(pid):
            os.kill(pid, signal.SIGKILL)
    t1 = os.path.join(D, "course-controle", "tentative-1.json")
    RAPPORT["tentative-1"] = ({k: v for k, v in lire_scelle(t1)["reglages"].items() if k != "lectures"}
                              if os.path.exists(t1) else "absente")

elif NOM in ("S4-sigterm-pendant-passe-argon", "S4b-sighup-pendant-passe-argon"):
    prep = preparer()
    pidf = os.path.join(D, "pids.txt")
    cmd = config_argon(dormir_s=60, pid_fichier=pidf, cout="plafond")
    p = lancer(args_course(prep, "course", cmd), cout_controle_claude=0.01, attendre=False)
    for _ in range(300):
        if os.path.exists(pidf) and open(pidf).read().strip():
            break
        time.sleep(0.1)
    pids = [int(x) for x in open(pidf).read().split()]
    p.send_signal(signal.SIGHUP if NOM.startswith("S4b") else signal.SIGTERM)
    out, err = p.communicate(timeout=60)
    resume(p.returncode, out.decode(), err.decode(), "course")
    time.sleep(0.5)
    RAPPORT["vivants_apres"] = {pid: vivant(pid) for pid in pids}
    for pid in pids:
        if vivant(pid):
            os.kill(pid, signal.SIGKILL)
    j = lire_scelle(os.path.join(D, "course", "manifeste-fin.json"))["reglages"]["journal"]
    RAPPORT["fin"] = {"cout_externe_usd": j["cout_externe_usd"], "cout_total_usd": j["cout_total_usd"],
                      "dernier_appel": {k: j["appels"][-1].get(k) for k in ("role", "statut", "cout_compte_usd", "externe")}}

elif NOM == "S5-taille-du-controle":
    # Grosses fiches d'Argon (champs au maximum de 3 000 caractères) : la passe 2 dépasse-t-elle le contrôle ?
    prep = preparer(taille_piece=20000, taille_materiau=20000)
    for champs in (300, 1500, 3000):
        cmd = config_argon(cout=0.01, gros_champs=champs, nombre_fiches=8)
        avant = len(argon_appels())
        code, out, err = lancer(args_course(prep, f"mesure-{champs}", cmd), cout_controle_claude=0.01)
        resume(code, out, err, f"mesure-{champs}")
        RAPPORT[f"tailles_argon-{champs}"] = [(a["controle"], a.get("passe"), a["taille"]) for a in argon_appels()[avant:]]
    # Argon qui casse au-delà de la taille du contrôle + 1 : le contrôle passe, la passe 2 casse après la passe 1 Claude
    t = RAPPORT["tailles_argon-3000"][0][2]
    cmd = config_argon(cout="plafond", gros_champs=3000, nombre_fiches=8, casse_au_dela=t + 1)
    avant = len(argon_appels())
    code, out, err = lancer(args_course(prep, "casse", cmd))
    resume(code, out, err, "casse-passe2")
    RAPPORT["casse-tailles"] = [(a["controle"], a.get("passe"), a["taille"]) for a in argon_appels()[avant:]]
    j = lire_scelle(os.path.join(D, "casse", "manifeste-fin.json"))["reglages"]["journal"]
    RAPPORT["casse-fin"] = {"cout_total_usd": j["cout_total_usd"], "cout_externe_usd": j["cout_externe_usd"],
                            "arret": j["arret"]}

elif NOM == "S8-sigterm-bras-apres-envoi":
    prep = preparer()
    cmd = config_argon(cout="plafond")
    code, out, err = lancer(args_course(prep, "course", cmd), cout_controle_claude=0.01)
    resume(code, out, err, "course")
    s = os.path.join(D, "course")
    att = attester_bras(s)
    pidf = os.path.join(D, "pids.txt")
    cmd2 = config_argon(dormir_s=60, pid_fichier=pidf, cout="plafond")
    p = lancer(args_bras("course", att, cmd2), attendre=False)
    for _ in range(300):
        if os.path.exists(pidf) and open(pidf).read().strip():
            break
        time.sleep(0.1)
    pids = [int(x) for x in open(pidf).read().split()]
    p.send_signal(signal.SIGTERM)
    out, err = p.communicate(timeout=60)
    resume(p.returncode, out.decode(), err.decode(), "bras-interrompu")
    time.sleep(0.5)
    RAPPORT["vivants_apres"] = {pid: vivant(pid) for pid in pids}
    for pid in pids:
        if vivant(pid):
            os.kill(pid, signal.SIGKILL)
    jb = lire_scelle(os.path.join(s, "manifeste-bras-rapporte.json"))["reglages"]["journal"]
    RAPPORT["bras_journal"] = {k: jb.get(k) for k in ("cout_total_usd", "arret", "consigne_envoyee")}
    RAPPORT["fichiers_course"] = sorted(f for f in os.listdir(s) if f.endswith(".json"))
    if os.path.exists(os.path.join(s, "classement-sans-bras.json")):
        RAPPORT["classement_sans_bras"] = {k: v for k, v in lire_scelle(os.path.join(s, "classement-sans-bras.json")).items()
                                           if k != "lignes"}
    code, out, err = lancer(args_bras("course", att, cmd))
    resume(code, out, err, "bras-relance")

elif NOM == "S7-refus-avant-controle":
    prep = preparer()
    cmd = config_argon(cout=0.01)
    code, out, err = lancer(args_course(prep, "c-tours", cmd, ("--max-tours", "3")))
    resume(code, out, err, "max-tours-3")
    RAPPORT["controle_cree"] = os.path.exists(os.path.join(D, "c-tours-controle"))
    os.makedirs(os.path.join(D, "c-existe"))
    code, out, err = lancer(args_course(prep, "c-existe", cmd))
    resume(code, out, err, "sortie-existe")
    RAPPORT["controle_cree_2"] = os.path.exists(os.path.join(D, "c-existe-controle"))
    code, out, err = lancer(args_course(prep, "c-nan", cmd, ("--budget-externe-usd", "nan")))
    resume(code, out, err, "budget-externe-nan")
    code, out, err = lancer(args_course(prep, "c-inf", cmd, ("--budget-total-usd", "inf", "--tolerer-somme-plafonds")))
    resume(code, out, err, "budget-total-inf-tolere")

elif NOM == "S6-taille-consigne-du-juge":
    # Pièces de juge (antériorité) de 100 000 caractères : la consigne du juge Argon (bras) dépasse-t-elle le contrôle ?
    prep = preparer(taille_piece=20000, taille_materiau=20000)
    pj = ecrire("piece-juge.md", "# Antériorité\n" + ("Résumé d'article. " * 6000)[:100000])
    lb2 = os.path.join(D, "liste-blanche-2.json")
    idn.construire_liste_blanche([prep["p"], prep["q"], prep["m"], prep["t"], pj], lb2)
    prep["lb"] = lb2
    cmd = config_argon(cout=0.01, gros_champs=600, nombre_fiches=8)
    code, out, err = lancer(args_course(prep, "course", cmd, ("--piece-juge", pj)), cout_controle_claude=0.01)
    resume(code, out, err, "course")
    s_ = os.path.join(D, "course")
    att = attester_bras(s_)
    code, out, err = lancer(args_bras("course", att, cmd))
    resume(code, out, err, "bras")
    RAPPORT["tailles_argon"] = [(a["role"], a["controle"], a.get("passe"), a["taille"]) for a in argon_appels()]
    RAPPORT["tailles_claude"] = sorted({(a["role"], a["controle"], a["taille"]) for a in claude_appels(err)})

elif NOM == "S9-controle-du-bras-diverge":
    # --budget-controle-usd 0.1 : verifier_reglages compte 0,1 pour le contrôle du bras, le cœur 0,2 (défaut non passé)
    prep = preparer()
    cmd = config_argon(cout="plafond")
    extra = ("--budget-controle-usd", "0.1", "--budget-externe-usd", "11.1")
    for i in range(2):
        code, out, err = lancer(args_course(prep, "course", cmd, extra))
        resume(code, out, err, f"essai{i + 1}")
    ctl = os.path.join(D, "course-controle")
    RAPPORT["controle"] = sorted(os.listdir(ctl)) if os.path.isdir(ctl) else None
    RAPPORT["sortie_creee"] = os.path.exists(os.path.join(D, "course"))
    RAPPORT["argon_appels"] = [(a["role"], a["controle"], a["cout_rendu"]) for a in argon_appels()]
    if os.path.exists(os.path.join(D, "course", "manifeste-depart.json")):
        s_ = os.path.join(D, "course")
        att = attester_bras(s_)
        code, out, err = lancer(args_bras("course", att, cmd))
        resume(code, out, err, "bras-sans-option")
        jb = lire_scelle(os.path.join(s_, "manifeste-bras-rapporte.json"))["reglages"]["journal"]
        RAPPORT["bras_journal"] = {k: jb.get(k) for k in ("cout_total_usd", "cout_externe_deja_compte_course_usd",
                                                          "plafond_externe_usd", "controle")}
        RAPPORT["argon_total"] = round(sum(a["cout_rendu"] for a in argon_appels()), 6)

elif NOM == "S9b-refus-du-coeur-apres-controles":
    # Contrôles Claude qui rendent « ok » au-dessus de leur plafond (0,5 > 0,2) : verifier_reglages passe, le cœur recalcule
    # avec le coût réel (1,0) et refuse ; tentative scellée ? relance ?
    prep = preparer()
    cmd = config_argon(cout="plafond")
    for i in range(3):
        code, out, err = lancer(args_course(prep, "course", cmd), cout_controle_claude=0.5)
        resume(code, out, err, f"essai{i + 1}")
    ctl = os.path.join(D, "course-controle")
    RAPPORT["controle"] = sorted(os.listdir(ctl)) if os.path.isdir(ctl) else None
    RAPPORT["sortie_creee"] = os.path.exists(os.path.join(D, "course"))
    for f in sorted(x for x in os.listdir(ctl) if x.endswith(".json")):
        r_ = lire_scelle(os.path.join(ctl, f))["reglages"]
        RAPPORT[f] = {k: r_.get(k) for k in ("cout_claude_usd", "cout_externe_usd", "relancable", "motifs_relance", "erreur")}
    RAPPORT["argon_appels"] = [(a["role"], a["controle"], a["cout_rendu"]) for a in argon_appels()]

elif NOM == "S10-controle-du-bras-au-bareme":
    # Doute de l'auteur : contrôle du bras à la consigne réelle du juge sous 0,2. Argon déclare un coût au barème haut
    # du code (BAREME_INCONNU : 10 $/M jetons d'entrée, 50 $/M de sortie) ; la commande ne borne pas son coût.
    grand = len(sys.argv) > 4 and sys.argv[4] == "grand"
    prep = preparer(taille_piece=20000, taille_materiau=20000) if grand else preparer()
    extra = ()
    if grand:
        pj = ecrire("piece-juge.md", "# Antériorité\n" + ("Résumé d'article. " * 6000)[:100000])
        lb2 = os.path.join(D, "liste-blanche-2.json")
        idn.construire_liste_blanche([prep["p"], prep["q"], prep["m"], prep["t"], pj], lb2)
        prep["lb"] = lb2
        extra = ("--piece-juge", pj)
    cmd = config_argon(cout="plafond", **({"gros_champs": 600, "nombre_fiches": 8} if grand else {}))
    code, out, err = lancer(args_course(prep, "course", cmd, extra))
    resume(code, out, err, "course")
    s_ = os.path.join(D, "course")
    att = attester_bras(s_)
    consigne_juge = os.path.join(s_, "juges-bras-rapporte", "traces-argon", "consigne-en-attente.md")
    RAPPORT["taille_consigne_du_juge"] = len(open(consigne_juge, encoding="utf-8").read())
    baremes = {"entree-seule-4c": {"entree": 10.0, "sortie": 50.0, "car_par_jeton": 4, "jetons_sortie": 0},
               "haut-3c-2000s": {"entree": 10.0, "sortie": 50.0, "car_par_jeton": 3, "jetons_sortie": 2000}}
    for nom_b, b in baremes.items():
        # copie fraîche de la course pour chaque barème
        import shutil
        s2 = os.path.join(D, "course-" + nom_b)
        shutil.copytree(s_, s2)
        att2 = attester_bras(s2)
        cmdb = config_argon(cout="plafond", bareme_controle=b, **({"gros_champs": 600, "nombre_fiches": 8} if grand else {}))
        avant = len(argon_appels())
        code, out, err = lancer(args_bras("course-" + nom_b, att2, cmdb))
        resume(code, out, err, f"bras-{nom_b}-essai1")
        RAPPORT[f"bras-{nom_b}-argon"] = [(a["role"], a["controle"], a["taille"], a["plafond"], a["cout_rendu"])
                                         for a in argon_appels()[avant:]]
        RAPPORT[f"bras-{nom_b}-fichiers"] = sorted(f for f in os.listdir(s2) if f.startswith(("bras-", "manifeste-bras",
                                                                                                "classement")))
        for f in RAPPORT[f"bras-{nom_b}-fichiers"]:
            if f.startswith("bras-tentative") and f.endswith(".json"):
                r_ = lire_scelle(os.path.join(s2, f))["reglages"]
                RAPPORT[f"bras-{nom_b}-{f}"] = {"cout_total_usd": r_["journal"]["cout_total_usd"],
                                                "relancable": r_.get("relancable"), "motifs": r_.get("motifs_relance"),
                                                "statut_controle": r_["journal"]["controle"].get("argon", {}).get("statut")}
        code, out, err = lancer(args_bras("course-" + nom_b, att2, cmdb))
        resume(code, out, err, f"bras-{nom_b}-essai2")
        code, out, err = lancer(args_bras("course-" + nom_b, att2, cmdb, ("--budget-controle-usd", "1.0")))
        resume(code, out, err, f"bras-{nom_b}-essai3-controle-1.0")

elif NOM == "S11-controle-du-bras-rend-des-notes":
    # Le juge externe lit la consigne de contrôle (qui porte maintenant toutes les fiches) et rend des notes au lieu de OK
    prep = preparer()
    cmd = config_argon(cout="plafond")
    code, out, err = lancer(args_course(prep, "course", cmd))
    resume(code, out, err, "course")
    s_ = os.path.join(D, "course")
    att = attester_bras(s_)
    cmdn = config_argon(cout="plafond", controle_repond_notes=True, cout_controle=0.05)
    code, out, err = lancer(args_bras("course", att, cmdn))
    resume(code, out, err, "bras-essai1-notes-au-controle")
    RAPPORT["fichiers"] = sorted(f for f in os.listdir(s_) if f.startswith(("bras-", "manifeste-bras", "classement")))
    t1 = os.path.join(s_, "bras-tentative-1.json")
    if os.path.exists(t1):
        r_ = lire_scelle(t1)["reglages"]
        RAPPORT["tentative-1"] = {"relancable": r_.get("relancable"), "erreur": str(r_.get("erreur"))[:300],
                                  "texte_garde": r_["journal"]["controle"].get("argon", {}).get("texte")}
    ctl = os.path.join(s_, "bras-rapporte-controle")
    RAPPORT["fichiers_controle"] = sorted(os.path.relpath(os.path.join(r, f), ctl) for r, _, fs in os.walk(ctl) for f in fs)
    code, out, err = lancer(args_bras("course", att, cmd))
    resume(code, out, err, "bras-essai2-normal")
    RAPPORT["classement_a_trois"] = os.path.exists(os.path.join(s_, "classement.json"))
    RAPPORT["argon"] = [(a["role"], a["controle"], a["taille"], a["cout_rendu"]) for a in argon_appels()]

elif NOM == "S5b-argon-casse-par-la-taille":
    # v41 : passe 2 d'Argon jouée juste après sa passe 1. (a) casse sous la taille du contrôle ; (b) listes longues :
    # la passe 2 dépasse le contrôle ; Argon casse entre les deux.
    prep = preparer(taille_piece=20000, taille_materiau=20000)
    cmd = config_argon(cout=0.01, listes_longues=60, nombre_fiches=8)
    code, out, err = lancer(args_course(prep, "mesure", cmd), cout_controle_claude=0.01)
    resume(code, out, err, "mesure")
    tailles = [(a["controle"], a.get("passe"), a["taille"]) for a in argon_appels()]
    RAPPORT["tailles_mesure"] = tailles
    t_ctl = tailles[0][2]
    t_p2 = max(t for c, p, t in tailles if p == 2)
    RAPPORT["passe2_depasse_controle"] = t_p2 > t_ctl
    for nom_c, limite in (("a-sous-le-controle", t_ctl - 1), ("b-entre-controle-et-passe2", max(t_ctl, t_p2 - 1))):
        avant = len(argon_appels())
        cmdc = config_argon(cout="plafond", listes_longues=60, nombre_fiches=8, casse_au_dela=limite)
        code, out, err = lancer(args_course(prep, "casse-" + nom_c, cmdc))
        resume(code, out, err, "casse-" + nom_c)
        RAPPORT["appels-" + nom_c] = [(a["controle"], a.get("passe"), a["taille"]) for a in argon_appels()[avant:]]
        RAPPORT["claude-" + nom_c] = [(a["role"], a["controle"], a["cout"]) for a in claude_appels(err)]
        mf = os.path.join(D, "casse-" + nom_c, "manifeste-fin.json")
        if os.path.exists(mf):
            j = lire_scelle(mf)["reglages"]["journal"]
            RAPPORT["fin-" + nom_c] = {"cout_total_usd": j["cout_total_usd"], "cout_externe_usd": j["cout_externe_usd"],
                                       "arret": j["arret"]}
        ctl = os.path.join(D, "casse-" + nom_c + "-controle")
        for f in sorted(x for x in os.listdir(ctl) if x.endswith(".json")) if os.path.isdir(ctl) else []:
            r_ = lire_scelle(os.path.join(ctl, f))["reglages"]
            RAPPORT[nom_c + "-" + f] = {k: r_.get(k) for k in ("cout_claude_usd", "cout_externe_usd", "relancable")}

elif NOM == "S3b-sigterm-pendant-controle-du-bras":
    prep = preparer()
    cmd = config_argon(cout="plafond")
    code, out, err = lancer(args_course(prep, "course", cmd), cout_controle_claude=0.01)
    resume(code, out, err, "course")
    s_ = os.path.join(D, "course")
    att = attester_bras(s_)
    pidf = os.path.join(D, "pids.txt")
    cmd2 = config_argon(dormir_controle_s=60, pid_fichier=pidf, cout="plafond")
    p = lancer(args_bras("course", att, cmd2), attendre=False)
    for _ in range(300):
        if os.path.exists(pidf) and open(pidf).read().strip():
            break
        time.sleep(0.1)
    pids = [int(x) for x in open(pidf).read().split()]
    p.send_signal(signal.SIGTERM)
    out, err = p.communicate(timeout=60)
    resume(p.returncode, out.decode(), err.decode(), "bras-controle-interrompu")
    time.sleep(0.5)
    RAPPORT["vivants_apres"] = {pid: vivant(pid) for pid in pids}
    for pid in pids:
        if vivant(pid):
            os.kill(pid, signal.SIGKILL)
    t = sorted(f for f in os.listdir(s_) if f.startswith(("bras-tentative", "manifeste-bras")) and f.endswith(".json"))
    RAPPORT["fichiers_bras"] = t
    for f in t:
        j = lire_scelle(os.path.join(s_, f))["reglages"]
        RAPPORT[f] = {"cout_total_usd": j["journal"]["cout_total_usd"], "relancable": j.get("relancable"),
                      "erreur": str(j.get("erreur"))[:200]}

elif NOM.startswith("D-"):
    # CL9 : options du devis v7 sexies aux tailles du devis (pièces 750 000 + matériau 350 000, huit fiches, seconde passe).
    # NOM = D-<option>-<tarif>[-q<taille question>] ; option ∈ {base, a, b, c} ; tarif ∈ {plafond, devis, haut}
    import shutil
    _, option, tarif_nom, *reste_nom = NOM.split("-")
    tq = int(reste_nom[0][1:]) if reste_nom else None
    tp = 650_000 if option == "b" else 750_000
    prep = preparer(taille_piece=tp, taille_materiau=350_000, taille_question=tq or 0)
    RAPPORT["tailles_fichiers"] = {k: os.path.getsize(prep[k]) for k in ("p", "m", "q")}
    tarifs = {"plafond": {},
              "devis": {"factice": "argon_factice_cl9.py", "tarif_tout": {"usd_par_car_entree": 2.5 / 1.1e6}},
              "haut": {"factice": "argon_factice_cl9.py", "tarif_tout": {"usd_par_car_entree": 10e-6 / 4,
                                                                          "usd_par_car_sortie": 50e-6 / 4}}}
    cfg = dict(cout="plafond", **tarifs[tarif_nom])
    if "factice" not in cfg:
        cfg["factice"] = "argon_factice_cl9.py"
    cmd = config_argon(**cfg)
    extra = {"base": (), "a": ("--budget-controle-externe-usd", "3.0", "--budget-externe-usd", "12.1"),
             "b": ("--taille-max-pieces", "650000"), "c": ("--taille-max-consigne-externe", "1200000")}[option]
    code, out, err = lancer(args_course(prep, "course", cmd, extra))
    resume(code, out, err, "course")
    RAPPORT["course_claude_appels"] = [(a["role"], a["controle"], a["cout"]) for a in claude_appels(err)]
    RAPPORT["argon_course"] = [(a["role"], a["controle"], a.get("passe"), a["plafond"], a["taille"], a["cout_rendu"])
                               for a in argon_appels()]
    ctl = os.path.join(D, "course-controle")
    RAPPORT["controle_fichiers"] = sorted(os.listdir(ctl)) if os.path.isdir(ctl) else None
    for f in (RAPPORT["controle_fichiers"] or []):
        if f.endswith(".json"):
            r_ = lire_scelle(os.path.join(ctl, f))["reglages"]
            RAPPORT["controle-" + f] = {k: r_.get(k) for k in ("cout_claude_usd", "cout_externe_usd", "relancable",
                                                                "motifs_relance", "erreur", "garde_taille", "cout_usd")}
    s = os.path.join(D, "course")
    RAPPORT["sortie_existe"] = os.path.exists(s)
    if os.path.exists(os.path.join(s, "manifeste-depart.json")):
        dep = lire_scelle(os.path.join(s, "manifeste-depart.json"))["reglages"]
        RAPPORT["somme_des_plafonds"] = dep["somme_des_plafonds"]
        RAPPORT["versions_taille"] = {k: dep["versions"].get(k) for k in ("taille_max_consigne_externe", "marge_controle_externe")}
    mf = os.path.join(s, "manifeste-fin.json")
    if os.path.exists(mf):
        j = lire_scelle(mf)["reglages"]["journal"]
        RAPPORT["course_fin"] = {k: j.get(k) for k in ("cout_total_usd", "cout_externe_usd", "cout_appels_de_controle_usd",
                                                       "cout_appels_de_controle_externes_usd", "arret")}
    if code == 0 and os.path.exists(os.path.join(s, "juges-bras-rapporte")):
        att = attester_bras(s)
        avant = len(argon_appels())
        code, out, err = lancer(args_bras("course", att, cmd))
        resume(code, out, err, "bras")
        RAPPORT["argon_bras"] = [(a["role"], a["controle"], a["plafond"], a["taille"], a["cout_rendu"])
                                 for a in argon_appels()[avant:]]
        RAPPORT["bras_fichiers"] = sorted(f for f in os.listdir(s) if f.startswith(("bras-", "manifeste-bras", "classement")))
        if os.path.exists(os.path.join(s, "manifeste-bras-rapporte.json")):
            jb = lire_scelle(os.path.join(s, "manifeste-bras-rapporte.json"))["reglages"]["journal"]
            RAPPORT["bras_journal"] = {k: jb.get(k) for k in ("cout_total_usd", "plafond_externe_usd", "arret", "garde_taille")}
    RAPPORT["argon_total"] = round(sum(a["cout_rendu"] for a in argon_appels()), 4)
    RAPPORT["classements"] = sorted(f for f in os.listdir(s) if f.startswith("classement")) if os.path.isdir(s) else []

else:
    raise SystemExit("scénario inconnu")

with open(os.path.join(D, "rapport.json"), "w", encoding="utf-8") as f:
    json.dump(RAPPORT, f, ensure_ascii=False, indent=1)
print(json.dumps(RAPPORT, ensure_ascii=False, indent=1))
