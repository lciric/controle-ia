"""Remplit les « À REMPLIR » du brouillon 10 du préenregistrement du pilote de T0.5 et écrit la version à sceller et sa
configuration (plan de lancement du pilote, étape 1). Chaque champ est remplacé par son contexte exact, une seule fois
(jamais de remplacement global ; AR-15). Les valeurs du verdict (noyau, durée projetée, `duree_max_s`) sont
recalculées ici depuis les résultats scellés de la revalidation v2, en rejouant la lecture gelée `lire_bras` (à 192
épisodes, elle doit redonner la lecture scellée ; à 180, l'option (a) de N-019 ; relecture R2, NO-04), et confrontées à
la proposition N-019 (PF-05, VR-05, PL-01) ; en mode reel, la décision de Lazar sur N-019 (GO de type « revendication »,
accordé par Lazar, qui cite N-019 et l'option (a), sans ligne « révocation » qui le nomme ; colonne d'état de N-019 à la
forme exacte « tranché (a) par Lazar : GO (R-…) » ; ligne R-… qui consigne le GO) est exigée (NO-03, CH-10) ; rien n'est
recopié à la main. Entrées lues sous leur sceau au commit, brouillon 10 et brouillon de configuration à leurs empreintes
attendues (CH-06). Préenregistrement scellé de la revalidation et sa configuration cités par chemin et empreinte
(vérification courte, VT-04).

Usage : python -I remplir_pilote_v1.py DEPOT COMMIT MODE DATE ENTROPIE SORTIE_PREREG SORTIE_CONFIG
        --taches CHEMIN --rapports-etat NOM=SHA[,NOM=SHA…] --rapports-relecture NOM=SHA[,…] --candidat-relu CHEMIN
        --go GO-AAAA-MM-JJ-NN --registre R-NNN   (mode reel ; ailleurs, valeurs factices masquées par la normalisation)
MODE : reel (version à sceller : COMMIT = HEAD, arbre suivi propre, date à moins d'une heure de l'horloge) ; candidat
(texte soumis à la relecture R2 : comme reel, sans exigence d'horloge ni de candidat relu ; les rapports de la relecture,
encore à venir, sont des paires factices non vérifiées) ; jouet (répétition sur un dépôt jetable : configuration réduite,
fichier de tâches réduit, aucune exigence d'horloge).
DATE : « AAAA-MM-JJ HH:MM UTC », dans tous les modes (CH-07). --taches : en modes reel et candidat, seul
donnees/t05-pilote-v1/taches-pilote-60-v1.json est admis (CH-07). ENTROPIE : fichier d'une ligne, entier dans ]0 ; 2^128[ (SeedSequence, R9).
--candidat-relu : texte relu par la relecture R2 (chemin sous brouillons/, au commit) ; mode reel : la version écrite
doit lui être égale une fois normalisée (champs du scellement masqués), sinon arrêt."""
import argparse
import datetime
import hashlib
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

