"""Lentille jacobienne contre lentille des logits, appliquées aux directions des sondes de P3 — v2.

Rédigé le 29 octobre 2026, en réponse à la contre-lecture de la v1 (CLJ-01 à CLJ-10). **Exploratoire, processeur seul,
non opposable** : aucun chiffre sorti de ce script ne sert de critère de porte. La v1 reste archivée sans modification
dans `…/comparaison-jlens-logitlens-sondes-p3-v1/`.

Ce qui change par rapport à la v1 (détail dans `note-faisabilite-jlens-sondes-p3-v2.md`, section « différentiel ») :
- CLJ-02 : une **règle primaire unique**, gelée dans ce fichier (`ENONCE_REGLE_PRIMAIRE`), donne quatre verdicts
  « cohérent » / « non cohérent » (2 sondes principales × 2 lentilles). Scores z, p et têtes restent descriptifs ;
- CLJ-03 : jetons de concept = jetons de **début de mot** seulement (un espace initial, puis le mot exact, casse libre) ;
  chaque mot de la liste doit avoir au moins un tel jeton, sinon refus `mot-sans-jeton` ; la liste doit porter son
  sceau compagnon ; la correspondance par préfixe est supprimée ;
- CLJ-04 : option `--empreintes-attendues` (format sha256sum ; la ligne qui nomme ce fichier lui-même est ignorée) ;
- CLJ-05 : une lentille `.pt` illisible donne le refus nommé `lentille-illisible` ;
- CLJ-06 : un index de fragments est reconnu à sa clé `weight_map`, quel que soit son nom ; le refus
  `empreinte-sondes-npz` nomme la vraie source de l'empreinte attendue ;
- CLJ-07 : option `--un-seul-couple SONDE,COUCHE` ;
- CLJ-09 : le manifeste porte le commit, la révision du modèle (`--revision-modele`), l'empreinte de
  `lentille-config.yaml` (`--lentille-config`) et le chemin complet de l'interpréteur ;
- CLJ-10 : la sortie écrit « ajustée sur N textes » d'après la configuration de la lentille, sinon « inconnu » ;
  si la configuration et le fichier de lentille divergent sur ce nombre : refus `lentille-config-discordante` ;
- k (20), le nombre de directions isotropes (200) et la graine sont des constantes gelées (plus d'options).

Convention de couche (CLJ-01, note `note-convention-couche-jlens-p3-v1.md`) : J[ℓ] du dépôt `anthropics/jacobian-lens`
lit la sortie du bloc décodeur ℓ (indice à partir de 0, premier élément du tuple, avant la normalisation finale), comme
la capture de P3 (`src/controle_ia/harnais/activations.py`). Le script suppose cette concordance : couche ℓ de P3 =
clé ℓ de la lentille, sans décalage.

Calcul (sous-commande `comparer`) :
- lentille des logits : logits = W_U · (g ⊙ v / rms(v)), v = w ; lentille jacobienne : même chose avec v = J_ℓ · w ;
  W_U = `lm_head.weight` [vocabulaire, largeur], g = `model.norm.weight`. Pour une direction seule la normalisation RMS
  n'agit que par un facteur positif ; −w donne exactement les logits opposés (pas de biais) ;
- règle primaire (voir `ENONCE_REGLE_PRIMAIRE`) ; puis, en descriptif : têtes brutes et de début de mot des deux sens,
  recouvrements entre lentilles, scores z et p contre isotropes et planchers (diagnostics, jamais critères) ;
- variantes descriptives facultatives : `--covariances` (motif a = Σ·w), `--activations-moyennes` (h̄ ± α‖h̄‖ŵ).

Refus nommés : code de sortie 2, ligne « REFUS <code> : … » sur la sortie d'erreur, aucune sortie écrite.

Sous-commande `verifier-concepts` : relit seulement le vocabulaire et la liste de mots, dit pour chaque mot ses jetons
de début de mot, refuse si un mot n'en a aucun. Elle ne lit ni sonde, ni lentille, ni résultat : elle peut précéder
l'exécution sans rien révéler.

Sous-commande `convertir-lentille` (exige torch) : `.pt` du dépôt → `.npz` (clés `J_<couche>`, `n_prompts`, `d_model`,
`source_layers`).

Usage (depuis la racine du dépôt, sur une machine qui a les entrées) :
  python3 -I -B <ce script> comparer \\
     --sondes-json diag/20261019-230011-p3-reel/sondes-figees.json \\
     --sondes-npz <entrees>/sondes-figees-legeres.npz \\
     --lentille <entrees>/lentille-Llama-3.1-8B-Instruct_jacobian_lens.pt \\
     --lentille-config <entrees>/lentille-config.yaml \\
     --desembedding <entrees>/model-00004-of-00004.safetensors:lm_head.weight \\
     --norme-finale <entrees>/model-00004-of-00004.safetensors:model.norm.weight \\
     --vocabulaire <entrees>/tokenizer.json \\
     --concepts <ce dossier>/concepts-sondes-p3-v2.json \\
     --empreintes-attendues <entrees>/empreintes-entrees-v1.txt \\
     --revision-modele 0e9e39f249a16976918f6564b8830bc894c89659 \\
     --sortie <sortie>/sortie-jlens-sondes-p3-v2.json
Spécification d'un tableau : `chemin.npy`, `chemin.npz:cle`, `chemin.safetensors:nom`, ou `index.json:nom` pour tout
fichier JSON qui porte une clé `weight_map` (par exemple `model.safetensors.index.json`).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import struct
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

VERSION = "v2"
GRAINE = 20261029             # gelée (R9) : directions isotropes par SeedSequence, clé dérivée de l'étiquette
K_TETE = 20                   # gelé : taille de la tête
N_ALEATOIRES = 200            # gelé : directions isotropes par couche
QUANTILE_PRIMAIRE = 0.99      # gelé
METHODE_QUANTILE = "inverted_cdf"
MIN_JETONS_PRIMAIRE = 2       # gelé : au moins deux jetons du concept dans la tête
N_PLANCHERS_MIN = 100         # en dessous, le quantile 0,99 n'a pas de sens : refus
EPS_RMS_LLAMA = 1e-5          # rms_norm_eps de Llama-3.1-8B-Instruct, utilisé seulement en variante « autour »
TAILLE_BLOC = 16384           # lignes de W_U traitées à la fois pour la matrice de Gram

ENONCE_REGLE_PRIMAIRE = (
    "Règle primaire unique, gelée avant toute exécution réelle (v2, 29 octobre 2026). "
    "Pour chaque sonde principale de P3 (une par concept, à sa couche : tromperie-difference_moyennes-c15, "
    "enjeux-lineaire-c15) et pour chacune des deux lentilles (logits, jacobienne), on décode la direction +w "
    "(variante « direction », sens de la classe 1). S = nombre de jetons de la liste du concept propre "
    "(concepts-sondes-p3-v2.json, jetons de début de mot) parmi les 20 jetons de tête, la tête étant restreinte aux "
    "jetons de début de mot (un espace initial, puis une lettre, puis lettres ou chiffres). On calcule la même "
    "statistique, par la même lentille et à la même couche, pour deux distributions nulles : 200 directions isotropes "
    "(graine 20261029, numpy.random.SeedSequence) et les planchers appariés en covariance de P3 pour ce concept "
    "(200 dans le run 20261019-230011-p3-reel ; refus en dessous de 100). Verdict « cohérent » si S >= 2 et si S est "
    "strictement supérieur au quantile 0,99 (méthode inverted_cdf de numpy) de chacune des deux distributions nulles ; "
    "sinon « non cohérent ». Quatre verdicts, lus tels quels, sans correction, sans seuil de rechange, sans autre "
    "liste de mots. Tout le reste de la sortie (scores z, p, têtes brutes, sens moins, autre concept, autres sondes et "
    "couches, variantes) est descriptif et ne sert pas de critère.")


class Refus(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(f"{code} : {message}")
        self.code = code


# --------------------------------------------------------------------------------------------------------------------
# Fichiers, empreintes

def sha256_fichier(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 22), b""):
            h.update(bloc)
    return h.hexdigest()


def sha256_texte(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def exiger(chemin, quoi: str) -> Path:
    p = Path(chemin)
    if not p.is_file():
        raise Refus("entree-absente", f"{quoi} introuvable : {p}")
    return p


def verifier_compagnon(chemin: Path, obligatoire: bool) -> str | None:
    """Empreinte compagnon `<fichier>.sha256` (format sha256sum). Rend l'empreinte vérifiée, ou None si absente."""
    comp = Path(str(chemin) + ".sha256")
    if not comp.is_file():
        if obligatoire:
            raise Refus("sceau-absent", f"{comp} absent")
        return None
    lignes = [l for l in comp.read_text(encoding="utf-8").splitlines() if l.strip()]
    if len(lignes) != 1 or len(lignes[0].split()) != 2:
        raise Refus("sceau-illisible", f"{comp}")
    attendue, nom = lignes[0].split()
    if nom != chemin.name:
        raise Refus("sceau-faux", f"{comp} nomme {nom!r}, pas {chemin.name!r}")
    reelle = sha256_fichier(chemin)
    if reelle != attendue:
        raise Refus("sceau-faux", f"{chemin} : empreinte {reelle[:12]}… ≠ sceau {attendue[:12]}…")
    return reelle


