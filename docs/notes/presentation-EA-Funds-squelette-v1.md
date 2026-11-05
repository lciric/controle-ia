# Présentation EA Funds — squelette de l'appel de 30 minutes — v1

Session 14, 2026-10-20 (R-267). Pour Lazar, qui parle seul à l'appel (contact externe : Lazar décide et envoie). Sources sur
le format et les questions : recherche web de Gemini (requête 012 du canal, réponse
`canal/gemini:brouillons/canal_gemini/inbox_pour_claude/reponse_a_012_format_et_questions_EA_Funds.md`) : **non
vérifiées**, à lire comme des pistes. En particulier, l'affirmation « le LTFF a été clos le 11 août 2026 et remplacé par le
Transformative AI Fund » est à vérifier avant l'appel (elle change le nom du fonds et peut-être l'évaluateur).

Les cases `[…]` se remplissent avec les résultats à venir (plan R-262) ; rien n'y est écrit avant leur verdict scellé.

## 1. Format attendu (d'après la recherche, à vérifier)

- 30 minutes avec l'évaluateur principal du dossier, qui a lu le formulaire avant ; pas de diaporama ; 2 à 5 minutes de
  cadrage par le candidat, puis 20 à 25 minutes de questions sur ses points d'incertitude.
- Avant : formulaire court, CV, liens vers les travaux et le code. Après : précisions par courriel si demandées.
- Conséquence : préparer **un cadrage de 3 minutes** et **des réponses de 60 à 90 secondes** aux questions probables, avec
  chacune une preuve à envoyer le lendemain.

## 2. Déroulé proposé

| minutes | contenu |
|---|---|
| 0 à 2 | accord sur l'agenda : « trois minutes de point, puis vos questions » |
| 2 à 5 | cadrage (section 3) |
| 5 à 27 | questions de l'évaluateur (section 4) ; proposer, si le nul de P3 l'inquiète, une mise à jour écrite sous trois semaines avec les résultats scellés |
| 27 à 30 | demander sa principale réserve et le document qui la lèverait ; date de décision |

## 3. Cadrage de trois minutes (texte de travail, en anglais pour l'appel)

1. **Problem and thesis (1 min).** Control protocols mostly rely on black-box monitors that judge one action at a time. A
   misaligned agent can sabotage *diffusely*: each action looks innocent alone. Our thesis: fragmentation destroys the
   external, per-action evidence, but not the internal one; if intent leaves a trace in activations, that trace can be
   accumulated over time with a false-positive guarantee. We test it with white-box probes against matched black-box
   monitors.
2. **Method and first result (1 min).** Every decisive step is pre-registered and sealed before data, read by fresh
   reviewers, and controlled against a covariance-matched random-probe floor, an instructed benign control, a
   "mention without use" condition and an equal-declared-cost test. Our first pre-registered white-box test has run: an
   instructed Llama-3.1-8B saboteur inflated its declared costs (effect established); two generic probes, trained without
   data from this organism, were not above their random floor: lower bounds 0.531 and 0.481, against floors 0.572 and
   0.536 — "not detected at this power". The verdict is under a pre-registered audit before I accept it. It cost about
   four dollars of compute. `[mise à jour : verdict complété après l'addendum 2]`
3. **Next two to six weeks, and what the grant buys (1 min).** `[résultat de P4-instrument : contrôle positif de
   l'instrument]` ; `[résultat de P3b : localisation au champ du coût, sonde entraînée sur l'organisme, contrôle contre la
   lecture du nombre écrit]` ; `[comparaison boîte noire sur les mêmes épisodes, organisme diffus, porte G0 fin
   novembre]` ; `[pilote du papier C]`. The grant buys `[N]` months full time and the compute to run the dose-response
   organisms and the sequential test (G1), and to publish the benchmark.

À ne pas dire (note du brainstorm, R-259) : le facteur de gonflement (≈ 33), une aire ponctuelle, un chiffre de puissance,
le drapeau T2, « did not separate », « white-box fails ».

## 4. Questions probables et réponses de travail (60 à 90 secondes chacune)

