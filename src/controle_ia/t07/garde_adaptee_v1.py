"""Garde adaptée de T0.7 à l'ouverture réduite de P3-bis (N-066, option 1 ; brouillon 19, `07039ed2…`, section « Écrits exigés par
P3-bis », (d), G1 à G6 ; section « Module », changements (xiv) et (xv)), v1 : **règles pures** sur les lignes de registre lues
(clé → {instant, sha256, chemin}), les lignes du journal des ouvertures de P3-bis (`journal_p3bis_v1.lire_journal_p3bis`), le
registre des préalables et les décisions du rendez-vous. Les fichiers sont lus par `lecture_v2.ouvrir`, qui appelle ces règles ;
la même fonction sert à l'énumération (0 bis) de `grille_l_t07_brouillon17.py` (`enumerer_0bis`).

Chaque garde rend une liste de **codes** (et de motifs) ; liste vide = la garde passe. Codes, dans l'ordre du texte (et de la grille
(0 bis), qui en tire la première issue vraie) : `CODES` ; chaque code dit s'il est un nœud ou une attente (`NATURE`).

- **Étape A** (`garde_etape_a`, à l'instant d'ouverture oA, lignes et journal tels qu'ils sont à oA) : étape déjà jouée (lignes
  `SCORES-T07` ou `SONDES-T07` ; la règle (0) du registre la refuse aussi) ; toute ligne `OUVERTURE-P3BIS` de mode
  `pleine-anticipee` (toute date) ; toute ligne de mode `pleine` avant oA ; `VERDICT-P3BIS` présente → G1 (`SCELLEMENT-T07`
  présente et strictement antérieure ; sinon refus, sans comparaison d'empreinte, m-4) puis G2 (une ouverture réduite avant oA,
  appui conforme, dernière décision « ouvrir », ligne de garde adaptée conforme et antérieure à cette décision ; motif selon la
  décision de la dernière ligne de rendez-vous : « ouvrir pleinement », « maintenir », absente) ; appui de toute ligne `reduite`
  comparé aux lignes citées, même sans `VERDICT-P3BIS` (« Ce que T0.7 en lit »).
- **Fin de l'étape A** (`garde_fin_etape_a`, juste avant d'écrire `SCORES-T07` et `SONDES-T07`) : ligne `pleine-anticipee` ;
  ligne `pleine` au plus tard à la fin ; `VERDICT-P3BIS` inscrite sans ouverture réduite au journal (chemin sans ouverture
  anticipée : règle du brouillon 14, gardée).
- **Étape B** (`garde_etape_b`) : G1 ; G4 (texte de lecture scellé après `VERDICT-P3BIS` sur un lancement à ouverture réduite) ;
  ligne `pleine-anticipee` ; ligne `pleine` au plus tard à la fin de l'étape A (fA = la plus tardive de `SCORES-T07` et
  `SONDES-T07`) ; appui de toute ligne `reduite` et `pleine` comparé aux lignes citées ; puis, si une ouverture réduite figure au
  journal, une ligne `pleine` strictement après fA (sinon refus, **attente**) ; sinon l'antériorité du chemin sans ouverture
  anticipée (`SCORES-T07` et `SONDES-T07` strictement antérieures à `VERDICT-P3BIS`). Le contrôle du verdict en prose (G3) est
  fait par `lecture_v2.ouvrir` avant `lire_issue_p3bis`.
- **G5** (`instant_fermeture`) : le plus tôt entre la première ouverture de l'étape A de ce run de 7b au journal de T0.7 (ou, à la
  première tentative, l'instant d'ouverture) et la première ligne `OUVERTURE-P3BIS`, quel que soit son mode.
- **R14** (`reserve_r14`) : une ouverture réduite strictement antérieure à la fin de l'étape A ; phrase de la table des critères.

**Interprétations déclarées** : (1) G1 est appliquée dès que `VERDICT-P3BIS` est lue (étapes A et B), sur tout chemin ; sur le
chemin sans ouverture anticipée, `SCELLEMENT-T07` < oA < fA < `VERDICT-P3BIS`, et G1 tient toujours quand ce texte est scellé ;
elle rend seulement `SCELLEMENT-T07` nécessaire à l'étape B dès que `VERDICT-P3BIS` y est (ce que R1 exige déjà) ; (2) une ligne
`pleine` datée exactement de la fin de l'étape A compte « avant la fin » (G3 exige « strictement après ») ; (3) la dernière ligne
de rendez-vous « à la date de l'ouverture réduite » est la dernière datée strictement avant elle ; (4) une ligne
`SCELLEMENT-JEUX-T07-*` datée exactement de l'instant de fermeture est hors de `sondes_lues` (« antérieures » : strict).
"""
from __future__ import annotations

