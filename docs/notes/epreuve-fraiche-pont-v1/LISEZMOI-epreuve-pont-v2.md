# « Épreuve fraîche » du pont fiche → loi, premier essai — LISEZMOI v2

Rédigé le 1er novembre 2026, à partir du relevé `date -u` de 18:02 (fini à 18:06), par le même sous-agent rédacteur que la v1,
après la contre-lecture 1 (`contre-lecture-preregistrement-epreuve-pont-v1.md`, `b688ae1f…`, « scellable après corrections »,
CL-01 à CL-13), pour GO-2026-11-01-09 (plafond 5 dollars, échéance 2026-11-08). **Rien n'a été lancé** : aucun appel de modèle,
aucun appel réseau, aucune clé lue ; rien de scellé ni de commis ; aucun fichier existant modifié (les pièces v1 restent
telles quelles, R12). Le LISEZMOI v1 reste valable pour l'historique ; celui-ci le remplace pour l'exécution.

## Ce qui est prêt (v2)

| fichier | rôle | SHA-256 |
|---|---|---|
| `preregistrement-epreuve-pont-v2.md` | préenregistrement v2 = v1 + corrections ; contre-lecture remplie ; restent `<<COMMIT_DU_DEPOT>>` et `<<EMPREINTE_VALEUR_ENGAGEE>>` | `b981ae8c17c02b8cf5fc702163dc2df68ed8b9e57937462262e7d75372684645` |
| `tirer_fiches_v2.py` | tirage : refus sans inscription poussée des deux empreintes (CL-02) ; témoins dans la première moitié (CL-12) | `b61a9021db0a64a97236e1ea2f0acb275fdc9cd722f14abdb0bfc94d5c612d59` |
| `lancer_epreuve_pont_v2.py` | lanceur : Argon sans reprise interne (CL-05), symétrie en miroir (CL-01), lisibilité (CL-07), témoins contrôlés, scellés et inscrits (CL-09), transcription du sous-agent (CL-09), appels en cours et tronqués, anomalie v56 (CL-10), environnement du run (CL-11), garde du préambule (CL-04) | `be3c43e61641ab91444c92714269651a0722f81362a46d20a6efce3825781f9f` |
| `lancer-epreuve-pont-v2.sh` | lanceur shell (noms v2 ; commentaire des clés rendu exact, CL-13 a) | `c40b8527876e6a1231ecc292eb26e1c636279b98899101ceb934bf6c9f03d7b3` |
| `test_epreuve_pont_v2.py` | 126 essais hors réseau | `1a531edee5f7a22eae28fef9653bbccc2e1e1584e743440834cd1764353e25ba` |
| `consigne-metteur-en-forme-temoins-v2.md` | consigne fermée des témoins : T6 sans chiffre hors de `3B:RIGOR`, étiquettes T1–T6 interdites, contrôles annoncés (CL-03, CL-09) | `255ca007001662c98b6b5aa1ab485d08ec50763a473dc4c82d31005ad5ae3a11` |

Inchangés et repris par la v2 : `catalogue-public-t05-v2-pont-v1.json` (`90f2440a…`), `noyau-pont-t05-v2-v1.json` (`4c07e7b4…`),
`verite-temoins-v1.json` (`00030bb7…`), le module `pont/pont_v1.py` (`9fb2d936…`). Le tableau « Pièces gelées » du
préenregistrement v2 compte 18 pièces ; une copie remplie factice (bloc-notes) passe le validateur et la vérification des 18.

**Essais** (Python du dépôt, `-I -B`, depuis un dossier vide) : `test_epreuve_pont_v2.py` avec `PONT_POLE_V56` : **126 réussis** ;
sans : **114 réussis, 12 ignorés** avec leur motif ; `test_epreuve_pont_v1.py` (inchangé) : 83 réussis avec la v56 ;
`pont/test_pont_v1.py` : 82 réussis. Banc de mutations sur les gardes nouvelles (hors dépôt) : **25 tuées sur 25** (une survivante
au premier passage, « environnement du run factice », tuée par deux essais ajoutés : dépôt sans git refusé, contenu de
`environnement-run.json` contrôlé).

## Ordre exact des gestes (session-depot)

1. **Fait** : contre-lecture 1 ; v2 écrite. Recommandé (non exigé) : un coup d'œil neuf sur la v2 pour vérifier que chaque
   traitement annoncé dans la section « Contre-lecture » est bien dans le texte et le code.
2. **Valeur engagée**, une seule fois, hors du dépôt, jamais montrée avant le scellement, aucun tirage d'essai avec elle :
   `python3 -c "import secrets; print(secrets.token_hex(32))" > <bloc-notes>/valeur-engagee-pont-v2.txt` ;
   empreinte : `printf %s "$(cat <bloc-notes>/valeur-engagee-pont-v2.txt)" | sha256sum`.
