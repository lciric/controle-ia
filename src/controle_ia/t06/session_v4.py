"""Chaîne de session de T0.6, v4 (C-V5-1 de la contre-lecture du lanceur v4, R-1657 ; nom neuf, R12 : `session_v3.py` reste tel quel).
Sous vastai 1.8.3, `search offers "id=<OFFRE>" --storage <Go> --raw` rend une liste VIDE et l'identifiant d'une même offre change d'une
recherche à l'autre (R-577, R-578 ; confirmé en réel par la fille 6, 7 novembre) : la v4 refuserait toute location. La v5 ne relit plus
une offre par son identifiant ; elle choisit l'offre dans la **liste filtrée**, relue juste avant la création, comme
`lancer_banque_t05_v3.sh` (R-578).

    python -I -m controle_ia.t06.session_v4 filtre CONFIG.json CARTE(course|relance)
        imprime le filtre de la recherche (langage de requête de vastai) tiré de la configuration : une carte, louable, nom de carte,
        mémoire vive en Go, cœurs effectifs, disque, prix horaire maximal de la carte.
    python -I -m controle_ia.t06.session_v4 choisir OFFRES.json CONFIG.json CARTE [MACHINES_EXCLUES (séparées par des virgules)]
        parcourt la liste dans l'ordre du prix croissant (carte + stockage, puis identifiant) et rend la **première** offre qui passe
        `session_v2.verifier_offre` (carte, mémoire de carte, une seule carte, mémoire vive, cœurs, disque, prix de la carte, du stockage
        et du téléchargement, louable) et dont la machine n'est pas exclue ; écrit « id=… rang=N … » (prix lus dans LA LISTE) ; liste
        vide, ou aucune offre conforme : code 1 et le motif de chaque refus (les trois premiers).
    autres sous-commandes : celles de `session_v3`.
Code 0 ; 1 avec un motif ; 2 sur un usage faux.
"""
from __future__ import annotations

import sys

from . import session_v2 as s2
from . import session_v3 as s3
from .session import GardeSession


def filtre_recherche(config: dict, carte: str) -> str:
    if carte not in ("course", "relance"):
        raise GardeSession("carte : « course » ou « relance »")
    c, b = config["carte"][carte], config["offre"]
    nom = str(c["nom_offre"]).replace(" ", "_")
    ram_go = int(-(-b["memoire_vive_min_mo"] // 1000))
    return (f"num_gpus=1 rentable=true gpu_name={nom} cpu_ram>={ram_go} cpu_cores_effective>={b['coeurs_effectifs_min']} "
            f"disk_space>={b['disque_min_go']} dph_total<={c['prix_max_usd_h']}")


def choisir_offre(offres, config: dict, carte: str, machines_exclues=()) -> dict:
    if isinstance(offres, dict) and "offers" in offres:
        offres = offres["offers"]
    if not isinstance(offres, list):
        raise GardeSession("liste d'offres illisible")
    if not offres:
        raise GardeSession("recherche filtrée : liste VIDE (aucune offre ne respecte le filtre)")
    exclues = {str(m) for m in machines_exclues}

    def cle(o):
        try:
            return (float(o.get("dph_total", 1e9)) + float(o.get("storage_total_cost", 0.0)), int(o.get("id", 0)))
        except (TypeError, ValueError):
            return (1e18, 0)
    refus = []
    for rang, o in enumerate(sorted((o for o in offres if isinstance(o, dict)), key=cle), 1):
        if str(o.get("machine_id")) in exclues:
            refus.append(f"rang {rang} : machine {o.get('machine_id')} déjà refusée")
            continue
        try:
            r = s2.verifier_offre([o], config, carte)
        except GardeSession as e:
            refus.append(f"rang {rang} : {e}")
            continue
        r["rang"] = rang
        return r
    raise GardeSession(f"aucune offre conforme sur {len(offres)} : " + " ; ".join(refus[:3]))


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 3 and argv[0] == "filtre":
            print(filtre_recherche(s2._lire_json(argv[1]), argv[2]))
        elif len(argv) in (4, 5) and argv[0] == "choisir":
            r = choisir_offre(s2._lire_json(argv[1]), s2._lire_json(argv[2]), argv[3], argv[4].split(",") if len(argv) == 5 and argv[4] else ())
            print(f"id={r['id']} rang={r['rang']} machine={r['machine_id']} prix_carte={r['prix_carte']:.4f} prix_stockage={r['prix_stockage']:.4f} "
                  f"telechargement={r['telechargement']:.4f} telechargement_forfait={r['telechargement_forfait_usd']:.4f} carte={r['carte']}")
        else:
            return s3.main(argv)
    except GardeSession as e:
        print(str(e))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