from itertools import permutations

from . import journal_p3bis_v1 as jp
from . import registre_v1 as rg

DEJA, ANTICIPEE, PLEINE_AVANT_A, VERDICT_AVANT_A = "deja", "anticipee", "pleine-avant-A", "verdict-avant-A"
PLEINE_AVANT_FIN_A, VERDICT_PENDANT_A = "pleine-avant-fin-A", "verdict-pendant-A"
SCELLEMENT_APRES_VERDICT, VERSION_APRES_VERDICT, APPUI_FAUX = "scellement-apres-verdict", "version-apres-verdict", "appui-faux"
ATTENTE_PLEINE, ATTENTE_VERDICT_PROSE, ANTERIORITE = "attente-pleine", "attente-verdict-prose", "anteriorite"
CODES = (DEJA, ANTICIPEE, PLEINE_AVANT_A, VERDICT_AVANT_A, PLEINE_AVANT_FIN_A, VERDICT_PENDANT_A, SCELLEMENT_APRES_VERDICT,
         VERSION_APRES_VERDICT, APPUI_FAUX, ATTENTE_PLEINE, ATTENTE_VERDICT_PROSE, ANTERIORITE)
NATURE = {DEJA: "refus (étape A déjà jouée)", ANTICIPEE: "nœud", PLEINE_AVANT_A: "nœud", VERDICT_AVANT_A: "nœud",
          PLEINE_AVANT_FIN_A: "nœud", VERDICT_PENDANT_A: "nœud", SCELLEMENT_APRES_VERDICT: "nœud", VERSION_APRES_VERDICT: "nœud",
          APPUI_FAUX: "nœud", ATTENTE_PLEINE: "attente (relance sur le même run)",
          ATTENTE_VERDICT_PROSE: "attente (relance sur le même run)", ANTERIORITE: "nœud"}
# Issues de l'énumération (0 bis) du script du brouillon 17 (`issues_garde_adaptee`), par code.
ISSUE_0BIS = {DEJA: "refus : étape A déjà jouée",
              ANTICIPEE: "nœud : ouverture pleine anticipée de P3-bis (toute date)",
              PLEINE_AVANT_A: "refus : ouverture pleine de P3-bis avant l'étape A (nœud)",
              VERDICT_AVANT_A: "refus : VERDICT-P3BIS avant l'étape A sans ouverture réduite valable (nœud)",
              PLEINE_AVANT_FIN_A: "nœud : ouverture pleine de P3-bis avant la fin de l'étape A",
              VERDICT_PENDANT_A: "nœud : VERDICT-P3BIS inscrite pendant l'étape A sans ouverture réduite (chemin du brouillon 14)",
              SCELLEMENT_APRES_VERDICT: "nœud : SCELLEMENT-T07 postérieur à VERDICT-P3BIS",
              VERSION_APRES_VERDICT: "nœud : SCELLEMENT-T07 postérieur à VERDICT-P3BIS",
              APPUI_FAUX: "nœud : appui d'une ouverture de P3-bis non conforme",
              ATTENTE_PLEINE: "attente : ouverture pleine de P3-bis après la fin de l'étape A pas encore écrite",
              ATTENTE_VERDICT_PROSE: "attente : verdict en prose de P3-bis absent",
              ANTERIORITE: "refus : SCORES-T07 et SONDES-T07 non strictement antérieures à VERDICT-P3BIS (chemin normal)"}
B_REDUITE, B_NORMAL = "étape B possible : ouverture réduite, pleine après fA", "étape B possible : chemin normal"
PHRASE_R14 = ("étape A jouée après l'ouverture de la seule issue de P3-bis ({date}, ligne {numero} du journal "
              "registres/ouvertures-p3bis-v1.md) : la cécité des décisions de tenue repose sur les écrits (a) à (c), non sur l'ordre ; "
              "voies « version neuve » et « texte nouveau » fermées sur 7b pour ce lancement (G4)")
