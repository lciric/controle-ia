# Orchestrateur du pôle, version 0.7.0 — v39 : porte PACE en bras de référence du juge figé ; garde appariée : écart non fini refusé — LISEZMOI v39

Lignée conv-audit (instance de reprise, Fable 5.1), écrit après le relevé `date -u` de **00:39 UTC** le 29 octobre 2026 ;
v1 à v38 gardées (R12). Deux causes : la décision de Lazar (29 octobre, 01:15 heure de Paris) « porte PACE comme bras de
référence du juge figé », et un défaut du code existant trouvé en l'écrivant.

| changement | détail | fichiers |
|---|---|---|
| **Porte PACE** (arXiv 2606.08106v1, corpus primaire v4) comme **bras de référence** | règle de pari de l'équation (2) de l'extrait (λ = 0,5, α = 0,05, validation dès E ≥ 1/α), appariement sur les mêmes instances, égalités écartées, arrêt à tout instant, témoin planté à gain connu, audit qui étiquette faux si l'écart ≤ 0, bras « acceptation gloutonne » ; la règle se ramène exactement à `trajectoire_log_richesse(v, lambdas=(λ,))` (essai) ; choix non fixés par l'extrait marqués [INFÉRÉ] ; **écart volontaire** : la référence reste fixe (dans PACE le candidat validé remplace le titulaire — sélection interdite par N-053) ; `comparer(…)` rend côte à côte PACE, notre pari apparié (borne de boucle e-BH, garde δ, parts bornées) et le glouton. **Jamais une sélection d'agent ; exploratoire, non préenregistré.** | `pole/porte_pace.py`, `demonstrations/porte_pace_v1.py`, `essais/test_v7_porte_pace.py` (18 essais), `../ideation-organisme-approches-v1/note-porte-pace-bras-de-reference-v1.md` |
| Ce que la démonstration montre (graine 20261029, synthétique, non opposable) | sous la nulle à 120 instances, 32 % des suites de 20 candidats contiennent une fausse validation avec PACE, 0,5 % avec notre pari ; un « tricheur » (gagne en exactitude, dépasse δ en faux positifs) est validé par PACE et le glouton, refusé par notre garde ; prix : à 40 instances, notre pari ne valide le témoin que dans 50 % des suites contre 90 % pour PACE | note, § résultats |
| **Défaut corrigé** (R4 : trouvé en cherchant ailleurs) | `pari_apparie.trajectoire_log_garde` : un écart de faux positifs **NaN ou infini** devenait **+1** par le jeu de `min`/`max`, la valeur la plus favorable à la promotion, sans erreur ; refus explicite (`ContrasteInvalide`) ; essai inverse. Aucune course scellée n'a été relue avec ce défaut à cette heure : à vérifier par session-depot sur les journaux des duels passés (une garde qui a promu avec un écart NaN serait à requalifier) | `pole/pari_apparie.py`, `essais/test_v7_pari_apparie.py` |

**340 essais passent.** Relecture ciblée v38 → v39 (porte PACE et correction) à ajouter à celle de la v38 chez session-depot.

```
python3 -B -m unittest essais.test_v7_porte_pace ; python3 -I -B demonstrations/porte_pace_v1.py
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v39.txt
```