def ecrire_scelle(chemin: Path, texte: str) -> str:
    if chemin.exists() or Path(str(chemin) + ".sha256").exists():
        raise Refus("sortie-existe", f"{chemin} existe déjà (R12)")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(texte, encoding="utf-8")
    sha = sha256_fichier(chemin)
    Path(str(chemin) + ".sha256").write_text(f"{sha}  {chemin.name}\n", encoding="utf-8")
    return sha


def lire_empreintes_attendues(chemin: Path) -> dict[str, str]:
    """Fichier au format sha256sum. La ligne qui nomme ce fichier lui-même est ignorée (fausse par construction)."""
    attendues = {}
    for n, l in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1):
        if not l.strip():
            continue
        m = re.match(r"^([0-9a-f]{64}) [ *](.+)$", l.strip())
        if not m:
            raise Refus("empreintes-attendues-illisibles", f"{chemin}, ligne {n} : {l[:80]!r}")
        nom = Path(m.group(2).strip()).name
        if nom == chemin.name:
            continue
        if nom in attendues and attendues[nom] != m.group(1):
            raise Refus("empreintes-attendues-illisibles", f"{chemin} : deux empreintes pour {nom}")
        attendues[nom] = m.group(1)
    return attendues


# --------------------------------------------------------------------------------------------------------------------
# Sondes (format de figees.py, relu sans torch)

def empreinte_sonde(famille, nom, couche, agregation, tableaux) -> str:
    """Copie de `sondes.familles._empreinte` appliquée à f"{famille}:{nom}"."""
    h = hashlib.sha256(f"{famille}:{nom}/{couche}/{agregation}".encode("utf-8"))
    for t in tableaux:
        h.update(np.ascontiguousarray(t, dtype=np.float64).tobytes())
    return h.hexdigest()


ORDRE_TABLEAUX = {"SondeLineaireJetons": ("w", "b", "q"), "SondeLineaire": ("w", "b", "q"),
                  "SondePerceptron": ("mu", "s", "W", "c", "v", "b", "q"), "SondeMahalanobis": ("mu", "P")}


def lire_sondes_npz(chemin: Path) -> tuple[dict, dict]:
    with np.load(chemin, allow_pickle=False) as z:
        if "index" not in z.files:
            raise Refus("sondes-npz-illisible", f"{chemin} : clé « index » absente (format de figees.py attendu)")
        index = json.loads(bytes(z["index"]).decode("utf-8"))
        sondes = {}
        for k, e in enumerate(index["sondes"]):
            t = {n: np.asarray(z[f"s{k}_{n}"], dtype=np.float64) for n in e["tableaux"]}
            classe = e["classe"]
            if classe not in ORDRE_TABLEAUX:
                raise Refus("sondes-npz-illisible", f"classe {classe!r} inconnue")
            ordre = []
            for n in ORDRE_TABLEAUX[classe]:
                if n == "b":
                    ordre.append(np.array([e["b"]], dtype=np.float64))
                elif n in t:
                    ordre.append(t[n])
            if classe == "SondeLineaire":      # harnais.sondes.SondeLineaire : empreinte non recopiée ici
                emp = None
            else:
                fam = e["famille"] if e.get("famille") is not None else {"SondePerceptron": "perceptron",
                                                                           "SondeMahalanobis": "mahalanobis"}.get(classe)
                emp = empreinte_sonde(fam, e["nom"], e["couche"], e["agregation"], ordre)
            if emp is not None and emp != e["empreinte"]:
                raise Refus("empreinte-sonde", f"{e['nom']} : empreinte recalculée {emp[:12]}… ≠ écrite {e['empreinte'][:12]}…")
            sondes[e["nom"]] = {**{c: e[c] for c in ("classe", "nom", "couche", "agregation", "famille", "b", "empreinte")},
                                "tableaux": t}
    return sondes, index.get("meta", {})


def choisir_sondes(fig: dict, sondes_npz: dict, mode: str, un_seul: str | None) -> list[dict]:
    res = fig["resultat"]
    entrees = {s["nom"]: s for s in res["sondes"]}
    princ = set(res["principales"].values())
    choix = []
    if un_seul is not None:
        nom, sep, couche_txt = un_seul.rpartition(",")
        if not sep or not nom or not re.fullmatch(r"\d+", couche_txt.strip()):
            raise Refus("parametre", f"--un-seul-couple {un_seul!r} : forme SONDE,COUCHE attendue")
        couche = int(couche_txt)
        nom = nom.strip()
        cand = nom if nom in entrees else f"{nom}-c{couche}"
        if cand not in entrees:
            raise Refus("sonde-introuvable", f"--un-seul-couple : ni {nom!r} ni {cand!r} dans sondes-figees.json")
        s = entrees[cand]
        if int(s["couche"]) != couche:
            raise Refus("sonde-introuvable", f"--un-seul-couple : {cand} est à la couche {s['couche']}, pas {couche}")
        if s["classe"] != "SondeLineaireJetons" or s["famille"] == "plancher":
            raise Refus("principale-non-lineaire", f"--un-seul-couple : {cand} ({s['classe']}, {s['famille']}) "
                        "n'est pas une direction de sonde")
        choix.append({"concept": cand.split("-")[0], "principale": cand in princ, **s})
    elif mode == "principales-par-couche":
        for concept, nom_p in sorted(res["principales"].items()):
            if nom_p not in entrees:
                raise Refus("sonde-introuvable", f"principale {nom_p} absente de sondes-figees.json")
            p = entrees[nom_p]
            if p["classe"] != "SondeLineaireJetons":
                raise Refus("principale-non-lineaire", f"{nom_p} est {p['classe']} : pas une direction")
            soeurs = sorted((s for s in res["sondes"] if s["famille"] == p["famille"] and s["nom"].startswith(concept + "-")
                             and s["famille"] != "plancher"), key=lambda s: s["couche"])
            for s in soeurs:
                choix.append({"concept": concept, "principale": s["nom"] == nom_p, **s})
    elif mode == "toutes-lineaires":
        for s in res["sondes"]:
            if s["classe"] == "SondeLineaireJetons" and s["famille"] != "plancher":
                choix.append({"concept": s["nom"].split("-")[0], "principale": s["nom"] in princ, **s})
    else:
        raise Refus("parametre", f"mode de sondes {mode!r} inconnu")
    for c in choix:
        if c["nom"] not in sondes_npz:
            raise Refus("sonde-introuvable", f"{c['nom']} absente du fichier de poids")
        n = sondes_npz[c["nom"]]
        if n["empreinte"] != c["empreinte"] or int(n["couche"]) != int(c["couche"]):
            raise Refus("empreinte-sonde", f"{c['nom']} : le fichier de poids ne porte pas la sonde de sondes-figees.json")
    return choix