MOTIF_OUVRIR_PLEINEMENT = "ouverture pleine anticipée décidée (ouvrir pleinement) : T0.7 ne lit plus 7b"
MOTIF_MAINTENIR = "décision maintenir : aucune ouverture réduite permise"
MOTIF_DECISION_ABSENTE = "décision absente"


def _o(journal: list, mode: str) -> list:
    return [l for l in jp.ouvertures(journal) if l["mode"] == mode]


def derniere_decision(prealables: dict | None, decisions: dict | None, avant: int | None = None) -> tuple[dict | None, dict | None]:
    """Dernière ligne `RENDEZ-VOUS-P3BIS-N` (datée strictement avant `avant` si donné) et sa décision lue ({numero : décision})."""
    if not prealables or not prealables["rendez_vous"]:
        return None, None
    lignes = [e for e in prealables["rendez_vous"] if avant is None or e["instant"] < avant]
    if not lignes:
        return None, None
    e = lignes[-1]
    return e, (decisions or {}).get(e["numero"])


def motif_selon_decision(prealables, decisions) -> str:
    """Motif d'un refus de G2 selon la décision que porte la dernière ligne de rendez-vous (brouillon 17, M-1)."""
    _, d = derniere_decision(prealables, decisions)
    if d is None:
        return MOTIF_DECISION_ABSENTE
    return {jp.OUVRIR_PLEINEMENT: MOTIF_OUVRIR_PLEINEMENT, jp.MAINTENIR: MOTIF_MAINTENIR,
            jp.OUVRIR: "décision ouvrir, mais aucune ouverture réduite valable au journal avant l'ouverture de l'étape A"}[d["decision"]]


def controler_reduite(o: dict, lignes: dict, prealables: dict | None, decisions: dict | None) -> str | None:
    """Appui d'une ligne `reduite` (G2 (i) à (iii)) : `RENDEZ-VOUS-P3BIS-N=<sha> GARDE-ADAPTEE-T07-P3BIS=<sha>`, N la dernière ligne
    de rendez-vous à la date de l'ouverture réduite, d'empreinte écrite par la ligne, décision « ouvrir » ; ligne de garde adaptée
    citant `prereg/T0.7-sondes-v0-v1.md` à l'empreinte de `SCELLEMENT-T07`, antérieure à la ligne de la décision. Rend le motif
    d'une faute, ou None."""
    lieu = f"ligne {o['numero']} du journal de P3-bis (reduite, {o['date']})"
    try:
        appui = jp.lire_appui(o["appui"])
    except rg.RefusRegistre as e:
        return f"{lieu} : {e}"
    if prealables is None:
        return f"{lieu} : registre des préalables de P3-bis non lu"
    ligne_rdv, decision = derniere_decision(prealables, decisions, o["instant"])
    if ligne_rdv is None:
        return f"{lieu} : aucune ligne RENDEZ-VOUS-P3BIS-N avant l'ouverture réduite : {MOTIF_DECISION_ABSENTE}"
    if len(appui) != 2 or appui[1][0] != jp.GARDE_ADAPTEE_T07_P3BIS or not jp.RENDEZ_VOUS.fullmatch(appui[0][0]):
        return f"{lieu} : appui {o['appui']!r} ≠ « RENDEZ-VOUS-P3BIS-N=… GARDE-ADAPTEE-T07-P3BIS=… »"
    if appui[0][0] != ligne_rdv["cle"]:
        return f"{lieu} : appui cite {appui[0][0]}, la dernière ligne de rendez-vous à cette date est {ligne_rdv['cle']}"
    if appui[0][1] != ligne_rdv["sha256"]:
        return f"{lieu} : empreinte de {appui[0][0]} dans l'appui ≠ celle qu'écrit la ligne"
    if decision is None or decision["decision"] != jp.OUVRIR:
        d = decision["decision"] if decision else "illisible"
        return (f"{lieu} : la ligne {ligne_rdv['cle']} cite une décision « {d} », « ouvrir » attendue"
                + (f" ({MOTIF_OUVRIR_PLEINEMENT})" if d == jp.OUVRIR_PLEINEMENT else f" ({MOTIF_MAINTENIR})" if d == jp.MAINTENIR else ""))
    g = prealables["garde_adaptee"]
    if g is None:
        return f"{lieu} : ligne {jp.GARDE_ADAPTEE_T07_P3BIS} absente du registre des préalables"
    if appui[1][1] != g["sha256"]:
        return f"{lieu} : empreinte de {jp.GARDE_ADAPTEE_T07_P3BIS} dans l'appui ≠ celle qu'écrit la ligne"
    if rg.SCELLEMENT_T07 not in lignes:
        return f"{lieu} : SCELLEMENT-T07 absente (G1)"
    if g["chemin"] != jp.PREREG_T07 or g["sha256"] != lignes[rg.SCELLEMENT_T07]["sha256"]:
        return (f"{lieu} : la ligne {jp.GARDE_ADAPTEE_T07_P3BIS} cite {g['chemin']!r} ({g['sha256'][:12]}…), pas le texte scellé "
                f"{jp.PREREG_T07} à l'empreinte de SCELLEMENT-T07")
    if not g["instant"] < ligne_rdv["instant"]:
        return f"{lieu} : la ligne {jp.GARDE_ADAPTEE_T07_P3BIS} ({g['date']}) ne précède pas la décision « ouvrir » ({ligne_rdv['date']})"
    return None


