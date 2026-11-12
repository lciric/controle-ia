"""Chaîne de session de T0.6, v8 (lanceur v9, R-1692 ; nom neuf, R12 : `session_v7.py` et les précédents restent tels quels).

Seule différence avec `session_v7.py` : **le stockage n'est plus compté deux fois** (défaut E2-2 de l'épreuve du 7 novembre). Avec
`vastai search offers … --storage <Go>`, la clé `dph_total` de l'offre INCLUT déjà le stockage demandé (`storage_total_cost`). Les v2 à v7
lisaient `prix_carte = dph_total` puis ajoutaient `prix_stockage = storage_total_cost` : 0,4034 USD/h estimés contre 0,362 facturés
(valeurs réelles : dph_total 0,3617, storage_total_cost 0,041667 ; carte seule 0,320 + disque 0,042). La v8 rend
`prix_carte = dph_total − storage_total_cost` et `prix_stockage = storage_total_cost` : la somme que lisent la garde de dépense et la
surveillance est exactement `dph_total`. Le tri des offres se fait aussi sur `dph_total` seul (avant : `dph_total + storage_total_cost`).
Le plafond horaire de la configuration (`prix_max_usd_h`) reste vérifié sur `dph_total`, comme avant (lecture prudente, inchangée).
Une offre dont `dph_total − storage_total_cost` n'est pas strictement positif est refusée (carte sans prix lisible).

Autres différences (contre-lecture Opus de la v8, R-1693 ; R-1694, R-1695) : (2) `instance_seule` : un objet d'erreur sans `id` (`{"success": false, …}`) ou un texte
d'erreur n'est PAS une absence ; l'absence n'est conclue que sur une liste NON vide qui ne contient pas l'identifiant, un objet portant un autre `id`, ou un texte/une erreur
JSON dont le statut vaut exactement 404 avec un message exact (« not found », « no such instance », « does not exist ») ; plus de recherche de « 404 » comme sous-chaîne ;
une réponse vide (`[]`, `{}`, `null`) n'est pas non plus une absence (même défaut que l'inventaire vide, R-1683) ; (3) `NaN` et toute valeur non finie de `cuda_max_good`
sont refusés par la garde locale ; (4) le filtre de recherche porte `gpu_ram>=N` avec N = partie entière de `memoire_carte_min_mo / 1024` : dans la requête de Vast,
`gpu_ram` se compte en **Go** (établi sans dépense par la fille 6, R-1695 : `gpu_ram>=79` garde l'unique 80 Go, `gpu_ram>=79000` ne rend rien) alors que la clé brute rendue
reste en Mo ; la garde locale reste en Mo. Pour 80 000 Mo : N = 78 (40 960 Mo = 40 Go refusé, 81 920 Mo accepté).

    python -I -m controle_ia.t06.session_v8 choisir OFFRES.json CONFIG.json CARTE [MACHINES_EXCLUES]   (comme la v7, prix corrigés)
    python -I -m controle_ia.t06.session_v8 plafond PLAFOND_USD DEPENSE_ANTERIEURE_DES_AUTRES_EPREUVES_USD   (R-1696 : plafond d'épreuve de la configuration, borné par le reste du GO)
    autres sous-commandes : celles de `session_v7`.
"""
from __future__ import annotations

import json
import math
import re
import sys

from . import session_v2 as s2
from . import session_v7 as s7
from .session import GardeSession

CUDA_MAX_GOOD_MIN = s7.CUDA_MAX_GOOD_MIN
FIABILITE_MIN_OFFRE = s7.FIABILITE_MIN_OFFRE
INET_DOWN_MIN_MBPS = s7.INET_DOWN_MIN_MBPS


