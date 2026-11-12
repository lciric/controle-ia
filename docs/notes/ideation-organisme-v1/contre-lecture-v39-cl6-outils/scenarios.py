"""Courses simulées CL6 : le lanceur v39 (copie de l'arbre relu), moteur simulé côté Claude, Argon factice local.

Usage : python -I -B scenarios.py COPIE_V39 DOSSIER_SIMULEE PYTHON [S1 S2 …]
Chaque scénario écrit sous DOSSIER_SIMULEE/<Sx>/ et imprime : code de sortie, dernière ligne d'erreur, appels reçus par
l'Argon factice (rôle, contrôle, plafond, taille de la consigne), fichiers écrits.
"""
import json
import os
import shutil
import signal
import subprocess
import sys
import time

COPIE, SIM, PY = sys.argv[1:4]
CHOISIS = set(sys.argv[4:])
LANCEUR = os.path.join(COPIE, "demonstrations", "ideation_v1.py")
ARGON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "argon_factice.py")
sys.path.insert(0, COPIE)
from pole import ideation as idn  # noqa: E402

PREP = os.path.join(SIM, "prep")


def preparer():
    if os.path.exists(os.path.join(PREP, "liste-blanche.json")):
        return
    os.makedirs(PREP, exist_ok=True)
    phrase = "Ce paragraphe de contexte décrit une famille de menaces diffuses et la manière de la mesurer. "
    fichiers = {"question.md": "Quelles questions de recherche affûtées ?",
                "piece-a.md": "# Pièce A\n" + phrase * 2000,          # ≈ 190 000 caractères
                "materiau.md": "# Matériau\n" + phrase * 2500}        # ≈ 237 000 caractères
    for nom, texte in fichiers.items():
        with open(os.path.join(PREP, nom), "w", encoding="utf-8") as f:
            f.write(texte)
    base = {"type": "question", "enonce": "Le transfert d'un moniteur vers le diffus suit-il une courbe prédite ?",
            "loi_predictive": {"espace_instances": "dix familles", "prediction": "rappel décroît", "signe": "-",
                               "metrique": "rappel à 1 % de fausses alertes"},
            "perte_traduction": "résumée par une pente", "questions_servies": ["Q4"],
            "avantage": {"source": "programme", "texte": "théorie explicite", "incopiable_parce_que": "exige la carte"},
            "originalite": {"niveau": "transposition", "texte": "détection de rupture"},
            "demande_organisme": {"nature": "ajout", "texte": "générateur"},
            "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"}, "piege": "artefact de découpe",
            "cosmetique_si": "courbes plates", "anteriorite": [{"reference": "Ramtin 2601.20022", "statut": "RAPPORTE"}]}
    temoins = {"temoins": [
        {"fiche": dict(base, nom="Sobre fort"), "attendu": "eligible", "classe": "vrai"},
        {"fiche": dict(base, nom="Verbeux vide", enonce="Long " * 50), "attendu": "ineligible",
         "note_max": {"falsifiabilite": 1}, "classe": "faux_falsifiabilite"},
        {"fiche": dict(base, nom="Assuré occupé", originalite={"niveau": "inedite", "texte": "jamais vu"}),
         "attendu": "ineligible", "note_max": {"originalite": 1}, "classe": "faux_anteriorite"},
        {"fiche": dict(base, nom="Jumeau"), "attendu": "eligible", "jumeau_de": "Sobre fort", "classe": "jumeau"}]}
    with open(os.path.join(PREP, "temoins.json"), "w", encoding="utf-8") as f:
        json.dump(temoins, f, ensure_ascii=False)
    idn.construire_liste_blanche([os.path.join(PREP, n) for n in ("question.md", "piece-a.md", "materiau.md", "temoins.json")],
                                 os.path.join(PREP, "liste-blanche.json"))
    m = os.path.join(PREP, "materiau.md")
    idn.ecrire_json_scelle(os.path.join(PREP, "attestation-materiau.json"),
                           {"lecteur": "relecteur CL6 (factice)", "lu_le": "2026-10-29", "materiau_sha256": {"materiau.md": idn.sha256_fichier(m)}})


def base(sortie):
    return [PY, "-I", "-B", LANCEUR, sortie, "--liste-blanche", os.path.join(PREP, "liste-blanche.json"),
            "--question", os.path.join(PREP, "question.md"), "--piece", os.path.join(PREP, "piece-a.md"),
            "--temoins", os.path.join(PREP, "temoins.json")]


def argon(journal, *opts):
    return " ".join([PY, "-I", ARGON, "--journal", journal] + list(opts))


ENV = {"PATH": "/usr/bin:/bin", "HOME": "/root", "LANG": "C.UTF-8"}


def lancer(cmd, attente=None):
    r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=attente or 600)
    return r.returncode, r.stdout, r.stderr


