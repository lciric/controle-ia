#!/usr/bin/env python3
"""Sonde de l'hôte durable d'A1-v3, **version 2** (GO-2026-11-04-09, GO de la machine, 35 USD).

Version 2 de `sonde_hote_durable_a1_v3.py` (la v1 reste telle quelle, R12), qui porte la contre-lecture
`contre-lecture-sonde-v1.md` (`07ba1356…`, « lançable après corrections ») :

- **M1** — une **minuterie de destruction**, détachée (`setsid`), sans Python, est lancée **en tout premier** par le script de
  démarrage du conteneur, avant le clonage : à l'échéance (départ du conteneur + `DUREE_MAX_S` + 25 min), elle détruit la
  machine par son identifiant (`DELETE /instances/<CONTAINER_ID>/`, clé d'instance), et l'arrête en repli ; le conteneur reste
  en vie jusqu'à l'échéance, quel que soit le code de l'amorce ; dans `fin` et `se_detruire`, toute exception est attrapée et
  mène au geste de repli.
- **M2** — `vastai destroy instance <ID> -y` partout où le pilote détruit.
- **M3** — `VAST_API_KEY` passée par `env -i` par son nom, exigée, masquée ; aucune sortie brute de `vastai` n'est affichée ni
  écrite (elle contient les variables d'environnement de la machine, R-1480) : seulement le code et une ligne masquée.
- **m1** — dépense comptée depuis le départ du conteneur (heure écrite par le script de démarrage) et bornée mécaniquement par la
  minuterie ; versement borné (deux poussées, 30 s, délais `git` de 120 s).
- **m2** — borne « jamais démarrée » : `controler` (session pilote) détruit par l'identifiant, avec `-y`, à T0 + 30 min si la
  machine n'a poussé aucun signe de vie, et après l'échéance finale si elle est encore listée ; état écrit à la création.
- **m3** — réponse de création lue en entier, puis ligne par ligne ; illisible : marqueur « création incertaine », aucune
  nouvelle location avant l'inventaire.
- **m5** — dépôt privé cloné au plus juste (`--filter=blob:none --depth 1`, au commit) ; versements sur des branches orphelines
  (aucun clone de `main`) ; durées chronométrées et versées.
- **f1 à f8** — masquage de toutes les clés ; liste des clés interdites commune à l'amorce et à Python ; message de commit propre
  à la sonde ; branche de refus à part ; journaux de l'amorce, de la minuterie et du démarrage versés ; `--storage 30` à la
  recherche ; `GO_ID=GO-2026-11-04-09` en tête de la ligne de location ; étiquette `sonde-a1-v3-v2` contrôlée avant tout geste,
  et jamais les instances 58936096, 58936099, 58936100.

Aucune clé d'Argon, aucun relais, aucun appel de modèle ; seul secret envoyé : le jeton GitHub (portée : nœud de Lazar, additif 2).
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

try:  # paquet (essais) ou fichier seul (machine : `python3 -I -B …/sonde_hote_durable_a1_v3_v2.py`)
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

VERSION = "sonde-hote-durable-a1-v3-v2"
GO_SONDE, MONTANT_GO_SONDE_USD = s1.GO_SONDE, s1.MONTANT_GO_SONDE_USD
ETIQUETTE = "sonde-a1-v3-v2"
BRANCHE = "donnees/sonde-hote-durable-a1-v3-v2"
BRANCHE_REFUS = "donnees/sonde-hote-durable-a1-v3-v2-refus"
BRANCHE_INTERROMPUE = "donnees/sonde-hote-durable-a1-v3-v2-interrompue"
BRANCHE_VIE = "donnees/sonde-hote-durable-a1-v3-v2-signe-de-vie"
AMORCE = "scripts/amorce_sonde_hote_durable_a1_v3_v2.sh"
MODULE = "src/controle_ia/sonde_hote_durable_a1_v3_v2.py"
PROTEGEES = (58936096, 58936099, 58936100)  # instances « R8 » de Lazar : jamais touchées
DUREE_DEFAUT_S, DUREE_MAX_S = 1200, 1800
MARGE_MINUTERIE_S = 1500          # 25 min après la durée de la sonde : installations, versement, destruction
VIE_APRES_ECHEANCE_S = 600        # le conteneur reste en vie 10 min après l'échéance, puis sort (repli : « exited »)
DEMARRAGE_MAX_S = 600             # borne écrite du temps entre la création et le départ du conteneur (pilote : m2)
BORNE_SIGNE_DE_VIE_S = 1800       # T0 + 30 min : sans signe de vie, le pilote détruit (m2)
PLAFOND_SONDE_USD = 0.50
DELAI_GIT_S = 120
# Liste commune à l'amorce v2 (f2) : même motif, même ordre.
CLES_INTERDITES = re.compile(r"^(CLE_ARGON|GEMINI.*|ANTHROPIC.*|OPENAI.*|MOONSHOT.*|KIMI.*|RR_.*API_KEY.*)$")
MOTIF_AMORCE = "CLE_ARGON|GEMINI*|ANTHROPIC*|OPENAI*|MOONSHOT*|KIMI*|RR_*API_KEY*"
SECRETS_PILOTE = ("GH_TOKEN", "VAST_API_KEY")
SECRETS_MACHINE = ("GH_TOKEN", "CONTAINER_API_KEY", "VAST_API_KEY")
FICHIERS_DEMARRAGE = ("sonde-v2-minuterie.txt", "sonde-v2-minuterie.log", "sonde-v2-temps.txt", "amorce-sonde-a1v3-v2.log")


def cles_de_modele(environ: dict) -> list[str]:
    return sorted(k for k, v in environ.items() if v and CLES_INTERDITES.match(k))


def cout_maximal_usd(dph: float, duree_s: int) -> float:
    """Borne mécanique (m1) : démarrage ≤ 10 min (écrit), puis la minuterie détruit à durée + 25 min ; en repli, le conteneur
    sort 10 min plus tard (« exited », plus de calcul facturé)."""
    return dph * (DEMARRAGE_MAX_S + duree_s + MARGE_MINUTERIE_S + VIE_APRES_ECHEANCE_S) / 3600


def verifier_duree(brut) -> int:
    if not isinstance(brut, str) or not re.fullmatch(r"[0-9]{1,5}", brut or ""):
        raise h.Refus(f"DUREE_MAX_S {brut!r} : entier de secondes exigé")
    d = int(brut)
    if not (60 <= d <= DUREE_MAX_S):
        raise h.Refus(f"DUREE_MAX_S {d} hors de [60 ; {DUREE_MAX_S}]")
    return d


def verifier_plafond(dph: float, duree_s: int, plafond_usd: float = PLAFOND_SONDE_USD) -> float:
    c = cout_maximal_usd(dph, duree_s)
    if c > plafond_usd:
        raise h.Refus(f"dépense de la sonde au plus {c:.4f} USD > plafond {plafond_usd} USD")
    return c


# --- script de démarrage du conteneur : la minuterie d'abord (M1), sans Python -------------------------------------------

MINUTERIE = r'''
ECH="$1"; R="$2"; API="$3"; J="$R/sonde-v2-minuterie.log"
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $(date -u -d @"$ECH" +%FT%TZ 2>/dev/null || echo "$ECH")" >> "$J"
echo "$$" > "$R/sonde-v2-minuterie.pid"
while [ "$(date +%s)" -lt "$ECH" ]; do sleep 5; done
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) identifiant illisible : aucun geste" >> "$J"; exit 3;; esac
case " 58936096 58936099 58936100 " in *" $CONTAINER_ID "*) echo "$(date -u +%FT%TZ) instance protégée : aucun geste" >> "$J"; exit 3;; esac
A="Authorization: Bearer ${CONTAINER_API_KEY:-}"
LAB=$(curl -sS -m 60 -H "$A" "$API/instances/$CONTAINER_ID/" 2>/dev/null | grep -o '"label": *"[^"]*"' | head -1)
if [ -n "$LAB" ] && ! printf '%s' "$LAB" | grep -q '"sonde-a1-v3-v2"'; then
    echo "$(date -u +%FT%TZ) étiquette lue $LAB, pas sonde-a1-v3-v2 : aucun geste" >> "$J"; exit 3
fi
[ -n "$LAB" ] || echo "$(date -u +%FT%TZ) étiquette non lue : destruction par l'identifiant posé par Vast" >> "$J"
c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "$A" "$API/instances/$CONTAINER_ID/" 2>/dev/null)
echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID : HTTP $c" >> "$J"
case "$c" in 2??) exit 0;; esac
c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "$A" -H "Content-Type: application/json" \
    -d '{"state": "stopped"}' "$API/instances/$CONTAINER_ID/" 2>/dev/null)
echo "$(date -u +%FT%TZ) repli : arrêt de l'instance $CONTAINER_ID : HTTP $c" >> "$J"
'''


def script_de_demarrage(commit_prive: str) -> str:
    """Processus principal du conteneur. Ordre : (1) minuterie détachée (échéance gardée sur disque : une reprise du conteneur
    garde l'échéance d'origine) ; (2) clone partiel au commit, chronométré ; (3) amorce ; (4) vie jusqu'à l'échéance + 10 min."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit_prive):
        raise h.Refus("commit du dépôt privé : hash complet de 40 caractères exigé")
    m64 = base64.b64encode(MINUTERIE.encode()).decode("ascii")
    return f'''set -u
R="${{RACINE_SONDE:-/root}}"; API="${{API_VAST:-{h.API_VAST}}}"
D="${{DUREE_MAX_S:-{DUREE_DEFAUT_S}}}"; case "$D" in ''|*[!0-9]*) D={DUREE_DEFAUT_S};; esac; [ "$D" -le {DUREE_MAX_S} ] || D={DUREE_MAX_S}
MARGE="${{SONDE_MARGE_S:-{MARGE_MINUTERIE_S}}}"; APRES="${{SONDE_VIE_APRES_S:-{VIE_APRES_ECHEANCE_S}}}"
if [ -s "$R/sonde-v2-minuterie.txt" ]; then read T0 ECH < "$R/sonde-v2-minuterie.txt"; else T0=$(date +%s); ECH=$((T0 + D + MARGE)); echo "$T0 $ECH" > "$R/sonde-v2-minuterie.txt"; fi
echo {m64} | base64 -d > "$R/sonde-v2-minuterie.sh"
setsid bash "$R/sonde-v2-minuterie.sh" "$ECH" "$R" "$API" < /dev/null >> "$R/sonde-v2-minuterie.log" 2>&1 &
echo "demarrage $(date -u +%FT%TZ) depart $T0 echeance $ECH" >> "$R/sonde-v2-temps.txt"
if [ ! -d "$R/amorce-depot/.git" ]; then
  t=$(date +%s)
  (command -v git >/dev/null || (apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null))
  A='!f() {{ echo username=x-access-token; echo "password=${{GH_TOKEN}}"; }}; f'
  git init -q "$R/amorce-depot" && git -C "$R/amorce-depot" remote add origin "$DEPOT_URL" &&
  timeout 600 git -C "$R/amorce-depot" -c credential.helper="$A" fetch -q --filter=blob:none --depth 1 origin {commit_prive} &&
  git -C "$R/amorce-depot" checkout -q --detach FETCH_HEAD
  echo "clone $? en $(( $(date +%s) - t )) s" >> "$R/sonde-v2-temps.txt"
fi
[ -f "$R/amorce-depot/{AMORCE}" ] && bash "$R/amorce-depot/{AMORCE}" 2>&1 | tee -a "$R/amorce-sonde-a1v3-v2.log"
echo "amorce finie $(date -u +%FT%TZ)" >> "$R/sonde-v2-temps.txt"
while [ "$(date +%s)" -lt $((ECH + APRES)) ]; do sleep 5; done
'''