BROUILLON = "brouillons/T0.5-pilote-8B-v1-brouillon10.md"
SHA_BROUILLON = "c3ee76a9f6d02e6f197dc397e0ddf1e2611038c52536212acfe2eabb97641bda"   # brouillon 10 scellé au commit (relecture R2, CH-06) : empreinte exigée
BROUILLON_CFG = "brouillons/T0.5-pilote-config-v1-brouillon1.json"
SHA_BROUILLON_CFG = "80d16f6e7a130586f03e4633b2935ed46c0f5f3ef722a55f737bfbe938fddebb"   # sans sceau (brouillons/) : empreinte exigée (CH-06)
TACHES = "donnees/t05-pilote-v1/taches-pilote-60-v1.json"   # modes reel et candidat : seul chemin admis (CH-07)
SOURCE_TACHES = "donnees/20261007-082440-t05-extraction/taches-evaluation.json"
SHA_SOURCE = "76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e"
RUN_REVAL = "20261011-225701-t05-revalidation-reel"
RESUME = f"diag/{RUN_REVAL}/resume.json"
MESURES = f"diag/{RUN_REVAL}/mesures-defaut.json"
MANIFESTE_REVAL = f"runs/{RUN_REVAL}/manifeste.json"
LECTURE = f"diag/{RUN_REVAL}/lecture-defaut.json"
VERDICT = "docs/verdicts/verdict-T0.5-revalidation-v2.md"
PREREG_REVAL = "prereg/T0.5-revalidation-equivalence-pilote-v2.md"   # R8, formule de duree_max_s (VT-04)
CONFIG_REVAL = "prereg/T0.5-revalidation-config-v1.json"
DECISION = "docs/decisions/decision-N-019-v1.md"         # retirée (R-145) : pièce scellée, contenu de l'option (a)
PROPOSITION = "docs/decisions/proposition-N-019-v2.md"   # proposition à Lazar (v2 ; la v1 est gardée) ; sa décision : GO cité
PLAN = "docs/procedures/pilote-T0.5-v1/plan-lancement-pilote-v3.md"
GO_FACTICE, REGISTRE_FACTICE = "GO-0000-00-00-00", "R-0"   # modes candidat et jouet : masqués par la normalisation
TACHES_PILOTE = 60
EPISODES_PAR_TACHE = 3
R8_MAX_S, PLAFOND_S, JUGES_S, FACTEUR = 7800, 15000, 7200, 1.2
DOCUMENTS = [  # (chemin, abrégé du brouillon ou None)
    ("docs/brief-claude-code-programme-complet-v2.md", "9261932a"), ("docs/programme-controle-ia-v2.md", "2fd63bad"),
    ("docs/decisions/proposition-P-006-T0.5-v1.md", "6fe36296"),
    ("docs/decisions/proposition-P-007-plan-G0-v1.md", "56b9182b"),
    ("docs/decisions/proposition-P-009-T0.6-organismes-v1.md", None),
    ("docs/decisions/proposition-P-010-T0.8-moniteur-par-action-v1.md", None),
    ("docs/procedures/T0.5-selection-papiers-v1.md", "8f43dcae"),
    ("runs/20261006-134235-t05-corpus/manifeste.json", "92612ab6"),
    ("diag/20261006-134235-t05-corpus/corpus.json", "57f0aa47"),
    ("docs/procedures/T0.5-extraction-v1.md", None),
    ("diag/20261007-082440-t05-extraction/bilan-extraction.json", None),
    ("docs/sources/invites-2606.08892-v1/index.json", None),
    ("prereg/T0.4-validation-modele-reel-v3.md", "4f711cd3"),
    ("docs/verdicts/verdict-T0.4-critere-1-G0-v3.md", "63444faa"),
]


def arret(msg: str) -> None:
    sys.exit(f"ARRÊT du remplissage du pilote : {msg}")


p = argparse.ArgumentParser()
for a in ("depot", "commit", "mode", "date", "entropie", "sortie_p", "sortie_c"):
    p.add_argument(a)
p.add_argument("--taches", required=True)
p.add_argument("--rapports-etat", required=True)
p.add_argument("--rapports-relecture", required=True)
p.add_argument("--candidat-relu", default=None)
p.add_argument("--go", default=None)
p.add_argument("--registre", default=None)
a = p.parse_args()
D = Path(a.depot)
if not re.fullmatch(r"[0-9a-f]{40}", a.commit) or a.mode not in ("reel", "candidat", "jouet"):
    arret("commit (40 hexadécimaux) ou mode (reel, candidat, jouet) invalide")
if not re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC", a.date):     # tous les modes (relecture R2, CH-07)
    arret("date attendue au format « AAAA-MM-JJ HH:MM UTC »")
if a.mode in ("reel", "candidat") and a.taches != TACHES:
    arret(f"--taches {a.taches!r} : seul {TACHES} est admis en modes reel et candidat (CH-07)")
if a.mode == "reel":
    ecart = abs((datetime.datetime.strptime(a.date, "%Y-%m-%d %H:%M UTC").replace(tzinfo=datetime.timezone.utc)
                 - datetime.datetime.now(datetime.timezone.utc)).total_seconds())
    if ecart > 3600:
        arret(f"date à {ecart:.0f} s de l'horloge (au plus 3 600 s)")
    if a.candidat_relu is None:
        arret("mode reel sans --candidat-relu")
    if not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", a.go or "") or not re.fullmatch(r"R-\d{3,4}", a.registre or ""):
        arret("mode reel : --go GO-AAAA-MM-JJ-NN et --registre R-NNN exigés (décision de Lazar sur N-019)")
elif a.go is not None or a.registre is not None:
    arret("--go et --registre : mode reel seulement")
