"""Extrait d'une branche d'épreuve (E2 ou E3, branche `essai/…` clonée) les SEULES mesures d'exploitation, par liste blanche
(C-V4-3 ; aucune sonde décisive lue : les aires, états de jeu, lignes de table et planchers ne sont jamais lus ni imprimés).
Bibliothèque standard seule ; aucun réseau.

    python3 -I -B scripts/extraire_mesures_epreuve_t06_v1.py RACINE_DE_LA_BRANCHE

Imprime un JSON : durées, mémoire de pointe, réglages de déterminisme, place disque, morceaux, identité à dose 0, garde d'équivalence
(99e centile), nombre et durée des pas de distillation, calcul de Mahalanobis, essais d'égalité (écart, tolérance, jetons tirés et
réels), durées par couple descriptif. Une clé absente est imprimée « absent » (jamais devinée)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ABSENT = "absent"


def _lire(chemin: Path) -> dict:
    if not chemin.is_file():
        return {}
    return json.loads(chemin.read_text(encoding="utf-8")).get("resultat", {})


def _cles(d: dict, *cles):
    return {k: d.get(k, ABSENT) for k in cles}


def mesures(racine: Path) -> dict:
    dossiers = sorted(p for p in (racine / "diag").glob("*-t06-*") if p.is_dir())
    if len(dossiers) != 1:
        raise SystemExit(f"un seul dossier diag/*-t06-* attendu, {len(dossiers)} trouvé(s)")
    d = dossiers[0]
    ep, di, ls, rs = (_lire(d / f"{n}.json") for n in ("episodes-t06", "distillation-t06", "lecture-sondes-t06", "resume"))
    desc = ep.get("descriptifs", {}) if isinstance(ep.get("descriptifs"), dict) else {}
    sous = ep.get("activations_sous_ensemble", {}) if isinstance(ep.get("activations_sous_ensemble"), dict) else {}
    journaux = di.get("journaux", {}) if isinstance(di.get("journaux"), dict) else {}
    pas = {ad: {"pas": len(j), "cles_d_un_pas": sorted(j[0]) if j and isinstance(j[0], dict) else ABSENT} for ad, j in journaux.items() if isinstance(j, list)}
    etats = ep.get("etats", {}) if isinstance(ep.get("etats"), dict) else {}
    verifs = ls.get("verifications_mahalanobis", {}) if isinstance(ls.get("verifications_mahalanobis"), dict) else {}
    tires = {k: v for k, v in verifs.items() if not k.endswith("/reels")}
    reels = {k: v for k, v in verifs.items() if k.endswith("/reels")}

    def resume_essais(x: dict) -> dict:
        return {"essais": len(x), "tous_egaux": all(isinstance(v, dict) and v.get("egal") is True for v in x.values()) if x else ABSENT,
                "ecart_relatif_max": max((v.get("ecart_relatif_max", 0.0) for v in x.values() if isinstance(v, dict)), default=ABSENT),
                "n_jetons_min_max": [min((v.get("n_jetons", 0) for v in x.values()), default=ABSENT), max((v.get("n_jetons", 0) for v in x.values()), default=ABSENT)]}
    return {
        "run": d.name,
        "episodes": {**_cles(desc, "duree_s", "memoire_pic_gio"), "reglages": ep.get("reglages", ABSENT), "disque": ep.get("disque", ABSENT),
                     "morceau": ep.get("morceau", ABSENT), "noyau_attention": ep.get("noyau_attention", ABSENT),
                     "sous_ensemble": _cles(sous, "actions", "total_notees", "couche", "precision"), "morceaux": len(sous.get("morceaux", [])),
                     "reecrits": len(sous.get("reecrits", [])), "chrono": {k: v for k, v in desc.items() if k not in ("duree_s", "memoire_pic_gio")}},
        "equivalence_99e_centile": {k: v.get("equivalence", ABSENT) for k, v in etats.items() if isinstance(v, dict)},
        "distillation": {**_cles(di, "duree_s", "pas_declares", "plan", "precision_adaptateurs", "jetons_controle"), "pas_par_adaptateur": pas,
                         "identite_dose_0": di.get("identite_dose_0", ABSENT)},
        "mahalanobis": {"calcul": ls.get("mahalanobis_calcul", ABSENT), "egalite_jetons_reels": ls.get("egalite_jetons_reels", ABSENT),
                        "jetons_tires": resume_essais(tires), "jetons_reels": resume_essais(reels)},
        "durees_par_couple_s": ls.get("durees_s", ABSENT),
        "resume": _cles(rs, "duree_s", "episodes", "actions", "actions_notees", "morceaux", "morceaux_reecrits", "mahalanobis_calcul"),
    }


if __name__ == "__main__":
    print(json.dumps(mesures(Path(sys.argv[1]).resolve()), ensure_ascii=False, indent=1, sort_keys=True))