| question probable (d'après la recherche, à vérifier) | réponse de travail | preuve à envoyer |
|---|---|---|
| 1. Comment cela se transfère-t-il à des systèmes plus capables, sans apprendre aux modèles à cacher leurs activations ? | règle gelée d'agrégation (maximum ou attention, jamais la moyenne, résistante à la dilution) ; tests d'évasion prévus (papier A, usurpation stylistique, papier C) ; `[résultat]` | programme v2 (règle 1), décision N-026 |
| 2. Dans quel régime les sondes battent-elles un moniteur boîte noire ? | précisément l'objet du plan 2 × 2 accès × agrégation ; sur un organisme flagrant (P3), le texte suffit ; l'enjeu est l'organisme diffus `[comparaison boîte noire]` | verdict de P3 ; note du brainstorm |
| 3. Que réfute exactement votre nul de P3 ? | ni l'idée, ni l'instrument : deux sondes génériques, à cette puissance, sur un organisme flagrant ; audit préenregistré en cours ; contrôle positif `[P4-instrument]` | verdict de P3, section 7 ; addendum 2 |
| 4. Que faites-vous si les résultats restent négatifs ? | jalons et portes écrits d'avance (G0 fin novembre, critères inchangés) ; théorème négatif : la corrélation, pas la marginale, porte alors le dommage, ce qui dicte un autre agrégateur ; résultats publiables dans les deux sens | programme, « hypothèse pivot » ; N-027 |
| 5. Pourquoi vous ? | `[Lazar]` : projet précédent sur la validité de construit de la sycophancie, audit de traçabilité, réplication préenregistrée qui a infirmé son propre résultat | dépôt du projet précédent |
| 6. Qui relit vos protocoles ? | contre-lectures par sous-agents neufs à chaque étape, relecture externe (Gemini), préenregistrements scellés ; `[relecteurs humains, à dire par Lazar]` | registres de décisions |
| 7. Pourquoi pas Apollo, Anthropic, Redwood, MATS ? | ils publient la détection par action ; nous visons la menace diffuse (accumulation dans le temps et entre agents) et la corruptibilité des moniteurs ; `[collisions vérifiées : état de l'art, R7, R8]` | état de l'art vérifié, niveau 2 |
| 8. Autres financeurs, refus ? | `[Lazar, en toute transparence]` | — |
| 9. Que faites-vous sans le financement, ou avec la moitié ? | `[Lazar]` | — |
| 10. Décomposition du budget | `[Lazar]` : allocation, durée, calcul (phase 0 : ≈ 67 USD de calcul à ce jour pour cinq lancements) | registre des dépenses |
| 11. Pourquoi tant de rigueur plutôt qu'itérer vite ? | les artefacts de texte et de longueur font de faux positifs dans la littérature sur les sondes ; la rigueur coûte peu (un test complet pour environ 4 USD) et évite de publier un faux positif | verdict de P3 ; `[références vérifiées par la revue]` |
| 12. Livrables à 1, 3 et 6 mois | 1 mois : `[P4-instrument, P3b, pilote C, verdicts scellés]` ; fin novembre : porte G0 ; puis papiers A et C | plan G0 (P-007, N-027) |
| 13. Qui utilisera vos résultats ? | `[Lazar]` : équipes de contrôle des laboratoires et instituts de sûreté ; banc public et protocoles scellés réutilisables | — |
| 14. Risque de double usage | organismes instruits sur un modèle ouvert de 8B, sabotage de coûts simulé, aucune capacité nouvelle ; consignes privées non publiées | consignes de confidentialité du dépôt |
| 15. Plus de calcul changerait-il les conclusions ? | oui pour l'échelle (passage à des modèles plus grands) ; le goulot actuel est le temps du chercheur | devis |

## 5. À préparer avant l'appel

1. Vérifier le nom actuel du fonds et de l'évaluateur (point du début).
2. Remplir les cases `[…]` avec les verdicts scellés seulement.
3. Choisir les pièces à envoyer après l'appel (préenregistrements scellés, verdicts) : la copie publique expurgée du dépôt
   (`lciric/controle-ia`) n'est mise à jour que par Lazar (nœud ; consignes permanentes).
