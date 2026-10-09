# Devis de calcul — v1

Rédigé le 2026-10-04. **Prix indicatifs** : Vast.ai est refusé par la politique réseau de l'environnement, je n'ai pas pu lire les offres du jour. Les prix sont des fourchettes de place de marché à confirmer au lancement ; la marge de 30 % est appliquée aux heures.
Instance de référence : 1 × A100 80 Go (bf16 ; Llama-3.1-8B tient avec un grand cache en génération, la LoRA et les passes avant longues passent sans acrobatie). Prix indicatif : 0,80 à 1,30 USD/h (central 1,00). Variantes : H100 80 Go (≈ 1,6–2,5 USD/h, ≈ 1,5–2× plus rapide : coût total voisin) ; RTX 4090 24 Go (≈ 0,30–0,55 USD/h : assez pour la génération seule, juste pour la LoRA et l'extraction longue).

## 1. Phase 0 — détail

| Poste | Contenu | Heures GPU |
|---|---|---|
| T0.4 harnais | validation sur 8B : rejeu au bit près, équivalence génération/passe avant, débit, stockage | 6 |
| T0.5 environnement | pilote : ~200 épisodes honnêtes + évaluateur faible (Llama-3.2-3B) | 5 |
| T0.6 famille (i) | 4 doses × 2 intensités + 2 contrôles croisés, ~150 épisodes chacun | 8 |
| T0.6 famille (ii) | données de distillation (~8 000 actions), LoRA 2 époques, évaluation de la grille | 10 |
| T0.7 sondes | activations (données génériques + épisodes), sondes, plancher apparié | 6 |
| T0.8 boîte noire | juge 8B + juge 3B par action ; TRACE-lite ; mêmes épisodes | 6 |
| T0.9 pilote papier C | 3 juges × 16 conditions × ~100 items + lecture des sondes (GO séparé) | 4 |
| Commun | téléchargements de modèles, mise en place, mise au point, temps mort | 8 |
| **Sous-total** | | **53** |
| Marge 30 % | | 16 |
| **Total** | | **69** |

| Coût | Calcul | USD |
|---|---|---|
| GPU | 69 h × 0,80–1,30 | 55–90 |
| Stockage | volume de 150 à 250 Go pendant le mois (≈ 0,10–0,20 USD/Go/mois, facturé même instance arrêtée) | 15–50 |
| Trafic | téléchargements de modèles (~60 Go) | < 5 |
| **Total phase 0** | | **≈ 75–145** |

**Demande de GO : plafond 150 USD pour la phase 0**, alerte à 80 % (120 USD), registre `registres/depenses.md`. Le pilote du papier C (4 h) reste soumis à un GO séparé à l'intérieur de ce plafond.

Estimation du stockage (T0.4) : activations par token, 3 couches × 4 096 dimensions × 2 octets = 24 Kio ; sous-échantillon d'entraînement de 1,5 million de tokens ≈ 36 Go ; vecteurs agrégés par action (30 000 actions) < 1 Go ; poids des modèles ≈ 25 Go. Volume recommandé : 150 Go.

## 2. Programme entier — ordres de grandeur

| Phase | Postes lourds | Heures GPU (équiv. A100) | USD indicatifs |
|---|---|---|---|
| 0 | instruments | ~70 | 75–145 |
| 1 (papier A) | ~5 000 épisodes gelés ; plan 2 × 2 ; lemme et théorème sur données réelles ; **attaques pondérales : réglage fin contre la sonde puis apprentissage par renforcement au niveau action (poste le plus lourd)** ; interventions ; ControlArena | 200–300 | 250–500 |
| Piste C | juges × familles × intensités ; sondes ; usurpation ; taxe de déplacement (obfuscation portée sur 8B) ; contre-mesures ; panel pour g bénin + attaquant itératif | 100–150 | 120–250 |
| 2 (papier B) | N = 2–3 ; collusion ; statistiques inter-agents | 80–150 | 100–250 |
| 3 (papier B) | N jusqu'à 10 ; environnement (b) agentique ; variantes LoRA ; panel de sondes et matrices de transfert d'attaque ; riposte avec adaptation rouge | 300–500 | 400–1 000 |
| G3 (option) | validation d'un proxy de vérité différée | 30–60 | 50–100 |
| Stockage | 7 mois × 200–400 Go | — | 200–450 |
| **Total** | | **≈ 800–1 200** | **≈ 1 200–2 700** |

Option hors devis : famille (iii) sur 70B (organismes de l'institut britannique, 2 × A100), +20–40 h, ≈ 60–120 USD.
