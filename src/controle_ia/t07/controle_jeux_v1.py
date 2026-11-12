"""Contrôles des jeux génériques par la chaîne de T0.7, avant l'extraction — v1 (fichier neuf, R12 ; écart E-8 de l'inventaire des jeux,
`docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/inventaire-jeux-t07-v1.md`, `c9910a54…` ; décision D-2 (a) de la mère, R-2101).

La consigne scellée des jeux (`docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`, `d9de50a6…`) confie à la chaîne de T0.7
deux gestes avant l'extraction :

1. **Rejeu du contrôle 9** (§ 7 ; § 8, contrôle 9) contre les textes de la course lue (7b ; « absents à la vérification ») :
   une suite de **8 mots consécutifs** (mots sans casse, sans accents, sans ponctuation : `normaliser`, copie de
   `scripts/verifier_jeux_synthetiques_t07_v2.py` `e53c9c27…` l. 142-151) commune entre une réponse, un bloc, un rappel ou une
   incitation des jeux et un texte d'action de la course met la paire **en défaut** ; les suites qui figurent aussi dans l'énoncé
   de la tâche (`questions` du fichier scellé des tâches de réserve) ne comptent pas. Une paire en défaut **n'est pas réécrite** :
   elle est **exclue** et consignée ; la tâche reste dans le jeu si elle garde au moins 8 paires (J-D, J-C) ou 4 paires par mode
   (J-A) (§ 10, étape 4), sinon elle sort du jeu (consigné) ; le jeu scellé et son empreinte ne changent pas. Bloc et rappel (J-D,
   membre positif) et incitation (J-C) sont pris comme les suites du contexte du membre absentes du **contexte de base** de la même
   tâche (contexte sans insertion : membre négatif de J-D ou membre de J-A, assemblés par la même fonction du script, § 2) ; sans
   contexte de base pour la tâche, l'insertion n'est pas isolée et c'est écrit (aucun repli silencieux).
2. **Remesure des jetons** (§ 2) comme **garde d'identité** : les moyennes de longueur que le journal du script écrit par jeu et par
   étiquette (`[INFO] longueurs <jeu>, étiquette <e> (moyennes sur <n> réponses) : {…}`, fonction `rapporter`, l. 1142-1153 :
   mots, caractères, jetons, et pour J-C et J-A les mêmes avant `COST:`) sont recalculées sur le jeu scellé avec le tokeniseur du
   modèle de la course ; **un écart est un arrêt** (R5 : tokeniseur ou texte différent), jamais une réécriture. Le journal est le
   seul fichier `journal-verification*.txt` scellé du dossier du jeu qui porte ses lignes (convention de dépôt du § 3 de la
   consigne ; à nommer par le texte, réserve déclarée) ; absent en mode réel : arrêt ; en jouet : « non vérifiée ».

Seuils des paires restantes : `min(seuil de la consigne, paires de la tâche dans le jeu scellé)` (un jeu jouet de deux paires par
tâche n'est pas vidé par la règle ; en mode réel, dix paires par tâche, le seuil est celui de la consigne).
"""
from __future__ import annotations

import ast
import json
import re
import unicodedata
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import verifier
from . import registre_v1 as rg
from . import sondes_neuves_v1 as sn

N_GRAMME = 8
SEUIL_PAIRES = {sn.JEU_JD: 8, sn.JEU_JC: 8}
SEUIL_PAIRES_PAR_MODE = {sn.JEU_JA: 4}
CHEMIN_ENONCES_REEL = "donnees/20261007-082440-t05-extraction/taches-entrainement.json"
SHA_ENONCES_REEL = "8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd"
EMPREINTE_TOKENISEUR = "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"
MESURES = ("caractères", "jetons", "mots")
MESURES_AVANT = ("caractères avant COST", "jetons avant COST", "mots avant COST")
LIGNE_LONGUEURS = re.compile(r"^\[INFO\] longueurs (?P<jeu>[a-z-]+), étiquette (?P<e>[01]) \(moyennes sur (?P<n>\d+) réponses\) : "
                             r"(?P<d>\{.*\})$")


