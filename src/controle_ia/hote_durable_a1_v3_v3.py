#!/usr/bin/env python3
"""Hôte durable de la troisième course d'A1-v3, **version 3** (machine : GO-2026-11-05-03 ; course : GO-2026-11-04-06).

Version 3 (R12 : v1 et v2 inchangées) : la v2, plus **seulement** trois corrections demandées après la contre-lecture n° 4
(`contre-lecture-n4-texte-v3-v1.md`, `b524b41c…`) et le fait relevé par la mère sur la sonde v10 (`faits-hote.json`,
`e53876b5` : sur l'image, `/usr/bin/python3` est Python 3.11.2, l'interpréteur de l'image, `/usr/local/bin/python3`, 3.13) :

- **C1** — le relais, la commande d'Argon et la course tournent sous l'interpréteur 3.13 de l'image : `python_relais` et
  `python_course` par chemin absolu (`PYTHON_IMAGE`), `PATH` du relais avec `/usr/local/bin` d'abord ; `/usr/bin/python3`
  (chemin écrit dans la configuration gelée, qui lance la commande d'Argon) devient, par l'amorce, un lien vers lui ;
  l'amorce refuse (destruction) si l'un des deux n'est pas 3.13 ; la machine revérifie et écrit les deux versions au journal.
- **C2** — la course ne part pas si le signe de vie n'est pas vérifié par `ls-remote` : refus avant la course (arrêt propre,
  versé sur la branche de refus), jamais une course détruite en marche par le contrôle du pilote à T0 + 30 min.
- **C3** — à la reprise du conteneur, le versement passe par une copie de nom neuf (`…-versement-interrompue-v1`) : une
  poussée finale manquée avant la reprise (copie `…-versement` restée sur le disque) n'empêche plus le versement.

Ce qui suit décrit la v2 :

Version 2 (R12 : `hote_durable_a1_v3.py`, la v1, inchangée). C'est la v1, plus **seulement** :

- une machine à **une** carte, ce que Vast loue (R-1511 : sur Vast, toutes les offres `num_gpus=0` sont des volumes de stockage,
  `resource_type` « disk », non louables comme machines ; sonde v10 réussie sur une machine « gpu », R-1527) : offre
  `resource_type` « gpu », `num_gpus` = 1, `cpu_ram` ≥ 8 000 Mo, cœurs ≥ 4, disque ≥ 30, fiabilité ≥ 0,98, prix ≤ 0,40 USD/h
  (vérification de la sonde v10, reprise telle quelle) ; la carte n'est pas utilisée ;
- deux GO lus par le pilote sur `main`, par la garde de `main` : **GO-2026-11-05-03** (la machine, 35 USD exactement, cité en tête
  de la ligne de location) et **GO-2026-11-04-06** (la course, 400 USD exactement, inchangé) ; la machine les revérifie ;
- les corrections des sondes v2 à v10 qui touchent la location, l'inventaire, la minuterie, le registre des GO et le versement
  (liste fermée, une ligne par point avec le numéro de l'additif d'origine : `rapport-redaction-v3-v2.md`, section 2) ; là où une
  correction de sonde contredit le texte v3 (données réelles, non factices), le texte prime et l'écart est écrit au rapport.

Côté pilote, le client de Vast est celui de la sonde v10, éprouvé en réel (`ClientPilote`), avec la seule différence que la clé
d'Argon est permise dans le corps (la seule clé de modèle) et masquée partout. Côté machine, la séquence est celle de la v1 ; la
minuterie de destruction (script de démarrage, sans Python) est celle de la sonde v10, à l'échéance de la machine.

Mode jouet des essais : aucune location, aucun appel de modèle, aucun réseau (dépôts locaux, Vast simulé par un fichier).
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import time
from contextlib import redirect_stderr
from pathlib import Path

try:  # paquet (essais) ou fichier seul (machine, pilote : `python3 -I -B …/hote_durable_a1_v3_v3.py`)
    from . import hote_durable_a1_v3 as h
    from . import sonde_hote_durable_a1_v3_v10 as s10
except ImportError:  # la v10 charge elle-même la v1 et la sonde v1 ; on reprend **son** objet `h` (une seule classe Refus)
    _ici = Path(__file__).resolve().parent
    _spec = importlib.util.spec_from_file_location("sonde_hote_durable_a1_v3_v10", _ici / "sonde_hote_durable_a1_v3_v10.py")
    s10 = importlib.util.module_from_spec(_spec)
    sys.modules["sonde_hote_durable_a1_v3_v10"] = s10
    _spec.loader.exec_module(s10)
    h = s10.h

VERSION = "hote-durable-a1-v3-v3"
GO_MACHINE, MONTANT_GO_MACHINE_USD = "GO-2026-11-05-03", 35.0  # machine « gpu » à une carte (R-1534) ; enveloppe 35 USD
GO_COURSE, MONTANT_GO_COURSE_USD = h.GO_ATTENDU, h.PLAFOND_COURSE_USD  # GO-2026-11-04-06, 400 USD : inchangés
ETIQUETTE = "a1-v3-troisieme-v1"  # étiquette de la machine de la course (celle de la v1), contrôlée trois fois (f8)
BRANCHE_VIE = "donnees/attaque-goodhart-v3-a1v3-troisieme-signe-de-vie-v1"  # m2 : signe de vie, branche orpheline
AMORCE = "scripts/amorce_hote_durable_a1_v3_v3.sh"
MODULE = "src/controle_ia/hote_durable_a1_v3_v3.py"
MODULES = ("hote_durable_a1_v3.py", "hote_durable_a1_v3_v3.py", "sonde_hote_durable_a1_v3.py", "sonde_hote_durable_a1_v3_v10.py")
PROTEGEES = s10.PROTEGEES  # 58936096, 58936099, 58936100 : jamais touchées
DUREE_MACHINE_S = int(h.DUREE_MAX_MACHINE_H * 3600)  # 80 h : plafond de vie écrit (texte v3, section 8)
DEMARRAGE_MAX_S = 600       # M-B : part de l'échéance absolue réservée au démarrage
MARGE_MINUTERIE_S = 3600    # après les 80 h : scellement, versement borné, destruction
RESERVE_VERSEMENT_S = 3600  # la garde arrête la course au plus tard 1 h avant l'échéance absolue (versement compris)
VIE_APRES_ECHEANCE_S = 600  # le conteneur vit 10 min après l'échéance, puis le principal attend la minuterie
ATTENTE_MINUTERIE_S = 300   # m-b
BORNE_SIGNE_DE_VIE_S = 1800  # m2 : T0 + 30 min
PREMIER_CONTROLE_S = 2400    # M-A : premier contrôle du pilote à T0 + 40 min
DELAI_GIT_S = 240            # chaque appel de git sur la machine (versement borné, m1)
ESSAIS_POUSSEE, ATTENTE_POUSSEE_S = 4, 60  # au pire 3 × 240 + 4 × (240 + 240 + 60) = 2 880 s < RESERVE_VERSEMENT_S
PLAFOND_LOCATION_USD = MONTANT_GO_MACHINE_USD
# Clés de modèle interdites partout, sauf CLE_ARGON (la seule, portée jusqu'au relais) ; même liste que l'amorce v2 (f2).
CLES_INTERDITES = re.compile(r"^(GEMINI.*|ANTHROPIC.*|OPENAI.*|MOONSHOT.*|KIMI.*|RR_.*API_KEY.*)$")
MOTIF_AMORCE = "GEMINI*|ANTHROPIC*|OPENAI*|MOONSHOT*|KIMI*|RR_*API_KEY*"
SECRETS_PILOTE = ("CLE_ARGON",) + s10.SECRETS_PILOTE  # GH_TOKEN, VAST_API_KEY et variables du mandataire (v6 a), masqués
FICHIERS_DEMARRAGE = ("a1v3-minuterie.txt", "a1v3-minuterie.log", "a1v3-temps.txt", "amorce-a1v3-v3.log", "a1v3-memoire.txt")
DETRUIRE_MAINTENANT = "a1v3-detruire-maintenant"  # posé par le script de démarrage si l'amorce refuse (code 2) : rien n'a tourné
CODE_REFUS_AMORCE = 2
PYTHON_IMAGE = "/usr/local/bin/python3"     # C1 : l'interpréteur 3.13 de l'image (`python:3.13-bookworm`)
PYTHON_CONFIGURATION = "/usr/bin/python3"   # C1 : chemin écrit dans la configuration gelée (commande d'Argon) ; Debian : 3.11
VERSION_PYTHON = "3.13"


def version_python(chemin: str) -> tuple[str, str]:
    """C1 : (« 3.13 », « Python 3.13.x ») de l'interpréteur ; (« illisible », motif) s'il ne répond pas."""
    try:
        court = h.lancer([chemin, "-c", "import sys; print('%d.%d' % sys.version_info[:2])"], delai=60)
        long = h.lancer([chemin, "--version"], delai=60)
    except (OSError, subprocess.TimeoutExpired) as x:
        return "illisible", type(x).__name__
    if court.returncode != 0:
        return "illisible", f"code {court.returncode}"
    return (court.stdout.decode("utf-8", "replace").strip(),
            (long.stdout + long.stderr).decode("utf-8", "replace").strip().splitlines()[0][:80] if (long.stdout + long.stderr).strip() else "?")


def cles_interdites(environ: dict) -> list[str]:
    return sorted(k for k, v in environ.items() if v and CLES_INTERDITES.match(k))


def verifier_go_exact(chemin_registre: Path, chemin_garde: Path, go_id: str, attendu: str, montant_usd: float,
                      aujourd_hui: dt.date) -> dict:
    """Comme `verifier_go` de la v1, pour un GO nommé : la garde de `main` telle quelle (type, Lazar, validité, révocation,
    extensions, R-389), puis un plafond d'exactement `montant_usd` sur la ligne et sur chaque extension."""
    if go_id != attendu:
        raise h.Refus(f"GO {go_id} : {attendu} exigé ici (aucun autre GO)")
    garde = h.charger_garde(chemin_garde, chemin_registre)
    tampon = io.StringIO()
    try:
        with redirect_stderr(tampon):
            garde.decider(f"GO_ID={go_id} vastai create instance 0", aujourd_hui)
    except SystemExit as e:
        if e.code not in (0, None):
            raise h.Refus(f"garde de main : {tampon.getvalue().strip()}") from None
    lignes = h.lignes_du_go(chemin_registre, go_id)
    if not lignes:
        raise h.Refus(f"{go_id} absent du registre")
    for cellules in lignes:
        m = h.MONTANT.match(cellules[4])
        if not m or abs(float(m.group(1).replace(",", ".")) - montant_usd) > 1e-9:
            raise h.Refus(f"{go_id} : plafond « {cellules[4]} » au lieu de exactement {montant_usd:g} USD")
    return {"go": go_id, "lignes": len(lignes), "plafond_usd": montant_usd,
            "registre_sha256": h.sha256_fichier(chemin_registre), "echeance": lignes[0][5]}


