#!/usr/bin/env python3
"""Essai de concordance du journal des ouvertures de P3-bis (écrivain) avec le lecteur de T0.7, v1.

Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-concordance-journal-p3bis-t07-v1.md`
(`042ba58a…`), mandat, points 1 à 3. Écrit le 2026-11-10 (heure relevée par `date -u` : 07:56 UTC) par un agent neuf, qui n'a
écrit ni le code de P3-bis, ni celui de T0.7, ni leurs textes.

    /home/user/controle-ia-travail/.venv/bin/python -I essai_concordance_journal_v1.py DOSSIER_NEUF [--clone CLONE]

1. Copie, par `git -C CLONE show <commit>:<chemin>`, l'écrivain (`premier_test_ia/ouverture_p3bis_v2.py` au commit `02217f1c`)
   et le lecteur (`t07/journal_p3bis_v1.py` au commit `8dc1cb09`, avec ce qu'il importe, `t07/registre_v1.py`, et son usager
   `t07/garde_adaptee_v1.py`, qui compare l'appui des lignes `reduite` et `pleine` aux lignes citées) sous `DOSSIER_NEUF/src/`,
   chaque fichier vérifié par son empreinte ; les fichiers communs (`controle_ia/__init__.py`, `gardes.py`) sont égaux aux deux
   commits (vérifié). `DOSSIER_NEUF` ne doit pas exister.
2. Dépôt git jetable `DOSSIER_NEUF/depot` (`GIT_CEILING_DIRECTORIES` = `DOSSIER_NEUF`) : deux jeux de paquets jouets (runs
   `run-a`, `run-b`) faits par les fonctions mêmes de l'écrivain (`fermer_run`, `paquet_lectures`, `sceller`), puis un banc par
   scénario (`depot/scenarios/<id>/` : registre des préalables, registre des scellements, décisions, fichiers cités scellés).
3. Chaque scénario fait **écrire** par `ouverture_p3bis_v2.ouvrir` (paramètre `instant` des essais, CP-08) une ou plusieurs
   lignes du journal `registres/ouvertures-p3bis-v1.md` ; le journal est ensuite **lu** par `journal_p3bis_v1.lire_journal_p3bis`.
   Pour chaque ligne écrite : lue telle quelle (mêmes clé, date, instant, mode, appui, paquets, motif que l'écrivain y lit, et
   même sens : ouverture du même mode, ou jamais une ouverture), refusée (motif du lecteur), ou mal interprétée (champ ou sens
   différent). Pour les scénarios à ouvertures : vue de T0.7 (appui comparé aux lignes citées par `garde_adaptee_v1`,
   codes de la garde de l'étape B sans `VERDICT-P3BIS`, réserve R14).
4. Sondes de tolérance : états du fichier du journal que l'écrivain n'écrit pas lui-même (vide, ligne vide, CRLF, …), lus par
   les deux modules.

N'écrit que sous `DOSSIER_NEUF` et ne l'efface pas (l'appelant l'efface par son chemin exact). Aucun appel externe.
Code de sortie : 0 si chaque tentative a donné à l'écrivain l'issue que le scénario vise (l'essai a bien exercé chaque type de
ligne), 1 sinon (essai faux). Les discordances observées ne changent pas le code : elles sont imprimées.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys
import tarfile
from pathlib import Path

COMMIT_ECRIVAIN = "02217f1cf5255ef87c42285fc579d38c5a6ff003"
COMMIT_LECTEUR = "8dc1cb09f5e764f37aa87cf1410bc6586249b3d1"
COPIES = (
    (COMMIT_ECRIVAIN, "src/controle_ia/__init__.py", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    (COMMIT_ECRIVAIN, "src/controle_ia/gardes.py", "a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439"),
    (COMMIT_ECRIVAIN, "src/controle_ia/scellement.py", "93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2"),
    (COMMIT_ECRIVAIN, "src/controle_ia/premier_test_ia/__init__.py",
     "c72da1602f1998e4c7b30b670e89143d6a9c6337b903164f4bc6eed5ab9a5f92"),
    (COMMIT_ECRIVAIN, "src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py",
     "330915f67402e097c2581fee0de2ed6950954f2c071356df19b27980bb5f5bb3"),
    (COMMIT_LECTEUR, "src/controle_ia/t07/__init__.py", "553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e"),
    (COMMIT_LECTEUR, "src/controle_ia/t07/registre_v1.py", "914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0"),
    (COMMIT_LECTEUR, "src/controle_ia/t07/journal_p3bis_v1.py",
     "389f68080545956c108631233e5ae89d88d7061bf493bb65d32144d47aa191a4"),
    (COMMIT_LECTEUR, "src/controle_ia/t07/garde_adaptee_v1.py",
     "7ff571d7b1f06db94043545bfe178a066613ddd734aacca1cf3ef52ba0b511de"),
)
COMMUNS = ("src/controle_ia/__init__.py", "src/controle_ia/gardes.py")   # importés des deux côtés : égaux aux deux commits

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


# ================================================================================================= copie et import
def copier(clone: Path, dossier: Path) -> None:
    for commit, chemin, attendu in COPIES:
        octets = subprocess.run(["git", "-C", str(clone), "show", f"{commit}:{chemin}"], capture_output=True, check=True).stdout
        sha = hashlib.sha256(octets).hexdigest()
        if sha != attendu:
            raise SystemExit(f"ESSAI FAUX : {chemin} au commit {commit[:8]} d'empreinte {sha}, {attendu} attendu")
        cible = dossier / chemin
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_bytes(octets)
    for chemin in COMMUNS:
        a = subprocess.run(["git", "-C", str(clone), "show", f"{COMMIT_ECRIVAIN}:{chemin}"], capture_output=True, check=True).stdout
        b = subprocess.run(["git", "-C", str(clone), "show", f"{COMMIT_LECTEUR}:{chemin}"], capture_output=True, check=True).stdout
        if a != b:
            raise SystemExit(f"ESSAI FAUX : {chemin} diffère entre les deux commits ; deux arbres séparés seraient nécessaires")


def importer(dossier: Path):
    sys.path.insert(0, str(dossier / "src"))
    import controle_ia                                                          # noqa: E402
    if not Path(controle_ia.__file__).resolve().is_relative_to(dossier.resolve()):
        raise SystemExit(f"ESSAI FAUX : controle_ia importé depuis {controle_ia.__file__}, hors de {dossier}")
    from controle_ia import gardes, scellement
    from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob
    from controle_ia.t07 import garde_adaptee_v1 as ga, journal_p3bis_v1 as jp, registre_v1 as rg
    for m in (gardes, scellement, ob, ga, jp, rg):
        if not Path(m.__file__).resolve().is_relative_to(dossier.resolve()):
            raise SystemExit(f"ESSAI FAUX : {m.__name__} importé hors de {dossier}")
    return gardes, scellement, ob, ga, jp, rg


# ================================================================================================= banc
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


def l_rdv(b: Banc, n: int, mot: str | None, date_dec: str | None, date_ligne: str) -> str:
    rel = f"docs/decisions/rendez-vous-P3-bis-v{n}.md"
    texte = f"# Rendez-vous de P3-bis, décision {n} (banc)\n\n"
    if mot is not None:
        texte += f"Décision : {mot}\n"
    if date_dec is not None:
        texte += f"Date : {date_dec}\n"
    return L(f"RENDEZ-VOUS-P3BIS-{n}", date_ligne, rel, b.scelle(rel, texte))


def l_scores(b: Banc, date: str) -> list:
    return [L("SCORES-T07", date, "donnees/r7b/scores-actions-t07.npz", b.scelle("donnees/r7b/scores-actions-t07.npz", "scores\n")),
            L("SONDES-T07", date, "diag/r7b/sondes-t07.json", b.scelle("diag/r7b/sondes-t07.json", "{}\n"))]


def monter(b: Banc, *, ecrits=True, scel=True, scel_date=D_SCEL, scel_rel=PREREG_T07, garde=D_GARDE, garde_cite=None,
           rdv=(), scores=None, retouche=None) -> None:
    """Registre des préalables et registre des scellements du banc. `rdv` : [(décision, date de la décision, date de la ligne)].
    `garde_cite` : (chemin, contenu) d'un autre texte cité par la garde adaptée. `retouche(b, lignes)` : lignes du registre des
    préalables modifiées pour un artefact."""
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


# ================================================================================================= paquets jouets
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


# ================================================================================================= essai
def lignes_de(texte):
    if texte is None or texte == "<dossier>":
        return []
    l = texte.split("\n")
    return l[:-1] if l and l[-1] == "" else l


def court(cellule: str) -> str:
    """Cellule abrégée pour l'impression : empreintes à 8 caractères, motif à son code."""
    return " ".join(m[:8] if len(m) == 64 else (m.split("=")[0] + "=" + m.split("=")[1][:8] if "=" in m else m)
                    for m in cellule.split(" "))