# ------------------------------------------------------------------------------------------------------------- suites de mots
def normaliser(texte: str) -> list[str]:
    """Copie de `verifier_jeux_synthetiques_t07_v2.normaliser` : mots sans casse, sans accents, sans ponctuation."""
    t = unicodedata.normalize("NFKD", texte)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.findall(r"[0-9a-z]+", t)


def n_grammes(mots: list[str], n: int = N_GRAMME) -> set[tuple[str, ...]]:
    """Copie de `verifier_jeux_synthetiques_t07_v2.n_grammes`."""
    return {tuple(mots[i:i + n]) for i in range(len(mots) - n + 1)}


def grammes(texte: str) -> set[tuple[str, ...]]:
    return n_grammes(normaliser(texte))


def _contexte(r: dict) -> str:
    return r["contexte_systeme"] + "\n" + r["observation"]


# ------------------------------------------------------------------------------------------------------------------- énoncés
def exiger_enonces_config(config: dict) -> None:
    """Clé facultative `enonces_reserve` ({chemin, sha256}) ; en mode réel, le fichier scellé des tâches de réserve de T0.5."""
    d = config.get("enonces_reserve")
    if d is None:
        return
    if not isinstance(d, dict) or set(d) != {"chemin", "sha256"} or not isinstance(d["chemin"], str) \
            or not isinstance(d["sha256"], str) or not rg.SHA.fullmatch(d["sha256"]):
        raise GardeArret("enonces_reserve : {chemin, sha256} attendu")
    if config["mode"] == "reel" and (d["chemin"] != CHEMIN_ENONCES_REEL or d["sha256"] != SHA_ENONCES_REEL):
        raise GardeArret(f"enonces_reserve : {CHEMIN_ENONCES_REEL} à l'empreinte {SHA_ENONCES_REEL[:8]}… attendu en mode réel")


def exiger_enonces_pour_l_etape(config: dict) -> None:
    """Étape A complète en mode réel : le rejeu du contrôle 9 exige l'énoncé des tâches (consigne v3, § 7) ; clé absente → refus."""
    if config["mode"] == "reel" and config.get("enonces_reserve") is None:
        raise GardeArret("mode réel : clé enonces_reserve absente ; le rejeu du contrôle 9 des jeux (consigne v3, § 7 ; E-8, D-2 (a)) "
                         "exige l'énoncé des tâches de réserve : refus")


def lire_enonces(racine: Path, config: dict) -> dict | None:
    """{identifiant: questions} du fichier cité (sceau vérifié) ; seuls `identifiant` et `questions` sont lus."""
    d = config.get("enonces_reserve")
    if d is None:
        return None
    chemin = Path(racine) / d["chemin"]
    try:
        rg.sceau_conforme(chemin, d["sha256"])
        taches = json.loads(chemin.read_text(encoding="utf-8"))["resultat"]["taches"]
        sortie = {str(t["identifiant"]): str(t["questions"]) for t in taches}
    except GardeArret:
        raise
    except (OSError, ValueError, KeyError, TypeError) as e:
        raise GardeArret(f"énoncés des tâches de réserve ({chemin}) illisibles ({type(e).__name__})") from None
    if len(sortie) != len(taches):
        raise GardeArret("énoncés des tâches de réserve : identifiant en double")
    return sortie


# ---------------------------------------------------------------------------------------------------------- rejeu du contrôle 9
def _paires(recs: list) -> dict:
    p: dict = {}
    for r in recs:
        p.setdefault((r["tache"], r["paire"]), []).append(r)
    return p


