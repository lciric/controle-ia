"""Écrit la version 2 du préenregistrement de la revalidation (T0.5) depuis la v1 scellée — révision 4 du générateur,
après le contrôle mécanique des dernières corrections (R-137 : CM-01 incise de la transparence, CM-05 trois candidats
cités, relu, vérifié et final, CM-07 rapports attendus complets et bien formés). Révision 3 : après la vérification des
corrections (R-136 : VT-01, VT-03 à VT-11, VC-01 à VC-04, VC-07, VC-10). Révision 2 : après la relecture R2 du candidat 2
(R-135).

Ne change de la v1 que : le titre ; l'en-tête (motif, ce qui change, en-tête de la v1 recopié) ; l'auteur et la date ;
le commit du code cité ; la mention de l'origine de l'entropie ; la ligne « Lancement » (PREREG, BRANCHE) ; la durée de
la suite au commit cité et les mesures de la tentative de la v1 (« Calcul ») ; une ligne de transparence ; une entrée
d'historique, en dernier dans la section « Contre-lecture », dont la fin « Pièces : … » est la seule partie variable
entre le candidat vérifié et la version scellée (avec la première date des lignes 3 et 8).

Arrêts (R5), avant toute écriture : commit cité = 6ec7434 (VT-11) ; v1 intacte ; arbre suivi propre ; ascendance
3b8c049 → commit → HEAD ; dans l'arbre gelé, seul le test M-1 change depuis la v1, rien depuis le commit cité ;
empreintes des deux scripts de l'instance égales à celles de la v1 ; chaque fichier cité suivi à HEAD et conforme à son
sceau (compagnon `.sha256` ou ligne de `empreintes.sha256` ; VT-10) ; suite lisible, au nombre de tests de la v1
(recompté à HEAD en mode reel). En mode reel (VT-02, VC-01 à VC-04) : date à moins d'une heure de l'horloge ; épingles
lues dans le script des contrôles donné (`--controles`) ; candidats relu, vérifié et final suivis à HEAD sous
`brouillons/`, scellés, aux empreintes épinglées, le final égal, une fois normalisé, à l'empreinte normalisée épinglée ;
rapports attendus (paires nom=empreinte épinglées, bien formées, sans doublon, égales à l'ensemble des rapports de la v2
présents à HEAD) suivis à HEAD, scellés, aux empreintes épinglées ; GO de la forme
GO-AAAA-MM-JJ-NN, ligne de `registres/go.md` de type « revendication », accordée par Lazar, qui cite N-018, sans
révocation ; ligne N-018 tranchée, qui cite ce GO et l'option (a) ; lignes de corrections et ligne du GO présentes dans
`registres/decisions.md`, la seconde citant le GO ; fin « Pièces » reconstruite exactement comme la reconstruisent les
contrôles. Sortie en mode exclusif (R12).

Usage : python -I remplir_revalidation_v2_r3.py DEPOT COMMIT MODE DATE_UTC SORTIE
        [--controles F --candidat-relu CHEMIN --candidat-verifie CHEMIN --candidat-final CHEMIN --go GO-… --registre R-…]
MODE : reel (version à sceller) ou essai (candidat : la fin « Pièces » vaut « (remplies au scellement) »)."""
import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path


def arret(msg: str) -> None:
    sys.exit(f"ARRÊT du remplissage de la v2 : {msg}")


ap = argparse.ArgumentParser()
for nom in ("depot", "commit", "mode", "date", "sortie"):
    ap.add_argument(nom)
for opt in ("--controles", "--candidat-relu", "--candidat-verifie", "--candidat-final", "--go", "--registre"):
    ap.add_argument(opt)
