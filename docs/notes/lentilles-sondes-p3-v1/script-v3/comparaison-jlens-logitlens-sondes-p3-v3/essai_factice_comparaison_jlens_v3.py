"""Essai de bout en bout, sur entrées synthétiques, de `comparaison_jlens_logitlens_sondes_p3_v3.py` — v3.

Aucun poids réel, aucune sortie réelle, aucune lecture de `donnees/`. Largeur 128, vocabulaire de 8 000 jetons, couches
7, 15 et 23, 200 planchers par concept à la couche 15 (comme P3), liste de mots v3 réelle (`concepts-sondes-p3-v3.json`,
contrôlée en dur par le script) et énoncé gelé réel (`enonce-regle-primaire-v3.txt`).

Le fichier de poids des sondes est écrit **par le code du dépôt** (`ecrire_sondes` de `premier_test_ia/figees.py`, classes
de `sondes/familles.py`, extraites par l'arbre syntaxique, sans torch) et relu par `lire_sondes` du dépôt.

Jeux d'entrées (mêmes noms de sondes que P3 : 5 familles × 3 couches × 2 concepts, principales
`tromperie-difference_moyennes-c15` et `enjeux-lineaire-c15`) :
- A, sain : cinq sondes non principales cohérentes par construction (direction alignée sur les jetons du concept,
  soit dans l'espace de sortie, soit à travers J⁻¹), à chaque couche, sous l'une ou l'autre lentille ; à la couche 15,
  planchers de « tromperie » concentrés sur la direction du concept (les planchers doivent rendre « non cohérent » un
  cas que les isotropes seules diraient « cohérent ») ;
- B, nul : toutes les directions aléatoires ;
- C, majoritaire : dix sondes plantées sous J seulement (b = 10, c = 0 : formulation permise) ;
- jeux de refus : principale sélectionnée, 15 sondes, 17 sondes, 199 et 201 planchers, direction nulle (cases
  manquantes), run réel simulé (empreintes des sondes contrôlées en dur).
Puis : recalcul indépendant des 32 cases (S, n_iso, n_pl) du jeu A, en double précision, par un code qui ne reprend
pas celui du script ; tests unitaires des bornes (n_iso 14/15, n_pl 2/3, S 1/2), du test du signe et des niveaux ;
mesure du temps et banc du noyau aux dimensions réelles (55 449 jetons de début de mot × 4 096), avec extrapolation.

Usage : python3 -I -B essai_factice_comparaison_jlens_v3.py --dossier <dossier neuf> [--depot <racine>] [--sans-banc]
Graines : numpy.random.SeedSequence(20261029) dérivée par étiquette (R9).
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import inspect
import json
import platform
import re
import struct
import subprocess
import sys
import time
import types
from dataclasses import dataclass, field  # noqa: F401  (espace de noms des classes extraites)
from fractions import Fraction
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "comparaison_jlens_logitlens_sondes_p3_v3.py"
REGLE = ICI.parents[1] / "regle-primaire-v3"
CONCEPTS = REGLE / "concepts-sondes-p3-v3.json"
ENONCE = REGLE / "enonce-regle-primaire-v3.txt"
CONCEPTS_V2 = ICI.parents[1] / "script-v2/comparaison-jlens-logitlens-sondes-p3-v2/concepts-sondes-p3-v2.json"
D, V = 128, 8000
GRAINE = 20261029
N_PLANCHERS = 200
RUN_REEL = "20261019-230011-p3-reel"
PRINC = {"tromperie": "tromperie-difference_moyennes-c15", "enjeux": "enjeux-lineaire-c15"}
FAMILLES = ["difference_moyennes", "lineaire", "perceptron", "attention", "mahalanobis"]


def rng(etiquette):
    cle = int.from_bytes(hashlib.sha256(etiquette.encode()).digest()[:8], "little")
    return np.random.default_rng(np.random.SeedSequence(entropy=GRAINE, spawn_key=(cle,)))


def sceller_simple(chemin: Path) -> str:
    sha = hashlib.sha256(chemin.read_bytes()).hexdigest()
    Path(str(chemin) + ".sha256").write_text(f"{sha}  {chemin.name}\n", encoding="utf-8")
    return sha


# ---------------------------------------------------------------- code du dépôt, extrait sans torch (comme la v2)
class GardeArret(Exception):
    pass


def extraire(chemin: Path, noms: set[str], espace: dict) -> None:
    arbre = ast.parse(chemin.read_text(encoding="utf-8"))
    garde = [n for n in arbre.body if (isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in noms)
             or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) in noms for t in n.targets))]
    manquants = noms - {getattr(n, "name", None) or n.targets[0].id for n in garde}
    if manquants:
        raise SystemExit(f"extraction : {manquants} introuvables dans {chemin}")
    futur = [n for n in arbre.body if isinstance(n, ast.ImportFrom) and n.module == "__future__"]
    module = types.ModuleType(f"extrait_{chemin.stem}")
    module.__dict__.update(espace)
    sys.modules[module.__name__] = module
    exec(compile(ast.Module(body=futur + garde, type_ignores=[]), str(chemin), "exec"), module.__dict__)
    espace.update({k: v for k, v in module.__dict__.items() if not k.startswith("__")})


def code_du_depot(depot: Path) -> dict:
    esp = {"np": np, "hashlib": hashlib, "json": json, "Path": Path, "GardeArret": GardeArret,
           "dataclass": dataclass, "field": field, "__name__": "extrait"}
    extraire(depot / "src/controle_ia/sondes/familles.py",
             {"_empreinte", "SondeLineaireJetons", "SondePerceptron", "SondeMahalanobis"}, esp)
    esp["SondeLineaire"] = None
    esp["_empreinte_familles"] = esp["_empreinte"]

    def verifier(chemin):
        return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()

    esp_f = dict(esp, sceller=lambda c: sceller_simple(Path(c)), verifier=verifier)
    extraire(depot / "src/controle_ia/premier_test_ia/figees.py", {"TABLEAUX", "_empreinte", "ecrire_sondes", "lire_sondes"},
             esp_f)
    esp_f["CLASSES"] = None
    return esp_f


# ---------------------------------------------------------------- vocabulaire byte-level et safetensors
def octets_vers_unicode():
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs, n = bs[:], 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return dict(zip(bs, (chr(c) for c in cs)))


def encoder_bl(texte: str) -> str:
    t = octets_vers_unicode()
    return "".join(t[b] for b in texte.encode("utf-8"))


def ecrire_safetensors(chemin: Path, tenseurs: dict):
    entete, morceaux, pos = {"__metadata__": {"format": "pt"}}, [], 0
    for nom, (x, dt) in tenseurs.items():
        if dt == "BF16":
            u = np.ascontiguousarray(x, dtype=np.float32).view(np.uint32)
            octets = ((u + 0x7FFF + ((u >> 16) & 1)) >> 16).astype("<u2").tobytes()
        else:
            octets = np.ascontiguousarray(x, dtype="<f4").tobytes()
        entete[nom] = {"dtype": dt, "shape": list(x.shape), "data_offsets": [pos, pos + len(octets)]}
        morceaux.append(octets)
        pos += len(octets)
    h = json.dumps(entete).encode()
    h += b" " * (-len(h) % 8)
    with open(chemin, "wb") as f:
        f.write(struct.pack("<Q", len(h)) + h + b"".join(morceaux))


def bf16(x):
    u = np.ascontiguousarray(x, dtype=np.float32).view(np.uint32)
    return (((u + 0x7FFF + ((u >> 16) & 1)) >> 16) << 16).astype(np.uint32).view(np.float32)


# ---------------------------------------------------------------- entrées communes
PARASITES = [" false", "False", "false", " FALSE", "\tfalse", " fib", "fib", " Fib", " life", " important", " legal",
             " lien", " lieutenant", "  lie", " mock", " crash", " kill", " deadline", " vital", " hidden"]


def construire_commun(e: Path, concepts: dict) -> dict:
    e.mkdir(parents=True)
    (e / "modele").mkdir()
    jetons = ["<|begin_of_text|>", "<|eot_id|>", "<|reserved_special_token_0|>"]
    for c in ("tromperie", "enjeux"):
        for m in concepts[c]:
            jetons += [" " + m, m]
        jetons += [" " + concepts[c][0].capitalize(), " " + concepts[c][1].upper()]
    jetons += PARASITES + [" café", ",", ".", " the", "\n", "!!", " 2026"]
    syll = ["ka", "lo", "mi", "ter", "sun", "pra", "vel", "dor", "qui", "zen", "bar", "fo", "nex", "ul", "ri", "go", "sa",
            "pe", "tu"]
    r = rng("vocabulaire")
    tous = {m.lower() for c in concepts if not c.startswith("_") for m in concepts[c]}
    deja = set(jetons)
    while len(jetons) < V:
        t = ("" if r.random() < 0.3 else " ") + "".join(r.choice(syll, size=r.integers(1, 5)))
        if t.strip().lower() not in tous and t not in deja:
            jetons.append(t)
            deja.add(t)
    vocab = {encoder_bl(t): i for i, t in enumerate(jetons) if i >= 3}
    tok = {"version": "1.0", "added_tokens": [{"id": i, "content": jetons[i], "special": True} for i in range(3)],
           "pre_tokenizer": {"type": "ByteLevel"}, "decoder": {"type": "ByteLevel"},
           "model": {"type": "BPE", "vocab": vocab, "merges": []}}
    (e / "modele" / "tokenizer.json").write_text(json.dumps(tok, ensure_ascii=False), encoding="utf-8")

    WU = bf16(rng("desembedding").normal(size=(V, D)) / np.sqrt(D))
    g = (1.0 + 0.1 * rng("norme").normal(size=D)).astype(np.float32)
    ecrire_safetensors(e / "modele" / "model-00001-of-00002.safetensors", {"model.norm.weight": (g, "F32")})
    ecrire_safetensors(e / "modele" / "model-00002-of-00002.safetensors", {"lm_head.weight": (WU, "BF16")})
    index = json.dumps({"weight_map": {"model.norm.weight": "model-00001-of-00002.safetensors",
                                       "lm_head.weight": "model-00002-of-00002.safetensors"}})
    (e / "modele" / "model.safetensors.index.json").write_text(index)

    def ortho(et):
        q, rr = np.linalg.qr(rng(et).normal(size=(D, D)))
        return q * np.sign(np.diag(rr))
    J = {7: ortho("J7"), 15: 1.3 * ortho("J15"), 23: np.eye(D) + 0.03 * rng("J23").normal(size=(D, D))}
    J = {c: m.astype(np.float16) for c, m in J.items()}
    with open(e / "lentille-factice.npz", "wb") as f:
        np.savez(f, **{f"J_{c}": m for c, m in J.items()}, n_prompts=np.array(461), d_model=np.array(D),
                 source_layers=np.arange(31))
    (e / "lentille-vide.pt").write_bytes(b"")
    # Configuration imbriquée, sur le modèle exact du vrai fichier (CLJ2-01) : n_prompts demandé 1 000 sous fit:,
    # prompts_fitted 461 sous results:
    cfg = ("# configuration factice, imbriquée comme lentille-config.yaml réel\nnp_model_id: \"llama3.1-8b-it\"\n"
           "hf_model_name: \"meta-llama/Llama-3.1-8B-Instruct\"\ndataset:\n  name: \"Salesforce/wikitext\"\n"
           "fit:\n  n_prompts: 1000\n  target_layer: null\n  levels: \"1e-2,5e-3,1e-3\"\ngpus:\n  gpu_0:\n"
           "    name: \"NVIDIA B200\"\n    free_gb: 178.4\nenvironment:\n  jlens_commit: null\nresults:\n"
           "  prompts_fitted: {n}\n  final_identity_distance: 0.636485\ncommand: \"fit_lens.py --n_prompts 1000\"\n")
    (e / "lentille-config.yaml").write_text(cfg.format(n=461), encoding="utf-8")
    (e / "lentille-config-discordante.yaml").write_text(cfg.format(n=460), encoding="utf-8")

    Jf = {c: m.astype(np.float64) for c, m in J.items()}
    ids = {c: [i for i, t in enumerate(jetons) if t.startswith(" ") and t[1:].isalpha() and t[1:].lower() in set(concepts[c])]
           for c in ("tromperie", "enjeux")}
    WU64 = WU.astype(np.float64)
    cible = {c: (WU64[ids[c]].mean(0) - WU64.mean(0)) / g for c in ids}        # u tel que g ⊙ u ∝ c̄ − m
    m = e / "modele"
    lignes = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in
              (e / "lentille-factice.npz", e / "lentille-config.yaml", m / "model-00001-of-00002.safetensors",
               m / "model-00002-of-00002.safetensors", m / "model.safetensors.index.json", m / "tokenizer.json")]
    (e / "empreintes-entrees-factices.txt").write_text("\n".join(lignes + ["0" * 64 + "  empreintes-entrees-factices.txt"])
                                                       + "\n", encoding="utf-8")
    return {"jetons": jetons, "ids": ids, "WU": WU, "g": g, "Jf": Jf, "cible": cible, "lignes_empreintes": lignes}


def ecrire_jeu(dossier: Path, code: dict, com: dict, plan: dict, planchers: dict, run_id: str, princ=None,
               n_pl=(N_PLANCHERS, N_PLANCHERS), retirer=(), ajouter=()) -> dict:
    """plan : nom → « J » (J⁻¹ · direction du concept), « sortie » (direction du concept), « zero » ; sinon aléatoire.
    planchers : concept → « alea » ou « concentre »."""
    S, P = code["SondeLineaireJetons"], code["SondePerceptron"]
    princ = princ or PRINC
    Jf, cible = com["Jf"], com["cible"]
    dossier.mkdir(parents=True)

    def bruit(et, echelle):
        x = rng(et).normal(size=D)
        return echelle * x / np.linalg.norm(x)

    sondes, entrees_json, aires, poids = [], [], {"tromperie": {}, "enjeux": {}}, {}
    noms_lin = [f"{c}-{f}-c{L}" for c in ("tromperie", "enjeux") for f in FAMILLES for L in (7, 15, 23)] + list(ajouter)
    for nom in noms_lin:
        if nom in retirer:
            continue
        concept, fam, L = nom.split("-")[0], nom.split("-")[1], int(nom.rsplit("-c", 1)[1])
        t = plan.get(nom)
        if t == "J":
            w0 = np.linalg.solve(Jf[L], cible[concept])
            w = w0 + bruit("bruit/" + nom, 0.15 * np.linalg.norm(w0))
        elif t == "sortie":
            w0 = cible[concept].copy()
            w = w0 + bruit("bruit/" + nom, 0.15 * np.linalg.norm(w0))
        elif t == "zero":
            w = np.zeros(D)
        else:
            w = rng("w/" + nom).normal(size=D)
        if fam == "mahalanobis":
            classe = "SondeMahalanobis"                     # absente du fichier léger, comme dans P3
            emp = code["_empreinte_familles"](f"mahalanobis:{nom}", L, "max", np.zeros(D), np.eye(D))
        elif fam == "perceptron":
            rr = rng("p/" + nom)
            s = P(nom, L, "max", rr.normal(size=D), np.abs(rr.normal(size=D)) + 0.5, rr.normal(size=(4, D)),
                  rr.normal(size=4), rr.normal(size=4), float(rr.normal()), None, "perceptron")
            sondes.append(s)
            classe, emp = "SondePerceptron", s.empreinte()
        else:
            q = rng("q/" + nom).normal(size=D) if fam == "attention" else None
            s = S(nom, L, "attention" if fam == "attention" else "max", w, float(rng("b/" + nom).normal()), q, fam)
            sondes.append(s)
            classe, emp = "SondeLineaireJetons", s.empreinte()
            poids[nom] = w
        entrees_json.append({"agregation": "attention" if fam == "attention" else "max", "classe": classe,
                             "couche": L, "empreinte": emp, "famille": fam, "nom": nom})
        aires[concept][nom] = 0.5
    pl_noms, pl_poids = {}, {}
    for (concept, n), mode in zip(zip(("tromperie", "enjeux"), n_pl), (planchers["tromperie"], planchers["enjeux"])):
        Lm = rng("L/" + concept).normal(size=(D, D)) / np.sqrt(D)
        a = np.linalg.solve(Jf[15], cible[concept])
        a = a / np.linalg.norm(a)
        pl_noms[concept], pl_poids[concept] = [], []
        for k in range(n):
            r = rng(f"pl/{concept}/{k}")
            w = Lm @ r.normal(size=D)
            if mode == "concentre":
                w = w + (6.0 + abs(r.normal())) * np.sqrt(D) * a
            nom = f"{PRINC[concept]}-plancher-plancher-{k}"
            s = S(nom, 15, "max", w, 0.0, None, "plancher")
            sondes.append(s)
            pl_noms[concept].append(nom)
            pl_poids[concept].append(w)
            entrees_json.append({"agregation": "max", "classe": "SondeLineaireJetons", "couche": 15,
                                 "empreinte": s.empreinte(), "famille": "plancher", "nom": nom})
    sha_leg = code["ecrire_sondes"](dossier / "sondes-figees-legeres.npz", sondes,
                                    {"principales": princ, "planchers": pl_noms, "complet": "0" * 64})
    relues, meta, _ = code["lire_sondes"](dossier / "sondes-figees-legeres.npz", sha_leg)   # contrôle croisé
    assert len(relues) == len(sondes) and meta["principales"] == princ
    fig = {"manifeste_sha256": "0" * 64, "run_id": run_id,
           "resultat": {"aires_validation": aires, "familles": FAMILLES, "principales": princ, "sondes": entrees_json,
                        "sondes_figees_sha256": "0" * 64, "sondes_legeres_sha256": sha_leg}}
    p = dossier / "sondes-figees.json"
    p.write_text(json.dumps(fig, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller_simple(p)
    return {"poids": poids, "planchers": {c: np.stack(v, axis=1) for c, v in pl_poids.items()}}


# ---------------------------------------------------------------- recalcul indépendant (double précision, argsort)
def recalcul_independant(com: dict, jeu: dict, concepts: dict) -> dict:
    """S, n_iso, n_pl des 32 cases, sans le code du script : logits complets en double précision, têtes par tri
    complet, début de mot = « espace puis lettres seulement » (équivalent ici : le vocabulaire factice n'a ni chiffre,
    ni apostrophe, ni trait d'union dans ses débuts de mot)."""
    jetons = com["jetons"]
    WU = com["WU"].astype(np.float64)
    g = com["g"].astype(np.float64)
    debut = np.array([t.startswith(" ") and len(t) > 1 and t[1:].isalpha() for t in jetons])
    ens = {c: {i for i, t in enumerate(jetons) if debut[i] and t[1:].lower() in set(concepts[c])} for c in concepts
           if not c.startswith("_")}
    idx_non = np.flatnonzero(~debut)

    def stat(Vd, Jm, concept):
        U = Vd if Jm is None else Jm @ Vd
        Y = g[:, None] * U / np.sqrt(np.mean(U * U, axis=0, keepdims=True))
        Lg = WU @ Y
        Lg[idx_non] = -np.inf
        tetes = np.argsort(-Lg, axis=0, kind="stable")[:20]
        return np.array([sum(int(i) in ens[concept] for i in tetes[:, j]) for j in range(Vd.shape[1])])

    sortie = {}
    for L in (7, 15, 23):
        cle = int.from_bytes(hashlib.sha256(f"isotropes-v3/c{L}".encode()).digest()[:8], "little")
        r = np.random.default_rng(np.random.SeedSequence(entropy=GRAINE, spawn_key=(cle,)))
        Viso = np.concatenate([r.standard_normal((1000, D)) for _ in range(10)], axis=0).T
        for lent in ("logits", "jacobienne"):
            Jm = None if lent == "logits" else com["Jf"][L]
            nuls = {c: np.concatenate([stat(Viso[:, a:a + 1000], Jm, c) for a in range(0, 10000, 1000)]) for c in ens}
            npl = {c: stat(jeu["planchers"][c], Jm, c) for c in ens} if L == 15 else None
            for nom, w in jeu["poids"].items():
                if int(nom.rsplit("-c", 1)[1]) != L or nom in PRINC.values():
                    continue
                c = nom.split("-")[0]
                S = int(stat(w[:, None], Jm, c)[0])
                sortie[(nom, lent)] = {"S": S, "n_iso": int((nuls[c] >= S).sum()),
                                       "n_pl": int((npl[c] >= S).sum()) if npl else None}
    return sortie


# ---------------------------------------------------------------- exécution et contrôles
def lancer(args, journal, cwd, script=SCRIPT):
    t = time.perf_counter()
    r = subprocess.run([sys.executable, "-I", "-B", str(script), *args], capture_output=True, text=True, cwd=cwd)
    r.duree = time.perf_counter() - t
    journal.append(f"$ python3 -I -B {script.name} {' '.join(args)}\n  code {r.returncode} ({r.duree:.1f} s)\n"
                   f"  {(r.stdout + r.stderr).strip()[:1500]}")
    return r


def charger_module():
    spec = importlib.util.spec_from_file_location("comparaison_v3", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def banc_dimensions_reelles(mod, lignes):
    """Noyau des nulles aux dimensions réelles, sur tableaux synthétiques (aucune entrée réelle lue)."""
    Vd, d, Vt = 55_449, 4_096, 128_256      # débuts de mot (règle v3, contre-lecture v2), largeur, vocabulaire
    r = np.random.default_rng(np.random.SeedSequence(entropy=GRAINE, spawn_key=(1,)))
    WUd = (r.standard_normal((Vd, d), dtype=np.float32) / 64.0)
    idx = np.arange(Vd, dtype=np.int64)
    Jm = np.eye(d) + 0.01 * r.standard_normal((d, d))
    g = np.ones(d)
    t = time.perf_counter()
    V0 = r.standard_normal((1000, d)).T
    t_gen = time.perf_counter() - t
    t = time.perf_counter()
    Y_l = mod.vers_sortie(V0, None, g, "direction", {})
    t_vs_l = time.perf_counter() - t
    t = time.perf_counter()
    Y_j = mod.vers_sortie(V0, Jm, g, "direction", {})
    t_vs_j = time.perf_counter() - t
    t = time.perf_counter()
    mod.tetes_debut_lot(WUd, idx, Y_l, 20)
    t_tl = time.perf_counter() - t
    t = time.perf_counter()
    mod.tetes_debut_lot(WUd, idx, Y_j, 20)
    t_tj = time.perf_counter() - t
    del WUd
    R = r.standard_normal((16384, d), dtype=np.float32)
    t = time.perf_counter()
    R64 = R.astype(np.float64)
    _ = R64.T @ R64
    t_gram = time.perf_counter() - t
    del R, R64
    WU = r.standard_normal((Vt, d), dtype=np.float32)
    y = r.standard_normal(d)
    t = time.perf_counter()
    for _ in range(5):
        lg = (WU @ y.astype(np.float32)).astype(np.float64)
        np.argsort(-lg, kind="stable")
    t_case = (time.perf_counter() - t) / 5
    del WU
    bloc = t_gen + t_vs_l + t_vs_j + t_tl + t_tj
    t_iso = 3 * 10 * bloc
    t_pl = 2 * 2 * 0.2 * (t_tl + t_tj) / 2
    t_gram_tot = Vt / 16384 * t_gram
    t_cases = 32 * (t_case * 8)            # 6 têtes + rangs + scores z, ordre de grandeur
    total = t_iso + t_pl + t_gram_tot + t_cases
    lignes += [
        f"Banc du noyau aux dimensions réelles (tableaux synthétiques, {platform.processor() or platform.machine()}, "
        f"numpy {np.__version__}) :",
        f"  tirage de 1 000 directions : {t_gen:.2f} s ; vers_sortie logits / jacobienne : {t_vs_l:.2f} / {t_vs_j:.2f} s",
        f"  têtes de 1 000 directions sur 55 449 × 4 096 : logits {t_tl:.2f} s, jacobienne {t_tj:.2f} s",
        f"  matrice de Gram, bloc de 16 384 lignes : {t_gram:.2f} s ; une case (logits complets + tri) : {t_case:.3f} s",
        f"  extrapolation : nulle isotrope 3 × 10 blocs = {t_iso:.0f} s ; planchers {t_pl:.0f} s ; Gram {t_gram_tot:.0f} s ;"
        f" cases et descriptif ≈ {t_cases:.0f} s",
        f"  calcul seul ≈ {total:.0f} s ({total / 60:.1f} min), hors lecture des entrées (lentille .pt de 1,04 Go par "
        "torch, fragment bf16 de 1,17 Go converti en float32, tokenizer de 9 Mo : de l'ordre d'une à deux minutes, "
        "non mesuré ici)"]
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--depot", default=str(ICI.parents[4]))
    ap.add_argument("--sans-banc", action="store_true")
    a = ap.parse_args()
    dossier, depot = Path(a.dossier).resolve(), Path(a.depot).resolve()
    if dossier.exists():
        raise SystemExit(f"{dossier} existe déjà (R12)")
    t_debut = time.perf_counter()
    concepts = json.loads(CONCEPTS.read_text(encoding="utf-8"))
    e, s, alt = dossier / "entrees", dossier / "sortie", dossier / "altere"
    com = construire_commun(e, concepts)
    code = code_du_depot(depot)
    plan_A = {"tromperie-lineaire-c7": "J", "enjeux-attention-c7": "sortie", "enjeux-difference_moyennes-c15": "sortie",
              "tromperie-attention-c15": "J", "tromperie-difference_moyennes-c23": "sortie"}
    pl_A = {"tromperie": "concentre", "enjeux": "alea"}
    pl_0 = {"tromperie": "alea", "enjeux": "alea"}
    plan_C = {n: "J" for n in ("tromperie-attention-c7", "tromperie-difference_moyennes-c7", "tromperie-lineaire-c7",
                               "enjeux-attention-c7", "enjeux-difference_moyennes-c7", "enjeux-lineaire-c7",
                               "tromperie-attention-c15", "tromperie-lineaire-c15", "enjeux-attention-c15",
                               "enjeux-difference_moyennes-c15")}
    jeux = {"A": ecrire_jeu(e / "A-sain", code, com, plan_A, pl_A, "essai-factice-jlens-v3-A")}
    ecrire_jeu(e / "B-nul", code, com, {}, pl_0, "essai-factice-jlens-v3-B")
    ecrire_jeu(e / "C-majoritaire", code, com, plan_C, pl_0, "essai-factice-jlens-v3-C")
    ecrire_jeu(e / "R-principale", code, com, plan_A, pl_A, "essai-factice-jlens-v3-R",
               princ={"tromperie": PRINC["tromperie"], "enjeux": "enjeux-attention-c15"})
    ecrire_jeu(e / "R-15-sondes", code, com, plan_A, pl_A, "essai-factice-jlens-v3-R", retirer=("enjeux-attention-c23",))
    ecrire_jeu(e / "R-17-sondes", code, com, plan_A, pl_A, "essai-factice-jlens-v3-R", ajouter=("tromperie-lineaire-c11",))
    ecrire_jeu(e / "R-199-planchers", code, com, plan_A, pl_A, "essai-factice-jlens-v3-R", n_pl=(199, 200))
    ecrire_jeu(e / "R-201-planchers", code, com, plan_A, pl_A, "essai-factice-jlens-v3-R", n_pl=(200, 201))
    ecrire_jeu(e / "R-direction-nulle", code, com, {**plan_A, "enjeux-attention-c7": "zero"}, pl_A,
               "essai-factice-jlens-v3-R")
    ecrire_jeu(e / "R-run-reel-simule", code, com, plan_A, pl_A, RUN_REEL)
    s.mkdir(parents=True)
    alt.mkdir()
    journal, controles, mesures = [], [], []

    def ok(nom, cond, detail=""):
        controles.append(f"{'OK' if cond else 'KO'}  {nom}{' — ' + detail if detail else ''}")

    m = e / "modele"

    def base(jeu, factice=True):
        j = e / jeu
        return (["comparer", "--sondes", "non-principales-lineaires",
                 "--sondes-json", str(j / "sondes-figees.json"), "--sondes-npz", str(j / "sondes-figees-legeres.npz"),
                 "--lentille", str(e / "lentille-factice.npz"), "--lentille-config", str(e / "lentille-config.yaml"),
                 "--desembedding", f"{m / 'model.safetensors.index.json'}:lm_head.weight",
                 "--norme-finale", f"{m / 'model.safetensors.index.json'}:model.norm.weight",
                 "--vocabulaire", str(m / "tokenizer.json"), "--concepts", str(CONCEPTS), "--enonce-regle", str(ENONCE),
                 "--empreintes-attendues", str(e / "empreintes-entrees-factices.txt"),
                 "--revision-modele", "0e9e39f249a16976918f6564b8830bc894c89659"]
                + (["--essai-factice"] if factice else []))

    def avec(liste, cle, valeur):
        l = list(liste)
        l[l.index(cle) + 1] = valeur
        return l

    cwd = str(dossier)
    mod = charger_module()

    # ---------------------------------------------------------------- Jeu A : sain
    r = lancer(base("A-sain") + ["--sortie", str(s / "sortie-A.json")], journal, cwd)
    ok("jeu A (sain) : code 0", r.returncode == 0, r.stderr.strip()[:300])
    mesures.append(f"jeu A : {r.duree:.1f} s de bout en bout")
    out = json.loads((s / "sortie-A.json").read_text(encoding="utf-8"))
    man = json.loads((s / "sortie-A-manifeste.json").read_text(encoding="utf-8"))
    mesures.append(f"jeu A, étapes (manifeste) : {man['durees_par_etape_s']}")
    rp = out["regle_primaire"]
    cs = {(c["sonde"], c["lentille"]): c for c in rp["cases"]}
    ok("A : 32 cases (16 sondes × 2 lentilles), complète, sondes = les 16 de la règle, dans son ordre",
       len(rp["cases"]) == 32 and rp["complete"] is True and rp["sondes_lues"] == list(mod.SONDES_V3)
       and [x["nom"] for x in out["sondes"]] == list(mod.SONDES_V3))
    ok("A : énoncé de la sortie = fichier gelé, empreinte be020390…, liste aac34d5c…",
       rp["enonce"] == ENONCE.read_text(encoding="utf-8")
       and rp["empreinte_enonce"] == "be02039011c50c50a4eca0c38c26c7d31c38f6fc7315567659e8fd6cb7b64820"
       and rp["liste_de_mots"]["sha256"] == "aac34d5cb52637fef6ebdd0d36009f8842efdef52d5e5298334e3a84f388bf6c")
    attendu_A = {("tromperie-lineaire-c7", "jacobienne"), ("tromperie-difference_moyennes-c23", "jacobienne"),
                 ("enjeux-attention-c7", "logits"), ("enjeux-difference_moyennes-c15", "logits"),
                 ("tromperie-difference_moyennes-c23", "logits")}
    coh = {k for k, v in cs.items() if v["verdict"] == "cohérent"}

    def fmt(k):
        v = cs[k]
        return f"{k[0]}/{k[1]} S={v['S']} n_iso={v['n_iso']} n_pl={v['n_pl']} → {v['verdict']}"
    ok("A : exactement les cinq cases plantées sont « cohérentes » (c7 sous J, c7 en sortie, c15 en sortie, c23 sous les "
       "deux)", coh == attendu_A, " ; ".join(fmt(k) for k in sorted(attendu_A | coh)))
    k_pl = ("tromperie-attention-c15", "jacobienne")
    dpl = out["sondes"][[x["nom"] for x in out["sondes"]].index(k_pl[0])]["lentilles"]["jacobienne"]["descriptif_regle"]
    ok("A : tromperie-attention-c15 sous J (plantée, planchers concentrés) : isotropes passées (n_iso ≤ 14), planchers "
       "non (n_pl > 2) → « non cohérent » ; « cohérent » sans planchers (descriptif)",
       cs[k_pl]["verdict"] == "non cohérent" and cs[k_pl]["S"] >= 2 and cs[k_pl]["n_iso"] <= 14 and cs[k_pl]["n_pl"] > 2
       and dpl["verdict_sans_planchers"] == "cohérent", fmt(k_pl))
    ok("A : nulles — couches 7 et 23 « isotropes seules » (n_pl absent), couche 15 « isotropes et planchers »",
       all((v["n_pl"] is None and v["nulles"] == "isotropes seules") if v["couche"] != 15
           else (isinstance(v["n_pl"], int) and v["nulles"] == "isotropes et planchers") for v in cs.values()))
    ok("A : chaque verdict recalculé à partir de (S, n_iso, n_pl) par la règle écrite dans l'essai",
       all(v["verdict"] == ("cohérent" if v["S"] >= 2 and v["n_iso"] <= 14 and (v["couche"] != 15 or v["n_pl"] <= 2)
                            else "non cohérent") for v in cs.values())
       and all(v["p_rang"] == f"{1 + v['n_iso']}/10001" for v in cs.values()))
    ve, cp = rp["verdict_ensemble"], rp["comparaison"]
    ok("A : verdict d'ensemble — jacobienne X = 2, logits X = 3, « verbalisation minoritaire, au-delà du hasard »",
       ve["jacobienne"]["X"] == 2 and ve["logits"]["X"] == 3
       and ve["jacobienne"]["niveau"] == ve["logits"]["niveau"] == "verbalisation minoritaire, au-delà du hasard"
       and ve["borne_erreur_familiale_nulle_isotrope"]["fraction"] == "480/10001",
       f"J {ve['jacobienne']['X']}, logits {ve['logits']['X']}")
    ok("A : comparaison — b = 1, c = 2, les deux = 1, p du signe = 1, formulation non permise, aucune phrase",
       cp["b_jacobienne_seule"] == 1 and cp["c_logits_seuls"] == 2 and cp["les_deux"] == 1
       and cp["test_du_signe_exact_bilateral"]["p"] == "1/1" and cp["formulation_permise"] is False
       and cp["phrase"] is None and cp["grille"]["tromperie-difference_moyennes-c23"] == "les deux"
       and cp["grille"]["tromperie-lineaire-c7"] == "jacobienne seule", json.dumps(cp["grille"], ensure_ascii=False)[:300])
    # Les principales n'apparaissent nulle part (hors énoncé et liste des exclues)
    o2 = json.loads(json.dumps(out))
    o2["regle_primaire"].pop("enonce")
    o2["regle_primaire"].pop("principales_exclues_non_decodees")
    texte = json.dumps(o2, ensure_ascii=False)
    ok("A : les deux principales n'apparaissent nulle part dans la sortie (hors énoncé et liste des exclues), ni dans le "
       "manifeste", all(p not in texte and p not in json.dumps(man, ensure_ascii=False) for p in PRINC.values()))
    # Recalcul indépendant
    t = time.perf_counter()
    ind = recalcul_independant(com, jeux["A"], concepts)
    t_ind = time.perf_counter() - t
    ecarts = [(k, ind[k], {x: cs[k][x] for x in ("S", "n_iso", "n_pl")}) for k in cs
              if (ind[k]["S"], ind[k]["n_pl"]) != (cs[k]["S"], cs[k]["n_pl"]) or abs(ind[k]["n_iso"] - cs[k]["n_iso"]) > 1]
    exacts = sum(ind[k] == {x: cs[k][x] for x in ("S", "n_iso", "n_pl")} for k in cs)
    verd_ind = all(mod.verdict_v3(ind[k]["S"], ind[k]["n_iso"], ind[k]["n_pl"], cs[k]["couche"]) == cs[k]["verdict"]
                   for k in cs)
    ok("A : recalcul indépendant des 32 cases (double précision, tri complet, graines rederivées) : S et n_pl identiques, "
       "n_iso à ±1 près, verdicts identiques", len(ind) == 32 and not ecarts and verd_ind,
       f"{exacts}/32 cases identiques au chiffre près ; écarts : {ecarts[:3]} ; {t_ind:.1f} s")
    # S = compte affiché ; S en mots distincts ; descriptif
    lignes_S = []
    bon = True
    for x in out["sondes"]:
        for l in ("logits", "jacobienne"):
            tt = x["lentilles"][l]["plus"]["tete_debut_de_mot"]
            S_aff = sum(1 for t in tt if t["texte"][1:].lower() in set(concepts[x["concept"]]))
            dr = x["lentilles"][l]["descriptif_regle"]
            bon &= (S_aff == cs[(x["nom"], l)]["S"] == dr["S_jetons"] and len(tt) == 20
                    and all(t["texte"].startswith(" ") for t in tt)
                    and dr["S_mots_distincts"] == len({t["texte"][1:].lower() for t in tt
                                                       if t["texte"][1:].lower() in set(concepts[x["concept"]])}))
            lignes_S.append(f"{x['nom']}/{l}:{S_aff}")
    ok("A : S = compte des jetons du concept dans la tête de début de mot affichée ; S en mots distincts juste", bon)
    st = out["descriptif"]["strates"]
    ok("A : strates descriptives — par couche, concept, famille ; couche 15 avec / sans planchers ; seuil v2",
       st["par_couche"]["7"] == {"logits": 1, "jacobienne": 1} and st["par_couche"]["23"] == {"logits": 1, "jacobienne": 1}
       and st["couche_15_avec_planchers"] == {"logits": 1, "jacobienne": 0}
       and st["couche_15_sans_planchers"]["jacobienne"] >= 1 and "X_au_seuil_v2_non_corrige" in st,
       f"c15 sans planchers {st['couche_15_sans_planchers']} ; seuil v2 {st['X_au_seuil_v2_non_corrige']}")
    nl = out["descriptif"]["nulles"]
    ok("A : résumés des nulles (médiane, quantile 0,99, comptes) : 12 isotropes (3 couches × 2 lentilles × 2 concepts) "
       "sur 10 000, 4 planchers sur 200",
       len(nl["isotropes"]) == 12 and all(v["n"] == 10000 for v in nl["isotropes"].values())
       and len(nl["planchers_couche_15"]) == 4 and all(v["n"] == 200 for v in nl["planchers_couche_15"].values()),
       "médianes iso : " + ", ".join(f"{k}={v['mediane']:g}" for k, v in list(nl["isotropes"].items())[:4]) + " …")
    dec = out["descriptif"]["declencheurs_audit"]["declenches"]
    ok("A : déclencheurs d'audit calculés (liste rendue, sans effet sur les verdicts)", isinstance(dec, list),
       f"{len(dec)} : {dec[:4]}")
    ok("A : sortie marquée « ESSAI FACTICE » ; manifeste : graines isotropes-v3/c7, c15, c23, essai factice",
       out["essai_factice"] is True and out["statut"].startswith("ESSAI FACTICE")
       and {"isotropes-v3/c7", "isotropes-v3/c15", "isotropes-v3/c23"} <= set(man["graines"])
       and man["essai_factice"] is True)
    ok("A : CLJ2-01 — configuration imbriquée lue : « ajustée sur 461 textes (… results.prompts_fitted) », pas 1 000",
       out["lentille_ajustee_sur"].startswith("ajustée sur 461 textes")
       and "results.prompts_fitted" in out["lentille_ajustee_sur"], out["lentille_ajustee_sur"])
    ok("A : empreintes attendues conformes ; sortie et manifeste scellés (sha256sum -c)",
       isinstance(man["empreintes_attendues"], dict)
       and subprocess.run(["sha256sum", "-c", "sortie-A.json.sha256", "sortie-A-manifeste.json.sha256"], cwd=s,
                          capture_output=True).returncode == 0)
    r = lancer(base("A-sain") + ["--sortie", str(s / "sortie-A-bis.json")], journal, cwd)
    ok("A : déterminisme — deuxième run, sortie identique octet pour octet (même machine)",
       r.returncode == 0 and (s / "sortie-A.json").read_bytes() == (s / "sortie-A-bis.json").read_bytes())

    # ---------------------------------------------------------------- Jeu B : nul
    r = lancer(base("B-nul") + ["--sortie", str(s / "sortie-B.json")], journal, cwd)
    ok("jeu B (nul) : code 0", r.returncode == 0, r.stderr.strip()[:300])
    if r.returncode == 0:
        oB = json.loads((s / "sortie-B.json").read_text(encoding="utf-8"))["regle_primaire"]
        vB = oB["verdict_ensemble"]
        ok("B : aucune case « cohérente » ; X = 0 pour les deux lentilles, « aucune verbalisation détectée » ; b = c = 0, "
           "p = 1, formulation non permise",
           all(c["verdict"] == "non cohérent" for c in oB["cases"])
           and vB["logits"]["X"] == vB["jacobienne"]["X"] == 0
           and vB["logits"]["niveau"] == "aucune verbalisation détectée"
           and oB["comparaison"]["formulation_permise"] is False,
           "S max " + str(max(c["S"] for c in oB["cases"])) + ", n_iso min " + str(min(c["n_iso"] for c in oB["cases"])))
        dB = json.loads((s / "sortie-B.json").read_text(encoding="utf-8"))["descriptif"]["declencheurs_audit"]["declenches"]
        ok("B : déclencheur d'audit « les deux lentilles ont X = 0 »", "les deux lentilles ont X = 0" in dB)

    # ---------------------------------------------------------------- Jeu C : majoritaire sous J
    r = lancer(base("C-majoritaire") + ["--sortie", str(s / "sortie-C.json")], journal, cwd)
    ok("jeu C (majoritaire) : code 0", r.returncode == 0, r.stderr.strip()[:300])
    if r.returncode == 0:
        oC = json.loads((s / "sortie-C.json").read_text(encoding="utf-8"))
        vC, cC = oC["regle_primaire"]["verdict_ensemble"], oC["regle_primaire"]["comparaison"]
        ok("C : jacobienne X = 10, « verbalisation majoritaire » ; logits X = 0",
           vC["jacobienne"]["X"] == 10 and vC["jacobienne"]["niveau"] == "verbalisation majoritaire"
           and vC["logits"]["X"] == 0, f"J {vC['jacobienne']['X']}, logits {vC['logits']['X']}")
        ok("C : b = 10, c = 0, p = 2/1024 = 1/512, formulation permise, phrase « la lentille jacobienne verbalise plus de "
           "sondes que la lentille des logits »",
           cC["b_jacobienne_seule"] == 10 and cC["c_logits_seuls"] == 0
           and cC["test_du_signe_exact_bilateral"]["p"] == "1/512" and cC["formulation_permise"] is True
           and cC["phrase"] == "la lentille jacobienne verbalise plus de sondes que la lentille des logits",
           f"p = {cC['test_du_signe_exact_bilateral']['p']}")
        dC = oC["descriptif"]["declencheurs_audit"]["declenches"]
        ok("C : déclencheur d'audit « b ≥ 6 avec c = 0 »", any(x.startswith("b = 10 ≥ 6") for x in dC))

    # ---------------------------------------------------------------- Tests unitaires de la règle (bords)
    vv = mod.verdict_v3
    bords = [vv(2, 14, None, 7) == "cohérent", vv(2, 15, None, 7) == "non cohérent",
             vv(2, 14, 2, 15) == "cohérent", vv(2, 14, 3, 15) == "non cohérent", vv(2, 15, 0, 15) == "non cohérent",
             vv(1, 0, None, 23) == "non cohérent", vv(1, 0, 0, 15) == "non cohérent", vv(20, 0, None, 23) == "cohérent"]
    ok("règle, bords : n_iso 14 → cohérent, 15 → non ; n_pl 2 → cohérent, 3 → non ; S 1 → non, 2 → oui", all(bords),
       str(bords))
    refus_u = []
    for args_v, code_v in (((2, 0, None, 15), "planchers-insuffisants"), ((2, 0, 1, 7), "incoherence-interne"),
                           ((2.0, 0, None, 7), "incoherence-interne"), ((True, 0, None, 7), "incoherence-interne")):
        try:
            vv(*args_v)
            refus_u.append(False)
        except mod.Refus as x:
            refus_u.append(x.code == code_v)
    ok("règle : couche 15 sans planchers, planchers hors couche 15, S non entier → refus", all(refus_u), str(refus_u))
    ok("règle : 14 = plus grand n_iso avec (1 + n)/10 001 ≤ 0,05/32 ; n_pl max = 200 − ⌈0,99 × 200⌉ = 2 ; borne 480/10 001",
       Fraction(15, 10001) <= Fraction(5, 100) / 32 < Fraction(16, 10001) and mod.n_iso_max_calcule() == 14
       and mod.n_pl_max_calcule() == 2 and mod.borne_familiale() == Fraction(480, 10001)
       and int(np.quantile(np.arange(1, 201), 0.99, method="inverted_cdf")) == 198)
    ok("règle : ni np.quantile ni quantile dans le verdict (verdict_v3 et son appel)",
       "quantile" not in inspect.getsource(mod.verdict_v3))
    minima = {6: (6, 0), 7: (7, 0), 8: (8, 0), 9: (8, 1), 10: (9, 1), 11: (10, 1), 12: (10, 2), 13: (11, 2), 14: (12, 2),
              15: (12, 3), 16: (13, 3)}
    bon = True
    for n, (bmin, cmax) in minima.items():
        permis = [(b, n - b) for b in range(n + 1) if b >= n - b and mod.test_signe_bilateral(b, n - b) <= Fraction(5, 100)]
        bon &= min(permis)[0] == bmin and min(permis)[1] == cmax
    p_ref = [float(mod.test_signe_bilateral(b, c)) for b, c in ((5, 0), (6, 0), (7, 1), (8, 1))]
    ok("test du signe : minima de la règle (6-0, 7-0, 8-0, 8-1, 9-1, 10-1, 10-2, 11-2, 12-2, 12-3, 13-3) retrouvés ; "
       "5-0 et 7-1 non permis ; symétrique ; p(0, 0) = 1",
       bon and p_ref[0] > 0.05 and p_ref[1] <= 0.05 and p_ref[2] > 0.05 and p_ref[3] <= 0.05
       and mod.test_signe_bilateral(0, 0) == 1 and mod.test_signe_bilateral(2, 9) == mod.test_signe_bilateral(9, 2),
       f"p(5,0)={p_ref[0]:.4f}, p(6,0)={p_ref[1]:.4f}, p(7,1)={p_ref[2]:.4f}, p(8,1)={p_ref[3]:.4f}")
    ok("niveaux : 0 → aucune ; 1 et 7 → minoritaire ; 8 et 16 → majoritaire",
       [mod.niveau(x) for x in (0, 1, 7, 8, 16)] == [mod.NIVEAUX[0], mod.NIVEAUX[1], mod.NIVEAUX[1], mod.NIVEAUX[2],
                                                      mod.NIVEAUX[2]])

    # ---------------------------------------------------------------- Refus
    def refus(nom, args, code_attendu, contient=None, script=SCRIPT):
        r = lancer(args, journal, cwd, script)
        cond = r.returncode == 2 and f"REFUS {code_attendu}" in r.stderr and (contient is None or contient in r.stderr)
        ok(f"refus {nom} : code 2 et « REFUS {code_attendu} »" + (f" nommant « {contient} »" if contient else ""), cond,
           r.stderr.strip()[:240])

    refus("principale dans la sélection (principales du fichier déplacées)",
          base("R-principale") + ["--sortie", str(s / "x01.json")], "principale-selectionnee", "enjeux-lineaire-c15")
    refus("15 sondes", base("R-15-sondes") + ["--sortie", str(s / "x02.json")], "compte-sondes", "enjeux-attention-c23")
    refus("17 sondes", base("R-17-sondes") + ["--sortie", str(s / "x03.json")], "compte-sondes", "tromperie-lineaire-c11")
    refus("199 planchers", base("R-199-planchers") + ["--sortie", str(s / "x04.json")], "planchers-insuffisants", "199")
    refus("201 planchers", base("R-201-planchers") + ["--sortie", str(s / "x05.json")], "planchers-insuffisants", "201")
    refus("case manquante (direction nulle : 2 cases sur 32)", base("R-direction-nulle") + ["--sortie", str(s / "x06.json")],
          "cases-manquantes", "enjeux-attention-c7/logits")
    refus("sans --essai-factice, run factice", base("A-sain", factice=False) + ["--sortie", str(s / "x07.json")],
          "run-inattendu")
    refus("sans --essai-factice, run réel simulé : empreintes des 16 sondes contrôlées en dur",
          base("R-run-reel-simule", factice=False) + ["--sortie", str(s / "x08.json")], "empreinte-sonde",
          "tromperie-attention-c7")
    # Liste de mots altérée, re-scellée (le sceau compagnon passe, l'empreinte en dur non)
    cj = json.loads(CONCEPTS.read_text(encoding="utf-8"))
    cj["tromperie"] = cj["tromperie"][:-1]
    p_la = alt / "concepts-sondes-p3-v3.json"
    p_la.write_text(json.dumps(cj, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller_simple(p_la)
    refus("liste de mots altérée et re-scellée", avec(base("A-sain"), "--concepts", str(p_la)) + ["--sortie", str(s / "x09.json")],
          "empreinte-concepts")
    refus("liste de mots v2 (scellée, autre empreinte)", avec(base("A-sain"), "--concepts", str(CONCEPTS_V2))
          + ["--sortie", str(s / "x10.json")], "empreinte-concepts")
    # Énoncé altéré dans le script (copie modifiée d'un caractère)
    src = SCRIPT.read_text(encoding="utf-8")
    assert src.count("si S >= 2, si ") == 1
    p_sa = alt / "script-enonce-altere" / SCRIPT.name
    p_sa.parent.mkdir()
    p_sa.write_text(src.replace("si S >= 2, si ", "si S >= 3, si "), encoding="utf-8")
    refus("énoncé altéré dans le script (« S >= 3 »)", base("A-sain") + ["--sortie", str(s / "x11.json")], "enonce-altere",
          script=p_sa)
    p_ea = alt / "enonce-regle-primaire-v3.txt"
    p_ea.write_text(ENONCE.read_text(encoding="utf-8").replace("n_iso <= 14", "n_iso <= 15"), encoding="utf-8")
    refus("fichier d'énoncé altéré (« n_iso <= 15 »)", avec(base("A-sain"), "--enonce-regle", str(p_ea))
          + ["--sortie", str(s / "x12.json")], "enonce-fichier-discordant")
    # Autres gardes reprises de la v2
    refus("sortie existante", base("A-sain") + ["--sortie", str(s / "sortie-A.json")], "sortie-existe")
    fj = json.loads((e / "A-sain" / "sondes-figees.json").read_text(encoding="utf-8"))
    fj["run_id"] = "autre"
    (alt / "sondes-figees.json").write_text(json.dumps(fj, ensure_ascii=False, indent=1), encoding="utf-8")
    (alt / "sondes-figees.json.sha256").write_text((e / "A-sain" / "sondes-figees.json.sha256").read_text())  # périmé
    refus("sceau du JSON des sondes faux", avec(base("A-sain"), "--sondes-json", str(alt / "sondes-figees.json"))
          + ["--sortie", str(s / "x13.json")], "sceau-faux")
    fj = json.loads((e / "A-sain" / "sondes-figees.json").read_text(encoding="utf-8"))
    fj["resultat"]["sondes"] = [x for x in fj["resultat"]["sondes"] if not x["nom"].endswith("-plancher-plancher-7")]
    p_pd = alt / "planchers-discordants" / "sondes-figees.json"
    p_pd.parent.mkdir()
    p_pd.write_text(json.dumps(fj, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller_simple(p_pd)
    refus("plancher du fichier de poids absent de sondes-figees.json (re-scellé)",
          avec(base("A-sain"), "--sondes-json", str(p_pd)) + ["--sortie", str(s / "x19.json")], "planchers-discordants",
          "plancher-plancher-7")
    b_cd = [x for x in avec(base("A-sain"), "--lentille-config", str(e / "lentille-config-discordante.yaml"))]
    i = b_cd.index("--empreintes-attendues")
    b_cd = b_cd[:i] + b_cd[i + 2:]
    refus("configuration imbriquée discordante (results.prompts_fitted 460 ≠ 461) — CLJ2-01",
          b_cd + ["--sortie", str(s / "x14.json")], "lentille-config-discordante", "460")
    lignes = com["lignes_empreintes"]
    p_ef = alt / "empreintes-fausses.txt"
    p_ef.write_text("\n".join(l if not l.endswith("tokenizer.json") else "a" * 64 + "  tokenizer.json" for l in lignes)
                    + "\n", encoding="utf-8")
    refus("empreinte attendue fausse", avec(base("A-sain"), "--empreintes-attendues", str(p_ef))
          + ["--sortie", str(s / "x15.json")], "empreinte-entree", "tokenizer.json")
    code_pt = "lentille-illisible" if importlib.util.find_spec("torch") else "torch-absent-pour-pt"
    b_pt = avec(base("A-sain"), "--lentille", str(e / "lentille-vide.pt"))
    i = b_pt.index("--empreintes-attendues")
    refus(f"lentille .pt vide ({'torch présent' if code_pt == 'lentille-illisible' else 'torch absent'})",
          b_pt[:i] + b_pt[i + 2:] + ["--sortie", str(s / "x16.json")], code_pt)
    r = lancer(["comparer", "--sondes", "toutes-lineaires"] + base("A-sain")[3:] + ["--sortie", str(s / "x17.json")],
               journal, cwd)
    ok("mode « toutes-lineaires » (v2) refusé par l'analyseur d'arguments (code non nul, aucune sortie)",
       r.returncode != 0 and not (s / "x17.json").exists(), r.stderr.strip().splitlines()[-1][:160] if r.stderr else "")
    r = lancer(base("A-sain") + ["--un-seul-couple", "tromperie-lineaire-c7,7", "--sortie", str(s / "x18.json")], journal, cwd)
    ok("--un-seul-couple refusé (option retirée en v3)", r.returncode != 0 and not (s / "x18.json").exists())
    r = lancer(["verifier-concepts", "--vocabulaire", str(m / "tokenizer.json"), "--concepts", str(CONCEPTS)], journal, cwd)
    ok("verifier-concepts sur la liste v3 et le vocabulaire factice : code 0, « liste v3 de la règle »",
       r.returncode == 0 and "liste v3 de la règle" in r.stdout)
    restes = [p.name for p in s.iterdir() if re.match(r"x\d", p.name)]
    ok("aucun refus n'a laissé de sortie", not restes, str(restes))

    # ---------------------------------------------------------------- Temps
    if not a.sans_banc:
        banc_dimensions_reelles(mod, mesures)
    else:
        mesures.append("banc aux dimensions réelles : non lancé (--sans-banc)")
    ko = [c for c in controles if c.startswith("KO")]
    texte = (f"Essai factice v3 — largeur {D}, vocabulaire {V}, {N_PLANCHERS} planchers par concept, 10 000 isotropes "
             f"par couche, graine {GRAINE}\nScript : {SCRIPT.name} ({hashlib.sha256(SCRIPT.read_bytes()).hexdigest()})\n"
             f"Essai : {Path(__file__).name} ({hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})\n"
             f"Interpréteur : python {sys.version.split()[0]}, numpy {np.__version__}, {platform.platform()}\n"
             f"Dépôt (code extrait) : {depot}\n\n" + "\n".join(controles)
             + f"\n\nBILAN : {len(controles) - len(ko)}/{len(controles)} contrôles OK\n\n--- temps ---\n"
             + "\n".join(mesures) + f"\nessai complet : {time.perf_counter() - t_debut:.0f} s\n"
             + "\n--- commandes ---\n" + "\n".join(journal) + "\n")
    texte = texte.replace(str(dossier), "<essai>").replace(str(ICI), "<dossier>").replace(str(depot), "<depot>")
    (dossier / "journal-essai-factice-v3.txt").write_text(texte, encoding="utf-8")
    print(texte.split("--- commandes ---")[0])
    return 1 if ko else 0


if __name__ == "__main__":
    sys.exit(main())
