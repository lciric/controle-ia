"""Banc de mutations des commandes v6 du tour fermé : chaque mutation est une altération ciblée d'une commande, dans une copie
du dossier ; la suite `test_commandes_tour_ferme_v6.py` doit alors échouer (mutation « tuée »). Le cas sain (dossier non muté,
suite entière) doit passer d'abord ; sinon le banc s'arrête (R5). Un motif introuvable ou présent plus d'une fois, ou un fichier
muté qui ne se lit plus comme du Python, arrête aussi le banc. Sans réseau hors boucle locale, sans clé, sans dépense. Rédigé le
3 novembre 2026 (sous-agent de session-depot) depuis le banc v5 (scellé).

v6 (CL5-02 de la contre-lecture de la v5) : **une mutation n'est « tuée » que par un essai de comportement** : la suite de
chaque mutation est jouée sans l'essai d'identité de `servir` (`--deselect`, il comparerait des octets et tuerait toute
mutation posée dans le prologue d'Argon, quel que soit son effet), et seul le code 1 de pytest (des essais échouent) compte ;
tout autre code (collecte, interruption, usage) arrête le banc. Le premier essai qui échoue est relevé.

Mutations jouées : les 91 du banc v5, transposées au texte de la v6 ; les cinq de la contre-lecture de la v5 (CL5-M1 à CL5-M3b,
dont trois survivaient à la suite v5) ; 15 propres à la v6 (S1 à S15 : réponse coupée, ligne de cause, registre corrompu,
`envoye` d'une erreur de l'amont, statut au registre).

    env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp PYTHONPATH=COPIE/orchestrator nice -n 10 \\
        /home/user/controle-ia-travail/.venv/bin/python -I -B mutations_commandes_tour_ferme_v6.py [--seulement K1,S3]

Code 0 si le cas sain passe et que toutes les mutations jouées sont tuées ; 1 sinon. Chaque suite est un processus `pytest` à
délai borné (arrêté par son PID au délai : `subprocess.run`, R10).
"""
import argparse
import ast
import os
import shutil
import subprocess
import sys
import tempfile
import time

ICI = os.path.dirname(os.path.abspath(__file__))
PY = "/home/user/controle-ia-travail/.venv/bin/python" if os.path.exists("/home/user/controle-ia-travail/.venv/bin/python") else sys.executable
SUITE = "test_commandes_tour_ferme_v6.py"
KIMI, ARGON = "commande_kimi_v6.py", "commande_argon_v56_nuit_v6.py"
IDENTITE_SERVIR = SUITE + "::test_bloc_servir_identique_a_la_v5"  # jamais juge d'une mutation (v6, CL5-02)
FICHIERS = (KIMI, ARGON, "commande_kimi_v4.py", "commande_argon_v56_nuit_v4.py", "commande_argon_v56_nuit_v5.py",
            "commande_argon_v56_nuit_v3.py",
            "registre_depense_cumulee_v1.py", SUITE)
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
PREMIER_CONTROLE = 'role=role, cause_refus="plafond_session")  # v3 (3), v4 (2)\n'
LIGNE_ARGPARSE = ('        rendre(2, erreur=f"arguments refusés par argparse (sortie {e.code})", envoye=False,\n'
                  '               role=(os.environ if environ is None else environ).get("ROLE_POLE"))\n')
SIGNATURE = 'return isinstance(objet, dict) and isinstance(objet.get("relais"), str) and objet["relais"].startswith("relais-kimi-")'
REGISTRE_V5 = "        rendre(3, erreur=str(e)[:300], envoye=False, cause_refus=cause_du_registre(e), **diag)"
CAUSE_SIGNEE_V5 = '            extra["cause_refus"] = CAUSES_RELAIS[e.code]  # v5 (1)'
FIN_RELAIS_ARGON_V5 = "        fin(3, cout=PLANCHER if avant else pire,"
CAUSE_RELAIS_ARGON = '        extra = {"cause_refus": CAUSES_RELAIS[e.code]} if e.code in CAUSES_RELAIS else {}'

