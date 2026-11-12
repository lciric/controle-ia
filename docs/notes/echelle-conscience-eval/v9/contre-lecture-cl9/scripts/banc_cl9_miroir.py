"""Banc cl9 (contre-lecture du brouillon v9-2) : vrai miroir de la famille D de cl7 sous une composante propre à un jeu.
Famille D (cl7, cl8) : fuite égale, contexte du jeu b PLUS FORT (k > 1), composante dans le jeu a, qui ramène q près
de 1 : « inverse » sous H_0. Miroir en signe : contexte du jeu b PLUS FAIBLE (k < 1), composante dans le jeu b (qui
ramène q près de 1), signature positive du jeu b au petit, négative du jeu a au grand : « positif » attendu sous H_0,
avec e(m) ≈ 0 (le terme α(1/k − 1) compense les signatures croisées).
Générateur : `fabriquer` de `banc_cl8_commun.py` (copie versée de cl8, empreinte 20835d6e…), qui rend à l'octet la
simulation scellée sans composante ; analyse v8 du commit TELLE QUELLE (mode répétition), sauf `etat_scripts`
remplacé par une constante pour qu'aucun appel git ne touche l'arbre de travail (sans effet en répétition).
    python -I -B banc_cl9_miroir.py SORTIE_JSONL PROCESSUS N_BOOT SCENARIO:GRAINE0:N [...]"""
import importlib.util, json, multiprocessing, pathlib, sys, tempfile
ICI = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("bz", ICI / "banc_cl8_commun_copie.py")
BZ = importlib.util.module_from_spec(spec); spec.loader.exec_module(BZ)
AN = BZ.AN
AN.etat_scripts = lambda: ("9ccc383c02a08e58928368b23471f4c438e06cda (non relu)", None)
O = BZ.O
SC = {
    # témoin : sans composante, contexte du jeu b × 0,6 : la réserve « contexte inégal » doit sonner
    "M_temoin_sans_composante": (0.7, 0.7, O(contexte_b=0.6, signature_b=0.32), O(contexte_b=0.6, signature=-0.8), 0.15),
    # miroir : composante dans b (norme 3,2), contexte du jeu b × 0,6, fuite égale 0,7 (H_0)
    "M_cb32_k0.6": (0.7, 0.7, O(commun_b=3.2, contexte_b=0.6, signature_b=0.32),
                    O(commun_b=3.2, contexte_b=0.6, signature=-0.8), 0.15),
    # composante seule (H_0, fuite égale, sans signature) : q ramené près de 1 sous k = 0,6 ?
    "M_cb32_k0.6_sans_signature": (0.7, 0.7, O(commun_b=3.2, contexte_b=0.6), O(commun_b=3.2, contexte_b=0.6), 0.15),
}
def un(t):
    nom, g, nboot = t
    a8, a70, o8, o70, tau = SC[nom]
    st = json.loads(BZ.STIM.read_text(encoding="utf-8"))["stimuli"]
    AN.N_BOOT = nboot
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)
        BZ.fabriquer(base / "p", BZ.STIM, st, a8, g, tau, **o8)
        BZ.fabriquer(base / "g", BZ.STIM, st, a70, g + 1, tau, **o70)
        code = AN.principal([str(BZ.STIM), str(base / "p"), str(base / "g"), str(g), str(base / "s"), "--repetition"])
        if code != 0:
            return {"scenario": nom, "graine": g, "code": code}
        r = json.loads((base / "s" / "analyse-echelle-v8.json").read_text(encoding="utf-8"))
    return {"scenario": nom, "graine": g, "n_boot": r["n_boot"],
            "lecture": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
            "reserves": r["reserves"], "lecture_par_sens": r["lecture_par_sens"],
            "e": {k: round(v, 3) for k, v in r["ecart_sens"].items()},
            "e_ic": {k: [round(x, 3) for x in v] for k, v in r["ecart_sens_ic"].items()},
            "q": {k: (None if v is None else round(v, 3)) for k, v in r["rapport_Ec"].items()},
            "q_ic": {k: [round(x, 3) for x in v] for k, v in r["rapport_Ec_ic"].items()},
            "lambda": {s: [round(r[m][s]["lambda"], 3) for m in ("petit", "grand")] for s in ("ab", "ba")},
            "lambda_ic": {s: [[round(x, 3) for x in r[m][s]["lambda_ic"]] for m in ("petit", "grand")] for s in ("ab", "ba")},
            "dl_ic": {s: [round(x, 3) for x in r["delta_lambda_ic"][s]] for s in ("ab", "ba")},
            "spec_ic": {s: [round(x, 3) for x in r["specificite_ic"][s]] for s in ("ab", "ba")},
            "cert": {s: [round(r[m][s]["A_ctx_fixe_ic"][0], 3) for m in ("petit", "grand")] for s in ("ab", "ba")},
            "couches": {m: r[m]["couche"] for m in ("petit", "grand")},
            "sha256_analyse": r["sha256_script"]}
def principal(argv):
    sortie, processus, nboot = pathlib.Path(argv[0]), int(argv[1]), int(argv[2])
    if sortie.exists(): sys.exit("sortie présente (R12)")
    travaux = []
    for x in argv[3:]:
        nom, g0, n = x.split(":")
        travaux += [(nom, int(g0) + 2 * j, nboot) for j in range(int(n))]
    with multiprocessing.get_context("fork").Pool(processus) as pool, open(sortie, "w", encoding="utf-8") as f:
        for ligne in pool.imap(un, travaux, chunksize=1):
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n"); f.flush()
    return 0
if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