def cout_maximal_usd(dph: float) -> float:
    """M-B, f-2 : borne comptée depuis la création ; la minuterie détruit au plus tard à l'échéance absolue (création + 10 min
    + 80 h + 1 h) ; si ses destructions sont toutes refusées, le conteneur sort 10 min plus tard, après 5 min d'attente.
    Hors borne : une machine qui ne lance jamais son script (bornée par `controler`, donc par une session) et une machine
    arrêtée par l'hôte (stockage seul ; la session qui reprend décide, texte v3, section 8)."""
    return dph * (DEMARRAGE_MAX_S + DUREE_MACHINE_S + MARGE_MINUTERIE_S + VIE_APRES_ECHEANCE_S + ATTENTE_MINUTERIE_S) / 3600


def verifier_plafond(dph: float, plafond_usd: float = PLAFOND_LOCATION_USD) -> float:
    c = cout_maximal_usd(dph)
    if c > plafond_usd:
        raise h.Refus(f"coût de la machine au plus {c:.4f} USD > plafond {plafond_usd:g} USD ({GO_MACHINE})")
    return c


def echeance_absolue(t_creation: dt.datetime) -> int:
    return int(t_creation.timestamp()) + DEMARRAGE_MAX_S + DUREE_MACHINE_S + MARGE_MINUTERIE_S


# --- script de démarrage : la minuterie d'abord, sans Python (sonde v10, à l'échéance de la machine) ------------------------

MINUTERIE = r'''
ECH="$1"; R="$2"; API="$3"; FIN="$4"; J="$R/a1v3-minuterie.log"
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH, fin de vie $FIN" >> "$J"
echo "$$" > "$R/a1v3-minuterie.pid"
appel() {  # appel METHODE ADRESSE : imprime le corps (GET) ou le code HTTP ; curl, sinon python3 (m-c)
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
while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/a1v3-detruire-maintenant" ]; do sleep 5; done
[ -e "$R/a1v3-detruire-maintenant" ] && echo "$(date -u +%FT%TZ) destruction demandée avant l'échéance (amorce en refus : rien n'a tourné)" >> "$J"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) identifiant illisible : aucun geste" >> "$J"; exit 3;; esac
case " 58936096 58936099 58936100 " in *" $CONTAINER_ID "*) echo "$(date -u +%FT%TZ) instance protégée : aucun geste" >> "$J"; exit 3;; esac
LAB=$(appel GET "$API/instances/$CONTAINER_ID/" | grep -o '"label": *"[^"]*"' | head -1)
if [ -n "$LAB" ] && ! printf '%s' "$LAB" | grep -q '"a1-v3-troisieme-v1"'; then
    echo "$(date -u +%FT%TZ) étiquette lue $LAB, pas a1-v3-troisieme-v1 : aucun geste" >> "$J"; exit 3
fi
[ -n "$LAB" ] || echo "$(date -u +%FT%TZ) étiquette non lue : destruction par l'identifiant posé par Vast" >> "$J"
n=0
while :; do  # m-a : la minuterie ne fait jamais d'arrêt ; le DELETE recommence chaque minute jusqu'à la fin de vie
    n=$((n + 1)); c=$(appel DELETE "$API/instances/$CONTAINER_ID/")
    echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID (essai $n) : HTTP $c" >> "$J"
    case "$c" in 2??) exit 0;; esac
    [ "$(date +%s)" -lt $((FIN - 60)) ] || { echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue avant la fin de vie" >> "$J"; exit 4; }
    sleep 60
done
'''