a = ap.parse_args()
D = Path(a.depot)
V1 = "prereg/T0.5-revalidation-equivalence-pilote-v1.md"
V2 = "prereg/T0.5-revalidation-equivalence-pilote-v2.md"
BRANCHE = "calcul/t05-revalidation-reel-v2"
ANCIEN = "3b8c049bec316272b4f65a0e51ef54a2c1e83217"
COMMIT_ATTENDU = "6ec7434119781a3abebac789174101b9ed6ae087"
TEST_CORRIGE = "tests/test_validation_reelle.py"
SUITE = "docs/procedures/revalidation-T0.5-v2/suite-6ec7434-environnement-neuf-v1.txt"
ENVIRONNEMENT = "docs/procedures/revalidation-T0.5-v2/environnement-suite-6ec7434-v1.txt"
PROCESSEUR = "traces/t05-instance-55292763-processeur-20261011/processeur.json"
TESTS_INSTANCE = "traces/t05-20261010-223801-JOkW/tests.txt"
JOURNAL_INSTANCE = "traces/t05-instance-55292763-20261010-224000/journal-instance.txt"
REPETITION = "prereg/contre-lectures/T0.5-revalidation-v2-repetition-jouet-v3-passage4-interrompu-v1.tar"
CORRECTIONS = "R-135 et R-136 et R-137"
if a.commit != COMMIT_ATTENDU or a.mode not in ("reel", "essai"):
    arret(f"commit ({COMMIT_ATTENDU[:7]} attendu) ou mode (reel, essai) invalide")
if Path(a.sortie).exists():
    arret(f"{a.sortie} existe déjà (R12)")
if not re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC", a.date):
    arret("date attendue au format « AAAA-MM-JJ HH:MM UTC »")
if a.mode == "reel":
    import datetime
    ecart = abs((datetime.datetime.strptime(a.date, "%Y-%m-%d %H:%M UTC").replace(tzinfo=datetime.timezone.utc)
                 - datetime.datetime.now(datetime.timezone.utc)).total_seconds())
    if ecart > 3600:
        arret(f"date à {ecart:.0f} s de l'horloge (au plus 3 600 s)")
    if not (a.controles and a.candidat_relu and a.candidat_verifie and a.candidat_final and a.go and a.registre):
        arret("mode reel : contrôles, candidats relu, vérifié et final, GO et registre obligatoires")
    if not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", a.go) or not re.fullmatch(r"R-\d+", a.registre):
        arret("GO (GO-AAAA-MM-JJ-NN) ou registre (R-n) mal formé")


def git(*args: str) -> bytes:
    r = subprocess.run(["git", "-C", str(D), *args], capture_output=True)
    if r.returncode != 0:
        arret(f"git {' '.join(args)} : {r.stderr.decode(errors='replace').strip()}")
    return r.stdout


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def au_head(p: str) -> bytes:
    return git("show", f"HEAD:{p}")


def scelle_au_head(p: str) -> str:
    """Empreinte du fichier à HEAD, après contrôle de son sceau (compagnon ou empreintes.sha256 du dossier ; VT-10)."""
    s = sha(au_head(p))
    nom = Path(p).name
    r = subprocess.run(["git", "-C", str(D), "show", f"HEAD:{p}.sha256"], capture_output=True)
    if r.returncode == 0:
        if r.stdout.decode("utf-8").strip() != f"{s}  {nom}":
            arret(f"sceau de {p} non conforme")
        return s
    lignes = au_head(str(Path(p).parent / "empreintes.sha256")).decode("utf-8").splitlines()
    if f"{s}  {nom}" not in lignes:
        arret(f"{p} absent de empreintes.sha256 ou d'empreinte différente")
    return s


sys.path.insert(0, str(D / "src"))
from controle_ia.harnais.validation_reelle import CHEMINS_GELES  # noqa: E402

if git("status", "--porcelain", "--untracked-files=no").strip():
    arret("arbre suivi non propre")
for anc, desc in ((ANCIEN, a.commit), (a.commit, "HEAD")):
    if subprocess.run(["git", "-C", str(D), "merge-base", "--is-ancestor", anc, desc]).returncode != 0:
        arret(f"{anc[:12]} n'est pas ancêtre de {desc[:12]}")
