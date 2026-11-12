"""cl7 : cas fabriqués de cl5 et cl6 (repris à l'identique de `cas_limites_lire_v6.py` de cl6) rejoués contre `lire()`
de `analyser_echelle_v7.py` TELLE QUELLE ; l'écart ponctuel e(m) n'existait pas en v6 : il est pris (1) au milieu des
intervalles de λ de chaque modèle (ce que vaudrait le point si l'intervalle était centré), (2) à des valeurs choisies.
Puis cas nouveaux de cl7 : la classe de CLT-01 (écart vrai sous δ, signatures croisées sous δ), sur intervalles."""
import importlib.util, json, pathlib, runpy
ARBRE = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v7")
spec = importlib.util.spec_from_file_location("an7", ARBRE / "scripts" / "analyser_echelle_v7.py")
AN = importlib.util.module_from_spec(spec); spec.loader.exec_module(AN)
CL6 = "/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v7/contre-lecture-cl6/scripts/cas_limites_lire_v6.py"
src = open(CL6, encoding="utf-8").read()
# on n'exécute que les dictionnaires de cas (ni l'import de l'analyse v6, ni principal)
debut = src.index("CAS_CL5 = {"); fin = src.index("def principal")
ns = {"AN": AN}
exec(compile(src[debut:fin], CL6, "exec"), ns)
CAS_CL5, CAS_CL6 = ns["CAS_CL5"], ns["CAS_CL6"]


def r_fictif(lp, lg, dl, lp_ba, lg_ba, dl_ba, sp=(0.1, 0.5), sp_ba=None, cert=(0.8, 0.8), cert_ba=None,
             ssi=None, prof=None, ecart=None):
    sp_ba, cert_ba = sp_ba or sp, cert_ba or cert
    ssi = ssi or {k: {"ab": [0.1, 0.5], "ba": [0.1, 0.5]} for k in ("petit", "grand")}
    p = {x: {"ab": False, "ba": False} for x in AN.ISSUES}
    for x, v in (prof or {}).items():
        p[x].update(v)
    if ecart is None:
        ecart = {"petit": sum(lp) / 2 - sum(lp_ba) / 2, "grand": sum(lg) / 2 - sum(lg_ba) / 2}
    return {"petit": {"ab": {"A_ctx_fixe_ic": [cert[0], 0.95], "lambda_ic": list(lp)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[0], 0.95], "lambda_ic": list(lp_ba)}},
            "grand": {"ab": {"A_ctx_fixe_ic": [cert[1], 0.95], "lambda_ic": list(lg)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[1], 0.95], "lambda_ic": list(lg_ba)}},
            "delta_lambda_ic": {"ab": list(dl), "ba": list(dl_ba)},
            "specificite_ic": {"ab": list(sp), "ba": list(sp_ba)},
            "specificite_signe_inverse_ic": ssi, "profondeur_contraire": p,
            "ecart_sens": ecart, "ecart_sens_ic": {k: [v - 0.1, v + 0.1] for k, v in ecart.items()}}


CAS_CL7 = {
    # écart vrai 0,2 (H_0 : |Δ| ≤ δ), signatures croisées de signes opposés qui ajoutent 0,2 à chaque sens, porté par le
    # 8B en a→b et par le 70B en b→a : chaque modèle change de 0,2 < δ d'un sens à l'autre
    "CLT-01 positif : écart vrai 0,2, +0,2 au 8B en a→b, −0,2 au 70B en b→a": dict(
        lp=(0.68, 0.92), lg=(0.30, 0.50), dl=(0.28, 0.52),
        lp_ba=(0.48, 0.72), lg_ba=(0.10, 0.30), dl_ba=(0.28, 0.52)),
    "CLT-01 inverse (miroir des signes)": dict(
        lp=(0.10, 0.30), lg=(0.48, 0.72), dl=(-0.52, -0.28), sp=(-0.6, -0.1),
        lp_ba=(0.30, 0.50), lg_ba=(0.68, 0.92), dl_ba=(-0.52, -0.28)),
    # « nul » sous H_A : écart vrai 0,4, compensé de 0,22 dans chaque sens par un modèle différent
    "CLT-01 nul sous H_A : écart vrai 0,4, −0,22 au 8B en a→b, +0,22 au 70B en b→a": dict(
        lp=(0.60, 0.74), lg=(0.38, 0.52), dl=(0.10, 0.24),
        lp_ba=(0.82, 0.96), lg_ba=(0.60, 0.74), dl_ba=(0.10, 0.24)),
}


def principal():
    for titre, cas in (("cl5", CAS_CL5), ("cl6", CAS_CL6), ("cl7", CAS_CL7)):
        for nom, kw in cas.items():
            for variante, e in (("e au milieu", None), ("e = 0", {"petit": 0.0, "grand": 0.0})):
                lecture, reserves, detail = AN.lire(r_fictif(**kw, ecart=e))
                print(json.dumps({"lot": titre, "cas": nom, "variante": variante, "lecture": lecture,
                                  "reserves": reserves, "issues_tenues": detail["issues_tenues_par_sens"],
                                  "coherence": [c["tenue"] for c in detail["coherence_des_sens"]]},
                                 ensure_ascii=False))


if __name__ == "__main__":
    principal()
