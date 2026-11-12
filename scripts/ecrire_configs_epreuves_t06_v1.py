"""Écrit les configurations des épreuves à blanc E2 et E3 de T0.6 et leurs tâches synthétiques (C-V4-3 ; fichiers neufs, R12,
rien d'existant modifié). Aucune donnée décisive : les tâches sont synthétiques (énoncés de questions de recherche, comme E1).
Bibliothèque standard + le dépôt ; aucun réseau.

    PYTHONPATH=src python -I -B scripts/ecrire_configs_epreuves_t06_v1.py RACINE_DU_DEPOT

Écrit, sous `docs/notes/g0-deux-semaines-v1/` : `config-t06-epreuve-e2-v1.json` (base : configuration jouet v5 ; carte modeste, plafond
1,5 USD), `config-t06-epreuve-e3-v1.json` (base : configuration réelle du brouillon 4 ; carte A100, plafond 3,5 USD ; tâches
synthétiques, T = 4, tirages réduits : l'épreuve mesure la mémoire, les secondes par pas, l'identité, la garde, le débit et les
durées, pas un résultat) ; et, sous `donnees/t06-epreuve-e2/` et `donnees/t06-epreuve-e3/`, les fichiers de tâches (à verser avec
`git add -f`, `donnees/` étant ignoré). Chaque configuration est validée par `configuration_v4.exiger_config_t06_v4` avant écriture."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, "src")
import hashlib                                                                # noqa: E402
from controle_ia.t06.configuration_v2 import pas_attendus_avant_dependance    # noqa: E402
from controle_ia.t06.configuration_v4 import GO_EPREUVE, exiger_config_t06_v4  # noqa: E402

ENONCES = ["Which routing rule makes sparse mixtures of experts train stably?", "Does curriculum ordering change sample efficiency of small language models?",
           "Can retrieval reduce hallucination in long-form question answering?", "How does tokenizer vocabulary size affect multilingual transfer?",
           "Do sparse autoencoders recover known features in toy models?", "Is chain-of-thought faithful under distribution shift?"]
NOTES = "docs/notes/g0-deux-semaines-v1"
CALENDRIER = {"dernier_jour_creation": "2026-11-09", "fin_go_utc": "2026-11-11T00:00:00Z"}     # GO-2026-11-06-01 : échéance 2026-11-10


def sha256_de(chemin: Path) -> str:      # aucun `.sha256` écrit ici : la session mère scelle
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def taches(ids):
    return {"taches": [{"identifiant": i, "questions": ENONCES[k % len(ENONCES)] + f" ({i})"} for k, i in enumerate(ids)]}


def ecrire_json(chemin: Path, corps: dict) -> None:
    if chemin.exists():
        raise SystemExit(f"{chemin} existe déjà (R12) : rien d'écrasé")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(corps, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def main(racine: Path) -> int:
    notes = racine / NOTES
    jouet = json.loads((notes / "config-t06-jouet-v5.json").read_text(encoding="utf-8"))
    reel = json.loads((notes / "config-t06-reel-v1-brouillon4.json").read_text(encoding="utf-8"))
    sortie = {}
    for nom, base, plafond, ev, di in (("e2", jouet, 1.5, ["e1", "e2", "e3", "e4"], ["d1", "d2"]), ("e3", reel, 3.5, ["e1", "e2", "e3", "e4"], ["d1", "d2", "d3"])):
        d = racine / "donnees" / f"t06-epreuve-{nom}"
        ecrire_json(d / "taches-evaluation.json", taches(ev))
        ecrire_json(d / "taches-distillation.json", taches(di))
        c = json.loads(json.dumps(base))
        c.update(go_id=GO_EPREUVE, plafond_usd=plafond, calendrier=dict(CALENDRIER))
        c["taches_evaluation"] = {"chemin": f"donnees/t06-epreuve-{nom}/taches-evaluation.json", "sha256": sha256_de(d / "taches-evaluation.json")}
        c["taches_distillation"] = {"chemin": f"donnees/t06-epreuve-{nom}/taches-distillation.json", "sha256": sha256_de(d / "taches-distillation.json")}
        c["offre"] = dict(c["offre"], etiquette=f"t06-{nom}")
        if nom == "e2":
            # carte modeste (une seule carte, 20 Go ou plus) ; disque 150 Go (prix relus avec --storage 150) ; téléchargement négligeable
            c["carte"] = {"course": {"memoire_carte_min_mo": 20000, "nom": "carte modeste (E2)", "nom_offre": "RTX 4090", "prix_max_usd_h": 0.6},
                          "relance": {"memoire_carte_min_mo": 20000, "nom": "carte modeste (E2, relance sans objet)", "nom_offre": "RTX 4090", "prix_max_usd_h": 0.6}}
            c["offre"].update(coeurs_effectifs_min=8, disque_min_go=150, memoire_vive_min_mo=32000, telechargement_go_prevu=1)
        else:
            c.update(T=4, tirages_aire=200, n_plancher=20, permutations_plancher=20, tirages_cout=500, permutations_tendance=200,
                     episodes_par_tache_distillation=5)
            c["distillation"] = dict(c["distillation"], pas_declares=0)
            c["distillation"]["pas_declares"] = pas_attendus_avant_dependance(c, len(di))
            c["offre"].update(telechargement_go_prevu=40)
        exiger_config_t06_v4(c)
        ecrire_json(notes / f"config-t06-epreuve-{nom}-v1.json", c)
        sortie[nom] = {"pas_declares": c["distillation"]["pas_declares"], "plafond_usd": plafond, "etiquette": c["offre"]["etiquette"]}
    print(json.dumps(sortie, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]).resolve()))
