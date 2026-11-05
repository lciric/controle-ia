"""Contre-lecture n° 5 (cl5) : cas limites de `lire()` de `analyser_echelle_v5.py` TELLE QUELLE, sur des intervalles
fabriqués (même forme que `r_fictif` des tests v5). Lecture seule de l'arbre de travail ; aucune écriture hors du bac à
sable. Usage : python -I -B cas_limites_lire_v5.py
"""
import importlib.util
import json
import pathlib

ARBRE = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v5")
spec = importlib.util.spec_from_file_location("an", ARBRE / "scripts" / "analyser_echelle_v5.py")
AN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AN)


def r_fictif(lp, lg, dl, lp_ba, lg_ba, dl_ba, sp=(0.1, 0.5), sp_ba=None, cert=(0.8, 0.8), cert_ba=None,
             ssi=None, prof=None):
    """Intervalles fabriqués, sens a→b puis b→a ; ssi[k][s] : intervalle de −λ − ν ; prof[issue][s] : drapeau."""
    sp_ba, cert_ba = sp_ba or sp, cert_ba or cert
    ssi = ssi or {k: {"ab": [0.1, 0.5], "ba": [0.1, 0.5]} for k in ("petit", "grand")}
    prof = prof or {x: {"ab": False, "ba": False} for x in AN.ISSUES}
    return {"petit": {"ab": {"A_ctx_fixe_ic": [cert[0], 0.95], "lambda_ic": list(lp)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[0], 0.95], "lambda_ic": list(lp_ba)}},
            "grand": {"ab": {"A_ctx_fixe_ic": [cert[1], 0.95], "lambda_ic": list(lg)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[1], 0.95], "lambda_ic": list(lg_ba)}},
            "delta_lambda_ic": {"ab": list(dl), "ba": list(dl_ba)},
            "specificite_ic": {"ab": list(sp), "ba": list(sp_ba)},
            "specificite_signe_inverse_ic": ssi, "profondeur_contraire": prof}


CAS = {
    # 1. fuite de signe inverse tenue dans chaque sens, mais par un modèle différent : le petit sous −δ en a→b
    #    seulement, le grand sous −δ en b→a seulement (deux signatures d'un seul jeu, de tailles différentes)
    "fsi croisée (petit en a→b, grand en b→a)": dict(
        lp=(-1.0, -0.6), lg=(-0.1, 0.1), dl=(-1.0, -0.6),
        lp_ba=(-0.1, 0.1), lg_ba=(-1.0, -0.6), dl_ba=(0.6, 1.0)),
    # 2. même chose, et « nul » tient aussi dans chaque sens ? (non : Δλ hors bande) ; variante où Δλ reste dans la bande
    "fsi croisée, un modèle sous −δ par sens, l'autre au bord": dict(
        lp=(-0.6, -0.3), lg=(-0.4, -0.2), dl=(-0.2, 0.1),
        lp_ba=(-0.4, -0.2), lg_ba=(-0.6, -0.3), dl_ba=(-0.1, 0.2)),
    # 3. témoin : même modèle sous −δ dans les deux sens (la vraie fuite de signe inverse du concept)
    "fsi du même modèle (petit) dans les deux sens": dict(
        lp=(-1.0, -0.6), lg=(-0.1, 0.1), dl=(-1.0, -0.6),
        lp_ba=(-1.0, -0.6), lg_ba=(-0.1, 0.1), dl_ba=(-1.0, -0.6)),
    # 4. « pas de fuite » d'un seul sens et « nul » des deux, avec « nul » placé après : réserve attendue
    "pas de fuite (a→b) + nul (deux sens)": dict(
        lp=(0.05, 0.22), lg=(0.0, 0.2), dl=(-0.10, 0.15),
        lp_ba=(0.10, 0.32), lg_ba=(0.08, 0.30), dl_ba=(-0.12, 0.14)),
    # 5. un sens certifié qui tient « pas de fuite » et « nul », l'autre indécis : seule la première issue est nommée
    "pas de fuite + nul (a→b), b→a indécis": dict(
        lp=(0.05, 0.22), lg=(0.0, 0.2), dl=(-0.10, 0.15),
        lp_ba=(0.3, 0.9), lg_ba=(0.1, 0.6), dl_ba=(-0.1, 0.6)),
    # 6. désaccord : fsi + nul (a→b) contre pas de fuite (b→a) sans nul
    "fsi + nul (a→b) contre pas de fuite seul (b→a)": dict(
        lp=(-1.1, -0.9), lg=(-1.0, -0.85), dl=(-0.2, 0.2),
        lp_ba=(-0.2, 0.25), lg_ba=(0.2, 0.25), dl_ba=(-0.45, 0.05)),
}


def principal():
    out = {}
    for nom, kw in CAS.items():
        r = r_fictif(**kw)
        lecture, reserves, detail = AN.lire(r)
        out[nom] = {"lecture": lecture, "reserves": reserves, "issues_tenues": detail["issues_tenues_par_sens"],
                    "conditions_manquantes": detail["conditions_manquantes"]}
        print(json.dumps({nom: out[nom]}, ensure_ascii=False))
    return out


if __name__ == "__main__":
    principal()
