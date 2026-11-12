"""Brouillon 10 du préenregistrement de P3-bis : brouillon 9 + couples B10-01 à B10-56 (accord du texte avec le code v2 et
la chaîne de session, GO prolongé). Écrit par un rédacteur neuf, sous-agent de la session mère
`session_01QPDgKgACWyCkCN8HjqwNXy`, le 10 novembre 2026, sur la consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-redaction-p3bis-brouillon10-v1.md` (`0fea27bd…`).

Chaque « ancien » doit apparaître exactement une fois, sinon arrêt sans rien écrire (R5) ; la sortie et le journal ne
doivent pas exister (R12). Le journal consigne : empreintes de l'entrée, des couples et de ce script ; chaque couple
(section, gelée ou non) ; comparaison de chaque section gelée au brouillon 9 (et contrôle que les couples non gelés n'en
touchent aucune) ; marqueurs restants ; `controle_ia.prereg.problemes` ; formes que la chaîne de session lit dans le texte
(recopiées de `docs/procedures/P3-bis-temoin-positif-v1/verifications_p3bis_v1.py`, `71153720…`, et de
`controles_avant_depense_p3bis_v1.sh`, `8571d2f3…`, branche `prep/p3bis-lanceur-v1`) ; sortie de l'essai de fermeture
citée. Aucun appel externe ; rien d'autre n'est écrit.

Usage, depuis la racine du dépôt :
  PYTHONPATH=src python <ce script> "$(date -u +%Y-%m-%dT%H:%M:%SZ)"            # écrit le brouillon 10 et le journal
  PYTHONPATH=src python <ce script> --essai COUPLES.json "$(date -u +…)"        # tout en mémoire, rien d'écrit
L'heure passée en argument est relevée par `date -u` (règle des heures)."""
import hashlib, json, re, sys
from pathlib import Path

from controle_ia.prereg import problemes, sections

DOSSIER = Path("brouillons/P3-bis-temoin-positif-v1")
ENTREE = DOSSIER / "P3-bis-preenregistrement-v1-brouillon9.md"
SORTIE = DOSSIER / "P3-bis-preenregistrement-v1-brouillon10.md"
COUPLES = DOSSIER / "P3-bis-preenregistrement-v1-brouillon10-couples-v1.json"
JOURNAL = DOSSIER / "P3-bis-preenregistrement-v1-brouillon10-journal-v1.txt"
EMPREINTE_ENTREE = "eb65773fa6b0099d5f3fdd43e1602852d527cdc5759f780d09c8a88ac241bca8"
EMPREINTE_COUPLES = "7ededee07d94aee871b0e65fbae9d53ec4c4903b2e6519c7013b3337d06237b6"
GELEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
          "Critères de lecture gelés", "Liste d'arrêt")
MARQUEURS_ATTENDUS = {"CHAINE_P3BIS", "COMMIT_CODE_P3BIS", "CONTRE_LECTURE_4_P3BIS", "EMPREINTES_CODE_P3BIS",
                      "EMPREINTE_CONFIG_P3BIS", "EMPREINTE_CONSIGNES_P3BIS", "IDENTITE_CODE_P3BIS", "LONGUEURS_P3BIS",
                      "PIECES_SUR_MAIN_P3BIS", "TESTS_ATTENDUS_P3BIS"}
# formes lues par la chaîne de session (branche prep/p3bis-lanceur-v1, commit 776b26cb)
GO_CALCUL = "GO-2026-11-10-02"
DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"
MOTIF_GO = r"GO-\d{4}-\d{2}-\d{2}-\d{2}"
VALEURS_TEXTE = (
    "au plus 2,10 USD de l'heure", "fiabilité ≥ 0,98", "stockage au plus 0,08 USD de l'heure",
    "téléchargement au plus 0,05 USD par Go", "au moins 30 cœurs effectifs", "128 000 Mo de mémoire vive",
    "disque ≥ 80 Go", "processeur AMD EPYC 7513 exigé d'abord", "douze essais à 15 minutes d'intervalle",
    "plafond exactement 80 USD", "création au plus tard le 23 novembre 2026",
    "≥ 20 USD plus 10 heures du prix des instances nommées en marche",
    "l'absence de ligne `PROGRES` pendant deux heures donne une alerte",
    "`duree_max_s` et `budget_entrainement_s` à `null`", "aucun `timeout`", "16 783 360 octets",
    f"`DEPOT_URL={DEPOT_URL}`", f"`GO_ID={GO_CALCUL}`")
