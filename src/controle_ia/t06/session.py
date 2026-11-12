"""Chaîne de session de T0.6 (brouillon 3, point 4 (vi) ; P3-bis, « Ce que le code et la chaîne doivent changer »,
point 5) : gardes mécaniques lues par `scripts/lancer_t06_v1.sh`. Bibliothèque standard seule (lancé par `python3 -I`,
hors du dépôt et avant toute installation). Aucun appel au réseau ni à l'outil de location : la garde lit un état et rend
une décision.

    python -I -m controle_ia.t06.session go REGISTRE_GO.md [AAAA-MM-JJ]
        GO-2026-11-02-28 seulement : une ligne de base à huit colonnes, type « calcul », plafond « 200 USD », accordée
        par Lazar ; date du jour entre l'accord et l'échéance ; aucune ligne de type « révocation » qui cite l'identifiant ;
        une seconde ligne au même identifiant n'est admise que comme extension (R-389) et ne change ni le plafond lu ici
        (200 USD, exact) ni la validité. Écrit « GO-2026-11-02-28 conforme ».
    python -I -m controle_ia.t06.session depense PRIX_CARTE PRIX_STOCKAGE CREE_LE_S [MAINTENANT_S] [FACTURE_USD]
        Dépense cumulée = heures écoulées depuis la création × prix de la carte + heures écoulées × prix du stockage ;
        la facture relevée la remplace si elle est plus grande. Écrit « cumulee=<usd> plafond=200 arret=oui|non ».
    python -I -m controle_ia.t06.session surveillance JOURNAL.txt MAINTENANT_S PRIX_CARTE PRIX_STOCKAGE CREE_LE_S [FACTURE]
        Décision de surveillance sans couperet de temps : « ARRET mort » (ligne « RUN MORT … » de l'amorce : processus du
        run mort sans résumé ni arrêt consigné), « ARRET depense » (dépense cumulée ≥ 200 USD), « FIN » (ligne « AMORCE …
        fin » : run terminé, résultats poussés), « ALERTE sans PROGRES depuis N s » (plus de deux heures sans ligne
        « PROGRES », aucun arrêt), sinon « POURSUIVRE ». Les heures des lignes sont lues dans leur horodatage UTC.
Code 0 ; 1 avec un motif sur la dernière ligne en cas de refus ; 2 sur un usage faux.
"""
from __future__ import annotations

import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

GO_ID = "GO-2026-11-02-28"
PLAFOND_USD = 200.0
ALERTE_SANS_PROGRES_S = 7200
LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
COLONNES = ("id", "accorde", "type", "perimetre", "plafond", "echeance", "par", "ref")
HORODATAGE = re.compile(r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})Z")
MOTIF_MORT = re.compile(r"^(?:AMORCE|INSTANCE) .*RUN MORT", re.M)
MOTIF_FIN = re.compile(r"^AMORCE .* fin, code [0-9]+", re.M)
MOTIF_REFUS = re.compile(r"^AMORCE .*refus", re.M)


class GardeSession(RuntimeError):
    pass


def _cellules(ligne: str) -> list[str]:
    return [x.strip() for x in ligne.strip().strip("|").split("|")]


def _date(s: str, quoi: str) -> date:
    try:
        return date.fromisoformat(s)
    except ValueError:
        raise GardeSession(f"{quoi} : date illisible {s!r}") from None


def _plafond(s: str) -> float | None:
    m = re.fullmatch(r"(\d+(?:[.,]\d+)?)\s*USD", s)
    return float(m.group(1).replace(",", ".")) if m else None


def verifier_go(chemin, aujourd_hui: date | None = None, go_id: str = GO_ID, plafond: float = PLAFOND_USD) -> dict:
    p = Path(chemin)
    if not p.is_file():
        raise GardeSession(f"registre {chemin} absent")
    j = aujourd_hui or datetime.now(timezone.utc).date()
    lignes = []
    for n, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if LIGNE_GO.match(l):
            c = _cellules(l)
            if len(c) != 8:
                raise GardeSession(f"ligne {n} : 8 colonnes attendues, {len(c)}")
            lignes.append(dict(zip(COLONNES, c), ligne=n))
    propres = [l for l in lignes if l["id"] == go_id]
    if not propres:
        raise GardeSession(f"{go_id} absent du registre")
    g, autres = propres[0], propres[1:]
    if g["type"] != "calcul":
        raise GardeSession(f"{go_id} : type {g['type']!r}, « calcul » attendu")
    if g["par"] != "Lazar":
        raise GardeSession(f"{go_id} : accordé par {g['par']!r}, « Lazar » attendu")
    if _plafond(g["plafond"]) != plafond:
        raise GardeSession(f"{go_id} : plafond {g['plafond']!r}, « {plafond:g} USD » exact attendu")
    accorde, echeance = _date(g["accorde"], "accord"), _date(g["echeance"], "échéance")
    for a in autres:
        if not (a["perimetre"].lower().startswith("extension") and a["type"] == "calcul" and a["par"] == "Lazar"
                and _date(a["accorde"], "extension") >= accorde and _date(a["echeance"], "extension") <= echeance):
            raise GardeSession(f"{go_id} : ligne {a['ligne']} en double, autre qu'une extension conforme (R-389)")
    if not accorde <= j <= echeance:
        raise GardeSession(f"{go_id} hors de sa période de validité ({accorde} → {echeance}) le {j}")
    for l in lignes:
        if l["type"] == "révocation" and (go_id in l["perimetre"] or go_id in l["ref"]):
            raise GardeSession(f"{go_id} révoqué par {l['id']}")
    return {"go": go_id, "plafond_usd": plafond, "accorde": str(accorde), "echeance": str(echeance), "ligne": g["ligne"]}