# --------------------------------------------------------------------------------------------------------------------
# Lentille et sa configuration

def charger_pt(chemin: Path):
    try:
        import torch
    except ImportError:
        raise Refus("torch-absent-pour-pt", "lentille .pt : convertir d'abord en .npz par `convertir-lentille` "
                    "sur une machine qui a torch") from None
    try:
        ck = torch.load(str(chemin), map_location="cpu", weights_only=True)
    except Exception as e:                                         # CLJ-05 : fichier tronqué, vide, ou pas un .pt
        raise Refus("lentille-illisible", f"{chemin} : torch.load a échoué ({type(e).__name__}: {str(e)[:160]})") from None
    if not isinstance(ck, dict) or "J" not in ck:
        cles = sorted(ck) if isinstance(ck, dict) else type(ck).__name__
        raise Refus("lentille-illisible", f"{chemin} : clé « J » absente ({cles} ; point de reprise de fit() ?)")
    return ck


def lire_lentille(chemin: Path, couches: list[int]) -> tuple[dict, dict]:
    if chemin.suffix == ".npz":
        try:
            z = np.load(chemin, allow_pickle=False)
        except Exception as e:
            raise Refus("lentille-illisible", f"{chemin} : {type(e).__name__}: {str(e)[:160]}") from None
        with z:
            J = {}
            for c in couches:
                cle = f"J_{c}"
                if cle not in z.files:
                    raise Refus("couche-absente-lentille", f"{chemin} : pas de clé {cle} (clés : {sorted(z.files)[:12]}…)")
                J[c] = np.asarray(z[cle], dtype=np.float64)
            meta = {k: (z[k].tolist() if k in z.files else None) for k in ("n_prompts", "d_model", "source_layers")}
    elif chemin.suffix == ".pt":
        ck = charger_pt(chemin)
        J = {}
        for c in couches:
            if c not in ck["J"]:
                raise Refus("couche-absente-lentille", f"{chemin} : couche {c} absente ({sorted(ck['J'])})")
            J[c] = ck["J"][c].float().numpy().astype(np.float64)
        meta = {"n_prompts": ck.get("n_prompts"), "d_model": ck.get("d_model"), "source_layers": ck.get("source_layers")}
    else:
        raise Refus("lentille-illisible", f"{chemin} : .npz ou .pt attendu")
    for c, m in J.items():
        if m.ndim != 2 or m.shape[0] != m.shape[1]:
            raise Refus("dimension", f"J_{c} de forme {m.shape} : carrée attendue")
        if not np.all(np.isfinite(m)):
            raise Refus("lentille-non-finie", f"J_{c} contient des valeurs non finies")
    return J, meta


def _valeur_yaml(v: str):
    v = v.strip()
    if v in ("", "null", "~", "None"):
        return None
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d*(e-?\d+)?", v):
        return float(v)
    return v.strip("'\"")


def lire_config_lentille(chemin: Path) -> dict:
    """Clés de premier niveau d'un YAML simple (« cle: valeur »), sans bibliothèque. Les blocs indentés sont ignorés."""
    cles = {}
    for l in chemin.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([A-Za-z_][\w.-]*)\s*:\s*(.*?)\s*$", l)
        if m:
            v = m.group(2)
            if " #" in v:
                v = v.split(" #", 1)[0]
            cles[m.group(1)] = _valeur_yaml(v)
    return cles


def nombre_de_textes(config: dict | None) -> tuple[int | None, str]:
    """CLJ-10 : « ajustée sur N textes » d'après la configuration, sinon « inconnu »."""
    if config is None:
        return None, "inconnu"
    for cle in ("prompts_fitted", "n_prompts"):
        if isinstance(config.get(cle), int):
            return config[cle], f"ajustée sur {config[cle]} textes (lentille-config.yaml, clé {cle})"
    return None, "inconnu"


# --------------------------------------------------------------------------------------------------------------------
# Poids : npy, npz, safetensors (lu en numpy, sans la bibliothèque safetensors)

_DTYPES_ST = {"F32": np.float32, "F16": np.float16, "F64": np.float64, "BF16": "bf16"}


def _lire_safetensors(chemin: Path, nom: str) -> np.ndarray:
    with open(chemin, "rb") as f:
        n = struct.unpack("<Q", f.read(8))[0]
        if n > 100_000_000:
            raise Refus("poids-illisibles", f"{chemin} : en-tête safetensors démesuré")
        entete = json.loads(f.read(n).decode("utf-8"))
    if nom not in entete:
        raise Refus("poids-introuvables", f"{chemin} : tenseur {nom!r} absent")
    e = entete[nom]
    debut, fin = e["data_offsets"]
    if e["dtype"] not in _DTYPES_ST:
        raise Refus("poids-illisibles", f"{nom} : type {e['dtype']} non pris en charge")
    brut = np.memmap(chemin, dtype=np.uint8, mode="r", offset=8 + n + debut, shape=(fin - debut,))
    if _DTYPES_ST[e["dtype"]] == "bf16":
        u = np.frombuffer(brut, dtype="<u2")
        x = (u.astype(np.uint32) << 16).view(np.float32)
    else:
        x = np.frombuffer(brut, dtype=np.dtype(_DTYPES_ST[e["dtype"]]).newbyteorder("<")).astype(np.float32)
    if x.size != int(np.prod(e["shape"])):
        raise Refus("poids-illisibles", f"{nom} : taille {x.size} ≠ forme {e['shape']}")
    return x.reshape(e["shape"])


FORMATS_TABLEAU = ("chemin.npy, chemin.npz:cle, chemin.safetensors:nom, ou un index JSON qui porte une clé "
                   "« weight_map » (quel que soit son nom, par exemple model.safetensors.index.json:nom)")


def lire_tableau(spec: str, quoi: str) -> tuple[np.ndarray, list[Path]]:
    """Rend le tableau en float32 et la liste des fichiers effectivement lus (pour le manifeste)."""
    chemin, _, cle = spec.partition(":")
    p = exiger(chemin, quoi)
    if p.suffix == ".json":                                         # CLJ-06 : reconnu à sa clé weight_map
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            raise Refus("poids-illisibles", f"{p} : JSON illisible ({e})") from None
        if not isinstance(d, dict) or not isinstance(d.get("weight_map"), dict):
            raise Refus("poids-illisibles", f"{p} : JSON sans clé « weight_map » ; formats acceptés : {FORMATS_TABLEAU}")
        if cle not in d["weight_map"]:
            raise Refus("poids-introuvables", f"{p} : {cle!r} absent de weight_map")
        fragment = exiger(p.parent / d["weight_map"][cle], f"fragment de {quoi}")
        return _lire_safetensors(fragment, cle), [p, fragment]
    if p.suffix == ".safetensors":
        return _lire_safetensors(p, cle), [p]
    if p.suffix == ".npy":
        return np.load(p, allow_pickle=False).astype(np.float32), [p]
    if p.suffix == ".npz":
        with np.load(p, allow_pickle=False) as z:
            if cle not in z.files:
                raise Refus("poids-introuvables", f"{p} : clé {cle!r} absente")
            return np.asarray(z[cle], dtype=np.float32), [p]
    raise Refus("poids-illisibles", f"{p} : format non reconnu ; formats acceptés : {FORMATS_TABLEAU}")


