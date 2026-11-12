"""Candidat 11 = candidat 10 (`c4083ffc…`, vérifié avant tout) + les couples U1 à U9 : chaîne v11 de la course (lanceur v11, amorce v9, `session_v10`, `lanceur_v5`, `configuration_v5`, suite ciblée et figée,
bras B v2), nombre attendu relevé à E3 bis sur la suite ciblée. Nouveau fichier (R12). Chaque « ancien » doit se trouver exactement une fois, sinon arrêt sans rien écrire. Aucune section « Hypothèses » à
« Liste d'arrêt » n'est touchée. Les cinq marqueurs restent. Les empreintes citées sont lues dans l'arbre au moment de l'exécution et consignées au journal.

    python3 -I -B appliquer-candidat11-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
C10, PREFIXE = "brouillons/T0.6-organismes-v0-v1-candidat10.md", "c4083ffc38815f99"
C11 = "brouillons/T0.6-organismes-v0-v1-candidat11.md"
FICHIERS = {
    "lanceur": "scripts/lancer_t06_v11.sh", "amorce": "scripts/amorce_instance_t06_v9.sh", "session": "src/controle_ia/t06/session_v10.py",
    "lanceur5": "src/controle_ia/t06/lanceur_v5.py", "config5": "src/controle_ia/t06/configuration_v5.py", "liste": "scripts/tests-cibles-t06-v1.txt",
    "exclus": "scripts/tests-exclus-t06-v1.txt", "bras": "src/controle_ia/audit_fuite_r1_v4/bras_b_v2.py",
    "addendum": "docs/notes/g0-deux-semaines-v1/bras-b-v2/addendum-bras-b-v2-brouillon-v1.md", "rapport": "docs/notes/g0-deux-semaines-v1/rapport-e3-echecs-et-v11-v1.md",
    "e3bis": "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3bis-v1.json", "course": "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json",
}


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(racine: Path) -> int:
    src = racine / C10
    if not sha(src).startswith(PREFIXE):
        raise SystemExit("candidat 10 : empreinte non conforme")
    sortie = racine / C11
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

    une("U1 statut", "- Statut : **candidat 10**, écrit le 2026-11-07 à partir de 22:30 UTC",
        "- Statut : **candidat 11**, écrit le 2026-11-08 (heure relevée par `date -u`) par la fille 10 (même rôle que ci-dessous). **Candidat 11 = candidat 10 (`c4083ffc38815f99…`, empreinte vérifiée avant tout) + les couples U1 à U9** : "
        "le point d'entrée devient le **lanceur v11** (`scripts/lancer_t06_v11.sh`, qui cite l'amorce v9 et `session_v10.py`) ; l'amorce devient l'**amorce v9** (suite ciblée et figée, `lanceur_v5`, bras B v2 par défaut) ; "
        "le run est joué par **`lanceur_v5`** et validé par **`configuration_v5`** (la v4 refusait le plafond d'une épreuve hors de 1,5 et 3,5 USD : défaut d'E3, masqué par la suite complète échouée) ; le nombre attendu `<<TESTS_ATTENDUS_T06>>` "
        "est la dernière ligne de la **suite ciblée** relevée à **E3 bis**, et non plus de la suite complète. Les cinq marqueurs restent, à remplir au scellement. Les phrases qui suivent décrivent le candidat 10 sur lequel il s'appuie. "
        "Candidat 10 : écrit le 2026-11-07 à partir de 22:30 UTC")
    bullet = (
        "      - **chaîne v11 de la course (candidat 11 ; couples U1 à U9)** — branche `prep/t06-v11` (le commit du code est le marqueur `<<COMMIT_CODE_T06>>`, rempli au scellement ; les empreintes ci-dessous sont celles de l'arbre du "
        "8 novembre, à recalculer au commit cité, tout écart : nœud). Raison : E3 du 7 novembre a échoué avant le run (suite complète : 50 échecs dont 46 d'environnement et 4 défauts de test ou de portabilité, rapport "
        f"`{FICHIERS['rapport']}`, `{h['rapport']}`) et a masqué un défaut du run (plafond d'épreuve refusé au démarrage). **Lanceur v11** (`{FICHIERS['lanceur']}`, `{h['lanceur']}`) ; **amorce v9** (`{FICHIERS['amorce']}`, `{h['amorce']}` : "
        f"suite ciblée et figée dont l'empreinte est écrite en dur, jamais de repli sur la suite complète ; `lanceur_v5` ; bras B v2 par défaut) ; **`session_v10.py`** (`{h['session']}` : `{{\"instances\": null}}` est une absence probable, non concluante ; "
        f"identifiant du message comparé ; total du GO des épreuves 5 ou 8) ; **`lanceur_v5.py`** (`{h['lanceur5']}`, copie du v4 dont seuls l'import et le nom de la commande changent) ; **`configuration_v5.py`** (`{h['config5']}`, plafond d'épreuve de 0 à 8 USD) ; "
        f"**suite ciblée** `{FICHIERS['liste']}` (`{h['liste']}`) et exclusions motivées `{FICHIERS['exclus']}` (`{h['exclus']}`) ; **bras B v2** (`{FICHIERS['bras']}`, `{h['bras']}` ; l'issue n'est plus imprimée ; G4 sur le score de W en log-cote, "
        f"décision de Lazar R-1734) et son **addendum** (brouillon `{FICHIERS['addendum']}`, `{h['addendum']}`, à sceller par Lazar avant toute lecture du bras B) ; configuration de la course **brouillon 5** (`{h['course']}`, inchangée) ; "
        f"configuration d'**E3 bis** (`{FICHIERS['e3bis']}`, `{h['e3bis']}`). La v10 et ses citations restent plus haut pour mémoire (R12).\n"
        "      - **ce que le candidat 7 ne change pas**")
    une("U2 chaîne v11", "      - **ce que le candidat 7 ne change pas**", bullet)
    une("U3 amorce (en-tête)", "- Amorce : `scripts/amorce_instance_t06_v8.sh`", "- Amorce : `scripts/amorce_instance_t06_v9.sh`")
    une("U4 lanceur (devis)", "`scripts/lancer_t06_v10.sh` (empreinte `<<EMPREINTES_CODE_T06>>`)", "`scripts/lancer_t06_v11.sh` (empreinte `<<EMPREINTES_CODE_T06>>`)")
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

    sur_ligne("U5 lancement du 11 nov.", "| **11 nov. (mer.)**", lambda l: l.replace("scripts/lancer_t06_v10.sh", "scripts/lancer_t06_v11.sh"))
    sur_ligne("U6 table EMPREINTES_CODE", "| `<<EMPREINTES_CODE_T06>>`", lambda l: l.replace("modules v2 à v9 compris, dont `session_v4.py` à `session_v9.py`, `audit_fuite_r1_v4/bras_b_v1.py`",
        "modules v2 à v10 compris, dont `session_v4.py` à `session_v10.py`, `configuration_v5.py`, `lanceur_v5.py`, `audit_fuite_r1_v4/bras_b_v1.py`, `audit_fuite_r1_v4/bras_b_v2.py`").replace("scripts/amorce_instance_t06_v8.sh` et `scripts/lancer_t06_v10.sh`",
        "scripts/amorce_instance_t06_v9.sh`, `scripts/lancer_t06_v11.sh`, `scripts/tests-cibles-t06-v1.txt` et `scripts/tests-exclus-t06-v1.txt`"))
    sur_ligne("U7a table EMPREINTE_AMORCE", "| `<<EMPREINTE_AMORCE_T06>>`", lambda l: l.replace("scripts/amorce_instance_t06_v8.sh", "scripts/amorce_instance_t06_v9.sh"))
    sur_ligne("U7b table VALEURS_CITEES", "| `<<VALEURS_CITEES_T06>>`", lambda l: l.replace("scripts/lancer_t06_v10.sh", "scripts/lancer_t06_v11.sh"))
    sur_ligne("U7c citations lues par la chaîne", "Citations que la chaîne lit mécaniquement", lambda l: l.replace("scripts/lancer_t06_v10.sh", "scripts/lancer_t06_v11.sh").replace(
        "dernière ligne exacte de la suite complète au commit cité, rejouée sous l'image et `requirements-gpu.txt` de l'instance, épreuve E3 ;",
        "dernière ligne exacte de la suite ciblée et figée (`scripts/tests-cibles-t06-v1.txt`) au commit cité, rejouée sous l'image et `requirements-gpu.txt` de l'instance, épreuve E3 bis ;"))
    sur_ligne("U8a Tests attendus (en-tête)", "- Tests attendus : `<<TESTS_ATTENDUS_T06>>`", lambda l: l.replace("dernière ligne exacte de la suite complète", "dernière ligne exacte de la suite ciblée et figée (`scripts/tests-cibles-t06-v1.txt`, E3 bis)"))
    sur_ligne("U8b plan daté", "| **7 nov. (sam.)**", lambda l: l.replace("E3 relève la dernière ligne exacte de la suite complète sous l'image", "E3 bis relève la dernière ligne exacte de la suite ciblée et figée sous l'image"))
    sur_ligne("U8c table TESTS_ATTENDUS", "| `<<TESTS_ATTENDUS_T06>>`", lambda l: l.replace("dernière ligne exacte de la suite complète (`N passed`, aucun essai sauté) rejouée sous l'image et `requirements-gpu.txt` de l'instance, épreuve E3 ;",
        "dernière ligne exacte de la suite ciblée et figée (`N passed`, aucun essai sauté) rejouée sous l'image et `requirements-gpu.txt` de l'instance, épreuve E3 bis ;").replace("| E3, avant le scellement |", "| E3 bis, avant le scellement |"))
    t = "\n".join(lignes)
    marq = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", t)))
    assert len(marq) == 5, marq
    sortie.write_text(t, encoding="utf-8")
    (ICI / "journal-candidat11-v1.md").write_text(
        f"# Journal du candidat 11 (v1)\n\nÉcrit {datetime.now(timezone.utc):%Y-%m-%dT%H:%MZ}. Source : `{C10}` {sha(src)}. Sortie : `{C11}` {sha(sortie)}. Marqueurs distincts : {len(marq)} ({', '.join(marq)}).\n\n"
        + "\n".join(journal) + "\n\nEmpreintes lues dans l'arbre :\n\n" + "\n".join(f"- `{FICHIERS[k]}` {v}" for k, v in h.items()) + "\n", encoding="utf-8")
    print(sha(sortie), len(marq))
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