def controler_pleine(o: dict, lignes: dict) -> str | None:
    """Appui d'une ligne `pleine` : `SCORES-T07=<sha> SONDES-T07=<sha>` aux empreintes de ces deux lignes du registre."""
    lieu = f"ligne {o['numero']} du journal de P3-bis (pleine, {o['date']})"
    if rg.SCORES_T07 not in lignes or rg.SONDES_T07 not in lignes:
        return f"{lieu} : SCORES-T07 ou SONDES-T07 absente du registre"
    attendu = f"{rg.SCORES_T07}={lignes[rg.SCORES_T07]['sha256']} {rg.SONDES_T07}={lignes[rg.SONDES_T07]['sha256']}"
    if o["appui"] != attendu:
        return f"{lieu} : appui {o['appui'][:60]!r}… ≠ « SCORES-T07=… SONDES-T07=… » aux empreintes des lignes"
    return None


def _g1(lignes: dict) -> str | None:
    if rg.VERDICT_P3BIS not in lignes:
        return None
    if rg.SCELLEMENT_T07 not in lignes:
        return "G1 : VERDICT-P3BIS présente et SCELLEMENT-T07 absente (aucune comparaison d'empreinte tentée, m-4) : T0.7 ne lit pas 7b"
    if not lignes[rg.SCELLEMENT_T07]["instant"] < lignes[rg.VERDICT_P3BIS]["instant"]:
        return (f"G1 : VERDICT-P3BIS ({rg.date_utc(lignes[rg.VERDICT_P3BIS]['instant'])}) pas strictement postérieure à SCELLEMENT-T07 "
                f"({rg.date_utc(lignes[rg.SCELLEMENT_T07]['instant'])}) : T0.7 ne lit pas 7b")
    return None


def garde_etape_a(oA: int, lignes: dict, journal: list, prealables: dict | None = None, decisions: dict | None = None,
                  deja: bool | None = None) -> list[tuple[str, str]]:
    """Garde adaptée à l'ouverture de l'étape A ; `deja` (défaut : `SCORES-T07` ou `SONDES-T07` dans `lignes`)."""
    codes = []
    deja = (rg.SCORES_T07 in lignes or rg.SONDES_T07 in lignes) if deja is None else deja
    if deja:
        codes.append((DEJA, "SCORES-T07 ou SONDES-T07 présente à l'ouverture de l'étape A : étape A déjà jouée"))
    for o in _o(journal, jp.PLEINE_ANTICIPEE):
        codes.append((ANTICIPEE, f"ligne {o['numero']} du journal de P3-bis : ouverture pleine-anticipee ({o['date']}) : "
                                 f"{MOTIF_OUVRIR_PLEINEMENT}"))
    for o in _o(journal, jp.PLEINE):
        if o["instant"] < oA:
            codes.append((PLEINE_AVANT_A, f"ligne {o['numero']} du journal de P3-bis : ouverture pleine ({o['date']}) avant l'ouverture "
                                          "de l'étape A (contraire à P3-bis, qui l'exige après SCORES-T07)"))
    reduites = [o for o in _o(journal, jp.REDUITE) if o["instant"] < oA]
    for o in reduites:
        m = controler_reduite(o, lignes, prealables, decisions)
        if m:
            codes.append((APPUI_FAUX, m))
    if rg.VERDICT_P3BIS in lignes:
        g1 = _g1(lignes)
        if g1:
            codes.append((VERDICT_AVANT_A, g1))
        elif not reduites:
            codes.append((VERDICT_AVANT_A, "G2 : VERDICT-P3BIS présente à l'ouverture de l'étape A sans ouverture réduite au journal de "
                                           f"P3-bis avant l'ouverture : {motif_selon_decision(prealables, decisions)}"))
        else:
            _, d = derniere_decision(prealables, decisions)      # appuis des réduites : contrôlés ci-dessus (APPUI_FAUX)
            if d is not None and d["decision"] == jp.OUVRIR_PLEINEMENT:
                codes.append((ANTICIPEE, f"G2 : dernière décision du rendez-vous : {MOTIF_OUVRIR_PLEINEMENT}"))
    return codes


