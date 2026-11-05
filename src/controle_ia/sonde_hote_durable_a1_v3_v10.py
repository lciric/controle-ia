#!/usr/bin/env python3
"""Sonde de l'hôte durable d'A1-v3, **version 10** (GO-2026-11-05-01, 1 USD).

Version 10 (R12 : v1 à v9 inchangées) : la v9, plus **seulement** ce qu'impose le résultat réel de la sonde v9 (rapport de la fille
`rapport-sonde-a1-v3-v9-2026-11-05-0201.md`) : machine louée, minuterie qui détruit, versement fait, mais aucune course factice
(« REFUS : registres/go.md illisible au commit … »). (a) Sur la machine, le registre est lu sur `canal/conv-audit-n04` au commit que
pose le pilote (`--commit-registre`, variable `COMMIT_REGISTRE`), comme la vraie course : commit sur la branche, aucun doublon (le
lecteur gelé les refuse), GO-2026-11-05-01 à 1 USD par la garde de ce commit ; fichiers lus avec l'aide d'identification. Le pilote,
lui, garde la garde de `main` sur le registre de `main`. (b) Relevés : facturation par le pilote (`facturation` : `vastai show
instance` filtré à `actual_status`, `dph_total`, `disk_usage`, `storage_cost`), et pilote de carte sur la machine (`nvidia-smi -L`,
une ligne, s'il existe). Ce qui suit décrit la v9 :

Version 9 (R12 : v1 à v8 inchangées) : la v8, plus **seulement** ce qu'impose le fait établi par la fille le 5 novembre 2026
(00:15 et 00:16 UTC, lecture seule) : sur Vast, toutes les offres `num_gpus=0` sont des volumes de stockage (`resource_type`
« disk ») et ne se louent pas comme machines. (a) Vérification d'offre propre : `resource_type` « gpu » exigé (« disk » refusé),
`num_gpus` = 1, `cpu_ram` ≥ 8 000 Mo (0 refusé ; l'exception « non renseignée » de la v5 est retirée), cœurs ≥ 4, disque ≥ 30,
fiabilité ≥ 0,98, prix ≤ 0,40 USD/h ; la mémoire réelle reste relevée sur la machine. (b) GO exigé : GO-2026-11-05-01, plafond
exactement 1 USD sur la ligne ; GO-2026-11-04-09 et -06 refusés. La carte n'est pas utilisée : aucun pilote, aucun calcul sur elle.
Ce qui suit décrit la v8 :

Version 8 (R12 : v1 à v7 inchangées) : la v7, plus **seulement** ce qu'imposent les faits constatés par la fille le 4 novembre 2026
(23:35 et 23:38 UTC) : avec `--raw`, `vastai` 1.8.3 écrit ses refus sur la **sortie d'erreur**, avec le **code 0** et une sortie
standard vide (forme `{'success': False, 'error': True, 'msg': 'error 404/3603: no_such_ask …'}`). (a) La création capture les
deux sorties ; `categoriser_reponse` lit la sortie standard d'abord, puis la sortie d'erreur, ne se fie jamais au code seul (un code
0 sans contrat est un refus) et extrait `error` et `msg` même d'un texte mal formé ; rien d'autre que la catégorie et ces deux champs
masqués n'est écrit ; les mots du certificat restent cherchés dans la sortie d'erreur. (b) Sur « no_such_ask », `louer` essaie au
plus 4 autres offres conformes, par prix croissant, chacune revérifiée, garde de dépense recalculée, chaque refus journalisé avec le
compte ; au cinquième « no_such_ask », refus final sans marqueur. Ce qui suit décrit la v7 :

Version 7 (R12 : v1 à v6 inchangées) : la v6, plus **seulement** ce qu'imposent les faits constatés par la fille le 4 novembre 2026
(23:09 et 23:11 UTC : deux « CREATION_INCERTAINE : réponse illisible », aucune instance créée, l'offre visée disparue ensuite).
(a) La réponse de `vastai create` est réduite à une catégorie sûre, écrite au journal : identifiant de contrat ; « no_such_ask » ;
« erreur Vast » avec les seuls champs `error` et `msg` (JSON ou représentation Python), tronqués à 200 caractères et masqués ;
sinon « illisible » avec la longueur seule. « no_such_ask » et « erreur Vast » avec `success` faux sont des refus sans marqueur de
création incertaine (Vast dit que rien n'est créé) ; les autres cas le gardent. (b) `controler` : `git ls-remote` reçoit les
variables du mandataire ; un échec de `ls-remote` rend le code 6 (« recontrôler »), jamais « pas de signe de vie ». (c) Les
longueurs de la commande de création (`--args`, `--env`, commande entière) sont écrites au journal. Ce qui suit décrit la v6 :

Version 6 (R12 : v1 à v5 inchangées) : la v5, plus **seulement** ce qu'impose le fait constaté par la fille le 4 novembre 2026
(22:48 et 22:51 UTC, rien créé) : son trafic sortant passe par un mandataire qui réémet les certificats, et `vastai` échouait
(« SSLCertVerificationError ») faute des variables du mandataire. (a) `ClientPilote._lancer` transmet aussi `HTTPS_PROXY`,
`HTTP_PROXY`, `NO_PROXY`, `SSL_CERT_FILE` et `REQUESTS_CA_BUNDLE` s'ils sont présents (non vides) dans l'environnement reçu, aucune
autre variable ; leurs valeurs sont masquées comme les secrets. (b) Un échec de `vastai` dont la sortie d'erreur contient
« CERTIFICATE_VERIFY_FAILED » ou « SSLCertVerificationError » est un refus « appel non parvenu à Vast (certificat) », sans marqueur
de création incertaine ; seule la présence de ces mots est lue, la sortie d'erreur n'est jamais écrite. Ce qui suit décrit la v5 :

Version 5 (R12 : `hote_durable_a1_v3.py` et les v1 à v4 inchangés) : la v4, plus **seulement** ce qu'impose le fait constaté
par la fille le 4 novembre 2026 vers 22:31 UTC (lecture seule) : sur Vast, les offres sans carte rendent `cpu_ram` = 0 (champ
non renseigné). (a) Vérification d'offre propre à la sonde (`verifier_offre_sonde`) : `cpu_ram` à 0 ou absent vaut « non
renseigné » et n'est accepté que si `cpu_cores_effective` ≥ 4 ; une valeur strictement positive sous 8 000 est refusée ; tous les
autres critères sont inchangés ; « mémoire non renseignée par Vast » est écrit au journal. (b) L'amorce relève la mémoire réelle
de la machine (`/proc/meminfo`, MemTotal) dans `sonde-v10-memoire.txt`, versé avec la sortie ; sous 2 Go, elle s'arrête
proprement (code 2 ; la minuterie détruit). Ce qui suit décrit la v4, reprise telle quelle :

Version 4 (R12 : v1, v2 et v3 inchangées) : la v3, plus **seulement** les corrections de `contre-lecture-sonde-v3.md`
(`92b5abfc…`) : **M-1** (délai dépassé de `vastai` rendu en `Refus` sans la ligne de commande ni l'environnement, création
marquée incertaine) ; **m-1** (tout échec de `vastai create` marque la création incertaine ; seconde location refusée tant que le
marqueur existe) ; **m-2, f-1** (amorce, `git` et chaque `apt-get` sous `timeout` borné par la fin de vie ; l'installation de
`curl` passe après la minuterie) ; **f-2** (attente finale du principal comptée dans la borne) ; **f-3** (en tir, premier contrôle à
T0 + 45) ; **f-6** (code 6 de `controler` : délai dépassé). Ce qui suit décrit la v3, reprise telle quelle :

Version 3 (R12 : v1 et v2 inchangées). Elle reprend la v2 (corrections de `contre-lecture-sonde-v1.md` : minuterie de destruction
lancée en tout premier, `-y`, `VAST_API_KEY` par son nom, clone partiel, branches orphelines, étiquette contrôlée, instances
58936096, 58936099 et 58936100 jamais touchées) et porte `contre-lecture-sonde-v2.md` (`a8fc1079…`, « lançable après
corrections ») :

- **M-A** — `controler` rend 5 (« listée : recontrôler ») et non 0 quand l'instance est encore listée ; contrôles à T0 + 40 et
  T0 + 70 min ; une machine listée 10 min après l'échéance finale est détruite par son identifiant, avec `-y`.
- **M-B** — le pilote pose dans le corps une **échéance absolue** `ECHEANCE_UTC_S` = création + 10 min + durée + marge ; la
  minuterie prend le minimum de cette échéance et de la sienne (départ du conteneur + durée + marge) : la machine est détruite au
  plus tard à l'échéance absolue, même si elle démarre tard ; borne écrite : prix × (10 min + durée + marge + 10 min) ≤ 0,50 USD.
  Le cas « jamais démarrée » (aucun processus sur la machine) reste borné par une session (`controler`), non par la machine.
- **m-a** — aucun « arrêt » de la machine, nulle part : l'arrêt tuerait la minuterie. La machine se détruit, même sans versement
  (données factices) ; si la destruction est refusée, elle laisse la minuterie recommencer ; la minuterie recommence le `DELETE`
  chaque minute jusqu'à la fin de vie du conteneur, sans repli `PUT stopped`.
- **m-b** — le processus principal ne sort qu'après la fin de la minuterie (attente bornée de 5 min après la fin de vie) : une
  reprise du conteneur après l'échéance détruit au lieu de sortir.
- **m-c** — `curl` exigé : installé avec `git` s'il manque ; absent, l'amorce refuse de partir (code 2, visible) et la minuterie
  passe par `python3` (bibliothèque standard), avec une alarme écrite.
- **m-d** — mode « tir de la minuterie » (`--tir-minuterie`) : la machine verse sans geste et la minuterie détruit, avec une marge
  courte ; essais du script de démarrage dans un espace de processus à part (`unshare -pf`).
- **f-a** — aucune sortie d'erreur de `vastai` lue ni écrite : en cas d'échec, le code seul.
- **f-b** — la ligne pour `registres/etat.md` renvoie à `controler`, qui contrôle l'étiquette.
- **f-d** — `sparse-checkout` de `scripts/` et `src/controle_ia/` avant le `checkout`, le tout sous `timeout`.
- **f-e** — crochets d'essai contrôlés (racine absolue, adresse en `https://`, marges entières), sinon valeurs par défaut.
- **f-f, f-g** — réserves : la facturation d'une instance « exited » et le sens de `--storage 30` sont à relever par la sonde.

Aucune clé d'Argon, aucun relais, aucun appel de modèle ; seul secret envoyé : le jeton GitHub (exposition acceptée pour la seule
sonde, R-1484).
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import importlib.util
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

try:  # paquet (essais) ou fichier seul (machine : `python3 -I -B …/sonde_hote_durable_a1_v3_v10.py`)
    from . import hote_durable_a1_v3 as h
    from . import sonde_hote_durable_a1_v3 as s1
except ImportError:
    _ici = Path(__file__).resolve().parent
    for _nom in ("hote_durable_a1_v3", "sonde_hote_durable_a1_v3"):
        _spec = importlib.util.spec_from_file_location(_nom, _ici / f"{_nom}.py")
        _m = importlib.util.module_from_spec(_spec)
        sys.modules[_nom] = _m
        _spec.loader.exec_module(_m)
    h, s1 = sys.modules["hote_durable_a1_v3"], sys.modules["sonde_hote_durable_a1_v3"]

VERSION = "sonde-hote-durable-a1-v3-v10"
GO_SONDE, MONTANT_GO_SONDE_USD = "GO-2026-11-05-01", 1.0  # v9 (b) : ligne du 5 novembre 2026, plafond 1 USD
ETIQUETTE = "sonde-a1-v3-v10"
BRANCHE = "donnees/sonde-hote-durable-a1-v3-v10"
BRANCHE_REFUS = "donnees/sonde-hote-durable-a1-v3-v10-refus"
BRANCHE_INTERROMPUE = "donnees/sonde-hote-durable-a1-v3-v10-interrompue"
BRANCHE_VIE = "donnees/sonde-hote-durable-a1-v3-v10-signe-de-vie"
AMORCE = "scripts/amorce_sonde_hote_durable_a1_v3_v10.sh"
MODULE = "src/controle_ia/sonde_hote_durable_a1_v3_v10.py"
PROTEGEES = (58936096, 58936099, 58936100)  # instances « R8 » de Lazar : jamais touchées
DUREE_DEFAUT_S, DUREE_MAX_S = 1200, 1800
MARGE_MINUTERIE_S = 1500          # 25 min après la durée de la sonde : installations, versement, destruction
VIE_APRES_ECHEANCE_S = 600        # le conteneur reste en vie 10 min après l'échéance, puis sort (repli : « exited »)
DEMARRAGE_MAX_S = 600             # part de l'échéance absolue réservée au démarrage (M-B : tenue par la minuterie)
MARGE_TIR_S = 600                 # mode « tir de la minuterie » (m-d) : marge courte après la durée de la sonde
ATTENTE_MINUTERIE_S = 300         # m-b : le principal attend la fin de la minuterie au plus 5 min après la fin de vie
RESERVE_VERSEMENT_S = 300         # la course factice s'arrête au plus tard 5 min avant l'échéance absolue
BORNE_SIGNE_DE_VIE_S = 1800       # T0 + 30 min : sans signe de vie, le pilote détruit (m2)
PLAFOND_SONDE_USD = 0.50
DELAI_GIT_S = 120
PROFONDEUR_CANAL = 200            # v10 (a) : historique récent de canal/conv-audit-n04 où chercher le commit du registre
CHAMPS_FACTURATION = ("actual_status", "dph_total", "disk_usage", "storage_cost")  # v10 (b) : seuls champs relevés
ESSAIS_NO_SUCH_ASK = 5            # v8 (b) : l'offre choisie et au plus 4 autres
DELAI_VASTAI_S = 300              # M-1 : délai d'un appel de `vastai` ; dépassé, `Refus` sans arguments ni environnement
# Liste commune à l'amorce v10 (f2) : même motif, même ordre.
CLES_INTERDITES = re.compile(r"^(CLE_ARGON|GEMINI.*|ANTHROPIC.*|OPENAI.*|MOONSHOT.*|KIMI.*|RR_.*API_KEY.*)$")
MOTIF_AMORCE = "CLE_ARGON|GEMINI*|ANTHROPIC*|OPENAI*|MOONSHOT*|KIMI*|RR_*API_KEY*"
VARIABLES_MANDATAIRE = ("HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY", "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE")  # v6 (a)
MOTS_CERTIFICAT = (b"CERTIFICATE_VERIFY_FAILED", b"SSLCertVerificationError")  # v6 (b) : présence lue, texte jamais écrit
SECRETS_PILOTE = ("GH_TOKEN", "VAST_API_KEY") + VARIABLES_MANDATAIRE  # v6 (a) : valeurs du mandataire masquées aussi
SECRETS_MACHINE = ("GH_TOKEN", "CONTAINER_API_KEY", "VAST_API_KEY")
FICHIERS_DEMARRAGE = ("sonde-v10-minuterie.txt", "sonde-v10-minuterie.log", "sonde-v10-temps.txt", "amorce-sonde-a1v3-v10.log",
                      "sonde-v10-memoire.txt")  # v5 (b) : mémoire réelle relevée par l'amorce
MEMOIRE_MIN_KB = 2 * 1024 * 1024  # v5 (b) : sous 2 Go de MemTotal, l'amorce s'arrête (la minuterie détruit)


def verifier_go_sonde(chemin_registre: Path, chemin_garde: Path, go_id: str, aujourd_hui: dt.date) -> dict:
    """v9 (b) : GO-2026-11-05-01 seul (GO-2026-11-04-09 et -06 refusés) ; la garde de `main` telle quelle (type, Lazar,
    validité, révocation, extensions), puis un plafond d'exactement 1 USD sur la ligne et sur chaque extension."""
    if go_id != GO_SONDE:
        raise h.Refus(f"GO {go_id} : la sonde v10 ne part que sous {GO_SONDE} (aucun autre GO)")
    garde = h.charger_garde(chemin_garde, chemin_registre)
    tampon = h.io.StringIO()
    try:
        with h.redirect_stderr(tampon):
            garde.decider(f"GO_ID={go_id} vastai create instance 0", aujourd_hui)
    except SystemExit as e:
        if e.code not in (0, None):
            raise h.Refus(f"garde de main : {tampon.getvalue().strip()}") from None
    lignes = h.lignes_du_go(chemin_registre, go_id)
    if not lignes:
        raise h.Refus(f"{go_id} absent du registre")
    for cellules in lignes:
        m = h.MONTANT.match(cellules[4])
        if not m or abs(float(m.group(1).replace(",", ".")) - MONTANT_GO_SONDE_USD) > 1e-9:
            raise h.Refus(f"{go_id} : plafond « {cellules[4]} » au lieu de exactement {MONTANT_GO_SONDE_USD:g} USD")
    return {"go": go_id, "lignes": len(lignes), "plafond_usd": MONTANT_GO_SONDE_USD,
            "registre_sha256": h.sha256_fichier(chemin_registre), "echeance": lignes[0][5]}


