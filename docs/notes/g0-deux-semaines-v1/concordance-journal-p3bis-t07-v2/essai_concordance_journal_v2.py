#!/usr/bin/env python3
"""Essai de concordance du journal des ouvertures de P3-bis (écrivain) avec le lecteur de T0.7, v2 — préalable P-9 de P3-bis.

Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-concordance-journal-p3bis-t07-p9-v1.md`
(`38a3b339…`), mandat, points 1 et 2. Écrit le 2026-11-11 (heure relevée par `date -u` : 13:37 UTC) par un agent neuf, qui n'a
écrit ni le code de P3-bis, ni celui de T0.7, ni leurs textes, ni leurs contre-lectures. Reprend la v1
(`concordance-journal-p3bis-t07-v1/essai_concordance_journal_v1.py`, `b30c9db7…`, gardée telle quelle, R12) ; changements :

- **commits finaux** : écrivain au commit du code de P3-bis `5e457525` (module `premier_test_ia/ouverture_p3bis_v3.py`, nommé
  par la consigne, **et** `premier_test_ia/ouverture_p3bis_v2.py`, que le plan, point 8, du candidat 1 nomme pour `ouvrir` ; les
  deux sont joués) ; lecteur au commit C7 `b4cd9953` de la ligne `CODE-T07` (`t07/journal_p3bis_v1.py` et ce qu'il importe,
  `t07/registre_v1.py` ; `t07/garde_adaptee_v1.py` pour la vue de T0.7) ;
- **deux bacs à sable** : `src/` de chaque commit extrait par `git archive <commit> src | tar -x -C <bac>`, empreintes
  comparées aux compagnons à leur commit (écrivain) et au fichier de la ligne `CODE-T07` (lecteur, sans compagnon au commit) ;
  l'écrivain et le lecteur tournent chacun dans **son propre processus** (`python -I`), qui n'importe que son bac ;
- **attentes mises à jour** aux corrections D-1 à D-4 (R-2103, R-2113) : horloge en arrière refusée sans ligne (D01, X06),
  `pleine-anticipee` refusée dès que `SCORES-T07` et `SONDES-T07` sont conformes (S06a, S08 ; lecture littérale S06c), fichier
  vide hors format (N05), chemin `prereg/T0.7-sondes-v0-v1.md` exigé sous « ouvrir » (D04 ; C-4 : D04b), clé `-01` (R08b) ;
- **retour chariot seul et fins de ligne mêlées** (C-1 de la contre-lecture `845c4de5…`), avec l'écrivain dans la boucle
  (X01 à X06) et en sondes d'état ;
- **oracle du texte** : le prédicat du plan, point 8, du candidat 1 de P3-bis (`9a56a657…`), récrit ici à la main sans importer
  aucun des deux codes, jugé sur chaque journal final et chaque sonde, à côté de l'écrivain (`lire_journal`) et du lecteur
  (`lire_journal_p3bis`) ; lectures déclarées de l'oracle : « espaces de bord » = U+0020 seulement ; chiffres de la date =
  ASCII ; fichier non décodable en UTF-8 = hors format.

    /home/user/controle-ia-travail/.venv/bin/python -I essai_concordance_journal_v2.py principal DOSSIER_NEUF [--clone CLONE]
    … principal DOSSIER_NEUF_2 --temoin     (témoin R5 : lecteur muté à dessein après la vérification des empreintes —
                                            ligne vide ignorée, refus pris pour ouverture — ; code 0 si l'essai le détecte)

`DOSSIER_NEUF` ne doit pas exister ; le script n'écrit que sous lui et ne l'efface pas. Aucun appel externe. Les sous-commandes
`ecrivain` et `lecteur` sont appelées par `principal`. Code de sortie : 0 si chaque empreinte est conforme et si chaque tentative
non exploratoire a donné à l'écrivain l'issue que le scénario vise, 1 sinon (essai faux). Les discordances ne changent pas le
code : elles sont imprimées.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
from datetime import datetime, timezone
from pathlib import Path

COMMIT_ECRIVAIN = "5e4575259478af3611e2c7fb1313342912caf484"
COMMIT_LECTEUR = "b4cd9953d199dd8f220f5162e5868c5b00fd392d"          # C7, ligne CODE-T07
CODE_T07_JSON = "registres/code-t07/CODE-T07-v2.json"
CODE_T07_JSON_SHA = "d5eb0b665df187d158fa84deff733b0f382fc309510163625f7aaea1ae9a692c"
REGISTRE_SCELLEMENTS = "registres/scellements-v1.md"
# empreintes attendues (relevées par `git show` au commit, puis contrôlées à l'extraction contre les compagnons)
ECRIVAIN = {
    "src/controle_ia/__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "src/controle_ia/gardes.py": "a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439",
    "src/controle_ia/scellement.py": "93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2",
    "src/controle_ia/premier_test_ia/__init__.py": "c72da1602f1998e4c7b30b670e89143d6a9c6337b903164f4bc6eed5ab9a5f92",
    "src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py": "1361382e669f26d5568c81044e160c7fc122f4264832ffb70ec8d9b4714d2a13",
    "src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py": "4a54a437e4a6031b1890f0f5f0261cf1141e72aee82d456d9fcd5483946693e9",
}
LECTEUR = {
    "src/controle_ia/__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "src/controle_ia/gardes.py": "a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439",
    "src/controle_ia/t07/__init__.py": "553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e",
    "src/controle_ia/t07/registre_v1.py": "e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec",
    "src/controle_ia/t07/journal_p3bis_v1.py": "f83f03d54accc0ac189e05c2f3e865b27ecb817f6c9366836d6e38d016826f73",
    "src/controle_ia/t07/garde_adaptee_v1.py": "7ff571d7b1f06db94043545bfe178a066613ddd734aacca1cf3ef52ba0b511de",
}
MODULES_ECRIVAIN = ("v3", "v2")

# Dates du banc (UTC). La date du rendez-vous de l'écrivain est 2026-11-20T12:00:00Z (`DATE_RENDEZ_VOUS`).
D_ECRIT = "2026-11-15T10:00:00Z"
D_SCEL = "2026-11-16T10:00:00Z"            # SCELLEMENT-T07
D_GARDE = "2026-11-16T11:00:00Z"           # GARDE-ADAPTEE-T07-P3BIS
D_PAQUET = "2026-11-17T00:00:00Z"          # date de la mise en paquet (`--date-paquet`)
D_DEC1, D_RDV1 = "2026-11-20T12:30:00Z", "2026-11-20T13:00:00Z"
D_SCORES_TOT = "2026-11-20T13:30:00Z"      # SCORES-T07 et SONDES-T07 avant l'ouverture réduite (E-8)
T_REDUITE = "2026-11-20T14:00:00Z"
T_ENTRE = "2026-11-20T14:10:00Z"
D_DEC2, D_RDV2 = "2026-11-20T14:30:00Z", "2026-11-20T15:00:00Z"
T_ANTICIPEE = "2026-11-20T16:00:00Z"
T_SOIR = "2026-11-20T17:00:00Z"
D_SCORES = "2026-11-21T10:00:00Z"          # SCORES-T07 et SONDES-T07 (fin de l'étape A)
T_AVANT = "2026-11-21T11:00:00Z"
T_PLEINE = "2026-11-21T12:00:00Z"
T_APRES = "2026-11-21T13:00:00Z"
T_T07 = "2026-11-30T00:00:00Z"             # instant où T0.7 lit le registre des préalables (étape B)
PREREG_T07 = "prereg/T0.7-sondes-v0-v1.md"
ECRITS = (("ECRIT-PERIMETRE-JEUX-P3BIS", "docs/ecrits/perimetre-v1.md"),
          ("ECRIT-LANCEMENT-RELANCE-P3BIS", "docs/ecrits/lancement-v1.md"),
          ("ECRIT-ENGAGEMENT-ETAPE-A-P3BIS", "docs/ecrits/engagement-v1.md"))
CHAMPS = ("cle", "date", "instant", "mode", "appui", "paquets", "motif")


def date_u() -> str:
    return subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()


def sha_octets(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


def texte_du_journal(octets: bytes) -> str:
    """Lecture en mode texte (CRLF et CR seul → LF), octets non UTF-8 gardés par `surrogateescape` (pour l'essai seulement)."""
    return octets.decode("utf-8", errors="surrogateescape").replace("\r\n", "\n").replace("\r", "\n")


# ================================================================================================= oracle du texte
ENTETE = ("| clé | date | mode | appui | paquets | motif |", "|---|---|---|---|---|---|")
CLES_JOURNAL = ("OUVERTURE-P3BIS", "REFUS-OUVERTURE-P3BIS")
MODES = ("pleine", "reduite", "pleine-anticipee")
CODES_FERMES = ("registre-absent", "ligne-absente", "ligne-double", "ligne-mal-formee", "sceau-faux", "compagnon-absent",
                "date-posterieure", "cle-inconnue", "rendez-vous-non-consecutif", "rendez-vous-non-croissant",
                "ligne-apres-decision-finale", "ni-scores-ni-ouvrir", "decision-maintenir", "garde-adaptee-absente",
                "garde-adaptee-posterieure", "deja-ouverte", "paquet-faux")
O_DATE = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})Z")
O_SHA = re.compile(r"[0-9a-f]{64}")
O_RDV = re.compile(r"RENDEZ-VOUS-P3BIS-[1-9][0-9]*")
O_CLES_APPUI = ("SCORES-T07", "SONDES-T07", "GARDE-ADAPTEE-T07-P3BIS")
SUIVANTS = {None: MODES, "reduite": ("pleine", "pleine-anticipee"), "pleine": (), "pleine-anticipee": ()}