def corps(commit_prive: str, offre: dict, duree_s: int, gh_token: str) -> dict:
    if not gh_token:
        raise h.Refus("GH_TOKEN absent : la sonde ne pourrait pas verser")
    env = {"COMMIT_PRIVE": commit_prive, "GO_ID": GO_SONDE, "PRIX_H_USD": f"{offre['dph_total']:.6f}",
           "DUREE_MAX_S": str(duree_s), "DEPOT_URL": h.DEPOT_PRIVE, "GH_TOKEN": gh_token}
    if cles_de_modele(env):
        raise h.Refus("clé de modèle dans le corps de la sonde")
    b64 = base64.b64encode(script_de_demarrage(commit_prive).encode()).decode("ascii")
    return {"image": h.IMAGE, "disk": 30, "label": ETIQUETTE, "env": env,
            "script": f"echo {b64} | base64 -d > /root/demarrage-sonde-v2.sh && bash /root/demarrage-sonde-v2.sh"}


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
        env = {k: self.environ[k] for k in ("PATH", "HOME", "LANG", "VAST_API_KEY") if self.environ.get(k)}
        r = subprocess.run([self.outil, *args], env=env, capture_output=True, timeout=300)

        def masque(octets: bytes) -> str:
            texte = octets.decode("utf-8", "replace")
            for nom, v in (secrets_en_plus or {}).items():
                if v:
                    texte = texte.replace(v, f"[{nom} masquée]")
            return self.masquer(texte)
        if r.returncode != 0:
            premiere = (masque(r.stdout + r.stderr).strip().splitlines() or [""])[0][:160]
            raise h.Refus(f"vastai {' '.join(args[:2])} : code {r.returncode} ; {premiere}")
        return masque(r.stdout)  # la sortie standard seule est lue ; la sortie d'erreur n'est jamais ni lue ni écrite

    def creer(self, offre_id: int, c: dict) -> int:
        if cles_de_modele(c["env"]):
            raise h.Refus("clé de modèle dans le corps : rien créé")
        if any(ch.isspace() or ch in "\"'" for v in c["env"].values() for ch in v):
            raise h.Refus("valeur d'environnement avec espace ou guillemet : refus (forme -e K=V)")
        env = " ".join(f"-e {k}={v}" for k, v in c["env"].items())
        texte = self._lancer(["create", "instance", str(offre_id), "--raw", "--image", c["image"], "--disk", str(c["disk"]),
                              "--cancel-unavail", "--label", c["label"], "--env", env, "--entrypoint", "bash", "--args",
                              "-c", c["script"]], {"GH_TOKEN": c["env"]["GH_TOKEN"]})
        return lire_reponse_de_creation(texte)

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


