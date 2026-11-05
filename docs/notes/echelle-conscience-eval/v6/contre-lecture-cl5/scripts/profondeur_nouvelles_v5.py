"""cl5 : réserves « profondeur » nouvelles de l'analyse v5 (CLW-02) calculées sur quatre couches, par `principal`
(et non sur un drapeau fabriqué) : pour « nul », « pas de fuite » et « fuite de signe inverse », un cas sain (même λ aux
quatre profondeurs) et un artefact (trois profondeurs sur quatre qui contredisent l'issue lue à L*). Générateur des
tests v5 (`fabriquer` de test_analyser_echelle_v5.py, importé tel quel). Mode répétition, 300 tirages. Lecture seule de
l'arbre ; sorties dans le bac à sable.
Usage : python -I -B profondeur_nouvelles_v5.py DOSSIER_NEUF
"""
import importlib.util
import json
import pathlib
import sys

ARBRE = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v5")
spec = importlib.util.spec_from_file_location("t", ARBRE / "tests" / "test_analyser_echelle_v5.py")
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
AN = T.AN
AN.N_BOOT = 300
STIMULI = ARBRE / "stimuli" / "echelle-v2.json"
COUCHES = (2, 3, 4, 6)          # L* attendue : 6 (contexte deux fois plus fort qu'aux trois autres)

# nom : (alpha petit à L*, alpha grand à L*, alpha petit aux trois autres, alpha grand aux trois autres, issue visée)
CAS = {
    "nul sain": (0.5, 0.5, 0.5, 0.5, "nul"),
    "nul artefact (Δλ 0,8 aux trois autres)": (0.5, 0.5, 1.0, 0.2, "nul"),
    "pas de fuite sain": (0.0, 0.0, 0.0, 0.0, "pas de fuite"),
    "pas de fuite artefact (λ petit 0,6 aux trois autres)": (0.0, 0.0, 0.6, 0.0, "pas de fuite"),
    "fuite de signe inverse saine": (-0.8, 0.0, -0.8, 0.0, "fuite de signe inverse"),
    "fuite de signe inverse artefact (λ petit +0,5 aux trois autres)": (-0.8, 0.0, 0.5, 0.0, "fuite de signe inverse"),
}


def principal(argv):
    racine = pathlib.Path(argv[0])
    racine.mkdir(parents=True)
    AN.ATTENDUS = {k: {**v, "couches": list(COUCHES)} for k, v in T.PETITS.items()}
    for k, (ap, ag, ap3, ag3, vise) in enumerate(CAS.items() and CAS.values()):
        nom = list(CAS)[k]
        d = racine / f"cas-{k}"
        p = T.fabriquer(d / "p", STIMULI, ap, 500 + 2 * k, couches=COUCHES,
                        alpha_couches={2: ap3, 3: ap3, 4: ap3, 6: ap})
        g = T.fabriquer(d / "g", STIMULI, ag, 501 + 2 * k, nom="grand", couches=COUCHES,
                        alpha_couches={2: ag3, 3: ag3, 4: ag3, 6: ag})
        code = AN.principal([str(STIMULI), str(p), str(g), "12345", str(d / "s"), "--repetition"])
        r = json.loads((d / "s" / "analyse-echelle-v5.json").read_text(encoding="utf-8")) if code == 0 else {}
        print(json.dumps({"cas": nom, "code": code, "lecture": r.get("lecture"), "reserves": r.get("reserves"),
                          "couches": {m: r[m]["couche"] for m in ("petit", "grand")} if r else None,
                          "profondeur_contraire_vise": r.get("profondeur_contraire", {}).get(vise),
                          "lambda_par_couche_petit_ab": r.get("petit", {}).get("lambda_par_couche", {}).get("ab"),
                          "delta_lambda_par_profondeur": r.get("delta_lambda_par_profondeur")},
                         ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
