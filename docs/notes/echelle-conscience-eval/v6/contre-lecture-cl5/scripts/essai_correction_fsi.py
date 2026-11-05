"""cl5 : essai, sur des intervalles fabriqués, de la correction proposée pour CLV-01 (« fuite de signe inverse » exigée
pour le MÊME modèle dans les deux sens). La règle est substituée dans une copie du module chargée en mémoire ; l'arbre
de travail n'est pas modifié. Comparaison : lecture v5 telle quelle, puis lecture corrigée.
Usage : python -I -B essai_correction_fsi.py
"""
import importlib.util
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cas_limites_lire_v5 as CL  # noqa: E402

ARBRE = CL.ARBRE


def module_corrige():
    spec = importlib.util.spec_from_file_location("an_corrige", ARBRE / "scripts" / "analyser_echelle_v5.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    origine = m.conditions
    m.ISSUES = ("fuite de signe inverse (petit)", "fuite de signe inverse (grand)", "positif", "inverse",
                "pas de fuite", "nul")

    def conditions(r, s):
        c = origine(r, s)
        d, n = m.SEUILS["delta"], m.NOM_SENS[s]
        fsi = c.pop("fuite de signe inverse")
        for k in ("petit", "grand"):
            hi = r[k][s]["lambda_ic"][1]
            c[f"fuite de signe inverse ({k})"] = [(f"borne haute de λ_{n}({k}) {hi:.3f} < −δ", hi < -d)]
        return c

    m.conditions = conditions
    m.PROFONDEUR = {**m.PROFONDEUR, **{f"fuite de signe inverse ({k})": m.PROFONDEUR["fuite de signe inverse"]
                                        for k in ("petit", "grand")}}
    origine_reserves = m.reserves

    def reserves(r, issue):
        if issue.startswith("fuite de signe inverse"):
            return _reserves_fsi(m, r, issue)          # réserves de la v5, restreintes au modèle nommé
        return origine_reserves(r, issue)

    m.reserves = reserves
    return m


def _reserves_fsi(m, r, issue):
    out, d = [], m.SEUILS["delta"]
    k = issue[issue.index("(") + 1:-1]
    if any(r[k][s]["lambda_ic"][1] < -d and r["specificite_signe_inverse_ic"][k][s][0] <= 0 for s in m.SENS):
        out.append(m.NON_SPECIFIQUE)
    if any(r["profondeur_contraire"][issue].values()):
        out.append(m.PROFONDEUR[issue])
    return out


def principal():
    corrige = module_corrige()
    for nom, kw in CL.CAS.items():
        r = CL.r_fictif(**kw)
        r["profondeur_contraire"] = {**r["profondeur_contraire"],
                                     **{f"fuite de signe inverse ({k})": {"ab": False, "ba": False}
                                        for k in ("petit", "grand")}}
        v5 = CL.AN.lire(r)[:2]
        c = corrige.lire(r)[:2]
        print(json.dumps({"cas": nom, "v5": v5, "corrigée": c}, ensure_ascii=False))


if __name__ == "__main__":
    principal()
