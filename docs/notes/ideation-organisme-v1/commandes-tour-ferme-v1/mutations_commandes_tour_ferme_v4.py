"""Banc de mutations des commandes v4 du tour fermé : chaque mutation est une altération ciblée d'une commande, dans une copie
du dossier ; la suite `test_commandes_tour_ferme_v4.py` doit alors échouer (mutation « tuée »). Le cas sain (dossier non muté)
doit passer d'abord ; sinon le banc s'arrête (R5). Un motif introuvable ou présent plus d'une fois arrête aussi le banc (jamais
une mutation sautée en silence). Sans réseau hors boucle locale, sans clé, sans dépense. Rédigé le 3 novembre 2026 (sous-agent
de session-depot).

Mutations jouées : les 23 du banc v3 (K1 à K11, A1 à A12), transposées au texte de la v4 ; les 12 de la contre-lecture de la
v3 (C1 à C12, `contre-lecture-v3/mes-mutations.txt`), transposées ; 29 propres à la v4 (N1 à N29 : suffixe d'étape retiré,
doublé ou au nom de l'autre fournisseur, champs `etape` et `etape_registre`, `cause_refus` fausse ou absente, refus 402 et 429
de Kimi rendus en code 3 ou sans la signature du relais, écart de modèle signalé par le relais Kimi (502), dernière
ligne d'argparse chez Argon, délai et signaux chez Argon).

    env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B \\
        mutations_commandes_tour_ferme_v4.py [--seulement K1,N3]

Code 0 si le cas sain passe et que toutes les mutations jouées sont tuées ; 1 sinon. Rapport (table) sur la sortie standard.
Chaque suite est un processus `pytest` à délai borné (arrêté par son PID au délai : `subprocess.run`, R10).
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time

ICI = os.path.dirname(os.path.abspath(__file__))
PY = "/home/user/controle-ia-travail/.venv/bin/python" if os.path.exists("/home/user/controle-ia-travail/.venv/bin/python") else sys.executable
SUITE = "test_commandes_tour_ferme_v4.py"
FICHIERS = ("commande_kimi_v4.py", "commande_argon_v56_nuit_v4.py", "commande_argon_v56_nuit_v3.py", "registre_depense_cumulee_v1.py",
            SUITE)
KIMI, ARGON = "commande_kimi_v4.py", "commande_argon_v56_nuit_v4.py"
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "HOME": tempfile.gettempdir(), "TMPDIR": tempfile.gettempdir()}

RETOUR_LECTEUR = "        return args.max_sortie_lecteur, args.sortie_min_jetons_lecteur\n"
ROLES_V3 = 'ROLES = ("proposeur_ideation", "juge_ideation", "experimentateur_test", "lecteur_test")  # v3 (1)\n'
RENDRE = "    cout = cout if (isinstance(cout, (int, float)) and math.isfinite(cout) and cout > 0) else PLANCHER\n"
SIGNAUX = "    signal.signal(signal.SIGTERM, interrompu)\n    signal.signal(signal.SIGINT, interrompu)\n"
DELAI = "fin(6 if isinstance(e, TimeoutError) else 3,"
SUFFIXE = "    return etape if etape.endswith(suffixe) else etape + suffixe\n"
CLASSEMENT = '        return "garde_etape" if str(e).startswith(PREFIXE_GARDE_ETAPE) else "garde_cumulee"\n'
CAUSES_RELAIS = 'CAUSES_RELAIS = {402: "relais_plafond", 429: "relais_max_appels"}'
DIAG_ETAPE = '"role": role, "etape": etape, "etape_registre": etape_registre}'
RESERVER_ETAPE = "etape=etape_registre, plafond_etape_usd=plafond_dur)"
SECOND_CONTROLE = 'role=role,\n               cause_refus="plafond_session")  # v3 (3), v4 (2)\n'
LIGNE_ARGPARSE = ('        rendre(2, erreur=f"arguments refusés par argparse (sortie {e.code})", envoye=False,\n'
                  '               role=(os.environ if environ is None else environ).get("ROLE_POLE"))\n')

MUTATIONS = [
    # --- banc v3, transposé (Kimi) -------------------------------------------------------------------------------------------
    ("K1", KIMI, "rôle lecteur_test retiré de ROLES", ROLES_V3, 'ROLES = ("proposeur_ideation", "juge_ideation", "experimentateur_test")\n'),
    ("K2", KIMI, "sortie minimale du lecteur ignorée (minimum général à sa place)", RETOUR_LECTEUR,
     "        return args.max_sortie_lecteur, args.sortie_min_jetons\n"),
    ("K3", KIMI, "sortie maximale du lecteur ignorée (sortie courte à sa place)", RETOUR_LECTEUR,
     "        return args.max_sortie_court, args.sortie_min_jetons_lecteur\n"),
    ("K4", KIMI, "champ envoye perdu sur le refus du plafond de session", '(corps {len(corps)} octets)", envoye=False,\n',
     '(corps {len(corps)} octets)",\n'),
    ("K5", KIMI, "sortie minimale non appliquée (envoi sous le minimum)", "    return n if n >= mini else None\n", "    return n\n"),
    ("K6", KIMI, "plafond de session absent toléré (défaut 1e9 à la place de nan)",
     'plafond = float(environ.get("PLAFOND_SESSION_USD", "nan"))', 'plafond = float(environ.get("PLAFOND_SESSION_USD", "1e9"))'),
    ("K7", KIMI, "version v3 rendue", 'VERSION = "commande-kimi-v4"\n', 'VERSION = "commande-kimi-v3"\n'),
    ("K8", KIMI, "contrôle de MODELE_DEMANDE_POLE retiré", "        if demande is not None and demande != args.modele:\n", "        if False:\n"),
    ("K9", KIMI, "champ role absent de la ligne de refus (code 2)",
     '        rendre(2, erreur=str(e)[:300], envoye=False, role=environ.get("ROLE_POLE"))  # v3 (3)\n',
     '        rendre(2, erreur=str(e)[:300], envoye=False)\n'),
    ("K10", KIMI, "porte « environnement » incomplète tolérée (ETAPE_POLE seul)",
     "    if etape is None and brut is None:\n        return None, None\n", "    if etape is None or brut is None:\n        return None, None\n"),
    ("K11", KIMI, "plafond cumulé du registre remplacé par 1e9",
     'ident = reg.reserver(args.registre, plafond_cumule_usd=args.plafond_cumule_usd, pire_cas_usd=pire, fournisseur="kimi",',
     'ident = reg.reserver(args.registre, plafond_cumule_usd=1e9, pire_cas_usd=pire, fournisseur="kimi",'),
    # --- banc v3, transposé (Argon) ------------------------------------------------------------------------------------------
    ("A1", ARGON, "rôle experimentateur_test retiré de ROLES", ROLES_V3, 'ROLES = ("proposeur_ideation", "juge_ideation", "lecteur_test")\n'),
    ("A2", ARGON, "sortie minimale du lecteur ignorée (minimum général à sa place)", RETOUR_LECTEUR,
     "        return args.max_sortie_lecteur, args.sortie_min_jetons\n"),
    ("A3", ARGON, "sortie maximale du lecteur ignorée (sortie courte à sa place)", RETOUR_LECTEUR,
     "        return args.max_sortie_court, args.sortie_min_jetons_lecteur\n"),
    ("A4", ARGON, "champ envoye perdu sur le refus du plafond de session", '({len(prompt)} caractères)", envoye=False,\n',
     '({len(prompt)} caractères)",\n'),
    ("A5", ARGON, "sortie minimale non appliquée (envoi sous le minimum)", "    if mt < mini:  # v3 (2)\n", "    if mt < 0:  # v3 (2)\n"),
    ("A6", ARGON, "plafond de session absent toléré (défaut 1e9 à la place de nan)",
     'plafond = float(environ.get("PLAFOND_SESSION_USD", "nan"))', 'plafond = float(environ.get("PLAFOND_SESSION_USD", "1e9"))'),
    ("A7", ARGON, "version v3 rendue", 'VERSION = "commande-argon-v56-nuit-v4"\n', 'VERSION = "commande-argon-v56-nuit-v3"\n'),
    ("A8", ARGON, "contrôle de MODELE_DEMANDE_POLE retiré", "        if demande is not None and demande != args.modele:\n", "        if False:\n"),
    ("A9", ARGON, "champ role absent de la ligne de refus (code 2)",
     '        rendre(2, erreur=str(e)[:300], envoye=False, role=environ.get("ROLE_POLE"))  # v3 (3)\n',
     '        rendre(2, erreur=str(e)[:300], envoye=False)\n'),
    ("A10", ARGON, "porte « environnement » incomplète tolérée (ETAPE_POLE seul)",
     "    if etape is None and brut is None:\n        return None, None\n", "    if etape is None or brut is None:\n        return None, None\n"),
    ("A11", ARGON, "plafond cumulé du registre remplacé par 1e9",
     'ident = reg.reserver(args.registre, plafond_cumule_usd=args.plafond_cumule_usd, pire_cas_usd=pire, fournisseur="argon",',
     'ident = reg.reserver(args.registre, plafond_cumule_usd=1e9, pire_cas_usd=pire, fournisseur="argon",'),
    ("A12", ARGON, "le relais (servir) tolère un corps sans Content-Length (411 perdu)",
     '            if longueur is None:\n                return self._json(411, {"erreur": "Content-Length exigé"})\n',
     '            if longueur is None:\n                longueur = "2"\n'),
    # --- contre-lecture de la v3 (mes-mutations.txt), transposées ------------------------------------------------------------
    ("C1", KIMI, "lecteur_test prend les bornes du proposeur", RETOUR_LECTEUR, "        return args.max_sortie_proposeur, args.sortie_min_jetons\n"),
    ("C2", ARGON, "lecteur_test prend les bornes du proposeur", RETOUR_LECTEUR, "        return args.max_sortie_proposeur, args.sortie_min_jetons\n"),
    ("C3", KIMI, "cout_usd = 0 sur code 4", RENDRE,
     "    cout = 0.0 if code == 4 else (cout if (isinstance(cout, (int, float)) and math.isfinite(cout) and cout > 0) else PLANCHER)\n"),
    ("C4", ARGON, "cout_usd = 0 sur code 4", RENDRE,
     "    cout = 0.0 if code == 4 else (cout if (isinstance(cout, (int, float)) and math.isfinite(cout) and cout > 0) else PLANCHER)\n"),
    ("C5", ARGON, "envoye vrai sur un refus 402/429 du relais", 'erreur=f"HTTP {e.code} : {motif}", envoye=not avant, **extra)\n',
     'erreur=f"HTTP {e.code} : {motif}", envoye=True, **extra)\n'),
    ("C6", KIMI, "envoye vrai sur un refus 402/429 du relais", "envoye=not avant_amont, **extra)\n", "envoye=True, **extra)\n"),
    ("C7", KIMI, "délai dépassé rendu en code 3 au lieu de 6", DELAI, "fin(3,"),
    ("C8", KIMI, "gestionnaires de signaux retirés", SIGNAUX, "    pass\n"),
    ("C9", KIMI, "contrôle du modèle servi retiré", "    if servi != args.modele:\n", "    if False:\n"),
    ("C10", ARGON, "contrôle du modèle servi retiré",
     "    if servi != args.modele:  # identifiant exact (servi observé à l'épreuve du pont : « gemini-4-argon »)\n", "    if False:\n"),
    ("C11", ARGON, "coût d'un échec pris au chiffre du relais, pas au pire cas réservé", '    if origine == "pire_cas":\n        cout = pire',
     '    if False:\n        cout = pire'),
    ("C12", KIMI, "garde d'étape du registre débranchée (plafond_etape_usd=None)", RESERVER_ETAPE,
     "etape=etape_registre, plafond_etape_usd=None)"),
    # --- propres à la v4 -----------------------------------------------------------------------------------------------------
    ("N1", KIMI, "suffixe d'étape retiré à l'appel du registre (clé = ETAPE_POLE)", RESERVER_ETAPE, "etape=etape, plafond_etape_usd=plafond_dur)"),
    ("N2", ARGON, "suffixe d'étape retiré à l'appel du registre (clé = ETAPE_POLE)", RESERVER_ETAPE, "etape=etape, plafond_etape_usd=plafond_dur)"),
    ("N3", KIMI, "suffixe d'étape retiré partout (etape_du_registre rend ETAPE_POLE)", SUFFIXE, "    return etape\n"),
    ("N4", ARGON, "suffixe d'étape retiré partout (etape_du_registre rend ETAPE_POLE)", SUFFIXE, "    return etape\n"),
    ("N5", KIMI, "suffixe d'étape doublé (idempotence perdue)", SUFFIXE, "    return etape + suffixe\n"),
    ("N6", ARGON, "suffixe d'étape doublé (idempotence perdue)", SUFFIXE, "    return etape + suffixe\n"),
    ("N7", KIMI, "champ etape de la dernière ligne = clé du registre (valeur reçue perdue)", DIAG_ETAPE,
     '"role": role, "etape": etape_registre, "etape_registre": etape_registre}'),
    ("N8", ARGON, "champ etape_registre absent de la dernière ligne", DIAG_ETAPE, '"role": role, "etape": etape}'),
    ("N9", KIMI, "cause : préfixe de la garde d'étape faux (garde d'étape lue garde cumulée)", 'PREFIXE_GARDE_ETAPE = "garde d\'étape ("',
     'PREFIXE_GARDE_ETAPE = "garde d\'etape ("'),
    ("N10", ARGON, "cause : garde d'étape et garde cumulée permutées", CLASSEMENT,
     '        return "garde_cumulee" if str(e).startswith(PREFIXE_GARDE_ETAPE) else "garde_etape"\n'),
    ("N11", KIMI, "cause absente sur le premier contrôle du plafond de session", 'role=role, cause_refus="plafond_session")', "role=role)"),
    ("N12", ARGON, "cause absente sur le second contrôle du plafond de session", SECOND_CONTROLE, "role=role)  # v3 (3), v4 (2)\n"),
    ("N13", KIMI, "cause absente sur un refus du registre", "cause_refus=cause_du_registre(e), ", ""),
    ("N14", ARGON, "cause : registre illisible lu garde cumulée", '    return "registre_illisible"\n', '    return "garde_cumulee"\n'),
    ("N15", KIMI, "refus 402/429 du relais rendu en code 3 (comportement v3)",
     "        if e.code in CAUSES_RELAIS and refus_du_relais(corps_erreur):", "        if False:"),
    ("N16", KIMI, "signature du relais ignorée (erreur de l'amont 402/429 rendue en code 4)",
     " and refus_du_relais(corps_erreur):", ":"),
    ("N17", ARGON, "causes 402 et 429 permutées", CAUSES_RELAIS, 'CAUSES_RELAIS = {402: "relais_max_appels", 429: "relais_plafond"}'),
    ("N18", KIMI, "causes 402 et 429 permutées", CAUSES_RELAIS, 'CAUSES_RELAIS = {402: "relais_max_appels", 429: "relais_plafond"}'),
    ("N19", ARGON, "cause_refus hors du code 4 (sur tout refus HTTP du relais)",
     '        extra = {"cause_refus": CAUSES_RELAIS[e.code]} if e.code in CAUSES_RELAIS else {}',
     '        extra = {"cause_refus": CAUSES_RELAIS.get(e.code, "relais_plafond")}'),
    ("N20", ARGON, "dernière ligne JSON d'argparse retirée (comportement v3)", LIGNE_ARGPARSE, "        raise\n"),
    ("N21", ARGON, "dernière ligne JSON d'argparse aussi pour servir (servir changé)", '        if argv[0] == "servir":\n            raise',
     '        if False:\n            raise'),
    ("N22", ARGON, "champ role absent de la ligne d'argparse", 'envoye=False,\n               role=(os.environ if environ is None else environ).get("ROLE_POLE"))\n',
     "envoye=False)\n"),
    ("N23", ARGON, "délai dépassé rendu en code 3 au lieu de 6", DELAI, "fin(3,"),
    ("N24", ARGON, "gestionnaires de signaux retirés", SIGNAUX, "    pass\n"),
    ("N25", KIMI, "cause fausse sur le second contrôle du plafond de session", '               cause_refus="plafond_session")  # v3 (3), v4 (2)\n',
     '               cause_refus="plafond_etape")  # v3 (3), v4 (2)\n'),
    ("N26", ARGON, "clé d'étape au nom de l'autre fournisseur", 'etape_du_registre(etape, "argon")', 'etape_du_registre(etape, "kimi")'),
    ("N27", KIMI, "cause : refus du registre toujours garde d'étape", CLASSEMENT, '        return "garde_etape"\n'),
    ("N28", KIMI, "écart de modèle signalé par le relais (502) perdu : modele_servi non rendu",
     'extra["modele_servi"] = ECART_RELAIS', 'extra["ecart"] = ECART_RELAIS'),
    ("N29", KIMI, "502 du relais rendu en code 3 au lieu de 5", "        code = 3 if e.code != 502 else 5\n", "        code = 3\n"),
]


def copier_dossier(dossier):
    for f in FICHIERS:
        shutil.copy(os.path.join(ICI, f), os.path.join(dossier, f))


def appliquer(dossier, fichier, avant, apres):
    chemin = os.path.join(dossier, fichier)
    with open(chemin, encoding="utf-8") as f:
        t = f.read()
    n = t.count(avant)
    if n != 1:
        raise RuntimeError(f"mutation inapplicable : motif trouvé {n} fois dans {fichier} : {avant[:70]!r}")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(t.replace(avant, apres))


def jouer_suite(dossier, arret_premier_echec):
    t0 = time.time()
    args = [PY, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", SUITE] + (["-x"] if arret_premier_echec else [])
    p = subprocess.run(args, cwd=dossier, env=ENV, capture_output=True, timeout=900)
    sortie = p.stdout.decode("utf-8", "replace")
    resume = [l for l in sortie.splitlines() if " passed" in l or " failed" in l or " error" in l]
    return p.returncode, (resume[-1].strip() if resume else sortie[-200:].strip()), round(time.time() - t0, 1)


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--seulement", default="", help="identifiants de mutations, séparés par des virgules")
    args = a.parse_args(argv)
    choisies = [m for m in MUTATIONS if not args.seulement or m[0] in args.seulement.split(",")]
    if len({m[0] for m in MUTATIONS}) != len(MUTATIONS):
        raise RuntimeError("identifiants de mutations en double")
    with tempfile.TemporaryDirectory(prefix="mutations-commandes-tf-v4-motifs-") as d:  # tous les motifs d'abord (aucune sautée)
        copier_dossier(d)
        for ident, fichier, _, avant, _ in choisies:
            n = open(os.path.join(d, fichier), encoding="utf-8").read().count(avant)
            if n != 1:
                raise RuntimeError(f"{ident} : motif trouvé {n} fois dans {fichier}")
    with tempfile.TemporaryDirectory(prefix="mutations-commandes-tf-v4-sain-") as sain:
        copier_dossier(sain)
        code, resume, duree = jouer_suite(sain, False)
    print(f"cas sain (dossier non muté) : {'passe' if code == 0 else 'ÉCHOUE'} — {resume} ({duree} s)", flush=True)
    if code != 0:
        print("le cas sain échoue : banc arrêté (R5)")
        return 1
    lignes, tuees = [], 0
    for ident, fichier, quoi, avant, apres in choisies:
        with tempfile.TemporaryDirectory(prefix=f"mutations-commandes-tf-v4-{ident}-") as d:
            copier_dossier(d)
            appliquer(d, fichier, avant, apres)
            code, resume, duree = jouer_suite(d, True)
        tuee = code != 0
        tuees += tuee
        lignes.append(f"| {ident} | `{fichier}` | {quoi} | {'tuée' if tuee else 'SURVIT'} | {resume} | {duree} s |")
        print(lignes[-1], flush=True)
    print(f"\nmutations tuées : {tuees} sur {len(choisies)} jouées")
    print("\n| id | fichier | mutation | sort | suite | durée |\n|---|---|---|---|---|---|\n" + "\n".join(lignes))
    return 0 if tuees == len(choisies) else 1


if __name__ == "__main__":
    sys.exit(principal())