def journal_argon(chemin):
    if not os.path.exists(chemin):
        return []
    return [json.loads(l) for l in open(chemin, encoding="utf-8") if l.strip()]


def fichiers(racine):
    out = []
    for d in sorted(p for p in os.listdir(os.path.dirname(racine)) if p.startswith(os.path.basename(racine))):
        for r, _, fs in os.walk(os.path.join(os.path.dirname(racine), d)):
            out += [os.path.relpath(os.path.join(r, f), os.path.dirname(racine)) for f in fs]
    return sorted(out)


def rapport(nom, code, out, err, jr):
    print(f"=== {nom} : code {code}")
    if err.strip():
        print("   erreur :", err.strip().splitlines()[-1][:400])
    if out.strip():
        print("   sortie :", " ".join(out.split())[:400])
    print("   appels Argon :", [(a["role"], "contrôle" if a["controle"] else "session", a["plafond"], a["taille"]) for a in jr])


def scenario_dossier(nom):
    d = os.path.join(SIM, nom)
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    return d


DEVIS = ["--seconde-passe", "--materiau", os.path.join(PREP, "materiau.md"),
         "--attestation-materiau", os.path.join(PREP, "attestation-materiau.json"),
         "--proposeur-externe", "argon=gemini-argon", "--juge-externe", "argon-j=gemini-argon"]


def S1():
    """Réglages du devis v7 quater (deux passes, Argon proposeur et juge, contrôle à 2,5) : refus avant tout appel ?"""
    d = scenario_dossier("S1")
    j = os.path.join(d, "argon.jsonl")
    code, out, err = lancer(base(os.path.join(d, "course")) + DEVIS + ["--commande-externe", argon(j)])
    rapport("S1 devis v7 quater tel quel", code, out, err, journal_argon(j))
    print("   fichiers :", fichiers(os.path.join(d, "course")))


def S2():
    """Contrôle d'Argon à 0,5 (somme externe 9,0 acceptée), Argon déclare son plafond à chaque session : le bras passe-t-il ?"""
    d = scenario_dossier("S2")
    j = os.path.join(d, "argon.jsonl")
    sortie = os.path.join(d, "course")
    cmd = argon(j, "--cout-plein", "--cout-controle", "0.5")
    code, out, err = lancer(base(sortie) + DEVIS + ["--commande-externe", cmd, "--budget-controle-externe-usd", "0.5"])
    rapport("S2a course, contrôle 0,5, Argon au plafond", code, out, err, journal_argon(j))
    fin = json.load(open(os.path.join(sortie, "manifeste-fin.json")))["reglages"]["journal"]
    print("   cout_externe_usd au manifeste de fin :", fin["cout_externe_usd"])
    att = os.path.join(d, "attestation-lecture.json")
    consigne = os.path.join(sortie, "juges-bras-rapporte", "traces-argon-j", "consigne-en-attente.md")
    idn.ecrire_json_scelle(att, {"lecteur": "relecteur CL6 (factice)", "lu_le": "2026-10-29",
                                 "fiches_validees_sha256": idn.sha256_fichier(os.path.join(sortie, "fiches-validees.json")),
                                 "consignes_en_attente_sha256": {"argon-j": idn.sha256_fichier(consigne)}})
    code, out, err = lancer([PY, "-I", "-B", LANCEUR, sortie, "--bras-rapporte-differe", "--attestation-lecture-humaine", att,
                             "--juge-externe", "argon-j=gemini-argon", "--commande-externe", cmd])
    rapport("S2b bras différé", code, out, err, journal_argon(j))
    print("   classement écrit :", [f for f in os.listdir(sortie) if f.startswith("classement")],
          "; manifestes du bras :", [f for f in os.listdir(sortie) if f.startswith(("manifeste-bras", "bras-tentative"))])


def S3():
    """Moteur simulé, proposeur et juge externes SANS commande (adaptateur scripté) : la répétition passe-t-elle ?"""
    d = scenario_dossier("S3")
    code, out, err = lancer(base(os.path.join(d, "course")) + ["--proposeur-externe", "argon=gemini-argon",
                                                               "--juge-externe", "argon-j=gemini-argon"])
    rapport("S3 simulé sans commande (v39)", code, out, err, [])


