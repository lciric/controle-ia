"""cl8 : cas fabriqués de cl7 (repris de cas_limites_lire_v7.py, versé) rejoués contre lire() de l'analyse v8 TELLE QUELLE,
avec des intervalles de e(m) et des rapports des Ec choisis ; bornes des deux réserves."""
import importlib.util, json, pathlib
ARBRE = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v8")
spec = importlib.util.spec_from_file_location("an8", ARBRE / "scripts" / "analyser_echelle_v8.py")
AN = importlib.util.module_from_spec(spec); spec.loader.exec_module(AN)

def r_fictif(lp, lg, dl, lp_ba, lg_ba, dl_ba, sp=(0.1, 0.5), sp_ba=None, cert=(0.8, 0.8), cert_ba=None,
             ssi=None, ecart=None, demi=0.1, q=(1.0, 1.0)):
    sp_ba, cert_ba = sp_ba or sp, cert_ba or cert
    ssi = ssi or {k: {"ab": [0.1, 0.5], "ba": [0.1, 0.5]} for k in ("petit", "grand")}
    p = {x: {"ab": False, "ba": False} for x in AN.ISSUES}
    if ecart is None:
        ecart = {"petit": sum(lp) / 2 - sum(lp_ba) / 2, "grand": sum(lg) / 2 - sum(lg_ba) / 2}
    return {"petit": {"ab": {"A_ctx_fixe_ic": [cert[0], 0.95], "lambda_ic": list(lp)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[0], 0.95], "lambda_ic": list(lp_ba)}},
            "grand": {"ab": {"A_ctx_fixe_ic": [cert[1], 0.95], "lambda_ic": list(lg)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[1], 0.95], "lambda_ic": list(lg_ba)}},
            "delta_lambda_ic": {"ab": list(dl), "ba": list(dl_ba)},
            "specificite_ic": {"ab": list(sp), "ba": list(sp_ba)},
            "specificite_signe_inverse_ic": ssi, "profondeur_contraire": p,
            "ecart_sens": ecart, "ecart_sens_ic": {k: [v - demi, v + demi] for k, v in ecart.items()},
            "rapport_Ec": {"petit": q[0], "grand": q[1]}}

POS = dict(lp=(0.68, 0.92), lg=(0.30, 0.50), dl=(0.28, 0.52), lp_ba=(0.48, 0.72), lg_ba=(0.10, 0.30), dl_ba=(0.28, 0.52))
INV = dict(lp=(0.10, 0.30), lg=(0.48, 0.72), dl=(-0.52, -0.28), sp=(-0.6, -0.1), lp_ba=(0.30, 0.50), lg_ba=(0.68, 0.92), dl_ba=(-0.52, -0.28))
NUL = dict(lp=(0.60, 0.74), lg=(0.38, 0.52), dl=(0.10, 0.24), lp_ba=(0.82, 0.96), lg_ba=(0.60, 0.74), dl_ba=(0.10, 0.24))
CAS = []
for nom, kw in (("positif cl7", POS), ("inverse cl7", INV), ("nul cl7", NUL)):
    CAS.append((nom + ", e ± 0,10 (cl7)", dict(kw)))
    CAS.append((nom + ", e ± 0,21 (intervalle qui contient zéro)", dict(kw, demi=0.21)))
    CAS.append((nom + ", e ± 0,21, q 1,14 et 0,88", dict(kw, demi=0.21, q=(1.14, 0.88))))
    CAS.append((nom + ", e ± 0,21, q 1,15 exactement", dict(kw, demi=0.21, q=(1.15, 1.0))))
    CAS.append((nom + ", e ± 0,21, q 1/1,15 exactement", dict(kw, demi=0.21, q=(1 / 1.15, 1.0))))
    CAS.append((nom + ", e ± 0,21, q non défini (petit)", dict(kw, demi=0.21, q=(None, 1.0))))
    CAS.append((nom + ", e à zéro pile au bord (borne basse 0)", dict(kw, demi=0.2, ecart={"petit": 0.2, "grand": 0.2})))
# issues qu'elles ne visent pas
FSI = dict(lp=(-0.7, -0.3), lg=(0.0, 0.2), dl=(-0.9, -0.3), lp_ba=(-0.6, -0.3), lg_ba=(0.0, 0.2), dl_ba=(-0.8, -0.3), ssi={k: {"ab": [0.1, 0.5], "ba": [0.1, 0.5]} for k in ("petit", "grand")})
CAS.append(("fuite de signe inverse (petit), e ± 0,05, q 1,5", dict(FSI, demi=0.05, q=(1.5, 1.5))))
PDF = dict(lp=(-0.2, 0.2), lg=(-0.2, 0.2), dl=(-0.2, 0.2), lp_ba=(-0.2, 0.2), lg_ba=(-0.2, 0.2), dl_ba=(-0.2, 0.2))
CAS.append(("pas de fuite et nul, e 0,3 ± 0,05, q 1,5", dict(PDF, ecart={"petit": 0.3, "grand": 0.0}, demi=0.05, q=(1.5, 1.5))))
CAS.append(("pas de fuite et nul, e 0,1 ± 0,05, q 1,5", dict(PDF, ecart={"petit": 0.1, "grand": 0.0}, demi=0.05, q=(1.5, 1.5))))
for nom, kw in CAS:
    lecture, reserves, detail = AN.lire(r_fictif(**kw))
    v8 = [x[:44] for x in reserves if x.startswith(("le λ du", "jeux de force"))]
    print(json.dumps({"cas": nom, "lecture": lecture, "reserves_v8": v8, "autres": len(reserves) - len(v8)}, ensure_ascii=False))
print("1/(1/1,15) =", repr(1 / (1 / 1.15)), "; hors bande à 1/1,15 :", AN.rapport_hors_bande(1 / 1.15), "; à 1,15 :", AN.rapport_hors_bande(1.15))