CONSTANTE_PROLOGUE = ("PLANCHER = 1e-6\n", "PLANCHER = 1e-6\nCODE_LIMITE = 4  # mutation CL5\n")
_PREF = "PREFIXE_GARDE_ETAPE = \"garde d'étape (\"  # v4 (2) : registre_depense_cumulee_v1.py l. 143 (fichier gelé, sha256 8ba92066…)\n"
CONSTANTE_APPELER = (_PREF, _PREF + "CODE_LIMITE = 4  # mutation CL5 (partie appeler)\n")
ECHEC_INTERFACE = '        fin(3, cout=cout, origine=origine, erreur="interface : " + str(o["echec"])[:300], **extra)'
ECHEC_429_EN_4 = ('        fin(CODE_LIMITE if "429" in str(o["echec"]) else 3, cout=cout, origine=origine, '
                  'erreur="interface : " + str(o["echec"])[:300], envoye="429" not in str(o["echec"]), **extra)')
COUPEE_KIMI = '    if fin_raison == "length" and role in ROLES_COUPEE_ADMISE:'
COUPEE_ARGON = '    if statut == "TRONQUE" and role in ROLES_COUPEE_ADMISE and origine == "usage":'
ROLES_COUPEE = 'ROLES_COUPEE_ADMISE = ("experimentateur_test", "lecteur_test")'
FIN_COUPEE = '        fin(0, texte=texte, cout=cout, origine=origine, statut="coupee", coupee=True, **extra)\n'
LIGNE_CAUSE = ("        print(f\"{VERSION} : cause_refus={diag['cause_refus']} : {str(diag.get('erreur', ''))[:200]}\", file=sys.stderr)\n"
               "        sys.stderr.flush()\n")
EXCEPT_V6 = "    except Exception as e:  # noqa: BLE001 — v6 (3) : toute exception du registre (octets non UTF-8 compris) : registre_illisible\n"
EXCEPT_V5 = "    except (reg.PlafondCumule, reg.RegistreIllisible, OSError) as e:\n"
STATUT_KIMI = 'statut=extra.get("cause_refus", "echec"), erreur=f"HTTP {e.code} : {motif}", envoye=not avant_amont'
STATUT_ARGON = 'statut=extra.get("cause_refus", "echec"), erreur=f"HTTP {e.code} : {motif}", envoye=not avant,'


def registre_en_code_4_si(cause):
    return REGISTRE_V5.replace("rendre(3,", f'rendre(4 if cause_du_registre(e) == "{cause}" else 3,')


