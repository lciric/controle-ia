"""Chaîne de session de T0.6, v3 (C-V4-3, nécessaire aux ordres des épreuves E2 et E3 ; nom neuf, R12 : `session.py` et
`session_v2.py` restent tels quels). La v2 fige le GO (GO-2026-11-02-28) et le plafond (200 USD) ; les épreuves à blanc E2 et E3
sont sous GO-2026-11-06-01 (5 USD, E2 ≤ 1,5 USD, E3 ≤ 3,5 USD). Ici l'identifiant du GO et le plafond sont des **arguments**, lus
par la chaîne dans la configuration (`go_id`, `plafond_usd`) ; la ligne du registre doit porter ce plafond **exact** (« 5 USD »
ou « 5 USD (E2 et E3 cumulés) » : un commentaire entre parenthèses après « USD » est admis, rien d'autre). Bibliothèque standard
seule ; aucun appel au réseau ni à l'outil de location.

    python -I -m controle_ia.t06.session_v3 go REGISTRE_GO.md GO_ID PLAFOND_USD [AAAA-MM-JJ]
    python -I -m controle_ia.t06.session_v3 depense PLAFOND_USD PRIX_CARTE PRIX_STOCKAGE CREE_LE_S ANTERIEURE_USD TELECHARGEMENT_USD [MAINTENANT_S|-] [FACTURE|-] [EPUISEMENT_SIMULE_S]
        comme `session_v2 depense`, au plafond donné ; `EPUISEMENT_SIMULE_S` (E2 seulement, ≥ 60) remplace l'heure d'épuisement
        par « création + ce nombre de secondes » pour éprouver le redémarrage après une dépense épuisée ; il ne peut qu'avancer
        l'heure (jamais la reculer au-delà de l'épuisement réel).
    python -I -m controle_ia.t06.session_v3 calendrier CONFIG.json REGISTRE_GO.md GO_ID PLAFOND_USD [AAAA-MM-JJ]
    python -I -m controle_ia.t06.session_v3 surveillance PLAFOND_USD JOURNAL MAINTENANT_S PRIX_CARTE PRIX_STOCKAGE CREE_LE_S ANTERIEURE TELECHARGEMENT [FACTURE]
    python -I -m controle_ia.t06.session_v3 offre|instances … : comme la v2.
Code 0 ; 1 avec un motif sur la dernière ligne ; 2 sur un usage faux.
"""
from __future__ import annotations

import math
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from . import session as s1
from . import session_v2 as s2
from .session import GardeSession, _nombre, decider_surveillance

_PLAFOND = re.compile(r"(\d+(?:[.,]\d+)?)\s*USD(?:\s*\([^()]*\))?")
ID_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2}")


def _plafond_ligne(cellule: str) -> float | None:
    m = _PLAFOND.fullmatch(cellule.strip())
    return float(m.group(1).replace(",", ".")) if m else None


def _exiger_arguments(go_id: str, plafond) -> float:
    if not ID_GO.fullmatch(str(go_id)):
        raise GardeSession(f"identifiant de GO illisible : {go_id!r}")
    p = _nombre(plafond, "plafond", positif=True)
    return p