def filtre_recherche(config: dict, carte: str) -> str:
    """Filtre de la v7 plus la clause de mémoire de carte, en Go (R-1694, R-1695)."""
    base = s7.filtre_recherche(config, carte)
    mo = config["carte"][carte]["memoire_carte_min_mo"]
    if isinstance(mo, bool) or not isinstance(mo, (int, float)) or not math.isfinite(mo) or mo <= 0:
        raise GardeSession(f"memoire_carte_min_mo illisible ({mo!r})")
    go = int(mo // 1024)
    if go < 1:
        raise GardeSession(f"memoire_carte_min_mo {mo} < 1 Go")
    nom = str(config["carte"][carte]["nom_offre"]).replace(" ", "_")
    marque = f"gpu_name={nom} "
    if base.count(marque) != 1:
        raise GardeSession("filtre de la v7 inattendu : clause gpu_name introuvable")
    return base.replace(marque, f"{marque}gpu_ram>={go} ")


def instance_seule(texte: str, ident: str) -> bool:
    """Réponse de `vastai show instance <ID> --raw`. Vrai : l'instance répond. Faux : ABSENCE établie. GardeSession : tout le reste (non concluant)."""
    brut = texte.strip()
    if not brut:
        raise GardeSession("réponse de show instance vide")
    try:
        v = json.loads(brut)
    except ValueError:
        if _dit_introuvable(brut):
            return False
        raise GardeSession("réponse de show instance illisible")
    if isinstance(v, dict) and "instances" in v:
        v = v["instances"]
    if isinstance(v, dict):
        if "id" in v:
            return str(v.get("id")) == str(ident)                       # un autre identifiant : l'instance demandée n'est pas celle-là
        if _statut_404(v) and any(_dit_introuvable(str(v.get(k, ""))) for k in ("error", "msg", "message", "detail")):
            return False
        raise GardeSession("réponse de show instance sans id (objet d'erreur ou inconnu) : non concluante")
    if isinstance(v, list) and v and all(isinstance(i, dict) and "id" in i for i in v):
        return any(str(i.get("id")) == str(ident) for i in v)
    raise GardeSession("réponse de show instance vide ou illisible : non concluante")


def _statut_404(v: dict) -> bool:
    return any(str(v.get(k)).strip() == "404" for k in ("status", "status_code", "code", "http_status"))


_INTROUVABLE = re.compile(r"^(error[: ]*)?(http )?(404[: ]*)?(instance )?(\d+ )?(not found|no such instance|does not exist)$")


def _dit_introuvable(texte: str) -> bool:
    t = re.sub(r"[\s.\"']+$", "", texte.strip().lower())
    return bool(_INTROUVABLE.match(t))


GO_EPREUVES_USD = "5"        # GO-2026-11-06-01 : 5 USD pour E2 et E3 cumulés
MARGE_GO_USD = "0.1"         # réserve : plafond d'épreuve + dépense antérieure des autres épreuves ≤ 5 − 0,1 = 4,9 (condition écrite dans les ordres)


def verifier_plafond_epreuve(plafond, anterieures) -> str:
    """R-1696 : le plafond d'une épreuve est lu dans sa configuration (plus de liste fermée 1,5 ou 3,5) mais borné par le reste du GO :
    0 < plafond et plafond + dépense réelle et finale des autres épreuves ≤ 5 − 0,1. Décimaux exacts (0,6 + 4,3 = 4,9 passe, 4,31 ne passe pas)."""
    from decimal import Decimal, InvalidOperation
    try:
        p, a = Decimal(str(plafond)), Decimal(str(anterieures))
    except InvalidOperation:
        raise GardeSession(f"plafond ({plafond!r}) ou dépense antérieure ({anterieures!r}) illisible")
    if not (p.is_finite() and a.is_finite()):
        raise GardeSession("plafond ou dépense antérieure non fini")
    if p <= 0 or a < 0:
        raise GardeSession(f"plafond {p} (> 0 exigé) ou dépense antérieure {a} (≥ 0 exigé)")
    limite = Decimal(GO_EPREUVES_USD) - Decimal(MARGE_GO_USD)
    if p + a > limite:
        raise GardeSession(f"plafond d'épreuve {p} + dépense antérieure {a} = {p + a} > {limite} (reste du GO de {GO_EPREUVES_USD} USD, marge {MARGE_GO_USD})")
    return f"plafond d'épreuve {p} + dépense antérieure {a} = {p + a} ≤ {limite}"


def corriger_prix(r: dict) -> dict:
    """`dph_total` (lu dans `prix_carte` par `verifier_offre`) inclut déjà le stockage : on le sépare."""
    total, sto = float(r["prix_carte"]), float(r["prix_stockage"])
    carte = total - sto
    if not (carte > 0):
        raise GardeSession(f"offre {r['id']} : dph_total {total} − stockage {sto} = {carte} USD/h, carte sans prix lisible")
    r = dict(r)
    r["prix_carte"], r["dph_total"] = carte, total
    return r


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
            return (float(o.get("dph_total", 1e9)), int(o.get("id", 0)))
        except (TypeError, ValueError):
            return (1e18, 0)
    refus = []
    for rang, o in enumerate(sorted((o for o in offres if isinstance(o, dict)), key=cle), 1):
        if str(o.get("machine_id")) in exclues:
            refus.append(f"rang {rang} : machine {o.get('machine_id')} déjà refusée")
            continue
        try:
            cuda = float(o["cuda_max_good"])
        except (KeyError, TypeError, ValueError):
            refus.append(f"rang {rang} : cuda_max_good absent ou illisible (garde locale)")
            continue
        if not math.isfinite(cuda):
            refus.append(f"rang {rang} : cuda_max_good non fini ({cuda}) (garde locale)")
            continue
        if cuda < CUDA_MAX_GOOD_MIN:
            refus.append(f"rang {rang} : cuda_max_good {cuda} < {CUDA_MAX_GOOD_MIN} (pilote trop ancien pour torch cu130)")
            continue
        try:
            r = corriger_prix(s2.verifier_offre([o], config, carte))
        except GardeSession as e:
            refus.append(f"rang {rang} : {e}")
            continue
        r["rang"] = rang
        r["cuda_max_good"] = cuda
        return r
    raise GardeSession(f"aucune offre conforme sur {len(offres)} : " + " ; ".join(refus[:3]))


def main(argv: list[str]) -> int:
    if len(argv) == 3 and argv[0] == "plafond":
        try:
            print(verifier_plafond_epreuve(argv[1], argv[2]))
        except GardeSession as e:
            print(str(e))
            return 1
        return 0
    if len(argv) == 3 and argv[0] == "filtre":
        try:
            print(filtre_recherche(s2._lire_json(argv[1]), argv[2]))
        except GardeSession as e:
            print(str(e))
            return 1
        return 0
    if len(argv) == 3 and argv[0] == "seule":
        try:
            texte = open(argv[1], encoding="utf-8", errors="replace").read()
            absente = not instance_seule(texte, argv[2])
        except OSError as e:
            print(f"réponse de show instance illisible ({e.__class__.__name__})")
            return 2
        except GardeSession as e:
            print(str(e))
            return 2
        if absente:
            print(f"instance {argv[2]} INTROUVABLE")
            return 4
        print(f"instance {argv[2]} répond")
        return 0
    if len(argv) in (4, 5) and argv[0] == "choisir":
        try:
            r = choisir_offre(s2._lire_json(argv[1]), s2._lire_json(argv[2]), argv[3], argv[4].split(",") if len(argv) == 5 and argv[4] else ())
        except GardeSession as e:
            print(str(e))
            return 1
        print(f"id={r['id']} rang={r['rang']} machine={r['machine_id']} prix_carte={r['prix_carte']:.6f} prix_stockage={r['prix_stockage']:.6f} "
              f"dph_total={r['dph_total']:.6f} telechargement={r['telechargement']:.4f} telechargement_forfait={r['telechargement_forfait_usd']:.4f} "
              f"cuda_max_good={r['cuda_max_good']} carte={r['carte']}")
        return 0
    return s7.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