def garde_fin_etape_a(fin: int, lignes: dict, journal: list, prealables: dict | None = None, decisions: dict | None = None,
                      controler_appuis: bool = False) -> list[tuple[str, str]]:
    """Juste avant `SCORES-T07` et `SONDES-T07` (datées `fin`) : lignes et journal relus à cet instant. `controler_appuis` (CT-10) :
    `VERDICT-P3BIS` inscrite avec une ouverture réduite → G1 et l'appui des réduites contrôlés aussi à la fin (registre des
    préalables relu), pour qu'aucune de ces deux lignes ne soit écrite sur un run que l'étape B refuserait."""
    codes = []
    for o in _o(journal, jp.PLEINE_ANTICIPEE):
        codes.append((ANTICIPEE, f"ligne {o['numero']} du journal de P3-bis : ouverture pleine-anticipee ({o['date']}) : "
                                 f"{MOTIF_OUVRIR_PLEINEMENT}"))
    for o in _o(journal, jp.PLEINE):
        if o["instant"] <= fin:
            codes.append((PLEINE_AVANT_FIN_A, f"ligne {o['numero']} du journal de P3-bis : ouverture pleine ({o['date']}) avant la fin "
                                              "de l'étape A : nœud"))
    reduites = [o for o in _o(journal, jp.REDUITE) if o["instant"] <= fin]
    if rg.VERDICT_P3BIS in lignes and not reduites:
        codes.append((VERDICT_PENDANT_A, "nœud : VERDICT-P3BIS inscrite pendant l'étape A sans ouverture réduite au journal de P3-bis "
                                         "(étape A non aboutie avant VERDICT-P3BIS, chemin sans ouverture anticipée)"))
    if controler_appuis and rg.VERDICT_P3BIS in lignes and reduites:
        g1 = _g1(lignes)
        if g1:
            codes.append((SCELLEMENT_APRES_VERDICT, g1))
        for o in reduites:
            m = controler_reduite(o, lignes, prealables, decisions)
            if m:
                codes.append((APPUI_FAUX, m))
    return codes


def fin_etape_a(lignes: dict) -> int | None:
    if rg.SCORES_T07 not in lignes or rg.SONDES_T07 not in lignes:
        return None
    return max(lignes[rg.SCORES_T07]["instant"], lignes[rg.SONDES_T07]["instant"])


def garde_g4(cle_scellement: str, lignes: dict, journal: list) -> str | None:
    """G4 (règle 4 restreinte) : sur un lancement à ouverture réduite, le texte qui lit 7b est celui dont la ligne de scellement
    (`cle_scellement`) précède strictement `VERDICT-P3BIS` ; sinon refus, nœud. Sans ouverture réduite : permis."""
    if not _o(journal, jp.REDUITE):
        return None
    if rg.VERDICT_P3BIS not in lignes:
        return None
    if cle_scellement not in lignes or not lignes[cle_scellement]["instant"] < lignes[rg.VERDICT_P3BIS]["instant"]:
        return (f"G4 : lancement à ouverture réduite de P3-bis : texte de lecture scellé ({cle_scellement}) absent ou postérieur à "
                "VERDICT-P3BIS : aucune version scellée après VERDICT-P3BIS ne lit 7b sur ce lancement")
    return None