def verifier_go_v3(chemin, go_id: str, plafond, jour: date | None = None) -> dict:
    """`session.verifier_go` au GO et au plafond donnés ; le plafond du registre peut porter un commentaire entre parenthèses."""
    p = _exiger_arguments(go_id, plafond)
    fichier = Path(chemin)
    if not fichier.is_file():
        raise GardeSession(f"registre {chemin} absent")
    lignes = []
    for n, l in enumerate(fichier.read_text(encoding="utf-8").splitlines(), 1):
        if s1.LIGNE_GO.match(l):
            c = s1._cellules(l)
            if len(c) != 8:
                raise GardeSession(f"ligne {n} : 8 colonnes attendues, {len(c)}")
            lignes.append(dict(zip(s1.COLONNES, c), ligne=n))
    propres = [l for l in lignes if l["id"] == go_id]
    if not propres:
        raise GardeSession(f"{go_id} absent du registre")
    g, autres = propres[0], propres[1:]
    if g["type"] != "calcul":
        raise GardeSession(f"{go_id} : type {g['type']!r}, « calcul » attendu")
    if g["par"] != "Lazar":
        raise GardeSession(f"{go_id} : accordé par {g['par']!r}, « Lazar » attendu")
    if _plafond_ligne(g["plafond"]) != p:
        raise GardeSession(f"{go_id} : plafond {g['plafond']!r}, « {p:g} USD » exact attendu")
    accorde, echeance = s1._date(g["accorde"], "accord"), s1._date(g["echeance"], "échéance")
    for a in autres:
        if not (a["perimetre"].lower().startswith("extension") and a["type"] == "calcul" and a["par"] == "Lazar"
                and s1._date(a["accorde"], "extension") >= accorde and s1._date(a["echeance"], "extension") <= echeance):
            raise GardeSession(f"{go_id} : ligne {a['ligne']} en double, autre qu'une extension conforme (R-389)")
    j = jour or datetime.now(timezone.utc).date()
    if not accorde <= j <= echeance:
        raise GardeSession(f"{go_id} hors de sa période de validité ({accorde} → {echeance}) le {j}")
    for l in lignes:
        if l["type"] == "révocation" and (go_id in l["perimetre"] or go_id in l["ref"]):
            raise GardeSession(f"{go_id} révoqué par {l['id']}")
    return {"go": go_id, "plafond_usd": p, "accorde": str(accorde), "echeance": str(echeance), "ligne": g["ligne"]}


def depense_cumulee_v3(plafond, prix_carte, prix_stockage, cree_le_s, anterieure_usd, telechargement_usd, maintenant_s=None,
                       facture_usd=None, epuisement_simule_s=None) -> dict:
    p = _nombre(plafond, "plafond", positif=True)
    p_c = _nombre(prix_carte, "prix de la carte", positif=True)
    p_s = _nombre(prix_stockage, "prix du stockage")
    cree = _nombre(cree_le_s, "création")
    ant = _nombre(anterieure_usd, "dépense antérieure")
    tel = _nombre(telechargement_usd, "téléchargement")
    now = _nombre(maintenant_s, "maintenant") if maintenant_s is not None else datetime.now(timezone.utc).timestamp()
    if now < cree:
        raise GardeSession("création postérieure à maintenant")
    h = (now - cree) / 3600.0
    instance = h * (p_c + p_s)
    if facture_usd is not None:
        instance = max(instance, _nombre(facture_usd, "facture"))
    cumulee = ant + tel + instance
    reste = p - ant - tel
    epuisement = cree + reste / (p_c + p_s) * 3600.0 if reste > 0 else cree
    simule = None
    if epuisement_simule_s is not None:
        simule = _nombre(epuisement_simule_s, "épuisement simulé", positif=True)
        if simule < 60:
            raise GardeSession(f"épuisement simulé : 60 s au moins, {simule:g} donné")
        if cree + simule < epuisement:
            epuisement = cree + simule                                      # n'avance que l'heure : jamais plus tard que l'épuisement réel
    return {"cumulee_usd": round(cumulee, 4), "instance_usd": round(instance, 4), "anterieure_usd": ant, "telechargement_usd": tel,
            "heures": round(h, 4), "plafond_usd": p, "arret": cumulee >= p, "epuisement_utc_s": int(math.floor(epuisement)),
            "simule": simule is not None}