def _nombre(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def verifier_offre_sonde(offres: list[dict], offre_id: int) -> dict:
    """v9 (a) : sur Vast, les offres sans carte sont des volumes (`resource_type` « disk ») ; la sonde loue une machine à **une**
    carte : `resource_type` « gpu » exigé (« disk » refusé explicitement), `num_gpus` = 1, `cpu_ram` ≥ 8 000 Mo (0 refusé :
    l'exception « non renseignée » de la v5 est retirée), cœurs ≥ 4, disque ≥ 30 Go, fiabilité ≥ 0,98, prix ≤ 0,40 USD/h."""
    choisies = [o for o in offres if isinstance(o, dict) and o.get("id") == offre_id]
    if len(choisies) != 1:
        raise h.Refus(f"offre {offre_id} : {len(choisies)} dans la réponse de la recherche (une exigée)")
    o = choisies[0]
    rt = o.get("resource_type")
    if rt == "disk":
        raise h.Refus(f"offre {offre_id} : resource_type « disk » : volume de stockage, pas une machine")
    if rt != "gpu":
        raise h.Refus(f"offre {offre_id} : resource_type {rt!r} ; « gpu » exigé")
    if o.get("num_gpus") != 1 or isinstance(o.get("num_gpus"), bool):
        raise h.Refus(f"offre {offre_id} : {o.get('num_gpus')!r} carte(s) ; une exigée")
    prix = o.get("dph_total")
    if not _nombre(prix) or not (0 < prix <= h.PRIX_MAX_H_USD):
        raise h.Refus(f"offre {offre_id} : prix horaire {prix!r} hors de ]0 ; {h.PRIX_MAX_H_USD}] USD")
    for champ, mini in h.OFFRE_MIN.items():  # cpu_cores_effective 4, cpu_ram 8 000 Mo, disk_space 30, reliability 0,98
        v = o.get(champ)
        if not _nombre(v) or v < mini:
            raise h.Refus(f"offre {offre_id} : {champ} = {v!r} < {mini}")
    return {"id": offre_id, "dph_total": float(prix), **{k: o.get(k) for k in h.OFFRE_MIN}, "resource_type": rt,
            "num_gpus": 1, "gpu_name": o.get("gpu_name"), "geolocation": o.get("geolocation"),
            "machine_id": o.get("machine_id"), "memoire_non_renseignee": False}


def offre_la_moins_chere_sonde(offres: list[dict], offre_id: int) -> dict:
    """L'offre choisie, conforme (`verifier_offre_sonde`) et la moins chère des offres conformes de la réponse."""
    choisie = verifier_offre_sonde(offres, offre_id)
    conformes = []
    for x in offres:
        try:
            conformes.append(verifier_offre_sonde([x], x.get("id")))
        except h.Refus:
            continue
    moins = min(c["dph_total"] for c in conformes)
    if choisie["dph_total"] > moins + 1e-12:
        raise h.Refus(f"offre {offre_id} à {choisie['dph_total']} USD/h : une offre conforme est moins chère ({moins})")
    return choisie


def cles_de_modele(environ: dict) -> list[str]:
    return sorted(k for k, v in environ.items() if v and CLES_INTERDITES.match(k))


class RefusAvantAppel(h.Refus):
    """Refus d'une garde du pilote **avant** tout appel à `vastai` : aucune instance n'a pu naître (m-1 : pas de marqueur)."""


class RefusVastSansCreation(RefusAvantAppel):
    """v7 (a) : Vast répond lui-même que rien n'est créé (« no_such_ask », ou `success` faux avec `error`/`msg`) : aucun
    marqueur de création incertaine."""


class RefusNoSuchAsk(RefusVastSansCreation):
    """v8 (b) : Vast répond « no_such_ask » (offre plus disponible) : rien créé ; `louer` essaie l'offre conforme suivante."""


class RefusRecontroler(h.Refus):
    """v7 (b) : le contrôle n'a pas pu établir un fait (échec de `ls-remote`) : code 6, recontrôler ; jamais « pas de signe de
    vie »."""


class RefusCertificat(RefusAvantAppel):
    """v6 (b) : `vastai` n'a pas pu établir la connexion (certificat refusé) : l'appel n'est pas parvenu à Vast, aucune instance
    n'a pu naître, donc aucun marqueur de création incertaine."""


def cout_maximal_usd(dph: float, duree_s: int, marge_s: int = MARGE_MINUTERIE_S) -> float:
    """Borne (M-B), comptée depuis la création : la minuterie détruit au plus tard à l'échéance absolue (création + 10 min +
    durée + marge) ; si toutes ses destructions sont refusées, le conteneur sort 10 min plus tard (« exited » : réserve f-f).
    Hors borne : la machine qui ne lance jamais son script (aucun processus) — bornée par `controler`, donc par une session."""
    return dph * (DEMARRAGE_MAX_S + duree_s + marge_s + VIE_APRES_ECHEANCE_S + ATTENTE_MINUTERIE_S) / 3600  # f-2


def verifier_duree(brut) -> int:
    if not isinstance(brut, str) or not re.fullmatch(r"[0-9]{1,5}", brut or ""):
        raise h.Refus(f"DUREE_MAX_S {brut!r} : entier de secondes exigé")
    d = int(brut)
    if not (60 <= d <= DUREE_MAX_S):
        raise h.Refus(f"DUREE_MAX_S {d} hors de [60 ; {DUREE_MAX_S}]")
    return d


def verifier_plafond(dph: float, duree_s: int, plafond_usd: float = PLAFOND_SONDE_USD, marge_s: int = MARGE_MINUTERIE_S) -> float:
    c = cout_maximal_usd(dph, duree_s, marge_s)
    if c > plafond_usd:
        raise h.Refus(f"dépense de la sonde au plus {c:.4f} USD > plafond {plafond_usd} USD")
    return c


# --- script de démarrage du conteneur : la minuterie d'abord (M1), sans Python -------------------------------------------

MINUTERIE = r'''
ECH="$1"; R="$2"; API="$3"; FIN="$4"; J="$R/sonde-v10-minuterie.log"
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH, fin de vie $FIN" >> "$J"
echo "$$" > "$R/sonde-v10-minuterie.pid"
appel() {  # appel METHODE ADRESSE [CORPS] : imprime le corps (GET) ou le code HTTP ; curl, sinon python3 (m-c)
    if command -v curl >/dev/null 2>&1; then
        if [ "$1" = GET ]; then curl -sS -m 60 -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" "$2" 2>/dev/null
        else curl -sS -m 60 -o /dev/null -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" "$2" 2>/dev/null; fi
    else
        python3 -I -c 'import os, sys, urllib.request as u
m, a = sys.argv[1], sys.argv[2]
q = u.Request(a, method=m, headers={"Authorization": "Bearer " + os.environ.get("CONTAINER_API_KEY", "")})
try:
    r = u.urlopen(q, timeout=60); print(r.read().decode() if m == "GET" else r.status, end="")
except Exception as e:
    print(getattr(e, "code", "000") if m != "GET" else "", end="")' "$1" "$2" 2>/dev/null
    fi
}
command -v curl >/dev/null 2>&1 || echo "$(date -u +%FT%TZ) ALARME : curl absent au départ de la minuterie : repli par python3" >> "$J"
while [ "$(date +%s)" -lt "$ECH" ]; do sleep 5; done
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) identifiant illisible : aucun geste" >> "$J"; exit 3;; esac
case " 58936096 58936099 58936100 " in *" $CONTAINER_ID "*) echo "$(date -u +%FT%TZ) instance protégée : aucun geste" >> "$J"; exit 3;; esac
LAB=$(appel GET "$API/instances/$CONTAINER_ID/" | grep -o '"label": *"[^"]*"' | head -1)
if [ -n "$LAB" ] && ! printf '%s' "$LAB" | grep -q '"sonde-a1-v3-v10"'; then
    echo "$(date -u +%FT%TZ) étiquette lue $LAB, pas sonde-a1-v3-v10 : aucun geste" >> "$J"; exit 3
fi
[ -n "$LAB" ] || echo "$(date -u +%FT%TZ) étiquette non lue : destruction par l'identifiant posé par Vast" >> "$J"
n=0
while :; do  # m-a : jamais d'arrêt (il tuerait cette minuterie) ; le DELETE recommence chaque minute jusqu'à la fin de vie
    n=$((n + 1)); c=$(appel DELETE "$API/instances/$CONTAINER_ID/")
    echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID (essai $n) : HTTP $c" >> "$J"
    case "$c" in 2??) exit 0;; esac
    [ "$(date +%s)" -lt $((FIN - 60)) ] || { echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue avant la fin de vie" >> "$J"; exit 4; }
    sleep 60
done
'''


def script_de_demarrage(commit_prive: str) -> str:
    """Processus principal du conteneur. Ordre : (0) `curl` installé s'il manque ; (1) minuterie détachée, échéance =
    minimum de l'échéance absolue du pilote (M-B) et de départ + durée + marge, gardée sur disque (une reprise garde l'échéance
    d'origine) ; (2) clone partiel, `sparse-checkout`, chronométré ; (3) amorce ; (4) vie jusqu'à l'échéance + 10 min, puis
    attente de la fin de la minuterie (m-b)."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit_prive):
        raise h.Refus("commit du dépôt privé : hash complet de 40 caractères exigé")
    m64 = base64.b64encode(MINUTERIE.encode()).decode("ascii")
    return f'''set -u
R="${{RACINE_SONDE:-/root}}"; case "$R" in /*) ;; *) R=/root;; esac
API="${{API_VAST:-{h.API_VAST}}}"; case "$API" in https://*) ;; *) API={h.API_VAST};; esac
D="${{DUREE_MAX_S:-{DUREE_DEFAUT_S}}}"; case "$D" in ''|*[!0-9]*) D={DUREE_DEFAUT_S};; esac; [ "$D" -le {DUREE_MAX_S} ] || D={DUREE_MAX_S}
MARGE="${{SONDE_MARGE_S:-{MARGE_MINUTERIE_S}}}"; case "$MARGE" in ''|*[!0-9]*) MARGE={MARGE_MINUTERIE_S};; esac
APRES="${{SONDE_VIE_APRES_S:-{VIE_APRES_ECHEANCE_S}}}"; case "$APRES" in ''|*[!0-9]*) APRES={VIE_APRES_ECHEANCE_S};; esac
ABS="${{ECHEANCE_UTC_S:-}}"; case "$ABS" in ''|*[!0-9]*) ABS="";; esac
if [ -s "$R/sonde-v10-minuterie.txt" ]; then read T0 ECH < "$R/sonde-v10-minuterie.txt"
else T0=$(date +%s); ECH=$((T0 + D + MARGE)); if [ -n "$ABS" ] && [ "$ABS" -lt "$ECH" ]; then ECH=$ABS; fi
     echo "$T0 $ECH" > "$R/sonde-v10-minuterie.txt"; fi
FINVIE=$((ECH + APRES))
echo {m64} | base64 -d > "$R/sonde-v10-minuterie.sh"
setsid bash "$R/sonde-v10-minuterie.sh" "$ECH" "$R" "$API" "$FINVIE" < /dev/null >> "$R/sonde-v10-minuterie.log" 2>&1 &
PM=$!
reste() {{ r=$(( FINVIE - $(date +%s) )); [ "$r" -gt 1 ] && echo "$r" || echo 1; }}  # m-2 : tout est borné par la fin de vie
borne() {{ r=$(reste); [ "$r" -lt "$1" ] && echo "$r" || echo "$1"; }}
command -v curl >/dev/null || timeout -k 5 "$(borne 120)" sh -c 'apt-get update -qq && apt-get install -y -qq curl git ca-certificates >/dev/null 2>&1'
echo "demarrage $(date -u +%FT%TZ) depart $T0 echeance $ECH absolue ${{ABS:-aucune}} curl $(command -v curl >/dev/null && echo oui || echo NON)" >> "$R/sonde-v10-temps.txt"
if [ ! -d "$R/amorce-depot/.git" ]; then
  t=$(date +%s)
  (command -v git >/dev/null || timeout -k 5 "$(borne 120)" sh -c 'apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null')
  A='!f() {{ echo username=x-access-token; echo "password=${{GH_TOKEN}}"; }}; f'
  git init -q "$R/amorce-depot" && git -C "$R/amorce-depot" remote add origin "$DEPOT_URL" &&
  git -C "$R/amorce-depot" sparse-checkout set scripts src/controle_ia &&
  timeout -k 5 "$(borne 600)" git -C "$R/amorce-depot" -c credential.helper="$A" fetch -q --filter=blob:none --depth 1 origin {commit_prive} &&
  timeout -k 5 "$(borne 600)" git -C "$R/amorce-depot" -c credential.helper="$A" checkout -q --detach FETCH_HEAD
  echo "clone $? en $(( $(date +%s) - t )) s" >> "$R/sonde-v10-temps.txt"
fi
[ -f "$R/amorce-depot/{AMORCE}" ] && timeout -k 10 "$(reste)" bash "$R/amorce-depot/{AMORCE}" 2>&1 | tee -a "$R/amorce-sonde-a1v3-v10.log"
echo "amorce finie $(date -u +%FT%TZ)" >> "$R/sonde-v10-temps.txt"
while [ "$(date +%s)" -lt "$FINVIE" ]; do sleep 5; done
# m-b : le principal ne sort qu'après la minuterie (sa mort tuerait tout l'espace de processus du conteneur)
[ -s "$R/sonde-v10-minuterie.pid" ] && PM=$(cat "$R/sonde-v10-minuterie.pid")
t=$(date +%s); while kill -0 "$PM" 2>/dev/null && [ $(( $(date +%s) - t )) -lt {ATTENTE_MINUTERIE_S} ]; do sleep 2; done
echo "fin du principal $(date -u +%FT%TZ)" >> "$R/sonde-v10-temps.txt"
'''


def corps(commit_prive: str, offre: dict, duree_s: int, gh_token: str, echeance_utc_s: int, tir: bool = False,
          commit_registre: str = "") -> dict:
    if not gh_token:
        raise h.Refus("GH_TOKEN absent : la sonde ne pourrait pas verser")
    if not isinstance(echeance_utc_s, int) or isinstance(echeance_utc_s, bool) or echeance_utc_s <= 0:
        raise h.Refus("échéance absolue (M-B) : entier de secondes exigé")
    env = {"COMMIT_PRIVE": commit_prive, "GO_ID": GO_SONDE, "PRIX_H_USD": f"{offre['dph_total']:.6f}",
           "DUREE_MAX_S": str(duree_s), "DEPOT_URL": h.DEPOT_PRIVE, "GH_TOKEN": gh_token,
           "ECHEANCE_UTC_S": str(echeance_utc_s), "TIR_MINUTERIE": "1" if tir else "0"}
    if commit_registre:  # v10 (a) : commit du registre sur canal/conv-audit-n04, lu sur la machine
        if not re.fullmatch(r"[0-9a-f]{40}", commit_registre):
            raise h.Refus("commit du registre : hash complet de 40 caractères exigé")
        env["COMMIT_REGISTRE"] = commit_registre
    if cles_de_modele(env):
        raise h.Refus("clé de modèle dans le corps de la sonde")
    b64 = base64.b64encode(script_de_demarrage(commit_prive).encode()).decode("ascii")
    return {"image": h.IMAGE, "disk": 30, "label": ETIQUETTE, "env": env,
            "script": f"echo {b64} | base64 -d > /root/demarrage-sonde-v10.sh && bash /root/demarrage-sonde-v10.sh"}


# --- côté pilote : l'outil vastai, sorties jamais affichées (M3, f1) ------------------------------------------------------


class ClientPilote:
    """`vastai` dans un sous-processus ; la clé de Vast vient de `VAST_API_KEY` (exigée) ; sortie jamais affichée ni écrite :
    seulement le code de sortie et une ligne masquée (toutes les valeurs de secrets remplacées)."""

    def __init__(self, environ: dict, outil: str = "vastai"):
        self.outil = outil
        self.environ = environ
        if not environ.get("VAST_API_KEY"):
            raise h.Refus("VAST_API_KEY absente de l'environnement (passée par env -i, par son nom)")
        self.secrets = {k: environ.get(k, "") for k in SECRETS_PILOTE}

    def masquer(self, texte: str) -> str:
        for nom, v in self.secrets.items():
            if v:
                texte = texte.replace(v, f"[{nom} masquée]")
        return texte

    def _lancer(self, args: list[str], secrets_en_plus: dict | None = None) -> str:
        env = {k: self.environ[k] for k in ("PATH", "HOME", "LANG", "VAST_API_KEY") + VARIABLES_MANDATAIRE
               if self.environ.get(k)}  # v6 (a) : variables du mandataire transmises si présentes, aucune autre
        try:
            r = subprocess.run([self.outil, *args], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               timeout=DELAI_VASTAI_S)  # f-a, v6 (b) : la sortie d'erreur n'est que cherchée, jamais écrite
        except subprocess.TimeoutExpired:  # M-1 : le message de l'exception porte la ligne de commande, jeton compris
            raise h.Refus(f"vastai {' '.join(args[:2])} : délai dépassé ({DELAI_VASTAI_S} s)") from None

        def masque(octets: bytes) -> str:
            texte = octets.decode("utf-8", "replace")
            for nom, v in (secrets_en_plus or {}).items():
                if v:
                    texte = texte.replace(v, f"[{nom} masquée]")
            return self.masquer(texte)
        certificat = any(m in (r.stderr or b"") for m in MOTS_CERTIFICAT)
        r = subprocess.CompletedProcess(r.args, r.returncode, r.stdout, None)  # la sortie d'erreur est oubliée ici
        if r.returncode != 0:  # f-a : le code seul ; aucune sortie (standard ni d'erreur) n'est écrite
            if certificat:
                raise RefusCertificat(f"vastai {' '.join(args[:2])} : appel non parvenu à Vast (certificat) ; code "
                                      f"{r.returncode}")
            raise h.Refus(f"vastai {' '.join(args[:2])} : code {r.returncode}")
        return masque(r.stdout)  # la sortie standard seule est lue ; la sortie d'erreur n'est jamais ni lue ni écrite

    def creer(self, offre_id: int, c: dict) -> int:
        if cles_de_modele(c["env"]):
            raise RefusAvantAppel("clé de modèle dans le corps : rien créé")
        if any(ch.isspace() or ch in "\"'" for v in c["env"].values() for ch in v):
            raise RefusAvantAppel("valeur d'environnement avec espace ou guillemet : refus (forme -e K=V)")
        # v8 (a) : les deux sorties sont capturées ; le code de sortie seul ne décide jamais ; rien de brut n'est écrit
        env = {k: self.environ[k] for k in ("PATH", "HOME", "LANG", "VAST_API_KEY") + VARIABLES_MANDATAIRE
               if self.environ.get(k)}
        args = arguments_de_creation(offre_id, c)
        try:
            r = subprocess.run([self.outil, *args], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               timeout=DELAI_VASTAI_S)
        except subprocess.TimeoutExpired:  # M-1
            raise h.Refus(f"vastai {' '.join(args[:2])} : délai dépassé ({DELAI_VASTAI_S} s)") from None
        sortie = (r.stdout or b"").decode("utf-8", "replace")
        erreur = (r.stderr or b"").decode("utf-8", "replace")
        certificat = any(m in (r.stderr or b"") for m in MOTS_CERTIFICAT)
        secrets = [v for v in self.secrets.values() if v] + [c["env"]["GH_TOKEN"]]
        cat, _ = categoriser_reponse(sortie, secrets)
        if cat == "illisible" and certificat:
            raise RefusCertificat(f"vastai {' '.join(args[:2])} : appel non parvenu à Vast (certificat) ; code {r.returncode}")
        return lire_reponse_de_creation(sortie, secrets, erreur, r.returncode)

    def facturation(self, ident: int) -> dict:
        """v10 (b) : `vastai show instance` ; seuls `CHAMPS_FACTURATION` sortent d'ici (la sortie brute porte l'environnement de
        la machine, jeton compris : jamais écrite)."""
        if ident in PROTEGEES:
            raise h.Refus(f"instance {ident} protégée : jamais touchée")
        texte = self._lancer(["show", "instance", str(ident), "--raw"])
        try:
            brut = json.loads(texte)
        except ValueError:
            raise h.Refus(f"relevé de l'instance {ident} illisible (longueur {len(texte)})") from None
        if isinstance(brut, list):
            brut = next((x for x in brut if isinstance(x, dict) and x.get("id") == ident), {})
        if not isinstance(brut, dict):
            raise h.Refus(f"relevé de l'instance {ident} : forme inattendue")
        return {"id": brut.get("id"), "label": brut.get("label"),
                **{k: brut[k] for k in CHAMPS_FACTURATION
                   if k in brut and (brut[k] is None or isinstance(brut[k], (int, float, str, bool)))}}

    def instances(self) -> list[dict]:
        texte = self._lancer(["show", "instances", "--raw"])
        try:
            return json.loads(texte)
        except ValueError:
            raise h.Refus("inventaire illisible") from None

    def detruire(self, ident: int) -> None:
        if ident in PROTEGEES:
            raise h.Refus(f"instance {ident} protégée : jamais touchée")
        self._lancer(["destroy", "instance", str(ident), "-y"])


def arguments_de_creation(offre_id: int, c: dict) -> list[str]:
    """Les arguments de `vastai create instance` (forme des amorces du dépôt) ; v7 (c) : leurs longueurs sont écrites."""
    env = " ".join(f"-e {k}={v}" for k, v in c["env"].items())
    return ["create", "instance", str(offre_id), "--raw", "--image", c["image"], "--disk", str(c["disk"]), "--cancel-unavail",
            "--label", c["label"], "--env", env, "--entrypoint", "bash", "--args", "-c", c["script"]]


def longueurs_de_creation(offre_id: int, c: dict) -> dict:
    a = arguments_de_creation(offre_id, c)
    return {"args_c": len(c["script"]), "env": len(a[a.index("--env") + 1]),
            "commande": len(" ".join(["vastai", *a]))}


def _champ_sur(valeur, secrets: list[str]) -> str:
    texte = str(valeur)[:200]
    for v in secrets:
        if v:
            texte = texte.replace(v, "[masquée]")
    return texte


def categoriser_reponse(texte: str, secrets: list[str]) -> tuple[str, str]:
    """v7 (a) : la réponse de `vastai create` réduite à une catégorie sûre. Rend (catégorie, détail écrivable) :
    (« contrat », identifiant) ; (« no_such_ask », error et msg) ; (« erreur Vast », error et msg) si `success` est faux ;
    (« erreur Vast sans success faux », error et msg) sinon pour un dictionnaire ; (« illisible », longueur seule)."""
    import ast
    rep = None
    for essai in [texte] + list(reversed(texte.strip().splitlines())):
        for lecteur in (json.loads, ast.literal_eval):
            try:
                x = lecteur(essai.strip())
            except (ValueError, SyntaxError, TypeError, MemoryError, RecursionError):
                continue
            if isinstance(x, dict):
                rep = x
                break
        if rep is not None:
            break
    if rep is None:
        rep = _champs_par_motif(texte)  # v8 (a) : forme mal formée (`'success': False?`, …) : error et msg seuls
    if rep is None:
        return "illisible", f"longueur {len(texte)}"
    ident = rep.get("new_contract")
    if rep.get("success") is True and isinstance(ident, int) and not isinstance(ident, bool):
        return "contrat", str(ident)
    detail = f"error={_champ_sur(rep.get('error'), secrets)!r} ; msg={_champ_sur(rep.get('msg'), secrets)!r}"
    if "no_such_ask" in str(rep.get("error")) or "no_such_ask" in str(rep.get("msg")):
        return "no_such_ask", detail
    if rep.get("success") is False:
        return "erreur Vast", detail
    return "erreur Vast sans success faux", detail


def _champs_par_motif(texte: str) -> dict | None:
    """v8 (a) : `error`, `msg` et `success` extraits par motif quand le texte n'est ni du JSON ni un littéral Python."""
    champs = {}
    for nom in ("error", "msg"):
        m = re.search(r"""['"]%s['"]\s*:\s*(?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)"|([^,}]+))""" % nom, texte)
        if m:
            champs[nom] = next(g for g in m.groups() if g is not None).strip()
    m = re.search(r"""['"]success['"]\s*:\s*(True|False|true|false)""", texte)
    if m:
        champs["success"] = m.group(1).lower() == "true"
    return champs if ("error" in champs or "msg" in champs) else None


