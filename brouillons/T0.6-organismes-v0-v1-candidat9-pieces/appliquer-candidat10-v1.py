"""Candidat 10 = candidat 9, révision 2 (`0050ab33…`, vérifié avant tout) + couples comptés T1 à T7 (citations portées au lanceur v10, à l'amorce v8, à session_v9,
au bras B, à la fenêtre de carte et à la configuration brouillon 5). Nouveau fichier (R12). Chaque « ancien » doit se trouver exactement une fois, sinon arrêt sans rien écrire.
Aucune section « Hypothèses » à « Liste d'arrêt » n'est touchée. Les cinq marqueurs restent.

    python3 -I -B appliquer-candidat10-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
C9R2, PREFIXE = "brouillons/T0.6-organismes-v0-v1-candidat9-r2.md", "0050ab3385d098f2"
C10 = "brouillons/T0.6-organismes-v0-v1-candidat10.md"
L9, A7 = "scripts/lancer_t06_v9.sh", "scripts/amorce_instance_t06_v7.sh"

T1 = ("- Statut : **candidat 9**, écrit le 2026-11-07 à partir de 21:21 UTC",
      "- Statut : **candidat 10**, écrit le 2026-11-07 à partir de 22:30 UTC (heure relevée par `date -u`) par la fille 10 (même rôle que ci-dessous). **Candidat 10 = candidat 9, révision 2 "
      "(`0050ab3385d098f2…`, empreinte vérifiée avant tout) + les couples comptés T1 à T7** : le point d'entrée devient le **lanceur v10** (`scripts/lancer_t06_v10.sh`, qui cite l'amorce v8 et "
      "`session_v9.py`) ; l'amorce devient l'**amorce v8** (`scripts/amorce_instance_t06_v8.sh`, bras B de l'audit de fuite en annexe après la dernière poussée) ; la configuration à copier sous "
      "`prereg/` est le **brouillon 5** (`docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json`, seul changement par rapport au brouillon 4 : `offre.stockage_max_usd_h` à 0,08). "
      "Les cinq marqueurs restent, à remplir au scellement. Les phrases qui suivent décrivent le candidat 9 sur lequel il s'appuie. "
      "Candidat 9 : écrit le 2026-11-07 à partir de 21:21 UTC")

T2 = ("      - **ce que le candidat 7 ne change pas**",
      "      - **chaîne v10 de la course (candidat 10 ; couples T1 à T7)** — branche d'intégration `prep/t06-course-v1` (le commit du code est le marqueur `<<COMMIT_CODE_T06>>`, rempli au scellement ; "
      "les empreintes ci-dessous sont celles de la tête du 7 novembre à 22:10 UTC, à recalculer au commit cité, tout écart : nœud) : **lanceur v10** (`scripts/lancer_t06_v10.sh`, "
      "`b98e84cf681886af8ed2ba850c1633e123bf8f492528ec1ea159872605aa1a07`, à la place du v9 : `instance_seule` ne conclut à l'absence que sur un 404 exact, quatre essais R5 de la contre-lecture "
      "du v9) ; **amorce v8** (`scripts/amorce_instance_t06_v8.sh`, `29913ace7105f00e96d5563d2e42c00820e5e9fa52b76789585899bcc2bac2fa`, à la place de la v7 : v7 plus le bras B, étape annexe "
      "qui ne peut pas faire échouer la course) ; **`session_v9.py`** (`d0443323d4ae2b7488c775759b23606d11fb910c87887cb52c9a4665841f2968`) ; **bras B** (`src/controle_ia/audit_fuite_r1_v4/bras_b_v1.py`, "
      "`afacfedb4cca0cc0490c35588d22d4454f614de5a9d9a88e6a88d52b6d02805d`, sa configuration `docs/notes/g0-deux-semaines-v1/config-bras-b-t06-v1.json`, "
      "`4fb0da2047730b3b86e9050b035e3bca57bd33e568cf6b55bc78517214d542b8`, scellée par la mère ; copies sans modification, 27 fichiers, manifeste `docs/notes/g0-deux-semaines-v1/bras-b-copies-manifeste-v1.md`) ; "
      "**fenêtre de carte** (`scripts/fenetre_carte_t06_v1.sh`, `bc0a67c39dda59264caf1c8389a4255a393ff0542abd7b719bed2f224d8b59ea`, GO-2026-11-07-02) ; **configuration de la course, brouillon 5** "
      "(`b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`, stockage à 0,08 USD de l'heure pour les deux cartes, clause de mémoire en Go : 78 pour la carte de course, 136 pour la relance ; "
      "plafond 200 USD, GO-2026-11-02-28 et téléchargement à 0,05 au plus inchangés) et son essai `tests/test_t06_config_course_brouillon5.py` "
      "(`92648cdb16ba29c4b9b9457dc927abdebe2432064d3b47d7a37ed3db9bbb8249`). Les citations de la v9 plus haut restent pour mémoire (R12) ; la configuration du brouillon 4 citée aux lignes de chemins "
      "et d'empreintes plus bas est remplacée par le brouillon 5 pour tout ce qui concerne le stockage ; aucune autre valeur n'a changé.\n"
      "      - **ce que le candidat 7 ne change pas**")


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(racine: Path) -> int:
    src = racine / C9R2
    if not sha(src).startswith(PREFIXE):
        raise SystemExit("candidat 9 révision 2 : empreinte non conforme")
    sortie = racine / C10
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    t = src.read_text(encoding="utf-8")
    lignes = t.split("\n")
    journal = ["| couple | occurrences avant | effet |", "|---|---|---|"]

    def une_fois(nom, ancien, nouveau, texte):
        n = texte.count(ancien)
        if n != 1:
            raise SystemExit(f"{nom} : « {ancien[:60]}… » trouvé {n} fois, une attendue : arrêt, rien écrit")
        journal.append(f"| {nom} | 1 | {len(ancien)} → {len(nouveau)} caractères |")
        return texte.replace(ancien, nouveau)

    t = une_fois("T1 statut", *T1, t)
    t = une_fois("T2 chaîne v10", *T2, t)
    # T3 à T6 : lignes précises, repérées par un début exact, une seule ligne chacune
    def sur_ligne(nom, debut, f):
        global_idx = [i for i, l in enumerate(lignes) if l.startswith(debut)]
        if len(global_idx) != 1:
            raise SystemExit(f"{nom} : début de ligne {debut!r} trouvé {len(global_idx)} fois, une attendue")
        i = global_idx[0]
        avant = lignes[i]
        lignes[i] = f(avant)
        if lignes[i] == avant:
            raise SystemExit(f"{nom} : aucun changement")
        journal.append(f"| {nom} | 1 | ligne {i + 1} modifiée |")
    lignes = t.split("\n")
    sur_ligne("T3 amorce (en-tête)", "- Amorce : `" + A7, lambda l: l.replace(A7, "scripts/amorce_instance_t06_v8.sh"))
    sur_ligne("T4 lanceur (devis)", "`" + L9 + "` (empreinte `<<EMPREINTES_CODE_T06>>`)", lambda l: l.replace(L9, "scripts/lancer_t06_v10.sh"))
    sur_ligne("T5 lancement du 11 nov.", "| **11 nov. (mer.)**", lambda l: l.replace(L9, "scripts/lancer_t06_v10.sh"))
    sur_ligne("T6a table EMPREINTES_CODE", "| `<<EMPREINTES_CODE_T06>>`", lambda l: l.replace("modules v2 à v8 compris, dont `session_v4.py` à `session_v8.py`", "modules v2 à v9 compris, dont `session_v4.py` à `session_v9.py`, "
        "`audit_fuite_r1_v4/bras_b_v1.py` et ses copies du manifeste").replace(A7, "scripts/amorce_instance_t06_v8.sh").replace(L9, "scripts/lancer_t06_v10.sh").replace("scripts/lancer_t06_v10.sh,", "scripts/lancer_t06_v10.sh,"))
    sur_ligne("T6b table EMPREINTE_AMORCE", "| `<<EMPREINTE_AMORCE_T06>>`", lambda l: l.replace(A7, "scripts/amorce_instance_t06_v8.sh"))
    sur_ligne("T6c table VALEURS_CITEES", "| `<<VALEURS_CITEES_T06>>`", lambda l: l.replace(L9, "scripts/lancer_t06_v10.sh"))
    sur_ligne("T7 citations lues par la chaîne", "Citations que la chaîne lit mécaniquement", lambda l: l.replace(L9, "scripts/lancer_t06_v10.sh"))
    t = "\n".join(lignes)
    sortie.write_text(t, encoding="utf-8")
    marq = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", t)))
    assert len(marq) == 5, marq
    (ICI / "journal-candidat10-v1.md").write_text(
        f"# Journal du candidat 10 (v1)\n\nÉcrit {datetime.now(timezone.utc):%Y-%m-%dT%H:%MZ}. Source : `{C9R2}` {sha(src)}. Sortie : `{C10}` {sha(sortie)}. Marqueurs distincts : {len(marq)} ({', '.join(marq)}).\n\n"
        + "\n".join(journal) + "\n", encoding="utf-8")
    print(sha(sortie), len(marq))
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
