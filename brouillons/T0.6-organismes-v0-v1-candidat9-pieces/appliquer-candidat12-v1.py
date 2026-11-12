"""Candidat 12 = candidat 11 (`9a1e2bcf…`, vérifié avant tout) + les couples V1 à V8 : chaîne v12 de la course (lanceur v12, amorce v10, `session_v11`, `lanceur_v5`, `configuration_v5`, bras B v4, suite ciblée
figée v2), configuration d'E3 bis v3, addendum v3, réserves de la contre-lecture de la v11 (v2) traitées (validation de `T06_TESTS_ATTENDUS`, essai de la vérification de GO-2026-11-06-01 à la création,
banc strict sur le code 5 de pytest). Nouveau fichier (R12). Chaque « ancien » doit se trouver exactement une fois, sinon arrêt sans rien écrire. Aucune section « Hypothèses » à « Liste d'arrêt » n'est touchée.
Les cinq marqueurs restent ; `<<TESTS_ATTENDUS_T06>>` attend la dernière ligne exacte relevée à E3 bis : jamais inventée. Les empreintes sont lues dans l'arbre à l'exécution et consignées au journal.

    python3 -I -B appliquer-candidat12-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
C11, PREFIXE = "brouillons/T0.6-organismes-v0-v1-candidat11.md", "9a1e2bcf6b2b878e"
C12 = "brouillons/T0.6-organismes-v0-v1-candidat12.md"
FICHIERS = {
    "lanceur": "scripts/lancer_t06_v12.sh", "amorce": "scripts/amorce_instance_t06_v10.sh", "session": "src/controle_ia/t06/session_v11.py",
    "lanceur5": "src/controle_ia/t06/lanceur_v5.py", "config5": "src/controle_ia/t06/configuration_v5.py", "bras": "src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py",
    "liste": "scripts/tests-cibles-t06-v2.txt", "exclus": "scripts/tests-exclus-t06-v2.txt", "banc": "scripts/banc_mutations_bras_b_v5.py",
    "addendum": "docs/notes/g0-deux-semaines-v1/bras-b-v2/addendum-bras-b-v2-brouillon-v3.md", "rapport": "docs/notes/g0-deux-semaines-v1/rapport-e3-echecs-et-v11-v2.md",
    "e3bis": "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3bis-v3.json", "course": "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json",
    "cfgbras": "docs/notes/g0-deux-semaines-v1/config-bras-b-t06-v1.json",
}


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(racine: Path) -> int:
    src = racine / C11
    if not sha(src).startswith(PREFIXE):
        raise SystemExit("candidat 11 : empreinte non conforme")
    sortie = racine / C12
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    h = {k: sha(racine / v) for k, v in FICHIERS.items()}
    t = src.read_text(encoding="utf-8")
    journal = ["| couple | occurrences avant | effet |", "|---|---|---|"]

    def une(nom, ancien, nouveau):
        nonlocal t
        n = t.count(ancien)
        if n != 1:
            raise SystemExit(f"{nom} : « {ancien[:70]}… » trouvé {n} fois, une attendue : arrêt, rien écrit")
        journal.append(f"| {nom} | 1 | {len(ancien)} → {len(nouveau)} caractères |")
        t = t.replace(ancien, nouveau)

    une("V1 statut", "- Statut : **candidat 11**, écrit le 2026-11-08 (heure relevée par `date -u`)",
        "- Statut : **candidat 12**, écrit le 2026-11-08 (heure relevée par `date -u`) par la fille 10 (même rôle que ci-dessous). **Candidat 12 = candidat 11 (`9a1e2bcf6b2b878e…`, empreinte vérifiée avant tout) + les couples V1 à V8** : "
        "le point d'entrée devient le **lanceur v12** (`scripts/lancer_t06_v12.sh`, qui valide `T06_TESTS_ATTENDUS` et cite l'amorce v10 et `session_v11.py`) ; l'amorce devient l'**amorce v10** (bras B v4 par défaut, suite ciblée figée v2) ; "
        "le bras B est la **v4** (tolérance de G4 0,3 en log-cote, borne incluse, lecture stricte : décision de Lazar, GO-2026-11-08-01) avec son addendum v3 ; E3 bis a joué la configuration **v3** (borne de prix de l'A100 relevée à 2,10 USD/h, R-1755) "
        "sous GO-2026-11-07-08 ; `<<TESTS_ATTENDUS_T06>>` attend la dernière ligne exacte relevée à E3 bis (jamais inventée). Les cinq marqueurs restent, à remplir au scellement. Les phrases qui suivent décrivent le candidat 11 sur lequel il s'appuie. "
        "Candidat 11 : écrit le 2026-11-08 (heure relevée par `date -u`)")
    bullet = (
        "      - **chaîne v12 de la course (candidat 12 ; couples V1 à V8)** — branche `prep/t06-course-v12` (le commit du code est le marqueur `<<COMMIT_CODE_T06>>`, rempli au scellement ; les empreintes ci-dessous sont celles de l'arbre du 8 novembre, "
        "à recalculer au commit cité, tout écart : nœud). **Pourquoi une chaîne v12** : l'ordre scellé d'E3 bis cite l'amorce v9 et la liste figée v1 par empreinte (la liste est écrite en dur dans l'amorce) et ne pouvait pas changer ; la course joue le bras B v4 et "
        f"valide `T06_TESTS_ATTENDUS`, d'où un lanceur, une amorce et une liste de nom neuf (R12). **Lanceur v12** (`{FICHIERS['lanceur']}`, `{h['lanceur']}` : lanceur v11 plus `T06_TESTS_ATTENDUS` validé `^[0-9]*$`, cite l'amorce v10) ; "
        f"**amorce v10** (`{FICHIERS['amorce']}`, `{h['amorce']}` : amorce v9 plus `bras_b_v4` par défaut et la liste v2 ; trois lignes changent) ; **`session_v11.py`** (`{h['session']}` : un identifiant différent de celui demandé est non concluant, total du GO lié à "
        f"`GO-2026-11-06-01` ou `GO-2026-11-07-08`, dépense antérieure ≥ 2,092 sous ce dernier) ; **`lanceur_v5.py`** (`{h['lanceur5']}`) et **`configuration_v5.py`** (`{h['config5']}`) ; **bras B v4** (`{FICHIERS['bras']}`, `{h['bras']}`, tolérance 0,3 incluse, lecture stricte) ; "
        f"**suite ciblée figée v2** `{FICHIERS['liste']}` (`{h['liste']}`) et exclusions motivées `{FICHIERS['exclus']}` (`{h['exclus']}`) ; banc de mutations du bras B strict sur le code 5 de pytest `{FICHIERS['banc']}` (`{h['banc']}`) ; "
        f"**addendum v3** (brouillon `{FICHIERS['addendum']}`, `{h['addendum']}`, à sceller par Lazar avant toute lecture du bras B) ; configuration d'**E3 bis v3** (`{FICHIERS['e3bis']}`, `{h['e3bis']}`) ; rapport `{FICHIERS['rapport']}` (`{h['rapport']}`) ; "
        f"configuration du bras B `{FICHIERS['cfgbras']}` (`{h['cfgbras']}`, inchangée) ; configuration de la course brouillon 5 (`{h['course']}`, inchangée). **Réserves de la contre-lecture de la v11 (v2) traitées** : validation de `T06_TESTS_ATTENDUS` ; "
        "essai de la vérification de GO-2026-11-06-01 à la création (mutation L2 tuée) ; banc strict sur le code 5 de pytest. **Non traitée ici** : la borne de l'annexe du bras B reste 2 400 s dans l'amorce (le pire cas d'environ 5 800 s est écrit à l'ordre de la course). "
        "La v11 et ses citations restent plus haut pour mémoire (R12).\n"
        "      - **ce que le candidat 7 ne change pas**")
    une("V2 chaîne v12", "      - **ce que le candidat 7 ne change pas**", bullet)
    une("V3 amorce (en-tête)", "- Amorce : `scripts/amorce_instance_t06_v9.sh`", "- Amorce : `scripts/amorce_instance_t06_v10.sh`")
    une("V4 lanceur (devis)", "`scripts/lancer_t06_v11.sh` (empreinte `<<EMPREINTES_CODE_T06>>`)", "`scripts/lancer_t06_v12.sh` (empreinte `<<EMPREINTES_CODE_T06>>`)")
    lignes = t.split("\n")

    def sur_ligne(nom, debut, f):
        idx = [i for i, l in enumerate(lignes) if l.startswith(debut)]
        if len(idx) != 1:
            raise SystemExit(f"{nom} : début {debut!r} trouvé {len(idx)} fois, une attendue")
        avant = lignes[idx[0]]
        lignes[idx[0]] = f(avant)
        if lignes[idx[0]] == avant:
            raise SystemExit(f"{nom} : aucun changement")
        journal.append(f"| {nom} | 1 | ligne {idx[0] + 1} modifiée |")

    sur_ligne("V5 lancement du 11 nov.", "| **11 nov. (mer.)**", lambda l: l.replace("scripts/lancer_t06_v11.sh", "scripts/lancer_t06_v12.sh"))
    sur_ligne("V6 table EMPREINTES_CODE", "| `<<EMPREINTES_CODE_T06>>`", lambda l: l.replace("modules v2 à v10 compris, dont `session_v4.py` à `session_v10.py`", "modules v2 à v11 compris, dont `session_v4.py` à `session_v11.py`")
              .replace("`audit_fuite_r1_v4/bras_b_v2.py` et ses copies", "`audit_fuite_r1_v4/bras_b_v4.py` et ses copies").replace("scripts/amorce_instance_t06_v9.sh`, `scripts/lancer_t06_v11.sh`, `scripts/tests-cibles-t06-v1.txt` et `scripts/tests-exclus-t06-v1.txt`",
              "scripts/amorce_instance_t06_v10.sh`, `scripts/lancer_t06_v12.sh`, `scripts/tests-cibles-t06-v2.txt` et `scripts/tests-exclus-t06-v2.txt`"))
    sur_ligne("V7a table EMPREINTE_AMORCE", "| `<<EMPREINTE_AMORCE_T06>>`", lambda l: l.replace("scripts/amorce_instance_t06_v9.sh", "scripts/amorce_instance_t06_v10.sh"))
    sur_ligne("V7b table VALEURS_CITEES", "| `<<VALEURS_CITEES_T06>>`", lambda l: l.replace("scripts/lancer_t06_v11.sh", "scripts/lancer_t06_v12.sh"))
    sur_ligne("V8 citations lues par la chaîne", "Citations que la chaîne lit mécaniquement", lambda l: l.replace("scripts/lancer_t06_v11.sh", "scripts/lancer_t06_v12.sh").replace(
        "`scripts/tests-cibles-t06-v1.txt`", "`scripts/tests-cibles-t06-v2.txt`"))
    t = "\n".join(lignes)
    marq = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", t)))
    assert len(marq) == 5, marq
    sortie.write_text(t, encoding="utf-8")
    (ICI / "journal-candidat12-v1.md").write_text(
        f"# Journal du candidat 12 (v1)\n\nÉcrit {datetime.now(timezone.utc):%Y-%m-%dT%H:%MZ}. Source : `{C11}` {sha(src)}. Sortie : `{C12}` {sha(sortie)}. Marqueurs distincts : {len(marq)} ({', '.join(marq)}).\n\n"
        + "\n".join(journal) + "\n\nEmpreintes lues dans l'arbre :\n\n" + "\n".join(f"- `{FICHIERS[k]}` {v}" for k, v in h.items()) + "\n", encoding="utf-8")
    print(sha(sortie), len(marq))
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