INTITULES = ("Configuration de P3 (empreinte canonique)", "Tâches de P3", "Commit du code d'analyse", "Entropie",
             "Tests attendus", "Chemin de la configuration de P3", "Chemin des tâches de P3", "Chemin des consignes de P3")
ESSAI_CHEMIN = "brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v1.txt"
ESSAI_EMPREINTE = "06e84ff732ebd7b30c33e18bdab7ea979fadb7d290da92c71383ac82072dceb5"
LIGNE_ESSAI_CONFORME = "ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def appliquer(t: str, couples: list) -> tuple[str, list]:
    lignes = []
    for c in couples:
        n = t.count(c["ancien"])
        if n != 1:
            sys.exit(f"couple {c['id']} : ancien trouvé {n} fois (1 exigé) ; rien n'est écrit")
        t = t.replace(c["ancien"], c["nouveau"])
        g = c["section_gelee"]
        lignes.append(f"{c['id']}\t{'GELÉE : ' + g if g else 'non gelée'}\t{c['section']}\tancien 1 fois\t"
                      f"{len(c['ancien'])} → {len(c['nouveau'])} caractères\t{c['motif']}")
    return t, lignes


def plat(t: str) -> str:
    return re.sub(r" +", " ", t.replace("\n", " "))


def controles(t9: str, t10: str, couples: list) -> list[tuple[bool, str]]:
    r = []
    s9, s10 = sections(t9), sections(t10)
    declarees = {}
    for c in couples:
        if c["section_gelee"]:
            declarees.setdefault(c["section_gelee"], []).append(c["id"])
    for g in GELEES:
        egale = s9.get(g) == s10.get(g)
        d = declarees.get(g, [])
        if egale:
            r.append((not d, f"section gelée « {g} » : égale à l'octet au brouillon 9" + (f" (mais couples déclarés {d})" if d else "")))
        else:
            r.append((bool(d), f"section gelée « {g} » : modifiée par {', '.join(d) if d else 'AUCUN COUPLE DÉCLARÉ'}"))
    for g in declarees:
        r.append((g in GELEES, f"section déclarée gelée « {g} » connue"))
    t_ng, _ = appliquer(t9, [c for c in couples if not c["section_gelee"]])
    sng = sections(t_ng)
    touchees = [g for g in GELEES if sng.get(g) != s9.get(g)]
    r.append((not touchees, "couples non gelés appliqués seuls : aucune section gelée touchée" if not touchees
              else f"couples non gelés qui touchent {touchees}"))
    # marqueurs
    trouves = re.findall(r"<<([A-Z0-9_]+)>>", t10)
    compte = {m: trouves.count(m) for m in sorted(set(trouves))}
    r.append((set(compte) == MARQUEURS_ATTENDUS and all(v == 1 for v in compte.values()),
              f"marqueurs restants : {len(compte)} distincts, {compte}"))
    r.append(("ESSAI_FERMETURE_P3BIS" not in t10.replace("`ESSAI_FERMETURE_P3BIS`", ""),
              "marqueur ESSAI_FERMETURE_P3BIS rempli (le nom ne reste qu'entre accents graves, sans chevrons)"))
    # formes lues par la chaîne
    m = re.findall(rf"^- GO : \*\*({MOTIF_GO})\*\*", t10, re.M)
    r.append((m == [GO_CALCUL] and len(re.findall(r"^- GO :", t10, re.M)) == 1,
              f"chaîne, `go` : une seule ligne « - GO : **…** », {m}"))
    lanc = [x for x in t10.split("\n") if x.startswith("- Lancement : ")]
    ok = len(lanc) == 1 and re.findall(rf"`GO_ID=({MOTIF_GO})`", lanc[0]) == [GO_CALCUL] \
        and set(re.findall(MOTIF_GO, lanc[0])) == {GO_CALCUL}
    r.append((ok, f"chaîne, `go` : première ligne « - Lancement : » unique, seul GO cité {GO_CALCUL}"))
    r.append(("`PREREG=prereg/P3-bis-temoin-positif-v1.md`, `BRANCHE=calcul/p3bis-reel-v1`" in t10
              and f"`DEPOT_URL={DEPOT_URL}`" in t10, "chaîne, contrôles bloc 12 : PREREG, BRANCHE, DEPOT_URL"))
    sg = " ".join(t10.replace("**", "").split())
    manquantes = [v for v in VALEURS_TEXTE if v not in sg]
    r.append((not manquantes, f"chaîne, `valeurs` : {len(VALEURS_TEXTE) - len(manquantes)} sur {len(VALEURS_TEXTE)}"
              + (f" ; manquantes {manquantes}" if manquantes else "")))
    doubles = {x: t10.count(f"{x} : `") for x in INTITULES if t10.count(f"{x} : `") != 1}
    r.append((not doubles, "chaîne, contrôles bloc 12 : huit intitulés lus une fois chacun" + (f" ; {doubles}" if doubles else "")))
    r.append((f"`{ESSAI_CHEMIN}` (`{ESSAI_EMPREINTE}`" in plat(t10),
              "chaîne, contrôles bloc 6 : sortie de l'essai de fermeture citée « `chemin` (`sha256` »"))
    p = Path(ESSAI_CHEMIN)
    if p.exists():
        b = p.read_bytes()
        lignes = [x for x in b.decode("utf-8").split("\n") if x.strip()]
        compagnon = Path(ESSAI_CHEMIN + ".sha256")
        r.append((sha(b) == ESSAI_EMPREINTE and lignes[-1] == LIGNE_ESSAI_CONFORME
                  and not any(x.startswith("NON CONFORME") for x in lignes)
                  and compagnon.exists() and compagnon.read_text(encoding="utf-8").split()[0] == ESSAI_EMPREINTE,
                  f"sortie de l'essai de fermeture : empreinte, compagnon, dernière ligne « {lignes[-1]} », aucune non conforme"))
    else:
        r.append((False, f"sortie de l'essai de fermeture absente : {ESSAI_CHEMIN}"))
    return r