def garde_etape_b(lignes: dict, journal: list, prealables: dict | None = None, decisions: dict | None = None,
                  cle_scellement: str = rg.SCELLEMENT_T07) -> list[tuple[str, str]]:
    """Garde adaptée à l'ouverture de l'étape B (G1, G3, G4 ; antériorité du chemin sans ouverture anticipée)."""
    codes = []
    g1 = _g1(lignes)
    if g1:
        codes.append((SCELLEMENT_APRES_VERDICT, g1))
    g4 = garde_g4(cle_scellement, lignes, journal)
    if g4 and not (g1 and cle_scellement == rg.SCELLEMENT_T07):         # pour ce texte, G4 coïncide avec G1 : un seul motif
        codes.append((VERSION_APRES_VERDICT, g4))
    for o in _o(journal, jp.PLEINE_ANTICIPEE):
        codes.append((ANTICIPEE, f"ligne {o['numero']} du journal de P3-bis : ouverture pleine-anticipee ({o['date']}) : "
                                 f"{MOTIF_OUVRIR_PLEINEMENT}"))
    fA = fin_etape_a(lignes)
    pleines_apres = []
    for o in _o(journal, jp.PLEINE):
        if fA is None or o["instant"] <= fA:
            codes.append((PLEINE_AVANT_FIN_A, f"ligne {o['numero']} du journal de P3-bis : ouverture pleine ({o['date']}) pas "
                                              "strictement après SCORES-T07 et SONDES-T07"))
        else:
            m = controler_pleine(o, lignes)
            if m:
                codes.append((APPUI_FAUX, m))
            else:
                pleines_apres.append(o)
    reduites = _o(journal, jp.REDUITE)
    for o in reduites:
        m = controler_reduite(o, lignes, prealables, decisions)
        if m:
            codes.append((APPUI_FAUX, m))
    if reduites:
        if not pleines_apres and not any(c in (PLEINE_AVANT_FIN_A, APPUI_FAUX) for c, _ in codes):
            codes.append((ATTENTE_PLEINE, "G3 : lancement à ouverture réduite de P3-bis : ligne OUVERTURE-P3BIS de mode pleine, datée "
                                          "strictement après SCORES-T07 et SONDES-T07, pas encore écrite : attente (relance sur le même run)"))
    elif fA is not None and rg.VERDICT_P3BIS in lignes:
        for k in (rg.SCORES_T07, rg.SONDES_T07):
            if not lignes[k]["instant"] < lignes[rg.VERDICT_P3BIS]["instant"]:
                codes.append((ANTERIORITE, f"registre : ligne {k} ({rg.date_utc(lignes[k]['instant'])}) pas strictement antérieure à "
                                           f"VERDICT-P3BIS ({rg.date_utc(lignes[rg.VERDICT_P3BIS]['instant'])}) (chemin sans ouverture "
                                           "réduite de P3-bis, CLT7B-03)"))
    return codes


def instant_fermeture(oA: int, premiere_ouverture_a: int | None, journal: list) -> tuple[int, str]:
    """G5 : instant de fermeture du périmètre (a) 3, et sa source."""
    candidats = [(premiere_ouverture_a if premiere_ouverture_a is not None else int(oA),
                  "première ouverture de l'étape A de ce run" if premiere_ouverture_a is not None else "ouverture en cours de l'étape A")]
    ouv = jp.ouvertures(journal)
    if ouv:
        candidats.append((min(o["instant"] for o in ouv), "première ligne OUVERTURE-P3BIS du journal de P3-bis"))
    t, source = min(candidats, key=lambda x: x[0])
    return int(t), source


def reduite_avant(journal: list, instant: int | None) -> dict | None:
    """Première ouverture réduite du journal strictement avant `instant` (toute date si `instant` est nul)."""
    r = [o for o in _o(journal, jp.REDUITE) if instant is None or o["instant"] < instant]   # appelée avec fA + 1 par R14 (CT-09)
    return {"date": r[0]["date"], "numero": r[0]["numero"], "instant": r[0]["instant"]} if r else None


def reserve_r14(journal: list, fin_a: int | None) -> dict | None:
    """R14 : une ouverture réduite strictement antérieure à la fin de l'étape A (fA) ; absente sur tout autre run."""
    if fin_a is None:
        return None
    r = reduite_avant(journal, fin_a + 1)        # CT-09 : « au plus tard à la fin », comme la garde de fin (`<=`)
    if r is None:
        return None
    return {"id": "R14", "phrase": PHRASE_R14.format(date=r["date"], numero=r["numero"]), "ouverture_reduite": r}


def premier_code(codes: list) -> str | None:
    """Code de plus haute priorité (ordre de `CODES`)."""
    vus = {c for c, _ in codes}
    return next((c for c in CODES if c in vus), None)