def oracle(chemin: Path) -> dict:
    """Prédicat du plan, point 8, du candidat 1 de P3-bis, récrit à la main d'après le texte (aucun des deux codes importé).
    Rend {"etat": "absent" | "au format" | "hors format", "lignes": [...], "fautes": [...]}."""
    p = Path(chemin)
    if not p.exists():
        return {"etat": "absent", "lignes": [], "fautes": []}
    if not p.is_file():
        return {"etat": "hors format", "lignes": [], "fautes": ["pas un fichier"]}
    b = p.read_bytes()
    if b == b"":
        return {"etat": "hors format", "lignes": [], "fautes": ["fichier vide (0 octet)"]}
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        return {"etat": "hors format", "lignes": [], "fautes": ["non lisible en UTF-8"]}
    t = t.replace("\r\n", "\n").replace("\r", "\n")          # CRLF et retour chariot seul lus comme LF, mêlés ou non
    fautes = []
    if not t.endswith("\n"):
        fautes.append("(i) pas de saut de ligne final")
        lignes = t.split("\n")
    else:
        lignes = t[:-1].split("\n")
    if tuple(lignes[:2]) != ENTETE:
        fautes.append("(ii) en-tête")
    lus = []
    for n, l in enumerate(lignes[2:], start=3):
        if l == "":
            fautes.append(f"(iii) l.{n} ligne vide")
            continue
        if not (len(l) >= 2 and l.startswith("|") and l.endswith("|")):
            fautes.append(f"(iii) l.{n} ne commence ou ne finit pas par |")
            continue
        c = [x.strip(" ") for x in l[1:-1].split("|")]
        if len(c) != 6:
            fautes.append(f"(iii) l.{n} {len(c)} cellules")
            continue
        cle, date, mode, appui, paquets, motif = c
        if cle not in CLES_JOURNAL:
            fautes.append(f"(iv) l.{n} clé")
            continue
        m = O_DATE.fullmatch(date)
        if not m:
            fautes.append(f"(iv) l.{n} forme de date")
            continue
        try:
            instant = int(datetime(*map(int, m.groups()), tzinfo=timezone.utc).timestamp())
        except ValueError:
            fautes.append(f"(iv) l.{n} date impossible")
            continue
        if mode not in MODES:
            fautes.append(f"(iv) l.{n} mode")
            continue
        cles, bon = [], True
        if appui != "-":
            for j in appui.split(" "):
                k, egal, s = j.partition("=")
                if not egal or not (k in O_CLES_APPUI or O_RDV.fullmatch(k)) or not O_SHA.fullmatch(s):
                    bon = False
                    break
                cles.append(k)
        if not bon:
            fautes.append(f"(v) l.{n} appui")
            continue
        if cle == "OUVERTURE-P3BIS":
            forme = {"pleine": cles == ["SCORES-T07", "SONDES-T07"],
                     "reduite": len(cles) == 2 and bool(O_RDV.fullmatch(cles[0])) and cles[1] == "GARDE-ADAPTEE-T07-P3BIS",
                     "pleine-anticipee": len(cles) == 1 and bool(O_RDV.fullmatch(cles[0]))}[mode]
            if not forme:
                fautes.append(f"(vi) l.{n} appui hors de la forme du mode")
                continue
            ps = paquets.split(" ")
            if not (len(ps) == 2 and all(O_SHA.fullmatch(x) for x in ps)):
                fautes.append(f"(vi) l.{n} paquets d'une ouverture")
                continue
            if motif != "-":
                fautes.append(f"(vi) l.{n} motif d'une ouverture")
                continue
        else:
            ps = paquets.split(" ")
            if not (paquets == "-" or (len(ps) == 2 and all(O_SHA.fullmatch(x) for x in ps))):
                fautes.append(f"(vi) l.{n} paquets d'un refus")
                continue
            code, sep, reste = motif.partition(" : ")
            if not (sep and code in CODES_FERMES and reste and reste[0] != " "):
                fautes.append(f"(vi) l.{n} motif d'un refus")
                continue
        lus.append({"numero": n, "cle": cle, "date": date, "instant": instant, "mode": mode, "appui": appui,
                    "paquets": paquets, "motif": motif})
    for k in range(1, len(lus)):
        if lus[k]["instant"] < lus[k - 1]["instant"]:
            fautes.append(f"(vii) l.{lus[k]['numero']} date qui recule")
    etat = None
    for x in lus:
        if x["cle"] != "OUVERTURE-P3BIS":
            continue
        if x["mode"] not in SUIVANTS[etat]:
            fautes.append(f"(viii) l.{x['numero']} ordre interdit")
            continue
        etat = x["mode"]
    if fautes:
        return {"etat": "hors format", "lignes": [], "fautes": fautes}
    return {"etat": "au format", "lignes": lus, "fautes": []}


