# Orchestrateur du pôle, version 0.7.0 — prise « idéation » : v38 — réponse à la relecture CL5 de la v37 — LISEZMOI v38

Lignée conv-audit (instance de reprise, Fable 5.1), écrit après le relevé `date -u` de **00:16 UTC** le 29 octobre 2026 ;
v1 à v37 gardées (R12). Répond à la relecture ciblée v36 → v37 de session-depot (`docs/notes/ideation-organisme-v1/
contre-lecture-v37-cl5.md` sur `main`, « lançable après corrections », message n° 130 : CL37-01 à 03 majeurs, 04 à 09
mineurs). **v38 n'est pas contre-lue** : relecture ciblée v37 → v38 annoncée chez session-depot (R2).

| constat | correction |
|---|---|
| **CL37-01** Argon proposeur après Claude ; contrôle sur 41 caractères | les proposeurs externes jouent **en tête de chaque passe** ; leur appel de contrôle se fait **sous le rôle `proposeur_ideation`** et **à la taille réelle** : `consigne_de_controle(supplement)` = la consigne de contrôle suivie des pièces servies, à ignorer (quota, taille de requête, délai éprouvés avant toute dépense Claude ; `--budget-controle-externe-usd 2.5`) ; `taille_consigne` et `role` au manifeste ; essai du lanceur avec une commande factice qui casse au-delà de 100 caractères → aucun appel Claude |
| **CL37-02** contrôle du bras qui a coûté scellé « rien dépensé » | `ControleRefuse` porte la lecture et le coût ; le bras le compte avant toute décision ; « rien envoyé » ne vaut que si **aucun processus n'est parti** (commande introuvable, clé dans l'environnement) ; sinon `bras-tentative-N.json` scellé avec le coût, **imputé au plafond externe** des tentatives suivantes ; **au plus 3 tentatives** (`MAX_TENTATIVES_BRAS`) ; essais (contrôle « KO » à 0,15 compté, plafond diminué, troisième tentative refusée) |
| **CL37-03** somme des plafonds > total ; relais incohérent | le cœur consigne la **somme des plafonds** (contrôles engagés, passes, juges) et la **refuse au-delà du total** (Claude et externe), sauf `tolerer_somme_plafonds` ; le lanceur lit l'état du relais avant la course et refuse si `plafond − réserve < total − plus petit plafond de juge` ; devis v7 quater : réserve 4, Fable proposeur 9,3 |
| CL37-04 refus après les contrôles ; défaut 400 000 | `verifier_reglages(…)` appelée par le lanceur **avant** tout contrôle (liste blanche, pièces et tailles, témoins, attestation du matériau, plafonds finis, somme des plafonds) ; `--taille-max-pieces` par défaut **750 000** (devis v7 ter) ; `math.isfinite` sur tous les plafonds |
| CL37-05 mutations survivantes | essais : proposeur sans juge externe sur course réelle ; juge externe présent dans l'essai CL35-04 ; lanceur avec commande factice (contrôle d'Argon avant toute passe, coût au journal, Argon en tête) ; médiane ≠ moyenne (notes 2, 2, 0 → 2) ; attestation complète au sceau faux ; chemin relatif |
| CL37-07 interruption | `except BaseException: os.killpg(…)` autour de `communicate` |
| CL37-08 délais | `DELAI_SESSION_S` 3 600 ; `DELAI_COMMANDE_S` 1 800 ; défauts du lanceur |
| CL37-09 écrits | réécrits ici ; le lanceur dit « bras non joué, relance permise » (code 2 mais relançable) |
| CL37-06 (non codé) | taille de chaque consigne : déjà `taille_pieces_servies` au départ ; le comptage en jetons des consignes scellées de la course simulée est une tâche du devis (session-depot, barème) |

**321 essais passent.** Course simulée (liste v4, proposeur et juge externes) : Argon en tête, contrôle à la taille réelle ;
bras : tentatives comptées. Relecture ciblée v37 → v38 chez session-depot avant tout lancement.

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v38.txt
```