def lire_reponse_de_creation(texte: str, secrets: list[str] | None = None, erreur: str = "", code: int = 0) -> int:
    """v7 (a), v8 (a) : sortie standard d'abord, puis sortie d'erreur ; seule la catégorie et ses champs sûrs sortent d'ici."""
    cat, detail = categoriser_reponse(texte, secrets or [])
    if cat == "illisible" and erreur:
        cat, detail = categoriser_reponse(erreur, secrets or [])
        if cat == "illisible":
            detail = f"sortie standard {len(texte)} caractères, sortie d'erreur {len(erreur)}, code {code}"
        else:
            detail = f"{detail} (sortie d'erreur, code {code})"
    elif cat == "illisible":
        detail = f"sortie standard {len(texte)} caractères, sortie d'erreur 0, code {code}"
    if cat == "contrat":
        return int(detail)
    if cat == "no_such_ask":
        raise RefusNoSuchAsk(f"réponse de création : {cat} ; {detail} (Vast : rien créé)")
    if cat == "erreur Vast":
        raise RefusVastSansCreation(f"réponse de création : {cat} ; {detail} (Vast : rien créé)")
    if cat == "illisible":
        raise h.Refus(f"CREATION_INCERTAINE : réponse de création : illisible ({detail}) : ne rien relancer avant l'inventaire")
    raise h.Refus(f"CREATION_INCERTAINE : réponse de création : {cat} ; {detail} : ne rien relancer avant l'inventaire")