# --------------------------------------------------------------------------------------------------------------------
# Vocabulaire et concepts

def _octets_vers_unicode() -> dict[int, str]:
    """Table de l'encodage par octets de GPT-2, reprise par les tokenizer.json « ByteLevel » (Llama 3 compris)."""
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return dict(zip(bs, (chr(c) for c in cs)))


def lire_vocabulaire(chemin: Path, taille: int | None) -> tuple[list[str], dict]:
    """taille None : tout le vocabulaire du fichier (sous-commande verifier-concepts)."""
    info = {"format": None, "jetons_lus": 0, "manquants": 0}
    if chemin.suffix == ".json":
        d = json.loads(chemin.read_text(encoding="utf-8"))
        if isinstance(d, list):
            info["format"] = "liste"
            paires = list(enumerate(str(t) for t in d))
        else:
            info["format"] = "tokenizer.json"
            inverse = {v: k for k, v in _octets_vers_unicode().items()}
            octets = isinstance(d.get("pre_tokenizer"), dict) or isinstance(d.get("decoder"), dict)
            paires = []
            for s, i in d["model"]["vocab"].items():
                if octets and all(ch in inverse for ch in s):
                    paires.append((i, bytes(inverse[ch] for ch in s).decode("utf-8", errors="replace")))
                else:
                    paires.append((i, s.replace("▁", " ")))
            paires += [(a["id"], a["content"]) for a in d.get("added_tokens", [])]
    else:
        info["format"] = "texte, un jeton par ligne"
        paires = list(enumerate(chemin.read_text(encoding="utf-8").split("\n")))
    if taille is None:
        taille = 1 + max(i for i, _ in paires)
    textes: list[str | None] = [None] * taille
    for i, t in paires:
        if 0 <= i < taille:
            textes[i] = t
    info["jetons_lus"] = sum(t is not None for t in textes)
    info["manquants"] = taille - info["jetons_lus"]
    return [t if t is not None else f"<id {i}>" for i, t in enumerate(textes)], info


def _corps_de_mot(s: str) -> bool:
    return bool(s) and all(ch.isalnum() or (0 < k < len(s) - 1 and ch in "'-’") for k, ch in enumerate(s))


def masque_mots(textes: list[str]) -> np.ndarray:
    """Même règle que jlens/vis.py::_meaningful_token_mask (descriptif)."""
    m = np.zeros(len(textes), dtype=bool)
    for i, t in enumerate(textes):
        s = t.strip()
        if not s or "<|" in s or (s.startswith("<") and s.endswith(">")):
            continue
        m[i] = _corps_de_mot(s)
    return m


def masque_debut_de_mot(textes: list[str]) -> np.ndarray:
    """Jeton de début de mot : un seul espace initial, puis une lettre, puis lettres ou chiffres (apostrophe ou trait
    d'union intérieurs admis). Exclut les morceaux sans espace, les tabulations, les retours, les nombres, le balisage."""
    m = np.zeros(len(textes), dtype=bool)
    for i, t in enumerate(textes):
        if len(t) < 2 or t[0] != " " or t.startswith("<id "):
            continue
        s = t[1:]
        m[i] = s[0].isalpha() and "<|" not in s and _corps_de_mot(s)
    return m


def lire_concepts(chemin: Path) -> dict[str, list[str]]:
    d = json.loads(chemin.read_text(encoding="utf-8"))
    concepts = {}
    for nom, liste in d.items():
        if nom.startswith("_"):
            continue
        if not isinstance(liste, list) or not liste:
            raise Refus("concepts-illisibles", f"{chemin} : {nom!r} n'est pas une liste non vide")
        mauvais = [m for m in liste if not isinstance(m, str) or not re.fullmatch(r"[a-z]+", m)]
        if mauvais:
            raise Refus("concepts-illisibles", f"{chemin} : {nom} : mots hors de [a-z]+ : {mauvais}")
        if len(set(liste)) != len(liste):
            raise Refus("concepts-illisibles", f"{chemin} : {nom} : mots en double")
        concepts[nom] = liste
    noms = sorted(concepts)
    for i, a in enumerate(noms):
        for b in noms[i + 1:]:
            commun = set(concepts[a]) & set(concepts[b])
            if commun:
                raise Refus("concepts-chevauchants", f"{a} et {b} partagent {sorted(commun)}")
    return concepts


def jetons_du_concept(textes: list[str], debut: np.ndarray, mots: list[str]) -> tuple[list[int], dict[str, list[int]]]:
    """Jetons de début de mot dont le mot (sans l'espace, casse libre) est exactement un mot de la liste."""
    cibles = set(mots)
    par_mot: dict[str, list[int]] = {m: [] for m in mots}
    for i in np.flatnonzero(debut):
        s = textes[i][1:].lower()
        if s in cibles:
            par_mot[s].append(int(i))
    ids = sorted(i for l in par_mot.values() for i in l)
    return ids, par_mot


def resoudre_concepts(textes, debut, concepts: dict) -> dict:
    sortie, sans = {}, {}
    for nom, mots in concepts.items():
        ids, par_mot = jetons_du_concept(textes, debut, mots)
        manq = [m for m, l in par_mot.items() if not l]
        if manq:
            sans[nom] = manq
        sortie[nom] = {"mots": mots, "jetons": [{"id": i, "texte": textes[i]} for i in ids],
                       "jetons_par_mot": {m: [textes[i] for i in l] for m, l in par_mot.items()}}
    if sans:
        raise Refus("mot-sans-jeton", f"mots sans jeton de début de mot dans le vocabulaire : {sans} — retirer ces mots "
                    "dans une nouvelle version de la liste, scellée avant l'exécution")
    return sortie


# --------------------------------------------------------------------------------------------------------------------
# Désembedding : statistiques du vocabulaire (moyenne, Gram) pour les scores z sans matrice [V, n]

class Desembedding:
    def __init__(self, WU: np.ndarray):
        self.WU = WU                                   # float32 [V, d]
        V, d = WU.shape
        self.moyenne = np.zeros(d)
        self.gram = np.zeros((d, d))
        for a in range(0, V, TAILLE_BLOC):
            R = WU[a:a + TAILLE_BLOC].astype(np.float64)
            self.moyenne += R.sum(axis=0)
            self.gram += R.T @ R
        self.moyenne /= V
        self.gram /= V

    def logits(self, y: np.ndarray) -> np.ndarray:
        return (self.WU @ y.astype(np.float32)).astype(np.float64)

    def z_lot(self, Y: np.ndarray, moyenne_concept: np.ndarray) -> np.ndarray:
        """Y [d, n] : z_j = ((c̄ − m)·y_j) / sqrt(y_jᵀ G y_j − (m·y_j)²)."""
        num = (moyenne_concept - self.moyenne) @ Y
        var = np.sum(Y * (self.gram @ Y), axis=0) - (self.moyenne @ Y) ** 2
        return num / np.sqrt(np.maximum(var, 1e-300))

    def tete_debut_lot(self, Y: np.ndarray, idx_debut: np.ndarray, k: int) -> np.ndarray:
        """Indices (dans le vocabulaire) des k jetons de tête parmi les jetons de début de mot, pour chaque colonne de
        Y [d, n] ; forme [k, n]. Sert aux distributions nulles de la règle primaire."""
        sortie = np.empty((k, Y.shape[1]), dtype=np.int64)
        for a in range(0, Y.shape[1], 50):
            L = (self.WU @ Y[:, a:a + 50].astype(np.float32))[idx_debut]
            part = np.argpartition(-L, k - 1, axis=0)[:k]
            sortie[:, a:a + 50] = idx_debut[part]
        return sortie


