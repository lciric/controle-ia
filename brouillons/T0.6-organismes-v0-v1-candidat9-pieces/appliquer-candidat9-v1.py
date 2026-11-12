"""Candidat 9 de T0.6 = candidat 8 (empreinte vérifiée avant tout) + six couples comptés (texte des couples dans ce script : chacun doit trouver son « ancien » exactement
une fois, sinon arrêt sans rien écrire) : (S1) statut ; (S2) le marqueur `<<REGLE_MOTS_ET_COUT_T06>>` est remplacé par le bloc v2 (`bloc-regle-mots-et-cout-v2.md`, option (b)
adoptée par Lazar, R-1717, GO-2026-11-07-03), avec le renvoi au bras B de l'audit de fuite comme étape annexe (GO-2026-11-07-04), régie par le texte de l'audit et non par T0.6 ;
(S3) la ligne du marqueur disparaît du tableau des marqueurs ; (S4) la fenêtre de GO-2026-11-07-02 (12 recherches à 15 minutes d'intervalle, puis `creation auto relance`)
est inscrite au point 9 du plan d'analyse. Bibliothèque standard ; aucun réseau, aucune clé.

    python3 -I -B appliquer-candidat9-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
C8, SHA_C8_PREFIXE = "brouillons/T0.6-organismes-v0-v1-candidat8.md", "8a7ae49d67dccb47"
C9 = "brouillons/T0.6-organismes-v0-v1-candidat9.md"
BLOC = "brouillons/T0.6-organismes-v0-v1-candidat8-pieces/bloc-regle-mots-et-cout-v2.md"
SHA_BLOC_PREFIXE = "8f8b712e"
ATTENDUS = {"COMMIT_CODE_T06", "EMPREINTES_CODE_T06", "EMPREINTE_AMORCE_T06", "TESTS_ATTENDUS_T06", "VALEURS_CITEES_T06"}
CLES = ["Entropie", "Commit du code d'analyse", "Configuration de T0.6 (empreinte canonique)", "Tâches d'évaluation de T0.6", "Tests attendus",
        "Chemin de la configuration de T0.6", "Chemin des tâches d'évaluation de T0.6", "Chemin des tâches de distillation de T0.6", "Chemin des consignes de P3"]
SHA_AUDIT_PREFIXE = "910a53dc"   # texte scellé de l'audit (point 7), empreinte complète lue sur main


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def un(texte: str, ancien: str, nouveau: str, nom: str, journal: list) -> str:
    n = texte.count(ancien)
    if n != 1:
        raise SystemExit(f"{nom} : « ancien » trouvé {n} fois, 1 attendu : arrêt, rien d'écrit")
    journal.append(f"| {nom} | {texte[: texte.index(ancien)].count(chr(10)) + 1} | 1 | {len(ancien)} | {len(nouveau)} |")
    return texte.replace(ancien, nouveau)


def main(racine: Path) -> int:
    c8, bloc = racine / C8, racine / BLOC
    if not sha(c8).startswith(SHA_C8_PREFIXE):
        raise SystemExit("candidat 8 : empreinte non conforme")
    if not sha(bloc).startswith(SHA_BLOC_PREFIXE):
        raise SystemExit("bloc v2 : empreinte non conforme")
    sortie = racine / C9
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    maintenant = datetime.now(timezone.utc)
    t = c8.read_text(encoding="utf-8")
    b = bloc.read_text(encoding="utf-8")
    texte_bloc = b[b.index("**Règle de lecture « mots et coût » (décisive).**"):b.index("## Ce que cette règle change par rapport à N-029")].rstrip("\n")
    journal = ["| couple | ligne | occurrences | longueur ancien | longueur nouveau |", "|---|---|---|---|---|"]
    # S1 statut
    t = un(t, "- Statut : **candidat 8**, écrit le ",
           f"- Statut : **candidat 9**, écrit le {maintenant.strftime('%Y-%m-%d')} à partir de {maintenant.strftime('%H:%M')} UTC (heure relevée par `date -u`) par la fille 10 (même rôle que ci-dessous). "
           f"**Candidat 9 = candidat 8 (`{sha(c8)}`, empreinte vérifiée avant tout) + les couples S1 à S4** : règle de lecture « mots et coût » (bloc v2, `{sha(bloc)}`) à la place du marqueur "
           "(option (b) adoptée par Lazar, R-1717, GO-2026-11-07-03) ; renvoi au bras B de l'audit de fuite (GO-2026-11-07-04) comme étape annexe ; règle de la fenêtre de carte "
           "(GO-2026-11-07-02). Les phrases qui suivent décrivent le candidat 8 sur lequel il s'appuie. Candidat 8 : écrit le ", "S1", journal)
    # S2 règle (le paragraphe entier, du titre à « scellable. »)
    debut = t.index("**Règle de lecture « mots et coût » (R-1704, candidat 8)")
    fin = t.index("le candidat n'est pas scellable.", debut) + len("le candidat n'est pas scellable.")
    paragraphe = t[debut:fin]
    reste = ("\n\n*Valeurs encore à fixer avant le scellement* (marquées « proposition » ci-dessus) : seuil d'échec de la base (0,70, alternative 0,65) et écart minimal de gain (0,05, "
             "à confirmer par le script de puissance) ; elles ne sont pas encore décidées.")
    annexe = (reste + "\n\n**Étape annexe — bras B de l'audit de fuite (GO-2026-11-07-04).** Après la course de T0.6 et la poussée de ses résultats, avant la destruction de l'instance, "
              "la machine de la course peut rejouer le contrefactuel de contexte du **bras B**, **régi par le texte de l'audit** `prereg/audit-fuite-r1-v4-v1.md` "
              f"(`910a53dc5ff00933c0d48b397cc7d164afc4e49c11f20c8ec257ae374aef7d84`, point 7) et **non par ce texte** ; elle ne change rien au run de T0.6 "
              "(ni ses entrées, ni ses sorties, ni ses règles de lecture) et aucune ligne de B ou de C ne la lit.")
    nouveau = ("**Règle de lecture « mots et coût », adoptée (option (b), Lazar, R-1717).** " + texte_bloc[len("**Règle de lecture « mots et coût » (décisive).**"):].lstrip(" ") + annexe)
    t = un(t, paragraphe, nouveau, "S2", journal)
    # S3 ligne du marqueur dans le tableau
    ligne = next(l for l in t.split("\n") if l.startswith("| `<<REGLE_MOTS_ET_COUT_T06>>` |"))
    t = un(t, ligne + "\n", "", "S3", journal)
    # S4 fenêtre
    t = un(t, "au plus 1,30 USD de l'heure (borne de P3, relue par les contrôles avant dépense). Une erreur de mémoire à la",
           "au plus 1,30 USD de l'heure (borne de P3, relue par les contrôles avant dépense). **Règle de la fenêtre (GO-2026-11-07-02, option (b) de Lazar, R-1700)** : le jour de la course, "
           "recherche d'une A100 SXM4 de 80 Go conforme (filtre complet, stockage au plus 0,08 USD de l'heure) **toutes les 15 minutes pendant 3 heures, soit 12 recherches à 0 USD** ; "
           "dès qu'une A100 conforme est rendue, création sur elle ; **sans A100 conforme au bout de la fenêtre**, `creation auto relance` sur la H200 NVL (au plus 4,70 USD de l'heure, "
           "au moins 140 Go de mémoire de carte, même filtre) ; plafond de 200 USD inchangé. Une erreur de mémoire à la", "S4", journal)
    if re.findall(r"\{[A-Z_0-9]+\}", t):
        raise SystemExit("accolades non résolues")
    marqueurs = sorted({m.strip("<>") for m in re.findall(r"<<[A-Z0-9_]+>>", t)})
    if set(marqueurs) != ATTENDUS:
        raise SystemExit(f"marqueurs : {marqueurs}, attendus {sorted(ATTENDUS)}")
    lignes = t.split("\n")
    comptes_c = {k: sum(1 for l in lignes if f"{k} : `" in l) for k in CLES}
    if comptes_c["Tests attendus"] != 1 or any(n > 1 for n in comptes_c.values()) or comptes_c["Entropie"] != 1:
        raise SystemExit(f"clés lues par la chaîne : {comptes_c}")
    sortie.write_text(t, encoding="utf-8")
    j = [f"# Journal du candidat 9 de T0.6 — {maintenant.strftime('%Y-%m-%dT%H:%M:%SZ')} (`date -u`)", "", f"- candidat 8 : `{C8}`, `{sha(c8)}` (vérifiée avant tout)",
         f"- bloc v2 : `{BLOC}`, `{sha(bloc)}`", f"- script : `appliquer-candidat9-v1.py`, `{sha(__file__)}`", "", *journal, "",
         f"Marqueurs du candidat 9, {len(marqueurs)} distincts (occurrences) :", "", *[f"- `{m}` : {t.count(f'<<{m}>>')}" for m in marqueurs], "",
         "Clés lues par la chaîne :", "", *[f"- « {k} : ` » : {n}" for k, n in comptes_c.items()], "", f"- résultat : `{C9}`, `{sha(sortie)}`, {t.count(chr(10)) + 1} lignes"]
    (ICI / "journal-candidat9-v1.md").write_text("\n".join(j) + "\n", encoding="utf-8")
    print("\n".join(j))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve()))
