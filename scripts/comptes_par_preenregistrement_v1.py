#!/usr/bin/env python3
"""Comptes des issues par préenregistrement et par groupe, lus dans une table de calibration rendue — v1.

Entrée : une table `calibration-v3.md` produite par `scripts/registres_taif_v3.py` (lignes de table qui commencent par
« | `prereg/ » ; première cellule : le préenregistrement ; huitième cellule : l'issue). Rien n'est saisi à la main : chaque
compte est recalculé depuis le texte de la table.

Sortie (sur la sortie standard, en markdown) :
  1. une ligne par préenregistrement qui a au moins une ligne tranchée (confirmée, réfutée ou non concluante) ;
  2. les comptes par groupe, et le taux de confirmation parmi les tranchées de chaque groupe.

Groupes (choix de la session-dépôt, écrit ici pour être contre-lu, et sans effet sur la table elle-même) :
  - « preuves en simulation » : la simulation du lemme et du théorème négatif (T0.3). Son verdict dit que 31 sur 31
    « était l'issue attendue par construction » et que 19 des 31 prédictions sont des vérifications de l'instrument.
  - « instruments » : la validation du harnais d'activations (T0.4, trois versions du préenregistrement, que la table
    compte séparément) et la revalidation de l'équivalence des noyaux (T0.5, v2). Elles valident un outil, pas une
    affirmation sur le monde.
  - « prédictions empiriques » : toutes les autres lignes tranchées.
Une ligne « mixte », « contradictoire », « sans objet », « non atteinte », « non déclenchée » ou sans verdict scellé n'entre
dans aucun taux ; elle est comptée à part, comme dans la table d'origine.

    python scripts/comptes_par_preenregistrement_v1.py CHEMIN/calibration-v3.md
"""
from __future__ import annotations

import collections
import sys
from pathlib import Path

TRANCHEES = ("confirmée", "réfutée", "non concluante")

GROUPE_PREUVES = {"prereg/T0.3-simulation-lemme-theoreme-v1.md"}
GROUPE_INSTRUMENTS = {
    "prereg/T0.4-validation-modele-reel-v1.md",
    "prereg/T0.4-validation-modele-reel-v2.md",
    "prereg/T0.4-validation-modele-reel-v3.md",
    "prereg/T0.5-revalidation-equivalence-pilote-v2.md",
}
NOMS_GROUPES = ("preuves en simulation", "instruments", "prédictions empiriques")


def groupe(prereg: str) -> str:
    if prereg in GROUPE_PREUVES:
        return NOMS_GROUPES[0]
    if prereg in GROUPE_INSTRUMENTS:
        return NOMS_GROUPES[1]
    return NOMS_GROUPES[2]


def lire_table(texte: str) -> dict[str, collections.Counter]:
    par: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for ligne in texte.splitlines():
        if not ligne.startswith("| `prereg/"):
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cellules) < 8:
            raise SystemExit(f"ligne de table trop courte ({len(cellules)} cellules) : {ligne[:80]}")
        prereg = cellules[0].strip("`")
        par[prereg][cellules[7]] += 1
    if not par:
        raise SystemExit("aucune ligne de prédiction lue : table vide ou format inattendu")
    return par


def taux(c: int, t: int) -> str:
    return f"{c} / {t} = {c / t:.3f}".replace(".", ",") if t else "sans objet (aucune tranchée)"


def rendre(par: dict[str, collections.Counter]) -> str:
    lignes = [
        "| préenregistrement | groupe | lignes | confirmées | réfutées | non concluantes | autres |",
        "|---|---|---|---|---|---|---|",
    ]
    sommes = {g: collections.Counter() for g in NOMS_GROUPES}
    total_lignes = 0
    for prereg in sorted(par):
        cnt = par[prereg]
        total_lignes += sum(cnt.values())
        tr = sum(cnt[k] for k in TRANCHEES)
        if not tr:
            sommes[groupe(prereg)]["hors taux"] += sum(cnt.values())
            continue
        g = groupe(prereg)
        for k in TRANCHEES:
            sommes[g][k] += cnt[k]
        autres = sum(v for k, v in cnt.items() if k not in TRANCHEES)
        sommes[g]["hors taux"] += autres
        lignes.append(
            f"| `{prereg}` | {g} | {sum(cnt.values())} | {cnt['confirmée']} | {cnt['réfutée']} | "
            f"{cnt['non concluante']} | {autres} |"
        )
    lignes += ["", "| groupe | confirmées | réfutées | non concluantes | taux de confirmation parmi les tranchées |",
               "|---|---|---|---|---|"]
    tout = collections.Counter()
    for g in NOMS_GROUPES:
        s = sommes[g]
        tout.update(s)
        t = sum(s[k] for k in TRANCHEES)
        lignes.append(f"| {g} | {s['confirmée']} | {s['réfutée']} | {s['non concluante']} | {taux(s['confirmée'], t)} |")
    t = sum(tout[k] for k in TRANCHEES)
    lignes.append(f"| **toutes** | {tout['confirmée']} | {tout['réfutée']} | {tout['non concluante']} | "
                  f"{taux(tout['confirmée'], t)} |")
    lignes += ["", f"Lignes lues : {total_lignes} ; tranchées : {t} ; hors taux : {tout['hors taux']}."]
    if t + tout["hors taux"] != total_lignes:
        raise SystemExit("les comptes ne bouclent pas : tranchées + hors taux ≠ lignes lues")
    return "\n".join(lignes) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    print(rendre(lire_table(Path(argv[1]).read_text(encoding="utf-8"))), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