# --------------------------------------------------------------------------------------------------------------------
# Lentilles appliquées à des directions

def rms(x, axis=0, eps=0.0):
    return np.sqrt(np.mean(x * x, axis=axis, keepdims=True) + eps)


def vers_sortie(V: np.ndarray, transport: np.ndarray | None, g: np.ndarray, variante: str, ctx: dict) -> np.ndarray:
    """Directions V [d, n] (espace de la couche) → vecteurs y [d, n] tels que logits = W_U · y.
    transport = J_l (lentille jacobienne) ou None (lentille des logits)."""
    T = (lambda X: X) if transport is None else (lambda X: transport @ X)
    if variante == "direction":
        U = T(V)
        return g[:, None] * U / rms(U)
    if variante == "motif":
        S = ctx["covariance"]
        A = (S[:, None] * V) if S.ndim == 1 else S @ V
        U = T(A)
        return g[:, None] * U / rms(U)
    if variante == "autour":
        h = ctx["activation_moyenne"][:, None]
        Vn = V / np.linalg.norm(V, axis=0, keepdims=True)
        pas = ctx["alpha"] * np.linalg.norm(h)
        Up, Um = T(h + pas * Vn), T(h - pas * Vn)
        return g[:, None] * (Up / rms(Up, eps=EPS_RMS_LLAMA) - Um / rms(Um, eps=EPS_RMS_LLAMA))
    raise Refus("parametre", f"variante {variante!r} inconnue")


def tete(logits: np.ndarray, textes: list[str], k: int, masque: np.ndarray | None = None) -> list[dict]:
    x = logits if masque is None else np.where(masque, logits, -np.inf)
    idx = np.argpartition(-x, k)[:k]
    idx = idx[np.argsort(-x[idx], kind="stable")]
    return [{"id": int(i), "texte": textes[i], "logit": round(float(logits[i]), 6)} for i in idx]


def recouvrement(a: list[dict], b: list[dict]) -> dict:
    A, B = {t["id"] for t in a}, {t["id"] for t in b}
    return {"intersection": len(A & B), "jaccard": round(len(A & B) / max(1, len(A | B)), 6),
            "communs": sorted(t["texte"] for t in a if t["id"] in B)}


def p_haut(z: float, nuls: np.ndarray) -> float:
    return float((1 + np.sum(nuls >= z)) / (len(nuls) + 1))


def graines_aleatoires(etiquette: str) -> np.random.SeedSequence:
    cle = int.from_bytes(hashlib.sha256(etiquette.encode("utf-8")).digest()[:8], "little")
    return np.random.SeedSequence(entropy=GRAINE, spawn_key=(cle,))


def quantile_primaire(nuls: np.ndarray) -> float:
    return float(np.quantile(np.asarray(nuls, dtype=np.float64), QUANTILE_PRIMAIRE, method=METHODE_QUANTILE))


def appliquer_regle(S: int, nul_iso: np.ndarray, nul_pl: np.ndarray | None) -> dict:
    q_iso = quantile_primaire(nul_iso)
    r = {"S": int(S), "isotropes": {"n": int(nul_iso.size), "quantile_0_99": q_iso,
                                    "p_haut_diagnostic": p_haut(S, nul_iso),
                                    "comptes": {str(v): int(c) for v, c in zip(*np.unique(nul_iso, return_counts=True))}}}
    ok = S >= MIN_JETONS_PRIMAIRE and S > q_iso
    if nul_pl is not None:
        q_pl = quantile_primaire(nul_pl)
        r["planchers"] = {"n": int(nul_pl.size), "quantile_0_99": q_pl, "p_haut_diagnostic": p_haut(S, nul_pl),
                          "comptes": {str(v): int(c) for v, c in zip(*np.unique(nul_pl, return_counts=True))}}
        ok = ok and S > q_pl
    else:
        r["planchers"] = {"statut": "absents à cette couche pour ce concept"}
    r["verdict"] = "cohérent" if ok else "non cohérent"
    return r


# --------------------------------------------------------------------------------------------------------------------
# Provenance (CLJ-09)

def commit_git(dossier: Path, fichier: Path) -> dict:
    try:
        r = subprocess.run(["git", "-C", str(dossier), "rev-parse", "HEAD"], capture_output=True, text=True, timeout=20)
        if r.returncode != 0:
            return {"commit": "inconnu", "source": f"git rev-parse a échoué : {r.stderr.strip()[:120]}"}
        s = subprocess.run(["git", "-C", str(dossier), "status", "--porcelain", "--", str(fichier)],
                           capture_output=True, text=True, timeout=20)
        etat = s.stdout.strip() or "propre (suivi et inchangé depuis le commit)"
        return {"commit": r.stdout.strip(), "source": f"git rev-parse HEAD dans {dossier}", "etat_du_script": etat}
    except (OSError, subprocess.SubprocessError) as e:
        return {"commit": "inconnu", "source": f"git indisponible ({type(e).__name__})"}


# --------------------------------------------------------------------------------------------------------------------
# Comparer