class Essai:
    def __init__(self, dossier: Path, mods):
        self.gardes, self.scellement, self.ob, self.ga, self.jp, self.rg = mods
        self.depot = dossier / "depot"
        self.faux, self.resultats, self.sondes = [], [], []

    # ---------------------------------------------------------------------------------------------- écrivain
    def etat(self, b: Banc):
        p = b.r / self.ob.JOURNAL_OUVERTURES
        if p.is_dir():
            return "<dossier>"
        return p.read_text(encoding="utf-8") if p.exists() else None

    def tenter(self, s: dict, b: Banc, mode: str, instant: str, attendu: tuple, run: str = "run-a", sortie: Path | None = None,
               panne_extraction: bool = False, n_lignes: int | None = None) -> None:
        ob, G = self.ob, self.gardes.GardeArret
        avant = self.etat(b)
        sortie = b.sortie() if sortie is None else sortie
        imprime = []
        extraire = ob.extraire
        if panne_extraction:
            def _panne(fichiers, sortie_):
                raise OSError("panne d'écriture simulée par l'essai")
            ob.extraire = _panne
        try:
            ob.ouvrir(b.r, mode, run, sortie, racine_paquets=self.depot, date_paquet=D_PAQUET,
                      instant=ob.instant_utc(instant), imprimer=imprime.append)
            issue = ("ouverture", mode, 0)
        except ob.RefusOuverture as e:
            issue = ("refus", e.code, 2)
        except ob.JournalImpossible:
            issue = ("journal-impossible", None, 2)
        except G as e:
            issue = ("arret", str(e)[:70], 1)
        finally:
            ob.extraire = extraire
        apres = self.etat(b)
        la, lp = lignes_de(avant), lignes_de(apres)
        if lp[:len(la)] != la:
            self.faux.append(f"{s['id']} : le journal n'est pas en ajout seul")
        neuves = [(n, x) for n, x in enumerate(lp, start=1)
                  if n > len(la) and not (n <= 2 and x == ob.ENTETE_JOURNAL[n - 1])]
        if attendu[0] in ("ouverture", "refus"):
            vise = issue[0] == attendu[0] and issue[1] == attendu[1]
        else:
            vise = issue[0] == attendu[0]
        if n_lignes is None:
            n_lignes = 1 if attendu[0] in ("ouverture", "refus") else 0
        if not vise or len(neuves) != n_lignes:
            self.faux.append(f"{s['id']} : tentative {mode} @{instant} : issue {issue} et {len(neuves)} ligne(s), {attendu} et "
                             f"{n_lignes} ligne(s) visées")
        s["tentatives"].append({"mode": mode, "instant": instant, "issue": issue, "neuves": neuves})

    # ---------------------------------------------------------------------------------------------- lecteur
    def lire(self, chemin: Path):
        try:
            return self.jp.lire_journal_p3bis(chemin), None
        except self.gardes.GardeArret as e:
            return None, f"{type(e).__name__} : {e}"

    def juger(self, s: dict, b: Banc) -> None:
        """Chaque ligne écrite, lue par T0.7 : telle quelle, refusée, ou mal interprétée."""
        ob, jp, ga = self.ob, self.jp, self.ga
        chemin = b.r / ob.JOURNAL_OUVERTURES
        lues, faute = self.lire(chemin)
        s["lecteur"] = {"faute": faute, "n": None if lues is None else len(lues)}
        try:
            s["ecrivain_relit"] = f"{len(ob.lire_journal(chemin))} ligne(s), aucun refus"
        except ob.RefusOuverture as e:
            s["ecrivain_relit"] = f"refus {e.code}"
        for t in s["tentatives"]:
            t["jugements"] = []
            for n, brute in t["neuves"]:
                ecr = ob.lire_ligne_journal(brute)
                if faute is not None:
                    t["jugements"].append((n, brute, "refusée", faute))
                    continue
                lu = next((x for x in lues if x["numero"] == n), None)
                if lu is None:
                    t["jugements"].append((n, brute, "mal interprétée", "ligne absente des lignes rendues"))
                    continue
                ecarts = [c for c in CHAMPS if lu[c] != ecr[c]]
                ouverte = lu in jp.ouvertures(lues)
                par_mode = {m: lu in ga._o(lues, m) for m in jp.MODES_P3BIS}
                sens_attendu = {m: (ecr["cle"] == ob.CLE_OUVERTURE and ecr["mode"] == m) for m in jp.MODES_P3BIS}
                if ecarts:
                    t["jugements"].append((n, brute, "mal interprétée", f"champs {ecarts}"))
                elif ouverte != (ecr["cle"] == ob.CLE_OUVERTURE) or par_mode != sens_attendu:
                    t["jugements"].append((n, brute, "mal interprétée", f"sens : ouverture {ouverte}, modes {par_mode}"))
                else:
                    sens = f"ouverture {lu['mode']}" if ouverte else "jamais une ouverture"
                    t["jugements"].append((n, brute, "lue telle quelle", sens))
        if s.get("vue_t07") and lues is not None:
            s["vue"] = self.vue_t07(b, lues)

    def vue_t07(self, b: Banc, lues: list) -> dict:
        """Ce que T0.7 fait des ouvertures lues : appui comparé aux lignes citées, garde de l'étape B (sans VERDICT-P3BIS), R14."""
        rg, jp, ga = self.rg, self.jp, self.ga
        t = rg.instant_utc(T_T07)
        try:
            brutes, _ = rg.lire_registre_detail(b.r / "registres/scellements-v1.md", (),
                                                (rg.SCELLEMENT_T07, rg.SCORES_T07, rg.SONDES_T07))
            lignes = rg.verifier_lignes(brutes, b.r, t)
            pre = jp.lire_prealables(b.r / jp.PREALABLES_P3BIS, b.r, t)
            decisions = {e["numero"]: jp.lire_decision(b.r, e) for e in pre["rendez_vous"]}
        except self.gardes.GardeArret as e:
            return {"erreur": f"{type(e).__name__} : {e}"}
        appuis = []
        for o in jp.ouvertures(lues):
            if o["mode"] == jp.REDUITE:
                m = ga.controler_reduite(o, lignes, pre, decisions)
            elif o["mode"] == jp.PLEINE:
                m = ga.controler_pleine(o, lignes)
            else:
                m = "sans objet (pleine-anticipee : nœud à toute date)"
            appuis.append((o["numero"], o["mode"], m or "appui conforme aux lignes citées"))
        codes = ga.garde_etape_b(lignes, lues, pre, decisions)
        r14 = ga.reserve_r14(lues, ga.fin_etape_a(lignes))
        return {"appuis": appuis, "codes_b": [c for c, _ in codes], "r14": None if r14 is None else r14["ouverture_reduite"]}

    # ---------------------------------------------------------------------------------------------- scénarios
    def scenario(self, ident: str, titre: str, attendu_lecteur: str = "lu", vue_t07: bool = False) -> tuple[dict, Banc]:
        racine = self.depot / "scenarios" / ident
        b = Banc(racine, self.scellement.sceller)
        s = {"id": ident, "titre": titre, "tentatives": [], "attendu_lecteur": attendu_lecteur, "vue_t07": vue_t07}
        self.resultats.append(s)
        return s, b

    def jouer(self) -> None:
        ob = self.ob
        O, R = "ouverture", "refus"

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
        self.juger(s, b)

        s, b = self.scenario("S02", "branche 1 : reduite sous « ouvrir », pleine-anticipee refusée, complément pleine",
                             vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        self.tenter(s, b, "pleine-anticipee", T_ENTRE, (R, "ni-scores-ni-ouvrir"))
        self.tenter(s, b, "pleine", T_SOIR, (R, "ligne-absente"))              # E-3 : pleine sous « ouvrir » sans lignes de T0.7
        b.ajouter("registres/scellements-v1.md", l_scores(b, D_SCORES))
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        self.juger(s, b)

        s, b = self.scenario("S03", "branche 2 : pleine-anticipee sous « ouvrir pleinement »", vue_t07=True)
        monter(b, rdv=[("ouvrir pleinement", D_DEC1, D_RDV1)])
        self.tenter(s, b, "pleine-anticipee", T_ANTICIPEE, (O, "pleine-anticipee"))
        self.juger(s, b)

        s, b = self.scenario("S04", "E-9 : « ouvrir », reduite, « ouvrir pleinement », complément pleine-anticipee", vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        b.ajouter("registres/prealables-p3bis-v1.md", [l_rdv(b, 2, "ouvrir pleinement", D_DEC2, D_RDV2)])
        self.tenter(s, b, "pleine-anticipee", T_ANTICIPEE, (O, "pleine-anticipee"))
        self.juger(s, b)

        s, b = self.scenario("S05", "E-8 : reduite sous « ouvrir » après SCORES-T07 et SONDES-T07, puis pleine", vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)], scores=D_SCORES_TOT)
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        self.tenter(s, b, "pleine", T_ANTICIPEE, (O, "pleine"))
        self.juger(s, b)

        s, b = self.scenario("S06a", "E-8 : pleine-anticipee sous « ouvrir pleinement » avec SCORES-T07 et SONDES-T07 inscrites",
                             vue_t07=True)
        monter(b, rdv=[("ouvrir pleinement", D_DEC1, D_RDV1)], scores=D_SCORES_TOT)
        self.tenter(s, b, "pleine-anticipee", T_ANTICIPEE, (O, "pleine-anticipee"))
        self.juger(s, b)

        s, b = self.scenario("S06b", "même banc que S06a, mode pleine demandé (chemin normal, rendez-vous sans objet)", vue_t07=True)
        monter(b, rdv=[("ouvrir pleinement", D_DEC1, D_RDV1)], scores=D_SCORES_TOT)
        self.tenter(s, b, "pleine", T_ANTICIPEE, (O, "pleine"))
        self.juger(s, b)

        s, b = self.scenario("S07", "E-9 ajout : reduite (run-a), complément pleine sur d'autres paquets (run-b), puis run-a",
                             vue_t07=True)
        monter(b, rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        b.ajouter("registres/scellements-v1.md", l_scores(b, D_SCORES))
        self.tenter(s, b, "pleine", T_PLEINE, (R, "paquet-faux"), run="run-b")
        self.tenter(s, b, "pleine", T_APRES, (O, "pleine"))
        self.juger(s, b)

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
            self.juger(s, b)

        s, b = self.scenario("R04b", "journal hors format (ligne à cinq cellules écrite à la main) : refus ligne-mal-formee, "
                                     "ligne neuve qui suit", attendu_lecteur="refus")
        monter(b, scores=D_SCORES)
        (b.r / ob.JOURNAL_OUVERTURES).write_text("\n".join(ob.ENTETE_JOURNAL) + "\n| OUVERTURE-P3BIS | 2026-11-20T13:00:00Z | "
                                                 "pleine | - | - |\n", encoding="utf-8")
        self.tenter(s, b, "pleine", T_PLEINE, (R, "ligne-mal-formee"))
        self.juger(s, b)

        # ---- lignes sans journal (E-3 (b) et (c)) ----
        s, b = self.scenario("N01", "journal impossible à écrire : dossier registres/ absent (refus sans ligne)")
        racine = b.r
        os.rmdir(racine / "registres")
        self.tenter(s, b, "pleine", T_PLEINE, ("journal-impossible",))
        self.juger(s, b)

        s, b = self.scenario("N02", "journal impossible à écrire : chemin du journal occupé par un dossier")
        monter(b, scores=D_SCORES)
        (b.r / ob.JOURNAL_OUVERTURES).mkdir()
        self.tenter(s, b, "pleine", T_PLEINE, ("journal-impossible",))
        self.juger(s, b)

        s, b = self.scenario("N04", "extraction en échec après la ligne OUVERTURE-P3BIS (code 1, la ligne reste)", vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "pleine", T_PLEINE, ("arret",), panne_extraction=True, n_lignes=1)
        self.juger(s, b)

        s, b = self.scenario("N05", "journal présent et vide (0 octet) avant la première tentative", vue_t07=True)
        monter(b, scores=D_SCORES)
        (b.r / ob.JOURNAL_OUVERTURES).write_bytes(b"")
        s["avant"] = {"lecteur": self.lire(b.r / ob.JOURNAL_OUVERTURES)[1] or "lu",
                      "ecrivain": f"{len(ob.lire_journal(b.r / ob.JOURNAL_OUVERTURES))} ligne(s), aucun refus"}
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        self.juger(s, b)

        # ---- sondes de discordance ----
        s, b = self.scenario("D01", "horloge en arrière : refus à 12:00, puis ouverture pleine à 11:00 (dates décroissantes)",
                             vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_PLEINE, (R, "ni-scores-ni-ouvrir"))
        self.tenter(s, b, "pleine", T_AVANT, (O, "pleine"))
        self.juger(s, b)

        s, b = self.scenario("D02", "deux tentatives à la même seconde (dates égales)", vue_t07=True)
        monter(b, scores=D_SCORES)
        self.tenter(s, b, "reduite", T_PLEINE, (R, "ni-scores-ni-ouvrir"))
        self.tenter(s, b, "pleine", T_PLEINE, (O, "pleine"))
        self.juger(s, b)

        s, b = self.scenario("D04", "reduite : SCELLEMENT-T07 et garde adaptée citant un texte autre que "
                                    "prereg/T0.7-sondes-v0-v1.md", vue_t07=True)
        monter(b, scel_rel="prereg/T0.7-autre-v1.md", rdv=[("ouvrir", D_DEC1, D_RDV1)])
        self.tenter(s, b, "reduite", T_REDUITE, (O, "reduite"))
        self.juger(s, b)

    # ---------------------------------------------------------------------------------------------- tolérance
    def tolerance(self) -> None:
        ob = self.ob
        base = self.depot / "scenarios" / "S02" / ob.JOURNAL_OUVERTURES
        t = base.read_text(encoding="utf-8")
        l = t.split("\n")
        variantes = [
            ("journal tel qu'écrit (S02)", t),
            ("fichier vide (0 octet)", ""),
            ("en-tête seul", "\n".join(ob.ENTETE_JOURNAL) + "\n"),
            ("ligne vide entre deux lignes", "\n".join(l[:3] + [""] + l[3:])),
            ("ligne vide en fin", t + "\n"),
            ("sans saut de ligne final", t[:-1]),
            ("fins de ligne CRLF", t.replace("\n", "\r\n")),
            ("espace en tête d'une ligne", "\n".join(l[:2] + [" " + l[2]] + l[3:])),
            ("ligne de séparation de la table à colonnes alignées", "\n".join(l[:1] + ["| --- | --- | --- | --- | --- | --- |"]
                                                                               + l[2:])),
        ]
        tete = "\n".join(ob.ENTETE_JOURNAL) + "\n"
        a, z = "a" * 64, "f" * 64
        seules = [   # une ligne écrite à la main après l'en-tête : formes que l'écrivain n'écrit jamais
            ("OUVERTURE pleine-anticipee à paquets « - »", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine-anticipee | "
                                                          f"RENDEZ-VOUS-P3BIS-1={a} | - | - |"),
            ("OUVERTURE pleine à appui « - »", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | {a} {z} | - |"),
            ("OUVERTURE à motif autre que « - »", f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | SCORES-T07={a} "
                                                 f"SONDES-T07={z} | {a} {z} | paquet-faux : texte |"),
            ("REFUS à motif hors de la liste fermée", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | - | "
                                                     "code-inconnu : texte |"),
            ("REFUS à motif sans code", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | - | - | texte libre |"),
            ("REFUS à appui hors forme", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | pleine | texte libre | - | "
                                        "deja-ouverte : texte |"),
            ("date impossible (30 février)", "| REFUS-OUVERTURE-P3BIS | 2026-02-30T00:00:00Z | pleine | - | - | deja-ouverte : t |"),
            ("mode inconnu", "| REFUS-OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | Pleine | - | - | deja-ouverte : t |"),
            ("clé inconnue", "| OUVERTURE-P3BIS-2 | 2026-11-22T00:00:00Z | pleine | - | - | - |"),
        ]
        variantes += [(nom, tete + ligne + "\n") for nom, ligne in seules]
        variantes += [("ordre interdit : reduite après pleine (S02 + une ligne)",
                       t + f"| OUVERTURE-P3BIS | 2026-11-22T00:00:00Z | reduite | RENDEZ-VOUS-P3BIS-1={a} "
                           f"GARDE-ADAPTEE-T07-P3BIS={z} | {a} {z} | - |\n")]
        d = self.depot / "sondes"
        d.mkdir()
        for k, (nom, texte) in enumerate(variantes):
            p = d / f"journal-{k}.md"
            p.write_bytes(texte.encode("utf-8"))
            try:
                e = f"{len(ob.lire_journal(p))} ligne(s)"
            except ob.RefusOuverture as x:
                e = f"refus {x.code}"
            lues, faute = self.lire(p)
            r = f"{len(lues)} ligne(s)" if faute is None else "JournalFautif (nœud)"
            self.sondes.append((nom, e, r))

    # ---------------------------------------------------------------------------------------------- constantes
    def constantes(self) -> list:
        ob, jp, rg = self.ob, self.jp, self.rg
        return [
            ("en-tête du journal", ob.ENTETE_JOURNAL, jp.ENTETE_JOURNAL),
            ("chemin du journal", ob.JOURNAL_OUVERTURES, jp.JOURNAL_P3BIS),
            ("clés du journal", (ob.CLE_OUVERTURE, ob.CLE_REFUS), (jp.OUVERTURE_P3BIS, jp.REFUS_OUVERTURE_P3BIS)),
            ("modes", ob.MODES, jp.MODES_P3BIS),
            ("motif de date", ob.DATE.pattern, rg.DATE.pattern),
            ("motif d'empreinte", ob.SHA.pattern, rg.SHA.pattern),
            ("motif de clé", ob.CLE.pattern, rg.CLE.pattern),
            ("format de date", ob.FORMAT_DATE, rg.FORMAT_DATE),
            ("registre des préalables", ob.REGISTRE_PREALABLES, jp.PREALABLES_P3BIS),
            ("clés d'écrit", ob.CLES_ECRITS, jp.CLES_ECRITS_P3BIS),
            ("clé de la garde adaptée", ob.CLE_GARDE_ADAPTEE, jp.GARDE_ADAPTEE_T07_P3BIS),
            ("fichier de décision", ob.FICHIER_DECISION, jp.FICHIER_DECISION),
            ("décisions", (ob.MAINTENIR, ob.OUVRIR, ob.OUVRIR_PLEINEMENT), jp.DECISIONS),
            ("clé de rendez-vous dans l'appui (écrivain) / au registre (lecteur)", ob.CLE_RDV_APPUI.pattern,
             jp.RENDEZ_VOUS.pattern.replace("([1-9][0-9]*)", "[1-9][0-9]*")),
            ("clé de rendez-vous au registre des préalables", ob.RENDEZ_VOUS.pattern, jp.RENDEZ_VOUS.pattern),
        ]

    # ---------------------------------------------------------------------------------------------- impression
    def imprimer(self) -> int:
        compte = {"lue telle quelle": 0, "refusée": 0, "mal interprétée": 0}
        discordances = []
        print(f"ESSAI DE CONCORDANCE DU JOURNAL P3-BIS -> T0.7 (écrivain {COMMIT_ECRIVAIN[:8]}, lecteur {COMMIT_LECTEUR[:8]})")
        print("\nCONSTANTES (écrivain | lecteur) :")
        for nom, e, l in self.constantes():
            print(f"  {nom} : {'égales' if e == l else 'DIFFÉRENTES'}" + ("" if e == l else f" : {e!r} | {l!r}"))
        for s in self.resultats:
            print(f"\n[{s['id']}] {s['titre']}")
            if "avant" in s:
                print(f"    avant toute tentative : écrivain {s['avant']['ecrivain']} ; lecteur {s['avant']['lecteur']}")
            for t in s["tentatives"]:
                i = t["issue"]
                print(f"  tentative {t['mode']} @{t['instant']} -> écrivain : {i[0]}"
                      + (f" {i[1]}" if i[1] else "") + f" (code {i[2]}) ; lignes écrites : {len(t['neuves'])}")
                for n, brute, verdict, motif in t["jugements"]:
                    c = [x.strip() for x in brute[1:-1].split("|")]
                    motif_c = c[5].split(" : ")[0]
                    print(f"    l.{n} | {c[0]} | {c[1]} | {c[2]} | {court(c[3])} | {court(c[4])} | {motif_c} |")
                    print(f"        lecteur T0.7 : {verdict} ({motif[:300]})")
                    compte[verdict] += 1
                    if verdict != "lue telle quelle" and s["attendu_lecteur"] == "lu":
                        discordances.append(f"{s['id']} l.{n} : {verdict}")
            if not any(t["neuves"] for t in s["tentatives"]):
                lu = s["lecteur"]
                print(f"    aucune ligne écrite ; lecteur T0.7 sur le journal : "
                      + ("absent ou sans ligne -> aucune ouverture" if lu["faute"] is None else lu["faute"][:200]))
            print(f"    écrivain relisant le journal final : {s['ecrivain_relit']}")
            if "vue" in s:
                v = s["vue"]
                if "erreur" in v:
                    print(f"    vue de T0.7 : erreur {v['erreur'][:200]}")
                else:
                    for n, mode, m in v["appuis"]:
                        print(f"    vue de T0.7 : l.{n} ({mode}) : {m[:200]}")
                    print(f"    vue de T0.7 : garde de l'étape B (sans VERDICT-P3BIS) : codes {v['codes_b'] or 'aucun'} ; "
                          f"R14 : {v['r14'] or 'absente'}")
        print("\nSONDES DE TOLÉRANCE (fichier non écrit tel quel par l'écrivain) : état | écrivain (lire_journal) | lecteur T0.7")
        for nom, e, r in self.sondes:
            print(f"  {nom} | {e} | {r}")
        print(f"\nLIGNES ÉCRITES : {sum(compte.values())} ; lues telles quelles : {compte['lue telle quelle']} ; refusées : "
              f"{compte['refusée']} ; mal interprétées : {compte['mal interprétée']}")
        print("REFUS OU ÉCARTS NON ATTENDUS PAR LES TEXTES : " + ("; ".join(discordances) if discordances else "aucun"))
        if self.faux:
            print("ESSAI FAUX : " + " ; ".join(self.faux))
            return 1
        print("ESSAI : chaque tentative a donné l'issue visée (chaque type de ligne exercé)")
        return 0


def main(argv) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("dossier")
    ap.add_argument("--clone", default="/home/user/controle-ia-travail")
    a = ap.parse_args(argv)
    dossier = Path(a.dossier).absolute()
    if dossier.exists():
        raise SystemExit(f"{dossier} existe déjà : un dossier neuf est exigé")
    dossier.mkdir(parents=True)
    copier(Path(a.clone), dossier)
    os.environ["GIT_CEILING_DIRECTORIES"] = str(dossier)
    depot = dossier / "depot"
    subprocess.run(["git", "init", "-q", str(depot)], check=True)
    mods = importer(dossier)
    essai = Essai(dossier, mods)
    for run in ("run-a", "run-b"):
        faire_paquets(depot, run, essai.ob, essai.scellement.sceller)
    essai.jouer()
    essai.tolerance()
    return essai.imprimer()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