def rejouer_controle_9(jeux: dict, textes_course, enonces: dict | None) -> dict:
    """Rejeu du contrôle 9 sur les jeux scellés présents (`{"JD"|"JC"|"JA": enregistrements}`) contre les textes d'action de la
    course. Rend {"jeux": jeux filtrés, "rapport": {…}} ; le rapport porte, par jeu, les paires exclues et leur motif, les tâches
    sorties du jeu et les comptes avant et après."""
    course: set = set()
    n_textes = 0
    for t in textes_course:
        course |= grammes(str(t))
        n_textes += 1
    base: dict = {}
    for cle in ("JD", "JA"):
        for r in jeux.get(cle, []):
            if r["jeu"] == sn.JEU_JD and r["instruction_id"] is not None:
                continue
            base.setdefault(r["tache"], grammes(_contexte(r)))
    filtres, rapport = {}, {"regle": "consigne v3 des jeux, § 7 et § 10 étape 4 (E-8, D-2 (a)) : suites de 8 mots communes avec un "
                                      "texte d'action de la course, hors énoncé de la tâche ; paire exclue, jamais réécrite",
                            "textes_course": n_textes, "enonces": "lus" if enonces is not None else "non cités (jouet)", "jeux": {}}
    for cle, recs in jeux.items():
        jeu = recs[0]["jeu"]
        paires = _paires(recs)
        defauts, sans_base = [], set()
        for (tache, paire), membres in paires.items():
            ge = grammes(enonces[tache]) if enonces and tache in enonces else set()
            motifs = []
            for m in sorted(membres, key=lambda x: x["membre"]):
                if (grammes(m["reponse"]) & course) - ge:
                    motifs.append(f"membre {m['membre']} : réponse")
                insere = (jeu == sn.JEU_JD and m["instruction_id"] is not None) or jeu == sn.JEU_JC
                if insere:
                    if tache not in base:
                        sans_base.add(tache)
                    elif ((grammes(_contexte(m)) - base[tache]) & course) - ge:
                        motifs.append(f"membre {m['membre']} : {'bloc ou rappel' if jeu == sn.JEU_JD else 'incitation'}")
            if motifs:
                defauts.append({"tache": tache, "paire": paire, "motifs": motifs})
        exclues = {(d["tache"], d["paire"]) for d in defauts}
        sorties = []
        for tache in sorted({t for t, _ in paires}):
            if jeu in SEUIL_PAIRES_PAR_MODE:
                for mode in sorted({membres[0]["mode"] for (t, _), membres in paires.items() if t == tache}):
                    n0 = sum(1 for (t, p), ms in paires.items() if t == tache and ms[0]["mode"] == mode)
                    n1 = sum(1 for (t, p), ms in paires.items() if t == tache and ms[0]["mode"] == mode and (t, p) not in exclues)
                    if n1 < min(SEUIL_PAIRES_PAR_MODE[jeu], n0):
                        sorties.append({"tache": tache, "mode": mode, "paires_restantes": n1, "paires_scellees": n0})
            else:
                n0 = sum(1 for (t, _) in paires if t == tache)
                n1 = sum(1 for (t, p) in paires if t == tache and (t, p) not in exclues)
                if n1 < min(SEUIL_PAIRES[jeu], n0):
                    sorties.append({"tache": tache, "paires_restantes": n1, "paires_scellees": n0})
        taches_sorties = {s["tache"] for s in sorties}
        filtres[cle] = [r for r in recs if (r["tache"], r["paire"]) not in exclues and r["tache"] not in taches_sorties]
        rapport["jeux"][cle] = {"jeu": jeu, "paires_scellees": len(paires), "paires_en_defaut": defauts, "taches_sorties": sorties,
                                "paires_gardees": len(_paires(filtres[cle])) if filtres[cle] else 0,
                                "insertion_non_isolee": sorted(sans_base)}
        if not filtres[cle]:
            del filtres[cle]
            rapport["jeux"][cle]["etat"] = "jeu vidé par le rejeu : aucune sonde apprise sur ce jeu"
    return {"jeux": filtres, "rapport": rapport}


# ------------------------------------------------------------------------------------------------------------ remesure des jetons
def mesurer_longueurs(recs: list, compter) -> dict:
    """Moyennes par étiquette, comme `rapporter` du script : `round(somme / nombre, 1)` sur les réponses (mots = suites non blanches,
    caractères, jetons sans jeton spécial) et, pour J-C et J-A, sur le texte avant `COST:`."""
    jeu = recs[0]["jeu"]
    sommes: dict = {0: {}, 1: {}}
    nombres = {0: 0, 1: 0}
    for r in recs:
        e = int(r["etiquette"])
        nombres[e] += 1
        texte = r["reponse"]
        valeurs = {"mots": len(texte.split()), "caractères": len(texte), "jetons": int(compter(texte))}
        if jeu != sn.JEU_JD:
            av = texte[:r["position_cost"]]
            valeurs.update({"mots avant COST": len(av.split()), "caractères avant COST": len(av), "jetons avant COST": int(compter(av))})
        for k, v in valeurs.items():
            sommes[e][k] = sommes[e].get(k, 0) + v
    return {e: {"n": nombres[e], "moyennes": {k: round(v / nombres[e], 1) for k, v in sommes[e].items()}}
            for e in (0, 1) if nombres[e]}


