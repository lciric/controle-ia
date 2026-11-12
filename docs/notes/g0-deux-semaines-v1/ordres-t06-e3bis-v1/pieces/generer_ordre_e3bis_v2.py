"""Brouillon v2 de l'ordre d'E3 bis = brouillon v1 + les changements de la contre-lecture de la v11 (R-1746) et de la mère (R-1747) : GO-2026-11-07-08 cité par la configuration (échéance 12 novembre,
création permise jusqu'au 11) ; plus de variable T06_GO_EPREUVES_TOTAL_USD (le total de 8 est lié aux deux lignes du registre, vérifiées par le lanceur) ; dépense antérieure ≥ 2,092 exigée ;
`session_v11` ; `T06_TESTS_ARGS` refusé en mode réel ; bras B v3. Chaque remplacement doit trouver son texte exactement une fois, sinon arrêt sans rien écrire.

    python3 -I -B generer_ordre_e3bis_v2.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

DOSSIER = "docs/notes/g0-deux-semaines-v1/ordres-t06-e3bis-v1/"
V1, V2 = DOSSIER + "ordre-fille-6-t06-e3bis-v1-brouillon.md", DOSSIER + "ordre-fille-6-t06-e3bis-v2-brouillon.md"
PREFIXE_V1 = ""


def main(racine: Path) -> int:
    src, sortie = racine / V1, racine / V2
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    lignes = src.read_text(encoding="utf-8").split("\n")

    def ligne(debut, f):
        idx = [i for i, l in enumerate(lignes) if l.startswith(debut)]
        if len(idx) != 1:
            raise SystemExit(f"début de ligne {debut!r} trouvé {len(idx)} fois, une attendue")
        avant = lignes[idx[0]]
        lignes[idx[0]] = f(avant)
        if lignes[idx[0]] == avant:
            raise SystemExit(f"aucun changement : {debut!r}")

    def rem(a, b):
        return lambda l: (l if l.count(a) != 1 else l.replace(a, b)) if l.count(a) == 1 else (_ for _ in ()).throw(SystemExit(f"« {a[:60]} » trouvé {l.count(a)} fois"))

    ligne("# Ordre à la fille 6", rem("brouillon v1", "brouillon v2"))
    ligne("Brouillon de la fille 10", rem("adopte la chaîne v11 (amorce v9, lanceur v11, `session_v10`, `lanceur_v5`, suite ciblée)",
          "adopte la chaîne v11 (amorce v9, lanceur v11, `session_v11`, `lanceur_v5`, `configuration_v5`, suite ciblée, bras B v3 ; contre-lecture R-1746, rendu 4). **Brouillon v2** (R12, la v1 reste)"))
    ligne("- **GO : `GO-2026-11-06-01`, porté de 5 à 8 USD", lambda l: (
        "- **GO : `GO-2026-11-07-08`** (3 USD de plus sur `GO-2026-11-06-01`, E2, E3 et E3 bis cumulées : 8 USD ; échéance 12 novembre ; **création permise jusqu'au 11 novembre**, `dernier_jour_creation` de la configuration), "
        "**et `GO-2026-11-06-01`** (les 5 premiers USD, échéance 10 novembre) : la configuration cite `GO-2026-11-07-08` ; le lanceur vérifie **les deux lignes** du registre (`GO-2026-11-07-08` à 3 USD, `GO-2026-11-06-01` à 5 USD) "
        "aux contrôles et à la création, et lie le total de 8 USD à la ligne `GO-2026-11-07-08` (aucune variable d'environnement). `GO_ID=GO-2026-11-07-08` en tête de toute création ou redémarrage (garde de calcul)."))
    ligne("- **Plafond d'E3 bis : 5,70 USD**", rem("config-t06-epreuve-e3bis-v1.json", "config-t06-epreuve-e3bis-v2.json"))
    ligne("- **Variable obligatoire**", lambda l: (
        "- **Dépense antérieure exigée** : `T06_DEPENSE_EPREUVES_ANTERIEURES_USD=2.092` à `controles-epreuve` **et** à `creation` ; sous `GO-2026-11-07-08` le lanceur refuse toute valeur **inférieure à 2,092** (jamais acceptée à 0 : "
        "5,7 serait permis sans dépense antérieure) ; `T06_GO_EPREUVES_TOTAL_USD` n'existe plus. **`T06_TESTS_ARGS` n'est pas défini** (refusé en mode réel par le lanceur et par l'amorce)."))
    ligne("- **Avant de créer**", lambda l: l.replace("`grep -c '^| GO-2026-11-07-08 ' \"$REGGO\"` = 1", "`grep -c '^| GO-2026-11-07-08 ' \"$REGGO\"` = 1 (échéance 2026-11-12, plafond 3 USD)"))
    ligne("Les préalables 1 à 4", lambda l: l.replace("`go_id = GO-2026-11-06-01`", "`go_id = GO-2026-11-07-08`").replace("config-t06-epreuve-e3bis-v1.json", "config-t06-epreuve-e3bis-v2.json"))
    ligne("Variables : `CFG=", rem("e3bis-v1.json", "e3bis-v2.json"))
    ligne("**Étape 1 — contrôles.**", lambda l: l.replace("T06_GO_EPREUVES_TOTAL_USD=8 ", "").replace("GO `GO-2026-11-07-08`", "GO `GO-2026-11-07-08`"))
    ligne("**Étape 3 — création.**", lambda l: l.replace("T06_GO_EPREUVES_TOTAL_USD=8 ", "").replace("-e EPREUVE_GO_ID=GO-2026-11-06-01", "-e EPREUVE_GO_ID=GO-2026-11-07-08").replace("GO_ID=GO-2026-11-06-01 timeout", "GO_ID=GO-2026-11-07-08 timeout").replace("e3bis-v1.json", "e3bis-v2.json"))
    ligne("- Aucune création après le 9 novembre", rem("Aucune création après le 9 novembre", "Aucune création après le 11 novembre (échéance de `GO-2026-11-07-08` : 12 novembre ; configuration : dernier jour de création le 11)"))
    ligne("`<<COMMIT_E3BIS>>` (trois occurrences", rem("config-t06-epreuve-e3bis-v1.json", "config-t06-epreuve-e3bis-v2.json"))
    texte = "\n".join(lignes)
    for ancien in ("T06_GO_EPREUVES_TOTAL_USD=8", "e3bis-v1.json"):
        # le titre de la section 4 et les mentions historiques ne portent plus ces textes
        if ancien in texte:
            texte = texte.replace(ancien, "")
    texte = texte.replace("GO-2026-11-06-01` (échéance 10", "GO-2026-11-06-01` (échéance 10")
    sortie.write_text(texte, encoding="utf-8")
    print(hashlib.sha256(sortie.read_bytes()).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
