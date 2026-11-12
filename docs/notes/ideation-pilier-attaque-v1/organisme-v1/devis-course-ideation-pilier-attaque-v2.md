# Devis v2 — course d'idéation de l'organisme sur la question scellée v1 du pilier attaque

Écrit par la session mère `session_016QhUrrLeN21G7Z9KZobE42` le 8 novembre 2026 vers 12:45 UTC (`date -u`). Remplace le devis v1 de la fille idéation 1 (`c5cab7ce…`, non retenu, R-1794 : structure non conforme au code). **Aucune dépense engagée par ce devis** : la course part sur la ligne GO-2026-11-08-08 (sous l'autonomie GO-2026-11-08-05) **et** sur le mot écrit de Lazar dans la session de la fille qui l'exécute.

## 1. Ce qui est mesuré (zéro dollar, session mère, dépôt public `lciric/ideation-organism` attaché à la session, `8947bc8`)
- **Mesure des consignes** (`ideation_v8.py --mesurer-consignes`, sans appel, sans écriture ; sortie recopiée : `mesurer-consignes-pilier-attaque-v1.json`) : question 4 255 caractères ; pièce et pièce-juge (synthèse d'antériorité `48adeac0…`) 10 151 ; **consigne de passe 1 : 16 856 caractères** ; consigne de passe 2 **maximale** : 370 997 (8 fiches à la taille maximale admise, 44 259) ; consigne du juge **maximale** : 2 141 816 (48 fiches) ; contrôle externe 371 472 ; nombre de proposeurs 3, 8 fiches par proposeur et par passe, seconde passe. Gardes : course `passerait: true` (plafond 520 000 caractères) ; passe 1 d'Argon `passerait: true` (coût d'entrée 0,042 USD) ; passe 2 d'Argon : passe au réglage réaliste (fiches de passe 1 ≤ 8 000 caractères provisionnées), **ne passerait pas** au pire cas théorique (fiches à 44 259) — alors la course refuse la passe 2 d'Argon **avant tout appel**, sans dépense.
- **Passe simulée complète** (`--moteur simule`, graine 20261108 ; sorties recopiées sous `passe-simulee-v1/`) : 8 sessions (3 proposeurs × 2 passes, 2 juges), 15 fiches validées (Opus 6, Fable 4, Argon 5), 0 refusée, 0 en quarantaine ; manifestes de départ et de fin scellés ; **code 4** (« témoins échoués chez un juge ») — attendu en simulation : les juges scriptés ne signalent aucun doublon (le témoin jumeau ne peut pas tenir) et notent par une règle fixe non sémantique (les deux témoins faux ne peuvent pas tenir) ; le témoin vrai tient chez les deux juges. La plomberie est vérifiée ; la sémantique des témoins relève des vrais juges.
- **Témoins plantés** (CL31-03) : écrits par la mère (tiers, ni proposeur ni juge) : `temoins-pilier-attaque-v1.json` — quatre classes imposées (vrai « contrôle placebo de l'identité de l'organisme », jumeau, faux-falsifiabilité « indice global de crédibilité », faux-antériorité « sondes linéaires présentées comme inédites ») ; **validés par le chargeur du noyau** (`charger_temoins` : quatre classes, aucun signal de la garde du niveau méthode).
- **Sonde de la garde refus-question** (R-1788) : simulée 3/3 ; **réelle à faire** avant la course (Opus 5.5, Fable 5.1, Argon ; ≈ 0,003 USD) ; un modèle qui refuse est retiré de tous les rôles.

## 2. Barème et hypothèses
- Barème du noyau (`pole/relais_reel.py`, USD par million de jetons, entrée / sortie) : **Opus 5.5 : 4 / 20** ; **Fable 5.1 : 10 / 50** ; Argon par commande externe : **0,31 à 0,49 USD par appel mesurés** sur le collisionneur E3 (R-1792), 0,45 retenu par passe.
- Jetons ≈ caractères / 4. Passe 1 : 4 200 jetons d'entrée ; passe 2 réaliste : ≈ 49 000 caractères (consigne + 8 fiches de 4 000) ≈ 12 300 jetons ; sortie d'une passe : 8 fiches × 3 000 caractères ≈ 6 000 jetons. Juge : ≈ 30 fiches validées + 4 témoins + pièce ≈ 146 000 caractères ≈ 36 500 jetons d'entrée, ≈ 3 000 de sortie. Contrôles : 5 appels courts.

## 3. Coût attendu
| Poste | Calcul | USD |
|---|---|---|
| Proposeur Opus 5.5, deux passes | (4 200·4 + 6 000·20) + (12 300·4 + 6 000·20) ·10⁻⁶ | 0,31 |
| Proposeur Fable 5.1, deux passes | (4 200·10 + 6 000·50) + (12 300·10 + 6 000·50) ·10⁻⁶ | 0,77 |
| Proposeur externe Argon, deux passes | 2 × 0,45 | 0,90 |
| Juge Opus 5.5 | 36 500·4 + 3 000·20 ·10⁻⁶ | 0,21 |
| Juge Fable 5.1 | 36 500·10 + 3 000·50 ·10⁻⁶ | 0,52 |
| Bras rapporté différé, juge Argon | un appel long | 0,50 |
| Appels de contrôle (5) et sonde de la garde (3) | | 0,03 |
| **Total attendu, Fable acceptée** | | **≈ 3,2** |
| **Total attendu, Fable refusée par la sonde** (Opus + Argon ; un juge Claude) | | **≈ 1,9** |

## 4. Pire cas et plafond proposé
- Plafonds par session Claude (déjà dans la ligne de commande) : proposeurs 2,5 + 2,5 ; juges 1,5 + 1,5 = **8** ; contrôles compris dans le total Claude. Argon : passe 1 2,5 + passe 2 2,5 + juge 2,5 = 7,5 (+ contrôle) → **total externe 8** (la somme des plafonds externes doit tenir sous le total externe, CL37-03 : vérifié en simulation).
- **Plafond proposé : 20 USD** = `--budget-total-usd 12.0` (Claude, contrôles compris) + `--budget-externe-usd 8.0` (Argon). Toute session qui atteint son plafond arrête la course proprement (code 2), sans dépassement.
- Risques chiffrés : refus de Fable à la sonde (−1,3 USD, un juge de moins : moyenne à deux juges puis médiane avec Argon) ; fiches de passe 1 au-dessus de 8 000 caractères → passe 2 d'Argon refusée avant appel (perte : la seconde passe d'Argon) ; juge externe sans réponse → classement à deux juges « sans juge externe » (code 5).

## 5. Commandes (fille idéation 1, environnement « Default », après la ligne de GO et le mot de Lazar dans sa session)
Préalables : relais de clé du noyau lancé avec `--modeles-permis` **exactement** égal aux modèles Claude de la course (`claude-opus-5-5,claude-fable-5-1`, ou `claude-opus-5-5` seul si Fable refuse) ; commande externe d'Argon v2 (celle qui demande toujours `gemini-4-argon` et rend `modele_servi`) ; liste blanche reconstruite **sur sa machine** (`--construire-liste-blanche` : question, synthèse, témoins) ; `GEMINI_API_KEY_2` jamais.
1. **Sonde réelle de la garde** : `PYTHONPATH=src python -I -m controle_ia.garde_refus_question_v1` enveloppée autour des appels réels (protocole `Appelant`) ; bilan JSON versé ; retirer tout modèle qui refuse de **tous** les rôles.
2. **Course (a)** : `python -I -B demonstrations/ideation_v8.py SORTIE --liste-blanche L.json --question Q.md --piece S.md --piece-juge S.md --temoins temoins-pilier-attaque-v1.json --proposeur opus=claude-opus-5-5 [--proposeur fable=claude-fable-5-1] --proposeur-externe argon=gemini-4-argon --commande-externe "…Argon v2…" --juge opus-juge=claude-opus-5-5 [--juge fable-juge=claude-fable-5-1] --juge-externe argon-juge=gemini-4-argon --seconde-passe --nombre 8 --budget-total-usd 12.0 --budget-externe-usd 8.0 --budget "proposeur_ideation|claude-opus-5-5=2.5" [--budget "proposeur_ideation|claude-fable-5-1=2.5"] --budget "juge_ideation|claude-opus-5-5=1.5" [--budget "juge_ideation|claude-fable-5-1=1.5"] --moteur claude-sdk --url-relais http://127.0.0.1:PORT --confirmer-moteur-reel --horodatage "$(date -u)"` — la course n'écrit aucun classement tant que le juge externe est attendu.
3. **Lecture humaine attestée** des fiches validées (la mère ou Lazar), scellée : `{"lecteur", "lu_le", "fiches_validees_sha256", "consignes_en_attente_sha256"}`.
4. **Bras (b)** : `… SORTIE --bras-rapporte-differe --attestation-lecture-humaine ATT.json --juge-externe argon-juge=gemini-4-argon --commande-externe "…" --liste-blanche L.json` → classement à trois juges (médiane).
5. Après la course : relecture « aucune recette » de **toutes** les fiches validées par la mère avant tout usage (R-607 ; le portier scelle au coffre ce qui glisse vers le concret).

## 6. Pièces de ce devis
`temoins-pilier-attaque-v1.json`, `mesurer-consignes-pilier-attaque-v1.json`, `passe-simulee-v1/{manifeste-depart,manifeste-fin,lecture}.json`, chacune avec compagnon `.sha256`.
