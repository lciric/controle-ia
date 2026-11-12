"""Écrit les fichiers de couples de la contre-lecture de la chaîne de la course de T0.6 (rendus 5 à 7 de la fille 10) et les
éprouve : chaque « ancien » doit se trouver exactement une fois dans la pièce visée (lue par `git show <commit>:<chemin>`), les
couples sont appliqués dans l'ordre sur une copie, puis on revérifie que chaque « nouveau » est présent. N'écrit que les quatre
fichiers JSON (dossier de la contre-lecture) et les copies corrigées sous DOSSIER_JETABLE.

Usage : python -I ecrire_et_eprouver_couples_v1.py DEPOT DOSSIER_CONTRE_LECTURE DOSSIER_JETABLE
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

DEPOT, CL, JET = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
C7, C5 = "8cb539f9b7ecd20fab133bfffb590ca8e1fdfc63", "84a62edd30bc30f79bef69cbcc34c42c72cc8acd"
ORDRE = "docs/notes/g0-deux-semaines-v1/ordres-t06-course-v2/ordre-fille-6-t06-course-v2-brouillon.md"
DEVIS = "docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v3.md"
CAND = "brouillons/T0.6-organismes-v0-v1-candidat12-r2.md"
ADD = "docs/notes/g0-deux-semaines-v1/bras-b-v2/addendum-bras-b-v2-brouillon-v3.md"

COUPLES = {
    "couples-ordre-course-v2-v1.json": (C7, ORDRE, [
        {"id": "O1 (bloquant, constat neuf E3-6) préalable : point E3-6 d'E3 bis réglé avant toute création",
         "ancien": "6. Dossier de travail neuf (R12) : `W=$(mktemp -d)`.",
         "nouveau": "6. Dossier de travail neuf (R12) : `W=$(mktemp -d)`.\n7. **Point E3-6 d'E3 bis réglé avant toute création** (garde d'équivalence au 99ᵉ centile éprouvée sur un lot à dose 1 ; non conforme au compte rendu final d'E3 bis, R-1769) : la mère remplit `<<REGLEMENT_E3_6>>` par le numéro de la ligne de `registres/decisions.md` de `main` qui l'établit (dans le registre du clone de `main`, `grep -c '^| <numéro> |'` = 1). Cette ligne donne, pour chacun des six états d'E3 bis (S100, S25, S50, S75, T100, dose0), lus sur la branche `essai/t06-e3bis-v1` (`a5c0e298`) dans `diag/<run>/episodes-t06.json` → `fiches[k].equivalence` regroupées par `phase` (l'extracteur v1 lit `etats[<état>].equivalence`, clé que la chaîne n'écrit jamais : son « absent » ne dit rien de la garde), le nombre d'actions contrôlées, le plus grand écart au 99ᵉ centile et la tolérance (0,2), et la lecture du contrôle négatif (`controles_negatifs[<état>]`) ; si aucune action n'a été contrôlée (tirage de 5 % sur les 16 paires (tâche, pas) d'E3 bis, les mêmes pour toutes les conditions : probabilité ≈ 0,44), elle porte la décision de Lazar (la course est le premier exercice de cette garde à dose 1 sur une carte, ou épreuve neuve). Marqueur vide ou ligne introuvable : arrêt et message."},
        {"id": "O2 (bloquant, avec O1) marqueur neuf à remplir par la mère",
         "ancien": "remplit les marqueurs `<<COMMIT_COURSE>>`, `<<CONFIG_COURSE>>` et `<<EMPREINTE_PREREG_T06>>`)",
         "nouveau": "remplit les marqueurs `<<COMMIT_COURSE>>`, `<<CONFIG_COURSE>>`, `<<EMPREINTE_PREREG_T06>>` et `<<REGLEMENT_E3_6>>`)"},
        {"id": "O3 (moyen, constat neuf E3-3) attendus de la distillation : exemples et époques par adaptateur",
         "ancien": "« tests : N passed » ne doit pas manquer plus de **90 minutes** après `MATERIEL` (sinon attendu manquant) ;",
         "nouveau": "« tests : N passed » ne doit pas manquer plus de **90 minutes** après `MATERIEL` (sinon attendu manquant) ; **distillation** (point E3-3 d'E3 bis : le journal de distillation porte une entrée par époque plus l'époque 0, et non une entrée par pas) : `PROGRES … etape=donnees-distillation saboteur_exemples=160 temoin_exemples=160` (160 transcriptions par adaptateur au plan (b), lot 1, trois époques : 480 pas d'AdamW chacun ; un nombre moindre est un attendu manquant isolé, à relever sans arrêt : pas effectifs = 3 × exemples), puis, pour chaque adaptateur, `etape=distillation adaptateur=<a> epoque=1`, `epoque=2`, `epoque=3` et `etape=adaptateur adaptateur=<a>` ; relève leurs heures (secondes par pas ≈ durée de l'époque 1 à l'époque 3 du même adaptateur divisée par 320, évaluation de la perte comprise ; `distillation.duree_s` compte depuis le début du run, chargement et génération compris, et ne sert pas à ce calcul) ;"},
        {"id": "O4 (moyen) commit de la course : ce que vérifie `controles` du lanceur v12",
         "ancien": "`COMMIT=<<COMMIT_COURSE>>` (ancêtre de `refs/remotes/origin/prep/t06-course-v12` ;",
         "nouveau": "`COMMIT=<<COMMIT_COURSE>>` (le commit de scellement du préenregistrement de T0.6 : `controles` le retrouve lui-même, comme le dernier commit de l'histoire extraite qui ajoute `prereg/T0.6-organismes-v0-v1.md.sha256`, exige qu'il soit ancêtre de `origin/main` et l'imprime en `S=` ; la mère le choisit aussi ancêtre de `refs/remotes/origin/prep/t06-course-v12` ; `T06_BRANCHE_CODE` est sans effet sur `controles`, il ne sert qu'à `controles-epreuve` ;"},
    ]),
    "couples-devis-v3-v1.json": (C7, DEVIS, [
        {"id": "D1 (moyen) pire cas sous un débit moindre de la H200 NVL et heures exactes",
         "ancien": "**Le devis ne dépasse pas le plafond de 200 USD**, mais la marge est faible : **P4' à la borne de prix de 4,70 USD/h atteint ≈ 198 USD (marge ≈ 2 USD)** ; à 4,04 USD/h (prix constatés) 173 USD.",
         "nouveau": "**Le devis ne dépasse pas le plafond de 200 USD**, mais la marge est faible : **P4' à la borne de prix de 4,70 USD/h atteint ≈ 198 USD (marge ≈ 2 USD)** ; à 4,04 USD/h (prix constatés) 173 USD. **Ces pires cas supposent la H200 NVL au débit de l'A100 (réserve : non mesuré).** Avec les heures exactes (17,98 h et non 17,9), P4' à la borne vaut ≈ 198,5 USD (marge ≈ 1,5 USD) ; il dépasse 200 USD dès que la H200 NVL met 0,9 % de temps de plus que l'hôte A100 lent de P1' (P3' dès 8,9 %). La seule garde est alors l'arrêt par identifiant à 200 USD cumulés : l'instance serait détruite avant la fin du run, course perdue pour environ 200 USD. Recalcul : `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/scripts/recalcul_devis_v3_v1.py`."},
        {"id": "D2 (mineur) provenance du devis v2 (R6)",
         "ancien": "(`docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v2.md`, qui reste tel quel, R12)",
         "nouveau": "(`docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v2.md`, qui reste tel quel, R12 ; il n'est ni sur `main` ni parmi les ancêtres de ce commit : branche `prep/t06-candidat8-v1`, commit `c99d41e`, empreinte `f6f6195c…`, R-1707)"},
    ]),
    "couples-candidat12-r2-v1.json": (C7, CAND, [
        {"id": "W5 (moyen) titre de section exigé par `controle_ia.prereg` (sceller_prereg refuse « Hypothèses »)",
         "ancien": "\n## Hypothèses\n", "nouveau": "\n## Hypothèse\n"},
        {"id": "W6 (moyen) marqueur rempli, mention historique sans chevrons (statut)",
         "ancien": "(nouveau fichier, R12 ; `<<TESTS_ATTENDUS_T06>>` rempli par la voie (a)",
         "nouveau": "(nouveau fichier, R12 ; `TESTS_ATTENDUS_T06` rempli par la voie (a)"},
        {"id": "W7 (moyen) mention historique sans chevrons (candidat 12 initial)",
         "ancien": "sous GO-2026-11-07-08 ; `<<TESTS_ATTENDUS_T06>>` attend la dernière ligne exacte relevée à E3 bis",
         "nouveau": "sous GO-2026-11-07-08 ; `TESTS_ATTENDUS_T06` attendait la dernière ligne exacte relevée à E3 bis"},
        {"id": "W8 (moyen) mention historique sans chevrons (candidat 11)",
         "ancien": "le nombre attendu `<<TESTS_ATTENDUS_T06>>` est la dernière ligne de la **suite ciblée**",
         "nouveau": "le nombre attendu `TESTS_ATTENDUS_T06` est la dernière ligne de la **suite ciblée**"},
        {"id": "W9 (moyen) mention historique sans chevrons (table des changements)",
         "ancien": "« Tests attendus » reçoit `<<TESTS_ATTENDUS_T06>>` (en-tête, seule",
         "nouveau": "« Tests attendus » reçoit `TESTS_ATTENDUS_T06` (en-tête, seule"},
        {"id": "W10 (moyen) table des marqueurs : marqueur rempli",
         "ancien": "| `<<TESTS_ATTENDUS_T06>>` | dernière ligne exacte de la suite ciblée et figée",
         "nouveau": "| `TESTS_ATTENDUS_T06` (rempli) | dernière ligne exacte de la suite ciblée et figée"},
        {"id": "W11 (moyen) empreintes caduques de la chaîne v11 sous une règle « tout écart : nœud »",
         "ancien": "à recalculer au commit cité, tout écart : nœud). Raison : E3 du 7 novembre a échoué avant le run",
         "nouveau": "à recalculer au commit cité, tout écart : nœud ; **paragraphe historique** : la course joue la chaîne v12 ; les empreintes du lanceur v11, de l'amorce v9, de la liste figée v1 et de ses exclusions écrites ci-dessous sont antérieures au rendu 4 de la fille 10 et caduques (R12 ; contre-lecture de la v11, v2, « Forme ») ; au commit de la course elles valent `e134419b45c9ea976d48a1d3d1878afe375e47230e87ce137afb534edb29caaa`, `6a6897ce80c5c2cdd99e6f92d09f0e1da6a3c712c626d44ff70261409ac583c1`, `562b65facf1bcbf765f4e8b0d9e27c2c5b41edadb050701e7350bbce47081572` et `5fc2d5dbb016d35b7b251da3c9a87be2428f68bc6948bd52865d00d36ad0cff3`, et cet écart n'est pas un nœud). Raison : E3 du 7 novembre a échoué avant le run"},
        {"id": "W12 (mineur) qui scelle l'addendum v3 (comme l'ordre de la course et R-1761)",
         "ancien": "`2ec90141f10be13d0966a6a373946658a6fe38660898c138b5112c81a7c617f1`, à sceller par Lazar avant toute lecture du bras B)",
         "nouveau": "`2ec90141f10be13d0966a6a373946658a6fe38660898c138b5112c81a7c617f1`, à sceller par la session mère avant toute lecture du bras B, GO-2026-11-08-01)"},
    ]),
    "couples-addendum-bras-b-v3-v1.json": (C5, ADD, [
        {"id": "A1 (mineur) qui scelle l'addendum (comme l'ordre de la course et R-1761)",
         "ancien": "Texte à part, que Lazar scellera avant toute lecture du bras B.",
         "nouveau": "Texte à part, que la session mère scellera avant toute lecture du bras B (GO-2026-11-08-01 : « addendum à sceller avant toute lecture » ; R-1761)."},
    ]),
}

JET.mkdir(parents=True, exist_ok=True)
bilan = {}
for nom, (commit, chemin, couples) in COUPLES.items():
    texte = subprocess.run(["git", "-C", str(DEPOT), "show", f"{commit}:{chemin}"], capture_output=True, check=True).stdout.decode("utf-8")
    sha_avant = hashlib.sha256(texte.encode("utf-8")).hexdigest()
    comptes = []
    for c in couples:
        n = texte.count(c["ancien"])
        comptes.append(n)
        if n != 1:
            raise SystemExit(f"{nom} {c['id']} : « ancien » trouvé {n} fois : arrêt, rien écrit")
        texte = texte.replace(c["ancien"], c["nouveau"])
    presents = [texte.count(c["nouveau"]) >= 1 for c in couples]
    (CL / nom).write_text(json.dumps(couples, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    copie = JET / (Path(chemin).stem + "-avec-couples.md")
    copie.write_text(texte, encoding="utf-8")
    bilan[nom] = {"piece": chemin, "commit": commit[:8], "sha256_piece": sha_avant, "couples": len(couples), "anciens_trouves_une_fois": comptes,
                  "nouveaux_presents": presents, "copie_corrigee": str(copie), "sha256_copie": hashlib.sha256(texte.encode("utf-8")).hexdigest(),
                  "sha256_fichier_couples": hashlib.sha256((CL / nom).read_bytes()).hexdigest()}
print(json.dumps(bilan, ensure_ascii=False, indent=1))
