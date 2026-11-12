"""Remplit les « À REMPLIR » du brouillon 6 de la revalidation (T0.5) et écrit la version à sceller et sa configuration.
Version 4 (vérification 3 du remplissage, N-4, N-5, N-6, N-9, N-10) : nombre et durée des tests lus dans la sortie
archivée de la suite (archive tar et membre), comparés au compte du commit ; entrée de contre-lecture qui cite les trois
vérifications et énumère les changements faits après la dernière ; phrase du coût et de la condition de crédit reprise
des chiffres de P-6 ; en-tête qualifié ; ligne de date sans « UTC » redondant.
Version 3 (vérification 2 du remplissage, C-1 à C-6) : nombre de tests recompté au commit (pytest --collect-only),
date au format « AAAA-MM-JJ HH:MM UTC » proche de l'horloge, entropie lue dans son fichier, durée des tests au format
« 493,14 », chiffres de la réserve RV-5 recalculés sur les fichiers de tâches, sorties ouvertes en mode exclusif (R12),
entrée mécanique dans la section « Contre-lecture » (candidat relu et rapports, par leurs empreintes).
Version 2 (vérification 1 du remplissage, D-4, D-6, D-7, D-10 ; V-2, V-4) : arrêts explicites, empreintes lues au
commit cité (git show), commit cité = HEAD sur un arbre suivi propre, empreinte canonique recalculée sur le fichier écrit.

Usage : python -I remplir_revalidation_v4.py DEPOT COMMIT FICHIER_ENTROPIE MODE DATE_UTC ARCHIVE_TESTS MEMBRE_TESTS
        SORTIE_PREREG SORTIE_CONFIG CANDIDAT_RELU RAPPORT_1 RAPPORT_2 RAPPORT_3
MODE : reel (version scellée) ou jouet (répétition sur un dépôt jetable : couches et tailles réduites).
DUREE_TESTS : durée de la suite complète au commit cité sur la session, en secondes (texte, par exemple « 481,70 »)."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


def arret(msg: str) -> None:
    sys.exit(f"ARRÊT du remplissage : {msg}")


if len(sys.argv) != 14:
    arret("treize arguments attendus")
(depot, commit, f_entropie, mode, date, archive_tests, membre_tests, sortie_p, sortie_c, relu, rapport_1, rapport_2,
 rapport_3) = sys.argv[1:14]
D = Path(depot)
if not re.fullmatch(r"[0-9a-f]{40}", commit) or mode not in ("reel", "jouet"):
    arret("commit (40 hexadécimaux) ou mode (reel, jouet) invalide")
import tarfile  # noqa: E402
with tarfile.open(archive_tests) as tf:
    sortie_tests = tf.extractfile(membre_tests).read().decode("utf-8").strip().splitlines()[-1]
m_tests = re.fullmatch(r"(\d+) passed in (\d+)\.(\d{2})s( \(\d+:\d{2}:\d{2}\))?", sortie_tests)
if not m_tests:
    arret(f"dernière ligne de la suite archivée illisible : {sortie_tests!r}")
tests, duree_tests = m_tests.group(1), f"{m_tests.group(2)},{m_tests.group(3)}"
entropie = Path(f_entropie).read_text(encoding="utf-8").strip()
if not entropie.isdigit() or not 0 < int(entropie) < 2 ** 128:
    arret(f"entropie de {f_entropie} hors de ]0 ; 2^128[")
if mode == "reel":
    import datetime
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC", date):
        arret("date attendue au format « AAAA-MM-JJ HH:MM UTC »")
    ecart = abs((datetime.datetime.strptime(date, "%Y-%m-%d %H:%M UTC").replace(tzinfo=datetime.timezone.utc)
                 - datetime.datetime.now(datetime.timezone.utc)).total_seconds())
    if ecart > 3600:
        arret(f"date à {ecart:.0f} s de l'horloge (au plus 3 600 s)")
for f in (sortie_p, sortie_c):
    if Path(f).exists():
        arret(f"{f} existe déjà (R12)")


def git(*args: str) -> bytes:
    r = subprocess.run(["git", "-C", str(D), *args], capture_output=True)
    if r.returncode != 0:
        arret(f"git {' '.join(args)} : {r.stderr.decode(errors='replace').strip()}")
    return r.stdout


if mode == "reel":
    if git("rev-parse", "HEAD").decode().strip() != commit:
        arret("le commit cité n'est pas HEAD")
    if git("status", "--porcelain", "--untracked-files=no").strip():
        arret("arbre suivi non propre")


if mode == "reel":       # nombre de tests recompté au commit cité (HEAD, arbre propre) : vérification 2, C-1
    r = subprocess.run([sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider"], cwd=D,
                       capture_output=True, text=True, env={**__import__("os").environ, "PYTHONPATH": "src"})
    m = re.search(r"^(\d+) tests? collected", r.stdout, re.M)
    if r.returncode != 0 or not m or m.group(1) != tests:
        arret(f"tests collectés au commit : {m.group(1) if m else 'illisible'} ≠ {tests}")


def sha_au_commit(p: str) -> str:
    return hashlib.sha256(git("show", f"{commit}:{p}")).hexdigest()


sys.path.insert(0, str(D / "src"))
from controle_ia.manifeste import config_canonique  # noqa: E402

BROUILLON_CFG = "brouillons/T0.5-revalidation-config-v1-brouillon3.json"
BROUILLON = "brouillons/T0.5-revalidation-equivalence-pilote-v1-brouillon6.md"
octets_cfg = git("show", f"{commit}:{BROUILLON_CFG}")
config = json.loads(octets_cfg.decode("utf-8"))
if config.get("mode") != "reel":
    arret("le brouillon 3 de la configuration n'est pas en mode reel")
if mode == "jouet":          # le modèle jouet n'a que 4 couches ; taille réduite (répétition de la chaîne seulement)
    config.update(mode="jouet", couches=[0, 1, 2], T=2, max_nouveaux=8, lot=2, nombre_taches=4,
                  actions_min_comparees=4, actions_min_controle_negatif=1)
    config["chemin"] = dict(config["chemin"], T=2)
    config["controle_positif"] = dict(config["controle_positif"], T=2, actions_min=1)
cfg_sha = hashlib.sha256(config_canonique(config)).hexdigest()
RUN = "donnees/20261007-082440-t05-extraction"
ENT, EVA = f"{RUN}/taches-entrainement.json", f"{RUN}/taches-evaluation.json"
amorce, instance = sha_au_commit("scripts/amorce_instance_t05.sh"), sha_au_commit("scripts/pilote_t05_instance.sh")
b6 = git("show", f"{commit}:{BROUILLON}")
t = b6.decode("utf-8")


def rep(a: str, b: str) -> None:
    global t
    n = t.count(a)
    if n != 1:
        arret(f"cible trouvée {n} fois : {a[:80]!r}")
    t = t.replace(a, b)


entete_ancien = t.split("\n")[2]
if not entete_ancien.startswith("Brouillon 6 du 2026-10-07 (session 11), non scellé"):
    arret("en-tête du brouillon 6 inattendu")
rep(entete_ancien,
    f"Version scellée le {date} (session 11, reprise), depuis le brouillon 6 du 2026-10-07 "
    f"(`{BROUILLON}`, `{hashlib.sha256(b6).hexdigest()}` ; gardé tel quel avec les brouillons 1 à 5). Ce qui change : "
    "les champs laissés à remplir par le brouillon (lignes de la date, des tâches et du chemin de la configuration "
    "reformulées en conséquence) ; les empreintes des documents qui font foi, écrites en entier (RV-21) ; trois "
    "précisions de fait (la durée de la suite des tests au commit cité et le coût au pire cas, « Calcul » ; la "
    "réserve RV-5 connue d'avance, « Transparence ») et une condition de lancement (le crédit Vast.ai, « Calcul ») ; "
    "une garde d'arrêt ajoutée avant l'installation, la poussée initiale de la branche par le script de l'instance "
    "(« Machine », liste d'arrêt ; vérification du remplissage, D-2) ; aucun seuil, aucune lecture ne change. Le "
    "brouillon 6 traitait la relecture du différentiel du brouillon 5 (Z-1 à Z-6) ; l'historique des contre-lectures, "
    "vérification du remplissage comprise (une entrée ajoutée), est dans la dernière section.")
rep("- Date (UTC) : À REMPLIR (scellement : après l'extraction ; la lecture de P-007 est confirmée par Lazar le 2026-10-07, R-094 ; W-5).",
    f"- Date (UTC) : {date.removesuffix(' UTC')} (scellement : après l'extraction, assemblée le 2026-10-10, R-124 ; la lecture de P-007 est confirmée par Lazar le 2026-10-07, R-094 ; W-5).")
rep("- Commit du code d'analyse : `À REMPLIR`", f"- Commit du code d'analyse : `{commit}`")
rep("  - Tests attendus : `À REMPLIR` (toute", f"  - Tests attendus : `{tests}` (toute")
rep("`scripts/amorce_instance_t05.sh` (`À REMPLIR`, sha256) et `scripts/pilote_t05_instance.sh` (`À REMPLIR`, sha256)",
    f"`scripts/amorce_instance_t05.sh` (`{amorce}`, sha256) et `scripts/pilote_t05_instance.sh` (`{instance}`, sha256)")
rep("- Entropie : `À REMPLIR` (tirée au scellement", f"- Entropie : `{entropie}` (tirée au scellement")
rep("- Configuration de la revalidation (empreinte canonique) : `À REMPLIR`",
    f"- Configuration de la revalidation (empreinte canonique) : `{cfg_sha}`")
rep("- Chemin de la configuration : `prereg/T0.5-revalidation-config-v1.json` (brouillon : `brouillons/T0.5-revalidation-config-v1-brouillon3.json`)",
    f"- Chemin de la configuration : `prereg/T0.5-revalidation-config-v1.json` (copie scellée du brouillon `{BROUILLON_CFG}`)")
rep("- Tâches d'entraînement : `À REMPLIR` (empreinte sha256 du fichier assemblé par l'extraction)",
    f"- Tâches d'entraînement : `{sha_au_commit(ENT)}` (empreinte sha256 du fichier assemblé par l'extraction, run `20261007-082440-t05-extraction`)")
rep("- Chemin des tâches d'entraînement : `À REMPLIR` (`donnees/<run d'extraction>/taches-entrainement.json`, dans",
    f"- Chemin des tâches d'entraînement : `{ENT}` (dans")
rep("- Tâches d'évaluation : `À REMPLIR` (empreinte sha256 du fichier ;",
    f"- Tâches d'évaluation : `{sha_au_commit(EVA)}` (empreinte sha256 du fichier ;")
rep("- Chemin des tâches d'évaluation : `À REMPLIR` (`donnees/<run d'extraction>/taches-evaluation.json`, dans",
    f"- Chemin des tâches d'évaluation : `{EVA}` (dans")
for chemin, court in [("docs/brief-claude-code-programme-complet-v2.md", "9261932a"), ("docs/programme-controle-ia-v2.md", "2fd63bad"),
                      ("livrables/premier-rendu-v1/devis-v1.md", "16d71feb"), ("prereg/T0.4-validation-modele-reel-v3.md", "4f711cd3"),
                      ("docs/verdicts/verdict-T0.4-critere-1-G0-v3.md", "63444faa"),
                      ("docs/procedures/validation-T0.4-modele-reel-v4.md", "4482f7cc"),
                      ("docs/notes/memoire-noyau-math-T0.4-v3-v2.md", "2e4e9683"),
                      ("docs/notes/memoire-double-precision-T0.4-v1.md", "b013428a"),
                      ("docs/decisions/proposition-P-007-plan-G0-v1.md", "56b9182b"),
                      ("prereg/contre-lectures/T0.5-pilote-rapport-contre-lecture-1-v1.md", "9d8e3c81")]:
    plein = sha_au_commit(chemin)
    if not plein.startswith(court):
        arret(f"{chemin} : empreinte {plein[:12]} ≠ abrégé {court}")
    rep(f"`{chemin}` ({court}…)", f"`{chemin}` (`{plein}`)")
rep("- Documents qui font foi (chemin et sha256 complets au scellement) :", "- Documents qui font foi (chemin et sha256 complets) :")
rep("pire cas, le plafond de l'amorce (300 minutes), soit ≈ 5,5 USD plus le stockage.",
    "pire cas, le plafond de l'amorce (300 minutes), soit ≈ 5,5 USD plus le stockage ; aux prix des offres conformes "
    "relevées le 2026-10-10 (1,08 à 1,2133 USD l'heure tout compris), avec les cinq minutes avant le KILL, le démarrage "
    "et le téléchargement (≈ 0,55 USD) : ≈ 6,1 à 6,8 USD, plus le disque de l'instance arrêtée (vérification du "
    "remplissage, P-6 et N-5). Condition de lancement : un crédit Vast.ai d'au moins six heures au prix de l'offre "
    "retenue, plus 0,9 USD (téléchargement et marge ; vérification du remplissage, P-1 et N-6) ; sinon, rien ne se crée.")
from controle_ia.environnements.revalider_pilote_a import taches_d_entrainement  # noqa: E402

if mode == "reel":
    _, dom = taches_d_entrainement(str(D / ENT), str(D / EVA), int(config["nombre_taches"]))
else:                    # répétition : les chiffres du domaine réel (16 tâches), seulement pour le texte
    _, dom = taches_d_entrainement(str(D / ENT), str(D / EVA), 16)
if dom["couvre_le_pilote"]:
    arret("les énoncés retenus couvrent le pilote : la précision RV-5 ne vaut plus")


def nombre(x) -> str:
    entier, _, dec = f"{x:.1f}".partition(".")
    groupes = f"{int(entier):,}".replace(",", " ")
    return groupes if float(x) == int(float(x)) else f"{groupes},{dec}"


rep("La suite complète compte aujourd'hui 642 tests : 866 s sur le processeur de la session (message du commit `e6ce058` ; R-101), soit le plus gros poste.",
    "La suite complète compte aujourd'hui 642 tests : 866 s sur le processeur de la session (message du commit `e6ce058` ; R-101), soit le plus gros poste "
    f"(au commit cité : {tests} tests, {duree_tests} s dans un environnement neuf installé seulement depuis "
    f"`requirements-gpu.txt`, sur la session, le 2026-10-10 : répétition jouet de l'amorce, archive "
    f"`prereg/contre-lectures/{Path(archive_tests).name}`, fichier `{membre_tests}` ; vérification du remplissage, D-3 "
    "et N-9).")
rep("- Connu avant le scellement : les résultats de T0.4 v1 à v3 (cités).",
    "- Connu avant le scellement : les résultats de T0.4 v1 à v3 (cités). Connu aussi, parce que déterminé par les seuls "
    f"fichiers cités, sans aucun épisode : les 16 énoncés retenus (de {nombre(dom['longueur_min_choisies'])} à "
    f"{nombre(dom['longueur_max_choisies'])} caractères) ne couvrent pas le plus long énoncé du pilote "
    f"({nombre(dom['longueur_max_evaluation'])} caractères ; 90e centile : {nombre(dom['longueur_q90_evaluation'])}) ; "
    "la réserve RV-5 (« énoncés de la revalidation plus courts que le plus long du pilote ») est donc acquise d'avance, "
    "et la dernière proposition de H-domaine (« les énoncés joués couvrent ceux du pilote ») est connue fausse d'avance : "
    "elle n'entre pas dans R5, elle ne donne qu'une réserve (table des critères) (vérification du remplissage, V-2, "
    "D-6 et C-5).")
rep("aux règles du lanceur : une ligne, nom de base, empreinte (W-1, W-10 ; X-3).",
    "aux règles du lanceur : une ligne, nom de base, empreinte (W-1, W-10 ; X-3). Il pousse ensuite la branche neuve "
    "telle quelle : un refus (droit d'écriture du jeton, que la session ne peut pas éprouver) arrête là, code 2, avant "
    "l'installation (vérification du remplissage, D-2).")
rep("sceau non conforme aux règles du lanceur (une ligne, nom de base, empreinte) : arrêt consigné au journal, code 2.",
    "sceau non conforme aux règles du lanceur (une ligne, nom de base, empreinte) ; poussée initiale de la branche "
    "refusée (vérification du remplissage, D-2) : arrêt consigné au journal, code 2.")
def sha_fichier(f: str) -> str:
    return hashlib.sha256(Path(f).read_bytes()).hexdigest()


rep("- Contrôle mécanique des corrections du brouillon 6, que le relecteur juge suffisant, sans nouvelle relecture (R-102) :",
    "- Vérification du remplissage du brouillon 6, avant le scellement (2026-10-10), par des sous-agents neufs, en trois "
    "vérifications, chacune avec contre-vérification adverse de ses remarques graves ; rapports "
    f"`{Path(rapport_1).name}` (`{sha_fichier(rapport_1)}`), `{Path(rapport_2).name}` (`{sha_fichier(rapport_2)}`) et "
    f"`{Path(rapport_3).name}` (`{sha_fichier(rapport_3)}`), sous `prereg/contre-lectures/` ; candidat relu par la "
    f"troisième : `{sha_fichier(relu)}`. Leurs remarques sont citées ici avec le préfixe « vérification du remplissage » "
    "(D-, L-, V- : première ; C-, K-, P- : deuxième ; M-, N- : troisième). Le code cité porte les corrections des deux "
    "premières (signal TERM, dépendances de l'instance, garde de calcul, poussée initiale) ; la troisième n'a trouvé "
    "sur lui que des remarques mineures. Après la troisième, seuls ont changé : la date, cette entrée, l'en-tête "
    "(codes qualifiés, liste des précisions), la phrase du coût au pire cas et de la condition de crédit (N-5, N-6) et "
    "la durée des tests, remesurée, et sa provenance (N-9) ; registre des décisions.\n"
    "- Contrôle mécanique des corrections du brouillon 6, que le relecteur juge suffisant, sans nouvelle relecture (R-102) :")
if "À REMPLIR" in t:
    arret("« À REMPLIR » restant : " + "; ".join(x[:60] for x in t.splitlines() if "À REMPLIR" in x))
with open(sortie_p, "x", encoding="utf-8") as f:
    f.write(t)
with open(sortie_c, "xb") as f:     # mode « reel » : copie octet pour octet du brouillon 3, déjà en mode « reel »
    f.write(octets_cfg if mode == "reel" else (json.dumps(config, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
relu = json.loads(Path(sortie_c).read_text(encoding="utf-8"))
if hashlib.sha256(config_canonique(relu)).hexdigest() != cfg_sha:
    arret("l'empreinte canonique du fichier de configuration écrit diffère de l'empreinte citée")
print(json.dumps({"config_canonique": cfg_sha, "amorce": amorce, "instance": instance, "entrainement": sha_au_commit(ENT),
                  "evaluation": sha_au_commit(EVA)}, ensure_ascii=False))
