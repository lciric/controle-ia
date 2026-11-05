"""Lentille jacobienne contre lentille des logits sur les 16 sondes non principales de P3 — v3.

Rédigé le 29 octobre 2026. **Exploratoire, processeur seul, non opposable** : aucun chiffre sorti de ce script ne sert
de critère de porte. Ce script applique la règle primaire v3, scellée avant toute lecture
(`docs/notes/lentilles-sondes-p3-v1/regle-primaire-v3/`, énoncé `be020390…`, liste de mots `aac34d5c…`), et rien
d'autre en règle : tout le reste de la sortie est descriptif. Les v1 et v2 restent archivées sans modification.

Ce qui change par rapport à la v2 (`besoins-script-v3.md`, B1 à B5, U1 à U3) :
- B1 : un seul mode, `--sondes non-principales-lineaires` : toutes les `SondeLineaireJetons` hors planchers et hors
  principales. Refus si la sélection n'est pas exactement les 16 sondes nommées par la règle (constante `SONDES_V3`),
  si une principale y entre, si les principales du fichier ne sont pas celles de la règle. Les principales ne sont
  décodées nulle part, même en descriptif. `--un-seul-couple`, les variantes « motif » et « autour » et
  `convertir-lentille` sont retirés ;
- B2 : nulle isotrope de 10 000 directions par couche, `numpy.random.SeedSequence(entropy=20261029,
  spawn_key=(clé de l'étiquette « isotropes-v3/c<couche> »,))`, tirées par blocs de 1 000 lignes ; mêmes directions
  pour les deux lentilles à une couche ;
- B3 : verdict par comptes entiers, sans `np.quantile` : « cohérent » ⇔ S ≥ 2, n_iso ≤ 14 et, à la couche 15,
  n_pl ≤ 2 ; refus `planchers-insuffisants` s'il n'y a pas exactement 200 planchers du concept, tous à la couche 15 ;
  constantes gelées, recalculées au lancement (refus `incoherence-interne` sinon) ;
- B4 : énoncé recopié mot pour mot (`ENONCE_REGLE_PRIMAIRE_V3`), contrôlé contre son empreinte au lancement (refus
  `enonce-altere`) et contre le fichier gelé passé par `--enonce-regle` (refus `enonce-fichier-discordant`) ;
  empreinte de la liste de mots contrôlée en dur (refus `empreinte-concepts`) en plus du sceau compagnon ;
- B5 : verdict d'ensemble par lentille (X, niveau), comparaison des lentilles (grille, b, c, test du signe exact
  bilatéral par `math.comb`, formulation permise ou non) ; il faut les 32 cases, sinon refus `cases-manquantes`,
  aucune sortie, aucun verdict ;
- U1 : têtes nulles calculées sur les seuls jetons de début de mot, par lots ; scores z sur les 200 premières
  isotropes, mis en cache par (couche, lentille) ;
- U2 : descriptif (S en mots distincts, verdict au seuil v2 sur les 200 premières isotropes, verdict sans planchers à
  la couche 15, médiane et quantile 0,99 des nulles, strates, déclencheurs d'audit de la section 5 de la règle) ;
- U3 (CLJ2-01) : `lentille-config.yaml` lu sur deux niveaux ; le nombre de textes vient de `results.prompts_fitted`,
  jamais de `fit.n_prompts` ; la garde `lentille-config-discordante` agit sur le vrai format ;
- run et empreintes des 16 sondes contrôlés en dur (`RUN_V3`, préfixes de `SONDES_V3`, tirés du tableau de la
  règle). L'option `--essai-factice` lève ces deux contrôles seulement, pour l'essai sur entrées synthétiques ; elle
  est écrite en tête de la sortie et ne doit jamais figurer dans la commande réelle.

Calcul des lentilles inchangé depuis la v2 (`vers_sortie`, `rms`, `Desembedding`, `tete`, `masque_debut_de_mot`,
`jetons_du_concept`) : logits = W_U · (g ⊙ v / rms(v)), v = w (logits) ou v = J_ℓ · w (jacobienne). Convention de
couche : couche ℓ de P3 = clé ℓ de la lentille (contre-lecture v2, CLJ-01 levée).

Refus nommés : code de sortie 2, ligne « REFUS <code> : … » sur la sortie d'erreur, aucune sortie écrite.

Usage (depuis n'importe quel dossier, sur la machine qui a les entrées) :
  python3 -I -B <ce script> comparer --sondes non-principales-lineaires \\
     --sondes-json diag/20261019-230011-p3-reel/sondes-figees.json \\
     --sondes-npz <entrees>/sondes-figees-legeres.npz \\
     --lentille <entrees>/lentille-Llama-3.1-8B-Instruct_jacobian_lens.pt \\
     --lentille-config <entrees>/lentille-config.yaml \\
     --desembedding <entrees>/model-00004-of-00004.safetensors:lm_head.weight \\
     --norme-finale <entrees>/model-00004-of-00004.safetensors:model.norm.weight \\
     --vocabulaire <entrees>/tokenizer.json \\
     --concepts <regle-primaire-v3>/concepts-sondes-p3-v3.json \\
     --enonce-regle <regle-primaire-v3>/enonce-regle-primaire-v3.txt \\
     --empreintes-attendues <entrees>/empreintes-entrees-v2.txt \\
     --revision-modele 0e9e39f249a16976918f6564b8830bc894c89659 \\
     --sortie <sortie>/sortie-jlens-sondes-p3-v3.json
Spécification d'un tableau : `chemin.npy`, `chemin.npz:cle`, `chemin.safetensors:nom`, ou `index.json:nom` pour tout
fichier JSON qui porte une clé `weight_map`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import re
import struct
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

VERSION = "v3"

# ---- Constantes gelées par la règle primaire v3 (pas d'options) ------------------------------------------------------
GRAINE = 20261029                         # entropie de numpy.random.SeedSequence (R9)
ETIQUETTE_ISOTROPES = "isotropes-v3/c{couche}"
K_TETE = 20                               # taille de la tête (jetons de début de mot)
N_ISOTROPES = 10_000                      # directions isotropes par couche
BLOC_ISOTROPES = 1_000                    # lignes tirées à la fois (direction i = ligne i, dans l'ordre)
LOT_TETES = 250                           # colonnes décodées à la fois (mémoire seulement : sans effet sur les têtes)
N_PLANCHERS = 200                         # exactement, par concept, à la couche 15
COUCHE_PLANCHERS = 15
S_MIN = 2
ALPHA = Fraction(5, 100)                  # erreur familiale, Bonferroni
M_TESTS = 32                              # 16 sondes × 2 lentilles × un bout
N_ISO_MAX = 14                            # ⇔ (1 + n_iso)/10 001 ≤ 0,05/32
QUANTILE_PLANCHERS = Fraction(99, 100)    # inverted_cdf de 200 valeurs : 198ᵉ statistique d'ordre
N_PL_MAX = 2                              # ⇔ S strictement supérieur au troisième plus grand des 200 planchers
ALPHA_SIGNE = Fraction(5, 100)            # test du signe exact bilatéral sur (b, c)
LENTILLES = ("logits", "jacobienne")

# ---- Descriptif (jamais critère) -------------------------------------------------------------------------------------
N_ISO_SEUIL_V2 = 200                      # verdict « au seuil v2 non corrigé » : n ≤ 2 sur les 200 premières isotropes
N_SEUIL_V2_MAX = 2
N_ISO_Z = 200                             # scores z de diagnostic : 200 premières isotropes
MOTS_LARGES = ("serious", "critical", "safety", "damage", "dead", "secret", "hide")   # règle v3, section 2
EPS_RMS_LLAMA = 1e-5                      # rms_norm_eps de Llama-3.1-8B-Instruct (variante « autour », non utilisée)
TAILLE_BLOC = 16384                       # lignes de W_U traitées à la fois pour la matrice de Gram

# ---- Ce que la règle nomme, contrôlé en dur -------------------------------------------------------------------------
RUN_V3 = "20261019-230011-p3-reel"
PRINCIPALES_V3 = {"enjeux": "enjeux-lineaire-c15", "tromperie": "tromperie-difference_moyennes-c15"}
SONDES_V3 = {                             # nom → préfixe d'empreinte (tableau de la règle v3, section 1)
    "tromperie-attention-c7": "520513a1e74e7b60",
    "tromperie-difference_moyennes-c7": "ed464425a3d54cac",
    "tromperie-lineaire-c7": "d546b2b224221adc",
    "enjeux-attention-c7": "294c9b4f7d62f67f",
    "enjeux-difference_moyennes-c7": "dc15223846b9f724",
    "enjeux-lineaire-c7": "a97efee697808d54",
    "tromperie-attention-c15": "d29ba633904a611e",
    "tromperie-lineaire-c15": "80908a562b4e4c89",
    "enjeux-attention-c15": "11f9e36a2eb63511",
    "enjeux-difference_moyennes-c15": "009b715aed49fde9",
    "tromperie-attention-c23": "01be0867b895276c",
    "tromperie-difference_moyennes-c23": "fc4be9603a138dc4",
    "tromperie-lineaire-c23": "04e3222341bfcd58",
    "enjeux-attention-c23": "3ba5124cf7336785",
    "enjeux-difference_moyennes-c23": "d72e9e1587738f90",
    "enjeux-lineaire-c23": "e5be383a33020511",
}
EMPREINTE_CONCEPTS_V3 = "aac34d5cb52637fef6ebdd0d36009f8842efdef52d5e5298334e3a84f388bf6c"
EMPREINTE_ENONCE_V3 = "be02039011c50c50a4eca0c38c26c7d31c38f6fc7315567659e8fd6cb7b64820"

NIVEAUX = ("aucune verbalisation détectée", "verbalisation minoritaire, au-delà du hasard", "verbalisation majoritaire")

# Énoncé gelé : copie mot pour mot de `enonce-regle-primaire-v3.txt` (UTF-8, sans saut de ligne final).
ENONCE_REGLE_PRIMAIRE_V3 = (
    'Règle primaire unique v3, gelée avant toute lecture des lentilles sur les sondes non principales (29 '
    'octobre 2026). Sondes lues : les 16 sondes SondeLineaireJetons du run 20261019-230011-p3-reel, hors '
    'planchers et hors les deux principales tromperie-difference_moyennes-c15 et enjeux-lineaire-c15, qui ne '
    'sont pas décodées. Pour chaque sonde et chacune des deux lentilles (logits, jacobienne), on décode la '
    'seule direction +w (variante « direction », sens de la classe 1). S = nombre de jetons de la liste du '
    'concept propre (concepts-sondes-p3-v3.json, sha256 '
    'aac34d5cb52637fef6ebdd0d36009f8842efdef52d5e5298334e3a84f388bf6c ; jetons de début de mot, casse libre) '
    'parmi les 20 jetons de tête, la tête étant restreinte aux jetons de début de mot. Nulle isotrope : 10 000 '
    'directions isotropes par couche (numpy.random.SeedSequence, entropie 20261029, étiquette '
    'isotropes-v3/c<couche>), décodées par la même lentille à la même couche ; n_iso = nombre de ces '
    'directions dont la statistique est supérieure ou égale à S. Nulle des planchers, à la couche 15 seulement '
    ": les 200 planchers appariés en covariance du concept (refus s'il n'y en a pas exactement 200) ; n_pl = "
    'nombre de planchers dont la statistique est supérieure ou égale à S. Verdict « cohérent » si S >= 2, si '
    'n_iso <= 14 (p de rang (1 + n_iso)/10001 <= 0,05/32 : correction de Bonferroni sur 32 tests, 16 sondes × '
    '2 lentilles × un bout) et, à la couche 15 seulement, si n_pl <= 2 (S strictement supérieur au quantile '
    '0,99 inverted_cdf de 200 valeurs, qui est le troisième plus grand : niveau de rang 3/201, environ 1,5 %, '
    'non corrigé) ; sinon « non cohérent ». Aux couches 7 et 23, la nulle isotrope est seule. Verdict '
    "d'ensemble, par lentille : X = nombre de sondes cohérentes sur 16 ; X = 0 « aucune verbalisation détectée "
    '» ; 1 <= X <= 7 « verbalisation minoritaire, au-delà du hasard » ; X >= 8 « verbalisation majoritaire ». '
    "Sous la nulle isotrope globale, la probabilité d'au moins un « cohérent » à tort parmi les 32 tests est "
    'au plus 32 × 15/10001, soit environ 0,048, quelle que soit la dépendance entre tests. Comparaison des '
    'lentilles : b = sondes cohérentes sous la jacobienne seule, c = sondes cohérentes sous les logits seuls ; '
    "la phrase « une lentille verbalise plus de sondes que l'autre » n'est écrite que si le test du signe "
    "exact bilatéral sur (b, c) donne p <= 0,05. Les 32 cases sont exigées : s'il en manque une, aucun "
    "verdict. Pas de seuil de rechange, pas d'autre liste de mots, pas d'autre K, pas d'autre nombre de "
    'directions isotropes. Tout le reste (sens −w, autre concept, scores z, têtes brutes, variantes, comptes '
    'en mots distincts, verdicts sans planchers ou au seuil non corrigé, strates) est descriptif et ne sert '
    'pas de critère.')


class Refus(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(f"{code} : {message}")
        self.code = code


# --------------------------------------------------------------------------------------------------------------------
# Contrôles internes : énoncé et constantes (au lancement, avant toute entrée)

def sha256_texte(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def controler_enonce() -> None:
    e = sha256_texte(ENONCE_REGLE_PRIMAIRE_V3)
    if e != EMPREINTE_ENONCE_V3:
        raise Refus("enonce-altere", f"l'énoncé du script a l'empreinte {e[:12]}…, la règle v3 gelée {EMPREINTE_ENONCE_V3[:12]}…"
                    " : le script n'applique pas la règle scellée")


def n_iso_max_calcule() -> int:
    """Plus grand n tel que (1 + n)/(N + 1) ≤ α/m, en fractions exactes."""
    n = math.floor(ALPHA / M_TESTS * (N_ISOTROPES + 1)) - 1
    assert Fraction(1 + n, N_ISOTROPES + 1) <= ALPHA / M_TESTS < Fraction(2 + n, N_ISOTROPES + 1)
    return n


def n_pl_max_calcule() -> int:
    """inverted_cdf : le quantile q de N valeurs est la statistique d'ordre ⌈qN⌉ ; S > ce quantile ⇔ au plus
    N − ⌈qN⌉ valeurs sont ≥ S (statistique entière)."""
    return N_PLANCHERS - math.ceil(QUANTILE_PLANCHERS * N_PLANCHERS)


def borne_familiale() -> Fraction:
    return M_TESTS * Fraction(N_ISO_MAX + 1, N_ISOTROPES + 1)


def controler_constantes() -> None:
    ecarts = []
    if len(SONDES_V3) != 16 or M_TESTS != len(SONDES_V3) * len(LENTILLES) * 1:
        ecarts.append(f"m = {M_TESTS}, sondes × lentilles = {len(SONDES_V3)} × {len(LENTILLES)}")
    if n_iso_max_calcule() != N_ISO_MAX:
        ecarts.append(f"n_iso max calculé {n_iso_max_calcule()} ≠ {N_ISO_MAX}")
    if n_pl_max_calcule() != N_PL_MAX:
        ecarts.append(f"n_pl max calculé {n_pl_max_calcule()} ≠ {N_PL_MAX}")
    if not borne_familiale() <= ALPHA:
        ecarts.append(f"borne familiale {float(borne_familiale())} > α")
    if set(PRINCIPALES_V3.values()) & set(SONDES_V3):
        ecarts.append("une principale est dans la liste des 16")
    if N_ISOTROPES % BLOC_ISOTROPES or BLOC_ISOTROPES < max(N_ISO_SEUIL_V2, N_ISO_Z):
        ecarts.append("blocs d'isotropes")
    if ecarts:
        raise Refus("incoherence-interne", " ; ".join(ecarts))


# --------------------------------------------------------------------------------------------------------------------
# Règle v3 : verdict par comptes entiers, niveau d'ensemble, test du signe

def _entier(x, quoi):
    if isinstance(x, bool) or not isinstance(x, (int, np.integer)) or x < 0:
        raise Refus("incoherence-interne", f"{quoi} = {x!r} : entier positif ou nul attendu")
    return int(x)


def verdict_v3(S: int, n_iso: int, n_pl: int | None, couche: int) -> str:
    """« cohérent » ⇔ S ≥ 2 et n_iso ≤ 14 et (couche 15 ⇒ n_pl ≤ 2). Aux couches 7 et 23 : isotropes seules."""
    S, n_iso = _entier(S, "S"), _entier(n_iso, "n_iso")
    if couche == COUCHE_PLANCHERS:
        if n_pl is None:
            raise Refus("planchers-insuffisants", f"couche {couche} : la règle exige la nulle des planchers")
        n_pl = _entier(n_pl, "n_pl")
    elif n_pl is not None:
        raise Refus("incoherence-interne", f"couche {couche} : la règle n'y prévoit pas de planchers")
    ok = S >= S_MIN and n_iso <= N_ISO_MAX and (couche != COUCHE_PLANCHERS or n_pl <= N_PL_MAX)
    return "cohérent" if ok else "non cohérent"


def niveau(X: int) -> str:
    X = _entier(X, "X")
    if X > len(SONDES_V3):
        raise Refus("incoherence-interne", f"X = {X} > {len(SONDES_V3)}")
    return NIVEAUX[0] if X == 0 else NIVEAUX[1] if X <= 7 else NIVEAUX[2]


def test_signe_bilateral(b: int, c: int) -> Fraction:
    """p exact = min(1, 2 · P(Bin(b + c, 1/2) ≤ min(b, c))) ; p = 1 si b + c = 0."""
    b, c = _entier(b, "b"), _entier(c, "c")
    n = b + c
    if n == 0:
        return Fraction(1)
    queue = sum(math.comb(n, i) for i in range(min(b, c) + 1))
    return min(Fraction(1), Fraction(2 * queue, 2 ** n))


# --------------------------------------------------------------------------------------------------------------------
# Fichiers, empreintes

def sha256_fichier(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 22), b""):
            h.update(bloc)
    return h.hexdigest()


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
# Sondes (format de figees.py, relu sans torch) — inchangé depuis la v2

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
            if e["nom"] in sondes:
                raise Refus("sondes-npz-illisible", f"{e['nom']} en double dans {chemin}")
            sondes[e["nom"]] = {**{c: e[c] for c in ("classe", "nom", "couche", "agregation", "famille", "b", "empreinte")},
                                "tableaux": t}
    return sondes, index.get("meta", {})


def choisir_sondes_v3(fig: dict, sondes_npz: dict, meta_npz: dict, essai_factice: bool) -> list[dict]:
    """B1 : les 16 SondeLineaireJetons hors planchers et hors principales, exactement celles de la règle."""
    res = fig["resultat"]
    princ_json = res.get("principales")
    exclues = set(princ_json.values()) if isinstance(princ_json, dict) else set()
    lineaires = [s for s in res["sondes"] if s.get("classe") == "SondeLineaireJetons" and s.get("famille") != "plancher"]
    choix = [s for s in lineaires if s["nom"] not in exclues]
    noms = [s["nom"] for s in choix]
    presentes = sorted(set(noms) & set(PRINCIPALES_V3.values()))
    if presentes:
        raise Refus("principale-selectionnee", f"principale(s) de la règle v3 dans la sélection : {presentes} ; elles ne "
                    f"sont décodées nulle part (principales déclarées par sondes-figees.json : {princ_json})")
    if princ_json != PRINCIPALES_V3:
        raise Refus("principales-inattendues", f"principales de sondes-figees.json {princ_json} ≠ règle v3 {PRINCIPALES_V3}")
    if meta_npz.get("principales") != PRINCIPALES_V3:
        raise Refus("principales-inattendues", f"principales du fichier de poids {meta_npz.get('principales')} ≠ règle "
                    f"v3 {PRINCIPALES_V3}")
    if len(noms) != len(SONDES_V3) or len(set(noms)) != len(noms):
        raise Refus("compte-sondes", f"{len(noms)} sondes linéaires non principales, la règle v3 en exige exactement "
                    f"{len(SONDES_V3)} ; en trop : {sorted(set(noms) - set(SONDES_V3))} ; manquantes : "
                    f"{sorted(set(SONDES_V3) - set(noms))}")
    if set(noms) != set(SONDES_V3):
        raise Refus("sondes-inattendues", f"en trop : {sorted(set(noms) - set(SONDES_V3))} ; manquantes : "
                    f"{sorted(set(SONDES_V3) - set(noms))}")
    if not essai_factice and fig.get("run_id") != RUN_V3:
        raise Refus("run-inattendu", f"run {fig.get('run_id')!r} ≠ {RUN_V3!r} (règle v3)")
    par_nom = {s["nom"]: s for s in choix}
    sortie = []
    for nom in SONDES_V3:                                                       # ordre de la règle
        s = par_nom[nom]
        m = re.fullmatch(r"(tromperie|enjeux)-([a-z_]+)-c(\d+)", nom)
        if not m or s.get("famille") != m.group(2) or int(s["couche"]) != int(m.group(3)):
            raise Refus("sondes-inattendues", f"{nom} : famille {s.get('famille')!r}, couche {s.get('couche')!r}")
        if not essai_factice and not str(s["empreinte"]).startswith(SONDES_V3[nom]):
            raise Refus("empreinte-sonde", f"{nom} : empreinte {str(s['empreinte'])[:16]}… ≠ préfixe de la règle v3 "
                        f"{SONDES_V3[nom]}")
        if nom not in sondes_npz:
            raise Refus("sonde-introuvable", f"{nom} absente du fichier de poids")
        n = sondes_npz[nom]
        if n["classe"] != "SondeLineaireJetons" or n["empreinte"] != s["empreinte"] or int(n["couche"]) != int(s["couche"]):
            raise Refus("empreinte-sonde", f"{nom} : le fichier de poids ne porte pas la sonde de sondes-figees.json")
        if "w" not in n["tableaux"]:
            raise Refus("sondes-npz-illisible", f"{nom} : pas de direction w")
        sortie.append({"concept": m.group(1), **s})
    return sortie


def planchers_v3(fig: dict, sondes_npz: dict, meta_npz: dict) -> dict[str, np.ndarray]:
    """Les planchers de chaque concept : exactement 200, tous à la couche 15 ; rend {concept: W [d, 200]}."""
    meta_pl = meta_npz.get("planchers")
    if not isinstance(meta_pl, dict) or set(meta_pl) != set(PRINCIPALES_V3):
        raise Refus("planchers-insuffisants", f"planchers du fichier de poids par concept attendus pour "
                    f"{sorted(PRINCIPALES_V3)} ; trouvés : {sorted(meta_pl) if isinstance(meta_pl, dict) else meta_pl!r}")
    json_pl = {s["nom"]: s for s in fig["resultat"]["sondes"] if s.get("famille") == "plancher"}
    meta_noms = [n for v in meta_pl.values() if isinstance(v, list) for n in v]
    if set(json_pl) != set(meta_noms):
        raise Refus("planchers-discordants", f"planchers de sondes-figees.json ({len(json_pl)}) ≠ planchers du fichier de "
                    f"poids ({len(set(meta_noms))}) ; écart : {sorted(set(json_pl) ^ set(meta_noms))[:6]}")
    sortie = {}
    for concept in sorted(PRINCIPALES_V3):
        noms = meta_pl[concept]
        if not isinstance(noms, list) or len(noms) != N_PLANCHERS or len(set(noms)) != len(noms):
            n = len(set(noms)) if isinstance(noms, list) else 0
            raise Refus("planchers-insuffisants", f"{concept} : {n} planchers distincts, la règle v3 en exige exactement "
                        f"{N_PLANCHERS}")
        W = []
        for n in noms:
            s = sondes_npz.get(n)
            if s is None or n not in json_pl:
                raise Refus("plancher-introuvable", f"{concept} : plancher {n} absent du fichier de poids ou de "
                            "sondes-figees.json")
            if (s["classe"] != "SondeLineaireJetons" or s["famille"] != "plancher"
                    or json_pl[n]["empreinte"] != s["empreinte"]):
                raise Refus("empreinte-sonde", f"plancher {n} : classe, famille ou empreinte discordante")
            if int(s["couche"]) != COUCHE_PLANCHERS or int(json_pl[n]["couche"]) != COUCHE_PLANCHERS:
                raise Refus("planchers-hors-couche-15", f"{concept} : plancher {n} à la couche {s['couche']} ; la règle "
                            f"v3 les suppose tous à la couche {COUCHE_PLANCHERS}")
            W.append(s["tableaux"]["w"])
        sortie[concept] = np.stack(W, axis=1)
    return sortie


# --------------------------------------------------------------------------------------------------------------------
# Lentille et sa configuration

def charger_pt(chemin: Path):
    try:
        import torch
    except ImportError:
        raise Refus("torch-absent-pour-pt", "lentille .pt : torch absent de cet interpréteur") from None
    try:
        ck = torch.load(str(chemin), map_location="cpu", weights_only=True)
    except Exception as e:                                         # CLJ-05 : fichier tronqué, vide, ou pas un .pt
        raise Refus("lentille-illisible", f"{chemin} : torch.load a échoué ({type(e).__name__}: {str(e)[:160]})") from None
    if not isinstance(ck, dict) or "J" not in ck:
        cles = sorted(ck) if isinstance(ck, dict) else type(ck).__name__
        raise Refus("lentille-illisible", f"{chemin} : clé « J » absente ({cles} ; point de reprise de fit() ?)")
    return ck


def _scalaire(x):
    if hasattr(x, "item") and getattr(x, "ndim", 0) == 0:
        x = x.item()
    if hasattr(x, "tolist"):
        x = x.tolist()
    return x


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
            meta = {k: (_scalaire(z[k]) if k in z.files else None) for k in ("n_prompts", "d_model", "source_layers")}
    elif chemin.suffix == ".pt":
        ck = charger_pt(chemin)
        J = {}
        for c in couches:
            if c not in ck["J"]:
                raise Refus("couche-absente-lentille", f"{chemin} : couche {c} absente ({sorted(ck['J'])})")
            J[c] = ck["J"][c].float().numpy().astype(np.float64)
        meta = {"n_prompts": _scalaire(ck.get("n_prompts")), "d_model": _scalaire(ck.get("d_model")),
                "source_layers": _scalaire(ck.get("source_layers"))}
        del ck
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
    if " #" in v and not v.startswith(('"', "'")):
        v = v.split(" #", 1)[0].strip()
    if v in ("", "null", "~", "None"):
        return None
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d*(e-?\d+)?", v):
        return float(v)
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def lire_config_lentille(chemin: Path) -> dict:
    """YAML simple sur deux niveaux, sans bibliothèque (CLJ2-01) : « cle: valeur » au premier niveau ; un bloc
    « cle: » suivi de lignes indentées de deux espaces « sous_cle: valeur ». Les niveaux plus profonds sont ignorés
    (leur clé parente vaut {})."""
    racine: dict = {}
    bloc = None
    for l in chemin.read_text(encoding="utf-8").splitlines():
        if not l.strip() or l.lstrip().startswith("#"):
            continue
        m0 = re.match(r"^([A-Za-z_][\w.-]*)\s*:(?:\s+(.*?))?\s*$", l)
        if m0:
            v = m0.group(2)
            if v is None or v.strip() == "":
                racine[m0.group(1)] = {}
                bloc = m0.group(1)
            else:
                racine[m0.group(1)] = _valeur_yaml(v)
                bloc = None
            continue
        m1 = re.match(r"^  ([A-Za-z_][\w.-]*)\s*:(?:\s+(.*?))?\s*$", l)
        if m1 and bloc is not None and isinstance(racine.get(bloc), dict):
            v = m1.group(2)
            racine[bloc][m1.group(1)] = {} if v is None or v.strip() == "" else _valeur_yaml(v)
    return racine


def nombre_de_textes(config: dict | None) -> tuple[int | None, str]:
    """CLJ2-01 : results.prompts_fitted seulement (jamais fit.n_prompts, qui est le nombre demandé)."""
    if config is None:
        return None, "inconnu (option --lentille-config absente)"
    r = config.get("results")
    if isinstance(r, dict) and isinstance(r.get("prompts_fitted"), int) and not isinstance(r["prompts_fitted"], bool):
        return r["prompts_fitted"], f"ajustée sur {r['prompts_fitted']} textes (lentille-config.yaml, clé results.prompts_fitted)"
    return None, "inconnu (pas de clé results.prompts_fitted entière dans lentille-config.yaml)"


# --------------------------------------------------------------------------------------------------------------------
# Poids : npy, npz, safetensors (lu en numpy, sans la bibliothèque safetensors) — inchangé depuis la v2

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
    if p.suffix == ".json":
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
# Vocabulaire et concepts — inchangé depuis la v2 (sauf contrôle des noms de concepts)

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
        raise Refus("mot-sans-jeton", f"mots sans jeton de début de mot dans le vocabulaire : {sans}")
    return sortie


# --------------------------------------------------------------------------------------------------------------------
# Désembedding — inchangé depuis la v2, plus le noyau des têtes nulles restreint aux jetons de début de mot (U1)

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


def tetes_debut_lot(WU_debut: np.ndarray, idx_debut: np.ndarray, Y: np.ndarray, k: int) -> np.ndarray:
    """Indices (dans le vocabulaire) des k jetons de tête parmi les jetons de début de mot, pour chaque colonne de
    Y [d, n] ; forme [k, n]. WU_debut = W_U restreint aux lignes de début de mot (float32). Sert aux nulles."""
    sortie = np.empty((k, Y.shape[1]), dtype=np.int64)
    for a in range(0, Y.shape[1], LOT_TETES):
        L = WU_debut @ np.ascontiguousarray(Y[:, a:a + LOT_TETES], dtype=np.float32)
        if not np.all(np.isfinite(L)):
            raise Refus("incoherence-interne", "logits non finis dans une distribution nulle")
        part = np.argpartition(-L, k - 1, axis=0)[:k]
        sortie[:, a:a + LOT_TETES] = idx_debut[part]
    return sortie


# --------------------------------------------------------------------------------------------------------------------
# Lentilles appliquées à des directions — inchangé depuis la v2

def rms(x, axis=0, eps=0.0):
    return np.sqrt(np.mean(x * x, axis=axis, keepdims=True) + eps)


def vers_sortie(V: np.ndarray, transport: np.ndarray | None, g: np.ndarray, variante: str, ctx: dict) -> np.ndarray:
    """Directions V [d, n] (espace de la couche) → vecteurs y [d, n] tels que logits = W_U · y.
    transport = J_l (lentille jacobienne) ou None (lentille des logits). La v3 n'emploie que « direction »."""
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


