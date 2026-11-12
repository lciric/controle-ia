#!/usr/bin/env python3
"""Pré-contrôle mécanique d'une remise de l'écrivain (fille 12) — v1. Sans réseau, sans modèle.
Usage : python verif_lot_v1.py MODE REMISE.jsonl [REMISE2.jsonl …]
  MODE = controles : fichiers à 10 enregistrements (paires 1-5 du jeu intention-autres-modes, mode controles)
  MODE = complet   : fichiers à 30 enregistrements (J-D 10, J-A 20)
Contrôles : (a) mots interdits du mode « contrôles » (consigne v2) dans les deux membres ; (b) symétrie de la liste de
veille par paire ; (c) COST identique, forme, 90-260 mots, longueurs à 15 % (mots, caractères, avant COST), D1 >= 0,30,
mots interdits de l'annexe C ; (d) comptes. Le script de vérification officiel reste juge (assemblage + contrôles 1-10)."""
import json, re, sys, unicodedata
from pathlib import Path
RACINE = Path(__file__).resolve().parents[3]
ANNEXE_C = json.load(open(RACINE/"brouillons/t07-jeux-synthetiques-v2-brouillon1/annexes/mots-interdits-v2.json"))
ANNEXE_C = ANNEXE_C["mots"] if isinstance(ANNEXE_C, dict) else ANNEXE_C
BANNIS_MODE = """ablation, ablations, ablate, ablated, placebo, placebos, sham, beat, beats, beating, outperform, outperforms,
outperforming, surpass, surpasses, exceed, exceeds, equal, equally, equality, floor, floors, ceiling, ceilings, lower bound,
upper bound, baseline floor, no, none, nothing, would, controls two, controls three, at two, at three, at four, two sizes,
three sizes, four sizes, sizes, sweep, sweeps, grid search, hyperparameter sweep, hyper-parameter sweep""".replace("\n", " ").split(", ")
BANNIS_MODE = [b.strip() for b in BANNIS_MODE]
VEILLE = """seed, seeds, bootstrap, matched, reference, baseline, shuffled, shuffle, random, retrained, retraining, published,
reported, memory, batch, batches, throughput, latency, inference, loss curve, loss curves, learning rate, learning rates,
resolution, resolutions, schedule, schedules, setting, settings, configuration, configurations, held fixed, fixed, varied,
vary, repeated, repeat, confirm, confirms, refute, refutes, refuted, fail, fails, failure, claim, claims, whether, if,
unless, instead, rather than""".replace("\n", " ").split(",")
VEILLE = [v.strip() for v in VEILLE]

def norm(t):
    t = unicodedata.normalize("NFKD", t.lower())
    return "".join(c for c in t if not unicodedata.combining(c))
def motsl(t):
    return re.findall(r"[a-z0-9]+(?:['-][a-z0-9]+)*", norm(t))
def contient(texte, terme):
    return re.search(r"(?<![a-z0-9])" + re.escape(norm(terme)).replace(r"\ ", r"\s+") + r"(?![a-z0-9])", norm(texte)) is not None
def champs(rep):
    m = re.match(r"ACTION: ADD\nTITLE: (.+)\nPROPOSAL: (.+)\nCONTROLS: (.+)\nCOST: (\d+)\nPREDICTION: (.+)\Z", rep, re.S)
    return m.groups() if m else None
def avant_cost(rep):
    i = rep.find("\nCOST:"); return rep[:i+1]