entropie = Path(a.entropie).read_text(encoding="utf-8").strip()
if not entropie.isdigit() or not 0 < int(entropie) < 2 ** 128:
    arret(f"entropie de {a.entropie} hors de ]0 ; 2^128[")
for f in (a.sortie_p, a.sortie_c):
    if Path(f).exists():
        arret(f"{f} existe déjà (R12)")


def git(*args: str) -> bytes:
    r = subprocess.run(["git", "-C", str(D), *args], capture_output=True)
    if r.returncode != 0:
        arret(f"git {' '.join(args)} : {r.stderr.decode(errors='replace').strip()}")
    return r.stdout


def au_commit(chemin: str) -> bytes:
    return git("show", f"{a.commit}:{chemin}")


def sha_au_commit(chemin: str) -> str:
    return hashlib.sha256(au_commit(chemin)).hexdigest()


def scelle_au_commit(chemin: str) -> str:
    """Empreinte d'un fichier cité, exigée égale à son sceau compagnon au commit (R6)."""
    sha = sha_au_commit(chemin)
    sceau = au_commit(chemin + ".sha256").decode("utf-8").split()
    if not sceau or sceau[0] != sha or sceau[1:] != [Path(chemin).name]:
        arret(f"{chemin} : sceau absent ou différent au commit")
    return sha


def paires(texte: str) -> list[tuple[str, str]]:
    sortie = []
    for x in texte.split(","):
        nom, _, sha = x.strip().partition("=")
        if not nom or not re.fullmatch(r"[0-9a-f]{64}", sha):
            arret(f"paire de rapport mal formée : {x!r}")
        sortie.append((nom, sha))
    return sortie


if a.mode in ("reel", "candidat"):
    if git("rev-parse", "HEAD").decode().strip() != a.commit:
        arret("le commit cité n'est pas HEAD")
    if git("status", "--porcelain", "--untracked-files=no").strip():
        arret("arbre suivi non propre")

sys.path.insert(0, str(D / "src"))
from controle_ia.environnements.lancer_pilote_a import empreinte_config  # noqa: E402
from controle_ia.environnements.revalider_pilote_a import (EPISODES_PILOTE, choisir_noyau,  # noqa: E402
                                                           duree_projetee_pilote, lire_bras)

# --- verdict de la revalidation : résultats scellés relus, R8 appliquée au pilote réduit (N-019) ------------------
res = json.loads(au_commit(RESUME))["resultat"]
mes = json.loads(au_commit(MESURES))["resultat"]
lec_complete = json.loads(au_commit(LECTURE))["resultat"]
lec = lec_complete["lecture"]
for chemin in (RESUME, MESURES, LECTURE, VERDICT, DECISION, PROPOSITION, MANIFESTE_REVAL,
               f"diag/{RUN_REVAL}/lecture-math.json"):
    scelle_au_commit(chemin)
if res.get("noyau_retenu") is not None or res.get("noeud") is not True:
    arret("le résumé de la revalidation ne conclut pas au nœud : N-019 ne s'applique pas")
manquants = [k for k in ("R1_garde_saine", "R1_marge", "R3_seuil_fonde", "R4_rejeu", "R5_domaine_couvert",
                         "R6_chemin_defaut", "R7_memoire", "audit_conforme", "garde_zone_generee_conforme")
             if lec.get(k) is not True]
if manquants or lec.get("R2_controle_negatif") != "conforme" or lec.get("R8_duree") is not False:
    arret(f"bras « defaut » : la prémisse de N-019 (tout conforme sauf R8) ne tient pas ({manquants})")
chrono = mes["chrono"]
d_reval = mes["duree_projetee_episodes_pilote_s"]
if EPISODES_PILOTE != 192 or duree_projetee_pilote(chrono, 16) != d_reval:
    arret("durée projetée scellée ≠ duree_projetee_pilote(chrono, 16) à 192 épisodes")
config_reval = json.loads(au_commit(MANIFESTE_REVAL))["config"]
lecture_math = json.loads(au_commit(f"diag/{RUN_REVAL}/lecture-math.json"))["resultat"]["lecture"]