def S4():
    """Signal d'arrêt à l'orchestrateur pendant une session d'Argon : SIGINT puis SIGTERM (R10 : arrêt par identifiant)."""
    for sig in (signal.SIGINT, signal.SIGTERM):
        d = scenario_dossier(f"S4-{sig.name}")
        j, pids = os.path.join(d, "argon.jsonl"), os.path.join(d, "pids.txt")
        p = subprocess.Popen(base(os.path.join(d, "course")) + ["--proposeur-externe", "argon=gemini-argon",
                                                                "--juge-externe", "argon-j=gemini-argon",
                                                                "--commande-externe", argon(j, "--dormir", "40", "--pids", pids)],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=ENV)
        for _ in range(200):
            if os.path.exists(pids) and open(pids).read().strip():
                break
            time.sleep(0.1)
        enfant, petit = map(int, open(pids).read().split())
        os.kill(p.pid, sig)
        out, err = p.communicate(timeout=60)
        time.sleep(0.5)

        def vivant(pid):
            try:
                etat = [l for l in open(f"/proc/{pid}/status") if l.startswith("State:")][0]
                return "Z" not in etat
            except OSError:
                return False
        print(f"=== S4 {sig.name} à l'orchestrateur (pid {p.pid}) : code {p.returncode} ; Argon factice (pid {enfant}) vivant : "
              f"{vivant(enfant)} ; son petit-enfant (pid {petit}) vivant : {vivant(petit)}")
        print("   erreur :", (err.strip().splitlines() or [""])[-1][:200])
        mf = os.path.join(d, "course", "manifeste-fin.json")
        if os.path.exists(mf):
            jr = json.load(open(mf))["reglages"]["journal"]
            print("   manifeste de fin : arret =", jr["arret"], "; cout_externe_usd =", jr["cout_externe_usd"],
                  "; appels comptés :", [(a["etiquette"], a["cout_compte_usd"]) for a in jr["appels"]])
        else:
            print("   manifeste de fin : absent")
        for pid in (enfant, petit):  # R10 : arrêt par identifiant de processus
            if vivant(pid):
                os.kill(pid, signal.SIGKILL)
                print(f"   arrêté par le relecteur : pid {pid}")


def S5():
    """Contrôle d'Argon à la taille réelle refusé (quota simulé : sortie 3 au-delà de 1 000 caractères) : coût consigné ?
    Puis relance dans la même SORTIE."""
    d = scenario_dossier("S5")
    j = os.path.join(d, "argon.jsonl")
    sortie = os.path.join(d, "course")
    cmd = base(sortie) + DEVIS + ["--commande-externe", argon(j, "--casse-au-dela", "1000"), "--budget-controle-externe-usd", "0.5"]
    for essai in (1, 2):
        code, out, err = lancer(cmd)
        rapport(f"S5 tentative {essai}", code, out, err, journal_argon(j))
    fs = fichiers(sortie)
    print("   fichiers :", fs)
    trouve = [f for f in fs if os.path.isfile(os.path.join(d, f)) and "0.5" in open(os.path.join(d, f), errors="replace").read()]
    print("   fichiers qui mentionnent le plafond compté (0.5) :", trouve)


def S6():
    """Argon casse au-delà de 300 000 caractères : le contrôle (pièces ≈ 190 000) passe ; la passe 2 (pièces + matériau) ?"""
    d = scenario_dossier("S6")
    j = os.path.join(d, "argon.jsonl")
    sortie = os.path.join(d, "course")
    code, out, err = lancer(base(sortie) + DEVIS + ["--commande-externe", argon(j, "--casse-au-dela", "300000"),
                                                    "--budget-controle-externe-usd", "0.5"])
    rapport("S6 Argon casse en passe 2", code, out, err, journal_argon(j))
    jr = json.load(open(os.path.join(sortie, "manifeste-fin.json")))["reglages"]["journal"]
    print("   journal :", [(a["etiquette"], a["statut"], a["cout_compte_usd"]) for a in jr["appels"]],
          "; cout_total_usd (Claude) =", jr["cout_total_usd"], "; arret =", jr["arret"][:120])


def S7():
    """Refus du cœur APRÈS les contrôles : SORTIE déjà existante, puis --max-tours 3."""
    d = scenario_dossier("S7")
    j = os.path.join(d, "argon.jsonl")
    sortie = os.path.join(d, "course")
    cmd = base(sortie) + ["--proposeur-externe", "argon=gemini-argon", "--juge-externe", "argon-j=gemini-argon",
                          "--commande-externe", argon(j, "--cout-controle", "0.3")]
    code, out, err = lancer(cmd)
    rapport("S7a première course", code, out, "", journal_argon(j))
    n = len(journal_argon(j))
    code, out, err = lancer(cmd)
    rapport("S7b même SORTIE", code, out, err, journal_argon(j)[n:])
    n = len(journal_argon(j))
    cmd2 = [x if x != sortie else sortie + "-mt" for x in cmd] + ["--max-tours", "3"]
    code, out, err = lancer(cmd2)
    rapport("S7c --max-tours 3", code, out, err, journal_argon(j)[n:])


for nom in ("S1", "S2", "S3", "S4", "S5", "S6", "S7"):
    if not CHOISIS or nom in CHOISIS:
        preparer()
        globals()[nom]()
