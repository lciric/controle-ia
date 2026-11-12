"""Essai de bout en bout, sur tenseurs factices, de `comparaison_jlens_logitlens_sondes_p3_v2.py` — v2.

Largeur 128, vocabulaire 2000, couches 7, 15 et 23, 200 planchers par sonde principale (comme P3). Aucun poids réel,
aucune lecture de `donnees/`. Repris de l'essai v1 ; ce qui change : la règle primaire (CLJ-02) est montrée sur les
trois signaux plantés et sur des directions aléatoires ; la liste de mots v2 et les jetons de début de mot (CLJ-03) ;
200 planchers factices au lieu de 20 (CLJ-08) ; les nouveaux refus et options (CLJ-04 à CLJ-07, CLJ-09, CLJ-10).

Le fichier de poids des sondes est écrit **par le code du dépôt** : `ecrire_sondes` de
`src/controle_ia/premier_test_ia/figees.py` et les classes de `src/controle_ia/sondes/familles.py`, extraites par l'arbre
syntaxique (le module importe torch, absent ici ; les fonctions extraites n'en ont pas besoin) ; `lire_sondes` du dépôt
relit le fichier factice (contrôle croisé).

Signaux plantés :
- tromperie, couche 15 (principale) : w = J₁₅⁻¹ · (direction du concept) — la règle doit dire « cohérent » sous la
  lentille jacobienne et « non cohérent » sous la lentille des logits ;
- enjeux, couche 15 (principale) : w = direction du concept dans l'espace de sortie — l'inverse ;
- tromperie, couche 23 : J₂₃ ≈ identité — application descriptive, « cohérent » sous les deux lentilles ;
- couche 7 et autres familles : directions aléatoires — « non cohérent » partout.

Usage : python3 -I -B essai_factice_comparaison_jlens_v2.py --dossier <dossier neuf> [--depot <racine du dépôt>]
Graines : numpy.random.SeedSequence(20261029) dérivée par étiquette (R9).
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import struct
import subprocess
import sys
import types
from dataclasses import dataclass, field  # noqa: F401  (espace de noms des classes extraites)
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "comparaison_jlens_logitlens_sondes_p3_v2.py"
CONCEPTS = ICI / "concepts-sondes-p3-v2.json"
D, V = 128, 2000
GRAINE = 20261029
N_PLANCHERS = 200


def rng(etiquette):
    cle = int.from_bytes(hashlib.sha256(etiquette.encode()).digest()[:8], "little")
    return np.random.default_rng(np.random.SeedSequence(entropy=GRAINE, spawn_key=(cle,)))


def sceller_simple(chemin: Path) -> str:
    sha = hashlib.sha256(chemin.read_bytes()).hexdigest()
    Path(str(chemin) + ".sha256").write_text(f"{sha}  {chemin.name}\n", encoding="utf-8")
    return sha


# ---------------------------------------------------------------- code du dépôt, extrait sans torch
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
    module = types.ModuleType(f"extrait_{chemin.stem}")       # module enregistré : exigé par dataclass
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
            octets = ((u + 0x7FFF + ((u >> 16) & 1)) >> 16).astype("<u2").tobytes()   # arrondi au plus proche pair
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


# ---------------------------------------------------------------- construction des entrées factices
PARASITES = [" false", "False", "false", " FALSE", "\tfalse", " fib", "fib", " Fib", " life", " important", " legal",
             " lien", " lieutenant", "  lie"]


def construire(e: Path, depot: Path, concepts: dict) -> dict:
    code = code_du_depot(depot)
    S, P = code["SondeLineaireJetons"], code["SondePerceptron"]
    e.mkdir(parents=True)
    (e / "modele").mkdir()

    # Vocabulaire : 3 spéciaux ; chaque mot des listes en début de mot (" mot"), sans espace ("mot") ; trois mots en
    # majuscule initiale (" Lie"…) ; parasites de la contre-lecture (booléens, fib, génériques, préfixes, double espace) ;
    # « café » (test des octets) ; syllabes ; ponctuation.
    jetons = ["<|begin_of_text|>", "<|eot_id|>", "<|reserved_special_token_0|>"]
    for c in ("tromperie", "enjeux"):
        for m in concepts[c]:
            jetons += [" " + m, m]
        jetons += [" " + concepts[c][0].capitalize()]
    jetons += PARASITES + [" café", ",", ".", " the", "\n", "!!", " 2026"]
    syll = ["ka", "lo", "mi", "ter", "sun", "pra", "vel", "dor", "qui", "zen", "bar", "fo", "nex", "ul", "ri", "go", "sa"]
    r = rng("vocabulaire")
    tous = {m.lower() for c in concepts if not c.startswith("_") for m in concepts[c]}
    while len(jetons) < V:
        t = ("" if r.random() < 0.3 else " ") + "".join(r.choice(syll, size=r.integers(1, 4)))
        if t.strip().lower() not in tous and t not in jetons:
            jetons.append(t)
    vocab = {encoder_bl(t): i for i, t in enumerate(jetons) if i >= 3}
    tok = {"version": "1.0", "added_tokens": [{"id": i, "content": jetons[i], "special": True} for i in range(3)],
           "pre_tokenizer": {"type": "ByteLevel"}, "decoder": {"type": "ByteLevel"},
           "model": {"type": "BPE", "vocab": vocab, "merges": []}}
    (e / "modele" / "tokenizer.json").write_text(json.dumps(tok, ensure_ascii=False), encoding="utf-8")

    # Poids de sortie (désembedding en bf16 dans le second fragment, norme en f32 dans le premier)
    WU = bf16(rng("desembedding").normal(size=(V, D)) / np.sqrt(D))
    g = (1.0 + 0.1 * rng("norme").normal(size=D)).astype(np.float32)
    ecrire_safetensors(e / "modele" / "model-00001-of-00002.safetensors", {"model.norm.weight": (g, "F32")})
    ecrire_safetensors(e / "modele" / "model-00002-of-00002.safetensors", {"lm_head.weight": (WU, "BF16")})
    index = json.dumps({"weight_map": {"model.norm.weight": "model-00001-of-00002.safetensors",
                                       "lm_head.weight": "model-00002-of-00002.safetensors"}})
    (e / "modele" / "model.safetensors.index.json").write_text(index)
    (e / "modele" / "index.json").write_text(index)            # CLJ-06 : même index sous un autre nom

    # Lentille : J7 orthogonale, J15 = 1,3 × orthogonale, J23 ≈ identité ; stockée en float16 (comme le dépôt)
    def ortho(et):
        q, rr = np.linalg.qr(rng(et).normal(size=(D, D)))
        return q * np.sign(np.diag(rr))
    J = {7: ortho("J7"), 15: 1.3 * ortho("J15"), 23: np.eye(D) + 0.03 * rng("J23").normal(size=(D, D))}
    J = {c: m.astype(np.float16) for c, m in J.items()}
    with open(e / "lentille-factice.npz", "wb") as f:
        np.savez(f, **{f"J_{c}": m for c, m in J.items()}, n_prompts=np.array(461), d_model=np.array(D),
                 source_layers=np.arange(31))
    with open(e / "lentille-sans-c23.npz", "wb") as f:
        np.savez(f, J_7=J[7], J_15=J[15], n_prompts=np.array(461), d_model=np.array(D))
    with open(e / "desembedding-largeur-fausse.npy", "wb") as f:
        np.save(f, WU[:, :48])
    (e / "lentille-vide.pt").write_bytes(b"")
    (e / "lentille-config.yaml").write_text(
        "# configuration factice, sur le modèle de celle de la lentille réelle\nmodel: meta-llama/Llama-3.1-8B-Instruct\n"
        "prompts_fitted: 461\ntarget_layer: null\njlens_commit: null\nfit:\n  n_prompts: 1000\n", encoding="utf-8")
    (e / "lentille-config-discordante.yaml").write_text(
        "model: meta-llama/Llama-3.1-8B-Instruct\nprompts_fitted: 1000\ntarget_layer: null\n", encoding="utf-8")

    # Directions plantées (jetons de concept = jetons de début de mot, casse libre)
    Jf = {c: m.astype(np.float64) for c, m in J.items()}
    ids = {c: [i for i, t in enumerate(jetons) if t.startswith(" ") and not t.startswith("  ")
               and t[1:].lower() in set(concepts[c])] for c in ("tromperie", "enjeux")}
    WU64 = WU.astype(np.float64)
    cible = {c: (WU64[ids[c]].mean(0) - WU64.mean(0)) / g for c in ids}       # u tel que g ⊙ u ∝ c̄ − m

    def bruit(et, echelle):
        x = rng(et).normal(size=D)
        return echelle * x / np.linalg.norm(x)
    plant = {
        ("tromperie", 15): np.linalg.solve(Jf[15], cible["tromperie"]),
        ("tromperie", 23): np.linalg.solve(Jf[23], cible["tromperie"]),
        ("enjeux", 15): cible["enjeux"].copy(),
    }
    sondes, aires = [], {"tromperie": {}, "enjeux": {}}
    princ = {"tromperie": "tromperie-difference_moyennes-c15", "enjeux": "enjeux-lineaire-c15"}
    familles = ["difference_moyennes", "lineaire", "perceptron", "attention", "mahalanobis"]
    entrees_json = []
    for concept in ("tromperie", "enjeux"):
        for fam in familles:
            for c in (7, 15, 23):
                nom = f"{concept}-{fam}-c{c}"
                w0 = plant.get((concept, c)) if nom.rsplit("-", 1)[0] == princ[concept].rsplit("-", 1)[0] else None
                if w0 is not None:
                    w = w0 + bruit("bruit/" + nom, 0.15 * np.linalg.norm(w0))
                else:
                    w = rng("w/" + nom).normal(size=D)
                if fam == "mahalanobis":
                    classe = "SondeMahalanobis"           # absente du fichier léger, comme dans P3
                    emp = code["_empreinte_familles"](f"mahalanobis:{nom}", c, "max", np.zeros(D), np.eye(D))
                elif fam == "perceptron":
                    rr = rng("p/" + nom)
                    s = P(nom, c, "max", rr.normal(size=D), np.abs(rr.normal(size=D)) + 0.5, rr.normal(size=(4, D)),
                          rr.normal(size=4), rr.normal(size=4), float(rr.normal()), None, "perceptron")
                    sondes.append(s)
                    classe, emp = "SondePerceptron", s.empreinte()
                else:
                    q = rng("q/" + nom).normal(size=D) if fam == "attention" else None
                    s = S(nom, c, "attention" if fam == "attention" else "max", w, float(rng("b/" + nom).normal()), q, fam)
                    sondes.append(s)
                    classe, emp = "SondeLineaireJetons", s.empreinte()
                entrees_json.append({"agregation": "attention" if fam == "attention" else "max", "classe": classe,
                                     "couche": c, "empreinte": emp, "famille": fam, "nom": nom})
                aires[concept][nom] = 0.5
    planchers = {}
    entrees_planchers = []
    for concept in ("tromperie", "enjeux"):
        L = rng("L/" + concept).normal(size=(D, D)) / np.sqrt(D)
        planchers[concept] = []
        for k in range(N_PLANCHERS):
            nom = f"{princ[concept]}-plancher-plancher-{k}"
            s = S(nom, 15, "max", L @ rng(f"pl/{concept}/{k}").normal(size=D), 0.0, None, "plancher")
            sondes.append(s)
            planchers[concept].append(nom)
            entrees_planchers.append({"agregation": "max", "classe": "SondeLineaireJetons", "couche": 15,
                                      "empreinte": s.empreinte(), "famille": "plancher", "nom": nom})

    def ecrire_jeu(dossier: Path, garder: int, run_id: str):
        dossier.mkdir(parents=True, exist_ok=True)
        noms_gardes = {n for c in planchers for n in planchers[c][:garder]}
        ss = [s for s in sondes if s.famille != "plancher" or s.nom in noms_gardes]
        pl = {c: planchers[c][:garder] for c in planchers}
        sha_leg = code["ecrire_sondes"](dossier / "sondes-figees-legeres.npz", ss,
                                        {"principales": princ, "planchers": pl, "complet": "0" * 64})
        relues, meta, _ = code["lire_sondes"](dossier / "sondes-figees-legeres.npz", sha_leg)   # contrôle croisé
        assert len(relues) == len(ss) and meta["principales"] == princ
        fig = {"manifeste_sha256": "0" * 64, "run_id": run_id,
               "resultat": {"aires_validation": aires, "familles": familles, "principales": princ,
                            "sondes": entrees_json + [x for x in entrees_planchers if x["nom"] in noms_gardes],
                            "sondes_figees_sha256": "0" * 64, "sondes_legeres_sha256": sha_leg}}
        p = dossier / "sondes-figees.json"
        p.write_text(json.dumps(fig, ensure_ascii=False, indent=1), encoding="utf-8")
        sceller_simple(p)

    ecrire_jeu(e, N_PLANCHERS, "essai-factice-jlens-v2")
    ecrire_jeu(e / "peu-de-planchers", 20, "essai-factice-jlens-v2-peu-de-planchers")

    # Variantes facultatives : variances diagonales et activations moyennes factices
    with open(e / "variances-factices.npz", "wb") as f:
        np.savez(f, **{f"c{c}": 0.5 + rng(f"var{c}").random(D) for c in (7, 15, 23)})
    with open(e / "activations-moyennes-factices.npz", "wb") as f:
        np.savez(f, **{f"c{c}": 3.0 * rng(f"moy{c}").normal(size=D) for c in (7, 15, 23)})

    # Empreintes attendues (CLJ-04), avec une ligne fausse qui nomme le fichier lui-même (doit être ignorée)
    m = e / "modele"
    lignes = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in
              (e / "lentille-factice.npz", e / "lentille-config.yaml", m / "model-00001-of-00002.safetensors",
               m / "model-00002-of-00002.safetensors", m / "model.safetensors.index.json", m / "tokenizer.json")]
    (e / "empreintes-entrees-factices.txt").write_text("\n".join(lignes + ["0" * 64 + "  empreintes-entrees-factices.txt"])
                                                       + "\n", encoding="utf-8")
    return {"ids": ids, "jetons": jetons, "lignes_empreintes": lignes}


# ---------------------------------------------------------------- exécution et contrôles
def lancer(args, journal, cwd, torch_factice=False):
    if torch_factice:      # CLJ-05 : un torch dont load lève EOFError, comme torch.load sur un fichier vide
        amorce = ("import sys, types, runpy\nt = types.ModuleType('torch')\n"
                  "def load(*a, **k):\n    raise EOFError('Ran out of input')\n"
                  "t.load = load\nt.__version__ = 'factice'\nsys.modules['torch'] = t\n"
                  f"sys.argv = [{str(SCRIPT)!r}, *sys.argv[1:]]\nrunpy.run_path({str(SCRIPT)!r}, run_name='__main__')\n")
        cmd = [sys.executable, "-I", "-B", "-c", amorce, *args]
    else:
        cmd = [sys.executable, "-I", "-B", str(SCRIPT), *args]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    journal.append(f"$ python3 -I -B {'<amorce torch factice> ' if torch_factice else ''}{SCRIPT.name} {' '.join(args)}\n"
                   f"  code {r.returncode}\n  {(r.stdout + r.stderr).strip()[:1500]}")
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--depot", default=str(ICI.parents[5]))
    a = ap.parse_args()
    dossier, depot = Path(a.dossier).resolve(), Path(a.depot).resolve()
    if dossier.exists():
        raise SystemExit(f"{dossier} existe déjà (R12)")
    concepts = json.loads(CONCEPTS.read_text(encoding="utf-8"))
    e, s, alt = dossier / "entrees", dossier / "sortie", dossier / "altere"
    info = construire(e, depot, concepts)
    s.mkdir(parents=True)
    alt.mkdir()
    journal, controles = [], []

    def ok(nom, cond, detail=""):
        controles.append(f"{'OK' if cond else 'KO'}  {nom}{' — ' + detail if detail else ''}")

    m = e / "modele"
    base = ["comparer", "--sondes-json", str(e / "sondes-figees.json"), "--sondes-npz", str(e / "sondes-figees-legeres.npz"),
            "--lentille", str(e / "lentille-factice.npz"), "--lentille-config", str(e / "lentille-config.yaml"),
            "--desembedding", f"{m / 'model.safetensors.index.json'}:lm_head.weight",
            "--norme-finale", f"{m / 'model.safetensors.index.json'}:model.norm.weight",
            "--vocabulaire", str(m / "tokenizer.json"), "--concepts", str(CONCEPTS),
            "--empreintes-attendues", str(e / "empreintes-entrees-factices.txt"),
            "--revision-modele", "0e9e39f249a16976918f6564b8830bc894c89659"]

    def avec(liste, cle, valeur):
        l = list(liste)
        l[l.index(cle) + 1] = valeur
        return l

    def sans(liste, cle):
        l = list(liste)
        i = l.index(cle)
        return l[:i] + l[i + 2:]

    cwd = str(dossier)       # lancé depuis un autre dossier que celui du script
    r = lancer(base + ["--sortie", str(s / "sortie-factice-v2.json")], journal, cwd)
    ok("run sain : code 0", r.returncode == 0, r.stderr.strip()[:300])
    out = json.loads((s / "sortie-factice-v2.json").read_text(encoding="utf-8"))
    par_nom = {x["nom"]: x for x in out["sondes"]}
    ok("sondes retenues : famille de la principale × 3 couches × 2 concepts", sorted(par_nom) == sorted(
        [f"tromperie-difference_moyennes-c{c}" for c in (7, 15, 23)] + [f"enjeux-lineaire-c{c}" for c in (7, 15, 23)]))

    # --- Règle primaire (CLJ-02)
    rp = out["regle_primaire"]
    vd = {(v["sonde"], v["lentille"]): v for v in rp["verdicts"]}
    import importlib.util
    spec = importlib.util.spec_from_file_location("comparaison_v2", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ok("règle primaire : quatre verdicts (2 principales × 2 lentilles), complète, énoncé empreinté",
       len(rp["verdicts"]) == 4 and rp["complete"] is True
       and rp["empreinte_enonce"] == hashlib.sha256(mod.ENONCE_REGLE_PRIMAIRE.encode()).hexdigest(),
       f"empreinte de l'énoncé {rp['empreinte_enonce'][:16]}…")

    def fmt(v):
        return (f"S={v['S']}, q99 isotropes={v['quantile_0_99_isotropes']:g}, q99 planchers={v['quantile_0_99_planchers']:g}"
                f" (n={v['n_planchers']}) → {v['verdict']}")
    t_j, t_l = vd[("tromperie-difference_moyennes-c15", "jacobienne")], vd[("tromperie-difference_moyennes-c15", "logits")]
    ok("signal 1, tromperie c15 plantée sous J : jacobienne « cohérent », logits « non cohérent »",
       t_j["verdict"] == "cohérent" and t_l["verdict"] == "non cohérent", f"J : {fmt(t_j)} ; logits : {fmt(t_l)}")
    e_j, e_l = vd[("enjeux-lineaire-c15", "jacobienne")], vd[("enjeux-lineaire-c15", "logits")]
    ok("signal 2, enjeux c15 plantée en sortie : logits « cohérent », jacobienne « non cohérent »",
       e_l["verdict"] == "cohérent" and e_j["verdict"] == "non cohérent", f"logits : {fmt(e_l)} ; J : {fmt(e_j)}")
    r23 = par_nom["tromperie-difference_moyennes-c23"]["regle"]
    ok("signal 3, tromperie c23 (J ≈ identité), application descriptive : « cohérent » sous les deux lentilles, "
       "isotropes seules (pas de plancher à c23)",
       all(r23[l]["verdict_descriptif"] == "cohérent" and "statut" in r23[l]["planchers"] for l in ("logits", "jacobienne"))
       and "descriptif" in r23["logits"]["statut"],
       "; ".join(f"{l} : S={r23[l]['S']}, q99={r23[l]['isotropes']['quantile_0_99']:g}" for l in ("logits", "jacobienne")))
    r7 = [(n, l, par_nom[n]["regle"][l]) for n in ("tromperie-difference_moyennes-c7", "enjeux-lineaire-c7")
          for l in ("logits", "jacobienne")]
    ok("directions aléatoires (couche 7, deux sondes, deux lentilles) : « non cohérent » partout",
       all(x["verdict_descriptif"] == "non cohérent" for _, _, x in r7),
       "; ".join(f"{n.split('-')[0]} {l} S={x['S']} q99={x['isotropes']['quantile_0_99']:g}" for n, l, x in r7))
    spec_t = par_nom["tromperie-difference_moyennes-c15"]["regle"]["jacobienne"]["comptes_par_concept_diagnostic"]
    ok("spécificité (diagnostic) : la tête de tromperie c15 sous J porte peu de jetons d'enjeux (≤ 2)",
       spec_t["enjeux"] <= 2, str(spec_t))
    tete_t = par_nom["tromperie-difference_moyennes-c15"]["variantes"]["direction"]["jacobienne"]["plus"]["tete_debut_de_mot"]
    ok("la statistique S compte bien les jetons du concept dans la tête de début de mot affichée",
       t_j["S"] == sum(1 for t in tete_t if t["texte"][1:].lower() in set(concepts["tromperie"]))
       and all(t["texte"].startswith(" ") for t in tete_t))

    # --- Diagnostics (descriptifs) repris de la v1
    def dz(nom, lentille, concept):
        return par_nom[nom]["variantes"]["direction"][lentille]["diagnostics_z"][concept]
    t15j, t15l = dz("tromperie-difference_moyennes-c15", "jacobienne", "tromperie"), \
        dz("tromperie-difference_moyennes-c15", "logits", "tromperie")
    ok("diagnostic z, tromperie c15 sous J : p_haut ≤ 0,01 contre isotropes et contre les 200 planchers (CLJ-08)",
       t15j["isotropes"]["p_haut"] <= 0.01 and t15j["planchers"]["p_haut"] <= 0.01 and t15j["planchers"]["n"] == 200,
       f"z={t15j['z']:.2f}, p iso={t15j['isotropes']['p_haut']:.4f}, p planchers={t15j['planchers']['p_haut']:.4f}")
    ok("diagnostic z, tromperie c15 sous la lentille des logits : p bilatéral > 0,05",
       t15l["isotropes"]["p_bilateral"] > 0.05, f"z={t15l['z']:.2f}, p={t15l['isotropes']['p_bilateral']:.3f}")
    rec23 = par_nom["tromperie-difference_moyennes-c23"]["variantes"]["direction"]["recouvrement"]
    ok("tromperie c23 (J ≈ identité) : les deux lentilles s'accordent (≥ 12/20 en tête +, cosinus > 0,9)",
       rec23["plus"]["intersection"] >= 12 and rec23["cosinus_logits_centres"] > 0.9,
       f"intersection {rec23['plus']['intersection']}, cosinus {rec23['cosinus_logits_centres']:.3f}")
    ok("planchers lus à la couche 15 (200), absents aux couches 7 et 23",
       par_nom["tromperie-difference_moyennes-c15"]["regle"]["jacobienne"]["planchers"]["n"] == 200
       and "statut" in dz("tromperie-difference_moyennes-c7", "jacobienne", "tromperie")["planchers"])
    bloc = par_nom["enjeux-lineaire-c15"]["variantes"]["direction"]["logits"]
    ok("signe : têtes « plus » et « moins » disjointes, logits de tête de signes opposés",
       not ({t["id"] for t in bloc["plus"]["tete"]} & {t["id"] for t in bloc["moins"]["tete"]})
       and bloc["plus"]["tete"][-1]["logit"] > 0 and bloc["moins"]["tete"][-1]["logit"] > 0)

    # --- Vocabulaire et concepts (CLJ-03)
    textes, _ = mod.lire_vocabulaire(m / "tokenizer.json", V)
    toks = json.loads((m / "tokenizer.json").read_text(encoding="utf-8"))
    cle_cafe = encoder_bl(" café")
    ok("décodage par octets : « ĠcafÃ© » relu « café » avec l'espace",
       textes[toks["model"]["vocab"][cle_cafe]] == " café")
    jt = {j["texte"] for c in out["concepts"].values() for j in c["jetons"]}
    ok("concepts : seuls les jetons de début de mot comptent ; parasites et morceaux sans espace exclus ; casse libre",
       not (jt & set(PARASITES)) and "lie" not in jt and "risk" not in jt and " lie" in jt and " Lie" in jt
       and " Danger" in jt and all(t.startswith(" ") and not t.startswith("  ") for t in jt),
       f"{len(out['concepts']['tromperie']['jetons'])} jetons tromperie, {len(out['concepts']['enjeux']['jetons'])} enjeux")
    ok("concepts : chaque mot de la liste v2 a au moins un jeton",
       all(len(l) >= 1 for c in out["concepts"].values() for l in c["jetons_par_mot"].values()))

    # --- Manifeste (CLJ-09) et nombre de textes (CLJ-10)
    man = json.loads((s / "sortie-factice-v2-manifeste.json").read_text(encoding="utf-8"))
    ok("manifeste : commit (40 hexadécimaux), révision du modèle, empreinte de lentille-config.yaml, interpréteur complet",
       bool(re.fullmatch(r"[0-9a-f]{40}", man["depot"]["commit"]))
       and man["revision_modele"] == "0e9e39f249a16976918f6564b8830bc894c89659"
       and man["lentille_config"]["sha256"] == hashlib.sha256((e / "lentille-config.yaml").read_bytes()).hexdigest()
       and Path(man["interpreteur"]).is_absolute(),
       f"commit {man['depot']['commit'][:12]}…, état du script : {man['depot'].get('etat_du_script', '?')[:40]}")
    ok("manifeste : empreintes attendues conformes (ligne propre du fichier ignorée), sortie empreintée, graines",
       isinstance(man["empreintes_attendues"], dict) and set(man["empreintes_attendues"]["entrees"].values())
       <= {"conforme", "contrôlée par sceau compagnon", "contrôlée par sondes_legeres_sha256 de sondes-figees.json"}
       and man["sortie"]["sha256"] == hashlib.sha256((s / "sortie-factice-v2.json").read_bytes()).hexdigest()
       and "aleatoire/c15" in man["graines"])
    ok("CLJ-10 : « ajustée sur 461 textes » écrit d'après la configuration",
       out["lentille_ajustee_sur"].startswith("ajustée sur 461 textes"), out["lentille_ajustee_sur"])
    r2 = subprocess.run(["sha256sum", "-c", "sortie-factice-v2.json.sha256", "sortie-factice-v2-manifeste.json.sha256"],
                        cwd=s, capture_output=True, text=True)
    ok("empreintes compagnons vérifiables par sha256sum -c", r2.returncode == 0, r2.stdout.strip().replace("\n", " ; "))

    # --- Déterminisme, index renommé (CLJ-06), un seul couple (CLJ-07), sans configuration (CLJ-10)
    r = lancer(base + ["--sortie", str(s / "sortie-factice-v2-bis.json")], journal, cwd)
    ok("déterminisme : deuxième run, sortie identique octet pour octet", r.returncode == 0 and
       (s / "sortie-factice-v2.json").read_bytes() == (s / "sortie-factice-v2-bis.json").read_bytes())
    b_idx = avec(avec(sans(base, "--empreintes-attendues"), "--desembedding", f"{m / 'index.json'}:lm_head.weight"),
                 "--norme-finale", f"{m / 'index.json'}:model.norm.weight")
    r = lancer(b_idx + ["--sortie", str(s / "sortie-factice-v2-index-renomme.json")], journal, cwd)
    ok("CLJ-06 : index de fragments nommé « index.json » accepté (clé weight_map), sortie identique",
       r.returncode == 0 and (s / "sortie-factice-v2.json").read_bytes()
       == (s / "sortie-factice-v2-index-renomme.json").read_bytes(), r.stderr.strip()[:200])
    r = lancer(base + ["--un-seul-couple", "tromperie-difference_moyennes-c15,15",
                       "--sortie", str(s / "sortie-factice-v2-un-couple.json")], journal, cwd)
    o1 = json.loads((s / "sortie-factice-v2-un-couple.json").read_text(encoding="utf-8")) if r.returncode == 0 else None
    ok("CLJ-07 : --un-seul-couple : une sonde, identique à celle du run complet ; règle marquée incomplète",
       o1 is not None and len(o1["sondes"]) == 1 and o1["sondes"][0] == par_nom["tromperie-difference_moyennes-c15"]
       and o1["regle_primaire"]["complete"] is False and len(o1["regle_primaire"]["verdicts"]) == 2,
       r.stderr.strip()[:200])
    r = lancer(base + ["--un-seul-couple", "enjeux-lineaire,15", "--sortie", str(s / "sortie-factice-v2-un-couple-court.json")],
               journal, cwd)
    o2 = json.loads((s / "sortie-factice-v2-un-couple-court.json").read_text(encoding="utf-8")) if r.returncode == 0 else None
    ok("CLJ-07 : forme courte « enjeux-lineaire,15 » résolue en enjeux-lineaire-c15",
       o2 is not None and [x["nom"] for x in o2["sondes"]] == ["enjeux-lineaire-c15"], r.stderr.strip()[:200])
    b_sc = sans(sans(base, "--lentille-config"), "--empreintes-attendues")
    r = lancer(b_sc + ["--un-seul-couple", "enjeux-lineaire-c7,7", "--sortie", str(s / "sortie-factice-v2-sans-config.json")],
               journal, cwd)
    o3 = json.loads((s / "sortie-factice-v2-sans-config.json").read_text(encoding="utf-8")) if r.returncode == 0 else None
    m3 = json.loads((s / "sortie-factice-v2-sans-config-manifeste.json").read_text(encoding="utf-8")) if o3 else None
    ok("CLJ-10 : sans --lentille-config, « inconnu » ; manifeste « absente » ; empreintes « non contrôlées »",
       o3 is not None and o3["lentille_ajustee_sur"] == "inconnu" and m3["lentille_config"].startswith("absente")
       and m3["empreintes_attendues"].startswith("non contrôlées"), r.stderr.strip()[:200])

    # --- Variantes, toutes les sondes linéaires (fichiers de variantes hors du fichier d'empreintes attendues : on retire
    # l'option, sinon la garde CLJ-04 refuse à bon droit)
    r = lancer(sans(base, "--empreintes-attendues") + ["--covariances", str(e / "variances-factices.npz"), "--activations-moyennes",
                       str(e / "activations-moyennes-factices.npz"), "--sondes", "toutes-lineaires",
                       "--sortie", str(s / "sortie-factice-variantes-v2.json")], journal, cwd)
    ok("variantes « motif » et « autour », toutes les sondes linéaires : code 0", r.returncode == 0, r.stderr.strip()[:300])
    if r.returncode == 0:
        ov = json.loads((s / "sortie-factice-variantes-v2.json").read_text(encoding="utf-8"))
        pn = {x["nom"]: x for x in ov["sondes"]}
        ok("variantes : 18 sondes, trois variantes chacune ; les quatre verdicts primaires inchangés",
           len(ov["sondes"]) == 18 and all(set(x["variantes"]) == {"direction", "motif", "autour"} for x in ov["sondes"])
           and ov["regle_primaire"]["verdicts"] == rp["verdicts"])
        x = pn["enjeux-difference_moyennes-c15"]["regle"]
        ok("direction aléatoire à la couche 15 (enjeux-difference_moyennes-c15), avec planchers : « non cohérent » sous "
           "les deux lentilles", all(x[l]["verdict_descriptif"] == "non cohérent" and x[l]["planchers"]["n"] == 200
                                     for l in ("logits", "jacobienne")),
           "; ".join(f"{l} S={x[l]['S']}" for l in ("logits", "jacobienne")))

    # --- Vérification de la liste seule
    r = lancer(["verifier-concepts", "--vocabulaire", str(m / "tokenizer.json"), "--concepts", str(CONCEPTS)], journal, cwd)
    ok("verifier-concepts sur la liste v2 : code 0", r.returncode == 0, r.stdout.strip().splitlines()[-1][:120])

    # --- Refus nommés
    def refus(nom, args, code_attendu, contient=None, torch_factice=False):
        r = lancer(args, journal, cwd, torch_factice)
        cond = r.returncode == 2 and f"REFUS {code_attendu}" in r.stderr and (contient is None or contient in r.stderr)
        ok(f"refus {nom} : code 2 et « REFUS {code_attendu} »" + (f" nommant « {contient} »" if contient else ""), cond,
           r.stderr.strip()[:220])

    refus("entrée absente", avec(base, "--lentille", str(e / "absente.npz")) + ["--sortie", str(s / "x01.json")],
          "entree-absente")
    refus("couche absente de la lentille", avec(sans(base, "--empreintes-attendues"), "--lentille",
                                                str(e / "lentille-sans-c23.npz")) + ["--sortie", str(s / "x02.json")],
          "couche-absente-lentille")
    refus("lentille .pt sans torch", avec(base, "--lentille", str(e / "lentille-vide.pt")) + ["--sortie", str(s / "x03.json")],
          "torch-absent-pour-pt")
    refus("lentille .pt illisible, torch présent (CLJ-05)", avec(base, "--lentille", str(e / "lentille-vide.pt"))
          + ["--sortie", str(s / "x04.json")], "lentille-illisible", "EOFError", torch_factice=True)
    refus("largeur discordante", avec(sans(base, "--empreintes-attendues"), "--desembedding",
                                      str(e / "desembedding-largeur-fausse.npy")) + ["--sortie", str(s / "x05.json")],
          "dimension")
    refus("sortie existante", base + ["--sortie", str(s / "sortie-factice-v2.json")], "sortie-existe")
    b = bytearray((e / "sondes-figees-legeres.npz").read_bytes())
    b[len(b) // 2] ^= 1
    (alt / "sondes-figees-legeres.npz").write_bytes(bytes(b))
    refus("poids de sondes altérés", avec(base, "--sondes-npz", str(alt / "sondes-figees-legeres.npz"))
          + ["--sortie", str(s / "x06.json")], "empreinte-sondes-npz", "sondes_legeres_sha256")
    refus("empreinte passée par option et fausse (CLJ-06)", base + ["--sha256-sondes-npz", "f" * 64,
                                                                    "--sortie", str(s / "x07.json")],
          "empreinte-sondes-npz", "option --sha256-sondes-npz")
    fj = json.loads((e / "sondes-figees.json").read_text(encoding="utf-8"))
    fj["resultat"]["principales"]["enjeux"] = "enjeux-difference_moyennes-c15"
    (alt / "sondes-figees.json").write_text(json.dumps(fj, ensure_ascii=False, indent=1), encoding="utf-8")
    (alt / "sondes-figees.json.sha256").write_text((e / "sondes-figees.json.sha256").read_text())   # sceau périmé, exprès
    refus("sceau du JSON faux (JSON modifié, sceau ancien)", avec(base, "--sondes-json", str(alt / "sondes-figees.json"))
          + ["--sortie", str(s / "x08.json")], "sceau-faux")
    cj = json.loads(CONCEPTS.read_text(encoding="utf-8"))
    cj["tromperie"] = cj["tromperie"] + ["deceiving"]
    p_sj = alt / "concepts-mot-sans-jeton.json"
    p_sj.write_text(json.dumps(cj, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller_simple(p_sj)
    refus("mot sans jeton de début de mot (comparer)", avec(base, "--concepts", str(p_sj)) + ["--sortie", str(s / "x09.json")],
          "mot-sans-jeton", "deceiving")
    refus("mot sans jeton de début de mot (verifier-concepts)",
          ["verifier-concepts", "--vocabulaire", str(m / "tokenizer.json"), "--concepts", str(p_sj)],
          "mot-sans-jeton", "deceiving")
    p_ns = alt / "concepts-sans-sceau.json"
    p_ns.write_text(CONCEPTS.read_text(encoding="utf-8"), encoding="utf-8")
    refus("liste de mots sans sceau compagnon", avec(base, "--concepts", str(p_ns)) + ["--sortie", str(s / "x10.json")],
          "sceau-absent")
    refus("configuration de lentille discordante (CLJ-10)",
          avec(sans(base, "--empreintes-attendues"), "--lentille-config", str(e / "lentille-config-discordante.yaml"))
          + ["--sortie", str(s / "x11.json")], "lentille-config-discordante")
    lignes = info["lignes_empreintes"]
    p_ef = alt / "empreintes-fausses.txt"
    p_ef.write_text("\n".join(l if not l.endswith("tokenizer.json") else "a" * 64 + "  tokenizer.json" for l in lignes)
                    + "\n", encoding="utf-8")
    refus("empreinte attendue fausse (CLJ-04)", avec(base, "--empreintes-attendues", str(p_ef))
          + ["--sortie", str(s / "x12.json")], "empreinte-entree", "tokenizer.json")
    p_ea = alt / "empreintes-incompletes.txt"
    p_ea.write_text("\n".join(l for l in lignes if not l.endswith("tokenizer.json")) + "\n", encoding="utf-8")
    refus("empreinte attendue absente (CLJ-04)", avec(base, "--empreintes-attendues", str(p_ea))
          + ["--sortie", str(s / "x13.json")], "empreinte-attendue-absente", "tokenizer.json")
    pp = e / "peu-de-planchers"
    refus("planchers insuffisants pour la règle primaire (20 < 100)",
          avec(avec(base, "--sondes-json", str(pp / "sondes-figees.json")), "--sondes-npz",
               str(pp / "sondes-figees-legeres.npz")) + ["--sortie", str(s / "x14.json")], "planchers-insuffisants")
    refus("--un-seul-couple, couche fausse", base + ["--un-seul-couple", "tromperie-difference_moyennes-c15,23",
                                                     "--sortie", str(s / "x15.json")], "sonde-introuvable")
    refus("--un-seul-couple, forme fausse", base + ["--un-seul-couple", "tromperie-difference_moyennes-c15",
                                                    "--sortie", str(s / "x16.json")], "parametre")
    refus("JSON de poids sans weight_map (CLJ-06)", avec(sans(base, "--empreintes-attendues"), "--desembedding",
                                                         f"{m / 'tokenizer.json'}:lm_head.weight")
          + ["--sortie", str(s / "x17.json")], "poids-illisibles", "weight_map")
    absents = [p.name for p in s.iterdir() if re.match(r"x\d", p.name)]
    ok("aucun refus n'a laissé de sortie", not absents, str(absents))

    ko = [c for c in controles if c.startswith("KO")]
    texte = (f"Essai factice v2 — largeur {D}, vocabulaire {V}, {N_PLANCHERS} planchers, graine {GRAINE}\n"
             f"Dépôt (code extrait) : {depot}\n\n" + "\n".join(controles)
             + f"\n\nBILAN : {len(controles) - len(ko)}/{len(controles)} contrôles OK\n\n--- commandes ---\n"
             + "\n".join(journal) + "\n")
    texte = texte.replace(str(dossier), "<essai>").replace(str(ICI), "<dossier>").replace(str(depot), "<depot>")
    (dossier / "journal-essai-factice-v2.txt").write_text(texte, encoding="utf-8")
    print(texte.split("--- commandes ---")[0])
    return 1 if ko else 0


if __name__ == "__main__":
    sys.exit(main())