def comparer(a) -> int:
    t0 = time.time()
    sortie = Path(a.sortie)
    manifeste_ch = sortie.with_name(sortie.stem + "-manifeste.json")
    for p in (sortie, manifeste_ch):
        if p.exists() or Path(str(p) + ".sha256").exists():
            raise Refus("sortie-existe", f"{p} existe déjà (R12)")
    lus: dict[str, Path] = {}

    # Sondes
    p_json = exiger(a.sondes_json, "sondes-figees.json")
    verifier_compagnon(p_json, obligatoire=True)
    fig = json.loads(p_json.read_text(encoding="utf-8"))
    lus["sondes_json"] = p_json
    p_npz = exiger(a.sondes_npz, "fichier de poids des sondes (sondes-figees-legeres.npz)")
    sha_npz = sha256_fichier(p_npz)
    if a.sha256_sondes_npz is not None:
        attendue, source = a.sha256_sondes_npz, "option --sha256-sondes-npz"
    elif p_npz.name == "sondes-figees.npz":
        attendue, source = fig["resultat"].get("sondes_figees_sha256"), "sondes_figees_sha256 de sondes-figees.json"
    else:
        attendue, source = fig["resultat"].get("sondes_legeres_sha256"), "sondes_legeres_sha256 de sondes-figees.json"
    if sha_npz != attendue:
        raise Refus("empreinte-sondes-npz", f"{p_npz} : {sha_npz[:12]}… ≠ attendue {str(attendue)[:12]}… ({source})")
    lus["sondes_npz"] = p_npz
    sondes_npz, meta_npz = lire_sondes_npz(p_npz)
    choix = choisir_sondes(fig, sondes_npz, a.sondes, a.un_seul_couple)
    couches = sorted({int(c["couche"]) for c in choix})

    # Concepts : sceau compagnon obligatoire (CLJ-03)
    p_c = exiger(a.concepts, "liste de mots des concepts")
    verifier_compagnon(p_c, obligatoire=True)
    lus["concepts"] = p_c
    concepts_mots = lire_concepts(p_c)
    for c in choix:
        if c["concept"] not in concepts_mots:
            raise Refus("concepts-illisibles", f"{p_c} : pas de liste pour le concept {c['concept']!r}")

    # Lentille, configuration, poids, vocabulaire
    p_lent = exiger(a.lentille, "fichier de lentille")
    J, meta_lent = lire_lentille(p_lent, couches)
    lus["lentille"] = p_lent
    config = None
    if a.lentille_config:
        p_cfg = exiger(a.lentille_config, "lentille-config.yaml")
        lus["lentille_config"] = p_cfg
        config = lire_config_lentille(p_cfg)
    n_textes, ajustee_sur = nombre_de_textes(config)
    if n_textes is not None and isinstance(meta_lent.get("n_prompts"), int) and meta_lent["n_prompts"] != n_textes:
        raise Refus("lentille-config-discordante", f"lentille n_prompts = {meta_lent['n_prompts']} ≠ {n_textes} "
                    "dans lentille-config.yaml : la configuration n'est pas celle de ce fichier de lentille")
    WU, f_wu = lire_tableau(a.desembedding, "désembedding")
    g, f_g = lire_tableau(a.norme_finale, "normalisation finale")
    for i, f in enumerate(f_wu):
        lus[f"desembedding_{i}"] = f
    for i, f in enumerate(f_g):
        lus[f"norme_finale_{i}"] = f
    g = g.astype(np.float64).reshape(-1)
    if WU.ndim != 2:
        raise Refus("dimension", f"désembedding de forme {WU.shape} : [vocabulaire, largeur] attendu")
    Vt, d = WU.shape
    tailles = {"désembedding (colonnes)": d, "normalisation finale": g.size,
               **{f"J_{c}": J[c].shape[0] for c in couches},
               **{c["nom"]: sondes_npz[c["nom"]]["tableaux"]["w"].size for c in choix}}
    if len(set(tailles.values())) != 1:
        raise Refus("dimension", f"largeurs discordantes : {tailles}")
    p_voc = exiger(a.vocabulaire, "vocabulaire")
    lus["vocabulaire"] = p_voc
    textes, info_voc = lire_vocabulaire(p_voc, Vt)
    mots = masque_mots(textes)
    debut = masque_debut_de_mot(textes)
    idx_debut = np.flatnonzero(debut)
    if idx_debut.size <= K_TETE:
        raise Refus("vocabulaire", f"{idx_debut.size} jetons de début de mot : plus de {K_TETE} attendus")
    concepts = resoudre_concepts(textes, debut, concepts_mots)

    # Variantes descriptives
    ctx_par_couche = {c: {} for c in couches}
    variantes = ["direction"]
    if a.covariances:
        p_cov = exiger(a.covariances, "covariances")
        lus["covariances"] = p_cov
        with np.load(p_cov, allow_pickle=False) as z:
            for c in couches:
                if f"c{c}" not in z.files:
                    raise Refus("couche-absente-covariances", f"{p_cov} : clé c{c} absente")
                S = np.asarray(z[f"c{c}"], dtype=np.float64)
                if S.shape not in ((d,), (d, d)):
                    raise Refus("dimension", f"covariance c{c} de forme {S.shape}")
                ctx_par_couche[c]["covariance"] = S
        variantes.append("motif")
    if a.activations_moyennes:
        p_am = exiger(a.activations_moyennes, "activations moyennes")
        lus["activations_moyennes"] = p_am
        with np.load(p_am, allow_pickle=False) as z:
            for c in couches:
                if f"c{c}" not in z.files:
                    raise Refus("couche-absente-activations", f"{p_am} : clé c{c} absente")
                h = np.asarray(z[f"c{c}"], dtype=np.float64).reshape(-1)
                if h.size != d:
                    raise Refus("dimension", f"activation moyenne c{c} de taille {h.size}")
                ctx_par_couche[c].update(activation_moyenne=h, alpha=a.alpha)
        variantes.append("autour")

    # Empreintes attendues (CLJ-04) : contrôle avant tout calcul
    controle_empreintes = "non contrôlées (option --empreintes-attendues absente)"
    if a.empreintes_attendues:
        p_att = exiger(a.empreintes_attendues, "fichier d'empreintes attendues")
        attendues = lire_empreintes_attendues(p_att)
        exemptes = {"sondes_json": "sceau compagnon", "sondes_npz": source, "concepts": "sceau compagnon"}
        detail = {}
        for k, p in lus.items():
            if k in exemptes:
                detail[k] = f"contrôlée par {exemptes[k]}"
                continue
            if p.name not in attendues:
                raise Refus("empreinte-attendue-absente", f"{p.name} ({k}) n'a pas de ligne dans {p_att.name}")
            reelle = sha256_fichier(p)
            if reelle != attendues[p.name]:
                raise Refus("empreinte-entree", f"{p} : {reelle[:12]}… ≠ attendue {attendues[p.name][:12]}… ({p_att.name})")
            detail[k] = "conforme"
        lus["empreintes_attendues"] = p_att
        controle_empreintes = {"fichier": p_att.name, "entrees": detail}

    de = Desembedding(WU)

    # Références nulles : planchers de P3 par (concept, couche), directions isotropes par couche (SeedSequence, R9)
    planchers = {}
    for concept, noms in (meta_npz.get("planchers") or {}).items():
        for n in noms:
            if n in sondes_npz:
                s = sondes_npz[n]
                planchers.setdefault((concept, int(s["couche"])), []).append(s["tableaux"]["w"])
    graines, aleatoires = {}, {}
    for c in couches:
        ss = graines_aleatoires(f"aleatoire/c{c}")
        graines[f"aleatoire/c{c}"] = {"entropie": str(ss.entropy), "spawn_key": [str(x) for x in ss.spawn_key]}
        aleatoires[c] = np.random.default_rng(ss).standard_normal((d, N_ALEATOIRES))
    cache_nuls: dict[tuple, np.ndarray] = {}

    def tetes_nulles(cle, V_nul, T):
        if cle not in cache_nuls:
            cache_nuls[cle] = de.tete_debut_lot(vers_sortie(V_nul, T, g, "direction", {}), idx_debut, K_TETE)
        return cache_nuls[cle]

    ids_concept = {n: np.array([j["id"] for j in info["jetons"]], dtype=np.int64) for n, info in concepts.items()}

    resultats, verdicts = [], []
    for c in choix:
        s = sondes_npz[c["nom"]]
        w = s["tableaux"]["w"]
        L = int(c["couche"])
        pl = planchers.get((c["concept"], L))
        if c["principale"] and (pl is None or len(pl) < N_PLANCHERS_MIN):
            raise Refus("planchers-insuffisants", f"{c['nom']} : {0 if pl is None else len(pl)} planchers à la couche "
                        f"{L} ; la règle primaire en exige au moins {N_PLANCHERS_MIN}")
        entree = {"nom": c["nom"], "concept": c["concept"], "principale": c["principale"], "famille": c["famille"],
                  "couche": L, "classe": c["classe"], "agregation": c["agregation"], "empreinte": c["empreinte"],
                  "biais_b": s["b"], "norme_w": float(np.linalg.norm(w)),
                  "norme_Jw_sur_norme_w": float(np.linalg.norm(J[L] @ w) / np.linalg.norm(w)),
                  "cosinus_w_Jw": float(w @ (J[L] @ w) / (np.linalg.norm(w) * np.linalg.norm(J[L] @ w))),
                  "regle": {}, "variantes": {}}
        for var in variantes:
            ctx = ctx_par_couche[L]
            bloc, logits_par_lentille = {}, {}
            for lentille, T in (("logits", None), ("jacobienne", J[L])):
                y = vers_sortie(w[:, None], T, g, var, ctx)[:, 0]
                lg = de.logits(y)
                logits_par_lentille[lentille] = lg
                r = {"plus": {"tete": tete(lg, textes, K_TETE), "tete_mots": tete(lg, textes, K_TETE, mots),
                              "tete_debut_de_mot": tete(lg, textes, K_TETE, debut)},
                     "moins": {"tete": tete(-lg, textes, K_TETE), "tete_mots": tete(-lg, textes, K_TETE, mots),
                               "tete_debut_de_mot": tete(-lg, textes, K_TETE, debut)}}

                # Règle primaire (variante « direction », sens plus, concept propre) : verdict pour les principales,
                # application descriptive pour les autres sondes.
                if var == "direction":
                    tete_plus = np.array([t["id"] for t in r["plus"]["tete_debut_de_mot"]], dtype=np.int64)
                    comptes = {n: int(np.isin(tete_plus, ids).sum()) for n, ids in ids_concept.items()}
                    t_iso = tetes_nulles(("iso", L, lentille), aleatoires[L], T)
                    nul_iso = np.isin(t_iso, ids_concept[c["concept"]]).sum(axis=0)
                    nul_pl = None
                    if pl:
                        t_pl = tetes_nulles(("plancher", c["concept"], L, lentille), np.stack(pl, axis=1), T)
                        nul_pl = np.isin(t_pl, ids_concept[c["concept"]]).sum(axis=0)
                    app = appliquer_regle(comptes[c["concept"]], nul_iso, nul_pl)
                    app["comptes_par_concept_diagnostic"] = comptes
                    if c["principale"]:
                        app["statut"] = "règle primaire"
                        verdicts.append({"sonde": c["nom"], "concept": c["concept"], "couche": L, "lentille": lentille,
                                         "S": app["S"], "quantile_0_99_isotropes": app["isotropes"]["quantile_0_99"],
                                         "quantile_0_99_planchers": app["planchers"]["quantile_0_99"],
                                         "n_planchers": app["planchers"]["n"], "verdict": app["verdict"]})
                    else:
                        app["statut"] = ("descriptif, hors règle primaire"
                                         + ("" if pl else " ; planchers absents : isotropes seules"))
                        app["verdict_descriptif"] = app.pop("verdict")
                    entree["regle"][lentille] = app

                # Diagnostics (descriptifs, jamais critères) : scores z et p, comme en v1
                diag = {}
                for nom_c, info_c in concepts.items():
                    ids = ids_concept[nom_c]
                    cbar = WU[ids].astype(np.float64).mean(axis=0)
                    z = float(de.z_lot(y[:, None], cbar)[0])
                    z_direct = float((lg[ids].mean() - lg.mean()) / lg.std())
                    if not np.isclose(z, z_direct, rtol=1e-4, atol=1e-4):      # logits en simple précision
                        raise Refus("incoherence-interne", f"score z par Gram {z} ≠ direct {z_direct}")
                    rangs = np.empty(Vt, dtype=int)
                    rangs[np.argsort(-lg, kind="stable")] = np.arange(1, Vt + 1)
                    tete_p = {t["id"] for t in r["plus"]["tete"]}
                    tete_m = {t["id"] for t in r["moins"]["tete"]}
                    item = {"z": z, "jetons_concept": int(ids.size),
                            "n_concept_tete_plus": len(tete_p & set(ids.tolist())),
                            "n_concept_tete_moins": len(tete_m & set(ids.tolist())),
                            "meilleur_rang_plus": int(rangs[ids].min()),
                            "meilleur_rang_moins": int((Vt + 1 - rangs[ids]).min())}
                    zn = de.z_lot(vers_sortie(aleatoires[L], T, g, var, ctx), cbar)
                    item["isotropes"] = {"n": int(zn.size), "p_haut": p_haut(z, zn), "p_bas": p_haut(-z, -zn),
                                         "p_bilateral": p_haut(abs(z), np.abs(zn)),
                                         "z_quantiles_5_50_95": [float(q) for q in np.quantile(zn, [0.05, 0.5, 0.95])]}
                    plc = planchers.get((c["concept"], L))
                    if plc:
                        zp = de.z_lot(vers_sortie(np.stack(plc, axis=1), T, g, var, ctx), cbar)
                        item["planchers"] = {"n": int(zp.size), "p_haut": p_haut(z, zp), "p_bas": p_haut(-z, -zp),
                                             "p_bilateral": p_haut(abs(z), np.abs(zp)),
                                             "z_quantiles_5_50_95": [float(q) for q in np.quantile(zp, [0.05, 0.5, 0.95])]}
                    else:
                        item["planchers"] = {"statut": "pas de plancher de ce concept à cette couche"}
                    diag[nom_c] = item
                r["diagnostics_z"] = diag
                bloc[lentille] = r
            a_, b_ = logits_par_lentille["logits"], logits_par_lentille["jacobienne"]
            ac, bc = a_ - a_.mean(), b_ - b_.mean()
            bloc["recouvrement"] = {
                "plus": recouvrement(bloc["logits"]["plus"]["tete"], bloc["jacobienne"]["plus"]["tete"]),
                "moins": recouvrement(bloc["logits"]["moins"]["tete"], bloc["jacobienne"]["moins"]["tete"]),
                "plus_mots": recouvrement(bloc["logits"]["plus"]["tete_mots"], bloc["jacobienne"]["plus"]["tete_mots"]),
                "moins_mots": recouvrement(bloc["logits"]["moins"]["tete_mots"], bloc["jacobienne"]["moins"]["tete_mots"]),
                "plus_debut_de_mot": recouvrement(bloc["logits"]["plus"]["tete_debut_de_mot"],
                                                  bloc["jacobienne"]["plus"]["tete_debut_de_mot"]),
                "cosinus_logits_centres": float(ac @ bc / (np.linalg.norm(ac) * np.linalg.norm(bc)))}
            entree["variantes"][var] = bloc
        resultats.append(entree)

    verdicts.sort(key=lambda v: (v["sonde"], v["lentille"]))         # ordre stable, quel que soit le mode
    principales_attendues = set(fig["resultat"]["principales"].values())
    corps = {
        "version": VERSION, "statut": "exploratoire, non opposable ; seule la règle primaire porte un verdict",
        "regle_primaire": {
            "enonce": ENONCE_REGLE_PRIMAIRE, "empreinte_enonce": sha256_texte(ENONCE_REGLE_PRIMAIRE),
            "parametres": {"k": K_TETE, "n_isotropes": N_ALEATOIRES, "graine": GRAINE, "quantile": QUANTILE_PRIMAIRE,
                           "methode_quantile": METHODE_QUANTILE, "min_jetons": MIN_JETONS_PRIMAIRE,
                           "n_planchers_min": N_PLANCHERS_MIN},
            "complete": {v["sonde"] for v in verdicts} == principales_attendues,
            "verdicts": verdicts},
        "convention_couche": "couche ℓ de P3 = clé ℓ de la lentille (sortie du bloc décodeur ℓ, indice à partir de 0) ; "
                             "voir note-convention-couche-jlens-p3-v1.md",
        "lecture_des_signes": "plus = direction +w (vers la classe 1 : consigne malhonnête pour « tromperie », "
                              "« high-stakes » pour « enjeux ») ; moins = −w",
        "run_sondes": fig.get("run_id"), "principales": fig["resultat"].get("principales"),
        "lentille_meta": meta_lent, "lentille_ajustee_sur": ajustee_sur, "largeur": d,
        "vocabulaire": {"taille_desembedding": Vt, **info_voc, "jetons_mots": int(mots.sum()),
                        "jetons_debut_de_mot": int(debut.sum())},
        "parametres": {"sondes": a.sondes, "un_seul_couple": a.un_seul_couple, "variantes": variantes,
                       "alpha": a.alpha if a.activations_moyennes else None,
                       "correspondance": "début de mot, exacte, casse libre"},
        "concepts": concepts, "sondes": resultats,
    }
    sha_sortie = ecrire_scelle(sortie, json.dumps(corps, ensure_ascii=False, indent=1) + "\n")
    try:
        import torch  # noqa: F401
        v_torch = torch.__version__
    except ImportError:
        v_torch = None
    ici = Path(__file__).resolve()
    provenance = ({"commit": a.commit, "source": "option --commit"} if a.commit else commit_git(ici.parent, ici))
    manifeste = {
        "script": ici.name, "script_sha256": sha256_fichier(ici), "version": VERSION,
        "interpreteur": sys.executable, "commande": [sys.executable, *sys.argv],
        "drapeaux_python": {"isolated": sys.flags.isolated, "dont_write_bytecode": sys.flags.dont_write_bytecode},
        "cree_le_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "duree_s": round(time.time() - t0, 2),
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "torch": v_torch,
                     "plateforme": platform.platform()},
        "depot": provenance,
        "revision_modele": a.revision_modele or "inconnue (option --revision-modele absente)",
        "lentille_config": ({"chemin": str(lus["lentille_config"]), "sha256": sha256_fichier(lus["lentille_config"]),
                             "cles": config, "ajustee_sur": ajustee_sur} if config is not None
                            else "absente (option --lentille-config absente)"),
        "empreintes_attendues": controle_empreintes,
        "regle_primaire_empreinte_enonce": sha256_texte(ENONCE_REGLE_PRIMAIRE),
        "entrees": {k: {"chemin": str(p), "sha256": sha256_fichier(p), "octets": p.stat().st_size} for k, p in lus.items()},
        "graines": {"mode": "numpy.random.SeedSequence(entropy=20261029, spawn_key=(sha256(etiquette)[:8],))", **graines},
        "sortie": {"chemin": sortie.name, "sha256": sha_sortie},
    }
    ecrire_scelle(manifeste_ch, json.dumps(manifeste, ensure_ascii=False, indent=1, default=str) + "\n")
    print(f"sortie : {sortie} ({sha_sortie[:12]}…) ; manifeste : {manifeste_ch} ; {len(resultats)} sondes, "
          f"variantes {variantes}")
    return 0