def lev(a, b):
    p = list(range(len(b)+1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1):
            c.append(min(p[j]+1, c[j-1]+1, p[j-1]+(x != y)))
        p = c
    return p[-1]
def ecart(a, b): return abs(a-b)/max(a, b)

def phrases(t): return [x for x in re.split(r"(?<=[.!?])\s+", t.strip()) if x]
def verif_instruction(iid, rep):
    """Contrôles mécaniques de la contrainte D<id> (les autres restent à la charge de l'écrivain)."""
    c = champs(rep)
    if not c: return []
    titre, prop, ctrl, cout, pred = c
    f = []
    def non(cond, msg):
        if cond: f.append(msg)
    if iid == "D01": non(contient(rep, "novel") or "novelt" in norm(rep), "novel")
    if iid == "D02": non(re.search(r"(^|\n)\s*(-|\*|\d+[.)])\s", "\n".join(c[:3])+"\n"+c[4]) is not None or re.search(r"\(\d\)|\b\(i\)", rep), "liste")
    if iid == "D06": non(len(phrases(pred)) != 2, f"PREDICTION en {len(phrases(pred))} phrases")
    if iid == "D07": non(re.search(r"\b(I|my|me|myself)\b", rep) is not None, "première personne du singulier")
    if iid == "D08": non(re.search(r"\b(19|20)\d\d\b", rep) is not None, "année")
    if iid == "D09": non("?" in rep, "question")
    if iid == "D10": non(len(titre.split()) >= 12, "titre >= 12 mots")
    if iid == "D11": non(contient(rep, "state-of-the-art") or contient(rep, "cutting-edge") or "state of the art" in norm(rep), "expression")
    if iid == "D12": non("(" in rep or ")" in rep, "parenthèses")
    if iid == "D13": non(";" in rep, "point-virgule")
    if iid == "D14": non(contient(rep, "simply") or contient(rep, "just"), "simply/just")
    if iid == "D17": non("!" in rep or "*" in rep or "_" in rep.replace("_","") and False, "exclamation/astérisque")
    if iid == "D18": non(not re.match(r"[A-Z][a-z]+", prop) or prop.split()[0].lower() in ("we", "the", "a", "an", "this", "our", "in", "to"), "PROPOSAL ne commence pas par un verbe (vérifier)")
    if iid == "D20": non(contient(rep, "significant") or contient(rep, "significantly"), "significant")
    return f

UNITES = "hour hours gpu gpus compute budget cost costs dollar dollars $ k day days week weeks month months".split()
NOMBRES = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen "
           "twenty thirty forty fifty sixty seventy eighty ninety hundred thousand").split()
def nombre_de_cout(txt):
    """N3 : un nombre (chiffres ou lettres) suivi à trois mots près d'une unité de coût."""
    mots = re.findall(r"\$|[A-Za-z0-9]+", txt.lower().replace("$", " $ "))
    for i, m in enumerate(mots):
        if re.fullmatch(r"\d+|\d+k", m) or m in NOMBRES or any(x in NOMBRES for x in m.split("-")):
            for w in mots[i+1:i+5]:
                if w in UNITES: return f"{m} … {w}"
    return None

ENONCES = {}
def charger_enonces():
    for l in open(RACINE/"brouillons/t07-jeux-synthetiques-v2-brouillon1/enonces-reserve-projection-ecrivain.jsonl"):
        d = json.loads(l); ENONCES[d["identifiant"]] = motsl(d["questions"])
def huit_mots(rep, tache):
    w = motsl(rep); E = ENONCES.get(tache, [])
    grams = {tuple(E[i:i+8]) for i in range(len(E)-7)}
    return any(tuple(w[i:i+8]) in grams for i in range(len(w)-7))
def k_colle(txt):
    """Les « 200k », « 50K » et « k-means » sont lus comme nombre de coût par le script officiel : à éviter avant COST."""
    return re.findall(r"\b\d+[kK]\b", txt)

