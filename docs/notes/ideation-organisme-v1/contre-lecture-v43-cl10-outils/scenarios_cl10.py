"""CL10 : têtes de scenarios_cl9.py (aides), lanceur_cl10.py (pannes pilotées), scénarios B-* (voie β du devis v7 octies),
R-* (CL40-01 c : reprise des contrôles). Scénarios de la contre-lecture CL7 (v39 → v40), repris et étendus en CL8 (v40 → v41) puis CL9 (v41 → v42, options du
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


def lancer(argv, cout_controle_claude=None, attendre=True, arbre=ARBRE, panne=None, casse=None):
    cmd = [sys.executable, "-B", os.path.join(OUTILS, "lanceur_cl10.py"), arbre]
    if cout_controle_claude is not None:
        cmd += ["--cout-controle-claude", str(cout_controle_claude)]
    if panne:
        cmd += ["--panne-coeur", panne]
    if casse:
        cmd += ["--claude-casse", casse]
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
# CL10
TARIFS = {"plafond": {},
          "b83": {"tarif_tout": {"usd_par_car_entree": 8.3e-6 / 4, "usd_par_car_sortie": 41.5e-6 / 4}},
          "haut": {"tarif_tout": {"usd_par_car_entree": 10e-6 / 4, "usd_par_car_sortie": 50e-6 / 4}}}
FICHES = {"petites": {"nombre_fiches": 8}, "reelles": {"nombre_fiches": 8, "gros_champs": 330},
          "max": {"nombre_fiches": 8, "fiches_maximales": True}}
BETA_COURSE = ["--budget-controle-externe-usd", "3.1", "--budget-externe-usd", "12.8",
               "--taille-max-consigne-externe", "1490000", "--prix-entree-usd-par-million-jetons", "8.3"]
BETA_BRAS = ["--taille-max-consigne-externe-bras", "1686000", "--prix-entree-usd-par-million-jetons", "8.3",
             "--budget-externe-usd", "12.8"]


def config_cl10(**k):
    c = os.path.join(D, f"argon-config-{len([f for f in os.listdir(D) if f.startswith('argon-config')])}.json")
    with open(c, "w") as f:
        json.dump(dict(k, journal=JOURNAL_ARGON), f)
    return f"{sys.executable} -I {os.path.join(OUTILS, 'argon_factice_cl10.py')} {c}"


def remplacer(liste, option, valeur):
    liste = list(liste)
    i = liste.index(option)
    liste[i + 1] = valeur
    return liste


def detail_argon(depuis=0):
    return [{"role": a["role"], "controle": a["controle"], "passe": a.get("passe"), "plafond": a["plafond"],
             "entree": a["taille"], "sortie": a.get("taille_sortie"), "cout": a["cout_rendu"],
             "depasse_plafond": a["cout_rendu"] > a["plafond"] + 1e-9} for a in argon_appels()[depuis:]]


def lire_dossier_controle(nom_sortie):
    ctl = os.path.join(D, nom_sortie + "-controle")
    res = {"fichiers": sorted(os.listdir(ctl)) if os.path.isdir(ctl) else None}
    for f in (res["fichiers"] or []):
        if f.endswith(".json"):
            r_ = lire_scelle(os.path.join(ctl, f))["reglages"]
            res[f] = {k: r_.get(k) for k in ("cout_claude_usd", "cout_externe_usd", "relancable", "motifs_relance", "erreur",
                                             "garde_taille", "controles_repris", "controles_a_refaire",
                                             "sommes_de_la_relance_hors_cette_tentative")}
            if isinstance(res[f].get("garde_taille"), dict):
                res[f]["garde_taille"] = {k: res[f]["garde_taille"].get(k) for k in ("taille_caracteres", "taille_max_caracteres")}
    return res


def bilan_course(nom_sortie):
    s = os.path.join(D, nom_sortie)
    b = {"sortie_existe": os.path.exists(s)}
    if os.path.exists(os.path.join(s, "manifeste-depart.json")):
        dep = lire_scelle(os.path.join(s, "manifeste-depart.json"))["reglages"]
        b["somme_des_plafonds"] = dep.get("somme_des_plafonds")
        b["versions_taille"] = dep["versions"].get("taille_max_consigne_externe")
        b["controles_repris"] = dep["versions"].get("controles_repris")
    mf = os.path.join(s, "manifeste-fin.json")
    if os.path.exists(mf):
        j = lire_scelle(mf)["reglages"]["journal"]
        b["fin"] = {k: j.get(k) for k in ("cout_total_usd", "cout_externe_usd", "cout_appels_de_controle_usd",
                                          "cout_appels_de_controle_externes_usd", "arret", "refus_pour_taille_par_proposeur",
                                          "controles_repris")}
        b["fin"]["gardes_taille_sessions"] = [{k: g.get(k) for k in ("passe", "taille_caracteres", "taille_max_caracteres",
                                                                    "provision_sortie_caracteres", "refusee")}
                                              for g in j.get("gardes_taille_sessions") or []]
    return b


def jouer_bras(nom_sortie, cmd, extra):
    s = os.path.join(D, nom_sortie)
    if not os.path.exists(os.path.join(s, "juges-bras-rapporte")):
        return None
    att = attester_bras(s)
    avant = len(argon_appels())
    code, out, err = lancer(args_bras(nom_sortie, att, cmd, extra))
    resume(code, out, err, "bras-" + nom_sortie)
    b = {"code": code, "argon": detail_argon(avant),
         "fichiers": sorted(f for f in os.listdir(s) if f.startswith(("bras-", "manifeste-bras", "classement")))}
    mb = os.path.join(s, "manifeste-bras-rapporte.json")
    if os.path.exists(mb):
        jb = lire_scelle(mb)["reglages"]["journal"]
        b["journal"] = {k: jb.get(k) for k in ("cout_total_usd", "plafond_externe_usd", "arret")}
        b["garde"] = {e: {k: g.get(k) for k in ("taille_caracteres", "taille_max_caracteres", "origine_taille_max")}
                      for e, g in (jb.get("garde_taille") or {}).items()}
    return b


if NOM.startswith("B-"):
    # B-<passes p31|p25>-<tarif>-<fiches>[-x<externe×10>][-g<garde>] : voie (β) du devis v7 octies, pièce 750 000, matériau
    # 350 000, question de 19 caractères, huit fiches, seconde passe, Argon proposeur et juge.
    parties = NOM.split("-")
    passes, tarif_nom, fiches_nom = parties[1], parties[2], parties[3]
    course = list(BETA_COURSE)
    for p_ in parties[4:]:
        if p_.startswith("x"):
            course = remplacer(course, "--budget-externe-usd", str(int(p_[1:]) / 10))
        if p_.startswith("g"):
            course = remplacer(course, "--taille-max-consigne-externe", p_[1:])
    if passes in ("p31", "p30"):
        course += ["--budget", f"proposeur_ideation|gemini-argon={passes[1]}.{passes[2]}"]
    juge33 = "j33" in parties[4:]
    if juge33:  # variante : juge d'Argon à 3,3 (somme 12,8 sans marge), garde du bras 3,3 / 8,3 × 4 millions
        course += ["--budget", "juge_ideation|gemini-argon=3.3"]
    prep = preparer(taille_piece=750_000, taille_materiau=350_000, taille_question=0)
    RAPPORT["tailles_fichiers"] = {k: os.path.getsize(prep[k]) for k in ("p", "m", "q")}
    fiches_cfg = FICHES.get(fiches_nom) or {"nombre_fiches": 8, "gros_champs": int(fiches_nom[1:])}
    cmd = config_cl10(cout="plafond", **TARIFS[tarif_nom], **fiches_cfg)
    RAPPORT["options_course"] = course
    code, out, err = lancer(args_course(prep, "mesure", cmd, course + ["--mesurer-consignes"]))
    try:
        m_ = json.loads(out)
        RAPPORT["mesure"] = {"consignes": {k: m_["consignes"][k] for k in ("consigne_passe_1", "consigne_passe_2_maximale",
                                                                          "consigne_de_controle_externe",
                                                                          "consigne_du_juge_maximale", "controle_du_bras")},
                             "garde_course": {k: m_["garde_course"][k] for k in ("taille_max_caracteres", "origine",
                                                                                "passerait", "cout_entree_controle_usd",
                                                                                "cout_entree_passe_2_maximale_usd")}}
    except ValueError:
        RAPPORT["mesure"] = {"code": code, "erreur": err[-800:]}
    code, out, err = lancer(args_course(prep, "course", cmd, course))
    resume(code, out, err, "lanceur-course")
    RAPPORT["claude"] = {"appels": len(claude_appels(err)), "cout": round(sum(a["cout"] for a in claude_appels(err)), 4),
                         "controles": sum(1 for a in claude_appels(err) if a["controle"])}
    RAPPORT["argon_course"] = detail_argon()
    RAPPORT["controle"] = lire_dossier_controle("course")
    RAPPORT["course"] = bilan_course("course")
    if code == 0:
        bras = list(BETA_BRAS)
        for p_ in parties[4:]:
            if p_.startswith("x"):
                bras = remplacer(bras, "--budget-externe-usd", str(int(p_[1:]) / 10))
        if juge33:
            bras = remplacer(bras, "--taille-max-consigne-externe-bras", "1590000") + ["--budget", "juge_ideation|gemini-argon=3.3"]
        RAPPORT["bras"] = jouer_bras("course", cmd, bras)
    RAPPORT["argon_total"] = round(sum(a["cout_rendu"] for a in argon_appels()), 4)
    RAPPORT["total"] = round(RAPPORT["argon_total"] + RAPPORT["claude"]["cout"], 4)
    s = os.path.join(D, "course")
    RAPPORT["classements"] = sorted(f for f in os.listdir(s) if f.startswith("classement")) if os.path.isdir(s) else []

elif NOM.startswith("BJ-"):
    # Garde du bras donnée (1 686 000, sans provision de sortie) contre défaut (1 166 746 à 8,3) : consigne du juge ≈ 1,5
    # million (pièce de juge de 750 000, fiches d'Argon aux bornes par champ), juge au barème 8,3, notes de ≈ 2 000 caractères.
    prep = preparer(taille_piece=2000, taille_materiau=2000, taille_question=0)
    pj = ecrire("piece-juge.md", ("# Antériorités\n" + "Référence citée. " * 50_000)[:750_000])
    prep["lb"] = os.path.join(D, "liste-blanche-avec-piece-juge.json")
    idn.construire_liste_blanche([prep["p"], prep["q"], prep["m"], prep["t"], pj], prep["lb"])
    cmd_course = config_cl10(cout="plafond", nombre_fiches=8, fiches_maximales=True)
    course = ["--budget-controle-externe-usd", "3.1", "--budget-externe-usd", "13.0", "--taille-max-consigne-externe",
              "1490000", "--prix-entree-usd-par-million-jetons", "8.3", "--budget", "proposeur_ideation|gemini-argon=3.1",
              "--piece-juge", pj]
    code, out, err = lancer(args_course(prep, "course", cmd_course, course))
    resume(code, out, err, "lanceur-course")
    RAPPORT["course"] = bilan_course("course")
    cmd_bras = config_cl10(cout="plafond", justif=400, **TARIFS["b83"])
    bras = ["--prix-entree-usd-par-million-jetons", "8.3", "--budget-externe-usd", "13.0"]
    if NOM == "BJ-option":
        bras += ["--taille-max-consigne-externe-bras", "1686000"]
    RAPPORT["bras"] = jouer_bras("course", cmd_bras, bras)
    RAPPORT["argon_total"] = round(sum(a["cout_rendu"] for a in argon_appels()), 4)
    s = os.path.join(D, "course")
    RAPPORT["classements"] = sorted(f for f in os.listdir(s) if f.startswith("classement")) if os.path.isdir(s) else []

elif NOM.startswith("R-"):
    # CL40-01 (c) : reprise des contrôles réussis. Petites pièces, réglages par défaut du lanceur ; contrôles d'Argon à 0,15,
    # contrôles Claude au plafond (0,2), sessions au plafond.
    import shutil
    prep = preparer()
    panne = os.path.join(D, "PANNE")
    ko = os.path.join(D, "ARGON-KO")
    casse = os.path.join(D, "CLAUDE-CASSE")
    cmd = config_cl10(cout="plafond", cout_controle=0.15, ko_si_existe=ko, nombre_fiches=2)
    etapes = []

    def essai(etiquette, prep_=None):
        avant = len(argon_appels())
        code, out, err = lancer(args_course(prep_ or prep, "course", cmd), panne=panne, casse=casse)
        resume(code, out, err, etiquette)
        ca = claude_appels(err)
        etapes.append({"essai": etiquette, "code": code, "claude_controles": sum(1 for a in ca if a["controle"]),
                       "claude_sessions": sum(1 for a in ca if not a["controle"]), "claude_cout": round(sum(a["cout"] for a in ca), 4),
                       "argon": [(a["controle"], a.get("passe"), a["cout_rendu"]) for a in argon_appels()[avant:]],
                       "fin_stderr": err.splitlines()[-1][:600] if err.splitlines() else ""})

    def changer_piece(suffixe):
        p = ecrire("piece-a.md", "# Pièce A modifiée " + suffixe + "\n" + "Texte de contexte changé. " * 80)
        lb = os.path.join(D, f"liste-blanche-{suffixe}.json")
        idn.construire_liste_blanche([p, prep["q"], prep["m"], prep["t"]], lb)
        return dict(prep, lb=lb, p=p)

    variante = NOM[2:]
    if variante == "reprise-journal-en-argument":  # la commande d'Argon nomme un fichier qui change (son journal)
        cmd = config_argon(factice="argon_factice_cl10.py", cout="plafond", cout_controle=0.15, ko_si_existe=ko, nombre_fiches=2)
        variante = "reprise"
    if variante == "reprise":  # T1 : tout réussit, cœur en panne ; T2 : rien à rejouer
        open(panne, "w").close()
        essai("T1-panne")
        os.remove(panne)
        essai("T2-relance")
    elif variante == "fichiers-changes":  # T1 réussi + panne ; pièce changée ; T2 : Argon rejoué (KO) ; T3 : Argon rejoué, OK
        open(panne, "w").close()
        essai("T1-panne")
        os.remove(panne)
        prep2 = changer_piece("v2")
        open(ko, "w").close()
        essai("T2-piece-changee-argon-ko", prep2)
        os.remove(ko)
        essai("T3-argon-ok", prep2)
    elif variante == "relais-casse":  # T1 réussi + panne ; T2 : Claude cassé à la même « adresse » (simulé)
        open(panne, "w").close()
        essai("T1-panne")
        os.remove(panne)
        open(casse, "w").close()
        essai("T2-claude-casse")
    elif variante == "quatre-tentatives":  # panne à chaque fois : la quatrième est-elle permise ?
        open(panne, "w").close()
        for i in range(4):
            essai(f"T{i + 1}-panne")
    RAPPORT["etapes"] = etapes
    RAPPORT["controle"] = lire_dossier_controle("course")
    RAPPORT["course"] = bilan_course("course")
    RAPPORT["argon_total"] = round(sum(a["cout_rendu"] for a in argon_appels()), 4)

else:
    raise SystemExit("scénario inconnu")

with open(os.path.join(D, "rapport.json"), "w", encoding="utf-8") as f:
    json.dump(RAPPORT, f, ensure_ascii=False, indent=1)
print(json.dumps(RAPPORT, ensure_ascii=False, indent=1))