def lire(duree_s: float) -> dict:
    """Lecture gelée du bras « defaut » (`lire_bras` du code cité), entrées scellées, durée projetée donnée."""
    chemin = lec_complete.get("chemin")
    return lire_bras(mes["mesures"], mes["controle_negatif"], lec_complete["repere"], mes["rejeu_identique"],
                     config_reval, zone_generee=lec_complete["zone_generee"], audit=lec_complete["audit"],
                     chemin=chemin["lecture"] if chemin else None, bras="defaut",
                     memoire_pic_gio=mes["memoire_pic_gio"], duree_projetee_s=duree_s)


# à 192 épisodes, la lecture rejouée redonne la lecture scellée, et le nœud (aucun noyau, aucune proposition)
if lire(d_reval) != lec or choisir_noyau({"defaut": lec, "math": lecture_math}) != (None, None):
    arret("lecture gelée rejouée à 192 épisodes ≠ lecture scellée, ou issue scellée autre que le nœud")
# option (a) de N-019 : la formule de R8 avec 180 épisodes au lieu de la constante 192 (écart nommé, NO-01)
d = (chrono["generation_s"] + chrono["passe_unique_s"]) * TACHES_PILOTE * EPISODES_PAR_TACHE / 16
if not d <= R8_MAX_S:
    arret(f"durée projetée du pilote réduit {d:.2f} s > {R8_MAX_S} s")
duree_max = min(PLAFOND_S, math.ceil((FACTEUR * d + JUGES_S) / 60) * 60)
lec_180 = lire(d)
change = sorted(k for k in set(lec) | set(lec_180) if lec.get(k) != lec_180.get(k))
if change != ["R8_duree", "conforme", "conforme_avec_marge"]:
    arret(f"lecture à 180 épisodes : clés changées {change} (attendu : R8_duree, conforme, conforme_avec_marge)")
noyau, prop = choisir_noyau({"defaut": lec_180, "math": lecture_math})
if noyau != "defaut":
    arret(f"choix du noyau sur le pilote réduit : {noyau!r} ({prop})")
proposition = au_commit(PROPOSITION).decode("utf-8")
if "7 584,02 s ≤ 7 800 s" not in proposition or "15 000 s" not in proposition or "noyau « defaut »" not in proposition:
    arret("la proposition N-019 ne porte pas les valeurs recalculées (7 584,02 s ; 15 000 s ; noyau « defaut »)")
if f"{d:.2f}" != "7584.02" or duree_max != 15000:
    arret(f"valeurs recalculées {d:.2f} s et {duree_max} s ≠ celles de N-019")
reserves = res.get("reserves") or []
if any("RV-5" not in r for r in reserves) or not reserves:
    arret(f"réserves du verdict inattendues : {reserves}")
# part des actions à zone générée sous 1 % du bras retenu : `lecture-defaut.json` → resultat.zone_generee (verdict,
# section 5) ; obligatoire, aucun repli silencieux (R5)
part_sous_1pc = json.loads(au_commit(LECTURE))["resultat"].get("zone_generee", {}).get("part_zone_generee_sous_1pc")
if not isinstance(part_sous_1pc, (int, float)) or not 0 <= part_sous_1pc <= 0.2:
    arret(f"part des actions à zone générée sous 1 % absente ou au-dessus de 0,2 : {part_sous_1pc}")

# --- tâches : fichier dérivé, égal aux 60 premières de la source -------------------------------------------------
sha_taches = scelle_au_commit(a.taches)
derive = json.loads(au_commit(a.taches))
if a.mode in ("reel", "candidat"):
    if scelle_au_commit(SOURCE_TACHES) != SHA_SOURCE:
        arret("source des tâches : empreinte inattendue")
    source = json.loads(au_commit(SOURCE_TACHES))["resultat"]["taches"]
    if derive.get("source", {}).get("sha256") != SHA_SOURCE or derive["taches"] != source[:TACHES_PILOTE] \
            or len(derive["taches"]) != TACHES_PILOTE:
        arret("fichier dérivé des tâches ≠ 60 premières tâches de la source")

# --- configuration ------------------------------------------------------------------------------------------------
if sha_au_commit(BROUILLON_CFG) != SHA_BROUILLON_CFG:
    arret(f"{BROUILLON_CFG} : empreinte ≠ {SHA_BROUILLON_CFG[:12]}… (CH-06)")