# --------------------------------------------------------------------------------------------------------------------
# Vérifier la liste de mots contre le vocabulaire seul

def verifier_concepts(a) -> int:
    p_c = exiger(a.concepts, "liste de mots des concepts")
    verifier_compagnon(p_c, obligatoire=True)
    p_voc = exiger(a.vocabulaire, "vocabulaire")
    textes, info = lire_vocabulaire(p_voc, None)
    debut = masque_debut_de_mot(textes)
    concepts = lire_concepts(p_c)
    lignes, sans = [], {}
    for nom, mots_c in concepts.items():
        _, par_mot = jetons_du_concept(textes, debut, mots_c)
        for m, l in par_mot.items():
            lignes.append(f"{nom}\t{m}\t{len(l)}\t{[textes[i] for i in l]}")
            if not l:
                sans.setdefault(nom, []).append(m)
    print(f"vocabulaire {p_voc.name} ({sha256_fichier(p_voc)[:12]}…, {len(textes)} jetons) ; liste {p_c.name} "
          f"({sha256_fichier(p_c)[:12]}…)\n" + "\n".join(lignes))
    if sans:
        raise Refus("mot-sans-jeton", f"mots sans jeton de début de mot : {sans}")
    print("tous les mots ont au moins un jeton de début de mot")
    return 0