def verifier_calendrier_v3(config: dict, registre_go, go_id: str, plafond, jour: date | None = None) -> dict:
    """`session_v2.verifier_calendrier` au GO et au plafond donnés (L11 : fin du GO = lendemain 00:00 UTC de son échéance)."""
    cal = config.get("calendrier")
    if not isinstance(cal, dict):
        raise GardeSession("configuration sans calendrier (L11)")
    try:
        dernier = date.fromisoformat(cal["dernier_jour_creation"])
        fin = datetime.fromisoformat(str(cal["fin_go_utc"]).replace("Z", "+00:00"))
    except (KeyError, TypeError, ValueError):
        raise GardeSession("calendrier illisible : dernier_jour_creation (AAAA-MM-JJ) et fin_go_utc (instant UTC) attendus") from None
    if fin.tzinfo is None or fin.utcoffset() != timedelta(0):
        raise GardeSession("calendrier : fin_go_utc en UTC attendue")
    go = verifier_go_v3(registre_go, go_id, plafond, jour)
    echeance = date.fromisoformat(go["echeance"])
    attendue = datetime.combine(echeance + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc)
    if fin != attendue:
        raise GardeSession(f"calendrier : fin_go_utc {cal['fin_go_utc']} ≠ lendemain 00:00 UTC de l'échéance du GO ({attendue.isoformat()})")
    if not dernier < echeance + timedelta(days=1):
        raise GardeSession(f"calendrier : dernier jour de création {dernier} après la fin du GO")
    j = jour or datetime.now(timezone.utc).date()
    if j > dernier:
        raise GardeSession(f"dernier jour de création ({dernier}) dépassé le {j} : nœud de Lazar, aucune création")
    return {"fin_go_utc_s": int(fin.timestamp()), "dernier_jour_creation": str(dernier), "echeance_go": str(echeance), "jour": str(j)}


def decider_surveillance_v3(journal: str, maintenant_s: float, depense: dict) -> str:
    """`session.decider_surveillance` avec le plafond de la dépense (le texte de la v1 nomme 200 USD)."""
    if depense["arret"] and not s1.MOTIF_MORT.search(journal):
        return (f"ARRET depense : dépense cumulée {depense['cumulee_usd']:.2f} USD ≥ plafond {depense['plafond_usd']:g} USD : arrêter "
                "l'instance par son identifiant (R10) ; résultats partiels consignés comme tels")
    return decider_surveillance(journal, maintenant_s, {**depense, "arret": False})


def main(argv: list[str]) -> int:
    try:
        if len(argv) in (4, 5) and argv[0] == "go":
            r = verifier_go_v3(argv[1], argv[2], argv[3], date.fromisoformat(argv[4]) if len(argv) == 5 else None)
            print(f"{r['go']} conforme (plafond {r['plafond_usd']:g} USD, {r['accorde']} → {r['echeance']})")
        elif len(argv) in (7, 8, 9, 10) and argv[0] == "depense":
            opt = [None if x in ('', '-') else x for x in argv[7:10]]              # « - » : valeur absente (facture sans simulation, etc.)
            d = depense_cumulee_v3(*argv[1:7], *(opt + [None] * (3 - len(opt))))
            print(f"cumulee={d['cumulee_usd']:.4f} instance={d['instance_usd']:.4f} heures={d['heures']:.4f} plafond={d['plafond_usd']:g} "
                  f"arret={'oui' if d['arret'] else 'non'} epuisement_utc_s={d['epuisement_utc_s']} simule={'oui' if d['simule'] else 'non'}")
            return 1 if d["arret"] else 0
        elif len(argv) in (5, 6) and argv[0] == "calendrier":
            r = verifier_calendrier_v3(s2._lire_json(argv[1]), argv[2], argv[3], argv[4], date.fromisoformat(argv[5]) if len(argv) == 6 else None)
            print(f"fin_go_utc_s={r['fin_go_utc_s']} dernier_jour_creation={r['dernier_jour_creation']} echeance_go={r['echeance_go']}")
        elif len(argv) in (9, 10) and argv[0] == "surveillance":
            texte = Path(argv[2]).read_text(encoding="utf-8") if Path(argv[2]).is_file() else ""
            now = _nombre(argv[3], "maintenant")
            d = depense_cumulee_v3(argv[1], argv[4], argv[5], argv[6], argv[7], argv[8], now, argv[9] if len(argv) > 9 else None)
            print(decider_surveillance_v3(texte, now, d))
        elif argv and argv[0] in ("offre", "instances"):
            return s2.main(argv)
        else:
            print("usage : go | depense | calendrier | surveillance | offre | instances (voir l'en-tête)", file=sys.stderr)
            return 2
    except GardeSession as e:
        print(str(e))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