config = json.loads(au_commit(BROUILLON_CFG).decode("utf-8"))
if config.get("mode") != "reel" or not str(config.get("duree_max_s", "")).startswith("À REMPLIR") \
        or not str(config.get("noyau_attention", "")).startswith("À REMPLIR"):
    arret("brouillon de la configuration inattendu")
config.update(noyau_attention=noyau, duree_max_s=duree_max)
if a.mode == "jouet":          # répétition sur processeur : modèle jouet, tailles réduites (chaîne seulement)
    config.update(mode="jouet", T=2, max_nouveaux=8, lot=2, couches=[0, 1, 2], max_nouveaux_juge=6, lot_juge=2,
                  lot_appariement=4)
    # le tokeniseur jouet n'a pas l'ouverture datée du gabarit réel : la garde du format (controler_format) arrêterait
    # la répétition dès le début (répétition du 2026-10-12, passage 1) ; seul le mode jouet perd ce champ
    for spec in [config["agent"], *config["juges"]]:
        spec.pop("texte_attendu_ouverture", None)
cfg_sha = empreinte_config(config)
amorce, instance = sha_au_commit("scripts/amorce_instance_t05.sh"), sha_au_commit("scripts/pilote_t05_instance.sh")
if a.mode in ("reel", "candidat"):
    # la collecte se fait dans l'arbre de travail : il doit être le commit cité, sans modification suivie
    if git("rev-parse", "HEAD").decode().strip() != a.commit or git("status", "--porcelain", "--untracked-files=no").strip():
        arret("arbre de travail ≠ commit cité (tête ou fichiers suivis modifiés) : collecte des tests non représentative")
    r = subprocess.run([sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider"], cwd=D,
                       capture_output=True, text=True, env={**os.environ, "PYTHONPATH": "src"})
    m = re.search(r"^(\d+) tests? collected", r.stdout, re.M)
    if r.returncode != 0 or not m:
        arret("collecte des tests illisible")
    tests = m.group(1)
else:
    tests = os.environ.get("TESTS_JOUET", "0")

# --- décision de Lazar sur N-019 (NO-03) : registres au commit ; mode reel seulement --------------------------------
if a.mode == "reel":
    lignes_go = au_commit("registres/go.md").decode("utf-8").split("\n")
    cellules = [[c.strip() for c in x.strip().strip("|").split("|")] for x in lignes_go if x.startswith(f"| {a.go} |")]
    if len(cellules) != 1 or len(cellules[0]) != 8:
        arret(f"{a.go} : absent de registres/go.md, en double ou mal formé")
    ident, accorde, typ, perimetre, plafond, echeance, par, ref = cellules[0]
    if typ != "revendication" or par != "Lazar" or "N-019" not in perimetre or "(a)" not in perimetre:
        arret(f"{a.go} : type {typ!r}, accordé par {par!r}, ou périmètre sans N-019 et l'option (a)")
    g = a.go          # révocation lue par cellules (vérification courte, VH-05)
    revocations = [l for l in lignes_go if l.startswith("| GO-") and (lambda c: (len(c) == 8 and c[2].lower() == "révocation" and (g in c[3] or g in c[7])) or (len(c) != 8 and "révocation" in l.lower() and g in l))([x.strip() for x in l.strip().strip("|").split("|")])]
    if revocations:
        arret(f"{a.go} révoqué dans registres/go.md")
    lignes_dec = au_commit("registres/decisions.md").decode("utf-8").split("\n")
    n19 = [x for x in lignes_dec if x.startswith("| N-019 |")]
    etat19 = n19[0].rsplit("|", 2)[-2].strip() if len(n19) == 1 else ""
    # forme exacte de la colonne d'état (relecture R2, CH-10) ; une révocation est une ligne « révocation » de go.md
    if not re.fullmatch(rf"tranché \(a\) par Lazar : {re.escape(a.go)} \({re.escape(a.registre)}\)", etat19):
        arret(f"N-019 : colonne d'état ≠ « tranché (a) par Lazar : {a.go} ({a.registre}) »")
    reg = [x for x in lignes_dec if x.startswith(f"| {a.registre} |")]
    if len(reg) != 1 or a.go not in reg[0]:
        arret(f"{a.registre} : ligne absente, en double ou sans {a.go}")
    go, registre = a.go, a.registre
else:
    go, registre = GO_FACTICE, REGISTRE_FACTICE

# --- texte --------------------------------------------------------------------------------------------------------
if not re.fullmatch(r"[0-9a-f]{64}", SHA_BROUILLON) or scelle_au_commit(BROUILLON) != SHA_BROUILLON:
    arret(f"{BROUILLON} : empreinte non épinglée ou ≠ {SHA_BROUILLON[:12]}… (CH-06)")
b8 = au_commit(BROUILLON)
t = b8.decode("utf-8")


def rep(x: str, y: str) -> None:
    global t
    n = t.count(x)
    if n != 1:
        arret(f"cible trouvée {n} fois : {x[:90]!r}")
    t = t.replace(x, y)


def nombre(x: float, dec: int = 2) -> str:
    entier, _, frac = f"{x:.{dec}f}".partition(".")
    groupes = f"{int(entier):,}".replace(",", " ")
    return groupes + ("," + frac if frac and dec else "")


rep("# Préenregistrement — T0.5, pilote 8B de l'environnement (a) — v1 — brouillon 10\n",
    "# Préenregistrement — T0.5, pilote 8B de l'environnement (a) — v1\n")
l3 = t.split("\n")[2]
if not l3.startswith("- Auteur : la session de mise en œuvre du programme de Lazar ; brouillon 10 du 2026-10-12"):
    arret("ligne d'auteur du brouillon 10 inattendue")
rep(l3, l3.replace("- Auteur : la session de mise en œuvre du programme de Lazar ; brouillon 10",
                   f"- Auteur : la session de mise en œuvre du programme de Lazar ; version scellée le {a.date}, "
                   f"depuis le brouillon 10 (`{BROUILLON}`, `{hashlib.sha256(b8).hexdigest()}`) : marqueurs de "
                   "remplissage remplis, empreintes abrégées complétées, titre, date, intitulé des documents qui font foi "
                   "et ligne des rapports ajustés (VT-13) ; brouillon 10", 1))
rep("- Date (UTC) : À REMPLIR (scellement : après l'extraction, N-014 et le verdict de la revalidation).",
    f"- Date (UTC) : {a.date.removesuffix(' UTC')} (scellement : après l'extraction, N-014, le verdict de la "
    "revalidation et N-019).")
rep("- Commit du code d'analyse : `À REMPLIR`", f"- Commit du code d'analyse : `{a.commit}`")
rep("- Décision de Lazar sur N-019 : `À REMPLIR` (GO de type", f"- Décision de Lazar sur N-019 : `{go}` ({registre}) "
    "(GO de type")
rep("`scripts/amorce_instance_t05.sh` (`À REMPLIR`, sha256) et `scripts/pilote_t05_instance.sh` (`À REMPLIR`, sha256)",
    f"`scripts/amorce_instance_t05.sh` (`{amorce}`, sha256) et `scripts/pilote_t05_instance.sh` (`{instance}`, sha256)")
rep("- Entropie : `À REMPLIR` (tirée au scellement", f"- Entropie : `{entropie}` (tirée au scellement")
rep("- Configuration du pilote (empreinte canonique) : `À REMPLIR`",
    f"- Configuration du pilote (empreinte canonique) : `{cfg_sha}`")
rep("- Tâches du pilote : `À REMPLIR` (empreinte", f"- Tâches du pilote : `{sha_taches}` (empreinte")
rep("- Chemin des tâches : `À REMPLIR` (fichier dérivé", f"- Chemin des tâches : `{a.taches}` (fichier dérivé")
rep("- Tests attendus : `À REMPLIR` (toute", f"- Tests attendus : `{tests}` (toute")
rep("verdict de la revalidation courte : `À REMPLIR` ; proposition N-019 : `À REMPLIR` (elle remplace la décision "
    "`docs/decisions/decision-N-019-v1.md`,",
    f"verdict de la revalidation courte : `{VERDICT}` (`{scelle_au_commit(VERDICT)}`) ; proposition N-019 : "
    f"`{PROPOSITION}` (`{scelle_au_commit(PROPOSITION)}`) (elle remplace la décision `{DECISION}` "
    f"(`{scelle_au_commit(DECISION)}`),")
rep("  - noyau d'attention du pilote : `À REMPLIR` ; durée projetée des épisodes du pilote (formule de R8 avec 180 "
    "épisodes au lieu de 192, (génération + passes uniques) × 180 / 16, aux mesures scellées du bras retenu ; la "
    "fonction `duree_projetee_pilote` du code cité garde 192 ; TX-11) : `À REMPLIR` s ; `duree_max_s` (formule "
    "gelée) : `À REMPLIR` s ;",
    f"  - noyau d'attention du pilote : `{noyau}` ; durée projetée des épisodes du pilote (formule de R8 avec 180 "
    "épisodes au lieu de 192, (génération + passes uniques) × 180 / 16, aux mesures scellées du bras retenu, "
    f"`{MESURES}`, `{scelle_au_commit(MESURES)}` ; la fonction `duree_projetee_pilote` du code cité garde 192 ; "
    f"TX-11) : `{nombre(d)}` s ; `duree_max_s` (formule gelée) : `{nombre(duree_max, 0)}` s ;")
texte_reserves = (" ; ".join(reserves) + f" ; part des actions à zone générée sous 1 % au bras retenu : "
                  f"{nombre(part_sous_1pc, 2)} (seuil de réserve 0,2 ; `{LECTURE}`)")
rep("  - réserves du verdict, reprises ici : `À REMPLIR` ;", f"  - réserves du verdict, reprises ici : {texte_reserves} ;")
rep("  - plan de lancement du pilote : `À REMPLIR` (remplace", f"  - plan de lancement du pilote : `{PLAN}` "
    f"(`{scelle_au_commit(PLAN)}`) (remplace")
rep("- Documents qui font foi (chemin et sha256 complets au scellement) :", "- Documents qui font foi (chemin et sha256 "
    "complets) :")
for chemin, court in DOCUMENTS:
    plein = scelle_au_commit(chemin)
    if court is not None and not plein.startswith(court):
        arret(f"{chemin} : empreinte {plein[:12]} ≠ abrégé {court}")
rep("  - `docs/brief-claude-code-programme-complet-v2.md` (9261932a…) et `docs/programme-controle-ia-v2.md` (2fd63bad…) ;",
    f"  - `docs/brief-claude-code-programme-complet-v2.md` (`{scelle_au_commit(DOCUMENTS[0][0])}`) et "
    f"`docs/programme-controle-ia-v2.md` (`{scelle_au_commit(DOCUMENTS[1][0])}`) ;")
rep("(R-085 ; proposition 6fe36296…)", f"(R-085 ; proposition `{DOCUMENTS[2][0]}`, `{scelle_au_commit(DOCUMENTS[2][0])}`)")
rep("  - P-007 (56b9182b…), retenue", f"  - P-007 (`{DOCUMENTS[3][0]}`, `{scelle_au_commit(DOCUMENTS[3][0])}`), retenue")
rep("  - P-009 et P-010 (usagers", f"  - P-009 (`{DOCUMENTS[4][0]}`, `{scelle_au_commit(DOCUMENTS[4][0])}`) et P-010 "
    f"(`{DOCUMENTS[5][0]}`, `{scelle_au_commit(DOCUMENTS[5][0])}`) (usagers")
rep("  - règle de sélection (8f43dcae…), run de sélection `20261006-134235-t05-corpus` (manifeste 92612ab6…, corpus "
    "57f0aa47…) ;",
    f"  - règle de sélection (`{DOCUMENTS[6][0]}`, `{scelle_au_commit(DOCUMENTS[6][0])}`), run de sélection "
    f"`20261006-134235-t05-corpus` (manifeste `{DOCUMENTS[7][0]}`, `{scelle_au_commit(DOCUMENTS[7][0])}` ; corpus "
    f"`{DOCUMENTS[8][0]}`, `{scelle_au_commit(DOCUMENTS[8][0])}`) ;")
rep("  - procédure d'extraction v1 (`À REMPLIR`) et son bilan (`À REMPLIR`) ;",
    f"  - procédure d'extraction v1 (`{DOCUMENTS[9][0]}`, `{scelle_au_commit(DOCUMENTS[9][0])}`) et son bilan "
    f"(`{DOCUMENTS[10][0]}`, `{scelle_au_commit(DOCUMENTS[10][0])}`) ;")
rep("  - index des invites transcrites (`docs/sources/invites-2606.08892-v1/index.json`, `À REMPLIR`) ;",
    f"  - index des invites transcrites (`{DOCUMENTS[11][0]}`, `{scelle_au_commit(DOCUMENTS[11][0])}`) ;")
rep("  - T0.4 v3 : préenregistrement (4f711cd3…) et verdict (63444faa… :",
    f"  - T0.4 v3 : préenregistrement (`{DOCUMENTS[12][0]}`, `{scelle_au_commit(DOCUMENTS[12][0])}`) et verdict "
    f"(`{DOCUMENTS[13][0]}`, `{scelle_au_commit(DOCUMENTS[13][0])}` :")
rep("Durée projetée des épisodes au débit mesuré par la revalidation (bras « defaut », 180 épisodes ; N-019 ; formule "
    "de R8 avec 180 au lieu de 192, TX-11) : `À REMPLIR` s.",
    "Durée projetée des épisodes au débit mesuré par la revalidation (bras « defaut », 180 épisodes ; N-019 ; formule "
    f"de R8 avec 180 au lieu de 192, TX-11) : {nombre(d)} s.")
rep("; au commit cité, `À REMPLIR` tests),", f"; au commit cité, {tests} tests),")
rep("  - `duree_max_s` (`À REMPLIR` s, par la formule gelée", f"  - `duree_max_s` ({nombre(duree_max, 0)} s, par la "
    "formule gelée")
etat = paires(a.rapports_etat)
rep("synthèse et critique de complétude ; rapports `À REMPLIR`.",
    "synthèse et critique de complétude ; rapports " + " ; ".join(
        f"`prereg/contre-lectures/{n}` (`{s}`)" for n, s in etat) + ".")
rel = paires(a.rapports_relecture)
rep("- Relecture R2 du brouillon 8 et du différentiel du code depuis la relecture b6 (`e6ce058`), puis vérifications "
    "courtes des candidats suivants et du différentiel du code depuis le candidat 1 (`942c65e`) : `À REMPLIR`.",
    "- Relecture R2 du brouillon 8 et du différentiel du code depuis la relecture b6 (`e6ce058`), puis vérifications "
    "courtes des candidats suivants et du différentiel du code depuis le candidat 1 (`942c65e`), par des sous-agents "
    "neufs : rapports " + " ; ".join(f"`prereg/contre-lectures/{n}` (`{s}`)" for n, s in rel) + ".")
rep(f"(`{PREREG_REVAL}`, `À REMPLIR` ;", f"(`{PREREG_REVAL}`, `{scelle_au_commit(PREREG_REVAL)}` ;")
rep(f"(`{CONFIG_REVAL}`, `À REMPLIR`)", f"(`{CONFIG_REVAL}`, `{scelle_au_commit(CONFIG_REVAL)}`)")
for n, s in etat + (rel if a.mode == "reel" else []):
    if a.mode in ("reel", "candidat") and scelle_au_commit(f"prereg/contre-lectures/{n}") != s:
        arret(f"rapport {n} : empreinte citée ≠ sceau au commit")
if "À REMPLIR" in t:
    arret("« À REMPLIR » restant : " + "; ".join(x[:70] for x in t.splitlines() if "À REMPLIR" in x))


import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location("normaliser_pilote_v1", Path(__file__).resolve().parent / "normaliser_pilote_v1.py")
_norm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_norm)            # normalisation partagée avec les contrôles avant dépense (une seule source)
normaliser = _norm.normaliser


if a.mode == "reel":
    relu = au_commit(a.candidat_relu).decode("utf-8")
    if normaliser(relu) != normaliser(t):
        arret("version écrite ≠ candidat relu, hors des champs du scellement")
with open(a.sortie_p, "x", encoding="utf-8") as f:
    f.write(t)
with open(a.sortie_c, "x", encoding="utf-8") as f:
    f.write(json.dumps(config, ensure_ascii=False, indent=2) + "\n")
if empreinte_config(json.loads(Path(a.sortie_c).read_text(encoding="utf-8"))) != cfg_sha:
    arret("empreinte canonique du fichier de configuration écrit ≠ empreinte citée")
print(json.dumps({"prereg_sha256": hashlib.sha256(t.encode("utf-8")).hexdigest(), "config_canonique": cfg_sha,
                  "noyau": noyau, "d_s": round(d, 4), "duree_max_s": duree_max, "tests": tests, "taches": sha_taches,
                  "normalise_sha256": hashlib.sha256(normaliser(t).encode("utf-8")).hexdigest()}, ensure_ascii=False))
