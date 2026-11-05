"""CL6 : réintroduit les défauts un par un, chacun dans une copie neuve de l'arbre v39, et lance les essais.

Usage : python -I -B mutations.py ARBRE_V39 DOSSIER_COPIES PYTHON [complet] [ID ...]
Sans « complet » : sous-ensemble des modules d'essais qui touchent le fichier muté ; avec « complet » : suite entière.
Une mutation est « tuée » si au moins un essai échoue ; « non appliquée » si le texte attendu n'est pas trouvé.
Les noms des copies ne contiennent jamais « argon » (essais:694 cherche ce mot dans un chemin relatif depuis la v38).
"""
import concurrent.futures
import os
import re
import shutil
import subprocess
import sys
import time

IDEATION = "pole/ideation.py"
LANCEUR = "demonstrations/ideation_v1.py"
ADAPT = "pole/adaptateurs.py"
PARI = "pole/pari_apparie.py"
PACE = "pole/porte_pace.py"
E_IDEATION = ["essais.test_v7_ideation"]
E_ADAPT = ["essais.test_adaptateurs", "essais.test_v7_plomberie", "essais.test_v7_ideation"]  # ordre : voir dépendance d ordre
E_PARI = ["essais.test_v7_pari_apparie", "essais.test_v7_porte_pace", "essais.test_v7_engagement_apparie",
          "essais.test_v7_monde_banque_scores", "essais.test_v7_demo_pari_apparie", "essais.test_v7_duel"]
E_PACE = ["essais.test_v7_porte_pace"]