# ------------------------------------------------------------------------------------------------ énumération (0 bis)
def _cas_synthetique(r: dict, mode: str, mode_p: str, deja: bool) -> dict:
    """Lignes, journal, préalables et décisions d'un cas de l'énumération (0 bis) : rang k → instant 1000 + 10 k ; appuis conformes."""
    t = {e: 1000 + 10 * k for e, k in r.items()}
    sha = {k: f"{i:064x}" for i, k in enumerate(("S", "V", "SC", "SO", "RDV"), start=1)}
    lignes = {rg.SCELLEMENT_T07: {"instant": t["S"], "sha256": sha["S"], "chemin": jp.PREREG_T07},
              rg.VERDICT_P3BIS: {"instant": t["V"], "sha256": sha["V"], "chemin": "docs/verdicts/issue.json"},
              rg.SCORES_T07: {"instant": t["fA"], "sha256": sha["SC"], "chemin": "donnees/r/scores-actions-t07.npz"},
              rg.SONDES_T07: {"instant": t["fA"], "sha256": sha["SO"], "chemin": "diag/r/sondes-t07.json"}}
    journal = []
    rdv_t = min(t["R"], t["P"]) - 3 if mode == "réduite" else t["P"] - 3
    decision = jp.OUVRIR if mode == "réduite" else jp.OUVRIR_PLEINEMENT if mode_p == jp.PLEINE_ANTICIPEE else None
    prealables = {"garde_adaptee": {"cle": jp.GARDE_ADAPTEE_T07_P3BIS, "instant": rdv_t - 2, "date": rg.date_utc(rdv_t - 2),
                                    "chemin": jp.PREREG_T07, "sha256": sha["S"]},
                  "rendez_vous": ([{"cle": "RENDEZ-VOUS-P3BIS-1", "numero": 1, "instant": rdv_t, "date": rg.date_utc(rdv_t),
                                    "chemin": jp.FICHIER_DECISION.format(n=1), "sha256": sha["RDV"]}] if decision else [])}
    decisions = {1: {"numero": 1, "decision": decision}} if decision else {}
    if mode == "réduite":
        journal.append({"cle": jp.OUVERTURE_P3BIS, "instant": t["R"], "date": rg.date_utc(t["R"]), "mode": jp.REDUITE,
                        "appui": f"RENDEZ-VOUS-P3BIS-1={sha['RDV']} {jp.GARDE_ADAPTEE_T07_P3BIS}={sha['S']}"})
    journal.append({"cle": jp.OUVERTURE_P3BIS, "instant": t["P"], "date": rg.date_utc(t["P"]), "mode": mode_p,
                    "appui": (f"{rg.SCORES_T07}={sha['SC']} {rg.SONDES_T07}={sha['SO']}" if mode_p == jp.PLEINE
                              else f"RENDEZ-VOUS-P3BIS-1={sha['RDV']}")})
    journal.sort(key=lambda o: o["instant"])
    for n, o in enumerate(journal, start=3):
        o["numero"] = n
    if mode == "réduite" and mode_p == jp.PLEINE_ANTICIPEE:     # « ouvrir » puis « ouvrir pleinement »
        rdv2 = t["P"] - 1
        prealables["rendez_vous"].append({"cle": "RENDEZ-VOUS-P3BIS-2", "numero": 2, "instant": rdv2, "date": rg.date_utc(rdv2),
                                          "chemin": jp.FICHIER_DECISION.format(n=2), "sha256": sha["RDV"][:-1] + "f"})
        decisions[2] = {"numero": 2, "decision": jp.OUVRIR_PLEINEMENT}
    return {"t": t, "lignes": lignes, "journal": journal, "prealables": prealables, "decisions": decisions, "deja": deja}


def _vus(c: dict, instant: int | None) -> tuple[dict, list, dict]:
    """Ce qui existe à `instant` (strictement avant) ; tout si `instant` est nul."""
    if instant is None:
        return dict(c["lignes"]), list(c["journal"]), c["prealables"]
    lignes = {k: v for k, v in c["lignes"].items() if v["instant"] < instant}
    journal = [o for o in c["journal"] if o["instant"] < instant]
    pre = {"garde_adaptee": c["prealables"]["garde_adaptee"] if c["prealables"]["garde_adaptee"]["instant"] < instant else None,
           "rendez_vous": [e for e in c["prealables"]["rendez_vous"] if e["instant"] < instant]}
    return lignes, journal, pre