def louer(a, client=None, aujourd_hui=None, environ=None, maintenant=None) -> int:
    environ = dict(os.environ) if environ is None else environ
    jl = Path(a.journal_local)
    j = h.Journal(jl, {k: environ.get(k, "") for k in SECRETS_PILOTE})
    ident_f, incertain_f, etat_f = (Path(str(jl) + x) for x in (".identifiant", ".creation-incertaine", ".etat.json"))
    try:
        if ident_f.exists() or incertain_f.exists():
            raise h.Refus("une location de la sonde v10 a déjà eu lieu ou est incertaine (R12) : inventaire d'abord")
        if environ.get("GO_ID") != GO_SONDE:
            raise h.Refus(f"GO_ID={GO_SONDE} exigé en tête de la ligne de location (f7)")
        if cles_de_modele(environ):
            raise h.Refus(f"clé de modèle dans l'environnement du pilote : {cles_de_modele(environ)}")
        aujourd_hui = aujourd_hui or dt.datetime.now(dt.timezone.utc).date()
        g = verifier_go_sonde(Path(a.registre_main), Path(a.garde_main), a.go, aujourd_hui)
        j.ecrire(f"sonde v10 : GO {g['go']} accepté par la garde de main, {g['plafond_usd']:g} USD")
        offres = json.loads(Path(a.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        o = offre_la_moins_chere_sonde(offres, int(a.offre))
        if o["memoire_non_renseignee"]:
            j.ecrire(f"sonde v10 : offre {o['id']} : mémoire non renseignée par Vast (cpu_ram = 0) ; "
                     f"{o['cpu_cores_effective']} cœurs ; mémoire réelle relevée sur la machine")
        duree = verifier_duree(a.duree_s)
        tir = bool(getattr(a, "tir_minuterie", False))
        marge = MARGE_TIR_S if tir else MARGE_MINUTERIE_S
        if a.verifier_seulement:
            cout = verifier_plafond(o["dph_total"], duree, marge_s=marge)
            c = corps(a.commit_prive, o, duree, environ.get("GH_TOKEN", ""),
                      int((maintenant or dt.datetime.now(dt.timezone.utc)).timestamp()) + DEMARRAGE_MAX_S + duree + marge, tir,
                      a.commit_registre)
            lg = longueurs_de_creation(o["id"], c)
            j.ecrire(f"sonde v10 : offre {o['id']} à {o['dph_total']} USD/h ; dépense au plus {cout:.4f} USD ; longueurs : "
                     f"--args {lg['args_c']}, --env {lg['env']}, commande {lg['commande']}")
            j.ecrire("sonde v10, vérification seulement : rien créé (variables : " + ", ".join(sorted(c["env"])) + ")")
            return 0
        client = client or ClientPilote(environ)
        # v8 (b) : sur « no_such_ask » (Vast : rien créé), au plus 4 autres offres conformes, par prix croissant, chacune
        # revérifiée ; garde de dépense recalculée à chaque essai ; au cinquième « no_such_ask », refus final sans marqueur.
        autres = []
        for x in sorted((x for x in offres if isinstance(x, dict) and x.get("id") != o["id"]),
                        key=lambda x: (x.get("dph_total") if isinstance(x.get("dph_total"), (int, float)) else 1e9,
                                       str(x.get("id")))):
            try:
                autres.append(verifier_offre_sonde([x], x.get("id")))
            except h.Refus:
                continue
        candidates = [o] + autres[:ESSAIS_NO_SUCH_ASK - 1]
        ident = None
        for n, oc in enumerate(candidates, 1):
            oc = verifier_offre_sonde(offres, oc["id"])
            cout = verifier_plafond(oc["dph_total"], duree, marge_s=marge)
            t_creation = maintenant or dt.datetime.now(dt.timezone.utc)
            echeance = int(t_creation.timestamp()) + DEMARRAGE_MAX_S + duree + marge
            c = corps(a.commit_prive, oc, duree, environ.get("GH_TOKEN", ""), echeance, tir, a.commit_registre)
            lg = longueurs_de_creation(oc["id"], c)
            j.ecrire(f"sonde v10 : essai {n}/{len(candidates)} : offre {oc['id']} à {oc['dph_total']} USD/h ; dépense au plus "
                     f"{cout:.4f} USD ≤ {PLAFOND_SONDE_USD} ; longueurs : --args {lg['args_c']}, --env {lg['env']}, "
                     f"commande {lg['commande']}")
            try:
                ident = client.creer(oc["id"], c)
                j.ecrire(f"sonde v10 : réponse de création : contrat {ident} (essai {n})")
                o = oc
                break
            except RefusNoSuchAsk as e:
                j.ecrire(f"sonde v10 : essai {n} refusé : {e}")
                if n == len(candidates):
                    raise RefusNoSuchAsk(f"{n} essai(s), tous « no_such_ask » : refus final (Vast : rien créé)") from None
            except RefusAvantAppel:  # certificat, autre erreur de Vast avec success faux, gardes : arrêt, sans marqueur
                raise
            except h.Refus as e:  # m-1 : réponse illisible, erreur sans success faux, délai : marqueur, arrêt
                incertain_f.write_text(f"{h.maintenant()} {str(e)[:120]}\n")
                raise
        t0 = t_creation
        etat = {"identifiant": ident, "etiquette": ETIQUETTE, "t0_utc": t0.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "borne_signe_de_vie_utc": (t0 + dt.timedelta(seconds=BORNE_SIGNE_DE_VIE_S)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "echeance_finale_utc": dt.datetime.fromtimestamp(echeance, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "controles_utc": [(t0 + dt.timedelta(minutes=m)).strftime("%Y-%m-%dT%H:%M:%SZ") for m in ((45, 70) if tir else (40, 70))],  # f-3
                "prix_h_usd": o["dph_total"], "cout_maximal_usd": round(cout, 4), "tir_minuterie": tir, "go": GO_SONDE}
        ident_f.write_text(f"{ident}\n")
        etat_f.write_text(json.dumps(etat, ensure_ascii=False, indent=1) + "\n")
        j.ecrire(f"sonde v10 créée : identifiant {ident}, étiquette {ETIQUETTE} ; T0 {etat['t0_utc']} ; signe de vie attendu "
                 f"avant {etat['borne_signe_de_vie_utc']} ; échéance finale {etat['echeance_finale_utc']}")
        j.ecrire("LIGNE POUR registres/etat.md : " + ligne_etat(etat))
        return 0
    except (h.Refus, OSError, ValueError, KeyError) as e:
        j.ecrire(f"REFUS : {e}")
        return 2


def ligne_etat(e: dict) -> str:
    return (f"- Sonde v10 de l'hôte durable d'A1-v3 ({GO_SONDE}) : instance **{e['identifiant']}**, étiquette "
            f"`{e['etiquette']}`, créée {e['t0_utc']}, échéance {e['echeance_finale_utc']} ; contrôles à "
            f"{' et '.join(e['controles_utc'])} ; toute session qui reprend lance `sonde_hote_durable_a1_v3_v10.py controler` "
            "(étiquette contrôlée, destruction par l'identifiant avec -y).")


def controler(a, client=None, signe_de_vie=None, maintenant=None, environ=None) -> int:
    """m2 et M-A : borne « jamais démarrée » et repli du pilote ; codes : 0 instance absente (détruite), 1 détruite par le
    pilote, 2 refus (étiquette, protégée, état illisible), 3 destruction demandée mais encore listée, 5 listée avant ses bornes :
    **recontrôler** (contrôles à T0 + 40, ou T0 + 45 en tir, et T0 + 70 min), 6 délai dépassé (`vastai` ou `ls-remote`, f-6) :
    recontrôler."""
    environ = dict(os.environ) if environ is None else environ
    j = h.Journal(Path(a.journal_local), {k: environ.get(k, "") for k in SECRETS_PILOTE})
    try:
        e = json.loads(Path(a.etat).read_text())
        ident = int(e["identifiant"])
        if ident in PROTEGEES:
            raise h.Refus(f"instance {ident} protégée : jamais touchée")
        now = maintenant or dt.datetime.now(dt.timezone.utc)
        lire = lambda k: dt.datetime.strptime(e[k], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        client = client or ClientPilote(environ)
        listees = [i for i in client.instances() if i.get("id") == ident]
        if not listees:
            j.ecrire(f"contrôle : instance {ident} absente de l'inventaire (détruite) ; rien à faire")
            return 0
        lab = listees[0].get("label")
        if lab != ETIQUETTE:
            raise h.Refus(f"instance {ident} : étiquette {lab!r}, pas {ETIQUETTE} : aucun geste (f8)")
        vie = signe_de_vie() if signe_de_vie else branche_existe(BRANCHE_VIE, environ)
        motif = None
        if now >= lire("borne_signe_de_vie_utc") and not vie:
            motif = "aucun signe de vie à T0 + 30 min (m2)"
        elif now >= lire("echeance_finale_utc") + dt.timedelta(seconds=VIE_APRES_ECHEANCE_S):
            motif = "encore listée après l'échéance finale (la minuterie n'a pas détruit)"
        if motif is None:
            j.ecrire(f"contrôle : instance {ident} ({listees[0].get('actual_status')}) ; signe de vie {'oui' if vie else 'non'} ;"
                     f" encore listée : RECONTRÔLER (au plus tard {e.get('controles_utc', ['?'])[-1]})")
            return 5
        j.ecrire(f"contrôle : {motif} : destruction de {ident} par son identifiant (-y)")
        client.detruire(ident)
        if [i for i in client.instances() if i.get("id") == ident]:
            j.ecrire(f"instance {ident} encore listée après la destruction : recommencer, puis consigner")
            return 3
        j.ecrire(f"instance {ident} détruite par le pilote, vérifiée par l'inventaire : consigner dans registres/arrets.md")
        return 1
    except RefusRecontroler as x:  # v7 (b) : un fait non établi n'est jamais « pas de signe de vie »
        j.ecrire(f"RECONTRÔLER : {x}")
        return 6
    except subprocess.TimeoutExpired as x:  # f-6 : seul le nom de la commande est écrit
        j.ecrire(f"DÉLAI DÉPASSÉ : {x.cmd[0] if isinstance(x.cmd, (list, tuple)) else 'commande'} ; recontrôler")
        return 6
    except (h.Refus, OSError, ValueError, KeyError) as x:
        j.ecrire(f"REFUS : {x}")
        return 6 if "délai dépassé" in str(x) else 2


def relever_facturation(a, client=None, environ=None) -> int:
    """v10 (b) : relevé de facturation du pilote, juste avant l'échéance ; écrit au journal du pilote les seuls champs
    `CHAMPS_FACTURATION` (et l'identifiant, l'étiquette) ; codes : 0 écrit, 2 refus (étiquette, protégée, état illisible),
    6 délai ou échec de `vastai` (recontrôler)."""
    environ = dict(os.environ) if environ is None else environ
    j = h.Journal(Path(a.journal_local), {k: environ.get(k, "") for k in SECRETS_PILOTE})
    try:
        e = json.loads(Path(a.etat).read_text())
        ident = int(e["identifiant"])
        if ident in PROTEGEES:
            raise h.Refus(f"instance {ident} protégée : jamais touchée")
        client = client or ClientPilote(environ)
        f = client.facturation(ident)
        if f.get("label") not in (None, ETIQUETTE):
            raise h.Refus(f"instance {ident} : étiquette {f.get('label')!r}, pas {ETIQUETTE} : aucun relevé écrit")
        champs = {k: f[k] for k in CHAMPS_FACTURATION if k in f}
        j.ecrire(f"relevé de facturation de l'instance {ident} : {json.dumps(champs, ensure_ascii=False, sort_keys=True)}")
        return 0
    except subprocess.TimeoutExpired:
        j.ecrire("DÉLAI DÉPASSÉ : vastai ; recontrôler")
        return 6
    except (h.Refus, OSError, ValueError, KeyError) as x:
        j.ecrire(f"REFUS : {x}")
        return 6 if ("délai dépassé" in str(x) or "code" in str(x)) else 2


def branche_existe(branche: str, environ: dict, outil: str = "git") -> bool:
    """v7 (b) : variables du mandataire transmises si présentes ; un échec (code non nul, délai, `git` absent) lève
    `RefusRecontroler` (code 6) et n'est jamais lu « pas de signe de vie » ; aucune sortie de `git` n'est écrite."""
    aide = ['-c', 'credential.helper=!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f']
    env = {"PATH": environ.get("PATH", "/usr/bin:/bin"), "HOME": environ.get("HOME", "/root"),
           "GH_TOKEN": environ.get("GH_TOKEN", ""), "GIT_TERMINAL_PROMPT": "0"}
    env.update({k: environ[k] for k in VARIABLES_MANDATAIRE if environ.get(k)})
    try:
        r = subprocess.run([outil, *aide, "ls-remote", h.DEPOT_PRIVE, f"refs/heads/{branche}"], capture_output=True,
                           timeout=120, env=env)
    except subprocess.TimeoutExpired:
        raise RefusRecontroler("ls-remote : délai dépassé") from None
    except OSError as x:
        raise RefusRecontroler(f"ls-remote : {type(x).__name__}") from None
    if r.returncode != 0:
        raise RefusRecontroler(f"ls-remote : code {r.returncode}")
    return bool(r.stdout.strip())


# --- côté machine -----------------------------------------------------------------------------------------------------------


class MachineSondeV10(s1.MachineSonde):
    """La séquence de la sonde v1, avec les corrections de la contre-lecture (versements orphelins, exceptions attrapées,
    étiquette contrôlée, dépense comptée depuis le départ du conteneur, journaux du démarrage versés)."""

    def relever_l_hote(self) -> None:
        """v10 (b) : les faits de la v9, plus une ligne sur le pilote de carte (`nvidia-smi -L` s'il existe)."""
        super().relever_l_hote()
        outil = shutil.which("nvidia-smi")
        if outil is None:
            ligne = "nvidia-smi absent"
        else:
            try:
                r = h.lancer([outil, "-L"], delai=60)
                ligne = ((r.stdout or b"").decode("utf-8", "replace").strip().splitlines() or [f"aucune ligne (code "
                                                                                              f"{r.returncode})"])[0][:200]
            except Exception as x:  # un fait à écrire, jamais un arrêt
                ligne = f"nvidia-smi : {type(x).__name__}"
        (self.t / "pilote-carte.txt").write_text(ligne + "\n")
        self.j.ecrire(f"pilote de carte : {ligne}")

    def __init__(self, r: h.Reglages, environ: dict[str, str], course_factice_s: float = s1.COURSE_FACTICE_S):
        super().__init__(r, environ, course_factice_s)
        self.secrets = {k: environ.get(k, "") for k in SECRETS_MACHINE}
        self.racine = r.travail.parent
        t0 = None
        try:
            t0 = float((self.racine / "sonde-v10-minuterie.txt").read_text().split()[0])
        except (OSError, ValueError, IndexError):
            pass
        # m1 : dépense et durée comptées depuis le départ du conteneur (écrit par le script de démarrage), sinon depuis ici
        self.depart_conteneur = t0
        if t0 is not None:
            self.debut = time.monotonic() - max(0.0, time.time() - t0)

    def principal(self) -> int:
        journal = self.t / "journal-sonde-a1-v3-v10.log"
        if self.etat_fichier.exists():
            self.j = h.Journal(journal, self.secrets)
            avant = self.etat_fichier.read_text().strip()
            self.j.ecrire(f"REPRISE du conteneur de la sonde v10 : état « {avant} » ; rien n'est relancé")
            if avant == "verse":
                return self.se_detruire(True)
            self.nature_fin = "reprise_du_conteneur"
            return self.fin(BRANCHE_INTERROMPUE)
        self.t.mkdir(parents=True, exist_ok=False)
        self.j = h.Journal(journal, self.secrets)
        self.j.ecrire(f"{VERSION} ; machine {self.env.get('CONTAINER_ID', '?')} ; prix {self.prix_h} USD/h ; départ du "
                      f"conteneur {self.depart_conteneur}")
        self.etat("demarrage")
        try:
            self.preparer_sonde()
            self.etat("course")
            self.garder_sonde()
        except h.Refus as e:
            self.j.ecrire(f"REFUS : {e}")
            self.nature_fin = "refus_avant_course" if self.course is None else "refus_pendant_la_course"
        except Exception as e:  # jamais un repli silencieux
            self.j.ecrire(f"EXCEPTION {type(e).__name__} : {self.j.masquer(str(e))[:300]}")
            self.nature_fin = "exception_de_l_hote"
        refus = self.course is None
        return self.fin(BRANCHE_REFUS if refus else BRANCHE)

    def preparer_sonde(self) -> None:
        e, r = self.env, self.r
        interdites = cles_de_modele(e)
        if interdites:
            raise h.Refus(f"clé de modèle dans l'environnement de la sonde : {interdites} (aucune clé d'Argon)")
        for k in ("GH_TOKEN", "GO_ID", "PRIX_H_USD"):
            if not e.get(k):
                raise h.Refus(f"variable {k} absente")
        duree = verifier_duree(e.get("DUREE_MAX_S"))
        r.duree_max_s = float(duree)
        if not (0 < self.prix_h <= h.PRIX_MAX_H_USD):
            raise h.Refus(f"prix horaire {self.prix_h} hors de ]0 ; {h.PRIX_MAX_H_USD}]")
        verifier_plafond(self.prix_h, duree, marge_s=MARGE_TIR_S if e.get("TIR_MINUTERIE") == "1" else MARGE_MINUTERIE_S)
        if not re.fullmatch(r"[0-9]{9,11}", e.get("ECHEANCE_UTC_S") or ""):
            raise h.Refus("ECHEANCE_UTC_S (échéance absolue du pilote, M-B) absente ou illisible")
        depart = self.depart_conteneur or time.time()
        reste = int(e["ECHEANCE_UTC_S"]) - RESERVE_VERSEMENT_S - depart  # la course factice laisse 5 min au versement
        if reste <= 60:
            raise h.Refus(f"échéance absolue trop proche ({reste:.0f} s utiles) : aucune course factice")
        r.duree_max_s = float(min(duree, reste))
        # v10 (a) : comme la vraie course, le registre lu sur la machine est celui de `canal/conv-audit-n04` au commit que pose
        # le pilote (`COMMIT_REGISTRE`), jamais celui de `main` (le lecteur gelé y refuse les doublons d'extension, R-389) ;
        # fichiers lus par `git show` avec l'aide d'identification (la v9 lisait sans elle : lecture paresseuse refusée).
        cr = e.get("COMMIT_REGISTRE") or ""
        if not re.fullmatch(r"[0-9a-f]{40}", cr):
            raise h.Refus("COMMIT_REGISTRE (commit du registre sur canal/conv-audit-n04) absent ou illisible")
        gh = self.secrets["GH_TOKEN"]
        h.git("fetch", "-q", "--filter=blob:none", "--depth", str(PROFONDEUR_CANAL), "origin",
              f"+refs/heads/{h.SOURCE_REGISTRE}:refs/remotes/origin/{h.SOURCE_REGISTRE}", cwd=r.clone_prive, gh_token=gh,
              delai=DELAI_GIT_S)
        if h.lancer(["git", "merge-base", "--is-ancestor", cr, f"refs/remotes/origin/{h.SOURCE_REGISTRE}"],
                    cwd=r.clone_prive, delai=DELAI_GIT_S).returncode != 0:
            raise h.Refus(f"commit du registre {cr} absent de la branche {h.SOURCE_REGISTRE} (ou au-delà de "
                          f"{PROFONDEUR_CANAL} commits)")
        reg, garde = self.t / "registre-go.md", self.t / "garde_calcul_canal.py"
        for chemin, dest in (("registres/go.md", reg), (".claude/hooks/garde_calcul.py", garde)):
            try:
                dest.write_text(h.git("show", f"{cr}:{chemin}", cwd=r.clone_prive, gh_token=gh, delai=DELAI_GIT_S),
                                encoding="utf-8")
            except h.Refus:
                raise h.Refus(f"{chemin} illisible au commit {cr} de {h.SOURCE_REGISTRE}") from None
        doubles = h.doublons_lecteur_du_lanceur(reg)
        if doubles:
            raise h.Refus(f"registre {cr} : identifiants en double {doubles} (le lecteur gelé le refuserait)")
        g = verifier_go_sonde(reg, garde, e["GO_ID"], r.aujourd_hui or dt.datetime.now(dt.timezone.utc).date())
        self.j.ecrire(f"registre de {h.SOURCE_REGISTRE} au commit {cr} : aucun doublon ; {g['go']} accepté, "
                      f"{g['plafond_usd']:g} USD, sha256 {g['registre_sha256']}")
        self.signe_de_vie()
        self.relever_l_hote()
        self.lire_cle_d_instance()
        sortie_f = self.t / "sortie-factice"
        out = open(self.t / "course-factice-stdout.log", "ab")
        self.course = subprocess.Popen([sys.executable, "-I", "-B", "-c", s1.COURSE_FACTICE, str(sortie_f),
                                        str(self.course_factice_s)],
                                       env={"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8"},
                                       stdout=out, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, start_new_session=True)
        self.j.ecrire(f"course factice détachée : PID {self.course.pid} (durée prévue {self.course_factice_s:g} s, plafond "
                      f"{r.duree_max_s:g} s depuis le départ du conteneur)")

    def _env_git(self) -> dict:
        return {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.environ.get("HOME", "/root"),
                "GH_TOKEN": self.secrets["GH_TOKEN"], "GIT_TERMINAL_PROMPT": "0", "LANG": "C.UTF-8"}

    def _url(self) -> str:
        return h.git("remote", "get-url", "origin", cwd=self.r.clone_prive, delai=DELAI_GIT_S).strip()

    def pousser_orphelin(self, branche: str, fichiers: list[Path], base: Path, message: str) -> str:
        """Versement sans clone de `main` (m5) : dépôt neuf, branche orpheline, poussée, vérification par ls-remote."""
        gh, url = self.secrets["GH_TOKEN"], self._url()
        if h.git("ls-remote", url, f"refs/heads/{branche}", gh_token=gh, delai=DELAI_GIT_S).strip():
            raise h.Refus(f"branche {branche} déjà présente (R12) : rien n'est écrasé")
        v = self.racine / f"versement-{branche.rsplit('/', 1)[-1]}"
        if v.exists():
            raise h.Refus(f"copie de versement {v} déjà présente (R12)")
        h.git("init", "-q", "-b", "versement", str(v), delai=DELAI_GIT_S)
        dest = v / branche
        for p in fichiers:
            cible = dest / p.relative_to(base)
            cible.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, cible)
        h.git("add", "-f", "-A", cwd=v, delai=DELAI_GIT_S)
        h.git("-c", "user.name=sonde-hote-durable-a1-v3", "-c", "user.email=sonde@invalid", "commit", "-q", "-m", message,
              cwd=v, delai=DELAI_GIT_S)
        local = h.git("rev-parse", "HEAD", cwd=v, delai=DELAI_GIT_S).strip()
        for essai in range(1, self.r.essais_poussee + 1):
            try:
                h.git("push", "-q", url, f"HEAD:refs/heads/{branche}", cwd=v, gh_token=gh, delai=DELAI_GIT_S)
                vu = h.git("ls-remote", url, f"refs/heads/{branche}", gh_token=gh, delai=DELAI_GIT_S).split()
                if vu and vu[0] == local:
                    return local
            except (h.Refus, subprocess.TimeoutExpired) as x:
                self.j.ecrire(f"poussée {essai}/{self.r.essais_poussee} de {branche} : {type(x).__name__}")
            time.sleep(self.r.attente_poussee_s)
        raise h.Refus(f"poussée de {branche} non vérifiée")

    def signe_de_vie(self) -> None:
        """m2 : une branche orpheline poussée tôt ; le pilote ne détruit pas à T0 + 30 min une machine qui l'a poussée."""
        f = self.t / "signe-de-vie.json"
        f.write_text(json.dumps({"utc": h.maintenant(), "machine": self.env.get("CONTAINER_ID"),
                                 "depart_conteneur": self.depart_conteneur, "version": VERSION}) + "\n")
        try:
            c = self.pousser_orphelin(BRANCHE_VIE, [f], self.t, "Sonde de l'hôte durable d'A1-v3, v10 : signe de vie")
            self.j.ecrire(f"signe de vie poussé : {BRANCHE_VIE} = {c}")
        except Exception as x:  # une mesure : son échec est écrit, la sonde continue (le pilote détruira à T0 + 30 min)
            self.j.ecrire(f"signe de vie non poussé : {type(x).__name__} : {self.j.masquer(str(x))[:200]}")

    def copier_journaux_du_demarrage(self) -> None:
        d = self.t / "demarrage"
        for nom in FICHIERS_DEMARRAGE:
            p = self.racine / nom
            if p.is_file():
                d.mkdir(exist_ok=True)
                shutil.copy2(p, d / nom)

    def sceller(self) -> Path:
        self.copier_journaux_du_demarrage()
        liste = self.t / "EMPREINTES-sonde-hote-durable-a1-v3-v10.txt"
        lignes = [f"{h.sha256_fichier(p)}  {p.relative_to(self.t)}" for p in self.fichiers_a_verser() if p != liste]
        liste.write_text("\n".join(lignes) + "\n")
        return liste

    def verser(self, branche: str, liste: Path) -> bool:
        c = self.pousser_orphelin(branche, self.fichiers_a_verser(), self.t,
                                  f"Sonde de l'hôte durable d'A1-v3, v10 : état scellé ({self.nature_fin}), liste "
                                  f"{h.sha256_fichier(liste)[:16]}…, versé avant toute lecture")
        self.j.ecrire(f"versé : {branche} = {c} (vérifié par ls-remote) ; liste {h.sha256_fichier(liste)}")
        self.etat("verse")
        return True

    def fin(self, branche: str) -> int:
        """M1(b) : toute exception du scellement ou du versement est écrite, puis le geste sur la machine a lieu."""
        pousse = False
        try:
            self.etat("scellement")
            if self.course is not None and self.course.poll() is None:
                self.code_course = h.arreter_par_pid(self.course, self.j, "course factice")
            self.j.ecrire(f"nature de la fin : {self.nature_fin} ; coût de la machine estimé {self.cout_machine():.4f} USD "
                          "depuis le départ du conteneur ; scellement")
            liste = self.sceller()
            fuite = self.fuites()
            if fuite:
                raise h.Refus(f"valeur de secret trouvée dans {fuite} : rien n'est versé")
            pousse = self.verser(branche, liste)
        except Exception as x:
            try:
                self.j.ecrire(f"VERSEMENT IMPOSSIBLE : {type(x).__name__} : {self.j.masquer(str(x))[:200]}")
            except Exception:
                pass
        return self.se_detruire(pousse)

    def client_vast(self):
        return h.ClientVastJouet(self.r.vast_jouet) if self.r.jouet else h.ClientVast(self.secrets["CONTAINER_API_KEY"])

    def se_detruire(self, pousse: bool) -> int:
        """Destruction par l'identifiant, étiquette contrôlée (f8), **jamais d'arrêt** (m-a : il tuerait la minuterie) ; toute
        exception attrapée (M1(b)) ; codes : 0 détruite, 4 aucun geste (identifiant, étiquette, client), 5 laissée à la
        minuterie (tir de la minuterie, ou destruction refusée)."""
        ident = self.env.get("CONTAINER_ID", "")
        ecrire = lambda m: self._ecrire_sans_echec(m)
        if not re.fullmatch(r"[0-9]{1,12}", ident or "") or int(ident) in PROTEGEES:
            ecrire(f"identifiant {ident!r} illisible ou protégé : aucun geste ; la minuterie et le pilote s'en chargent")
            return 4
        n = int(ident)
        try:
            client = self.client_vast()
        except Exception as x:
            ecrire(f"client de Vast impossible ({type(x).__name__}) : la minuterie s'en charge")
            return 4
        try:
            vues = [i for i in client.instances() if i.get("id") == n]
            lab = vues[0].get("label") if vues else None
            if lab is not None and lab != ETIQUETTE:
                ecrire(f"étiquette lue {lab!r}, pas {ETIQUETTE} : aucun geste")
                return 4
        except Exception as x:
            ecrire(f"étiquette non lue ({type(x).__name__}) : geste par l'identifiant posé par Vast")
        if self.env.get("TIR_MINUTERIE") == "1":  # m-d : la minuterie doit détruire elle-même (tir réel)
            ecrire(f"tir de la minuterie : aucun geste de la machine {n} ; versé : {'oui' if pousse else 'NON'} ; "
                   "la minuterie détruit à l'échéance")
            return 5
        if not pousse:
            ecrire(f"versement non vérifié : destruction quand même (données factices ; un arrêt tuerait la minuterie, m-a)")
        try:
            ecrire(f"destruction de la machine par son identifiant {n}")
            client.detruire(n)
            return 0
        except Exception as x:  # m-a : jamais d'arrêt ; la minuterie recommence le DELETE chaque minute
            ecrire(f"destruction refusée ({type(x).__name__}) : aucun arrêt (il tuerait la minuterie) ; la minuterie "
                   "recommence à l'échéance")
            return 5

    def _ecrire_sans_echec(self, m: str) -> None:
        try:
            self.j.ecrire(m)
        except Exception:
            print(m, flush=True)


def reglages(environ: dict) -> h.Reglages:
    """m1 : versement borné (deux poussées, 30 s) ; la durée vient de `DUREE_MAX_S`, contrôlée dans `preparer_sonde`."""
    return h.Reglages(travail=Path("/root/sonde-a1-v3-v10"), clone_prive=Path("/root/amorce-depot"), duree_max_s=DUREE_DEFAUT_S,
                      periode_s=30, plafond_machine_usd=PLAFOND_SONDE_USD, essais_poussee=2, attente_poussee_s=30)


def principal(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    l = sous.add_parser("louer")
    for nom in ("--go", "--registre-main", "--garde-main", "--offres", "--offre", "--commit-prive", "--journal-local"):
        l.add_argument(nom, required=True)
    l.add_argument("--commit-registre", required=True, help="v10 (a) : commit du registre sur canal/conv-audit-n04")
    l.add_argument("--duree-s", default=str(DUREE_DEFAUT_S))
    l.add_argument("--verifier-seulement", action="store_true")
    l.add_argument("--tir-minuterie", action="store_true", help="m-d : la machine verse sans geste, la minuterie détruit")
    c = sous.add_parser("controler")
    c.add_argument("--etat", required=True)
    c.add_argument("--journal-local", required=True)
    fa = sous.add_parser("facturation")  # v10 (b) : relevé du pilote juste avant l'échéance
    fa.add_argument("--etat", required=True)
    fa.add_argument("--journal-local", required=True)
    o = sous.add_parser("offre")
    o.add_argument("--offres", required=True)
    sous.add_parser("hote")
    args = a.parse_args(argv)
    if args.mode == "louer":
        return louer(args)
    if args.mode == "controler":
        return controler(args)
    if args.mode == "facturation":
        return relever_facturation(args)
    if args.mode == "offre":  # m4 : l'offre la moins chère des conformes, tirée de la réponse brute
        offres = json.loads(Path(args.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        conformes = []
        for x in offres:
            try:
                conformes.append(verifier_offre_sonde([x], x.get("id")))
            except h.Refus:
                continue
        if not conformes:
            print("aucune offre conforme", file=sys.stderr)
            return 2
        print(min(conformes, key=lambda x: (x["dph_total"], x["id"]))["id"])
        return 0
    env = dict(os.environ)
    return MachineSondeV10(reglages(env), env).principal()


if __name__ == "__main__":
    sys.exit(principal())