MUTATIONS = [
    # --- banc v4, transposé (Kimi) -------------------------------------------------------------------------------------------
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
    ("K7", KIMI, "version v5 rendue", 'VERSION = "commande-kimi-v6"\n', 'VERSION = "commande-kimi-v5"\n'),
    ("K8", KIMI, "contrôle de MODELE_DEMANDE_POLE retiré", "        if demande is not None and demande != args.modele:\n", "        if False:\n"),
    ("K9", KIMI, "champ role absent de la ligne de refus (code 2)",
     '        rendre(2, erreur=str(e)[:300], envoye=False, role=environ.get("ROLE_POLE"))  # v3 (3)\n',
     '        rendre(2, erreur=str(e)[:300], envoye=False)\n'),
    ("K10", KIMI, "porte « environnement » incomplète tolérée (ETAPE_POLE seul)",
     "    if etape is None and brut is None:\n        return None, None\n", "    if etape is None or brut is None:\n        return None, None\n"),
    ("K11", KIMI, "plafond cumulé du registre remplacé par 1e9",
     'ident = reg.reserver(args.registre, plafond_cumule_usd=args.plafond_cumule_usd, pire_cas_usd=pire, fournisseur="kimi",',
     'ident = reg.reserver(args.registre, plafond_cumule_usd=1e9, pire_cas_usd=pire, fournisseur="kimi",'),
    # --- banc v4, transposé (Argon) ------------------------------------------------------------------------------------------
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
    ("A7", ARGON, "version v5 rendue", 'VERSION = "commande-argon-v56-nuit-v6"\n', 'VERSION = "commande-argon-v56-nuit-v5"\n'),
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
    ("C5", ARGON, "envoye vrai sur un refus 402/429 du relais", 'erreur=f"HTTP {e.code} : {motif}", envoye=not avant, **extra)',
     'erreur=f"HTTP {e.code} : {motif}", envoye=True, **extra)'),
    ("C6", KIMI, "envoye vrai sur un refus 402/429 du relais", "envoye=not avant_amont, **extra)", "envoye=True, **extra)"),
    ("C7", KIMI, "délai dépassé rendu en code 3 au lieu de 6", DELAI, "fin(3,"),
    ("C8", KIMI, "gestionnaires de signaux retirés", SIGNAUX, "    pass\n"),
    ("C9", KIMI, "contrôle du modèle servi retiré", "    if servi != args.modele:\n", "    if False:\n"),
    ("C10", ARGON, "contrôle du modèle servi retiré",
     "    if servi != args.modele:  # identifiant exact (servi observé à l'épreuve du pont : « gemini-4-argon »)\n", "    if False:\n"),
    ("C11", ARGON, "coût d'un échec pris au chiffre du relais, pas au pire cas réservé", '    if origine == "pire_cas":\n        cout = pire',
     '    if False:\n        cout = pire'),
    ("C12", KIMI, "garde d'étape du registre débranchée (plafond_etape_usd=None)", RESERVER_ETAPE,
     "etape=etape_registre, plafond_etape_usd=None)"),
    # --- banc v4, mutations propres à la v4, transposées ---------------------------------------------------------------------
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
    ("N15", KIMI, "cause du refus signé du relais perdue (signature jamais lue ; code 3 sans cause, comme en v3)",
     "        if e.code in CAUSES_RELAIS and signe:", "        if False:"),
    ("N16", KIMI, "signature du relais ignorée (toute erreur lue refus du relais : cause et rien parti)",
     "        signe = refus_du_relais(corps_erreur)", "        signe = True"),
    ("N17", ARGON, "causes 402 et 429 permutées", CAUSES_RELAIS, 'CAUSES_RELAIS = {402: "relais_max_appels", 429: "relais_plafond"}'),
    ("N18", KIMI, "causes 402 et 429 permutées", CAUSES_RELAIS, 'CAUSES_RELAIS = {402: "relais_max_appels", 429: "relais_plafond"}'),
    ("N19", ARGON, "cause_refus sur tout refus HTTP du relais (403 compris)", CAUSE_RELAIS_ARGON,
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
    # --- contre-lecture de la v4 (contre-lecture-v4/mes-mutations.txt), transposées ; X6b ajoutée -------------------------------
    ("X1", KIMI, "signature du relais relâchée : toute chaîne `relais` vaut refus du relais", SIGNATURE,
     'return isinstance(objet, dict) and isinstance(objet.get("relais"), str)'),
    ("X2", KIMI, "signature du relais exacte « relais-kimi-v3 » (un relais v4 signé serait lu amont)", SIGNATURE,
     'return isinstance(objet, dict) and objet.get("relais") == "relais-kimi-v3"'),
    ("X3", KIMI, "corps d'erreur tronqué à 300 octets avant la lecture de la signature",
     "        corps_erreur = e.read()  # v4 (3)", "        corps_erreur = e.read()[:300]  # mutation X3 ; v4 (3)"),
    ("X4", ARGON, "OSError du registre lue garde_cumulee (RegistreIllisible inchangé)",
     '        return "garde_etape" if str(e).startswith(PREFIXE_GARDE_ETAPE) else "garde_cumulee"\n    return "registre_illisible"',
     '        return "garde_etape" if str(e).startswith(PREFIXE_GARDE_ETAPE) else "garde_cumulee"\n'
     '    if isinstance(e, OSError):\n        return "garde_cumulee"\n    return "registre_illisible"'),
    ("X5", ARGON, "refus d'argparse rendu en code 4 (que la v64 lirait « budget_depasse »)",
     '        rendre(2, erreur=f"arguments refusés par argparse (sortie {e.code})", envoye=False,',
     '        rendre(4, erreur=f"arguments refusés par argparse (sortie {e.code})", envoye=False,'),
    ("X6", KIMI, "clé d'étape non suffixée pour le seul proposeur",
     '    etape_registre = etape_du_registre(etape, "kimi")  # v4 (1)',
     '    etape_registre = etape if role == "proposeur_ideation" else etape_du_registre(etape, "kimi")  # mutation X6'),
    ("X6b", ARGON, "clé d'étape non suffixée pour le seul proposeur",
     '    etape_registre = etape_du_registre(etape, "argon")  # v4 (1)',
     '    etape_registre = etape if role == "proposeur_ideation" else etape_du_registre(etape, "argon")  # mutation X6b'),
    # --- propres à la règle de la v5 (B11, I33) --------------------------------------------------------------------------------
    ("R1", KIMI, "refus du registre rendu en code 4 (comportement v4)", REGISTRE_V5, REGISTRE_V5.replace("rendre(3,", "rendre(4,")),
    ("R2", ARGON, "refus du registre rendu en code 4 (comportement v4)", REGISTRE_V5, REGISTRE_V5.replace("rendre(3,", "rendre(4,")),
    ("R3", KIMI, "refus 402/429 signé du relais rendu en code 4 (comportement v4)", CAUSE_SIGNEE_V5,
     '            code, extra["cause_refus"] = 4, CAUSES_RELAIS[e.code]  # v5 (1)'),
    ("R4", ARGON, "refus 402/429 du relais rendu en code 4 (comportement v2 à v4)", FIN_RELAIS_ARGON_V5,
     "        fin(4 if e.code in (402, 429) else 3, cout=PLANCHER if avant else pire,"),
    ("R5", KIMI, "402/429 de l'amont transmis par le relais rendu en code 4 (lecture littérale écartée en v4)",
     "        code = 3 if e.code != 502 else 5\n", "        code = 4 if e.code in (402, 429) else (3 if e.code != 502 else 5)\n"),
    ("R6", KIMI, "modele_servi nul remis sur la ligne de code 4 (premier contrôle du plafond de session)", PREMIER_CONTROLE,
     'role=role, cause_refus="plafond_session", modele_servi=None)  # v3 (3), v4 (2)\n'),
    ("R7", ARGON, "modele_servi vide remis sur la ligne de code 4 (second contrôle du plafond de session)", SECOND_CONTROLE,
     'role=role,\n               cause_refus="plafond_session", modele_servi="")  # v3 (3), v4 (2)\n'),
    ("R8", KIMI, "refus remis sur la ligne de code 4 (second contrôle du plafond de session)",
     '               cause_refus="plafond_session")  # v3 (3), v4 (2)\n',
     '               cause_refus="plafond_session", refus=True)  # v3 (3), v4 (2)\n'),
    ("R9", ARGON, "stop_reason « refusal » remis sur la ligne de code 4 (premier contrôle du plafond de session)", PREMIER_CONTROLE,
     'role=role, cause_refus="plafond_session", stop_reason="refusal")  # v3 (3), v4 (2)\n'),
    ("R10", KIMI, "plafond_session rendu en code 3 (premier contrôle)",
     'rendre(4, erreur=f"pire cas au-dessus du plafond de session {plafond} USD (corps',
     'rendre(3, erreur=f"pire cas au-dessus du plafond de session {plafond} USD (corps'),
    ("R11", ARGON, "plafond_session rendu en code 3 (second contrôle)",
     '        rendre(4, erreur="pire cas au-dessus du plafond de session", envoye=False, role=role,',
     '        rendre(3, erreur="pire cas au-dessus du plafond de session", envoye=False, role=role,'),
    ("R12", KIMI, "refus du registre compté au pire cas, pas au plancher", "cause_refus=cause_du_registre(e), **diag)",
     "cause_refus=cause_du_registre(e), cout=pire, **diag)"),
    ("R13", ARGON, "envoye vrai sur un refus du registre (code 3)", REGISTRE_V5, REGISTRE_V5.replace("envoye=False", "envoye=True")),
    ("R14", ARGON, "garde d'étape seule rendue en code 4", REGISTRE_V5, registre_en_code_4_si("garde_etape")),
    ("R15", KIMI, "registre illisible seul rendu en code 4", REGISTRE_V5, registre_en_code_4_si("registre_illisible")),
    ("R16", ARGON, "429 du relais seul rendu en code 4", FIN_RELAIS_ARGON_V5,
     "        fin(4 if e.code == 429 else 3, cout=PLANCHER if avant else pire,"),
    ("R17", ARGON, "cause absente sur un refus 402/429 du relais (code 3 sans cause)", CAUSE_RELAIS_ARGON, "        extra = {}"),
    ("R18", KIMI, "garde cumulée seule rendue en code 4", REGISTRE_V5, registre_en_code_4_si("garde_cumulee")),
    ("R19", ARGON, "plafond_session rendu en code 3 (premier contrôle)",
     'rendre(4, erreur=f"pire cas au-dessus du plafond de session {plafond} USD ({len(prompt)} caractères)"',
     'rendre(3, erreur=f"pire cas au-dessus du plafond de session {plafond} USD ({len(prompt)} caractères)"'),
    ("R20", KIMI, "plafond_session rendu en code 3 (second contrôle)",
     '        rendre(4, erreur="pire cas au-dessus du plafond de session après point fixe"',
     '        rendre(3, erreur="pire cas au-dessus du plafond de session après point fixe"'),
    # --- contre-lecture de la v5 (cl5-v5/outils/mes_mutations_v1.py), transposées : constantes nommées --------------------------
    ("CL5-M1", KIMI, "400, 411 et 413 du relais rendus en code 4 par une constante nommée",
     [CONSTANTE_PROLOGUE, ("        code = 3 if e.code != 502 else 5\n",
                           "        code = CODE_LIMITE if e.code in (400, 411, 413) else (3 if e.code != 502 else 5)\n")]),
    ("CL5-M2", ARGON, "400, 411 et 413 du relais rendus en code 4 (constante dans le prologue, au-dessus de servir)",
     [CONSTANTE_PROLOGUE, (FIN_RELAIS_ARGON_V5, "        fin(CODE_LIMITE if e.code in (400, 411, 413) else 3, cout=PLANCHER if avant else pire,")]),
    ("CL5-M2b", ARGON, "400, 411 et 413 du relais rendus en code 4 (constante dans la partie appeler)",
     [CONSTANTE_APPELER, (FIN_RELAIS_ARGON_V5, "        fin(CODE_LIMITE if e.code in (400, 411, 413) else 3, cout=PLANCHER if avant else pire,")]),
    ("CL5-M3", ARGON, "échec de l'interface portant « 429 » rendu en code 4, envoye faux (constante dans le prologue)",
     [CONSTANTE_PROLOGUE, (ECHEC_INTERFACE, ECHEC_429_EN_4)]),
    ("CL5-M3b", ARGON, "échec de l'interface portant « 429 » rendu en code 4, envoye faux (constante dans appeler)",
     [CONSTANTE_APPELER, (ECHEC_INTERFACE, ECHEC_429_EN_4)]),
    # --- propres à la v6 ---------------------------------------------------------------------------------------------------------
    ("S1", KIMI, "réponse coupée en code 0 pour tous les rôles (proposeur compris)", COUPEE_KIMI, '    if fin_raison == "length":'),
    ("S2", ARGON, "réponse coupée en code 0 pour tous les rôles (proposeur compris)", COUPEE_ARGON,
     '    if statut == "TRONQUE" and origine == "usage":'),
    ("S3", KIMI, "réponse coupée de l'étage en code 5 (comportement v5)", ROLES_COUPEE, "ROLES_COUPEE_ADMISE = ()"),
    ("S4", ARGON, "vérificateur retiré des rôles à réponse coupée admise", ROLES_COUPEE, 'ROLES_COUPEE_ADMISE = ("experimentateur_test",)'),
    ("S5", KIMI, "statut coupee non écrit au registre (tronque)", FIN_COUPEE, FIN_COUPEE.replace('statut="coupee"', 'statut="tronque"')),
    ("S6", ARGON, "champ coupee absent de la ligne", FIN_COUPEE, FIN_COUPEE.replace("coupee=True, ", "")),
    ("S7", ARGON, "réponse coupée sans usage acceptée en code 0", COUPEE_ARGON, '    if statut == "TRONQUE" and role in ROLES_COUPEE_ADMISE:'),
    ("S8", KIMI, "texte d'une réponse coupée non rendu", FIN_COUPEE, FIN_COUPEE.replace("texte=texte", 'texte=""')),
    ("S9", KIMI, "ligne de cause retirée de la sortie d'erreur", LIGNE_CAUSE, "        pass\n"),
    ("S10", ARGON, "ligne de cause retirée de la sortie d'erreur", LIGNE_CAUSE, "        pass\n"),
    ("S11", KIMI, "registre corrompu hors des exceptions prises (code 1 sans ligne, v5)", EXCEPT_V6, EXCEPT_V5),
    ("S12", ARGON, "registre corrompu hors des exceptions prises (code 1 sans ligne, v5)", EXCEPT_V6, EXCEPT_V5),
    ("S13", KIMI, "erreur de l'amont transmise comptée rien parti, au plancher (v5)",
     "        avant_amont = e.code in (400, 402, 403, 411, 413, 429) and signe", "        avant_amont = e.code in (400, 402, 403, 411, 413, 429)"),
    ("S14", KIMI, "cause d'un refus du relais non écrite au registre (statut echec)", STATUT_KIMI,
     'erreur=f"HTTP {e.code} : {motif}", envoye=not avant_amont'),
    ("S15", ARGON, "cause d'un refus du relais non écrite au registre (statut echec)", STATUT_ARGON,
     'erreur=f"HTTP {e.code} : {motif}", envoye=not avant,'),
]


def copier_dossier(dossier):
    for f in FICHIERS:
        shutil.copy(os.path.join(ICI, f), os.path.join(dossier, f))


def remplacements(avant, apres):
    """Une mutation : un remplacement (avant, apres), ou une liste de remplacements (apres vaut alors None)."""
    return avant if apres is None else [(avant, apres)]


def muter(t, fichier, paires):
    for avant, apres in paires:
        n = t.count(avant)
        if n != 1:
            raise RuntimeError(f"mutation inapplicable : motif trouvé {n} fois dans {fichier} : {avant[:70]!r}")
        t = t.replace(avant, apres)
    return t


def appliquer(dossier, fichier, avant, apres=None):
    chemin = os.path.join(dossier, fichier)
    with open(chemin, encoding="utf-8") as f:
        t = muter(f.read(), fichier, remplacements(avant, apres))
    ast.parse(t, filename=fichier)  # une faute de syntaxe n'est jamais comptée « tuée » : elle arrête le banc
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(t)


def jouer_suite(dossier, arret_premier_echec):
    t0 = time.time()
    args = [PY, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", SUITE] + (
        ["-x", "--deselect", IDENTITE_SERVIR] if arret_premier_echec else [])  # v6 : l'identité ne juge pas une mutation
    p = subprocess.run(args, cwd=dossier, env=ENV, capture_output=True, timeout=900)
    sortie = p.stdout.decode("utf-8", "replace")
    resume = [l for l in sortie.splitlines() if " passed" in l or " failed" in l or " error" in l]
    premier = [l.split(" ", 1)[1].split(" - ")[0] for l in sortie.splitlines() if l.startswith(("FAILED ", "ERROR "))]
    return (p.returncode, (resume[-1].strip() if resume else sortie[-200:].strip()), round(time.time() - t0, 1),
            premier[0].replace(SUITE + "::", "") if premier else "—")


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--seulement", default="", help="identifiants de mutations, séparés par des virgules")
    args = a.parse_args(argv)
    if not os.environ.get("PYTHONPATH"):
        print("PYTHONPATH absent (dossier `orchestrator` de la copie du dépôt public, commit eaa74ca) : banc arrêté (R5)")
        return 1
    ENV["PYTHONPATH"] = os.environ["PYTHONPATH"]
    choisies = [m for m in MUTATIONS if not args.seulement or m[0] in args.seulement.split(",")]
    if len({m[0] for m in MUTATIONS}) != len(MUTATIONS):
        raise RuntimeError("identifiants de mutations en double")
    with tempfile.TemporaryDirectory(prefix="mutations-commandes-tf-v6-motifs-") as d:  # tous les motifs d'abord (aucune sautée)
        copier_dossier(d)
        for ident, fichier, _, *paire in choisies:
            t = open(os.path.join(d, fichier), encoding="utf-8").read()
            ast.parse(muter(t, fichier, remplacements(*paire) if len(paire) == 2 else paire[0]), filename=fichier)
    with tempfile.TemporaryDirectory(prefix="mutations-commandes-tf-v6-sain-") as sain:
        copier_dossier(sain)
        code, resume, duree, _ = jouer_suite(sain, False)
    print(f"cas sain (dossier non muté) : {'passe' if code == 0 else 'ÉCHOUE'} — {resume} ({duree} s)", flush=True)
    if code != 0:
        print("le cas sain échoue : banc arrêté (R5)")
        return 1
    lignes, tuees = [], 0
    for ident, fichier, quoi, *paire in choisies:
        with tempfile.TemporaryDirectory(prefix=f"mutations-commandes-tf-v6-{ident}-") as d:
            copier_dossier(d)
            appliquer(d, fichier, *(paire if len(paire) == 2 else (paire[0], None)))
            code, resume, duree, premier = jouer_suite(d, True)
        if code not in (0, 1):
            print(f"{ident} : pytest sort en code {code} (ni réussite ni échec d'essais) : banc arrêté")
            return 1
        tuee = code == 1 and premier != "—" and "test_bloc_servir_identique" not in premier
        tuees += tuee
        lignes.append(f"| {ident} | `{fichier}` | {quoi} | {'tuée' if tuee else 'SURVIT'} | {resume} | `{premier}` | {duree} s |")
        print(lignes[-1], flush=True)
    print(f"\nmutations tuées : {tuees} sur {len(choisies)} jouées")
    print("\n| id | fichier | mutation | sort | suite | premier essai qui échoue | durée |\n|---|---|---|---|---|---|---|\n"
          + "\n".join(lignes))
    return 0 if tuees == len(choisies) else 1


if __name__ == "__main__":
    sys.exit(principal())