# (id, constat, fichier, ancien, nouveau, occurrence (0 : unique exigée ; k : k-ième), essais)
MUTATIONS = [
    ("M01", "CL37-01 Argon en tête de passe", IDEATION,
     "tous_proposeurs = [(e, m) for e, m, _ in proposeurs_externes] + list(proposeurs)  # v38",
     "tous_proposeurs = list(proposeurs) + [(e, m) for e, m, _ in proposeurs_externes]  # v38", 0, E_IDEATION),
    ("M02", "CL37-01 contrôle à la taille réelle", LANCEUR,
     'supplement=verif["texte_pieces"])[m]', "supplement=None)[m]", 0, E_IDEATION),
    ("M03", "CL37-01 rôle proposeur au contrôle", LANCEUR,
     'exiger_cout=bool(args.commande_externe), role="proposeur_ideation",',
     'exiger_cout=bool(args.commande_externe), role="juge_ideation",', 0, E_IDEATION),
    ("M04", "CL37-01 coût du contrôle externe compté", LANCEUR,
     'cout_controle_externe += float(lecture_ext.get("cout_declare_usd") or 0.0)', "cout_controle_externe += 0.0", 0,
     E_IDEATION),
    ("M05", "CL37-01 contrôle externe retiré", LANCEUR,
     "for e, m in prop_ext:  # CL36-02 / CL37-01", "for e, m in []:  # CL36-02 / CL37-01", 0, E_IDEATION),
    ("M06", "CL37-02 coût du contrôle refusé compté (bras)", IDEATION,
     'journal["cout_total_usd"] += float(lecture_controle.get("cout_declare_usd") or 0.0)\n                journal["non_lance"]',
     'journal["cout_total_usd"] += 0.0\n                journal["non_lance"]', 0, E_IDEATION),
    ("M07", "CL37-02 « rien envoyé » exige « aucun processus parti »", IDEATION,
     'journal["cout_total_usd"] <= 0\n                       and (journal["non_lance"] or isinstance(e, CleDansEnvironnement)))',
     'journal["cout_total_usd"] <= 0)', 0, E_IDEATION),
    ("M08", "CL37-02 au plus trois tentatives", IDEATION,
     "if len(tentatives_non_jouees) + len(tentatives_payees) >= MAX_TENTATIVES_BRAS:",
     "if len(tentatives_non_jouees) + len(tentatives_payees) >= MAX_TENTATIVES_BRAS + 100:", 0, E_IDEATION),
    ("M09", "CL37-02 coût des tentatives imputé au plafond externe", IDEATION,
     'deja_externe = float(fin["journal"].get("cout_externe_usd", 0.0)) + cout_tentatives',
     'deja_externe = float(fin["journal"].get("cout_externe_usd", 0.0))', 0, E_IDEATION),
    ("M10", "CL37-02 tentatives payées dans la borne", IDEATION,
     "if len(tentatives_non_jouees) + len(tentatives_payees) >= MAX_TENTATIVES_BRAS:",
     "if len(tentatives_non_jouees) >= MAX_TENTATIVES_BRAS:", 0, E_IDEATION),
    ("M11", "CL37-03 somme Claude refusée au cœur", IDEATION,
     "if somme_claude > budget_total_usd + 1e-9:", "if False and somme_claude > budget_total_usd + 1e-9:", 3, E_IDEATION),
    ("M12", "CL37-03 somme externe refusée au cœur", IDEATION,
     "        if somme_externe > budget_externe_usd + 1e-9:", "        if False:", 0, E_IDEATION),
    ("M13", "CL37-03 somme Claude refusée par verifier_reglages", IDEATION,
     "if somme_claude > budget_total_usd + 1e-9:", "if False and somme_claude > budget_total_usd + 1e-9:", 1, E_IDEATION),
    ("M14", "CL37-03 somme externe refusée par verifier_reglages", IDEATION,
     "if (proposeurs_externes or juges_externes) and somme_externe > budget_externe_usd + 1e-9:", "if False:", 1,
     E_IDEATION),
    ("M15", "CL37-03 cohérence relais lue par le lanceur", LANCEUR,
     "if float(plafond_relais) - float(reserve) < args.budget_total_usd - plus_petit_juge - 1e-9:", "if False:", 0,
     E_IDEATION),
    ("M16", "CL37-04 verifier_reglages avant tout contrôle", LANCEUR,
     "    verif = idn.verifier_reglages(\n",
     "    idn.appel_de_controle(adaptateur, sorted({m for _, m in proposeurs} | {m for _, m in juges}), sortie_controle + "
     "\"-avant\", args.budget_controle_usd, lire_relais, exiger_cout=(args.moteur == \"claude-sdk\"))\n"
     "    verif = idn.verifier_reglages(\n", 0, E_IDEATION),
    ("M17", "CL37-04 totaux finis au cœur (math.isfinite)", IDEATION,
     "if isinstance(b, bool) or not isinstance(b, (int, float)) or not math.isfinite(b) or b < 0:",
     "if isinstance(b, bool) or not isinstance(b, (int, float)) or b < 0:", 4, E_IDEATION),
    ("M18", "CL37-04 défaut --taille-max-pieces 750 000", LANCEUR,
     'a.add_argument("--taille-max-pieces", type=int, default=750_000,',
     'a.add_argument("--taille-max-pieces", type=int, default=400_000,', 0, E_IDEATION),
    ("M19", "CL37-04 plafonds par session finis dans verifier_reglages", IDEATION,
     "if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v <= 0:",
     "if isinstance(v, bool) or not isinstance(v, (int, float)) or v <= 0:", 1, E_IDEATION),
    ("M20", "CL37-07 groupe arrêté sur interruption", ADAPT,
     "        except BaseException:  # v38 (CL37-07) : interruption de l'orchestrateur → la commande ne survit pas\n"
     "            try:\n                os.killpg(p.pid, signal.SIGKILL)\n            except OSError:\n                pass\n"
     "            raise\n", "", 0, E_ADAPT),
    ("M21", "CL37-08 délai de session 3 600", ADAPT, "DELAI_SESSION_S = 3600", "DELAI_SESSION_S = 1800", 0, E_ADAPT),
    ("M22", "CL37-08 délai de commande 1 800 (adaptateur et lanceur)", ADAPT,
     "DELAI_COMMANDE_S = 1800  # v38 (CL37-08)", "DELAI_COMMANDE_S = 900  # v38 (CL37-08)", 0, E_ADAPT),
    ("M23", "CL37-05 (ex-M5) juge externe oublié sur course réelle", IDEATION,
     'if moteur == "claude-sdk" and not (juges_externes and proposeurs_externes):  # v37 (CL36-03)',
     'if moteur == "claude-sdk" and not (proposeurs_externes):  # v37 (CL36-03)', 2, E_IDEATION),
    ("M24", "CL37-05 (ex-M12) médiane à trois juges", IDEATION,
     "agg = statistics.mean if nj <= 2 else statistics.median", "agg = statistics.mean", 0, E_IDEATION),
    ("M25", "CL37-05 (ex-M13) sceau de l'attestation", IDEATION,
     "    if not verifier_scelle(chemin):\n        raise CourseInterrompue(f\"attestation non scellée",
     "    if False:\n        raise CourseInterrompue(f\"attestation non scellée", 0, E_IDEATION),
    ("M26", "CL35-13 (ex-M1) groupe arrêté au délai (killpg → kill)", ADAPT,
     "os.killpg(p.pid, signal.SIGKILL)  # CL35-13", "os.kill(p.pid, signal.SIGKILL)  # CL35-13", 0, E_ADAPT),
    ("M27", "CL36-01 (ex-M3) coût 0 sur commande introuvable", ADAPT,
     'return Resultat("", [], 0.0, "erreur", "commande externe non lancée ("',
     'return Resultat("", [], 0.2, "erreur", "commande externe non lancée ("', 0, E_ADAPT),
    ("M28", "CL36-01 (ex-M15) condition d'écriture de reponse.md (bras)", IDEATION,
     'if r.statut == "ok" or cout > 0 or texte:  # CL36-01', "if True:  # CL36-01", 0, E_IDEATION),
    ("M29", "CL36-03 (ex-M6) lanceur : Argon obligatoire sur course réelle", LANCEUR,
     'if args.moteur == "claude-sdk" and not (prop_ext and juges_ext):  # CL36-03', "if False:  # CL36-03", 0,
     E_IDEATION),
    ("M30", "CL36-04 (ex-M11) défaut du juge Opus (4)", LANCEUR,
     '("juge_ideation", "claude-opus-5-5"): 4.0', '("juge_ideation", "claude-opus-5-5"): 5.0', 0, E_IDEATION),
    ("M31", "CL35-07 (ex-M17) commande avec --juge-externe seul hors bras", LANCEUR,
     "if args.commande_externe and not (args.bras_rapporte_differe or args.proposeur_externe):",
     "if args.commande_externe and not (args.bras_rapporte_differe or args.proposeur_externe or args.juge_externe):", 0,
     E_IDEATION),
    ("M32", "v39 écart de garde non fini refusé", PARI,
     "        if isinstance(g, bool) or not isinstance(g, (int, float)) or not math.isfinite(g):\n"
     "            raise ContrasteInvalide(f\"écart de faux positifs non fini ou non numérique : {g!r}\")",
     "        pass", 0, E_PARI),
    ("M33", "v39 PACE : écarts vérifiés par la porte", PACE,
     "        if not _nombre(g) or not math.isfinite(g):", "        if False:", 0, E_PACE),
    ("M34", "v39 PACE : gain réel non fini refusé", PACE,
     "if gain is not None and (not _nombre(gain) or not math.isfinite(gain)):", "if False:", 0, E_PACE),
    ("M35", "v39 PACE : e-BH de notre bras (et non l'arrêt par candidat)", PACE,
     'd["pari_apparie"]["validee"] = d["nom"] in retenues', 'd["pari_apparie"]["validee"] = d["pari_apparie"]["arretee_au_seuil"]',
     0, E_PACE),
    ("M36", "v39 PACE : δ de la garde vérifié", PACE,
     "if delta is None or not _nombre(delta) or not 0.0 < delta < 1.0:", "if delta is None:", 0, E_PACE),
    ("M37", "v39 PACE : témoin planté (contrôle positif) compté", PACE,
     'k["temoins_valides"] += d["temoin"]', "pass", 0, E_PACE),
    ("M38", "CL37-05 (ex-M8) garde CL35-04 : adaptateur simulé sur course réelle", IDEATION,
     'if a is None or (moteur == "claude-sdk" and getattr(a, "nom", None) != "commande-externe"):',
     "if a is None:", 2, E_IDEATION),
]