def _nombre(s, quoi: str, positif: bool = False) -> float:
    try:
        v = float(s)
    except (TypeError, ValueError):
        raise GardeSession(f"{quoi} illisible : {s!r}") from None
    if v != v or v < 0 or (positif and v <= 0):
        raise GardeSession(f"{quoi} : nombre {'strictement positif' if positif else 'positif'} attendu, {s!r}")
    return v


def depense_cumulee(prix_carte, prix_stockage, cree_le_s, maintenant_s=None, facture_usd=None) -> dict:
    p_c = _nombre(prix_carte, "prix de la carte", positif=True)
    p_s = _nombre(prix_stockage, "prix du stockage")
    cree = _nombre(cree_le_s, "création")
    now = _nombre(maintenant_s, "maintenant") if maintenant_s is not None else datetime.now(timezone.utc).timestamp()
    if now < cree:
        raise GardeSession("création postérieure à maintenant")
    h = (now - cree) / 3600.0
    cumulee = h * (p_c + p_s)
    if facture_usd is not None:
        cumulee = max(cumulee, _nombre(facture_usd, "facture"))
    return {"cumulee_usd": round(cumulee, 4), "heures": round(h, 4), "plafond_usd": PLAFOND_USD, "arret": cumulee >= PLAFOND_USD}


def _derniere_heure(texte: str, motif: str) -> float | None:
    heures = [m.group(1) for m in HORODATAGE.finditer("\n".join(l for l in texte.splitlines() if motif in l))]
    if not heures:
        return None
    return max(datetime.strptime(h, "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc).timestamp() for h in heures)


def decider_surveillance(journal: str, maintenant_s: float, depense: dict) -> str:
    """Décision écrite sur une ligne ; jamais d'arrêt sur la seule durée."""
    if MOTIF_MORT.search(journal):
        return "ARRET mort : processus du run mort sans résumé ni arrêt consigné : arrêter l'instance par son identifiant (R10)"
    if depense["arret"]:
        return (f"ARRET depense : dépense cumulée {depense['cumulee_usd']:.2f} USD ≥ plafond {PLAFOND_USD:g} USD : arrêter "
                "l'instance par son identifiant (R10) ; résultats partiels consignés comme tels")
    if MOTIF_FIN.search(journal):
        return "FIN : run terminé (ligne de fin de l'amorce) ; instance à arrêter par son identifiant, disque gardé jusqu'au verdict"
    if MOTIF_REFUS.search(journal):
        return "REFUS : l'amorce a refusé avant le run (destruction par la minuterie) ; vérifier l'inventaire"
    derniere = _derniere_heure(journal, "PROGRES ")
    if derniere is None:
        derniere = _derniere_heure(journal, "AMORCE ")
    if derniere is not None and maintenant_s - derniere > ALERTE_SANS_PROGRES_S:
        return f"ALERTE sans PROGRES depuis {int(maintenant_s - derniere)} s : alerte à la session, aucun arrêt"
    return "POURSUIVRE"


def main(argv: list[str]) -> int:
    try:
        if len(argv) in (2, 3) and argv[0] == "go":
            r = verifier_go(argv[1], date.fromisoformat(argv[2]) if len(argv) == 3 else None)
            print(f"{r['go']} conforme (plafond {r['plafond_usd']:g} USD, {r['accorde']} → {r['echeance']})")
        elif len(argv) in (4, 5, 6) and argv[0] == "depense":
            d = depense_cumulee(argv[1], argv[2], argv[3], argv[4] if len(argv) > 4 else None, argv[5] if len(argv) > 5 else None)
            print(f"cumulee={d['cumulee_usd']:.4f} heures={d['heures']:.4f} plafond={PLAFOND_USD:g} arret={'oui' if d['arret'] else 'non'}")
            return 1 if d["arret"] else 0
        elif len(argv) in (6, 7) and argv[0] == "surveillance":
            texte = Path(argv[1]).read_text(encoding="utf-8") if Path(argv[1]).is_file() else ""
            now = _nombre(argv[2], "maintenant")
            d = depense_cumulee(argv[3], argv[4], argv[5], now, argv[6] if len(argv) > 6 else None)
            print(decider_surveillance(texte, now, d))
        else:
            print("usage : go REGISTRE [JOUR] | depense PRIX_CARTE PRIX_STOCKAGE CREE_LE_S [MAINTENANT_S] [FACTURE] | "
                  "surveillance JOURNAL MAINTENANT_S PRIX_CARTE PRIX_STOCKAGE CREE_LE_S [FACTURE]", file=sys.stderr)
            return 2
    except GardeSession as e:
        print(str(e))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