change = git("diff", "--name-only", ANCIEN, a.commit, "--", *CHEMINS_GELES).decode().split()
if change != [TEST_CORRIGE]:
    arret(f"arbre gelé entre {ANCIEN[:7]} et {a.commit[:7]} : {change} au lieu de [{TEST_CORRIGE}]")
if git("diff", "--name-only", a.commit, "HEAD", "--", *CHEMINS_GELES).strip():
    arret(f"arbre gelé différent entre le commit cité {a.commit[:12]} et HEAD")
sha_v1 = scelle_au_head(V1)
t = au_head(V1).decode("utf-8")
for script in ("scripts/amorce_instance_t05.sh", "scripts/pilote_t05_instance.sh"):
    if f"`{script}` (`{sha(git('show', f'{a.commit}:{script}'))}`, sha256)" not in t:
        arret(f"{script} : empreinte au commit cité différente de celle de la v1")
s_suite, s_env, s_proc = scelle_au_head(SUITE), scelle_au_head(ENVIRONNEMENT), scelle_au_head(PROCESSEUR)
s_tests_inst, s_journal, s_rep = scelle_au_head(TESTS_INSTANCE), scelle_au_head(JOURNAL_INSTANCE), scelle_au_head(REPETITION)
lignes = [x for x in au_head(SUITE).decode("utf-8").strip().splitlines() if x and not x.startswith("code ")]
if not lignes:
    arret(f"{SUITE} sans ligne lisible")
m = re.fullmatch(r"(\d+) passed in (\d+)\.(\d{2})s( \(\d+:\d{2}:\d{2}\))?", lignes[-1])
if not m:
    arret(f"dernière ligne de la suite illisible : {lignes[-1]!r}")
tests, duree = m.group(1), f"{m.group(2)},{m.group(3)}"
if f"  - Tests attendus : `{tests}` (toute" not in t:
    arret(f"nombre de tests {tests} différent de celui de la v1")