3. **Remplir** dans `preregistrement-epreuve-pont-v2.md` : `<<EMPREINTE_VALEUR_ENGAGEE>>` (l'empreinte, entre accents graves) et
   `<<COMMIT_DU_DEPOT>>` (`git rev-parse --short HEAD`). La section « Contre-lecture » est déjà remplie.
4. **Sceller** (racine du dépôt, `PYTHONPATH=src`) :
   `python -c "from controle_ia.prereg import sceller_prereg; print(sceller_prereg('donnees/epreuve-fraiche-pont-v1/preregistrement-epreuve-pont-v2.md'))"`,
   puis `python -m controle_ia.scellement sceller` sur `tirer_fiches_v2.py`, `lancer_epreuve_pont_v2.py`,
   `lancer-epreuve-pont-v2.sh`, `test_epreuve_pont_v2.py`, `consigne-metteur-en-forme-temoins-v2.md`, `verite-temoins-v1.json`,
   `catalogue-public-t05-v2-pont-v1.json`, `noyau-pont-t05-v2-v1.json` (le lanceur exige ces compagnons).
5. **Inscrire et pousser (CL-02)** : une ligne de `registres/decisions.md` portant **en entier** l'empreinte du préenregistrement
   v2 scellé et celle de la valeur engagée ; commettre, pousser. Le tirage le vérifie sur le disque et dans la référence poussée.
6. **Tirage** : `cd donnees/epreuve-fraiche-pont-v1 && /home/user/controle-ia-travail/.venv/bin/python -I -B tirer_fiches_v2.py --valeur-engagee <bloc-notes>/valeur-engagee-pont-v2.txt --ref-poussee <référence poussée, par exemple origin/main>`
   → `fiches-tirees/F-01.json` … `F-08.json` et `manifeste-tirage-v2.json`. Ne pas ouvrir les fiches.
7. **Témoins** : déplier l'archive v56 hors du dépôt (commande du LISEZMOI v1, geste 6, dossier `<bloc-notes>/v56-epreuve-pont`) ;
   lancer **un sous-agent neuf** avec pour seule pièce `consigne-metteur-en-forme-temoins-v2.md` et, dans sa lettre de mission,
   `DOSSIER_V56=<bloc-notes>/v56-epreuve-pont/orchestrateur-v56` ; il écrit `temoins/T1.json` … `T6.json`. Puis :
   (a) `… lancer_epreuve_pont_v2.py verifier-transcription --transcription <fichier JSONL de la session du sous-agent>` (code 0
   exigé ; sinon témoins jetés, nouveau sous-agent neuf) ; (b) `… lancer_epreuve_pont_v2.py verifier-temoins --pole-v56 <…>` ;
   (c) sceller les six témoins ; (d) inscrire leurs six empreintes **en entier** dans `registres/decisions.md` (le lanceur l'exige).
8. **Lancement** (en tâche de fond ; ≈ 1 heure attendue, borne 7 000 secondes) :
   `cd donnees/epreuve-fraiche-pont-v1 && GO_ID=GO-2026-11-01-09 bash lancer-epreuve-pont-v2.sh lancer run-epreuve-pont-v2 3`
   (clés `GEMINI_API_KEY_2` et `KIMI_API_KEY` prises de l'environnement de la session). Sorties : `run-epreuve-pont-v2/` —
   `environnement-run.json` (commit, versions), `manifeste-run.json`, `items/item-kk/`, `journal.jsonl` (début et fin de chaque
   appel), `manifeste-run-fin.json`, `agregat-v2.json`, journal du relais Kimi (port 8802).
9. **Si refus** (R-750) : si la catégorie touche ce que nos règles interdisent, **aucun tour neuf**. Sinon : préambule plus
   technique et plus spécifique (domaine, vocabulaire défini ; ni sortie, ni code, ni témoin, ni épreuve : le lanceur le garde),
   scellé, puis `GO_ID=GO-2026-11-01-09 bash lancer-epreuve-pont-v2.sh reprendre-refus run-epreuve-pont-v2 <préambule> run-epreuve-pont-v2-reprise 3`
   (une seule fois ; plafond cumulé ; `agregat-reprise-v2.json`, avec les réponses du premier tour rapportées). Processus tué :
   `lancer_epreuve_pont_v2.py agreger --run run-epreuve-pont-v2` (appels en cours comptés au pire cas ; croiser avec le journal
   du relais Kimi).
10. **Lecture** par un **lecteur neuf** : critères L1 à L5 et règles de lisibilité gelés ; liste de symétrie en miroir (elle prime) ;
    réponses tronquées et anomalies de la vraie garde v56 lues à part ; concordance des empreintes des témoins entre le registre et
    `manifeste-run.json` ; lecture agrégée seule transmise à conv-audit.
11. **Consigner** : dépense, décisions, passation ; sceller la lecture.

## Ce qui reste à session-depot

Gestes 2 à 11. Coût estimé inchangé : ≈ 3,3 dollars (2,0 à 6,4, SUPPOSÉ) ; la garde peut arrêter avant la fin (des fiches
réelles d'abord, plus aucun témoin perdu tant qu'au plus sept passages le sont). Non vérifié faute d'appel réel : format des
réponses de Kimi et d'Argon à la consigne, durée des appels de Kimi, borne de sortie d'Argon pensées comprises (SUPPOSÉ : un
dépassement arrête le tour).