# --------------------------------------------------------------------------------------------------------------------
# Convertir une lentille .pt en .npz (exige torch)

def convertir_lentille(a) -> int:
    p = exiger(a.pt, "lentille .pt")
    sortie = Path(a.sortie)
    if sortie.exists() or Path(str(sortie) + ".sha256").exists():
        raise Refus("sortie-existe", f"{sortie} existe déjà (R12)")
    ck = charger_pt(p)
    import torch
    tab = {}
    for c in a.couches:
        if c not in ck["J"]:
            raise Refus("couche-absente-lentille", f"{p} : couche {c} absente ({sorted(ck['J'])})")
        tab[f"J_{c}"] = ck["J"][c].to(torch.float16).numpy()
    tab["n_prompts"] = np.array(ck.get("n_prompts", -1))
    tab["d_model"] = np.array(ck.get("d_model", -1))
    tab["source_layers"] = np.array(ck.get("source_layers", []))
    with open(sortie, "wb") as f:
        np.savez(f, **tab)
    sha = sha256_fichier(sortie)
    Path(str(sortie) + ".sha256").write_text(f"{sha}  {sortie.name}\n", encoding="utf-8")
    print(f"{sortie} : couches {a.couches}, empreinte {sha} (source {p.name} : {sha256_fichier(p)})")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sp = ap.add_subparsers(dest="commande", required=True)
    c = sp.add_parser("comparer")
    c.add_argument("--sondes-json", required=True)
    c.add_argument("--sondes-npz", required=True)
    c.add_argument("--sha256-sondes-npz", default=None, help="empreinte attendue (défaut : celle de sondes-figees.json)")
    c.add_argument("--lentille", required=True)
    c.add_argument("--lentille-config", default=None, help="lentille-config.yaml (empreinte, nombre de textes)")
    c.add_argument("--desembedding", required=True)
    c.add_argument("--norme-finale", required=True)
    c.add_argument("--vocabulaire", required=True)
    c.add_argument("--concepts", required=True, help="liste de mots scellée (concepts-sondes-p3-v2.json)")
    c.add_argument("--empreintes-attendues", default=None, help="fichier au format sha256sum (CLJ-04)")
    c.add_argument("--sondes", choices=("principales-par-couche", "toutes-lineaires"), default="principales-par-couche")
    c.add_argument("--un-seul-couple", default=None, metavar="SONDE,COUCHE",
                   help="une seule sonde : nom complet ou sans le suffixe -c<couche>, puis la couche")
    c.add_argument("--covariances", default=None, help="npz, clés c<couche> : (d,) variances ou (d, d) covariance")
    c.add_argument("--activations-moyennes", default=None, help="npz, clés c<couche> : (d,)")
    c.add_argument("--alpha", type=float, default=0.1)
    c.add_argument("--revision-modele", default=None, help="révision des poids du modèle (consignée au manifeste)")
    c.add_argument("--commit", default=None, help="commit du dépôt (défaut : git rev-parse HEAD du dossier du script)")
    c.add_argument("--sortie", required=True)
    k = sp.add_parser("verifier-concepts")
    k.add_argument("--vocabulaire", required=True)
    k.add_argument("--concepts", required=True)
    v = sp.add_parser("convertir-lentille")
    v.add_argument("--pt", required=True)
    v.add_argument("--couches", type=int, nargs="+", default=[7, 15, 23])
    v.add_argument("--sortie", required=True)
    a = ap.parse_args(argv)
    try:
        return {"comparer": comparer, "verifier-concepts": verifier_concepts,
                "convertir-lentille": convertir_lentille}[a.commande](a)
    except Refus as e:
        print(f"REFUS {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