def script_de_demarrage(commit_prive: str) -> str:
    """Processus principal du conteneur. Ordre : (1) minuterie détachée (`setsid`, sans Python), échéance = minimum de
    l'échéance absolue du pilote (M-B) et de départ + 80 h + 1 h, gardée sur disque (une reprise garde l'échéance d'origine) ;
    (2) `curl` installé s'il manque, sous `timeout` (f-1) ; (3) clone partiel, `sparse-checkout`, chronométré (m5, f-d) ;
    (4) amorce sous `timeout` borné par la fin de vie (m-2) ; si elle refuse (code 2) ou manque, destruction demandée à la
    minuterie (rien n'a tourné) et plus rien n'est lancé, même à une reprise ; (5) vie jusqu'à la fin de vie, puis attente
    de la fin de la minuterie (m-b)."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit_prive):
        raise h.Refus("commit du dépôt privé : hash complet de 40 caractères exigé")
    m64 = base64.b64encode(MINUTERIE.encode()).decode("ascii")
    return f'''set -u
R="${{RACINE_A1V3:-/root}}"; case "$R" in /*) ;; *) R=/root;; esac
API="${{API_VAST:-{h.API_VAST}}}"; case "$API" in https://*) ;; *) API={h.API_VAST};; esac
D="${{A1V3_DUREE_S:-{DUREE_MACHINE_S}}}"; case "$D" in ''|*[!0-9]*) D={DUREE_MACHINE_S};; esac; [ "$D" -le {DUREE_MACHINE_S} ] || D={DUREE_MACHINE_S}
MARGE="${{A1V3_MARGE_S:-{MARGE_MINUTERIE_S}}}"; case "$MARGE" in ''|*[!0-9]*) MARGE={MARGE_MINUTERIE_S};; esac; [ "$MARGE" -le {MARGE_MINUTERIE_S} ] || MARGE={MARGE_MINUTERIE_S}
APRES="${{A1V3_VIE_APRES_S:-{VIE_APRES_ECHEANCE_S}}}"; case "$APRES" in ''|*[!0-9]*) APRES={VIE_APRES_ECHEANCE_S};; esac; [ "$APRES" -le {VIE_APRES_ECHEANCE_S} ] || APRES={VIE_APRES_ECHEANCE_S}
ABS="${{ECHEANCE_UTC_S:-}}"; case "$ABS" in ''|*[!0-9]*) ABS="";; esac
if [ -s "$R/a1v3-minuterie.txt" ]; then read T0 ECH < "$R/a1v3-minuterie.txt"
else T0=$(date +%s); ECH=$((T0 + D + MARGE)); if [ -n "$ABS" ] && [ "$ABS" -lt "$ECH" ]; then ECH=$ABS; fi
     echo "$T0 $ECH" > "$R/a1v3-minuterie.txt"; fi
FINVIE=$((ECH + APRES))
echo {m64} | base64 -d > "$R/a1v3-minuterie.sh"
setsid bash "$R/a1v3-minuterie.sh" "$ECH" "$R" "$API" "$FINVIE" < /dev/null >> "$R/a1v3-minuterie.log" 2>&1 &
PM=$!
reste() {{ r=$(( FINVIE - $(date +%s) )); [ "$r" -gt 1 ] && echo "$r" || echo 1; }}
borne() {{ r=$(reste); [ "$r" -lt "$1" ] && echo "$r" || echo "$1"; }}
command -v curl >/dev/null || timeout -k 5 "$(borne 120)" sh -c 'apt-get update -qq && apt-get install -y -qq curl git ca-certificates >/dev/null 2>&1'
echo "demarrage $(date -u +%FT%TZ) depart $T0 echeance $ECH absolue ${{ABS:-aucune}} curl $(command -v curl >/dev/null && echo oui || echo NON)" >> "$R/a1v3-temps.txt"
if [ ! -e "$R/{DETRUIRE_MAINTENANT}" ] && [ ! -d "$R/amorce-depot/.git" ]; then
  t=$(date +%s)
  (command -v git >/dev/null || timeout -k 5 "$(borne 120)" sh -c 'apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null')
  A='!f() {{ echo username=x-access-token; echo "password=${{GH_TOKEN}}"; }}; f'
  git init -q "$R/amorce-depot" && git -C "$R/amorce-depot" remote add origin "$DEPOT_URL" &&
  git -C "$R/amorce-depot" sparse-checkout set scripts src/controle_ia &&
  timeout -k 5 "$(borne 600)" git -C "$R/amorce-depot" -c credential.helper="$A" fetch -q --filter=blob:none --depth 1 origin {commit_prive} &&
  timeout -k 5 "$(borne 600)" git -C "$R/amorce-depot" -c credential.helper="$A" checkout -q --detach FETCH_HEAD
  echo "clone $? en $(( $(date +%s) - t )) s" >> "$R/a1v3-temps.txt"
fi
if [ -e "$R/{DETRUIRE_MAINTENANT}" ]; then
  echo "reprise après un refus de l'amorce : rien n'est lancé" >> "$R/a1v3-temps.txt"; FINVIE=$(( $(date +%s) + APRES ))
elif [ -f "$R/amorce-depot/{AMORCE}" ]; then
  timeout -k 10 "$(reste)" bash "$R/amorce-depot/{AMORCE}" 2>&1 | tee -a "$R/amorce-a1v3-v3.log"; CODE=${{PIPESTATUS[0]}}
  echo "amorce finie $(date -u +%FT%TZ) code $CODE" >> "$R/a1v3-temps.txt"
  if [ "$CODE" = "{CODE_REFUS_AMORCE}" ]; then
    echo "amorce en refus : destruction demandée à la minuterie" >> "$R/a1v3-temps.txt"; : > "$R/{DETRUIRE_MAINTENANT}"; FINVIE=$(( $(date +%s) + APRES ))
  fi
else
  echo "amorce absente du clone : destruction demandée à la minuterie" >> "$R/a1v3-temps.txt"; : > "$R/{DETRUIRE_MAINTENANT}"; FINVIE=$(( $(date +%s) + APRES ))
fi
while [ "$(date +%s)" -lt "$FINVIE" ]; do sleep 5; done
[ -s "$R/a1v3-minuterie.pid" ] && PM=$(cat "$R/a1v3-minuterie.pid")
t=$(date +%s); while kill -0 "$PM" 2>/dev/null && [ $(( $(date +%s) - t )) -lt {ATTENTE_MINUTERIE_S} ]; do sleep 2; done
echo "fin du principal $(date -u +%FT%TZ)" >> "$R/a1v3-temps.txt"
'''


def corps(commit_prive: str, commit_public: str, sha_texte: str, commit_registre: str, offre: dict,
          secrets: dict[str, str], echeance_utc_s: int) -> dict:
    for nom, valeur, motif in (("commit_prive", commit_prive, r"[0-9a-f]{40}"), ("commit_public", commit_public, r"[0-9a-f]{40}"),
                               ("sha_texte", sha_texte, r"[0-9a-f]{64}"), ("commit_registre", commit_registre, r"[0-9a-f]{40}")):
        if not isinstance(valeur, str) or not re.fullmatch(motif, valeur):
            raise h.Refus(f"{nom} : forme exacte exigée ({motif})")
    manquants = [k for k in ("CLE_ARGON", "GH_TOKEN") if not secrets.get(k)]
    if manquants:
        raise h.Refus(f"secrets absents de l'environnement : {', '.join(manquants)}")
    if not isinstance(echeance_utc_s, int) or isinstance(echeance_utc_s, bool) or echeance_utc_s <= 0:
        raise h.Refus("échéance absolue (M-B) : entier de secondes exigé")
    env = {"COMMIT_PRIVE": commit_prive, "COMMIT_PUBLIC": commit_public, "SHA_TEXTE": sha_texte,
           "COMMIT_REGISTRE": commit_registre, "GO_ID": GO_COURSE, "GO_MACHINE": GO_MACHINE,
           "PRIX_H_USD": f"{offre['dph_total']:.6f}", "DEPOT_URL": h.DEPOT_PRIVE, "ECHEANCE_UTC_S": str(echeance_utc_s),
           "CLE_ARGON": secrets["CLE_ARGON"], "GH_TOKEN": secrets["GH_TOKEN"]}
    if cles_interdites(env):
        raise h.Refus("clé de modèle autre que CLE_ARGON dans le corps")
    b64 = base64.b64encode(script_de_demarrage(commit_prive).encode("utf-8")).decode("ascii")
    return {"image": h.IMAGE, "disk": 30, "label": ETIQUETTE, "env": env,
            "script": f"echo {b64} | base64 -d > /root/demarrage-a1v3-v3.sh && bash /root/demarrage-a1v3-v3.sh"}


# --- côté pilote : le client de la sonde v10 (éprouvé en réel), la clé d'Argon permise et masquée -------------------------


class ClientPiloteV3(s10.ClientPilote):
    """`vastai` dans un sous-processus, `VAST_API_KEY` par son nom, variables du mandataire seules transmises (v6 a), délai
    rendu en `Refus` sans la ligne de commande (M-1), aucune sortie brute écrite (f-a), certificat refusé sans marqueur (v6 b),
    réponse de création catégorisée sur les deux sorties (v7 a, v8 a) ; destruction avec `-y`, instances protégées (M2, f8)."""

    def __init__(self, environ: dict, outil: str = "vastai"):
        super().__init__(environ, outil)
        self.secrets = {k: environ.get(k, "") for k in SECRETS_PILOTE}  # la clé d'Argon est masquée aussi

    def creer(self, offre_id: int, c: dict) -> int:
        if cles_interdites(c["env"]):
            raise s10.RefusAvantAppel("clé de modèle autre que CLE_ARGON dans le corps : rien créé")
        if any(ch.isspace() or ch in "\"'" for v in c["env"].values() for ch in v):
            raise s10.RefusAvantAppel("valeur d'environnement avec espace ou guillemet : refus (forme -e K=V)")
        env = {k: self.environ[k] for k in ("PATH", "HOME", "LANG", "VAST_API_KEY") + s10.VARIABLES_MANDATAIRE
               if self.environ.get(k)}
        args = s10.arguments_de_creation(offre_id, c)
        try:
            r = subprocess.run([self.outil, *args], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               timeout=s10.DELAI_VASTAI_S)
        except subprocess.TimeoutExpired:  # M-1 : le message de l'exception porte la ligne de commande, secrets compris
            raise h.Refus(f"vastai {' '.join(args[:2])} : délai dépassé ({s10.DELAI_VASTAI_S} s)") from None
        sortie = (r.stdout or b"").decode("utf-8", "replace")
        erreur = (r.stderr or b"").decode("utf-8", "replace")
        certificat = any(m in (r.stderr or b"") for m in s10.MOTS_CERTIFICAT)
        secrets = [v for v in self.secrets.values() if v] + [c["env"]["GH_TOKEN"], c["env"]["CLE_ARGON"]]
        cat, _ = s10.categoriser_reponse(sortie, secrets)
        if cat == "illisible" and certificat:
            raise s10.RefusCertificat(f"vastai {' '.join(args[:2])} : appel non parvenu à Vast (certificat) ; code "
                                      f"{r.returncode}")
        return s10.lire_reponse_de_creation(sortie, secrets, erreur, r.returncode)


def louer(a, client=None, aujourd_hui=None, environ=None, maintenant=None) -> int:
    """Partie pilote : GO de la machine et de la course, offre, borne de dépense, création ; état et ligne pour
    `registres/etat.md`. Rend 0 (créée, ou vérification seule) ou 2 (refus)."""
    environ = dict(os.environ) if environ is None else environ
    jl = Path(a.journal_local)
    j = h.Journal(jl, {k: environ.get(k, "") for k in SECRETS_PILOTE})
    ident_f, incertain_f, etat_f = (Path(str(jl) + x) for x in (".identifiant", ".creation-incertaine", ".etat.json"))
    try:
        if ident_f.exists() or incertain_f.exists():  # m3, m-1 : une seule location ; incertaine : inventaire d'abord
            raise h.Refus("une location de l'hôte durable v3 a déjà eu lieu ou est incertaine (R12) : inventaire d'abord")
        if environ.get("GO_ID") != GO_MACHINE:  # f7
            raise h.Refus(f"GO_ID={GO_MACHINE} exigé en tête de la ligne de location (f7)")
        if cles_interdites(environ):
            raise h.Refus(f"clé de modèle autre que CLE_ARGON dans l'environnement du pilote : {cles_interdites(environ)}")
        aujourd_hui = aujourd_hui or dt.datetime.now(dt.timezone.utc).date()
        gm = verifier_go_exact(Path(a.registre_main), Path(a.garde_main), a.go_machine, GO_MACHINE, MONTANT_GO_MACHINE_USD,
                               aujourd_hui)
        gc = h.verifier_go(Path(a.registre_main), Path(a.garde_main), a.go, MONTANT_GO_COURSE_USD, aujourd_hui)
        j.ecrire(f"{VERSION} : machine {gm['go']} ({gm['plafond_usd']:g} USD) et course {gc['go']} ({gc['plafond_usd']:g} USD) "
                 f"acceptés par la garde de main ; registre {gc['registre_sha256']}")
        offres = json.loads(Path(a.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        o = s10.offre_la_moins_chere_sonde(offres, int(a.offre))  # v9 a : « gpu », une carte, cpu_ram ≥ 8 000 Mo, …
        secrets = {k: environ.get(k, "") for k in ("CLE_ARGON", "GH_TOKEN")}
        if a.verifier_seulement:
            cout = verifier_plafond(o["dph_total"])
            c = corps(a.commit_prive, a.commit_public, a.sha_texte, a.commit_registre, o, secrets,
                      echeance_absolue(maintenant or dt.datetime.now(dt.timezone.utc)))
            lg = s10.longueurs_de_creation(o["id"], c)
            j.ecrire(f"offre {o['id']} ({o.get('gpu_name')}) à {o['dph_total']} USD/h ; coût de la machine au plus {cout:.4f} "
                     f"USD ≤ {PLAFOND_LOCATION_USD:g} ; longueurs : --args {lg['args_c']}, --env {lg['env']}, commande "
                     f"{lg['commande']}")
            j.ecrire("vérification seulement : rien créé (variables : " + ", ".join(sorted(c["env"])) + ")")
            return 0
        client = client or ClientPiloteV3(environ)
        autres = []  # v8 b : sur « no_such_ask », au plus 4 autres offres conformes, par prix croissant
        for x in sorted((x for x in offres if isinstance(x, dict) and x.get("id") != o["id"]),
                        key=lambda x: (x.get("dph_total") if isinstance(x.get("dph_total"), (int, float)) else 1e9,
                                       str(x.get("id")))):
            try:
                autres.append(s10.verifier_offre_sonde([x], x.get("id")))
            except h.Refus:
                continue
        candidates = [o] + autres[:s10.ESSAIS_NO_SUCH_ASK - 1]
        ident = None
        for n, oc in enumerate(candidates, 1):
            oc = s10.verifier_offre_sonde(offres, oc["id"])
            cout = verifier_plafond(oc["dph_total"])
            t_creation = maintenant or dt.datetime.now(dt.timezone.utc)
            echeance = echeance_absolue(t_creation)
            c = corps(a.commit_prive, a.commit_public, a.sha_texte, a.commit_registre, oc, secrets, echeance)
            lg = s10.longueurs_de_creation(oc["id"], c)
            j.ecrire(f"essai {n}/{len(candidates)} : offre {oc['id']} ({oc.get('gpu_name')}) à {oc['dph_total']} USD/h ; coût "
                     f"au plus {cout:.4f} USD ≤ {PLAFOND_LOCATION_USD:g} ; longueurs : --args {lg['args_c']}, --env "
                     f"{lg['env']}, commande {lg['commande']}")
            try:
                ident = client.creer(oc["id"], c)
                j.ecrire(f"réponse de création : contrat {ident} (essai {n})")
                o = oc
                break
            except s10.RefusNoSuchAsk as e:
                j.ecrire(f"essai {n} refusé : {e}")
                if n == len(candidates):
                    raise s10.RefusNoSuchAsk(f"{n} essai(s), tous « no_such_ask » : refus final (Vast : rien créé)") from None
            except s10.RefusAvantAppel:  # certificat, erreur de Vast avec success faux, gardes : sans marqueur
                raise
            except h.Refus as e:  # m-1 : réponse illisible, erreur sans success faux, délai : marqueur, arrêt
                incertain_f.write_text(f"{h.maintenant()} {str(e)[:120]}\n")
                raise
        t0 = t_creation
        fmt = "%Y-%m-%dT%H:%M:%SZ"
        etat = {"identifiant": ident, "etiquette": ETIQUETTE, "t0_utc": t0.strftime(fmt),
                "borne_signe_de_vie_utc": (t0 + dt.timedelta(seconds=BORNE_SIGNE_DE_VIE_S)).strftime(fmt),
                "echeance_finale_utc": dt.datetime.fromtimestamp(echeance, dt.timezone.utc).strftime(fmt),
                "controles_utc": [(t0 + dt.timedelta(seconds=PREMIER_CONTROLE_S)).strftime(fmt),
                                  (dt.datetime.fromtimestamp(echeance, dt.timezone.utc)
                                   + dt.timedelta(seconds=VIE_APRES_ECHEANCE_S + ATTENTE_MINUTERIE_S + 300)).strftime(fmt)],
                "prix_h_usd": o["dph_total"], "cout_maximal_usd": round(cout, 4), "go_machine": GO_MACHINE, "go_course": GO_COURSE,
                "version": VERSION}
        ident_f.write_text(f"{ident}\n")
        etat_f.write_text(json.dumps(etat, ensure_ascii=False, indent=1) + "\n")
        j.ecrire(f"machine créée : identifiant {ident} (offre {o['id']}, {o['dph_total']} USD/h), étiquette {ETIQUETTE} ; T0 "
                 f"{etat['t0_utc']} ; signe de vie attendu avant {etat['borne_signe_de_vie_utc']} ; échéance finale "
                 f"{etat['echeance_finale_utc']}")
        j.ecrire("LIGNE POUR registres/etat.md : " + ligne_etat(etat))
        return 0
    except (h.Refus, OSError, ValueError, KeyError) as e:
        j.ecrire(f"REFUS : {e}")
        return 2


def ligne_etat(e: dict) -> str:
    return (f"- Hôte durable v3 d'A1-v3 ({GO_MACHINE} ; course {GO_COURSE}) : instance **{e['identifiant']}**, étiquette "
            f"`{e['etiquette']}`, créée {e['t0_utc']}, échéance {e['echeance_finale_utc']} ; contrôles à "
            f"{' et '.join(e['controles_utc'])} ; toute session qui reprend lance `hote_durable_a1_v3_v3.py controler` "
            "(étiquette contrôlée ; destruction par l'identifiant, avec -y, seulement sans signe de vie à T0 + 30 min).")


def _journal_pilote(a, environ) -> h.Journal:
    return h.Journal(Path(a.journal_local), {k: environ.get(k, "") for k in SECRETS_PILOTE})


def controler(a, client=None, signe_de_vie=None, maintenant=None, environ=None) -> int:
    """m2, M-A, f-6, v7 b. Codes : 0 absente ; 1 détruite par le pilote (aucun signe de vie à T0 + 30 min : rien n'a tourné) ;
    2 refus (étiquette, protégée, état illisible) ; 3 destruction demandée mais encore listée ; 5 listée avant ses bornes :
    recontrôler ; 6 délai dépassé ou `ls-remote` en échec : recontrôler ; 7 encore listée après l'échéance finale : **aucun
    geste**, la session décide (machine arrêtée par l'hôte, données possibles sur son disque : texte v3, section 8)."""
    environ = dict(os.environ) if environ is None else environ
    j = _journal_pilote(a, environ)
    try:
        e = json.loads(Path(a.etat).read_text())
        ident = int(e["identifiant"])
        if ident in PROTEGEES:
            raise h.Refus(f"instance {ident} protégée : jamais touchée")
        now = maintenant or dt.datetime.now(dt.timezone.utc)
        lire = lambda k: dt.datetime.strptime(e[k], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        client = client or ClientPiloteV3(environ)
        listees = [i for i in client.instances() if i.get("id") == ident]
        if not listees:
            j.ecrire(f"contrôle : instance {ident} absente de l'inventaire (détruite) ; rien à faire")
            return 0
        lab = listees[0].get("label")
        if lab != ETIQUETTE:
            raise h.Refus(f"instance {ident} : étiquette {lab!r}, pas {ETIQUETTE} : aucun geste (f8)")
        etat_vast = listees[0].get("actual_status")
        if now >= lire("echeance_finale_utc") + dt.timedelta(seconds=VIE_APRES_ECHEANCE_S):
            j.ecrire(f"contrôle : instance {ident} ({etat_vast}) encore listée après l'échéance finale : AUCUN GESTE ; la session "
                     "décide (texte v3, section 8 : une machine arrêtée garde ses données) ; consigner")
            return 7
        vie = signe_de_vie() if signe_de_vie else s10.branche_existe(BRANCHE_VIE, environ)
        if now >= lire("borne_signe_de_vie_utc") and not vie:
            j.ecrire(f"contrôle : aucun signe de vie à T0 + 30 min (m2) : destruction de {ident} par son identifiant (-y)")
            client.detruire(ident)
            if [i for i in client.instances() if i.get("id") == ident]:
                j.ecrire(f"instance {ident} encore listée après la destruction : recommencer, puis consigner")
                return 3
            j.ecrire(f"instance {ident} détruite par le pilote, vérifiée par l'inventaire : consigner dans registres/arrets.md")
            return 1
        j.ecrire(f"contrôle : instance {ident} ({etat_vast}) ; signe de vie {'oui' if vie else 'non'} ; encore listée : "
                 f"RECONTRÔLER (au plus tard {e.get('controles_utc', ['?'])[-1]})")
        return 5
    except s10.RefusRecontroler as x:
        j.ecrire(f"RECONTRÔLER : {x}")
        return 6
    except subprocess.TimeoutExpired as x:
        j.ecrire(f"DÉLAI DÉPASSÉ : {x.cmd[0] if isinstance(x.cmd, (list, tuple)) else 'commande'} ; recontrôler")
        return 6
    except (h.Refus, OSError, ValueError, KeyError) as x:
        j.ecrire(f"REFUS : {x}")
        return 6 if "délai dépassé" in str(x) else 2


def relever_facturation(a, client=None, environ=None) -> int:
    """v10 b : `vastai show instance` ; seuls `CHAMPS_FACTURATION` (et l'identifiant, l'étiquette) sortent ; codes : 0 écrit,
    2 refus (étiquette, protégée, état illisible), 6 délai ou échec de `vastai` (recontrôler)."""
    environ = dict(os.environ) if environ is None else environ
    j = _journal_pilote(a, environ)
    try:
        e = json.loads(Path(a.etat).read_text())
        ident = int(e["identifiant"])
        if ident in PROTEGEES:
            raise h.Refus(f"instance {ident} protégée : jamais touchée")
        client = client or ClientPiloteV3(environ)
        f = client.facturation(ident)
        if f.get("label") not in (None, ETIQUETTE):
            raise h.Refus(f"instance {ident} : étiquette {f.get('label')!r}, pas {ETIQUETTE} : aucun relevé écrit")
        champs = {k: f[k] for k in s10.CHAMPS_FACTURATION if k in f}
        j.ecrire(f"relevé de facturation de l'instance {ident} : {json.dumps(champs, ensure_ascii=False, sort_keys=True)}")
        return 0
    except subprocess.TimeoutExpired:
        j.ecrire("DÉLAI DÉPASSÉ : vastai ; recontrôler")
        return 6
    except (h.Refus, OSError, ValueError, KeyError) as x:
        j.ecrire(f"REFUS : {x}")
        return 6 if ("délai dépassé" in str(x) or "code" in str(x)) else 2


# --- côté machine ----------------------------------------------------------------------------------------------------------


def git_octets(*args, cwd=None, gh_token: str = "", delai: float = DELAI_GIT_S) -> bytes:
    """Comme `h.git`, avec l'aide d'identification (v10 a : lecture paresseuse d'un clone partiel), mais rend des octets."""
    aide = ['-c', 'credential.helper=!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f']
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.environ.get("HOME", "/root"),
           "GH_TOKEN": gh_token, "GIT_TERMINAL_PROMPT": "0", "LANG": "C.UTF-8"}
    r = h.lancer(["git", *aide, *args], cwd=cwd, env=env, delai=delai)
    if r.returncode != 0:
        raise h.Refus(f"git {args[0]} : code {r.returncode}")
    return r.stdout


class MachineV3(h.Machine):
    """La séquence de la v1 ; ce qui change : dépense comptée depuis le départ du conteneur (m1) et course bornée par l'échéance
    absolue (M-B) ; deux GO revérifiés sur `main` ; dépôt privé en clone partiel lu avec l'aide d'identification (m5, v10 a) ;
    signe de vie (m2) ; journaux du démarrage versés (f5) ; versement borné, « partie de main » sans clone entier (m1, m5) ;
    fin et geste sur la machine qui attrapent toute exception (M1 b) ; étiquette et instances protégées contrôlées (f8)."""

    def __init__(self, r: h.Reglages, environ: dict[str, str], python_configuration: str = PYTHON_CONFIGURATION):
        super().__init__(r, environ)
        self.racine = r.travail.parent
        self.python_configuration = python_configuration  # C1
        t0 = None
        try:
            t0 = float((self.racine / "a1v3-minuterie.txt").read_text().split()[0])
        except (OSError, ValueError, IndexError):
            pass
        self.depart_conteneur = t0
        if t0 is not None:  # m1 : durée et coût comptés depuis le départ du conteneur (écrit par le script de démarrage)
            self.debut = time.monotonic() - max(0.0, time.time() - t0)

    def principal(self) -> int:
        journal = self.t / "journal-hote-a1-v3-troisieme-v1.log"
        if self.etat_fichier.exists():  # reprise du conteneur : jamais de relance (R12)
            self.j = h.Journal(journal, self.secrets)
            avant = self.etat_fichier.read_text().strip()
            self.j.ecrire(f"REPRISE du conteneur : état précédent « {avant} » ; rien n'est relancé")
            if avant == "verse":
                return self.se_detruire(True)
            self.nature_fin = "reprise_du_conteneur"
            return self.fin(h.BRANCHE_INTERROMPUE)
        self.t.mkdir(parents=True, exist_ok=False)
        self.j = h.Journal(journal, self.secrets)
        self.j.ecrire(f"{VERSION} ; machine {self.env.get('GO_MACHINE')} ; course {self.env.get('GO_ID')} ; prix {self.prix_h} "
                      f"USD/h ; plafond machine {self.r.plafond_machine_usd} USD, {self.r.duree_max_s / 3600:g} h ; identifiant "
                      f"{self.env.get('CONTAINER_ID', '?')} ; départ du conteneur {self.depart_conteneur}")
        self.etat("demarrage")
        try:
            self.preparer()
            self.etat("course")
            self.garder()
        except h.Refus as e:
            self.j.ecrire(f"REFUS : {e}")
            self.nature_fin = "refus_avant_course" if self.course is None else "refus_pendant_la_course"
        except Exception as e:  # jamais un repli silencieux : écrit, puis fin propre
            self.j.ecrire(f"EXCEPTION {type(e).__name__} : {self.j.masquer(str(e))[:500]}")
            self.nature_fin = "exception_de_l_hote"
        return self.fin(h.BRANCHE_DONNEES if self.course is not None else h.BRANCHE_REFUS)

    def env_relais(self) -> dict:  # C1 : `/usr/local/bin` d'abord (la v1 mettait `/usr/bin` d'abord)
        return {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8", "GEMINI_API_KEY": self.secrets["CLE_ARGON"]}

    def verifier_interpreteurs(self) -> None:
        """C1 : relais, course et chemin de la configuration gelée sous Python 3.13 ; les versions au journal ; sinon refus."""
        vus = {nom: (chemin, *version_python(chemin)) for nom, chemin in (("relais", self.r.python_relais),
               ("course", self.r.python_course), ("configuration gelée", self.python_configuration))}
        self.j.ecrire("interpréteurs (C1) : " + " ; ".join(f"{n} {c} : {lg}" for n, (c, _, lg) in vus.items()))
        faux = [f"{n} {c} ({v})" for n, (c, v, _) in vus.items() if v != VERSION_PYTHON]
        if faux:
            raise h.Refus(f"interpréteur autre que Python {VERSION_PYTHON} (C1) : {', '.join(faux)} : rien ne part")

    def _show(self, commit: str, chemin: str) -> bytes:
        try:
            return git_octets("show", f"{commit}:{chemin}", cwd=self.r.clone_prive, gh_token=self.secrets["GH_TOKEN"])
        except h.Refus:
            raise h.Refus(f"{chemin} illisible au commit {commit}") from None

    def preparer(self) -> None:
        r, e = self.r, self.env
        for k in ("CLE_ARGON", "GH_TOKEN", "COMMIT_PUBLIC", "SHA_TEXTE", "COMMIT_REGISTRE", "GO_ID", "GO_MACHINE", "PRIX_H_USD",
                  "ECHEANCE_UTC_S"):
            if not e.get(k):
                raise h.Refus(f"variable {k} absente")
        if cles_interdites(e):
            raise h.Refus(f"clé de modèle autre que CLE_ARGON dans l'environnement de la machine : {cles_interdites(e)}")
        if not (0 < self.prix_h <= h.PRIX_MAX_H_USD):
            raise h.Refus(f"prix horaire {self.prix_h} hors de ]0 ; {h.PRIX_MAX_H_USD}]")
        verifier_plafond(self.prix_h)
        self.verifier_interpreteurs()  # C1
        if not re.fullmatch(r"[0-9]{9,11}", e["ECHEANCE_UTC_S"]):
            raise h.Refus("ECHEANCE_UTC_S (échéance absolue du pilote, M-B) illisible")
        depart = self.depart_conteneur or time.time()
        reste = int(e["ECHEANCE_UTC_S"]) - RESERVE_VERSEMENT_S - depart  # M-B : 1 h gardée au versement avant la minuterie
        if reste <= 60:
            raise h.Refus(f"échéance absolue trop proche ({reste:.0f} s utiles) : rien ne part")
        r.duree_max_s = float(min(r.duree_max_s, reste))
        self.j.ecrire(f"durée de la course bornée à {r.duree_max_s:.0f} s (80 h au plus, échéance absolue moins 1 h)")
        gh, cr = self.secrets["GH_TOKEN"], e["COMMIT_REGISTRE"]
        jour = r.aujourd_hui or dt.datetime.now(dt.timezone.utc).date()
        # 1. Branches lues en clone partiel (m5), le canal sur PROFONDEUR_CANAL commits (v10 a)
        h.git("fetch", "-q", "--filter=blob:none", "--depth", "1", "origin",
              *[f"+refs/heads/{b}:refs/remotes/origin/{b}" for b in ("main", h.REF_SOURCES, h.REF_CONFIGURATION)],
              cwd=r.clone_prive, gh_token=gh, delai=DELAI_GIT_S)
        h.git("fetch", "-q", "--filter=blob:none", "--depth", str(s10.PROFONDEUR_CANAL), "origin",
              f"+refs/heads/{h.SOURCE_REGISTRE}:refs/remotes/origin/{h.SOURCE_REGISTRE}", cwd=r.clone_prive, gh_token=gh,
              delai=DELAI_GIT_S)
        # 2. GO sur main, par la garde de main (fichiers lus avec l'aide d'identification, v10 a)
        tete_main = h.git("rev-parse", "refs/remotes/origin/main", cwd=r.clone_prive, delai=DELAI_GIT_S).strip()
        reg_main, garde = self.t / "registre-go-main.md", self.t / "garde_calcul_main.py"
        reg_main.write_bytes(self._show(tete_main, "registres/go.md"))
        garde.write_bytes(self._show(tete_main, ".claude/hooks/garde_calcul.py"))
        g = h.verifier_go(reg_main, garde, e["GO_ID"], MONTANT_GO_COURSE_USD, jour)
        gm = verifier_go_exact(reg_main, garde, e["GO_MACHINE"], GO_MACHINE, MONTANT_GO_MACHINE_USD, jour)
        self.j.ecrire(f"GO accepté par la garde de main {tete_main} : {json.dumps(g, ensure_ascii=False)} ; machine : "
                      f"{json.dumps(gm, ensure_ascii=False)}")
        self.j.ecrire("grep main : " + " ; ".join(self._grep(reg_main, e["GO_ID"]) + self._grep(reg_main, GO_MACHINE)))
        # 3. Registre passé au lanceur : copie entière du canal au commit fixé, sans retouche, sans doublon (texte v3, section 4)
        if h.lancer(["git", "merge-base", "--is-ancestor", cr, f"refs/remotes/origin/{h.SOURCE_REGISTRE}"],
                    cwd=r.clone_prive, delai=DELAI_GIT_S).returncode != 0:
            raise h.Refus(f"commit du registre {cr} absent de la branche {h.SOURCE_REGISTRE} (ou au-delà de "
                          f"{s10.PROFONDEUR_CANAL} commits)")
        reg = self.t / "registre-go.md"
        reg.write_bytes(self._show(cr, "registres/go.md"))
        doubles = h.doublons_lecteur_du_lanceur(reg)
        if doubles:
            raise h.Refus(f"registre {cr} : identifiants en double {doubles} (le lanceur le refuserait)")
        h.verifier_go(reg, garde, e["GO_ID"], MONTANT_GO_COURSE_USD, jour)
        self.sha_registre = h.sha256_fichier(reg)
        self.j.ecrire(f"registre-go.md : commit {cr} de {h.SOURCE_REGISTRE}, aucun doublon, sha256 {self.sha_registre} ; grep : "
                      + " ; ".join(self._grep(reg, e["GO_ID"])))
        # 4. Signe de vie (m2), exigé (C2), puis la suite de la v1
        if not self.signe_de_vie():
            raise h.Refus("signe de vie non vérifié par ls-remote (C2) : la course ne part pas (le contrôle du pilote "
                          "détruirait à T0 + 30 min une course en marche)")
        self.extraire_sources()
        h.git("clone", "-q", r.depot_public, str(r.clone_public))
        h.git("checkout", "-q", "--detach", e["COMMIT_PUBLIC"], cwd=r.clone_public)
        if h.lancer(["git", "merge-base", "--is-ancestor", r.commit_code_gele, e["COMMIT_PUBLIC"]],
                    cwd=r.clone_public).returncode != 0:
            raise h.Refus(f"le commit {e['COMMIT_PUBLIC']} ne descend pas du code gelé {r.commit_code_gele}")
        texte = r.clone_public / h.NOM_TEXTE
        vu = h.sha256_fichier(texte) if texte.is_file() else None
        compagnon = Path(str(texte) + ".sha256")
        comp = compagnon.read_text().split()[0] if compagnon.is_file() else None
        if not (vu == e["SHA_TEXTE"] == comp):
            raise h.Refus(f"texte v3 : empreinte {vu}, attendue {e['SHA_TEXTE']}, compagnon {comp}")
        statut = h.git("status", "--porcelain", cwd=r.clone_public)
        if statut.strip():
            raise h.Refus("arbre du dépôt public modifié : " + statut[:200])
        self.j.ecrire(f"dépôt public {e['COMMIT_PUBLIC']} (descend de {r.commit_code_gele}) ; texte {vu} = compagnon ; "
                      "git status --porcelain vide")
        if not h.port_libre(r.port):
            raise h.Refus(f"port {r.port} déjà pris : un autre relais vit (Argon seul)")
        self.lancer_relais()
        self.verifier_seulement()
        self.lancer_course()

    def extraire_sources(self) -> None:
        """Comme la v1, mais `git archive` et `git show` avec l'aide d'identification (clone partiel, v10 a)."""
        r = self.r
        r.racine_sources.mkdir(parents=True, exist_ok=True)
        ref = f"refs/remotes/origin/{h.REF_SOURCES}"
        try:
            arch = git_octets("archive", ref, h.NUIT, "donnees/espece-seule-v1/collisionneur_v7.py", cwd=r.clone_prive,
                              gh_token=self.secrets["GH_TOKEN"])
        except h.Refus as x:
            raise h.Refus(f"git archive {ref} : {x}") from None
        with tarfile.open(fileobj=io.BytesIO(arch)) as tar:
            tar.extractall(r.racine_sources, filter="data")
        conf = self._show(f"refs/remotes/origin/{h.REF_CONFIGURATION}", h.CHEMIN_CONF_DANS_REF)
        (r.racine_sources / h.NUIT / "configuration-mini-course-kimi-argon-v3.json").write_bytes(conf)
        for chemin, attendu in r.empreintes.items():
            p = r.racine_sources / chemin
            vu = h.sha256_fichier(p) if p.is_file() else None
            if vu != attendu:
                raise h.Refus(f"pièce {chemin} : empreinte {vu}, attendue {attendu}")
        c = json.loads((r.racine_sources / h.NUIT / "configuration-mini-course-kimi-argon-v3.json").read_text())
        for nom, piece in c.get("pieces", {}).items():
            p = r.racine_sources / h.NUIT / piece["chemin"]
            if not p.is_file() or h.sha256_fichier(p) != piece["sha256"]:
                raise h.Refus(f"pièce {nom} de la configuration : empreinte différente ou fichier absent")
        self.j.ecrire(f"pièces gelées : {len(r.empreintes)} empreintes égales ; {len(c.get('pieces', {}))} pièces de la "
                      "configuration égales")

    # -- versements
    def _url(self) -> str:
        return h.git("remote", "get-url", "origin", cwd=self.r.clone_prive, delai=DELAI_GIT_S).strip()

    def _pousser(self, v: Path, branche: str, url: str) -> str | None:
        """Poussée bornée (m1) : `essais_poussee` essais, attente constante, délais de `DELAI_GIT_S` ; vérifiée par ls-remote."""
        gh = self.secrets["GH_TOKEN"]
        local = h.git("rev-parse", "HEAD", cwd=v, delai=DELAI_GIT_S).strip()
        for essai in range(1, self.r.essais_poussee + 1):
            try:
                h.git("push", "-q", url, f"HEAD:refs/heads/{branche}", cwd=v, gh_token=gh, delai=DELAI_GIT_S)
                vu = h.git("ls-remote", url, f"refs/heads/{branche}", gh_token=gh, delai=DELAI_GIT_S).split()
                if vu and vu[0] == local:
                    return local
            except (h.Refus, subprocess.TimeoutExpired) as x:
                self.j.ecrire(f"poussée {essai}/{self.r.essais_poussee} de {branche} : {type(x).__name__}")
            if essai < self.r.essais_poussee:
                time.sleep(self.r.attente_poussee_s)
        return None

    def signe_de_vie(self) -> bool:
        """m2 : branche orpheline poussée tôt (aucune donnée de la course) ; le pilote ne détruit pas à T0 + 30 min une machine
        qui l'a poussée. C2 : rend vrai seulement si la poussée est vérifiée par `ls-remote` ; sinon la course ne part pas."""
        f = self.t / "signe-de-vie.json"
        f.write_text(json.dumps({"utc": h.maintenant(), "machine": self.env.get("CONTAINER_ID"),
                                 "depart_conteneur": self.depart_conteneur, "version": VERSION}) + "\n")
        try:
            gh, url = self.secrets["GH_TOKEN"], self._url()
            if h.git("ls-remote", url, f"refs/heads/{BRANCHE_VIE}", gh_token=gh, delai=DELAI_GIT_S).strip():
                raise h.Refus(f"branche {BRANCHE_VIE} déjà présente (R12)")
            v = self.racine / "versement-signe-de-vie-a1v3"
            if v.exists():
                raise h.Refus(f"copie {v} déjà présente (R12)")
            h.git("init", "-q", "-b", "signe-de-vie", str(v), delai=DELAI_GIT_S)
            (v / BRANCHE_VIE).mkdir(parents=True)
            shutil.copy2(f, v / BRANCHE_VIE / f.name)
            h.git("add", "-f", "-A", cwd=v, delai=DELAI_GIT_S)
            h.git("-c", "user.name=hote-durable-a1-v3", "-c", "user.email=hote@invalid", "commit", "-q", "-m",
                  "A1-v3, troisième course : signe de vie de l'hôte durable v3 (aucune donnée de la course)", cwd=v,
                  delai=DELAI_GIT_S)
            c = self._pousser(v, BRANCHE_VIE, url)
            self.j.ecrire(f"signe de vie poussé : {BRANCHE_VIE} = {c}" if c else "signe de vie non vérifié par ls-remote")
            return bool(c)
        except Exception as x:
            self.j.ecrire(f"signe de vie non poussé : {type(x).__name__} : {self.j.masquer(str(x))[:200]}")
            return False

    def copier_journaux_du_demarrage(self) -> None:
        d = self.t / "demarrage"
        for nom in FICHIERS_DEMARRAGE:
            p = self.racine / nom
            if p.is_file():
                d.mkdir(exist_ok=True)
                shutil.copy2(p, d / nom)

    def sceller(self) -> Path:
        self.copier_journaux_du_demarrage()  # f5 : départ, échéance, minuterie, amorce, mémoire, versés avec la sortie
        return super().sceller()

    def verser(self, branche: str, liste: Path) -> bool:
        """Branche neuve **partie de `main`** (texte v3, section 8), sans clone entier de `main` (m5 : l'arbre de `main` pèse
        2,4 Go) : clone superficiel, partiel (`--filter=blob:none`) et clairsemé (`--sparse`, puis le seul dossier versé) ;
        refus si la branche existe (R12) ; poussée bornée, vérifiée par ls-remote."""
        r, gh = self.r, self.secrets["GH_TOKEN"]
        url = self._url()
        if h.git("ls-remote", url, f"refs/heads/{branche}", gh_token=gh, delai=DELAI_GIT_S).strip():
            raise h.Refus(f"branche {branche} déjà présente (R12) : rien n'est écrasé")
        suffixe = "-versement-interrompue-v1" if branche == h.BRANCHE_INTERROMPUE else "-versement"  # C3
        v = r.travail.parent / (r.travail.name + suffixe)
        if v.exists():
            raise h.Refus(f"copie de versement {v} déjà présente (R12)")
        h.git("clone", "-q", "--depth", "1", "--filter=blob:none", "--sparse", "--single-branch", "--branch", "main", url,
              str(v), gh_token=gh, delai=DELAI_GIT_S)
        h.git("sparse-checkout", "set", branche, cwd=v, gh_token=gh, delai=DELAI_GIT_S)
        h.git("checkout", "-q", "-b", branche, cwd=v, delai=DELAI_GIT_S)
        dest = v / branche
        dest.mkdir(parents=True, exist_ok=False)
        for p in self.fichiers_a_verser():
            cible = dest / p.relative_to(self.t)
            cible.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, cible)
        h.git("add", "-f", str(dest), cwd=v, delai=DELAI_GIT_S)
        h.git("-c", "user.name=hote-durable-a1-v3", "-c", "user.email=hote@invalid", "commit", "-q", "-m",
              f"A1-v3, troisième course : état scellé de l'hôte durable v3 ({self.nature_fin}), liste "
              f"{h.sha256_fichier(liste)[:16]}…, versé avant toute lecture", cwd=v, delai=DELAI_GIT_S)
        c = self._pousser(v, branche, url)
        if not c:
            return False
        self.j.ecrire(f"versé : {branche} = {c} (vérifié par ls-remote) ; liste {h.sha256_fichier(liste)}")
        self.etat("verse")
        return True

    def fin(self, branche: str) -> int:
        """M1 b : toute exception du scellement ou du versement est écrite, puis le geste sur la machine a lieu."""
        pousse = False
        try:
            self.etat("scellement")
            if self.course is not None and self.course.poll() is None:
                self.code_course = h.arreter_par_pid(self.course, self.j, "course")
            if self.relais is not None:
                dernier = h.etat_relais(self.r.port)
                if dernier:
                    self.j.ecrire(f"relais, relevé final : {dernier.get('appels')} appels, {dernier.get('depense_usd')} USD")
                h.arreter_par_pid(self.relais, self.j, "relais")
            if hasattr(self, "sha_registre"):
                apres = h.sha256_fichier(self.t / "registre-go.md")
                self.j.ecrire(f"registre-go.md après la course : {apres} "
                              f"({'inchangé' if apres == self.sha_registre else 'CHANGÉ'})")
            self.j.ecrire(f"nature de la fin : {self.nature_fin} ; coût de la machine estimé {self.cout_machine():.4f} USD depuis "
                          "le départ du conteneur ; scellement (liste d'empreintes, puis copie versée, sans autre écriture)")
            liste = self.sceller()
            fuite = self.fuites()
            if fuite:
                raise h.Refus(f"valeur de secret trouvée dans {fuite} : rien n'est versé")
            pousse = self.verser(branche, liste)
        except Exception as x:
            try:
                self.j.ecrire(f"VERSEMENT IMPOSSIBLE : {type(x).__name__} : {self.j.masquer(str(x))[:300]}")
            except Exception:
                pass
        return self.se_detruire(pousse)

    def client_vast(self):
        return h.ClientVastJouet(self.r.vast_jouet) if self.r.jouet else h.ClientVast(self.secrets["CONTAINER_API_KEY"])

    def _ecrire_sans_echec(self, m: str) -> None:
        try:
            self.j.ecrire(m)
        except Exception:
            print(m, flush=True)

    def se_detruire(self, pousse: bool) -> int:
        """Texte v3, section 8 : poussée vérifiée → destruction par l'identifiant ; destruction refusée, poussée non vérifiée
        ou secret trouvé → **arrêt** (données gardées ; l'arrêt arrête aussi la minuterie : la session qui reprend décide).
        Étiquette et instances protégées contrôlées (f8) ; toute exception attrapée (M1 b). Codes : 0 détruite, 3 arrêtée,
        4 aucun geste (identifiant, étiquette, client, arrêt refusé : la minuterie détruit à l'échéance)."""
        ident = self.env.get("CONTAINER_ID", "")
        ecrire = self._ecrire_sans_echec
        if not re.fullmatch(r"[0-9]{1,12}", ident or "") or int(ident) in PROTEGEES:
            ecrire(f"identifiant de la machine illisible ou protégé ({ident!r}) : aucun geste ; la minuterie et la session qui "
                   "reprend s'en chargent (R14)")
            return 4
        n = int(ident)
        try:
            client = self.client_vast()
        except Exception as x:
            ecrire(f"client de Vast impossible ({type(x).__name__}) : aucun geste ; la minuterie détruit à l'échéance")
            return 4
        try:
            vues = [i for i in client.instances() if i.get("id") == n]
            lab = vues[0].get("label") if vues else None
            if lab is not None and lab != ETIQUETTE:
                ecrire(f"étiquette lue {lab!r}, pas {ETIQUETTE} : aucun geste")
                return 4
        except Exception as x:
            ecrire(f"étiquette non lue ({type(x).__name__}) : geste par l'identifiant posé par Vast")
        if pousse:
            try:
                ecrire(f"destruction de la machine par son identifiant {n}")
                client.detruire(n)
                return 0
            except Exception as x:
                ecrire(f"destruction refusée ({type(x).__name__}) : arrêt de la machine {n} par son identifiant")
        else:
            ecrire(f"versement non vérifié : la machine {n} est ARRÊTÉE, non détruite (données gardées ; l'arrêt arrête aussi "
                   "la minuterie) ; la session qui reprend décide (R14)")
        try:
            client.arreter(n)
            return 3
        except Exception as x:
            ecrire(f"arrêt de la machine {n} refusé ({type(x).__name__}) : la minuterie détruit à l'échéance ; la session qui "
                   "reprend s'en charge (R14)")
            return 4


def reglages() -> h.Reglages:
    """Défauts de la v1 (chemins écrits par le texte v3, 80 h, 32 USD, relevé chaque minute), versement borné (m1)."""
    return h.Reglages(essais_poussee=ESSAIS_POUSSEE, attente_poussee_s=ATTENTE_POUSSEE_S, python_relais=PYTHON_IMAGE,
                      python_course=PYTHON_IMAGE)  # C1 : chemins absolus de l'interpréteur 3.13


def principal(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    l = sous.add_parser("louer")
    for nom in ("--go", "--go-machine", "--registre-main", "--garde-main", "--offres", "--offre", "--commit-prive",
                "--commit-public", "--sha-texte", "--commit-registre", "--journal-local"):
        l.add_argument(nom, required=True)
    l.add_argument("--verifier-seulement", action="store_true")
    for nom in ("controler", "facturation"):
        c = sous.add_parser(nom)
        c.add_argument("--etat", required=True)
        c.add_argument("--journal-local", required=True)
    o = sous.add_parser("offre")
    o.add_argument("--offres", required=True)
    sous.add_parser("inventaire")
    sous.add_parser("hote")
    args = a.parse_args(argv)
    if args.mode == "louer":
        return louer(args)
    if args.mode == "controler":
        return controler(args)
    if args.mode == "facturation":
        return relever_facturation(args)
    if args.mode == "offre":  # m4 : la moins chère des offres conformes de la réponse brute
        offres = json.loads(Path(args.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        conformes = []
        for x in offres:
            try:
                conformes.append(s10.verifier_offre_sonde([x], x.get("id")))
            except h.Refus:
                continue
        if not conformes:
            print("aucune offre conforme", file=sys.stderr)
            return 2
        print(min(conformes, key=lambda x: (x["dph_total"], x["id"]))["id"])
        return 0
    if args.mode == "inventaire":  # champs filtrés : jamais l'environnement des machines
        try:
            print(json.dumps([h.champs_filtres(i) for i in ClientPiloteV3(dict(os.environ)).instances()],
                             ensure_ascii=False, indent=1))
            return 0
        except h.Refus as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 2
    return MachineV3(reglages(), dict(os.environ)).principal()


if __name__ == "__main__":
    sys.exit(principal())
