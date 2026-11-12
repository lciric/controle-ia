"""Contre-lecture n° 6 (cl6) : cas limites de `lire()` de `analyser_echelle_v6.py` TELLE QUELLE, sur des intervalles
fabriqués : (1) les six cas de cl5 (`cas_limites_lire_v5.py`), rejoués à l'identique ; (2) cas nouveaux de cl6.
Lecture seule de l'arbre de travail. Usage : python -I -B cas_limites_lire_v6.py
"""
import importlib.util
import json
import pathlib

ARBRE = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v6")
spec = importlib.util.spec_from_file_location("an", ARBRE / "scripts" / "analyser_echelle_v6.py")
AN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AN)


def r_fictif(lp, lg, dl, lp_ba, lg_ba, dl_ba, sp=(0.1, 0.5), sp_ba=None, cert=(0.8, 0.8), cert_ba=None,
             ssi=None, prof=None):
    """Même forme que dans `cas_limites_lire_v5.py` de cl5 ; `prof` : {issue: {sens: drapeau}} partiel."""
    sp_ba, cert_ba = sp_ba or sp, cert_ba or cert
    ssi = ssi or {k: {"ab": [0.1, 0.5], "ba": [0.1, 0.5]} for k in ("petit", "grand")}
    p = {x: {"ab": False, "ba": False} for x in AN.ISSUES}
    for x, v in (prof or {}).items():
        p[x].update(v)
    return {"petit": {"ab": {"A_ctx_fixe_ic": [cert[0], 0.95], "lambda_ic": list(lp)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[0], 0.95], "lambda_ic": list(lp_ba)}},
            "grand": {"ab": {"A_ctx_fixe_ic": [cert[1], 0.95], "lambda_ic": list(lg)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[1], 0.95], "lambda_ic": list(lg_ba)}},
            "delta_lambda_ic": {"ab": list(dl), "ba": list(dl_ba)},
            "specificite_ic": {"ab": list(sp), "ba": list(sp_ba)},
            "specificite_signe_inverse_ic": ssi, "profondeur_contraire": p}


CAS_CL5 = {
    "fsi croisée (petit en a→b, grand en b→a)": dict(
        lp=(-1.0, -0.6), lg=(-0.1, 0.1), dl=(-1.0, -0.6),
        lp_ba=(-0.1, 0.1), lg_ba=(-1.0, -0.6), dl_ba=(0.6, 1.0)),
    "fsi croisée, un modèle sous −δ par sens, l'autre au bord": dict(
        lp=(-0.6, -0.3), lg=(-0.4, -0.2), dl=(-0.2, 0.1),
        lp_ba=(-0.4, -0.2), lg_ba=(-0.6, -0.3), dl_ba=(-0.1, 0.2)),
    "fsi du même modèle (petit) dans les deux sens": dict(
        lp=(-1.0, -0.6), lg=(-0.1, 0.1), dl=(-1.0, -0.6),
        lp_ba=(-1.0, -0.6), lg_ba=(-0.1, 0.1), dl_ba=(-1.0, -0.6)),
    "pas de fuite (a→b) + nul (deux sens)": dict(
        lp=(0.05, 0.22), lg=(0.0, 0.2), dl=(-0.10, 0.15),
        lp_ba=(0.10, 0.32), lg_ba=(0.08, 0.30), dl_ba=(-0.12, 0.14)),
    "pas de fuite + nul (a→b), b→a indécis": dict(
        lp=(0.05, 0.22), lg=(0.0, 0.2), dl=(-0.10, 0.15),
        lp_ba=(0.3, 0.9), lg_ba=(0.1, 0.6), dl_ba=(-0.1, 0.6)),
    "fsi + nul (a→b) contre pas de fuite seul (b→a)": dict(
        lp=(-1.1, -0.9), lg=(-1.0, -0.85), dl=(-0.2, 0.2),
        lp_ba=(-0.2, 0.25), lg_ba=(0.2, 0.25), dl_ba=(-0.45, 0.05)),
}

CAS_CL6 = {
    # « positif » dont l'écart est porté par le petit dans un sens et par le grand dans l'autre : λ de chaque modèle
    # différent d'un sens à l'autre de 0,5 (signatures croisées de signes opposés sous une fuite égale de 0,5)
    "positif croisé : écart porté par le 8B en a→b, par le 70B en b→a": dict(
        lp=(0.85, 1.15), lg=(0.4, 0.6), dl=(0.35, 0.65),
        lp_ba=(0.4, 0.6), lg_ba=(-0.1, 0.1), dl_ba=(0.35, 0.65)),
    "inverse croisé : écart porté par le 8B en a→b, par le 70B en b→a": dict(
        lp=(-0.1, 0.1), lg=(0.4, 0.6), dl=(-0.65, -0.35),
        lp_ba=(0.4, 0.6), lg_ba=(0.85, 0.95), dl_ba=(-0.65, -0.35), sp=(-0.6, -0.1)),
    "nul croisé : 8B à 0,2 en a→b, 70B à 1,0 en b→a (écart vrai de 0,8 compensé)": dict(
        lp=(0.05, 0.35), lg=(0.05, 0.35), dl=(-0.15, 0.15),
        lp_ba=(0.85, 1.15), lg_ba=(0.85, 1.15), dl_ba=(-0.15, 0.15)),
    # réserves nommées : la réserve « fuite non spécifique » nomme-t-elle le bon modèle ?
    "fsi (grand) commune, réserve non spécifique du grand": dict(
        lp=(-0.1, 0.1), lg=(-1.0, -0.6), dl=(0.5, 1.0),
        lp_ba=(-0.1, 0.1), lg_ba=(-1.0, -0.6), dl_ba=(0.5, 1.0),
        ssi={"petit": {"ab": [-0.5, 0.2], "ba": [-0.5, 0.2]}, "grand": {"ab": [0.1, 0.5], "ba": [-0.2, 0.5]}}),
    "fsi (petit) commune, fsi (grand) d'un seul sens, nul des deux": dict(
        lp=(-1.1, -0.9), lg=(-1.0, -0.85), dl=(-0.2, 0.2),
        lp_ba=(-1.1, -0.9), lg_ba=(-0.5, -0.1), dl_ba=(-0.2, 0.2)),
    "profondeur du grand quand seul le petit est prononcé": dict(
        lp=(-1.0, -0.6), lg=(-0.1, 0.1), dl=(-1.0, -0.6),
        lp_ba=(-1.0, -0.6), lg_ba=(-0.1, 0.1), dl_ba=(-1.0, -0.6),
        prof={AN.FSI["grand"]: {"ab": True}}),
    # Δλ de signe opposé d'un sens à l'autre, chaque sens tenant « nul » : nul prononcé
    "nul avec Δλ de signes opposés d'un sens à l'autre": dict(
        lp=(0.3, 0.6), lg=(0.2, 0.5), dl=(0.0, 0.24),
        lp_ba=(0.2, 0.5), lg_ba=(0.3, 0.6), dl_ba=(-0.24, 0.0)),
}


def principal():
    for titre, cas in (("cl5", CAS_CL5), ("cl6", CAS_CL6)):
        for nom, kw in cas.items():
            lecture, reserves, detail = AN.lire(r_fictif(**kw))
            print(json.dumps({"lot": titre, "cas": nom, "lecture": lecture, "reserves": reserves,
                              "issues_tenues": detail["issues_tenues_par_sens"],
                              "lecture_par_sens": detail["lecture_par_sens"],
                              "conditions_manquantes": detail["conditions_manquantes"]}, ensure_ascii=False))


if __name__ == "__main__":
    principal()