def lire_longueurs(texte: str, jeu: str) -> dict:
    sortie = {}
    for ligne in texte.splitlines():
        m = LIGNE_LONGUEURS.match(ligne)
        if m and m.group("jeu") == jeu:
            e = int(m.group("e"))
            if e in sortie:
                raise GardeArret(f"journal du script : deux lignes de longueurs pour {jeu}, étiquette {e}")
            try:
                d = ast.literal_eval(m.group("d"))
            except (ValueError, SyntaxError):
                raise GardeArret(f"journal du script : ligne de longueurs illisible ({jeu}, étiquette {e})") from None
            sortie[e] = {"n": int(m.group("n")), "moyennes": d}
    return sortie


def journal_du_jeu(chemin_jeu: Path, jeu: str) -> tuple[Path, dict] | None:
    """Le journal du script du dossier du jeu qui porte ses lignes de longueurs (scellé) ; plusieurs → arrêt ; aucun → None."""
    trouves = []
    for f in sorted(Path(chemin_jeu).parent.glob("journal-verification*.txt")):
        lu = lire_longueurs(f.read_text(encoding="utf-8"), jeu)
        if lu:
            trouves.append((f, lu))
    if len(trouves) > 1:
        raise GardeArret(f"remesure des jetons : plusieurs journaux du script portent le jeu {jeu} ({[f.name for f, _ in trouves]}) : "
                         "arrêt (journal ambigu)")
    if not trouves:
        return None
    verifier(trouves[0][0])
    return trouves[0]


def remesurer_jetons(cle: str, recs: list, chemin_jeu: Path, compter, mode: str) -> dict:
    """Garde d'identité du jeu (consigne v3, § 2) : écart avec le journal du script → `GardeArret`. Rend le rapport."""
    jeu = recs[0]["jeu"]
    j = journal_du_jeu(chemin_jeu, jeu)
    if j is None:
        if mode == "reel":
            raise GardeArret(f"remesure des jetons de {cle} : aucun journal du script scellé (journal-verification*.txt) dans "
                             f"{Path(chemin_jeu).parent} : identité du jeu non vérifiable : arrêt")
        return {"etat": "non vérifiée : journal du script absent (jouet)"}
    chemin, attendu = j
    texte = chemin.read_text(encoding="utf-8")
    if mode == "reel" and EMPREINTE_TOKENISEUR not in texte:
        raise GardeArret(f"remesure des jetons de {cle} : le journal {chemin.name} ne cite pas le tokeniseur {EMPREINTE_TOKENISEUR[:8]}… : arrêt")
    obtenu = mesurer_longueurs(recs, compter)
    cles = MESURES + (MESURES_AVANT if jeu != sn.JEU_JD else ())
    ecarts = []
    for e in (0, 1):
        a, o = attendu.get(e), obtenu.get(e)
        if a is None or o is None:
            ecarts.append(f"étiquette {e} : {'absente du journal' if a is None else 'absente du jeu'}")
            continue
        if a["n"] != o["n"]:
            ecarts.append(f"étiquette {e} : {o['n']} réponses pour {a['n']} au journal")
        for k in cles:
            if k not in a["moyennes"]:
                ecarts.append(f"étiquette {e} : « {k} » absent du journal")
            elif float(a["moyennes"][k]) != float(o["moyennes"][k]):
                ecarts.append(f"étiquette {e}, {k} : {o['moyennes'][k]} pour {a['moyennes'][k]} au journal")
    if ecarts:
        raise GardeArret(f"remesure des jetons de {cle} : écart avec le journal du script {chemin.name} ({' ; '.join(ecarts[:6])}) : "
                         "tokeniseur ou texte différent (R5) : arrêt")
    return {"etat": "conforme", "journal": chemin.name, "journal_sha256": verifier(chemin), "comparees": list(cles),
            "reponses": {str(e): obtenu[e]["n"] for e in obtenu}}