def main(argv: list[str]) -> int:
    essai = len(argv) == 4 and argv[1] == "--essai"
    if not essai and len(argv) != 2:
        sys.exit(__doc__)
    heure = argv[-1]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", heure):
        sys.exit("heure attendue AAAA-MM-JJTHH:MM:SSZ, relevée par date -u")
    b9 = ENTREE.read_bytes()
    if sha(b9) != EMPREINTE_ENTREE:
        sys.exit(f"empreinte de {ENTREE} inattendue")
    chemin_couples = Path(argv[2]) if essai else COUPLES
    bc = chemin_couples.read_bytes()
    if not essai and sha(bc) != EMPREINTE_COUPLES:
        sys.exit(f"empreinte de {COUPLES} inattendue")
    couples = json.loads(bc.decode("utf-8"))
    t9 = b9.decode("utf-8")
    t10, lignes = appliquer(t9, couples)
    r = controles(t9, t10, couples)
    j = [f"Journal du brouillon 10 de P3-bis — {heure} (heure relevée par date -u, passée en argument)",
         f"entrée {ENTREE} {sha(b9)}",
         f"couples {chemin_couples} {sha(bc)} ({len(couples)} couples, dont "
         f"{sum(1 for c in couples if c['section_gelee'])} dans des sections gelées)",
         f"script {Path(__file__).as_posix()} {sha(Path(__file__).read_bytes())}",
         "", "couples appliqués, dans l'ordre :"] + lignes
    j += ["", f"sortie {SORTIE} {sha(t10.encode('utf-8'))}", "", "contrôles :"]
    j += [("CONFORME — " if ok else "NON CONFORME — ") + texte for ok, texte in r]
    if not essai:
        if SORTIE.exists() or JOURNAL.exists():
            sys.exit(f"{SORTIE} ou {JOURNAL} existe déjà (R12)")
        SORTIE.write_text(t10, encoding="utf-8")
        p = problemes(SORTIE)
    else:
        tmp = Path(argv[2]).with_name("essai-brouillon10.md")
        tmp.write_text(t10, encoding="utf-8")
        p = problemes(tmp)
        tmp.unlink()
    j += ["", "controle_ia.prereg.problemes (attendu : la contre-lecture 4 sans ses empreintes et les dix marqueurs gardés) :"]
    j += [f"  {x}" for x in p]
    attendus = sorted(MARQUEURS_ATTENDUS)
    ok_p = len(p) == 2 and p[0] == "contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)" \
        and p[1] == "marqueurs de gabarit restants : " + ", ".join(f"<<{m}>>" for m in attendus)
    j += [("CONFORME — " if ok_p else "NON CONFORME — ") + "problemes() égal à l'attendu"]
    tous = all(ok for ok, _ in r) and ok_p
    j += ["", "BROUILLON 10 : " + ("CONTRÔLES CONFORMES" if tous else "CONTRÔLES NON CONFORMES")]
    texte = "\n".join(j) + "\n"
    if essai:
        print(texte)
    else:
        JOURNAL.write_text(texte, encoding="utf-8")
        print(sha(SORTIE.read_bytes()), SORTIE)
        print(sha(JOURNAL.read_bytes()), JOURNAL)
        print(j[-1])
    return 0 if tous else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
