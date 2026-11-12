"""Scénarios de la contre-lecture CL7 (v39 → v40), joués sur une copie, avec l'Argon factice local.

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


def preparer(taille_piece=2000, taille_materiau=2000):
    p = ecrire("piece-a.md", "# Pièce A\n" + ("Texte de contexte. " * (taille_piece // 19 + 1))[:taille_piece])
    q = ecrire("question.md", "Quelles questions ?")
    m = ecrire("materiau.md", "# Matériau\n" + ("Tour interne. " * (taille_materiau // 14 + 1))[:taille_materiau])
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


def config_argon(**k):
    c = os.path.join(D, f"argon-config-{len(os.listdir(D))}.json")
    with open(c, "w") as f:
        json.dump(k, f)
    return f"{sys.executable} -I {os.path.join(OUTILS, 'argon_factice.py')} {JOURNAL_ARGON} {c}"


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

else:
    raise SystemExit("scénario inconnu")

with open(os.path.join(D, "rapport.json"), "w", encoding="utf-8") as f:
    json.dump(RAPPORT, f, ensure_ascii=False, indent=1)
print(json.dumps(RAPPORT, ensure_ascii=False, indent=1))