def lire_reponse_de_creation(texte: str) -> int:
    """m3 : le texte entier d'abord (JSON indenté), puis ligne par ligne ; illisible ou refusé : `Refus`."""
    rep = None
    try:
        rep = json.loads(texte)
    except ValueError:
        for ligne in reversed(texte.strip().splitlines()):
            try:
                rep = json.loads(ligne)
                break
            except ValueError:
                continue
    if not isinstance(rep, dict):
        raise h.Refus("CREATION_INCERTAINE : réponse illisible : ne rien relancer avant l'inventaire")
    ident = rep.get("new_contract")
    if not rep.get("success") or not isinstance(ident, int) or isinstance(ident, bool):
        raise h.Refus(f"création refusée par Vast (succès {rep.get('success')!r})")
    return ident


def louer(a, client=None, aujourd_hui=None, environ=None, maintenant=None) -> int:
    environ = dict(os.environ) if environ is None else environ
    jl = Path(a.journal_local)
    j = h.Journal(jl, {k: environ.get(k, "") for k in SECRETS_PILOTE})
    ident_f, incertain_f, etat_f = (Path(str(jl) + x) for x in (".identifiant", ".creation-incertaine", ".etat.json"))
    try:
        if ident_f.exists() or incertain_f.exists():
            raise h.Refus("une location de la sonde v2 a déjà eu lieu ou est incertaine (R12) : inventaire d'abord")
        if environ.get("GO_ID") != GO_SONDE:
            raise h.Refus(f"GO_ID={GO_SONDE} exigé en tête de la ligne de location (f7)")
        if cles_de_modele(environ):
            raise h.Refus(f"clé de modèle dans l'environnement du pilote : {cles_de_modele(environ)}")
        aujourd_hui = aujourd_hui or dt.datetime.now(dt.timezone.utc).date()
        g = s1.verifier_go_sonde(Path(a.registre_main), Path(a.garde_main), a.go, aujourd_hui)
        j.ecrire(f"sonde v2 : GO {g['go']} accepté par la garde de main, {g['plafond_usd']:g} USD")
        offres = json.loads(Path(a.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        o = s1.offre_la_moins_chere(offres, int(a.offre))
        duree = verifier_duree(a.duree_s)
        cout = verifier_plafond(o["dph_total"], duree)
        j.ecrire(f"sonde v2 : offre {o['id']} à {o['dph_total']} USD/h, la moins chère des conformes ; durée {duree} s ; "
                 f"dépense au plus {cout:.4f} USD (borne de la minuterie) ≤ {PLAFOND_SONDE_USD} USD")
        c = corps(a.commit_prive, o, duree, environ.get("GH_TOKEN", ""))
        if a.verifier_seulement:
            j.ecrire("sonde v2, vérification seulement : rien créé (variables : " + ", ".join(sorted(c["env"])) + ")")
            return 0
        client = client or ClientPilote(environ)
        try:
            ident = client.creer(o["id"], c)
        except h.Refus as e:
            if "CREATION_INCERTAINE" in str(e):
                incertain_f.write_text(f"{h.maintenant()}\n")
            raise
        t0 = maintenant or dt.datetime.now(dt.timezone.utc)
        etat = {"identifiant": ident, "etiquette": ETIQUETTE, "t0_utc": t0.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "borne_signe_de_vie_utc": (t0 + dt.timedelta(seconds=BORNE_SIGNE_DE_VIE_S)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "echeance_finale_utc": (t0 + dt.timedelta(seconds=DEMARRAGE_MAX_S + duree + MARGE_MINUTERIE_S))
                .strftime("%Y-%m-%dT%H:%M:%SZ"), "prix_h_usd": o["dph_total"], "cout_maximal_usd": round(cout, 4),
                "go": GO_SONDE}
        ident_f.write_text(f"{ident}\n")
        etat_f.write_text(json.dumps(etat, ensure_ascii=False, indent=1) + "\n")
        j.ecrire(f"sonde v2 créée : identifiant {ident}, étiquette {ETIQUETTE} ; T0 {etat['t0_utc']} ; signe de vie attendu "
                 f"avant {etat['borne_signe_de_vie_utc']} ; échéance finale {etat['echeance_finale_utc']}")
        j.ecrire("LIGNE POUR registres/etat.md : " + ligne_etat(etat))
        return 0
    except (h.Refus, OSError, ValueError, KeyError) as e:
        j.ecrire(f"REFUS : {e}")
        return 2


def ligne_etat(e: dict) -> str:
    return (f"- Sonde v2 de l'hôte durable d'A1-v3 (GO-2026-11-04-09) : instance **{e['identifiant']}**, étiquette "
            f"`{e['etiquette']}`, créée {e['t0_utc']} ; sans signe de vie à {e['borne_signe_de_vie_utc']}, ou encore listée "
            f"après {e['echeance_finale_utc']} : `vastai destroy instance {e['identifiant']} -y` (toute session qui reprend).")


def controler(a, client=None, signe_de_vie=None, maintenant=None, environ=None) -> int:
    """m2 : borne « jamais démarrée » et repli du pilote ; codes : 0 rien à faire ou attendre, 1 détruite par le pilote,
    2 refus (étiquette, protégée, état illisible), 3 détruite demandée mais encore listée."""
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
                     " attendre")
            return 0
        j.ecrire(f"contrôle : {motif} : destruction de {ident} par son identifiant (-y)")
        client.detruire(ident)
        if [i for i in client.instances() if i.get("id") == ident]:
            j.ecrire(f"instance {ident} encore listée après la destruction : recommencer, puis consigner")
            return 3
        j.ecrire(f"instance {ident} détruite par le pilote, vérifiée par l'inventaire : consigner dans registres/arrets.md")
        return 1
    except (h.Refus, OSError, ValueError, KeyError) as x:
        j.ecrire(f"REFUS : {x}")
        return 2


def branche_existe(branche: str, environ: dict) -> bool:
    aide = ['-c', 'credential.helper=!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f']
    r = subprocess.run(["git", *aide, "ls-remote", h.DEPOT_PRIVE, f"refs/heads/{branche}"], capture_output=True, timeout=120,
                       env={"PATH": environ.get("PATH", "/usr/bin:/bin"), "HOME": environ.get("HOME", "/root"),
                            "GH_TOKEN": environ.get("GH_TOKEN", ""), "GIT_TERMINAL_PROMPT": "0"})
    return r.returncode == 0 and bool(r.stdout.strip())


# --- côté machine -----------------------------------------------------------------------------------------------------------


class MachineSondeV2(s1.MachineSonde):
    """La séquence de la sonde v1, avec les corrections de la contre-lecture (versements orphelins, exceptions attrapées,
    étiquette contrôlée, dépense comptée depuis le départ du conteneur, journaux du démarrage versés)."""

    def __init__(self, r: h.Reglages, environ: dict[str, str], course_factice_s: float = s1.COURSE_FACTICE_S):
        super().__init__(r, environ, course_factice_s)
        self.secrets = {k: environ.get(k, "") for k in SECRETS_MACHINE}
        self.racine = r.travail.parent
        t0 = None
        try:
            t0 = float((self.racine / "sonde-v2-minuterie.txt").read_text().split()[0])
        except (OSError, ValueError, IndexError):
            pass
        # m1 : dépense et durée comptées depuis le départ du conteneur (écrit par le script de démarrage), sinon depuis ici
        self.depart_conteneur = t0
        if t0 is not None:
            self.debut = time.monotonic() - max(0.0, time.time() - t0)

    def principal(self) -> int:
        journal = self.t / "journal-sonde-a1-v3-v2.log"
        if self.etat_fichier.exists():
            self.j = h.Journal(journal, self.secrets)
            avant = self.etat_fichier.read_text().strip()
            self.j.ecrire(f"REPRISE du conteneur de la sonde v2 : état « {avant} » ; rien n'est relancé")
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
        verifier_plafond(self.prix_h, duree)
        h.git("fetch", "-q", "--filter=blob:none", "--depth", "1", "origin", "+refs/heads/main:refs/remotes/origin/main",
              cwd=r.clone_prive, gh_token=self.secrets["GH_TOKEN"], delai=DELAI_GIT_S)
        tete = h.git("rev-parse", "refs/remotes/origin/main", cwd=r.clone_prive, delai=DELAI_GIT_S).strip()
        reg, garde = self.t / "registre-go-main.md", self.t / "garde_calcul_main.py"
        for chemin, dest in (("registres/go.md", reg), (".claude/hooks/garde_calcul.py", garde)):
            sortie = h.lancer(["git", "show", f"{tete}:{chemin}"], cwd=r.clone_prive, delai=DELAI_GIT_S,
                              env=self._env_git())
            if sortie.returncode != 0:
                raise h.Refus(f"{chemin} illisible au commit {tete}")
            dest.write_bytes(sortie.stdout)
        g = s1.verifier_go_sonde(reg, garde, e["GO_ID"], r.aujourd_hui or dt.datetime.now(dt.timezone.utc).date())
        self.j.ecrire(f"GO accepté par la garde de main {tete} : {g['go']}, {g['plafond_usd']:g} USD")
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
            c = self.pousser_orphelin(BRANCHE_VIE, [f], self.t, "Sonde de l'hôte durable d'A1-v3, v2 : signe de vie")
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
        liste = self.t / "EMPREINTES-sonde-hote-durable-a1-v3-v2.txt"
        lignes = [f"{h.sha256_fichier(p)}  {p.relative_to(self.t)}" for p in self.fichiers_a_verser() if p != liste]
        liste.write_text("\n".join(lignes) + "\n")
        return liste

    def verser(self, branche: str, liste: Path) -> bool:
        c = self.pousser_orphelin(branche, self.fichiers_a_verser(), self.t,
                                  f"Sonde de l'hôte durable d'A1-v3, v2 : état scellé ({self.nature_fin}), liste "
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
        """Destruction par l'identifiant, étiquette contrôlée (f8), arrêt en repli ; toute exception attrapée (M1(b)) ; la
        minuterie de la machine reste le dernier recours."""
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
        if pousse:
            try:
                ecrire(f"destruction de la machine par son identifiant {n}")
                client.detruire(n)
                return 0
            except Exception as x:
                ecrire(f"destruction refusée ({type(x).__name__}) : arrêt de la machine {n}")
        else:
            ecrire(f"versement non vérifié : la machine {n} est ARRÊTÉE, non détruite (la minuterie détruira à l'échéance)")
        try:
            client.arreter(n)
            return 3
        except Exception as x:
            ecrire(f"arrêt refusé ({type(x).__name__}) : la minuterie et le pilote s'en chargent")
            return 4

    def _ecrire_sans_echec(self, m: str) -> None:
        try:
            self.j.ecrire(m)
        except Exception:
            print(m, flush=True)


def reglages(environ: dict) -> h.Reglages:
    """m1 : versement borné (deux poussées, 30 s) ; la durée vient de `DUREE_MAX_S`, contrôlée dans `preparer_sonde`."""
    return h.Reglages(travail=Path("/root/sonde-a1-v3-v2"), clone_prive=Path("/root/amorce-depot"), duree_max_s=DUREE_DEFAUT_S,
                      periode_s=30, plafond_machine_usd=PLAFOND_SONDE_USD, essais_poussee=2, attente_poussee_s=30)


def principal(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    l = sous.add_parser("louer")
    for nom in ("--go", "--registre-main", "--garde-main", "--offres", "--offre", "--commit-prive", "--journal-local"):
        l.add_argument(nom, required=True)
    l.add_argument("--duree-s", default=str(DUREE_DEFAUT_S))
    l.add_argument("--verifier-seulement", action="store_true")
    c = sous.add_parser("controler")
    c.add_argument("--etat", required=True)
    c.add_argument("--journal-local", required=True)
    o = sous.add_parser("offre")
    o.add_argument("--offres", required=True)
    sous.add_parser("hote")
    args = a.parse_args(argv)
    if args.mode == "louer":
        return louer(args)
    if args.mode == "controler":
        return controler(args)
    if args.mode == "offre":  # m4 : l'offre la moins chère des conformes, tirée de la réponse brute
        offres = json.loads(Path(args.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        conformes = []
        for x in offres:
            try:
                conformes.append(h.verifier_offre([x], x.get("id")))
            except h.Refus:
                continue
        if not conformes:
            print("aucune offre conforme", file=sys.stderr)
            return 2
        print(min(conformes, key=lambda x: (x["dph_total"], x["id"]))["id"])
        return 0
    env = dict(os.environ)
    return MachineSondeV2(reglages(env), env).principal()


if __name__ == "__main__":
    sys.exit(principal())
