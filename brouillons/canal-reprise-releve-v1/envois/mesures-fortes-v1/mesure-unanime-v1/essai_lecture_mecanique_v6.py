"""Essai **déposé** de la lecture mécanique v5 (CV7-4, CV8-6) : à partir de l'essai synthétique v8 (sortie brute, jamais retouchée à la
main), des copies modifiées en mémoire exercent les neuf feuilles de M2 ter, les six audits (M3, M2 contrôle, M2 bis réfutée, maximum de M4,
placebo, cellule de M3 à zéro) qui suspendent la ligne, la réserve des bras à zéro, les bornes exactes, la réfutation de
M2 bis, et les refus du manifeste. Sortie : un JSON brut écrit par ce script seul.

Usage : python -I -B essai_lecture_mecanique_v6.py SORTIE_SYNTHETIQUE.json TABLE.json > essai-lecture-mecanique-v6.json
"""
import copy
import importlib.util
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("lm", os.path.join(ICI, "lecture_mecanique_v6.py"))
lm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lm)


def main():
    base = json.load(open(sys.argv[1], encoding="utf-8"))
    table_fichier = json.load(open(sys.argv[2], encoding="utf-8"))
    table, tm = table_fichier["table"], table_fichier.get("manifeste", {})
    out = {"sources": {"sortie": sys.argv[1], "table": sys.argv[2]}, "brut": lm.lire(base, table, table_manifeste=tm), "feuilles": [], "audits": {}, "divers": {}}

    def cas(v0, vm, vmp, bbD, bbDp, bbDd=-0.01):
        d = copy.deepcopy(base); r = d["resultats"]
        r["tau=0.0"]["ville:processus_e"]["reelles"]["mediane"] = v0
        r["melange_actions_permutees_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vm
        r["melange_pas_fixe_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vmp
        r["ville_tau0_reelles_moins_melange"]["intervalle_95"] = [bbD, bbD + 0.05]
        r["ville_tau0_reelles_moins_melange_pas_fixe"]["intervalle_95"] = [bbDp, bbDp + 0.05]
        r["ville_tau0_melange_pas_fixe_moins_melange"]["intervalle_95"] = [bbDd, bbDd + 0.05]
        return lm.lire(d, table, table_manifeste=tm)["verdicts"]["M2_ter"]
    for args in [(0.03, 0, 0, 0.01, 0.01), (0.08, 0.06, 0, -0.01, 0), (0.08, 0.01, 0, -0.01, 0), (0.08, 0.06, 0, 0.01, 0.01), (0.08, 0.06, 0, 0.01, -0.01),
                 (0.08, 0.01, 0.01, 0.01, 0.01), (0.08, 0.01, 0.07, 0.01, 0.01), (0.08, 0.01, 0.01, 0.01, -0.01, 0.01), (0.08, 0.01, 0.01, 0.01, -0.01, -0.01)]:
        out["feuilles"].append({"entrees": list(args), "feuille": cas(*args)})
    assert len({f["feuille"] for f in out["feuilles"]}) == 9
    # audits : chacun suspend la ligne
    def audit(nom, modif):
        d = copy.deepcopy(base); modif(d["resultats"])
        l = lm.lire(d, table, table_manifeste=tm)
        out["audits"][nom] = {"audits": l["audits"], "ligne": l["ligne_de_lecture"][:80], "verdict": {k: l["verdicts"][k] for k in l["audits"]}}
    audit("M3_cellule_sup_B", lambda r: r["tau=0.0"]["conforme:max"]["reelles"].__setitem__("mediane", 0.3))
    audit("M2_controle", lambda r: r["tau=2.0"]["ville:processus_e"]["reelles"].__setitem__("mediane", 0.02))
    audit("M4_max", lambda r: r["M4_dependance_seule_variance_constante_tau=2"]["conforme:max"]["reelles"].__setitem__("mediane", 0.12))
    audit("placebo", lambda r: r["tau=0.0"]["conforme:max"]["placebos"].__setitem__("mediane", 0.3))
    def zero(r):
        r["tau=0.0"]["conforme:page"]["reelles"]["mediane"] = 0.0; r["tau=0.0"]["conforme:page"]["reelles"]["q3"] = 0.0
    audit("cellule_M3_a_zero", zero)
    for nom, info in out["audits"].items():
        assert info["audits"] and info["ligne"].startswith("AUDIT"), nom
    # réserve : bras à zéro
    d = copy.deepcopy(base); d["resultats"]["M4_dependance_seule_variance_constante_tau=2"]["conforme:max"]["reelles"].update({"mediane": 0.0, "q3": 0.0})
    l = lm.lire(d, table, table_manifeste=tm); out["divers"]["bras_a_zero"] = {"reserves": l["reserves"], "audits": l["audits"]}
    # bornes exactes
    d = copy.deepcopy(base); d["resultats"]["M4_exces_apparie"]["exces"] = 0.02 + 1e-12
    out["divers"]["exces_exactement_0_02"] = lm.lire(d, table, table_manifeste=tm)["verdicts"]["M4"]
    # M2 bis réfutée
    d = copy.deepcopy(base); d["resultats"]["ville_tau2_moins_tau0"]["intervalle_95"] = [-0.05, -0.001]; d["resultats"]["ville_tau2_moins_tau0"]["mediane"] = -0.02
    out["divers"]["M2_bis_refutee"] = lm.lire(d, table, table_manifeste=tm)["verdicts"]["M2_bis"]
    # refus du manifeste
    refus = {}
    for nom, modif in {"autre_script": lambda m: m.__setitem__("script", "analyse_fausses_alertes_v7.py"),
                       "E_table_different": None,
                       "empreinte_script": "x"}.items():
        d = copy.deepcopy(base)
        try:
            if nom == "E_table_different":
                lm.lire(d, table, table_manifeste={"E": 50})
            elif nom == "empreinte_script":
                lm.lire(d, table, table_manifeste=tm, empreinte_script="attendue-autre")
            else:
                modif(d["manifeste"]); lm.lire(d, table, table_manifeste=tm)
            refus[nom] = "PAS DE REFUS"
        except SystemExit as e:
            refus[nom] = f"refus : {e}"
    # CV8-6 : refus propres au mode réel (tirages, rééchantillonnages, commit) sur une sortie au format réel
    reel = copy.deepcopy(base); reel["manifeste"]["synthetique"] = False; reel["manifeste"]["tirages"] = 20; reel["manifeste"]["bootstrap"] = 2000; reel["manifeste"]["commit"] = "abc"
    for nom, modif in {"tirages_hors_fixe": lambda m: m.__setitem__("tirages", 5), "bootstrap_hors_fixe": lambda m: m.__setitem__("bootstrap", 300),
                       "commit_absent": lambda m: m.__setitem__("commit", None)}.items():
        d = copy.deepcopy(reel); modif(d["manifeste"])
        try:
            lm.lire(d, table, table_manifeste=tm); refus[nom] = "PAS DE REFUS"
        except SystemExit as e:
            refus[nom] = f"refus : {e}"
    lm.lire(reel, table, table_manifeste=tm)  # cas sain : manifeste réel conforme accepté
    # CV8-3 : M2 bis réfutée = audit qui suspend
    d = copy.deepcopy(base); d["resultats"]["ville_tau2_moins_tau0"]["intervalle_95"] = [-0.05, -0.001]; d["resultats"]["ville_tau2_moins_tau0"]["mediane"] = -0.02
    l = lm.lire(d, table, table_manifeste=tm); out["audits"]["M2_bis_refutee"] = {"audits": l["audits"], "ligne": l["ligne_de_lecture"][:80]}
    assert "M2_bis" in l["audits"] and l["ligne_de_lecture"].startswith("AUDIT")
    # CV8-4 : (2a) avec D′ > 0 → réserve
    d = copy.deepcopy(base); r_ = d["resultats"]
    r_["tau=0.0"]["ville:processus_e"]["reelles"]["mediane"] = 0.08; r_["melange_actions_permutees_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = 0.06
    r_["ville_tau0_reelles_moins_melange"]["intervalle_95"] = [-0.01, 0.04]; r_["ville_tau0_reelles_moins_melange_pas_fixe"]["intervalle_95"] = [0.01, 0.06]
    l = lm.lire(d, table, table_manifeste=tm); out["divers"]["2a_avec_Dprime_positive"] = {"feuille": l["verdicts"]["M2_ter"], "reserves": l["reserves"]}
    assert l["reserves"]
    out["divers"]["refus_manifeste"] = refus
    assert all(v.startswith("refus") for v in refus.values())
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