def appliquer(copie, fichier, ancien, nouveau, occ):
    chemin = os.path.join(copie, fichier)
    with open(chemin, encoding="utf-8") as f:
        texte = f.read()
    n = texte.count(ancien)
    if occ == 0:
        if n != 1:
            return f"non appliquée : {n} occurrence(s), unique exigée"
        texte = texte.replace(ancien, nouveau)
    else:
        if n < occ:
            return f"non appliquée : {n} occurrence(s) < {occ}"
        pos = -1
        for _ in range(occ):
            pos = texte.index(ancien, pos + 1)
        texte = texte[:pos] + nouveau + texte[pos + len(ancien):]
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(texte)
    return None


def jouer(arbre, dossier, python, complet, m):
    ident, constat, fichier, ancien, nouveau, occ, essais = m
    copie = os.path.join(dossier, f"copie-{ident.lower()}")
    if os.path.exists(copie):
        shutil.rmtree(copie)
    shutil.copytree(arbre, copie, ignore=shutil.ignore_patterns("__pycache__"))
    refus = appliquer(copie, fichier, ancien, nouveau, occ)
    if refus:
        return ident, constat, refus, "", 0.0
    commande = [python, "-B", "-m", "unittest"] + (["discover", "-s", "essais", "-t", ".", "-p", "test_*.py"] if complet else essais)
    debut = time.time()
    r = subprocess.run(commande, cwd=copie, capture_output=True, text=True, timeout=1800,
                       env={"PATH": "/usr/bin:/bin", "HOME": "/root", "LANG": "C.UTF-8"})
    duree = time.time() - debut
    sortie = r.stdout + r.stderr
    echecs = sorted(set(re.findall(r"^(?:FAIL|ERROR): (\S+) \((\S+)\)", sortie, re.M)))
    ran = re.search(r"Ran (\d+) tests?", sortie)
    verdict = "tuée" if r.returncode != 0 else "survivante"
    detail = f"{ran.group(1) if ran else '?'} essais ; " + ", ".join(f"{t} ({c.split('.')[-1]})" for t, c in echecs[:4])
    with open(os.path.join(dossier, f"sortie-{ident.lower()}{'-complet' if complet else ''}.txt"), "w") as f:
        f.write(sortie)
    shutil.rmtree(copie)
    return ident, constat, verdict, detail, duree


def main():
    arbre, dossier, python = sys.argv[1:4]
    reste = sys.argv[4:]
    complet = bool(reste) and reste[0] == "complet"
    ids = set(reste[1:] if complet else reste)
    choisies = [m for m in MUTATIONS if not ids or m[0] in ids]
    os.makedirs(dossier, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        resultats = list(ex.map(lambda m: jouer(arbre, dossier, python, complet, m), choisies))
    for ident, constat, verdict, detail, duree in resultats:
        print(f"{ident} | {constat} | {verdict} | {detail} | {duree:.0f} s")


if __name__ == "__main__":
    main()
