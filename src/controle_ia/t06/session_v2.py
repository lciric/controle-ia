"""Chaîne de session de T0.6, v2 (contre-lecture du lanceur v1, C08, C09, C12, C15 ; nom neuf, R12 : `session.py` reste tel
quel). Bibliothèque standard seule ; aucun appel au réseau ni à l'outil de location.

    python -I -m controle_ia.t06.session_v2 go REGISTRE_GO.md [AAAA-MM-JJ]
        comme la v1 (`session.verifier_go`).
    python -I -m controle_ia.t06.session_v2 depense PRIX_CARTE PRIX_STOCKAGE CREE_LE_S ANTERIEURE_USD TELECHARGEMENT_USD [MAINTENANT_S] [FACTURE]
        Dépense cumulée de la course = dépense des tentatives antérieures (relevée au registre des dépenses, H200 comprise)
        + forfait de téléchargement + heures écoulées × (carte + stockage) ; la facture relevée remplace la part de
        l'instance si elle est plus grande. Écrit « cumulee=… plafond=200 arret=oui|non epuisement_utc_s=… » : l'heure où
        le plafond est épuisé au prix de l'offre, calculée à la création et passée à l'amorce (`DEPENSE_EPUISEE_UTC_S`).
    python -I -m controle_ia.t06.session_v2 offre OFFRE.json CONFIG.json CARTE(course|relance)
        Vérifie une offre relue (`vastai search offers "id=<OFFRE>" --raw`) contre la configuration : nom de carte, mémoire
        de carte, une seule carte, mémoire vive, cœurs effectifs, disque, prix de la carte (≤ prix maximal de la carte
        nommée), stockage et téléchargement ; écrit « id=… prix_carte=… prix_stockage=… telechargement=… ».
    python -I -m controle_ia.t06.session_v2 instances INSTANCES.json ETIQUETTE
        Refuse toute instance du programme (étiquette qui commence par ETIQUETTE) encore présente sur le compte.
    python -I -m controle_ia.t06.session_v2 calendrier CONFIG.json REGISTRE_GO.md [AAAA-MM-JJ]
        L11 : la fin du GO de la configuration (`calendrier.fin_go_utc`) est le lendemain à 00:00 UTC de l'échéance du GO
        lue au registre ; le dernier jour de création précède la fin du GO ; le jour donné (défaut : aujourd'hui) ne
        dépasse pas le dernier jour de création. Écrit « fin_go_utc_s=… dernier_jour_creation=… echeance_go=… ».
    python -I -m controle_ia.t06.session_v2 surveillance JOURNAL MAINTENANT_S PRIX_CARTE PRIX_STOCKAGE CREE_LE_S ANTERIEURE TELECHARGEMENT [FACTURE]
        comme la v1, avec le cumul de la course.
Code 0 ; 1 avec un motif sur la dernière ligne ; 2 sur un usage faux.
"""
from __future__ import annotations

import json
import math
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from .session import GardeSession, _nombre, decider_surveillance, verifier_go

PLAFOND_USD = 200.0


def depense_cumulee_v2(prix_carte, prix_stockage, cree_le_s, anterieure_usd, telechargement_usd, maintenant_s=None,
                       facture_usd=None) -> dict:
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
    reste = PLAFOND_USD - ant - tel
    epuisement = cree + reste / (p_c + p_s) * 3600.0 if reste > 0 else cree
    return {"cumulee_usd": round(cumulee, 4), "instance_usd": round(instance, 4), "anterieure_usd": ant, "telechargement_usd": tel,
            "heures": round(h, 4), "plafond_usd": PLAFOND_USD, "arret": cumulee >= PLAFOND_USD,
            "epuisement_utc_s": int(math.floor(epuisement))}


def _lire_json(chemin) -> object:
    try:
        return json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise GardeSession(f"{chemin} : JSON illisible ({type(e).__name__})") from None


def _entier(v) -> bool:
    return isinstance(v, int) and not isinstance(v, bool)