# ================================================================================================= extraction (principal)
def git_show(clone: Path, commit: str, chemin: str) -> bytes | None:
    r = subprocess.run(["git", "-C", str(clone), "show", f"{commit}:{chemin}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def extraire_src(clone: Path, commit: str, bac: Path) -> None:
    """`git archive <commit> src | tar -x -C <bac>`."""
    bac.mkdir(parents=True)
    archive = subprocess.Popen(["git", "-C", str(clone), "archive", commit, "src"], stdout=subprocess.PIPE)
    tar = subprocess.run(["tar", "-x", "-C", str(bac)], stdin=archive.stdout)
    archive.stdout.close()
    if archive.wait() != 0 or tar.returncode != 0:
        raise SystemExit(f"ESSAI FAUX : extraction de src au commit {commit[:8]} en échec")


def verifier_bacs(clone: Path, dossier: Path) -> tuple[list, list]:
    """Empreintes : fichier extrait = `git show` au commit = valeur attendue ; compagnon au commit, s'il existe, égal ;
    côté lecteur, fichier de la ligne `CODE-T07` (sceau et champ `commit`)."""
    lignes, faux = [], []
    for cote, commit, table in (("écrivain", COMMIT_ECRIVAIN, ECRIVAIN), ("lecteur", COMMIT_LECTEUR, LECTEUR)):
        bac = dossier / ("bac-ecrivain" if cote == "écrivain" else "bac-lecteur")
        for chemin, attendu in table.items():
            ext = sha_octets((bac / chemin).read_bytes()) if (bac / chemin).is_file() else None
            gs = git_show(clone, commit, chemin)
            gs = sha_octets(gs) if gs is not None else None
            comp = git_show(clone, commit, chemin + ".sha256")
            comp = comp.decode().split()[0] if comp else None
            comp_ext = (bac / (chemin + ".sha256")).is_file()
            etat = "conforme" if ext == gs == attendu and (comp is None or comp == attendu) else "NON CONFORME"
            if etat != "conforme":
                faux.append(f"{cote} {chemin} : extrait {ext}, git show {gs}, attendu {attendu}, compagnon {comp}")
            lignes.append(f"{cote} {commit[:8]} {chemin} : {ext} ; compagnon au commit : "
                          + (f"{comp} ({'égal' if comp == ext else 'DIFFÉRENT'})" if comp else "aucun")
                          + ("" if (comp is not None) == comp_ext else " ; compagnon extrait incohérent") + f" ; {etat}")
    # fichier de la ligne CODE-T07 (dans le clone de travail, tel qu'inscrit au registre)
    j = clone / CODE_T07_JSON
    octets = j.read_bytes()
    reg = [l for l in (clone / REGISTRE_SCELLEMENTS).read_text(encoding="utf-8").splitlines() if l.startswith("| CODE-T07 |")]
    cellules = [c.strip() for c in reg[-1].strip("|").split("|")] if reg else []
    code = json.loads(octets)
    ok = (sha_octets(octets) == CODE_T07_JSON_SHA and len(reg) == 1 and cellules[2] == CODE_T07_JSON
          and cellules[3] == CODE_T07_JSON_SHA and code["commit"] == COMMIT_LECTEUR)
    lignes.append(f"ligne CODE-T07 : {' | '.join(cellules)} ; fichier {sha_octets(octets)} ; commit {code['commit'][:8]} ; "
                  + ("conforme" if ok else "NON CONFORME"))
    if not ok:
        faux.append("ligne CODE-T07 ou son fichier non conformes")
    for chemin, attendu in LECTEUR.items():
        cle = chemin
        if "/t07/" in chemin:
            v = code["fichiers"].get(cle)
            etat = "égale" if v == attendu else "DIFFÉRENTE"
            if v != attendu:
                faux.append(f"{chemin} : CODE-T07 {v}, attendu {attendu}")
            lignes.append(f"lecteur {chemin} : empreinte de CODE-T07-v2.json {v} ({etat})")
    for chemin in ("src/controle_ia/__init__.py", "src/controle_ia/gardes.py"):
        a = git_show(clone, COMMIT_ECRIVAIN, chemin)
        b = git_show(clone, COMMIT_LECTEUR, chemin)
        lignes.append(f"commun {chemin} : {'mêmes octets aux deux commits' if a == b else 'DIFFÉRENT entre les commits'}")
    return lignes, faux


# ================================================================================================= écrivain (processus propre)
class Banc:
    def __init__(self, racine: Path, sceller):
        self.r, self._sceller = racine, sceller
        for d in ("registres", "docs/decisions", "sorties"):
            (racine / d).mkdir(parents=True, exist_ok=True)
        self.n_sortie = 0

    def scelle(self, rel: str, contenu: str, compagnon: bool = True) -> str:
        p = self.r / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(contenu, encoding="utf-8")
        if compagnon:
            self._sceller(p)
        return hashlib.sha256(p.read_bytes()).hexdigest()

    def ajouter(self, registre: str, lignes) -> None:
        p = self.r / registre
        neuf = not p.exists()
        with open(p, "a", encoding="utf-8") as f:
            if neuf:
                f.write(f"# {registre} (banc d'essai de concordance)\n\n")
            for l in lignes:
                f.write(l + "\n")

    def sortie(self) -> Path:
        self.n_sortie += 1
        return self.r / "sorties" / f"ouverture-{self.n_sortie}"


def L(cle, date, rel, sha) -> str:
    return f"| {cle} | {date} | {rel} | {sha} |"


def l_ecrits(b: Banc, date=D_ECRIT) -> list:
    return [L(k, date, rel, b.scelle(rel, f"écrit {k} (banc)\n")) for k, rel in ECRITS]


def l_scellement(b: Banc, date=D_SCEL, rel=PREREG_T07) -> tuple[str, str]:
    sha = b.scelle(rel, "texte de T0.7 (banc)\n")
    return L("SCELLEMENT-T07", date, rel, sha), sha


def l_rdv(b: Banc, n: int, mot: str | None, date_dec: str | None, date_ligne: str, cle: str | None = None) -> str:
    rel = f"docs/decisions/rendez-vous-P3-bis-v{n}.md"
    texte = f"# Rendez-vous de P3-bis, décision {n} (banc)\n\n"
    if mot is not None:
        texte += f"Décision : {mot}\n"
    if date_dec is not None:
        texte += f"Date : {date_dec}\n"
    return L(cle or f"RENDEZ-VOUS-P3BIS-{n}", date_ligne, rel, b.scelle(rel, texte))


def l_scores(b: Banc, date: str) -> list:
    return [L("SCORES-T07", date, "donnees/r7b/scores-actions-t07.npz", b.scelle("donnees/r7b/scores-actions-t07.npz", "scores\n")),
            L("SONDES-T07", date, "diag/r7b/sondes-t07.json", b.scelle("diag/r7b/sondes-t07.json", "{}\n"))]


def monter(b: Banc, *, ecrits=True, scel=True, scel_date=D_SCEL, scel_rel=PREREG_T07, garde=D_GARDE, garde_cite=None,
           rdv=(), scores=None, retouche=None) -> None:
    """Registre des préalables et registre des scellements du banc (comme la v1). `rdv` : [(décision, date de la décision, date
    de la ligne)]. `garde_cite` : (chemin, contenu) d'un autre texte cité par la garde adaptée. `retouche(b, lignes)` : lignes du
    registre des préalables modifiées pour un artefact."""
    pre, sc = [], []
    sha_scel = None
    if scel:
        ligne, sha_scel = l_scellement(b, scel_date, scel_rel)
        sc.append(ligne)
    if ecrits:
        pre += l_ecrits(b)
    if garde is not None:
        if garde_cite is not None:
            pre.append(L("GARDE-ADAPTEE-T07-P3BIS", garde, garde_cite[0], b.scelle(*garde_cite)))
        else:
            if sha_scel is None:
                sha_scel = b.scelle(scel_rel, "texte de T0.7 (banc)\n")
            pre.append(L("GARDE-ADAPTEE-T07-P3BIS", garde, scel_rel, sha_scel))
    for n, (mot, dd, dl) in enumerate(rdv, start=1):
        pre.append(l_rdv(b, n, mot, dd, dl))
    if retouche is not None:
        pre = retouche(b, pre)
    if pre:                                       # aucune ligne : registre des préalables absent (R01)
        b.ajouter("registres/prealables-p3bis-v1.md", pre)
    if scores is not None:
        sc += l_scores(b, scores)
    if sc:
        b.ajouter("registres/scellements-v1.md", sc)


def faire_paquets(depot: Path, run: str, ob, sceller) -> None:
    d = depot / "donnees" / run
    d.mkdir(parents=True)
    (d / "jouet.txt").write_text(f"donnée jouet du {run}\n", encoding="utf-8")
    sceller(d / "jouet.txt")
    (depot / "diag" / run).mkdir(parents=True)
    (depot / "diag" / run / "episodes-p3.json").write_text("{}\n", encoding="utf-8")
    sceller(depot / "diag" / run / "episodes-p3.json")
    ob.fermer_run(depot, run, partiel=True)
    cible = depot / ob.dossier_ferme(run) / ob.PAQUET_LECTURES
    cible.parent.mkdir(parents=True)
    archive = ob.tar_de([(f"runs/lecture-jouet-{run}/sortie.txt", f"sortie jouet du {run}\n".encode())], tarfile.PAX_FORMAT)
    cible.write_bytes(ob.paquet_lectures(archive, ob.tirer_sel()))
    sceller(cible)


def lignes_de(texte):
    if texte is None or texte == "<dossier>":
        return []
    l = texte.split("\n")
    return l[:-1] if l and l[-1] == "" else l


def avec_fins(lignes: list, fins) -> bytes:
    """Lignes rejointes avec des fins de ligne données (une par ligne, répétées en cycle)."""
    return "".join(l + fins[k % len(fins)] for k, l in enumerate(lignes)).encode("utf-8")


class Ecrivain:
    def __init__(self, travail: Path, ob, gardes, scellement):
        self.ob, self.gardes, self.scellement = ob, gardes, scellement
        self.depot = travail / "depot"
        self.sondes_dir = travail / "sondes"
        self.sondes_dir.mkdir()
        self.faux, self.resultats, self.sondes = [], [], []

    # ---------------------------------------------------------------------------------------------- tentatives
    def etat(self, b: Banc):
        p = b.r / self.ob.JOURNAL_OUVERTURES
        if p.is_dir():
            return "<dossier>"
        return texte_du_journal(p.read_bytes()) if p.exists() else None

    def tenter(self, s: dict, b: Banc, mode: str, instant: str, attendu: tuple | None, run: str = "run-a",
               sortie: Path | None = None, panne_extraction: bool = False, n_lignes: int | None = None,
               attendu_texte: str | None = None) -> None:
        """`attendu` None : tentative exploratoire (issue rapportée, non exigée ; `attendu_texte` dit ce que le texte prévoit)."""
        ob, G = self.ob, self.gardes.GardeArret
        avant = self.etat(b)
        sortie = b.sortie() if sortie is None else sortie
        extraire = ob.extraire
        if panne_extraction:
            def _panne(fichiers, sortie_):
                raise OSError("panne d'écriture simulée par l'essai")
            ob.extraire = _panne
        try:
            ob.ouvrir(b.r, mode, run, sortie, racine_paquets=self.depot, date_paquet=D_PAQUET,
                      instant=ob.instant_utc(instant), imprimer=lambda *_: None)
            issue = ["ouverture", mode, 0, ""]
        except ob.RefusOuverture as e:
            issue = ["refus", e.code, 2, str(e)[:160]]
        except ob.HorlogeEnArriere as e:
            issue = ["horloge-en-arriere", None, 2, str(e)[:160]]
        except ob.JournalImpossible as e:
            issue = ["journal-impossible", None, 2, str(e)[:160]]
        except G as e:
            issue = ["arret", None, 1, str(e)[:160]]
        except Exception as e:                                       # noqa: BLE001 — rapporté, jamais avalé en silence
            issue = ["exception", type(e).__name__, "trace, 1", str(e)[:160]]
        finally:
            ob.extraire = extraire
        apres = self.etat(b)
        la, lp = lignes_de(avant), lignes_de(apres)
        if lp[:len(la)] != la:
            self.faux.append(f"{s['id']} : le journal n'est pas en ajout seul")
        neuves = [(n, x) for n, x in enumerate(lp, start=1)
                  if n > len(la) and not (n <= 2 and x == ob.ENTETE_JOURNAL[n - 1] and avant is None)]
        if attendu is not None:
            if attendu[0] in ("ouverture", "refus"):
                vise = issue[0] == attendu[0] and issue[1] == attendu[1]
            else:
                vise = issue[0] == attendu[0]
            if n_lignes is None:
                n_lignes = 1 if attendu[0] in ("ouverture", "refus") else 0
            if not vise or len(neuves) != n_lignes:
                self.faux.append(f"{s['id']} : tentative {mode} @{instant} : issue {issue[:3]} et {len(neuves)} ligne(s), "
                                 f"{attendu} et {n_lignes} ligne(s) visées")
        parses = []
        for n, brute in neuves:
            try:
                d = ob.lire_ligne_journal(brute)
                parses.append([n, brute, {c: d[c] for c in CHAMPS}])
            except G as e:
                parses.append([n, brute, {"faute_ecrivain": str(e)}])
        s["tentatives"].append({"mode": mode, "instant": instant, "issue": issue, "attendu": attendu,
                                "attendu_texte": attendu_texte, "neuves": parses})

    def main_sur_journal(self, b: Banc, octets: bytes) -> None:
        (b.r / self.ob.JOURNAL_OUVERTURES).write_bytes(octets)

    def instantane(self, s: dict, b: Banc, nom: str) -> None:
        """Copie de l'état présent du journal, gardée comme sonde d'état (lue par les trois juges)."""
        p = self.sondes_dir / f"{s['id']}-{len(s.setdefault('instantanes', [])) + 1}.md"
        p.write_bytes((b.r / self.ob.JOURNAL_OUVERTURES).read_bytes())
        s["instantanes"].append(str(p))
        self.sonde(f"{s['id']} : {nom}", p)

    def relire(self, s: dict, b: Banc) -> None:
        chemin = b.r / self.ob.JOURNAL_OUVERTURES
        s["journal_present"] = chemin.exists()
        try:
            s["ecrivain_relit"] = f"{len(self.ob.lire_journal(chemin))} ligne(s), aucun refus"
        except self.ob.RefusOuverture as e:
            s["ecrivain_relit"] = f"refus {e.code}"
        except Exception as e:                                       # noqa: BLE001
            s["ecrivain_relit"] = f"exception {type(e).__name__}"

    # ---------------------------------------------------------------------------------------------- scénarios
    def scenario(self, ident: str, titre: str, attendu_lecteur: str = "lu", vue_t07: bool = False) -> tuple[dict, Banc]:
        racine = self.depot / "scenarios" / ident
        b = Banc(racine, self.scellement.sceller)
        s = {"id": ident, "titre": titre, "tentatives": [], "attendu_lecteur": attendu_lecteur, "vue_t07": vue_t07,
             "racine": str(racine), "journal": str(racine / self.ob.JOURNAL_OUVERTURES)}
        self.resultats.append(s)
        return s, b

    def jouer(self) -> None:
        ob = self.ob
        O, R = "ouverture", "refus"
        J = self.relire

        # ---- ouvertures (chaque mode, chaque chemin) ----
        s, b = self.scenario("S01", "chemin normal : pleine, puis deja-ouverte (pleine et reduite), puis erreurs d'appel",
                             vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        prem = b.r / "sorties" / "ouverture-1"
        self.tenter(s, b, "pleine", T_APRES, (R, "deja-ouverte"))
        self.tenter(s, b, "reduite", T_APRES, (R, "deja-ouverte"))
        self.tenter(s, b, "totale", T_APRES, ("arret",))                       # mode inconnu : erreur d'appel, aucune ligne
        self.tenter(s, b, "pleine", T_APRES, ("arret",), sortie=prem)           # sortie déjà présente : aucune ligne
        J(s, b)

        s, b = self.scenario("S02", "branche 1 : reduite sous « ouvrir », pleine-anticipee refusée, complément pleine",
                             vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        self.tenter(s, b, "pleine-anticipee", T_ENTRE, (R, "ni-scores-ni-ouvrir"))
        self.tenter(s, b, "pleine", T_SOIR, (R, "ligne-absente"))              # E-3 : pleine sous « ouvrir » sans lignes de T0.7
        b.ajouter("registres/scellements-v1.md", l_scores(b, D_SCORES))
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        J(s, b)

        s, b = self.scenario("S03", "branche 2 : pleine-anticipee sous « ouvrir pleinement »", vue_t07=True)
        monter(b, rdv=[("ouvrir pleinement", D_DEC1, D_RDV1)])
        self.tenter(s, b, "pleine-anticipee", T_ANTICIPEE, (O, "pleine-anticipee"))
        J(s, b)

        s, b = self.scenario("S04", "E-9 : « ouvrir », reduite, « ouvrir pleinement », complément pleine-anticipee", vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        b.ajouter("registres/prealables-p3bis-v1.md", [l_rdv(b, 2, "ouvrir pleinement", D_DEC2, D_RDV2)])
        self.tenter(s, b, "pleine-anticipee", T_ANTICIPEE, (O, "pleine-anticipee"))
        J(s, b)

        s, b = self.scenario("S05", "E-8 : reduite sous « ouvrir » après SCORES-T07 et SONDES-T07, puis pleine", vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)], scores=D_SCORES_TOT)
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        self.tenter(s, b, "pleine", T_ANTICIPEE, (O, "pleine"))
        J(s, b)

        s, b = self.scenario("S06a", "E-8, D-2 : pleine-anticipee sous « ouvrir pleinement », SCORES-T07 et SONDES-T07 conformes "
                                     "(refus), puis pleine", vue_t07=True)
        monter(b, rdv=[("ouvrir pleinement", D_DEC1, D_RDV1)], scores=D_SCORES_TOT)
        self.tenter(s, b, "pleine-anticipee", T_ANTICIPEE, (R, "ni-scores-ni-ouvrir"))
        self.tenter(s, b, "pleine", T_SOIR, (O, "pleine"))
        J(s, b)

        s, b = self.scenario("S06b", "E-8 : même banc que S06a, pleine demandée d'emblée (rendez-vous sans objet)", vue_t07=True)
        monter(b, rdv=[("ouvrir pleinement", D_DEC1, D_RDV1)], scores=D_SCORES_TOT)
        self.tenter(s, b, "pleine", T_ANTICIPEE, (O, "pleine"))
        J(s, b)

        s, b = self.scenario("S06c", "D-2, lecture littérale (R-2113) : SCORES-T07 inscrite sans compagnon (non conforme), "
                                     "pleine-anticipee sous « ouvrir pleinement » permise", vue_t07=True)
        monter(b, rdv=[("ouvrir pleinement", D_DEC1, D_RDV1)], scores=D_SCORES_TOT)
        os.remove(b.r / "donnees/r7b/scores-actions-t07.npz.sha256")
        self.tenter(s, b, "pleine-anticipee", T_ANTICIPEE, (O, "pleine-anticipee"))
        J(s, b)

        s, b = self.scenario("S07", "E-9 ajout : reduite (run-a), complément pleine sur d'autres paquets (run-b), puis run-a",
                             vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        b.ajouter("registres/scellements-v1.md", l_scores(b, D_SCORES))
        self.tenter(s, b, "pleine", T_PLEINE, (R, "paquet-faux"), run="run-b")
        self.tenter(s, b, "pleine", T_APRES, (O, "pleine"))
        J(s, b)

        s, b = self.scenario("S08", "E-9 et D-2 : reduite sous « ouvrir », SCORES-T07 et SONDES-T07 conformes, « ouvrir "
                                    "pleinement », pleine-anticipee refusée, puis pleine", vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        b.ajouter("registres/scellements-v1.md", l_scores(b, "2026-11-20T14:20:00Z"))
        b.ajouter("registres/prealables-p3bis-v1.md", [l_rdv(b, 2, "ouvrir pleinement", D_DEC2, D_RDV2)])
        self.tenter(s, b, "pleine-anticipee", T_ANTICIPEE, (R, "ni-scores-ni-ouvrir"))
        self.tenter(s, b, "pleine", T_SOIR, (O, "pleine"))
        J(s, b)

        # ---- refus : chaque code de la liste fermée, et les cas que la liste ne nomme pas (E-3) ----
        refus = [
            ("R01", "registre-absent", "pleine", dict(ecrits=False, garde=None, scores=D_SCORES), None),
            ("R02", "ligne-absente", "pleine", dict(scores=D_SCORES), lambda b_, p: [x for x in p if "ENGAGEMENT" not in x]),
            ("R03", "ligne-double", "pleine", dict(scores=D_SCORES), lambda b_, p: p + [p[0]]),
            ("R04a", "ligne-mal-formee", "pleine", dict(scores=D_SCORES),
             lambda b_, p: [x.replace(D_ECRIT, "2026-11-15 10:00:00") if "PERIMETRE" in x else x for x in p]),
            ("R04c", "ligne-mal-formee", "reduite", dict(rdv=[("ouvrir", None, D_RDV1)]), None),         # décision sans « Date : »
            ("R04d", "ligne-mal-formee", "reduite", dict(rdv=[("ouvrir", "2026-11-20T11:00:00Z", D_RDV1)]), None),   # avant le RDV
            ("R05a", "sceau-faux", "pleine", dict(scores=D_SCORES),
             lambda b_, p: [x.rsplit("| ", 1)[0] + "| " + "0" * 64 + " |" if "LANCEMENT" in x else x for x in p]),
            ("R05b", "sceau-faux", "pleine", dict(scores=D_SCORES),                                     # fichier cité absent
             lambda b_, p: (os.remove(b_.r / ECRITS[1][1]), os.remove(b_.r / (ECRITS[1][1] + ".sha256")), p)[2]),
            ("R06", "compagnon-absent", "pleine", dict(scores=D_SCORES),
             lambda b_, p: (os.remove(b_.r / (ECRITS[2][1] + ".sha256")), p)[1]),
            ("R07", "date-posterieure", "pleine", dict(scores=D_SCORES),
             lambda b_, p: [x.replace(D_ECRIT, "2026-11-25T10:00:00Z") if "PERIMETRE" in x else x for x in p]),
            ("R08", "cle-inconnue", "pleine", dict(scores=D_SCORES),
             lambda b_, p: p + [L("AUTRE-CLE-P3BIS", D_ECRIT, ECRITS[0][1], hashlib.sha256((b_.r / ECRITS[0][1]).read_bytes())
                                  .hexdigest())]),
            ("R09", "rendez-vous-non-consecutif", "reduite", dict(),
             lambda b_, p: p + [l_rdv(b_, 2, "ouvrir", D_DEC1, D_RDV1)]),
            ("R10", "rendez-vous-non-croissant", "reduite", dict(rdv=[("maintenir", D_DEC1, D_RDV1), ("ouvrir", D_DEC1, D_RDV1)]),
             None),
            ("R11", "ligne-apres-decision-finale", "pleine-anticipee",
             dict(rdv=[("ouvrir pleinement", D_DEC1, D_RDV1), ("maintenir", D_DEC2, D_RDV2)]), None),
            ("R12a", "ni-scores-ni-ouvrir", "pleine", dict(), None),
            ("R12b", "ni-scores-ni-ouvrir", "reduite", dict(rdv=[("ouvrir pleinement", D_DEC1, D_RDV1)]), None),
            ("R13", "decision-maintenir", "reduite", dict(rdv=[("maintenir", D_DEC1, D_RDV1)]), None),
            ("R14a", "garde-adaptee-absente", "reduite", dict(garde=None, rdv=[("ouvrir", D_DEC1, D_RDV1)]), None),
            ("R14b", "garde-adaptee-absente", "reduite",
             dict(garde_cite=("docs/ecrits/autre-texte-v1.md", "autre texte\n"), rdv=[("ouvrir", D_DEC1, D_RDV1)]), None),
            ("R15a", "garde-adaptee-posterieure", "reduite", dict(garde="2026-11-20T13:30:00Z", rdv=[("ouvrir", D_DEC1, D_RDV1)]),
             None),
            ("R15b", "garde-adaptee-posterieure", "reduite", dict(scel_date=D_RDV1, rdv=[("ouvrir", D_DEC1, D_RDV1)]), None),
            ("R17a", "paquet-faux", "pleine", dict(scores=D_SCORES), None),
        ]
        instants = {"pleine": T_PLEINE, "reduite": T_REDUITE, "pleine-anticipee": T_ANTICIPEE}
        for ident, code, mode, kw, retouche in refus:
            s, b = self.scenario(ident, f"refus {code} (mode {mode})")
            monter(b, retouche=retouche, **kw)
            self.tenter(s, b, mode, instants[mode], (R, code), run="run-absent" if ident == "R17a" else "run-a")
            J(s, b)

        s, b = self.scenario("R08b", "clé de rendez-vous à zéro en tête (RENDEZ-VOUS-P3BIS-01) : cle-inconnue ; préalables lus "
                                     "par T0.7", vue_t07=True)
        monter(b, retouche=lambda b_, p: p + [l_rdv(b_, 1, "ouvrir", D_DEC1, D_RDV1, cle="RENDEZ-VOUS-P3BIS-01")])
        self.tenter(s, b, "reduite", T_REDUITE, (R, "cle-inconnue"))
        J(s, b)

        s, b = self.scenario("R04b", "journal hors format (ligne à cinq cellules écrite à la main) : refus ligne-mal-formee, "
                                     "ligne neuve qui suit", attendu_lecteur="refus")
        monter(b, scores=D_SCORES)
        self.main_sur_journal(b, ("\n".join(ob.ENTETE_JOURNAL) + "\n| OUVERTURE-P3BIS | 2026-11-20T13:00:00Z | pleine | - | - |\n")
                              .encode())
        self.tenter(s, b, "pleine", T_PLEINE, (R, "ligne-mal-formee"))
        J(s, b)

        # ---- lignes sans journal (E-3 (b) et (c)) ; fichier vide (D-3) ; fichier non UTF-8 (exploratoire) ----
        s, b = self.scenario("N01", "journal impossible à écrire : dossier registres/ absent (refus sans ligne)")
        os.rmdir(b.r / "registres")
        self.tenter(s, b, "pleine", T_PLEINE, ("journal-impossible",))
        J(s, b)

        s, b = self.scenario("N02", "journal impossible à écrire : chemin du journal occupé par un dossier",
                             attendu_lecteur="refus")
        monter(b, scores=D_SCORES)
        (b.r / ob.JOURNAL_OUVERTURES).mkdir()
        self.tenter(s, b, "pleine", T_PLEINE, ("journal-impossible",))
        J(s, b)

        s, b = self.scenario("N04", "extraction en échec après la ligne OUVERTURE-P3BIS (code 1, la ligne reste)", vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "pleine", T_PLEINE, ("arret",), panne_extraction=True, n_lignes=1)
        J(s, b)

        s, b = self.scenario("N05", "D-3 : journal présent et vide (0 octet) avant la tentative : hors format, refus avec ligne, "
                                    "aucun en-tête écrit", attendu_lecteur="refus")
        monter(b, scores=D_SCORES)
        self.main_sur_journal(b, b"")
        self.instantane(s, b, "fichier vide avant la tentative")
        self.tenter(s, b, "pleine", T_PLEINE, (R, "ligne-mal-formee"))
        self.tenter(s, b, "pleine", T_APRES, (R, "ligne-mal-formee"))
        J(s, b)

        s, b = self.scenario("N06", "exploratoire : journal non lisible en UTF-8 (un octet 0xFF dans le texte d'un motif)",
                             attendu_lecteur="refus")
        monter(b, scores=D_SCORES)
        self.main_sur_journal(b, ("\n".join(ob.ENTETE_JOURNAL) + "\n").encode()
                              + b"| REFUS-OUVERTURE-P3BIS | 2026-11-21T10:30:00Z | pleine | - | - | deja-ouverte : x\xff |\n")
        self.instantane(s, b, "journal non UTF-8 avant la tentative")
        self.tenter(s, b, "pleine", T_PLEINE, None, attendu_texte="hors format : refus ligne-mal-formee, une ligne neuve suit")
        J(s, b)

        # ---- D-1 et D-4 ----
        s, b = self.scenario("D01", "D-1 : horloge en arrière : refus à 12:00, puis pleine demandée à 11:00 (refus sans ligne)",
                             vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_PLEINE, (R, "ni-scores-ni-ouvrir"))
        self.tenter(s, b, "pleine", T_AVANT, ("horloge-en-arriere",))
        J(s, b)

        s, b = self.scenario("D01b", "C-2 : ligne bien formée à 12:00, puis ligne hors format écrite à la main ; tentative à "
                                     "11:00 (dernière ligne hors format tenue pour antérieure)", attendu_lecteur="refus")
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_PLEINE, (R, "ni-scores-ni-ouvrir"))
        with open(b.r / ob.JOURNAL_OUVERTURES, "a", encoding="utf-8") as f:
            f.write("| REFUS-OUVERTURE-P3BIS | 2026-11-21T12:30:00Z | pleine | - | - |\n")
        self.tenter(s, b, "pleine", T_AVANT, (R, "ligne-mal-formee"))
        J(s, b)

        s, b = self.scenario("D02", "deux tentatives à la même seconde (dates égales)", vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_PLEINE, (R, "ni-scores-ni-ouvrir"))
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        J(s, b)

        s, b = self.scenario("D04", "D-4 : reduite, SCELLEMENT-T07 et garde adaptée citant un texte autre que "
                                    "prereg/T0.7-sondes-v0-v1.md (refus garde-adaptee-absente)", vue_t07=True)
        monter(b, scel_rel="prereg/T0.7-autre-v1.md", rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (R, "garde-adaptee-absente"))
        J(s, b)

        s, b = self.scenario("D04b", "C-4 : voie normale (pleine), SCELLEMENT-T07 et garde adaptée citant un autre chemin "
                                     "(non jugé hors de la branche 1)", vue_t07=True)
        monter(b, scel_rel="prereg/T0.7-autre-v1.md", scores=D_SCORES)
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        J(s, b)

        # ---- retour chariot seul et fins de ligne mêlées, l'écrivain dans la boucle (C-1 de 845c4de5) ----
        def lignes_lf(b_):
            return texte_du_journal((b_.r / ob.JOURNAL_OUVERTURES).read_bytes())[:-1].split("\n")

        s, b = self.scenario("X01", "retour chariot seul : refus, journal récrit en CR seul, puis pleine (ouverture) et "
                                    "deja-ouverte", vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_AVANT, (R, "ni-scores-ni-ouvrir"))
        self.main_sur_journal(b, avec_fins(lignes_lf(b), ["\r"]))
        self.instantane(s, b, "journal en CR seul")
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        self.instantane(s, b, "CR seul, puis la ligne de l'écrivain (CR LF, puis LF)")
        self.tenter(s, b, "pleine", T_APRES, (R, "deja-ouverte"))
        J(s, b)

        s, b = self.scenario("X02", "fins de ligne mêlées (CRLF, CR, LF) : reduite, refus, pleine", vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        self.main_sur_journal(b, avec_fins(lignes_lf(b), ["\r\n", "\r", "\n"]))
        self.instantane(s, b, "en-tête CRLF puis CR, ligne LF")
        self.tenter(s, b, "pleine-anticipee", T_ENTRE, (R, "ni-scores-ni-ouvrir"))
        self.main_sur_journal(b, avec_fins(lignes_lf(b), ["\r", "\n", "\r\n"]))
        self.instantane(s, b, "fins CR, LF, CRLF en cycle")
        b.ajouter("registres/scellements-v1.md", l_scores(b, D_SCORES))
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        J(s, b)

        s, b = self.scenario("X03", "CRLF partout : refus, journal récrit en CRLF, puis pleine", vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_AVANT, (R, "ni-scores-ni-ouvrir"))
        self.main_sur_journal(b, avec_fins(lignes_lf(b), ["\r\n"]))
        self.instantane(s, b, "journal en CRLF")
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        J(s, b)

        s, b = self.scenario("X04", "CR seul sans fin de ligne finale : hors format, refus ligne-mal-formee (l'écrivain ajoute "
                                    "le saut), puis pleine", vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_AVANT, (R, "ni-scores-ni-ouvrir"))
        self.main_sur_journal(b, avec_fins(lignes_lf(b), ["\r"])[:-1])
        self.instantane(s, b, "CR seul, sans fin de ligne finale")
        self.tenter(s, b, "pleine", T_PLEINE, (R, "ligne-mal-formee"))
        self.tenter(s, b, "pleine", T_APRES, (O, "pleine"))
        J(s, b)

        s, b = self.scenario("X05", "CR suivi de CRLF (ligne vide) : hors format, refus ligne-mal-formee",
                             attendu_lecteur="refus")
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_AVANT, (R, "ni-scores-ni-ouvrir"))
        l = lignes_lf(b)
        self.main_sur_journal(b, (l[0] + "\n" + l[1] + "\r\r\n" + "\n".join(l[2:]) + "\n").encode())
        self.instantane(s, b, "CR puis CRLF après l'en-tête")
        self.tenter(s, b, "pleine", T_PLEINE, (R, "ligne-mal-formee"))
        J(s, b)

        s, b = self.scenario("X06", "D-1 sur un journal en CR seul : refus à 12:00, puis pleine à 11:00 (refus sans ligne)",
                             vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_PLEINE, (R, "ni-scores-ni-ouvrir"))
        self.main_sur_journal(b, avec_fins(lignes_lf(b), ["\r"]))
        self.tenter(s, b, "pleine", T_AVANT, ("horloge-en-arriere",))
        J(s, b)

    # ---------------------------------------------------------------------------------------------- sondes d'état
    def sonde(self, nom: str, p: Path) -> None:
        ob = self.ob
        try:
            lus = ob.lire_journal(p)
            e = {"etat": "lu", "n": len(lus), "lignes": [{c: x[c] for c in CHAMPS} for x in lus]}
        except ob.RefusOuverture as x:
            e = {"etat": f"refus {x.code}", "motif": str(x)[:240]}
        except Exception as x:                                          # noqa: BLE001
            e = {"etat": f"exception {type(x).__name__}", "motif": str(x)[:240]}
        self.sondes.append({"nom": nom, "chemin": str(p), "ecrivain": e})

    def tolerance(self) -> None:
        ob = self.ob
        t = texte_du_journal((self.depot / "scenarios" / "S02" / ob.JOURNAL_OUVERTURES).read_bytes())
        l = t[:-1].split("\n")
        tete = "\n".join(ob.ENTETE_JOURNAL) + "\n"
        a, z = "a" * 64, "f" * 64
        r3 = l[2]                                                       # OUVERTURE reduite (S02, l. 3)
        etats = [
            ("journal tel qu'écrit (S02)", t.encode()),
            ("fichier vide (0 octet)", b""),
            ("fichier d'une espace", b" "),
            ("fichier d'un seul saut de ligne", b"\n"),
            ("en-tête seul", tete.encode()),
            ("en-tête seul, sans saut final", tete[:-1].encode()),
            ("ligne vide entre deux lignes", ("\n".join(l[:3] + [""] + l[3:]) + "\n").encode()),
            ("ligne vide en fin", (t + "\n").encode()),
            ("sans saut de ligne final", t[:-1].encode()),
            ("espace en tête d'une ligne", ("\n".join(l[:2] + [" " + l[2]] + l[3:]) + "\n").encode()),
            ("espace après le dernier « | »", ("\n".join(l[:2] + [l[2] + " "] + l[3:]) + "\n").encode()),
            ("séparation de table à colonnes alignées", ("\n".join(l[:1] + ["| --- | --- | --- | --- | --- | --- |"] + l[2:])
                                                         + "\n").encode()),
            ("fins de ligne CRLF", t.replace("\n", "\r\n").encode()),
            ("retour chariot seul (CR partout)", t.replace("\n", "\r").encode()),
            ("fins mêlées LF, CRLF, CR en cycle", avec_fins(l, ["\n", "\r\n", "\r"])),
            ("fins mêlées : en-tête CRLF, corps CR", avec_fins(l[:2], ["\r\n"]) + avec_fins(l[2:], ["\r"])),
            ("CR seul, sans fin de ligne finale", t.replace("\n", "\r")[:-1].encode()),
            ("CR suivi de CRLF entre deux lignes (ligne vide)", ("\n".join(l[:3]) + "\r\r\n" + "\n".join(l[3:]) + "\n").encode()),
            ("LF suivi de CR entre deux lignes (ligne vide)", ("\n".join(l[:3]) + "\n\r" + "\n".join(l[3:]) + "\n").encode()),
            ("CR au milieu d'une ligne", ("\n".join(l[:2] + [r3.replace(" | reduite | ", " |\rreduite | ")] + l[3:]) + "\n").encode()),
            ("CR final après le dernier LF", (t + "\r").encode()),
            ("marque d'ordre d'octets (BOM) en tête", b"\xef\xbb\xbf" + t.encode()),
        ]
        seules = [   # une ligne écrite à la main après l'en-tête
            ("OUVERTURE pleine-anticipee à paquets « - »", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine-anticipee | "
                                                          f"RENDEZ-VOUS-P3BIS-1={a} | - | - |"),
            ("OUVERTURE pleine à appui « - »", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | {a} {z} | - |"),
            ("OUVERTURE à motif autre que « - »", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | SCORES-T07={a} "
                                                 f"SONDES-T07={z} | {a} {z} | paquet-faux : texte |"),
            ("OUVERTURE reduite aux clés d'appui inversées", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | reduite | "
                                                            f"GARDE-ADAPTEE-T07-P3BIS={a} RENDEZ-VOUS-P3BIS-1={z} | {a} {z} | - |"),
            ("OUVERTURE pleine-anticipee, clé RENDEZ-VOUS-P3BIS-01 dans l'appui", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | "
                                                                                f"pleine-anticipee | RENDEZ-VOUS-P3BIS-01={a} | {a} {z} | - |"),
            ("OUVERTURE pleine, empreinte en majuscules", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | SCORES-T07={'A' * 64}"
                                                         f" SONDES-T07={z} | {a} {z} | - |"),
            ("OUVERTURE pleine, deux espaces entre les jetons", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | SCORES-T07={a}"
                                                               f"  SONDES-T07={z} | {a} {z} | - |"),
            ("REFUS à motif hors de la liste fermée", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | - | "
                                                     "code-inconnu : texte |"),
            ("REFUS à motif sans code", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | - | texte libre |"),
            ("REFUS à motif sans texte", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | - | deja-ouverte : |"),
            ("REFUS à motif, deux espaces après « : »", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | - | "
                                                       "deja-ouverte :  texte |"),
            ("REFUS à appui hors forme", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | texte libre | - | "
                                        "deja-ouverte : texte |"),
            ("REFUS à appui d'une seule clé connue", f"| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | SCORES-T07={a} | - | "
                                                    "ligne-absente : texte |"),
            ("REFUS à paquets d'une seule empreinte", f"| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | {a} | "
                                                     "paquet-faux : texte |"),
            ("REFUS, NUL dans le texte du motif", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | - | "
                                                 "deja-ouverte : t\x00x |"),
            ("REFUS, séparateur de ligne Unicode U+2028 dans le motif", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - "
                                                                      "| - | deja-ouverte : t x |"),
            ("tabulation en bord de cellule (clé)", "|\tREFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | - | "
                                                   "deja-ouverte : t |"),
            ("espace insécable en bord de cellule (mode)", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | - | "
                                                          "deja-ouverte : t |"),
            ("chiffres pleine chasse dans la date", "| REFUS-OUVERTURE-P3BIS | ２０２６-11-22T00:00:00Z | pleine | - "
                                                   "| - | deja-ouverte : t |"),
            ("seconde 60 (23:59:60)", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T23:59:60Z | pleine | - | - | deja-ouverte : t |"),
            ("date impossible (30 février)", "| REFUS-OUVERTURE-P3BIS | 2026-02-30T00:00:00Z | pleine | - | - | deja-ouverte : t |"),
            ("mode inconnu", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | Pleine | - | - | deja-ouverte : t |"),
            ("clé inconnue", "| OUVERTURE-P3BIS-2 | 2026-11-22T00:00:00Z | pleine | - | - | - |"),
            ("cinq cellules", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | deja-ouverte : t |"),
        ]
        etats += [(nom, (tete + ligne + "\n").encode("utf-8")) for nom, ligne in seules]
        ref = "| REFUS-OUVERTURE-P3BIS | {} | pleine | - | - | deja-ouverte : t |"
        etats += [
            ("deux lignes, dates égales", (tete + ref.format("2026-11-22T00:00:00Z") + "\n" + ref.format("2026-11-22T00:00:00Z")
                                           + "\n").encode()),
            ("deux lignes, date qui recule d'une seconde", (tete + ref.format("2026-11-22T00:00:01Z") + "\n"
                                                           + ref.format("2026-11-22T00:00:00Z") + "\n").encode()),
            ("ordre interdit : reduite après pleine (S02 + une ligne)",
             (t + f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | reduite | RENDEZ-VOUS-P3BIS-1={a} GARDE-ADAPTEE-T07-P3BIS={z} | "
                  f"{a} {z} | - |\n").encode()),
            ("ordre interdit : deux reduite", (tete + f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | reduite | RENDEZ-VOUS-P3BIS-1={a}"
                                               f" GARDE-ADAPTEE-T07-P3BIS={z} | {a} {z} | - |\n"
                                               + f"| OUVERTURE-P3BIS | 2026-11-22T00:00:01Z | reduite | RENDEZ-VOUS-P3BIS-1={a}"
                                               f" GARDE-ADAPTEE-T07-P3BIS={z} | {a} {z} | - |\n").encode()),
        ]
        for k, (nom, octets) in enumerate(etats):
            p = self.sondes_dir / f"etat-{k:02d}.md"
            p.write_bytes(octets)
            self.sonde(nom, p)
        d = self.sondes_dir / "etat-dossier.md"
        d.mkdir()
        self.sonde("dossier à la place du fichier", d)
        self.sonde("journal absent", self.sondes_dir / "etat-absent.md")

    # ---------------------------------------------------------------------------------------------- constantes
    def constantes(self) -> dict:
        ob = self.ob
        return {"entete": list(ob.ENTETE_JOURNAL), "chemin": ob.JOURNAL_OUVERTURES, "cles": [ob.CLE_OUVERTURE, ob.CLE_REFUS],
                "modes": list(ob.MODES), "date": ob.DATE.pattern, "sha": ob.SHA.pattern, "cle": ob.CLE.pattern,
                "format_date": ob.FORMAT_DATE, "prealables": ob.REGISTRE_PREALABLES, "ecrits": list(ob.CLES_ECRITS),
                "garde": ob.CLE_GARDE_ADAPTEE, "decision": ob.FICHIER_DECISION,
                "decisions": [ob.MAINTENIR, ob.OUVRIR, ob.OUVRIR_PLEINEMENT], "rdv": ob.RENDEZ_VOUS.pattern,
                "rdv_appui": ob.CLE_RDV_APPUI.pattern, "motifs_refus": list(ob.MOTIFS_REFUS), "jeton": ob.JETON_APPUI.pattern,
                "paquets": ob.PAQUETS_CELLULE.pattern, "motif": ob.MOTIF_CELLULE.pattern, "prereg_t07": ob.PREREG_T07,
                "scores_sondes": [ob.SCORES_T07, ob.SONDES_T07]}


def identite_v2_v3(v2, v3) -> dict:
    """Fonctions et constantes de module de la v3 comparées à la v2 (même bac, deux modules)."""
    import inspect
    diff_f, diff_c = [], []
    noms = sorted(set(vars(v2)) | set(vars(v3)))
    for n in noms:
        a, b = getattr(v2, n, None), getattr(v3, n, None)
        if a is b:
            continue
        if inspect.isfunction(a) or inspect.isfunction(b) or inspect.isclass(a) or inspect.isclass(b):
            try:
                if inspect.getsource(a) != inspect.getsource(b):
                    diff_f.append(n)
            except (TypeError, OSError):
                diff_f.append(n)
        elif not inspect.ismodule(a) and not n.startswith("__"):
            if repr(a) != repr(b):
                diff_c.append(n)
    return {"fonctions_differentes": diff_f, "constantes_differentes": diff_c}


def main_ecrivain(dossier: Path, module: str) -> int:
    bac = dossier / "bac-ecrivain"
    sys.path.insert(0, str(bac / "src"))
    import importlib
    import controle_ia                                                          # noqa: E402
    from controle_ia import gardes, scellement                                  # noqa: E402
    ob = importlib.import_module(f"controle_ia.premier_test_ia.ouverture_p3bis_{module}")
    autre = importlib.import_module("controle_ia.premier_test_ia.ouverture_p3bis_v2") if module == "v3" else None
    for m in (controle_ia, gardes, scellement, ob):
        if not Path(m.__file__).resolve().is_relative_to(bac.resolve()):
            raise SystemExit(f"ESSAI FAUX : {m.__name__} importé hors du bac de l'écrivain ({m.__file__})")
    if any(n.startswith("controle_ia.t07") for n in sys.modules):
        raise SystemExit("ESSAI FAUX : un module de T0.7 est chargé dans le processus de l'écrivain")
    travail = dossier / f"ecrivain-{module}"
    travail.mkdir()
    os.environ["GIT_CEILING_DIRECTORIES"] = str(dossier)
    depot = travail / "depot"
    subprocess.run(["git", "init", "-q", str(depot)], check=True)
    e = Ecrivain(travail, ob, gardes, scellement)
    for run in ("run-a", "run-b"):
        faire_paquets(depot, run, ob, scellement.sceller)
    e.jouer()
    e.tolerance()
    sortie = {"module": module, "fichier": ob.__file__, "sha256": sha_octets(Path(ob.__file__).read_bytes()),
              "constantes": e.constantes(), "scenarios": e.resultats, "sondes": e.sondes, "faux": e.faux,
              "modules_charges": sorted(n for n in sys.modules if n.startswith("controle_ia")),
              "identite_v2_v3": identite_v2_v3(autre, ob) if autre is not None else None}
    (travail / "ecrivain.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


# ================================================================================================= lecteur (processus propre)
def main_lecteur(dossier: Path, module: str) -> int:
    bac = dossier / "bac-lecteur"
    sys.path.insert(0, str(bac / "src"))
    import controle_ia                                                          # noqa: E402
    from controle_ia import gardes                                              # noqa: E402
    from controle_ia.t07 import garde_adaptee_v1 as ga, journal_p3bis_v1 as jp, registre_v1 as rg   # noqa: E402
    for m in (controle_ia, gardes, ga, jp, rg):
        if not Path(m.__file__).resolve().is_relative_to(bac.resolve()):
            raise SystemExit(f"ESSAI FAUX : {m.__name__} importé hors du bac du lecteur ({m.__file__})")
    if any(n.startswith("controle_ia.premier_test_ia") for n in sys.modules):
        raise SystemExit("ESSAI FAUX : un module de P3-bis est chargé dans le processus du lecteur")
    travail = dossier / f"ecrivain-{module}"
    entree = json.loads((travail / "ecrivain.json").read_text(encoding="utf-8"))

    def lire(chemin: Path) -> dict:
        if not Path(chemin).exists():
            return {"etat": "absent", "lignes": jp.lire_journal_p3bis(Path(chemin))}
        try:
            lues = jp.lire_journal_p3bis(Path(chemin))
        except jp.JournalFautif as e:
            return {"etat": "JournalFautif", "motif": str(e)[:400]}
        except gardes.GardeArret as e:
            return {"etat": f"GardeArret {type(e).__name__}", "motif": str(e)[:400]}
        except Exception as e:                                          # noqa: BLE001 — rapporté
            return {"etat": f"exception {type(e).__name__}", "motif": str(e)[:400]}
        ouv = jp.ouvertures(lues)
        return {"etat": "lu", "lignes": [{**{c: x[c] for c in ("numero",) + CHAMPS}, "ouverture": x in ouv,
                                          "modes": {m: x in ga._o(lues, m) for m in jp.MODES_P3BIS}} for x in lues],
                "_brutes": lues}

    def vue_t07(racine: Path, lues: list) -> dict:
        t = rg.instant_utc(T_T07)
        try:
            brutes, _ = rg.lire_registre_detail(racine / "registres/scellements-v1.md", (),
                                                (rg.SCELLEMENT_T07, rg.SCORES_T07, rg.SONDES_T07))
            lignes = rg.verifier_lignes(brutes, racine, t)
            pre = jp.lire_prealables(racine / jp.PREALABLES_P3BIS, racine, t)
            decisions = {e["numero"]: jp.lire_decision(racine, e) for e in pre["rendez_vous"]}
        except gardes.GardeArret as e:
            return {"erreur": f"{type(e).__name__} : {e}"[:400]}
        appuis = []
        for o in jp.ouvertures(lues):
            if o["mode"] == jp.REDUITE:
                m = ga.controler_reduite(o, lignes, pre, decisions)
            elif o["mode"] == jp.PLEINE:
                m = ga.controler_pleine(o, lignes)
            else:
                m = "sans objet (pleine-anticipee : nœud à toute date)"
            appuis.append([o["numero"], o["mode"], m or "appui conforme aux lignes citées"])
        codes = ga.garde_etape_b(lignes, lues, pre, decisions)
        r14 = ga.reserve_r14(lues, ga.fin_etape_a(lignes))
        return {"appuis": appuis, "codes_b": [c for c, _ in codes], "premier": ga.premier_code(codes),
                "r14": None if r14 is None else r14["ouverture_reduite"]}

    sortie = {"constantes": {"entete": list(jp.ENTETE_JOURNAL), "chemin": jp.JOURNAL_P3BIS,
                             "cles": [jp.OUVERTURE_P3BIS, jp.REFUS_OUVERTURE_P3BIS], "modes": list(jp.MODES_P3BIS),
                             "date": rg.DATE.pattern, "sha": rg.SHA.pattern, "cle": rg.CLE.pattern, "format_date": rg.FORMAT_DATE,
                             "prealables": jp.PREALABLES_P3BIS, "ecrits": list(jp.CLES_ECRITS_P3BIS),
                             "garde": jp.GARDE_ADAPTEE_T07_P3BIS, "decision": jp.FICHIER_DECISION, "decisions": list(jp.DECISIONS),
                             "rdv": jp.RENDEZ_VOUS.pattern, "rdv_appui": jp.CLE_RDV_APPUI.pattern,
                             "motifs_refus": list(jp.MOTIFS_REFUS), "jeton": jp.JETON_APPUI.pattern,
                             "paquets": jp.PAQUETS_CELLULE.pattern, "motif": jp.MOTIF_CELLULE.pattern, "prereg_t07": jp.PREREG_T07,
                             "scores_sondes": [rg.SCORES_T07, rg.SONDES_T07]},
              "scenarios": {}, "sondes": {}, "modules_charges": None}
    for s in entree["scenarios"]:
        r = lire(Path(s["journal"]))
        brutes = r.pop("_brutes", None)
        if s["vue_t07"] and brutes is not None:
            r["vue"] = vue_t07(Path(s["racine"]), brutes)
        sortie["scenarios"][s["id"]] = r
    for x in entree["sondes"]:
        r = lire(Path(x["chemin"]))
        r.pop("_brutes", None)
        sortie["sondes"][x["nom"]] = r
    sortie["modules_charges"] = sorted(n for n in sys.modules if n.startswith("controle_ia"))
    (travail / "lecteur.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


# ================================================================================================= principal
def court(cellule: str) -> str:
    return " ".join(m[:8] if len(m) == 64 else (m.split("=")[0] + "=" + m.split("=")[1][:8] if "=" in m else m)
                    for m in cellule.split(" "))


def verdict_ecrivain(e: dict) -> str:
    return "lu" if e["etat"] == "lu" else ("absent" if e["etat"] == "absent" else "refusé")


def imprimer_module(module: str, ecr: dict, lec: dict, faux: list, bilan: dict) -> None:
    print(f"\n=================== ÉCRIVAIN ouverture_p3bis_{module} ({ecr['sha256'][:12]}…) -> LECTEUR journal_p3bis_v1 "
          f"(C7 {COMMIT_LECTEUR[:8]}) ===================")
    print(f"modules chargés, processus de l'écrivain : {', '.join(ecr['modules_charges'])}")
    print(f"modules chargés, processus du lecteur : {', '.join(lec['modules_charges'])}")
    if ecr.get("identite_v2_v3"):
        i = ecr["identite_v2_v3"]
        print(f"v3 contre v2 (même bac) : fonctions ou classes différentes : {i['fonctions_differentes'] or 'aucune'} ; constantes "
              f"de module différentes : {i['constantes_differentes'] or 'aucune'}")
    print("CONSTANTES (écrivain | lecteur) :")
    for k, v in ecr["constantes"].items():
        w = lec["constantes"][k]
        egal = v == w
        print(f"  {k} : {'égales' if egal else 'DIFFÉRENTES'}" + ("" if egal else f" : {v!r} | {w!r}"))
        if not egal:
            bilan["constantes"].append(k)
    for s in ecr["scenarios"]:
        r = lec["scenarios"][s["id"]]
        o = oracle(Path(s["journal"]))
        print(f"\n[{s['id']}] {s['titre']}")
        for t in s["tentatives"]:
            i = t["issue"]
            att = "" if t["attendu"] is not None else f" [exploratoire ; le texte prévoit : {t['attendu_texte']}]"
            print(f"  tentative {t['mode']} @{t['instant']} -> écrivain : {i[0]}" + (f" {i[1]}" if i[1] else "")
                  + f" (code {i[2]}) ; lignes écrites : {len(t['neuves'])}{att}"
                  + (f"\n      motif : {i[3]}" if i[0] in ("horloge-en-arriere", "journal-impossible", "arret", "exception") else ""))
            for n, brute, ecr_l in t["neuves"]:
                c = [x.strip() for x in brute[1:-1].split("|")]
                print(f"    l.{n} | {c[0]} | {c[1]} | {c[2]} | {court(c[3])} | {court(c[4])} | {c[5].split(' : ')[0]} |")
                if "faute_ecrivain" in ecr_l:
                    verdict, motif = "ESSAI FAUX", f"l'écrivain ne relit pas sa propre ligne : {ecr_l['faute_ecrivain']}"
                    faux.append(f"{module} {s['id']} l.{n} : {motif}")
                elif r["etat"] != "lu":
                    verdict, motif = "refusée", f"{r['etat']} : {r.get('motif', '')}"
                else:
                    lu = next((x for x in r["lignes"] if x["numero"] == n), None)
                    if lu is None:
                        verdict, motif = "mal interprétée", "ligne absente des lignes rendues"
                    else:
                        ecarts = [k for k in CHAMPS if lu[k] != ecr_l[k]]
                        sens = {m: (ecr_l["cle"] == "OUVERTURE-P3BIS" and ecr_l["mode"] == m) for m in MODES}
                        if ecarts:
                            verdict, motif = "mal interprétée", f"champs {ecarts}"
                        elif lu["ouverture"] != (ecr_l["cle"] == "OUVERTURE-P3BIS") or lu["modes"] != sens:
                            verdict, motif = "mal interprétée", f"sens : ouverture {lu['ouverture']}, modes {lu['modes']}"
                        else:
                            verdict = "lue telle quelle"
                            motif = f"ouverture {lu['mode']}" if lu["ouverture"] else "jamais une ouverture"
                print(f"        lecteur T0.7 : {verdict} ({motif[:300]})")
                bilan["lignes"][verdict] = bilan["lignes"].get(verdict, 0) + 1
                if verdict != "lue telle quelle" and not (verdict == "refusée" and s["attendu_lecteur"] == "refus"):
                    bilan["discordances"].append(f"{module} {s['id']} l.{n} : {verdict}")
                if verdict == "refusée" and s["attendu_lecteur"] == "refus":
                    bilan["refus_attendus"].append(f"{module} {s['id']} l.{n}")
        if not any(t["neuves"] for t in s["tentatives"]):
            print(f"    aucune ligne écrite ; lecteur T0.7 sur le journal : "
                  + ({"absent": "absent -> aucune ouverture", "lu": f"{len(r.get('lignes', []))} ligne(s) lue(s)"}
                     .get(r["etat"], f"{r['etat']} : {r.get('motif', '')[:200]}")))
        print(f"    écrivain relisant le journal final : {s['ecrivain_relit']}")
        lecteur_final = "absent" if r["etat"] == "absent" else ("lu" if r["etat"] == "lu" else "refusé")
        ecrivain_final = ("absent" if not s["journal_present"] and s["ecrivain_relit"].startswith("0 ligne")
                          else "lu" if "aucun refus" in s["ecrivain_relit"] else "refusé")
        oracle_final = {"absent": "absent", "au format": "lu", "hors format": "refusé"}[o["etat"]]
        print(f"    journal final : oracle du texte {o['etat']}" + (f" ({'; '.join(o['fautes'])[:200]})" if o["fautes"] else "")
              + f" ; écrivain {ecrivain_final} ; lecteur {lecteur_final} ({r['etat']})")
        if len({ecrivain_final, lecteur_final, oracle_final}) > 1:
            bilan["journaux_desaccord"].append(f"{module} {s['id']} : oracle {oracle_final}, écrivain {ecrivain_final}, lecteur "
                                                f"{lecteur_final} ({r['etat']})")
        if r["etat"] not in ("lu", "absent", "JournalFautif"):
            bilan["traitement"].append(f"{module} {s['id']} (journal final) : écrivain {s['ecrivain_relit']} ; lecteur {r['etat']} "
                                       f"(pas JournalFautif)")
        if ecrivain_final == lecteur_final == oracle_final == "lu" and r["etat"] == "lu":
            lo = [{k: y[k] for k in CHAMPS} for y in o["lignes"]]
            ll = [{k: y[k] for k in CHAMPS} for y in r["lignes"]]
            if lo != ll:
                bilan["journaux_desaccord"].append(f"{module} {s['id']} : lignes de l'oracle ≠ lignes du lecteur")
        if "vue" in r:
            v = r["vue"]
            if "erreur" in v:
                print(f"    vue de T0.7 : erreur {v['erreur'][:240]}")
            else:
                for n, mode, m in v["appuis"]:
                    print(f"    vue de T0.7 : l.{n} ({mode}) : {m[:200]}")
                print(f"    vue de T0.7 : garde de l'étape B (sans VERDICT-P3BIS) : codes {v['codes_b'] or 'aucun'} "
                      f"(premier : {v['premier']}) ; R14 : {v['r14'] or 'absente'}")
    print(f"\nSONDES D'ÉTAT ({module}) : état | oracle du texte | écrivain (lire_journal) | lecteur (lire_journal_p3bis) | lignes")
    for x in ecr["sondes"]:
        r = lec["sondes"][x["nom"]]
        o = oracle(Path(x["chemin"]))
        e = x["ecrivain"]
        vo = {"absent": "absent", "au format": "lu", "hors format": "refusé"}[o["etat"]]
        ve = "absent" if (vo == "absent" and e["etat"] == "lu" and e["n"] == 0) else verdict_ecrivain(e)
        vl = "absent" if r["etat"] == "absent" else ("lu" if r["etat"] == "lu" else "refusé")
        egales = ""
        if ve == vl == "lu":
            le = [{k: y[k] for k in CHAMPS} for y in e["lignes"]]
            ll = [{k: y[k] for k in CHAMPS} for y in r["lignes"]]
            egales = "lignes égales" if le == ll else "LIGNES DIFFÉRENTES"
            if le != ll:
                bilan["sondes_desaccord"].append(f"{module} {x['nom']} : lignes lues différentes")
            if vo == "lu":
                lo = [{k: y[k] for k in CHAMPS} for y in o["lignes"]]
                if lo != le:
                    egales += " ; oracle : LIGNES DIFFÉRENTES"
        texte_o = o["etat"] + (f" [{'; '.join(o['fautes'])[:90]}]" if o["fautes"] else f" [{len(o['lignes'])} ligne(s)]")
        texte_e = e["etat"] + (f" [{e['n']} ligne(s)]" if e["etat"] == "lu" else "")
        texte_l = r["etat"] + (f" [{len(r['lignes'])} ligne(s)]" if r["etat"] == "lu" else "")
        print(f"  {x['nom']} | {texte_o} | {texte_e} | {texte_l} | {egales}")
        if ve != vl:
            bilan["sondes_desaccord"].append(f"{module} {x['nom']} : écrivain {ve} ({e['etat']}), lecteur {vl} ({r['etat']})")
        elif r["etat"] not in ("lu", "absent", "JournalFautif"):
            bilan["traitement"].append(f"{module} {x['nom']} : écrivain {e['etat']} ; lecteur {r['etat']} (pas JournalFautif)")
        if vo != ve or vo != vl:
            bilan["texte_contre_codes"].append(f"{module} {x['nom']} : oracle {vo}, écrivain {ve}, lecteur {vl}")


MUTATIONS_TEMOIN = (   # lecteur faussé à dessein (témoin R5) : ligne vide ignorée (tolérance du brouillon 19) ; refus pris pour ouverture
    ("        if \"\\r\" in brute or not (len(brute) >= 2",
     "        if brute == \"\":\n            continue\n        if \"\\r\" in brute or not (len(brute) >= 2"),
    ("    return [l for l in journal if l[\"cle\"] == OUVERTURE_P3BIS]", "    return list(journal)"),
)


def muter_lecteur(dossier: Path) -> list:
    p = dossier / "bac-lecteur" / "src/controle_ia/t07/journal_p3bis_v1.py"
    texte = p.read_text(encoding="utf-8")
    for avant, apres in MUTATIONS_TEMOIN:
        if texte.count(avant) != 1:
            raise SystemExit(f"ESSAI FAUX : mutation du témoin introuvable ou non unique : {avant!r}")
        texte = texte.replace(avant, apres)
    p.write_text(texte, encoding="utf-8")
    return [f"lecteur muté (témoin) : {p.name} -> {sha_octets(p.read_bytes())}"]


def main_principal(dossier: Path, clone: Path, temoin: bool = False) -> int:
    debut = date_u()
    if dossier.exists():
        raise SystemExit(f"{dossier} existe déjà : un dossier neuf est exigé")
    dossier.mkdir(parents=True)
    extraire_src(clone, COMMIT_ECRIVAIN, dossier / "bac-ecrivain")
    extraire_src(clone, COMMIT_LECTEUR, dossier / "bac-lecteur")
    lignes, faux = verifier_bacs(clone, dossier)
    if temoin and not faux:
        lignes += muter_lecteur(dossier)
    py = subprocess.run([sys.executable, "-I", "-c", "import sys, numpy; print(sys.version.split()[0], numpy.__version__)"],
                        capture_output=True, text=True).stdout.strip()
    gitv = subprocess.run(["git", "--version"], capture_output=True, text=True).stdout.strip()
    print(f"ESSAI DE CONCORDANCE DU JOURNAL P3-BIS -> T0.7, v2 (préalable P-9) ; début {debut} (date -u)"
          + (" ; PASSAGE TÉMOIN : LECTEUR MUTÉ À DESSEIN" if temoin else ""))
    print(f"interpréteur {sys.executable} -I (Python et numpy : {py}) ; {gitv}")
    print(f"écrivain : commit {COMMIT_ECRIVAIN} ; lecteur : commit {COMMIT_LECTEUR} (C7, ligne CODE-T07)")
    print("\nEMPREINTES (fichier extrait par git archive | tar -x ; git show au commit ; compagnon au commit) :")
    for l in lignes:
        print(f"  {l}")
    if faux:
        print("ESSAI FAUX : " + " ; ".join(faux))
        return 1
    bilan = {"lignes": {}, "discordances": [], "refus_attendus": [], "journaux_desaccord": [], "sondes_desaccord": [],
             "texte_contre_codes": [], "traitement": [], "constantes": []}
    for module in (MODULES_ECRIVAIN[:1] if temoin else MODULES_ECRIVAIN):
        for role in ("ecrivain", "lecteur"):
            r = subprocess.run([sys.executable, "-I", str(Path(__file__).resolve()), role, str(dossier), "--module", module],
                               capture_output=True, text=True, cwd=str(dossier))
            if r.returncode != 0:
                print(f"ESSAI FAUX : processus {role} ({module}) : code {r.returncode}\n{r.stdout[-2000:]}\n{r.stderr[-4000:]}")
                return 1
        ecr = json.loads((dossier / f"ecrivain-{module}" / "ecrivain.json").read_text(encoding="utf-8"))
        lec = json.loads((dossier / f"ecrivain-{module}" / "lecteur.json").read_text(encoding="utf-8"))
        faux += [f"{module} : {f}" for f in ecr["faux"]]
        imprimer_module(module, ecr, lec, faux, bilan)
    print("\n=================== BILAN ===================")
    print("LIGNES ÉCRITES ET LUES (modules de l'écrivain joués : "
          + ", ".join(MODULES_ECRIVAIN[:1] if temoin else MODULES_ECRIVAIN) + ") : "
          + " ; ".join(f"{k} : {v}" for k, v in sorted(bilan["lignes"].items())))
    print("REFUS DU LECTEUR ATTENDUS PAR LES DEUX TEXTES (journal hors format) : " + (", ".join(bilan["refus_attendus"]) or "aucun"))
    print("LIGNES REFUSÉES OU MAL INTERPRÉTÉES NON ATTENDUES (discordances de lecture) : "
          + ("; ".join(bilan["discordances"]) or "aucune"))
    print("JOURNAUX FINAUX OÙ ORACLE, ÉCRIVAIN ET LECTEUR DIVERGENT : " + ("; ".join(bilan["journaux_desaccord"]) or "aucun"))
    print("SONDES OÙ ÉCRIVAIN ET LECTEUR DIVERGENT (acceptation ou lignes) : " + ("; ".join(bilan["sondes_desaccord"]) or "aucune"))
    print("SONDES OÙ L'ORACLE DU TEXTE DIFFÈRE D'UN DES CODES : " + ("; ".join(bilan["texte_contre_codes"]) or "aucune"))
    print("SONDES OÙ LE LECTEUR REFUSE AUTREMENT QUE PAR JournalFautif : " + ("; ".join(bilan["traitement"]) or "aucune"))
    print("CONSTANTES DIFFÉRENTES : " + (", ".join(bilan["constantes"]) or "aucune"))
    fin = date_u()
    if temoin:
        vu = bool(bilan["discordances"]) and bool(bilan["sondes_desaccord"])
        print(f"TÉMOIN (lecteur muté) : {len(bilan['discordances'])} discordance(s) de lecture et {len(bilan['sondes_desaccord'])} "
              f"désaccord(s) de sondes relevés -> {'DÉTECTÉ' if vu else 'NON DÉTECTÉ (essai insensible)'}")
        print(f"fin {fin} (date -u)")
        return 0 if vu else 1
    if faux:
        print("ESSAI FAUX : " + " ; ".join(faux))
        print(f"fin {fin} (date -u)")
        return 1
    print("ESSAI : empreintes conformes ; chaque tentative non exploratoire a donné l'issue visée (chaque type de ligne exercé)")
    print(f"fin {fin} (date -u)")
    return 0


def main(argv) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("role", choices=("principal", "ecrivain", "lecteur"))
    ap.add_argument("dossier")
    ap.add_argument("--clone", default="/home/user/controle-ia-travail")
    ap.add_argument("--module", choices=MODULES_ECRIVAIN, default="v3")
    ap.add_argument("--temoin", action="store_true", help="principal : lecteur muté à dessein, l'essai doit le détecter (R5)")
    a = ap.parse_args(argv)
    dossier = Path(a.dossier).absolute()
    if a.role == "principal":
        return main_principal(dossier, Path(a.clone), a.temoin)
    if a.role == "ecrivain":
        return main_ecrivain(dossier, a.module)
    return main_lecteur(dossier, a.module)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
