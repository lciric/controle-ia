"""Couple S5 (décision de la mère, routine, R-1717 ; contestable par la contre-lecture du candidat final) : candidat 9 (`4acab311…`, vérifié avant tout) → candidat 9, révision 2
(nouveau fichier, R12). Le seuil « la base réussit » est **aire moyenne ≥ 0,70 avec la borne basse au-dessus du quantile 0,95 du plancher** ; l'écart de gain est **+ 0,05** ;
l'alternative à 0,65 est retirée du texte et mentionnée comme écartée. Chaque « ancien » doit se trouver exactement une fois, sinon arrêt sans rien écrire.

    python3 -I -B appliquer-couple-s5-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
C9, PREFIXE_C9 = "brouillons/T0.6-organismes-v0-v1-candidat9.md", "4acab3114076e55a"
C9R2 = "brouillons/T0.6-organismes-v0-v1-candidat9-r2.md"
COUPLES = [
    ("S5a", "2. **Quand la base décisive « réussit » à une dose** *(proposition)* : sa borne basse", "2. **Quand la base décisive « réussit » à une dose** : sa borne basse"),
    ("S5b", " *(Autre seuil à discuter : 0,65, milieu de la plage ; recommandation : 0,70, confiance moyenne.)*", " *(Seuil retenu par la mère, routine ; l'alternative à 0,65, milieu de la plage, est écartée.)*"),
    ("S5c", "*(proposition : 0,05 à confirmer par le script de puissance avant lecture)*", "*(écart fixé à + 0,05 par la mère, routine ; contestable par la contre-lecture du candidat final)*"),
    ("S5d", "*Valeurs encore à fixer avant le scellement* (marquées « proposition » ci-dessus) : seuil d'échec de la base (0,70, alternative 0,65) et écart minimal de gain (0,05, à confirmer par le script de puissance) ; elles ne sont pas encore décidées.",
     "*Valeurs fixées par la mère (décision de routine, que la contre-lecture du candidat final peut contester)* : seuil « la base réussit » = aire moyenne ≥ 0,70 avec la borne basse au-dessus du quantile 0,95 du plancher ; écart de gain = + 0,05 ; l'alternative à 0,65 est écartée."),
]


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(racine: Path) -> int:
    c9 = racine / C9
    if not sha(c9).startswith(PREFIXE_C9):
        raise SystemExit("candidat 9 : empreinte non conforme")
    sortie = racine / C9R2
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    t = c9.read_text(encoding="utf-8")
    j = ["| couple | ligne | occurrences | longueur ancien | longueur nouveau |", "|---|---|---|---|---|"]
    for nom, a, n in COUPLES:
        if t.count(a) != 1:
            raise SystemExit(f"{nom} : « ancien » trouvé {t.count(a)} fois, 1 attendu : arrêt, rien d'écrit")
        j.append(f"| {nom} | {t[: t.index(a)].count(chr(10)) + 1} | 1 | {len(a)} | {len(n)} |")
        t = t.replace(a, n)
    if "*(proposition" in t or "0,65, milieu de la plage, est écartée" not in t:
        raise SystemExit("S5 : reste de « proposition » ou mention de l'alternative absente")
    sortie.write_text(t, encoding="utf-8")
    maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (ICI / "journal-couple-s5-v1.md").write_text("\n".join([f"# Journal du couple S5 — {maintenant} (`date -u`)", "", f"- candidat 9 : `{C9}`, `{sha(c9)}` (vérifiée avant tout)",
                                                           f"- script : `appliquer-couple-s5-v1.py`, `{sha(__file__)}`", "", *j, "", f"- résultat : `{C9R2}`, `{sha(sortie)}`, {t.count(chr(10)) + 1} lignes"]) + "\n", encoding="utf-8")
    print("\n".join(j), "\n", sha(sortie))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve()))