def _fini(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def verifier_offre(offres, config: dict, carte: str) -> dict:
    """Une offre relue (liste d'une offre, ou dictionnaire) contre `config["carte"][carte]` et `config["offre"]`."""
    if carte not in ("course", "relance"):
        raise GardeSession("carte : « course » ou « relance »")
    if isinstance(offres, dict) and "offers" in offres:
        offres = offres["offers"]
    if isinstance(offres, dict):
        offres = [offres]
    if not isinstance(offres, list) or len(offres) != 1 or not isinstance(offres[0], dict):
        raise GardeSession(f"offre relue : exactement une offre attendue, {len(offres) if isinstance(offres, list) else 'forme inconnue'}")
    o = offres[0]
    c, b = config["carte"][carte], config["offre"]
    if not _entier(o.get("id")):
        raise GardeSession("offre : identifiant illisible")
    if o.get("gpu_name") != c["nom_offre"]:
        raise GardeSession(f"offre {o['id']} : carte {o.get('gpu_name')!r} ≠ {c['nom_offre']!r} ({carte})")
    if not (_fini(o.get("gpu_ram")) and o["gpu_ram"] >= c["memoire_carte_min_mo"]):
        raise GardeSession(f"offre {o['id']} : mémoire de carte {o.get('gpu_ram')} < {c['memoire_carte_min_mo']} Mo")
    if not (_entier(o.get("num_gpus")) and o["num_gpus"] == 1):
        raise GardeSession(f"offre {o['id']} : {o.get('num_gpus')} carte(s), une seule attendue")
    if not (_fini(o.get("cpu_ram")) and o["cpu_ram"] >= b["memoire_vive_min_mo"]):
        raise GardeSession(f"offre {o['id']} : mémoire vive {o.get('cpu_ram')} < {b['memoire_vive_min_mo']} Mo")
    if not (_fini(o.get("cpu_cores_effective")) and o["cpu_cores_effective"] >= b["coeurs_effectifs_min"]):
        raise GardeSession(f"offre {o['id']} : {o.get('cpu_cores_effective')} cœurs effectifs < {b['coeurs_effectifs_min']}")
    if not (_fini(o.get("disk_space")) and o["disk_space"] >= b["disque_min_go"]):
        raise GardeSession(f"offre {o['id']} : disque {o.get('disk_space')} < {b['disque_min_go']} Go")
    prix = o.get("dph_total")
    if not (_fini(prix) and 0 < prix <= c["prix_max_usd_h"]):
        raise GardeSession(f"offre {o['id']} : prix {prix} USD/h hors de ]0, {c['prix_max_usd_h']}] ({c['nom']})")
    sto = o.get("storage_total_cost")
    if not (_fini(sto) and 0 <= sto <= b["stockage_max_usd_h"]):
        raise GardeSession(f"offre {o['id']} : stockage {sto} USD/h hors de [0, {b['stockage_max_usd_h']}]")
    tel = o.get("inet_down_cost")
    if not (_fini(tel) and 0 <= tel <= b["telechargement_max_usd_go"]):
        raise GardeSession(f"offre {o['id']} : téléchargement {tel} USD/Go hors de [0, {b['telechargement_max_usd_go']}]")
    if o.get("rentable") is False:
        raise GardeSession(f"offre {o['id']} : non louable")
    forfait = float(tel) * float(b["telechargement_go_prevu"])
    return {"id": int(o["id"]), "prix_carte": float(prix), "prix_stockage": float(sto), "telechargement": float(tel),
            "telechargement_forfait_usd": forfait, "carte": c["nom"], "machine_id": o.get("machine_id"), "host_id": o.get("host_id")}


def verifier_calendrier(config: dict, registre_go, jour: date | None = None) -> dict:
    """L11 : calendrier de la configuration contre le registre des GO (bibliothèque standard, lecture sans le paquet)."""
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
    go = verifier_go(registre_go, jour)
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


def verifier_instances(instances, etiquette: str) -> dict:
    if isinstance(instances, dict) and "instances" in instances:
        instances = instances["instances"]
    if instances is None:
        instances = []
    if not isinstance(instances, list):
        raise GardeSession("inventaire des instances illisible")
    presentes = []
    for i in instances:
        if not isinstance(i, dict):
            raise GardeSession("inventaire : entrée illisible")
        if str(i.get("label") or "").startswith(etiquette):
            presentes.append(f"{i.get('id')} ({i.get('actual_status')}, {i.get('cur_state')})")
    if presentes:
        raise GardeSession(f"instance(s) du programme déjà sur le compte : {', '.join(presentes)} : aucune création")
    return {"instances_du_programme": 0, "total": len(instances)}


def main(argv: list[str]) -> int:
    try:
        if len(argv) in (2, 3) and argv[0] == "go":
            r = verifier_go(argv[1], date.fromisoformat(argv[2]) if len(argv) == 3 else None)
            print(f"{r['go']} conforme (plafond {r['plafond_usd']:g} USD, {r['accorde']} → {r['echeance']})")
        elif len(argv) in (6, 7, 8) and argv[0] == "depense":
            d = depense_cumulee_v2(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6] if len(argv) > 6 else None,
                                   argv[7] if len(argv) > 7 else None)
            print(f"cumulee={d['cumulee_usd']:.4f} instance={d['instance_usd']:.4f} heures={d['heures']:.4f} plafond={PLAFOND_USD:g} "
                  f"arret={'oui' if d['arret'] else 'non'} epuisement_utc_s={d['epuisement_utc_s']}")
            return 1 if d["arret"] else 0
        elif len(argv) == 4 and argv[0] == "offre":
            r = verifier_offre(_lire_json(argv[1]), _lire_json(argv[2]), argv[3])
            print(f"id={r['id']} prix_carte={r['prix_carte']:.4f} prix_stockage={r['prix_stockage']:.4f} "
                  f"telechargement={r['telechargement']:.4f} telechargement_forfait={r['telechargement_forfait_usd']:.4f} carte={r['carte']}")
        elif len(argv) == 3 and argv[0] == "instances":
            r = verifier_instances(_lire_json(argv[1]), argv[2])
            print(f"aucune instance du programme ({r['total']} instance(s) sur le compte)")
        elif len(argv) in (3, 4) and argv[0] == "calendrier":
            r = verifier_calendrier(_lire_json(argv[1]), argv[2], date.fromisoformat(argv[3]) if len(argv) == 4 else None)
            print(f"fin_go_utc_s={r['fin_go_utc_s']} dernier_jour_creation={r['dernier_jour_creation']} echeance_go={r['echeance_go']}")
        elif len(argv) in (8, 9) and argv[0] == "surveillance":
            texte = Path(argv[1]).read_text(encoding="utf-8") if Path(argv[1]).is_file() else ""
            now = _nombre(argv[2], "maintenant")
            d = depense_cumulee_v2(argv[3], argv[4], argv[5], argv[6], argv[7], now, argv[8] if len(argv) > 8 else None)
            print(decider_surveillance(texte, now, d))
        else:
            print("usage : go | depense | offre | instances | calendrier | surveillance (voir l'en-tête)", file=sys.stderr)
            return 2
    except GardeSession as e:
        print(str(e))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