def graines(etiquette: str) -> np.random.SeedSequence:
    cle = int.from_bytes(hashlib.sha256(etiquette.encode("utf-8")).digest()[:8], "little")
    return np.random.SeedSequence(entropy=GRAINE, spawn_key=(cle,))


def resume_nulle(nuls: np.ndarray) -> dict:
    """Descriptif seulement (jamais dans un verdict)."""
    nuls = np.asarray(nuls)
    return {"n": int(nuls.size), "mediane": float(np.median(nuls)), "moyenne": round(float(nuls.mean()), 6),
            "quantile_0_99_inverted_cdf": float(np.quantile(nuls.astype(np.float64), 0.99, method="inverted_cdf")),
            "maximum": int(nuls.max()), "comptes": {str(v): int(c) for v, c in zip(*np.unique(nuls, return_counts=True))}}


# --------------------------------------------------------------------------------------------------------------------
# Provenance

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
    durees: dict[str, float] = {}
    tp = time.perf_counter()

    def etape(nom):
        nonlocal tp
        t = time.perf_counter()
        durees[nom] = round(t - tp, 3)
        tp = t

    controler_enonce()
    controler_constantes()
    if a.sondes != "non-principales-lineaires":
        raise Refus("parametre", f"mode {a.sondes!r} : la v3 n'a que « non-principales-lineaires »")
    sortie = Path(a.sortie)
    manifeste_ch = sortie.with_name(sortie.stem + "-manifeste.json")
    for p in (sortie, manifeste_ch):
        if p.exists() or Path(str(p) + ".sha256").exists():
            raise Refus("sortie-existe", f"{p} existe déjà (R12)")
    lus: dict[str, Path] = {}

    # Énoncé gelé (B4) : le fichier de la règle doit être, octet pour octet, la constante du script
    p_en = exiger(a.enonce_regle, "énoncé gelé de la règle v3")
    if p_en.read_bytes() != ENONCE_REGLE_PRIMAIRE_V3.encode("utf-8") or sha256_fichier(p_en) != EMPREINTE_ENONCE_V3:
        raise Refus("enonce-fichier-discordant", f"{p_en} ({sha256_fichier(p_en)[:12]}…) n'est pas l'énoncé de ce script "
                    f"({EMPREINTE_ENONCE_V3[:12]}…)")
    lus["enonce_regle"] = p_en

    # Liste de mots : empreinte en dur (CLJ2-05), puis sceau compagnon
    p_c = exiger(a.concepts, "liste de mots des concepts")
    sha_c = sha256_fichier(p_c)
    if sha_c != EMPREINTE_CONCEPTS_V3:
        raise Refus("empreinte-concepts", f"{p_c} : {sha_c[:12]}… ≠ liste v3 de la règle {EMPREINTE_CONCEPTS_V3[:12]}…")
    verifier_compagnon(p_c, obligatoire=True)
    lus["concepts"] = p_c
    concepts_mots = lire_concepts(p_c)
    if set(concepts_mots) != set(PRINCIPALES_V3):
        raise Refus("concepts-illisibles", f"{p_c} : concepts {sorted(concepts_mots)} ≠ {sorted(PRINCIPALES_V3)}")

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
    choix = choisir_sondes_v3(fig, sondes_npz, meta_npz, a.essai_factice)
    pl_par_concept = planchers_v3(fig, sondes_npz, meta_npz)
    couches = sorted({int(c["couche"]) for c in choix})
    if couches != [7, 15, 23]:
        raise Refus("sondes-inattendues", f"couches {couches} ≠ [7, 15, 23]")
    etape("lecture_sondes")

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
    n_lent = meta_lent.get("n_prompts")
    if n_textes is not None and isinstance(n_lent, int) and not isinstance(n_lent, bool) and n_lent != n_textes:
        raise Refus("lentille-config-discordante", f"lentille n_prompts = {n_lent} ≠ results.prompts_fitted = {n_textes} "
                    "dans lentille-config.yaml : la configuration n'est pas celle de ce fichier de lentille")
    etape("lecture_lentille")
    WU, f_wu = lire_tableau(a.desembedding, "désembedding")
    g, f_g = lire_tableau(a.norme_finale, "normalisation finale")
    for i, f in enumerate(f_wu):
        lus[f"desembedding_{i}"] = f
    for i, f in enumerate(f_g):
        lus[f"norme_finale_{i}"] = f
    g = g.astype(np.float64).reshape(-1)
    if WU.ndim != 2:
        raise Refus("dimension", f"désembedding de forme {WU.shape} : [vocabulaire, largeur] attendu")
    if not (np.all(np.isfinite(WU)) and np.all(np.isfinite(g))):
        raise Refus("poids-non-finis", "désembedding ou normalisation finale non finis")
    Vt, d = WU.shape
    tailles = {"désembedding (colonnes)": d, "normalisation finale": g.size,
               **{f"J_{c}": J[c].shape[0] for c in couches},
               **{c["nom"]: sondes_npz[c["nom"]]["tableaux"]["w"].size for c in choix},
               **{f"planchers {k}": v.shape[0] for k, v in pl_par_concept.items()}}
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
    etape("lecture_poids_vocabulaire")

    # Empreintes attendues (CLJ-04) : contrôle avant tout calcul
    controle_empreintes = "non contrôlées (option --empreintes-attendues absente)"
    if a.empreintes_attendues:
        p_att = exiger(a.empreintes_attendues, "fichier d'empreintes attendues")
        attendues = lire_empreintes_attendues(p_att)
        exemptes = {"sondes_json": "sceau compagnon", "sondes_npz": source,
                    "concepts": f"empreinte en dur {EMPREINTE_CONCEPTS_V3[:12]}… et sceau compagnon",
                    "enonce_regle": f"empreinte en dur {EMPREINTE_ENONCE_V3[:12]}… et égalité avec la constante du script"}
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
    etape("controle_empreintes")

    # Les 32 cases : directions décodables ? (sinon : aucune sortie, aucun verdict)
    Y_case: dict[tuple, np.ndarray] = {}
    manquantes = []
    for c in choix:
        w = sondes_npz[c["nom"]]["tableaux"]["w"].reshape(-1)
        L = int(c["couche"])
        for lentille in LENTILLES:
            T = None if lentille == "logits" else J[L]
            v = w if T is None else T @ w
            if not np.all(np.isfinite(v)) or not np.any(v != 0):
                manquantes.append(f"{c['nom']}/{lentille} (direction {'w' if T is None else 'J·w'} nulle ou non finie)")
                continue
            y = vers_sortie(w[:, None], T, g, "direction", {})[:, 0]
            if not np.all(np.isfinite(y)):
                manquantes.append(f"{c['nom']}/{lentille} (vecteur de sortie non fini)")
                continue
            Y_case[(c["nom"], lentille)] = y
    if manquantes or len(Y_case) != M_TESTS:
        raise Refus("cases-manquantes", f"{len(Y_case)} cases sur {M_TESTS} ; manquantes : {manquantes} — la règle v3 "
                    "exige les 32 cases : aucun verdict")
    for concept, W in pl_par_concept.items():
        if not np.all(np.isfinite(W)) or np.any(np.linalg.norm(W, axis=0) == 0):
            raise Refus("planchers-insuffisants", f"{concept} : plancher nul ou non fini")
    etape("cases")

    de = Desembedding(WU)
    WU_debut = np.ascontiguousarray(WU[idx_debut])
    ids_concept = {n: np.array([j["id"] for j in info["jetons"]], dtype=np.int64) for n, info in concepts.items()}
    etape("desembedding")

    # Nulle isotrope (B2) : 10 000 directions par couche, mêmes directions pour les deux lentilles
    graines_man, tetes_iso, Y_iso_z = {}, {}, {}
    for L in couches:
        et = ETIQUETTE_ISOTROPES.format(couche=L)
        ss = graines(et)
        graines_man[et] = {"entropie": str(ss.entropy), "spawn_key": [str(x) for x in ss.spawn_key]}
        rng = np.random.default_rng(ss)
        for lentille in LENTILLES:
            tetes_iso[(L, lentille)] = np.empty((K_TETE, N_ISOTROPES), dtype=np.int64)
        for a0 in range(0, N_ISOTROPES, BLOC_ISOTROPES):
            V = rng.standard_normal((BLOC_ISOTROPES, d)).T                       # direction i = ligne i
            for lentille in LENTILLES:
                T = None if lentille == "logits" else J[L]
                Y = vers_sortie(V, T, g, "direction", {})
                tetes_iso[(L, lentille)][:, a0:a0 + BLOC_ISOTROPES] = tetes_debut_lot(WU_debut, idx_debut, Y, K_TETE)
                if a0 == 0:
                    Y_iso_z[(L, lentille)] = Y[:, :N_ISO_Z].copy()
    stats_iso = {(L, lent, n): np.isin(tetes_iso[(L, lent)], ids).sum(axis=0)
                 for (L, lent) in tetes_iso for n, ids in ids_concept.items()}
    etape("nulle_isotrope")

    # Nulle des planchers (couche 15) : les 200 planchers du concept, par la même lentille
    stats_pl, Y_pl = {}, {}
    for concept, W in pl_par_concept.items():
        for lentille in LENTILLES:
            T = None if lentille == "logits" else J[COUCHE_PLANCHERS]
            Y = vers_sortie(W, T, g, "direction", {})
            if not np.all(np.isfinite(Y)):
                raise Refus("planchers-insuffisants", f"{concept}/{lentille} : planchers non décodables")
            Y_pl[(concept, lentille)] = Y
            t_pl = tetes_debut_lot(WU_debut, idx_debut, Y, K_TETE)
            stats_pl[(concept, lentille)] = np.isin(t_pl, ids_concept[concept]).sum(axis=0)
            if stats_pl[(concept, lentille)].size != N_PLANCHERS:
                raise Refus("incoherence-interne", "nombre de planchers décodés")
    etape("nulle_planchers")

    # Cases de la règle, puis descriptif par sonde
    cbar = {n: WU[ids].astype(np.float64).mean(axis=0) for n, ids in ids_concept.items()}
    cache_z: dict[tuple, np.ndarray] = {}

    def z_nuls(cle, Y, n_c):
        if (cle, n_c) not in cache_z:
            cache_z[(cle, n_c)] = de.z_lot(Y, cbar[n_c])
        return cache_z[(cle, n_c)]

    cases, resultats = {}, []
    set_ids = {n: set(ids.tolist()) for n, ids in ids_concept.items()}
    for c in choix:
        nom, L, concept = c["nom"], int(c["couche"]), c["concept"]
        s = sondes_npz[nom]
        w = s["tableaux"]["w"].reshape(-1)
        Jw = J[L] @ w
        entree = {"nom": nom, "concept": concept, "famille": c["famille"], "couche": L, "classe": c["classe"],
                  "agregation": c["agregation"], "empreinte": c["empreinte"], "biais_b": s["b"],
                  "norme_w": float(np.linalg.norm(w)), "norme_Jw_sur_norme_w": float(np.linalg.norm(Jw) / np.linalg.norm(w)),
                  "cosinus_w_Jw": float(w @ Jw / (np.linalg.norm(w) * np.linalg.norm(Jw))), "lentilles": {}}
        logits_par_lentille = {}
        for lentille in LENTILLES:
            y = Y_case[(nom, lentille)]
            lg = de.logits(y)
            if not np.all(np.isfinite(lg)):
                raise Refus("cases-manquantes", f"{nom}/{lentille} : logits non finis — aucun verdict")
            logits_par_lentille[lentille] = lg
            r = {"plus": {"tete": tete(lg, textes, K_TETE), "tete_mots": tete(lg, textes, K_TETE, mots),
                          "tete_debut_de_mot": tete(lg, textes, K_TETE, debut)},
                 "moins": {"tete": tete(-lg, textes, K_TETE), "tete_mots": tete(-lg, textes, K_TETE, mots),
                           "tete_debut_de_mot": tete(-lg, textes, K_TETE, debut)}}
            ids_plus = [t["id"] for t in r["plus"]["tete_debut_de_mot"]]
            ids_moins = [t["id"] for t in r["moins"]["tete_debut_de_mot"]]
            if len(ids_plus) != K_TETE or len(set(ids_plus)) != K_TETE or not all(debut[i] for i in ids_plus):
                raise Refus("incoherence-interne", f"{nom}/{lentille} : tête de début de mot mal formée")
            comptes = {n: sum(i in set_ids[n] for i in ids_plus) for n in ids_concept}
            S = comptes[concept]
            jetons_S = [textes[i] for i in ids_plus if i in set_ids[concept]]
            mots_S = sorted({t[1:].lower() for t in jetons_S})
            nul = stats_iso[(L, lentille, concept)]
            n_iso = int(np.count_nonzero(nul >= S))
            n_iso_200 = int(np.count_nonzero(nul[:N_ISO_SEUIL_V2] >= S))
            n_pl = int(np.count_nonzero(stats_pl[(concept, lentille)] >= S)) if L == COUCHE_PLANCHERS else None
            verdict = verdict_v3(S, n_iso, n_pl, L)
            case = {"sonde": nom, "concept": concept, "famille": c["famille"], "couche": L, "lentille": lentille,
                    "S": S, "n_iso": n_iso, "p_rang": f"{1 + n_iso}/{N_ISOTROPES + 1}",
                    "p_rang_valeur": float(Fraction(1 + n_iso, N_ISOTROPES + 1)), "n_pl": n_pl,
                    "nulles": "isotropes et planchers" if L == COUCHE_PLANCHERS else "isotropes seules",
                    "verdict": verdict}
            cases[(nom, lentille)] = case
            # Descriptif de la case (jamais critère)
            seuil_v2 = (S >= S_MIN and n_iso_200 <= N_SEUIL_V2_MAX
                        and (L != COUCHE_PLANCHERS or n_pl <= N_SEUIL_V2_MAX))
            r["descriptif_regle"] = {
                "statut": "descriptif, ne sert pas de critère",
                "S_jetons": S, "S_mots_distincts": len(mots_S), "jetons_du_concept_en_tete": jetons_S,
                "mots_du_concept_en_tete": mots_S, "comptes_par_concept_plus": comptes,
                "comptes_par_concept_moins": {n: sum(i in set_ids[n] for i in ids_moins) for n in ids_concept},
                "n_iso_200_premieres": n_iso_200,
                "verdict_seuil_v2_non_corrige": "cohérent" if seuil_v2 else "non cohérent",
                "verdict_sans_planchers": (("cohérent" if S >= S_MIN and n_iso <= N_ISO_MAX else "non cohérent")
                                           if L == COUCHE_PLANCHERS else "sans objet (pas de planchers à cette couche)"),
                "planchers_quantile_0_99_troisieme_plus_grand_de_200": (
                    float(np.quantile(stats_pl[(concept, lentille)].astype(np.float64), 0.99, method="inverted_cdf"))
                    if L == COUCHE_PLANCHERS else None)}
            # Diagnostics z (descriptifs) : 200 premières isotropes, planchers à la couche 15
            diag = {}
            rangs = np.empty(Vt, dtype=np.int64)
            rangs[np.argsort(-lg, kind="stable")] = np.arange(1, Vt + 1)
            tete_p = {t["id"] for t in r["plus"]["tete"]}
            tete_m = {t["id"] for t in r["moins"]["tete"]}
            for n_c, ids in ids_concept.items():
                z = float(de.z_lot(y[:, None], cbar[n_c])[0])
                z_direct = float((lg[ids].mean() - lg.mean()) / lg.std())
                if not np.isclose(z, z_direct, rtol=1e-4, atol=1e-4):      # logits en simple précision
                    raise Refus("incoherence-interne", f"score z par Gram {z} ≠ direct {z_direct}")
                item = {"z": z, "jetons_concept": int(ids.size),
                        "n_concept_tete_plus": len(tete_p & set_ids[n_c]),
                        "n_concept_tete_moins": len(tete_m & set_ids[n_c]),
                        "meilleur_rang_plus": int(rangs[ids].min()),
                        "meilleur_rang_moins": int((Vt + 1 - rangs[ids]).min())}
                zn = z_nuls(("iso", L, lentille), Y_iso_z[(L, lentille)], n_c)
                item["isotropes_200_premieres"] = {
                    "n": int(zn.size), "p_haut": p_haut(z, zn), "p_bas": p_haut(-z, -zn),
                    "p_bilateral": p_haut(abs(z), np.abs(zn)),
                    "z_quantiles_5_50_95": [float(q) for q in np.quantile(zn, [0.05, 0.5, 0.95])]}
                if L == COUCHE_PLANCHERS:
                    zp = z_nuls(("pl", concept, lentille), Y_pl[(concept, lentille)], n_c)
                    item["planchers"] = {"n": int(zp.size), "p_haut": p_haut(z, zp), "p_bas": p_haut(-z, -zp),
                                         "p_bilateral": p_haut(abs(z), np.abs(zp)),
                                         "z_quantiles_5_50_95": [float(q) for q in np.quantile(zp, [0.05, 0.5, 0.95])]}
                else:
                    item["planchers"] = {"statut": "pas de plancher à cette couche"}
                diag[n_c] = item
            r["diagnostics_z"] = diag
            entree["lentilles"][lentille] = r
        a_, b_ = logits_par_lentille["logits"], logits_par_lentille["jacobienne"]
        ac, bc = a_ - a_.mean(), b_ - b_.mean()
        bl = entree["lentilles"]
        entree["recouvrement"] = {
            "plus": recouvrement(bl["logits"]["plus"]["tete"], bl["jacobienne"]["plus"]["tete"]),
            "moins": recouvrement(bl["logits"]["moins"]["tete"], bl["jacobienne"]["moins"]["tete"]),
            "plus_debut_de_mot": recouvrement(bl["logits"]["plus"]["tete_debut_de_mot"],
                                              bl["jacobienne"]["plus"]["tete_debut_de_mot"]),
            "cosinus_logits_centres": float(ac @ bc / (np.linalg.norm(ac) * np.linalg.norm(bc)))}
        resultats.append(entree)
    etape("cases_et_descriptif")

    # Les 32 cases exigées ; ensemble des sondes = les 16 de la règle
    attendues = {(n, l) for n in SONDES_V3 for l in LENTILLES}
    if set(cases) != attendues or len(cases) != M_TESTS:
        raise Refus("cases-manquantes", f"manquantes : {sorted(attendues - set(cases))} — aucun verdict")
    complete = True

    # Verdict d'ensemble par lentille (B5)
    coherentes = {l: [n for n in SONDES_V3 if cases[(n, l)]["verdict"] == "cohérent"] for l in LENTILLES}
    borne = borne_familiale()
    ensemble = {l: {"X": len(coherentes[l]), "sur": len(SONDES_V3), "niveau": niveau(len(coherentes[l])),
                    "sondes_coherentes": coherentes[l]} for l in LENTILLES}
    ensemble["borne_erreur_familiale_nulle_isotrope"] = {
        "expression": f"{M_TESTS} × {N_ISO_MAX + 1}/{N_ISOTROPES + 1}", "fraction": f"{borne.numerator}/{borne.denominator}",
        "valeur": float(borne), "lecture": "probabilité d'au moins un « cohérent » à tort parmi les 32 tests, sous la "
        "nulle isotrope globale, quelle que soit la dépendance entre tests (Bonferroni)"}

    # Comparaison des lentilles (B5)
    grille = {}
    for n in SONDES_V3:
        jj, ll = cases[(n, "jacobienne")]["verdict"] == "cohérent", cases[(n, "logits")]["verdict"] == "cohérent"
        grille[n] = "les deux" if jj and ll else "jacobienne seule" if jj else "logits seuls" if ll else "aucune"
    b = sum(v == "jacobienne seule" for v in grille.values())
    c_ = sum(v == "logits seuls" for v in grille.values())
    p_signe = test_signe_bilateral(b, c_)
    permise = p_signe <= ALPHA_SIGNE
    phrase = None
    if permise:
        phrase = ("la lentille jacobienne verbalise plus de sondes que la lentille des logits" if b > c_
                  else "la lentille des logits verbalise plus de sondes que la lentille jacobienne")
    comparaison = {"grille": grille, "b_jacobienne_seule": b, "c_logits_seuls": c_,
                   "les_deux": sum(v == "les deux" for v in grille.values()),
                   "aucune": sum(v == "aucune" for v in grille.values()),
                   "test_du_signe_exact_bilateral": {"n": b + c_, "p": f"{p_signe.numerator}/{p_signe.denominator}",
                                                     "p_valeur": float(p_signe),
                                                     "definition": "min(1, 2 · P(Bin(b + c, 1/2) ≤ min(b, c))), p = 1 si b + c = 0"},
                   "formulation_permise": bool(permise), "phrase": phrase,
                   "reserve": "les sondes ne sont pas indépendantes (même concept, même famille à trois couches) : ce "
                              "test est une règle de formulation, pas une garantie d'inférence"}

    # Descriptif : strates, nulles, déclencheurs d'audit (règle v3, sections 4 et 5)
    def compter(pred):
        return {l: sum(1 for n in SONDES_V3 if pred(n, l)) for l in LENTILLES}

    par_n = {x["nom"]: x for x in resultats}
    desc = lambda n, l: par_n[n]["lentilles"][l]["descriptif_regle"]      # noqa: E731
    strates = {
        "statut": "descriptif, ne sert pas de critère",
        "par_couche": {str(L): compter(lambda n, l, L=L: cases[(n, l)]["couche"] == L
                                       and cases[(n, l)]["verdict"] == "cohérent") for L in couches},
        "par_concept": {k: compter(lambda n, l, k=k: cases[(n, l)]["concept"] == k and cases[(n, l)]["verdict"] == "cohérent")
                        for k in sorted(PRINCIPALES_V3)},
        "par_famille": {f: compter(lambda n, l, f=f: cases[(n, l)]["famille"] == f and cases[(n, l)]["verdict"] == "cohérent")
                        for f in sorted({x["famille"] for x in choix})},
        "couche_15_avec_planchers": compter(lambda n, l: cases[(n, l)]["couche"] == COUCHE_PLANCHERS
                                            and cases[(n, l)]["verdict"] == "cohérent"),
        "couche_15_sans_planchers": compter(lambda n, l: cases[(n, l)]["couche"] == COUCHE_PLANCHERS
                                            and desc(n, l)["verdict_sans_planchers"] == "cohérent"),
        "X_au_seuil_v2_non_corrige": compter(lambda n, l: desc(n, l)["verdict_seuil_v2_non_corrige"] == "cohérent"),
        "S_jetons_et_mots_distincts": {f"{n}/{l}": [cases[(n, l)]["S"], desc(n, l)["S_mots_distincts"]]
                                       for n in SONDES_V3 for l in LENTILLES}}
    nulles = {"statut": "descriptif, ne sert pas de critère",
              "isotropes": {f"c{L}/{l}/{k}": resume_nulle(stats_iso[(L, l, k)])
                            for L in couches for l in LENTILLES for k in sorted(ids_concept)},
              "planchers_couche_15": {f"{k}/{l}": {**resume_nulle(stats_pl[(k, l)]),
                                                   "libelle_quantile": "troisième plus grand de 200"}
                                      for k in sorted(pl_par_concept) for l in LENTILLES}}
    declenches = []
    for l in LENTILLES:
        if ensemble[l]["X"] >= 12:
            declenches.append(f"lentille {l} : X = {ensemble[l]['X']} ≥ 12")
    if all(ensemble[l]["X"] == 0 for l in LENTILLES):
        declenches.append("les deux lentilles ont X = 0")
    if b >= 6 and c_ == 0:
        declenches.append(f"b = {b} ≥ 6 avec c = 0")
    if c_ >= 6 and b == 0:
        declenches.append(f"c = {c_} ≥ 6 avec b = 0")
    for (n, l), cs in sorted(cases.items()):
        if cs["S"] >= 10:
            declenches.append(f"{n}/{l} : S = {cs['S']} ≥ 10")
    for L in couches:
        for l in LENTILLES:
            for k in sorted(ids_concept):
                med = float(np.median(stats_iso[(L, l, k)]))
                if med >= 1:
                    declenches.append(f"nulle isotrope c{L}/{l} pour {k} : médiane {med:g} ≥ 1")
    for (n, l), cs in sorted(cases.items()):
        if cs["verdict"] == "cohérent":
            m_ = desc(n, l)["mots_du_concept_en_tete"]
            if len(m_) == 1:
                declenches.append(f"{n}/{l} cohérent : tous les jetons du concept viennent du seul mot {m_[0]!r}")
            elif set(m_) <= set(MOTS_LARGES):
                declenches.append(f"{n}/{l} cohérent : tous les jetons du concept viennent des mots larges {m_}")
    audit = {"declenches": declenches, "lecture": "l'audit ne change aucun verdict ; il ajoute une réserve (règle v3, "
             "section 5) : lire les têtes de début de mot des cas en cause, les comptes des nulles, et les mêmes cas "
             "sous l'autre concept"}
    etape("ensemble")

    statut = ("exploratoire, non opposable ; seules les 32 cases de la règle primaire v3 portent un verdict, puis le "
              "verdict d'ensemble par lentille et la règle de formulation de la comparaison ; tout le reste est descriptif")
    if a.essai_factice:
        statut = ("ESSAI FACTICE : run et empreintes des 16 sondes non contrôlés (--essai-factice) ; aucun verdict de "
                  "cette sortie ne vaut pour la règle v3. " + statut)
    corps = {
        "version": VERSION, "essai_factice": bool(a.essai_factice), "statut": statut,
        "regle_primaire": {
            "enonce": ENONCE_REGLE_PRIMAIRE_V3, "empreinte_enonce": sha256_texte(ENONCE_REGLE_PRIMAIRE_V3),
            "empreinte_enonce_attendue": EMPREINTE_ENONCE_V3,
            "liste_de_mots": {"fichier": p_c.name, "sha256": sha_c, "attendue": EMPREINTE_CONCEPTS_V3},
            "parametres": {"k": K_TETE, "n_isotropes": N_ISOTROPES, "graine": GRAINE,
                           "etiquette_isotropes": ETIQUETTE_ISOTROPES, "n_planchers": N_PLANCHERS,
                           "couche_planchers": COUCHE_PLANCHERS, "S_min": S_MIN, "m_tests": M_TESTS,
                           "alpha": str(ALPHA), "n_iso_max": N_ISO_MAX, "n_pl_max": N_PL_MAX,
                           "alpha_test_du_signe": str(ALPHA_SIGNE), "sens": "+w seulement",
                           "variante": "direction"},
            "sondes_lues": list(SONDES_V3), "principales_exclues_non_decodees": sorted(PRINCIPALES_V3.values()),
            "complete": complete,
            "cases": [cases[(n, l)] for n in SONDES_V3 for l in LENTILLES],
            "verdict_ensemble": ensemble, "comparaison": comparaison},
        "descriptif": {"strates": strates, "nulles": nulles, "declencheurs_audit": audit},
        "convention_couche": "couche ℓ de P3 = clé ℓ de la lentille (sortie du bloc décodeur ℓ, indice à partir de 0) ; "
                             "contre-lecture v2, CLJ-01 levée",
        "lecture_des_signes": "plus = direction +w (vers la classe 1 : consigne malhonnête pour « tromperie », "
                              "« high-stakes » pour « enjeux ») ; moins = −w, descriptif",
        "run_sondes": fig.get("run_id"), "lentille_meta": meta_lent, "lentille_ajustee_sur": ajustee_sur,
        "largeur": d,
        "vocabulaire": {"taille_desembedding": Vt, **info_voc, "jetons_mots": int(mots.sum()),
                        "jetons_debut_de_mot": int(debut.sum())},
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
    durees["ecriture_sortie"] = round(time.perf_counter() - tp, 3)
    manifeste = {
        "script": ici.name, "script_sha256": sha256_fichier(ici), "version": VERSION,
        "essai_factice": bool(a.essai_factice),
        "interpreteur": sys.executable, "commande": [sys.executable, *sys.argv],
        "drapeaux_python": {"isolated": sys.flags.isolated, "dont_write_bytecode": sys.flags.dont_write_bytecode},
        "cree_le_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "duree_s": round(time.time() - t0, 2),
        "durees_par_etape_s": durees,
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "torch": v_torch,
                     "plateforme": platform.platform()},
        "depot": provenance,
        "revision_modele": a.revision_modele or "inconnue (option --revision-modele absente)",
        "lentille_config": ({"chemin": str(lus["lentille_config"]), "sha256": sha256_fichier(lus["lentille_config"]),
                             "cles": config, "ajustee_sur": ajustee_sur} if config is not None
                            else "absente (option --lentille-config absente)"),
        "empreintes_attendues": controle_empreintes,
        "regle_primaire_v3": {"empreinte_enonce": sha256_texte(ENONCE_REGLE_PRIMAIRE_V3),
                              "empreinte_liste_de_mots": sha_c},
        "entrees": {k: {"chemin": str(p), "sha256": sha256_fichier(p), "octets": p.stat().st_size} for k, p in lus.items()},
        "graines": {"mode": "numpy.random.SeedSequence(entropy=20261029, spawn_key=(int.from_bytes(sha256(etiquette)"
                            "[:8], 'little'),)) ; default_rng ; standard_normal((1000, d)) dix fois de suite ; "
                            "direction i = ligne i", **graines_man},
        "sortie": {"chemin": sortie.name, "sha256": sha_sortie},
    }
    ecrire_scelle(manifeste_ch, json.dumps(manifeste, ensure_ascii=False, indent=1, default=str) + "\n")
    print(f"sortie : {sortie} ({sha_sortie[:12]}…) ; manifeste : {manifeste_ch} ; {len(resultats)} sondes, "
          f"{len(cases)} cases ; durée {manifeste['duree_s']} s")
    return 0


