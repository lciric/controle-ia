"""Banc de mutations des commandes v3 du tour fermé (TF-01) : chaque mutation est une altération ciblée d'une commande, dans une
copie du dossier ; la suite `test_commandes_tour_ferme_v3.py` doit alors échouer (mutation « tuée »). Le cas sain (dossier non
muté) doit passer d'abord ; sinon le banc s'arrête (R5). Sans réseau, sans clé, sans dépense. Rédigé le 2 novembre 2026
(sous-agent de session-depot).

    nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B mutations_commandes_tour_ferme_v3.py [--seulement K1,A3]

Code 0 si le cas sain passe et que toutes les mutations jouées sont tuées ; 1 sinon. Rapport (table) sur la sortie standard.
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
FICHIERS = ("commande_kimi_v3.py", "commande_argon_v56_nuit_v3.py", "registre_depense_cumulee_v1.py", "test_commandes_tour_ferme_v3.py")
KIMI, ARGON = "commande_kimi_v3.py", "commande_argon_v56_nuit_v3.py"
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "HOME": tempfile.gettempdir(), "TMPDIR": tempfile.gettempdir()}

RETOUR_LECTEUR = "        return args.max_sortie_lecteur, args.sortie_min_jetons_lecteur\n"
ROLES_V3 = 'ROLES = ("proposeur_ideation", "juge_ideation", "experimentateur_test", "lecteur_test")  # v3 (1)\n'

MUTATIONS = [
    # --- Kimi -------------------------------------------------------------------------------------------------------------
    ("K1", KIMI, "rôle lecteur_test retiré de ROLES", ROLES_V3,
     'ROLES = ("proposeur_ideation", "juge_ideation", "experimentateur_test")\n'),
    ("K2", KIMI, "sortie minimale du lecteur ignorée (minimum général à sa place)", RETOUR_LECTEUR,
     "        return args.max_sortie_lecteur, args.sortie_min_jetons\n"),
    ("K3", KIMI, "sortie maximale du lecteur ignorée (sortie courte à sa place)", RETOUR_LECTEUR,
     "        return args.max_sortie_court, args.sortie_min_jetons_lecteur\n"),
    ("K4", KIMI, "champ envoye perdu sur le refus du plafond de session",
     '            rendre(4, erreur=f"pire cas au-dessus du plafond de session {plafond} USD (corps {len(corps)} octets)", envoye=False,\n'
     '                   role=role)  # v3 (3)\n',
     '            rendre(4, erreur=f"pire cas au-dessus du plafond de session {plafond} USD (corps {len(corps)} octets)",\n'
     '                   role=role)  # v3 (3)\n'),
    ("K5", KIMI, "sortie minimale non appliquée (envoi sous le minimum)", "    return n if n >= mini else None\n", "    return n\n"),
    ("K6", KIMI, "plafond de session absent toléré (défaut 1e9 à la place de nan)",
     'plafond = float(environ.get("PLAFOND_SESSION_USD", "nan"))', 'plafond = float(environ.get("PLAFOND_SESSION_USD", "1e9"))'),
    ("K7", KIMI, "version v2 rendue", 'VERSION = "commande-kimi-v3"\n', 'VERSION = "commande-kimi-v2"\n'),
    ("K8", KIMI, "contrôle de MODELE_DEMANDE_POLE retiré",
     "        if demande is not None and demande != args.modele:\n", "        if False:\n"),
    ("K9", KIMI, "champ role absent de la ligne de refus (code 2)",
     '        rendre(2, erreur=str(e)[:300], envoye=False, role=environ.get("ROLE_POLE"))  # v3 (3)\n',
     '        rendre(2, erreur=str(e)[:300], envoye=False)\n'),
    ("K10", KIMI, "porte « environnement » incomplète tolérée (ETAPE_POLE seul)",
     "    if etape is None and brut is None:\n        return None, None\n", "    if etape is None or brut is None:\n        return None, None\n"),
    ("K11", KIMI, "plafond cumulé du registre remplacé par 1e9",
     "ident = reg.reserver(args.registre, plafond_cumule_usd=args.plafond_cumule_usd, pire_cas_usd=pire, fournisseur=\"kimi\",",
     "ident = reg.reserver(args.registre, plafond_cumule_usd=1e9, pire_cas_usd=pire, fournisseur=\"kimi\","),
    # --- Argon (`appeler`) --------------------------------------------------------------------------------------------------
    ("A1", ARGON, "rôle experimentateur_test retiré de ROLES", ROLES_V3,
     'ROLES = ("proposeur_ideation", "juge_ideation", "lecteur_test")\n'),
    ("A2", ARGON, "sortie minimale du lecteur ignorée (minimum général à sa place)", RETOUR_LECTEUR,
     "        return args.max_sortie_lecteur, args.sortie_min_jetons\n"),
    ("A3", ARGON, "sortie maximale du lecteur ignorée (sortie courte à sa place)", RETOUR_LECTEUR,
     "        return args.max_sortie_court, args.sortie_min_jetons_lecteur\n"),
    ("A4", ARGON, "champ envoye perdu sur le refus du plafond de session",
     '        rendre(4, erreur=f"pire cas au-dessus du plafond de session {plafond} USD ({len(prompt)} caractères)", envoye=False,\n'
     '               role=role)  # v3 (3)\n',
     '        rendre(4, erreur=f"pire cas au-dessus du plafond de session {plafond} USD ({len(prompt)} caractères)",\n'
     '               role=role)  # v3 (3)\n'),
    ("A5", ARGON, "sortie minimale non appliquée (envoi sous le minimum)", "    if mt < mini:  # v3 (2)\n", "    if mt < 0:  # v3 (2)\n"),
    ("A6", ARGON, "plafond de session absent toléré (défaut 1e9 à la place de nan)",
     'plafond = float(environ.get("PLAFOND_SESSION_USD", "nan"))', 'plafond = float(environ.get("PLAFOND_SESSION_USD", "1e9"))'),
    ("A7", ARGON, "version v2 rendue", 'VERSION = "commande-argon-v56-nuit-v3"\n', 'VERSION = "commande-argon-v56-nuit-v2"\n'),
    ("A8", ARGON, "contrôle de MODELE_DEMANDE_POLE retiré",
     "        if demande is not None and demande != args.modele:\n", "        if False:\n"),
    ("A9", ARGON, "champ role absent de la ligne de refus (code 2)",
     '        rendre(2, erreur=str(e)[:300], envoye=False, role=environ.get("ROLE_POLE"))  # v3 (3)\n',
     '        rendre(2, erreur=str(e)[:300], envoye=False)\n'),
    ("A10", ARGON, "porte « environnement » incomplète tolérée (ETAPE_POLE seul)",
     "    if etape is None and brut is None:\n        return None, None\n", "    if etape is None or brut is None:\n        return None, None\n"),
    ("A11", ARGON, "plafond cumulé du registre remplacé par 1e9",
     "ident = reg.reserver(args.registre, plafond_cumule_usd=args.plafond_cumule_usd, pire_cas_usd=pire, fournisseur=\"argon\",",
     "ident = reg.reserver(args.registre, plafond_cumule_usd=1e9, pire_cas_usd=pire, fournisseur=\"argon\","),
    ("A12", ARGON, "le relais (servir) tolère un corps sans Content-Length (411 perdu)",
     '            if longueur is None:\n                return self._json(411, {"erreur": "Content-Length exigé"})\n',
     '            if longueur is None:\n                longueur = "2"\n'),
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
    args = [PY, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "test_commandes_tour_ferme_v3.py"] + (["-x"] if arret_premier_echec else [])
    p = subprocess.run(args, cwd=dossier, env=ENV, capture_output=True, timeout=900)
    sortie = p.stdout.decode("utf-8", "replace")
    resume = [l for l in sortie.splitlines() if " passed" in l or " failed" in l or " error" in l]
    return p.returncode, (resume[-1].strip() if resume else sortie[-200:].strip()), round(time.time() - t0, 1)


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--seulement", default="", help="identifiants de mutations, séparés par des virgules")
    args = a.parse_args(argv)
    choisies = [m for m in MUTATIONS if not args.seulement or m[0] in args.seulement.split(",")]
    with tempfile.TemporaryDirectory(prefix="mutations-commandes-tf-sain-") as sain:
        copier_dossier(sain)
        code, resume, duree = jouer_suite(sain, False)
    print(f"cas sain (dossier non muté) : {'passe' if code == 0 else 'ÉCHOUE'} — {resume} ({duree} s)")
    if code != 0:
        print("le cas sain échoue : banc arrêté (R5)")
        return 1
    lignes, tuees = [], 0
    for ident, fichier, quoi, avant, apres in choisies:
        with tempfile.TemporaryDirectory(prefix=f"mutations-commandes-tf-{ident}-") as d:
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