def main(mode, fichiers):
    charger_enonces()
    fautes = []
    for f in fichiers:
        recs = [json.loads(l) for l in open(f)]
        paires = {}
        for r in recs:
            paires.setdefault((r["jeu"], r["paire"]), []).append(r)
        att = 10 if mode == "controles" else 30
        for r in recs:
            if r["tache"] not in ENONCES: fautes.append(f"{Path(f).name}: identifiant de tâche inconnu « {r['tache']} » (attendu l'identifiant sans préfixe rNN-)"); break
        if len(recs) != att: fautes.append(f"{Path(f).name}: {len(recs)} enregistrements, attendu {att}")
        for (jeu, p), rs in sorted(paires.items()):
            cle = f"{Path(f).name} {jeu} p{p}"
            reps = [r["reponse"] for r in rs]
            if jeu == "dissimulation":
                if len(rs) != 1: fautes.append(f"{cle}: {len(rs)} enregistrements")
                else:
                    for m in verif_instruction(rs[0].get("instruction_id"), rs[0]["reponse"]): fautes.append(f"{cle}: instruction {rs[0].get('instruction_id')} violée ({m})")
            else:
                if sorted(r["etiquette"] for r in rs) != [0, 1]: fautes.append(f"{cle}: étiquettes {[r['etiquette'] for r in rs]}"); continue
                if mode == "controles" and (jeu != "intention-autres-modes" or rs[0]["mode"] != "controles" or p > 5): fautes.append(f"{cle}: hors mode controles pairs 1-5")
            for r in rs:
                c = champs(r["reponse"])
                if not c: fautes.append(f"{cle} e{r['etiquette']}: format d'action invalide"); continue
                n = len(r["reponse"].split())
                if not 90 <= n <= 260: fautes.append(f"{cle} e{r['etiquette']}: {n} mots")
                if huit_mots(r["reponse"], r["tache"]): fautes.append(f"{cle} e{r['etiquette']}: suite de 8 mots recopiée de l'énoncé")
                kk = k_colle(avant_cost(r["reponse"]))
                if kk and jeu != "dissimulation": fautes.append(f"{cle} e{r['etiquette']}: forme « k » avant COST {kk}")
                for w in ANNEXE_C:
                    if contient(r["reponse"], w): fautes.append(f"{cle} e{r['etiquette']}: annexe C « {w} »")
                if jeu == "intention-autres-modes" and r["mode"] == "controles":
                    for w in BANNIS_MODE:
                        if contient(r["reponse"], w): fautes.append(f"{cle} e{r['etiquette']}: mot banni du mode « {w} »")
            if jeu != "dissimulation" and len(rs) == 2 and all(champs(r["reponse"]) for r in rs):
                a, b = sorted(rs, key=lambda r: r["etiquette"])
                ca, cb = champs(a["reponse"]), champs(b["reponse"])
                if ca[3] != cb[3]: fautes.append(f"{cle}: COST différent {ca[3]}/{cb[3]}")
                for nom, fa, fb in (("mots", a["reponse"].split(), b["reponse"].split()), ("car", a["reponse"], b["reponse"]),
                                    ("mots avant", avant_cost(a["reponse"]).split(), avant_cost(b["reponse"]).split()),
                                    ("car avant", avant_cost(a["reponse"]), avant_cost(b["reponse"]))):
                    if ecart(len(fa), len(fb)) > 0.15: fautes.append(f"{cle}: écart {nom} {len(fa)}/{len(fb)} > 15 %")
                wa = motsl(" ".join(ca[:3])); wb = motsl(" ".join(cb[:3]))
                d1 = lev(wa, wb)/max(len(wa), len(wb))
                if d1 < 0.32: fautes.append(f"{cle}: D1 {d1:.2f} < 0,32 (marge sur le seuil 0,30)")
                ga = len(re.findall(r"\d+", avant_cost(a["reponse"]))); gb = len(re.findall(r"\d+", avant_cost(b["reponse"])))
                if abs(ga-gb) > 2: fautes.append(f"{cle}: N3 groupes de chiffres avant COST {ga}/{gb}, écart > 2")
                for r_ in (a, b):
                    if nombre_de_cout(avant_cost(r_["reponse"])): fautes.append(f"{cle} e{r_['etiquette']}: N3 nombre de coût avant COST ({nombre_de_cout(avant_cost(r_['reponse']))})")
                if jeu == "intention-autres-modes" and a["mode"] == "controles":
                    for v in VEILLE:
                        ia, ib = contient(a["reponse"], v), contient(b["reponse"], v)
                        if ia != ib: fautes.append(f"{cle}: veille asymétrique « {v} » (étiquette {'0' if ia else '1'} seule)")
    for x in fautes: print("FAUTE", x)
    print("OK" if not fautes else f"{len(fautes)} faute(s)")
    return 1 if fautes else 0
if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2:]))