def classer_cas(r: dict, mode: str, mode_p: str, deja: bool) -> dict:
    """Un cas de (0 bis) joué par les gardes du module, chacune sur ce qui existe à son instant : étape A à oA (lignes et journal
    antérieurs ; `deja` : étape A déjà jouée), fin de l'étape A à fA, étape B après tous les événements. Rend l'étape où la chaîne
    s'arrête, les codes de chaque garde et l'issue : la première, dans l'ordre du texte, des codes de toutes les gardes (comme les
    prédicats du script, écrits sur l'ensemble des dates), ou l'étape B possible."""
    c = _cas_synthetique(r, mode, mode_p, deja)
    t = c["t"]
    la, ja, pa = _vus(c, t["oA"])
    la = {k: v for k, v in la.items() if k not in (rg.SCORES_T07, rg.SONDES_T07)}
    a = garde_etape_a(t["oA"], la, ja, pa, c["decisions"], deja=deja)
    lf, jf, _ = _vus(c, t["fA"])
    f = garde_fin_etape_a(t["fA"], lf, jf)
    lb, jb, pb = _vus(c, None)
    b = garde_etape_b(lb, jb, pb, c["decisions"])
    arret = "A" if a else "fin-A" if f else "B" if b else None
    tous = a + f + b
    code = premier_code(tous)
    if code is None:
        issue = B_REDUITE if mode == "réduite" else B_NORMAL
    else:
        issue = ISSUE_0BIS[code]
    return {"arret": arret, "codes": {"A": [x for x, _ in a], "fin-A": [x for x, _ in f], "B": [x for x, _ in b]}, "issue": issue,
            "etape_b": arret is None}


def enumerer_0bis() -> dict:
    """Énumération (0 bis) du brouillon 17 (192 cas, 8 configurations impossibles sautées) jouée par les gardes du module ; rend
    les cas (clé (ordre, mode, mode_p, deja) → issue), les effectifs par issue et le nombre d'étapes B possibles."""
    cas, issues, impossibles = {}, {}, 0
    for mode in ("pleine", "réduite"):
        evenements = ("S", "oA", "fA", "V", "P") + (("R",) if mode == "réduite" else ())
        for ordre in permutations(evenements):
            r = {e: i for i, e in enumerate(ordre)}
            if not (r["S"] < r["oA"] < r["fA"]):
                continue
            if mode == "pleine" and not r["P"] < r["V"]:
                continue
            if mode == "réduite" and not (r["R"] < r["V"] and r["R"] < r["P"]):
                continue
            if mode == "réduite" and r["R"] > r["fA"]:
                impossibles += 4
                continue
            for mode_p in (jp.PLEINE, jp.PLEINE_ANTICIPEE):
                for deja in (False, True):
                    x = classer_cas(r, mode, mode_p, deja)
                    cas[(ordre, mode, mode_p, deja)] = x
                    issues[x["issue"]] = issues.get(x["issue"], 0) + 1
    return {"cas": cas, "n": len(cas), "impossibles": impossibles, "issues": dict(sorted(issues.items())),
            "etapes_b": sum(x["etape_b"] for x in cas.values())}


__all__ = ["garde_etape_a", "garde_fin_etape_a", "garde_etape_b", "garde_g4", "instant_fermeture", "reserve_r14", "reduite_avant",
           "controler_reduite", "controler_pleine", "derniere_decision", "motif_selon_decision", "premier_code", "fin_etape_a",
           "classer_cas", "enumerer_0bis", "CODES", "NATURE", "ISSUE_0BIS", "B_REDUITE", "B_NORMAL", "PHRASE_R14", "DEJA",
           "ANTICIPEE", "PLEINE_AVANT_A", "VERDICT_AVANT_A", "PLEINE_AVANT_FIN_A", "VERDICT_PENDANT_A", "SCELLEMENT_APRES_VERDICT",
           "VERSION_APRES_VERDICT", "APPUI_FAUX", "ATTENTE_PLEINE", "ATTENTE_VERDICT_PROSE", "ANTERIORITE",
           "MOTIF_OUVRIR_PLEINEMENT", "MOTIF_MAINTENIR", "MOTIF_DECISION_ABSENTE"]
