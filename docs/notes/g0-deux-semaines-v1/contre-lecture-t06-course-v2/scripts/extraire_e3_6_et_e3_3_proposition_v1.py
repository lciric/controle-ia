"""PROPOSITION du contre-lecteur (non une pièce de la chaîne) : lecture corrigée des points E3-6 et E3-3 d'une branche d'épreuve
de T0.6, en complément de `scripts/extraire_mesures_epreuve_t06_v1.py` (inchangé), par liste blanche, bibliothèque standard seule.

E3-6 : la chaîne (`lanceur_v5` → `lanceur.jouer_evaluation`) écrit le bloc d'équivalence PAR FICHE d'épisode
(`episodes-t06.json` → `fiches[k].equivalence` : actions contrôlées, tolérance, statistique, écarts par couche) et le contrôle
négatif PAR ÉTAT (`controles_negatifs[<état>]`), jamais sous `etats[<état>]` où lit la v1. Rendu ici, par état : fiches, actions
contrôlées, plus grand écart de la statistique de la garde (99e centile en production), tolérance, et comptes du contrôle négatif.
E3-3 : le journal de distillation a une entrée par époque plus l'époque 0 (perte avant entraînement) ; les pas d'AdamW effectifs
sont écrits par la chaîne sous `distillation-t06.json` → `donnees.<adaptateur>.pas_declares` (pas, conforme_au_declare) et
`donnees.<adaptateur>.exemples`.
Aucune aire, aucun état de sonde décisive, aucune ligne de table : seules les clés nommées ci-dessous sont lues.

    python3 -I -B extraire_e3_6_et_e3_3_proposition_v1.py RACINE_DE_LA_BRANCHE
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ABSENT = "absent"


def _lire(chemin: Path) -> dict:
    if not chemin.is_file():
        return {}
    return json.loads(chemin.read_text(encoding="utf-8")).get("resultat", {})


def mesures(racine: Path) -> dict:
    dossiers = sorted(p for p in (racine / "diag").glob("*-t06-*") if p.is_dir())
    if len(dossiers) != 1:
        raise SystemExit(f"un seul dossier diag/*-t06-* attendu, {len(dossiers)} trouvé(s)")
    d = dossiers[0]
    ep, di = _lire(d / "episodes-t06.json"), _lire(d / "distillation-t06.json")
    etats = ep.get("etats", {}) if isinstance(ep.get("etats"), dict) else {}
    fiches = ep.get("fiches", []) if isinstance(ep.get("fiches"), list) else []
    cn = ep.get("controles_negatifs", {}) if isinstance(ep.get("controles_negatifs"), dict) else {}
    par_etat = {}
    for nom in etats:
        fs = [f for f in fiches if isinstance(f, dict) and f.get("phase") == nom]
        controlees, ecart_max, tolerances, statistiques = 0, None, set(), set()
        for f in fs:
            eq = f.get("equivalence", {}) if isinstance(f.get("equivalence"), dict) else {}
            stat = eq.get("statistique", "max")
            statistiques.add(stat)
            if "tolerance" in eq:
                tolerances.add(eq["tolerance"])
            actions = eq.get("actions", [])
            controlees += len(actions)
            table = eq.get("ecarts_q99" if stat == "q99" else "ecarts", {})
            for cle in actions:
                for v in (table.get(cle, {}) or {}).values():
                    ecart_max = v if ecart_max is None else max(ecart_max, v)
        c = cn.get(nom, {}) if isinstance(cn.get(nom), dict) else {}
        par_etat[nom] = {"fiches": len(fs), "actions_controlees": controlees, "statistique": sorted(statistiques) or ABSENT,
                         "tolerance": sorted(tolerances) or ABSENT, "ecart_max": ecart_max if ecart_max is not None else ABSENT,
                         "conforme": (ecart_max is not None and all(ecart_max <= t for t in tolerances)) if controlees else "non observé",
                         "controle_negatif": {k: c.get(k, ABSENT) for k in ("comparables", "passent", "courtes", "lecture", "statistique")}}
    journaux = di.get("journaux", {}) if isinstance(di.get("journaux"), dict) else {}
    donnees = di.get("donnees", {}) if isinstance(di.get("donnees"), dict) else {}
    distillation = {}
    for ad in sorted(set(journaux) | set(donnees)):
        x = donnees.get(ad, {}) if isinstance(donnees.get(ad), dict) else {}
        j = journaux.get(ad, [])
        pd = x.get("pas_declares", {}) if isinstance(x.get("pas_declares"), dict) else {}
        distillation[ad] = {"exemples": x.get("exemples", ABSENT), "episodes_sans_cible": x.get("episodes_sans_cible", ABSENT),
                            "actions_exclues": x.get("exclues", ABSENT), "actions": x.get("actions", ABSENT),
                            "pas_effectifs": pd.get("pas", ABSENT), "pas_declares": pd.get("pas_declares", ABSENT),
                            "conforme_au_declare": pd.get("conforme_au_declare", ABSENT),
                            "epoques_journalisees": [e.get("epoque") for e in j if isinstance(e, dict)] if isinstance(j, list) else ABSENT}
    return {"run": d.name, "E3_6_equivalence_par_etat": par_etat, "E3_3_distillation_par_adaptateur": distillation}


if __name__ == "__main__":
    print(json.dumps(mesures(Path(sys.argv[1]).resolve()), ensure_ascii=False, indent=1, sort_keys=True))