# --------------------------------------------------------------------------------------------------------------------
# Vérifier la liste de mots contre le vocabulaire seul (ne lit ni sonde, ni lentille, ni résultat)

def verifier_concepts(a) -> int:
    controler_enonce()
    p_c = exiger(a.concepts, "liste de mots des concepts")
    verifier_compagnon(p_c, obligatoire=True)
    sha_c = sha256_fichier(p_c)
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
          f"({sha_c[:12]}…, {'liste v3 de la règle' if sha_c == EMPREINTE_CONCEPTS_V3 else 'PAS la liste v3 de la règle'})\n"
          + "\n".join(lignes))
    if sans:
        raise Refus("mot-sans-jeton", f"mots sans jeton de début de mot : {sans}")
    print("tous les mots ont au moins un jeton de début de mot")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sp = ap.add_subparsers(dest="commande", required=True)
    c = sp.add_parser("comparer")
    c.add_argument("--sondes", required=True, choices=("non-principales-lineaires",))
    c.add_argument("--sondes-json", required=True)
    c.add_argument("--sondes-npz", required=True)
    c.add_argument("--sha256-sondes-npz", default=None, help="empreinte attendue (défaut : celle de sondes-figees.json)")
    c.add_argument("--lentille", required=True)
    c.add_argument("--lentille-config", default=None, help="lentille-config.yaml (empreinte, nombre de textes)")
    c.add_argument("--desembedding", required=True)
    c.add_argument("--norme-finale", required=True)
    c.add_argument("--vocabulaire", required=True)
    c.add_argument("--concepts", required=True, help="concepts-sondes-p3-v3.json (empreinte contrôlée en dur)")
    c.add_argument("--enonce-regle", required=True, help="enonce-regle-primaire-v3.txt (égal à la constante du script)")
    c.add_argument("--empreintes-attendues", default=None, help="fichier au format sha256sum (CLJ-04)")
    c.add_argument("--revision-modele", default=None, help="révision des poids du modèle (consignée au manifeste)")
    c.add_argument("--commit", default=None, help="commit du dépôt (défaut : git rev-parse HEAD du dossier du script)")
    c.add_argument("--essai-factice", action="store_true",
                   help="entrées synthétiques seulement : lève le contrôle du run et des empreintes des 16 sondes")
    c.add_argument("--sortie", required=True)
    k = sp.add_parser("verifier-concepts")
    k.add_argument("--vocabulaire", required=True)
    k.add_argument("--concepts", required=True)
    a = ap.parse_args(argv)
    try:
        return {"comparer": comparer, "verifier-concepts": verifier_concepts}[a.commande](a)
    except Refus as e:
        print(f"REFUS {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