if a.mode == "reel":
    r = subprocess.run([sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider"], cwd=D,
                       capture_output=True, text=True, env={**__import__("os").environ, "PYTHONPATH": "src"})
    mc = re.search(r"^(\d+) tests? collected", r.stdout, re.M)
    if r.returncode != 0 or not mc or mc.group(1) != tests:
        arret(f"tests collectés à HEAD : {mc.group(1) if mc else 'illisible'} ≠ {tests}")
c7 = a.commit[:7]


def rep(x: str, y: str) -> None:
    global t
    n = t.count(x)
    if n != 1:
        arret(f"cible trouvée {n} fois : {x[:80]!r}")
    t = t.replace(x, y)


rep("# Préenregistrement — T0.5 — revalidation courte de l'équivalence sur le domaine du pilote — v1",
    "# Préenregistrement — T0.5 — revalidation courte de l'équivalence sur le domaine du pilote — v2")
entete_v1 = t.split("\n")[2]
if not entete_v1.startswith("Version scellée le 2026-10-10 19:41 UTC"):
    arret("en-tête de la v1 inattendu")
rep(entete_v1,
    f"Version 2, scellée le {a.date}, depuis la v1 scellée le 2026-10-10 19:41 UTC (`{V1}`, `{sha_v1}` ; gardée telle "
    "quelle). La v1 n'a joué aucun épisode : sur l'instance 55292763, la suite des tests a échoué avant le run (« 1 failed, "
    "669 passed » ; `tests/test_validation_reelle.py::test_p4_contraire_se_lit_au_vu_du_repere`, un test qui supposait non "
    "nul le 99e centile des écarts de production du modèle jouet en bfloat16, la grandeur que lit la garde ; il y est resté "
    "sous 1e-9, nul en émulation de la classe vectorielle de ce processeur, AVX2 pour torch, sans AVX-512, alors que le "
    "maximum reste non nul, environ 1e-3 en émulation ; processeur AMD EPYC 7513, modèle relevé "
    f"(`{PROCESSEUR}`, `{s_proc}`) ; R-132, R-134). Elle n'est pas relancée telle quelle : la cause est déterministe, et "
    "l'option (b) de N-018, relancer la v1 sur un processeur de classe AVX-512, choisirait le matériel pour passer une "
    f"garde. D'où cette version (N-018). Ce qui change : le commit du code cité (le test corrigé, commit `{c7}` ; le code "
    "de la revalidation, les scripts de l'instance, la configuration, l'entropie et le nombre de tests sont inchangés) ; "
    "la durée de la suite à ce commit et les mesures de la tentative de la v1 sur l'instance (« Calcul ») ; la mention de "
    "l'origine de l'entropie (la même) ; le chemin de ce préenregistrement et la branche de résultats, passés au script de "
    f"l'instance (`PREREG={V2}`, `BRANCHE={BRANCHE}` : la v1 occupe les défauts) ; le titre, cet en-tête, l'auteur et "
    "la date, une ligne de transparence et une entrée d'historique. Aucun seuil, aucune lecture, aucune graine ne change.\n\n"
    "En-tête de la v1, pour mémoire : « " + entete_v1 + " »")
rep("- Auteur : la session de mise en œuvre du programme de Lazar ; rédaction le 2026-10-07.",
    "- Auteur : la session de mise en œuvre du programme de Lazar ; rédaction le 2026-10-07 ; version 2 rédigée le 2026-10-10.")
rep("- Date (UTC) : 2026-10-10 19:41 (scellement :",
    f"- Date (UTC) : {a.date.removesuffix(' UTC')} (version 2 ; v1 le 2026-10-10 19:41 ; scellement de la v1 :")
rep(f"- Commit du code d'analyse : `{ANCIEN}`",
    f"- Commit du code d'analyse : `{a.commit}` (v1 : `{ANCIEN}` ; seul change, entre les deux, dans l'arbre gelé "
    f"(`CHEMINS_GELES`) : `{TEST_CORRIGE}`)")
rep("(tirée au scellement par `numpy.random.SeedSequence`, écrite une seule fois).",
    "(tirée au scellement de la v1 par `numpy.random.SeedSequence`, écrite une seule fois ; la même pour la v2).")
rep("--run-id <run> --prereg prereg/T0.5-revalidation-equivalence-pilote-v1.md`.",
    f"--run-id <run> --prereg {V2}` ; ce chemin et la branche de résultats `{BRANCHE}` sont passés au script par "
    "l'environnement de l'instance (`PREREG`, `BRANCHE`), la v1 et sa branche occupant les défauts ; l'amorce les "
    "transmet telles quelles (elle ne lit `BRANCHE` que pour sa poussée de secours après son plafond) ; éprouvé par la "
    f"répétition jouet v3 de la chaîne, passage 1 (`{REPETITION}`, `{s_rep}` ; passage 4 interrompu par le disque plein "
    "de la session).")
rep("(au commit cité : 670 tests, 475,09 s dans un environnement neuf installé seulement depuis `requirements-gpu.txt`, "
    "sur la session, le 2026-10-10 : répétition jouet de l'amorce, archive "
    "`prereg/contre-lectures/T0.5-revalidation-repetition-jouet-v5.tar`, fichier `racine-1-sain/t05/tests.txt` ; "
    "vérification du remplissage, D-3 et N-9).",
    f"(au commit cité : {tests} tests, {duree} s dans un environnement neuf installé seulement depuis "
    f"`requirements-gpu.txt`, sur la session, le 2026-10-10 : `{SUITE}` (`{s_suite}`), environnement `{ENVIRONNEMENT}` "
    f"(`{s_env}`) ; au commit de la v1 : 670 tests, 475,09 s sur la session, répétition jouet de l'amorce, archive "
    "`prereg/contre-lectures/T0.5-revalidation-repetition-jouet-v5.tar`, fichier `racine-1-sain/t05/tests.txt`, "
    "vérification du remplissage, D-3 et N-9 ; sur l'instance 55292763, au commit de la v1 : 1 échec et 669 réussis en "
    f"501,51 s, `{TESTS_INSTANCE}` (`{s_tests_inst}`), soit 10 min 25 s de la ligne « AMORCE » à la fin des tests, "
    f"`{JOURNAL_INSTANCE}` (`{s_journal}`)).")
rep("- Connu avant le scellement : les résultats de T0.4 v1 à v3 (cités).",
    "- Connu avant le scellement de la v2 : la tentative de la v1, arrêtée aux tests, avant tout manifeste et tout "
    "épisode (R-132) ; aucun résultat de run n'existe. Audit des tests sensibles au matériel par un sous-agent neuf "
    "(`prereg/contre-lectures/T0.5-revalidation-audit-tests-materiel-v1.md`, "
    "`dd1becf7be90650b79419b3d336ad2406a7ae4d704d643f7be26885bb7efff6c` ; R-133) : aucun autre test à risque élevé ni "
    "moyen ; risques faibles notés, non corrigés avant la relance : trois tests qui exigent au moins un jeton à écart de "
    "production non nul dans la zone générée (audit de symétrie ; le 99e centile de l'action entière, que lit la garde, "
    "peut être nul), passés sur les deux "
    "classes de processeur, AVX2 et AVX-512 ; tolérances de 1e-30 et 1e-12 ; passage de minuit pendant "
    "`test_garde_calcul`, que le lanceur rend improbable (aucune création entre 23:30 et 00:00 UTC, heure relue juste "
    "avant) ; un hôte sans AVX2 ferait échouer trois tests, donc arrêter avant le run (risque résiduel déclaré, R-135).\n"
    "- Connu avant le scellement : les résultats de T0.4 v1 à v3 (cités).")
derniere = [x for x in t.split("\n") if x.startswith("- Contrôle mécanique des corrections du brouillon 6")]
if len(derniere) != 1:
    arret("dernière entrée de l'historique de la v1 introuvable")


def normaliser(texte: str) -> str:
    ls = texte.split("\n")
    for i in (2, 7):
        ls[i] = re.sub(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", "AAAA-MM-JJ HH:MM", ls[i], count=1)
    ls = [re.sub(r"^(- Version 2 \(N-018\) : .*) Pièces : .*$", r"\1 Pièces : (remplies au scellement).", x) for x in ls]
    return sha("\n".join(ls).encode("utf-8"))


if a.mode == "reel":
    ctl = Path(a.controles).read_text(encoding="utf-8")

    def epingle(nom: str) -> str:
        m_ = re.search(rf'^{nom}="?([^"\n#]*?)"?\s*(#.*)?$', ctl, re.M)
        if not m_ or "A_EPINGLER" in m_.group(1):
            arret(f"épingle {nom} absente des contrôles")
        return m_.group(1).strip()
    pieces = []
    for role, chemin, cle in (("candidat relu", a.candidat_relu, "CANDIDAT_RELU"),
                              ("candidat vérifié", a.candidat_verifie, "CANDIDAT_VERIFIE"),
                              ("candidat final, contrôlé après les dernières corrections", a.candidat_final, "CANDIDAT_FINAL")):
        if chemin != epingle(f"{cle}_CHEMIN") or not chemin.startswith("brouillons/"):
            arret(f"{role} : chemin {chemin} ≠ épingle")
        s = scelle_au_head(chemin)
        if s != epingle(cle):
            arret(f"{role} : empreinte {s[:12]} ≠ épingle")
        pieces.append(f"{role} `{chemin}` (`{s}`)")
    if normaliser(au_head(a.candidat_final).decode("utf-8")) != epingle("CANDIDAT_NORMALISE"):
        arret("candidat final : empreinte normalisée ≠ épingle")
    brutes = epingle("RAPPORTS_ATTENDUS").split()
    if not brutes or not all(re.fullmatch(r"[^=\s]+=[0-9a-f]{64}", x) for x in brutes):
        arret("rapports attendus vides ou mal formés (nom=empreinte)")
    paires = [x.split("=") for x in brutes]
    if len({n for n, _ in paires}) != len(paires):
        arret("rapports attendus en double")
    presents = {Path(x).name for x in git("ls-tree", "-r", "--name-only", "HEAD", "prereg/contre-lectures/").decode().split()
                if re.fullmatch(r"prereg/contre-lectures/T0\.5-revalidation-v2-(relecture|verification)-[a-z-]+-v1\.(md|json|tar)", x)}
    if presents != {n for n, _ in paires}:
        arret(f"rapports de la v2 présents ≠ rapports attendus : {sorted(presents ^ {n for n, _ in paires})}")
    for nom, s_att in paires:
        if not re.fullmatch(r"T0\.5-revalidation-v2-(relecture|verification)-[a-z-]+-v1\.(md|json|tar)", nom):
            arret(f"rapport {nom} au nom inattendu")
        if scelle_au_head(f"prereg/contre-lectures/{nom}") != s_att:
            arret(f"rapport {nom} : empreinte ≠ épingle")
        pieces.append(f"`{nom}` (`{s_att}`)")
    go = au_head("registres/go.md").decode("utf-8").splitlines()
    ligne_go = [x for x in go if x.startswith(f"| {a.go} |")]
    if len(ligne_go) != 1:
        arret(f"{a.go} absent de registres/go.md ou en double")
    c = [x.strip() for x in ligne_go[0].strip().strip("|").split("|")]
    if len(c) != 8 or c[2] != "revendication" or c[6] != "Lazar" or "N-018" not in c[3]:
        arret(f"{a.go} : ligne mal formée, d'un autre type, non accordée par Lazar ou sans N-018")
    if any(x.startswith("| ") and "révocation" in x and a.go in x for x in go):
        arret(f"{a.go} révoqué")
    dec = au_head("registres/decisions.md").decode("utf-8").splitlines()
    n18 = [x for x in dec if x.startswith("| N-018 |")]
    if len(n18) != 1 or n18[0].rstrip().endswith("| en attente |") or a.go not in n18[0] or "(a)" not in n18[0].rsplit("|", 2)[-2]:
        arret("N-018 : absent, en attente, sans le GO ou sans l'option (a) dans son état")
    for r_ in CORRECTIONS.split(" et ") + [a.registre]:
        if not any(x.startswith(f"| {r_} |") for x in dec):
            arret(f"{r_} absent de registres/decisions.md")
    if a.go not in [x for x in dec if x.startswith(f"| {a.registre} |")][0]:
        arret(f"{a.registre} ne cite pas {a.go}")
    fin = ("Pièces : " + " ; ".join(pieces) + f" ; corrections : {CORRECTIONS} ; décision de Lazar : {a.go} ({a.registre}).")
else:
    fin = "Pièces : (remplies au scellement)."
entree = ("- Version 2 (N-018) : différentiel v1 → v2 (texte ; code dans l'arbre gelé, `git diff " + ANCIEN[:7] + " " + c7
          + " -- <CHEMINS_GELES>` : un seul fichier de test) relu avant le scellement par des sous-agents neufs, en trois "
          "angles (texte, code et cause, chaîne de lancement), avec contre-vérification adverse des remarques graves ; "
          "corrections vérifiées par des sous-agents neufs (deux angles, avec sceptiques) ; dernières corrections "
          "contrôlées mécaniquement par un sous-agent neuf, dont les remarques ont été traitées. " + fin)
rep(derniere[0], derniere[0] + "\n" + entree)
permises = ("- Commit du code d'analyse", "En-tête de la v1", "- Version 2 (N-018)")
reste = [x for x in t.splitlines() if (ANCIEN in x or ANCIEN[:7] in x) and not x.startswith(permises)]
if reste:
    arret("ancien commit restant hors des lignes permises : " + " | ".join(x[:80] for x in reste))
with open(a.sortie, "x", encoding="utf-8") as f:
    f.write(t)
print(f"v2 écrite : {a.sortie} ; sha256 {sha(t.encode())} ; normalisée {normaliser(t)} ; tests {tests} ; durée {duree} s")
