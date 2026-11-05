# Devis — P-041 (test (a) Bailey, examen final) et collisionneur protocelles — v1

31 octobre 2026, ≈ 10:30 UTC. Session-depot (Opus 4.6). Aucune dépense, aucun lancement.

---

## 1. Test (a) de Bailey — reproduction de la boucle adversaire sur carte graphique

**Objet** : reproduire le protocole de Bailey et collègues (arXiv 2412.09565, p. 11) sur Llama-3-8B-Instruct : un optimiseur d'entrées adverses entraîne des plongements pour camoufer un comportement, pendant qu'une sonde linéaire sur les activations est réentraînée à chaque époque ; 70+ époques ; moniteurs et attaques sauvegardés tour par tour. R-888 (R-611 levée), R-889 (hors gel), R-890 (lancement approuvé).

**Composantes** :

| Poste | Description | Coût attendu | Coût pire cas |
|---|---|---:|---:|
| Carte graphique (location Vast.ai) | A100 40 Go, ~12 à 24 heures de calcul (70 époques × ~10-20 min chacune : passes directes et rétrogrades sur le modèle 8B, entraînement de la sonde) | 15 USD | 36 USD |
| Infrastructure | Machine jetable (R-868, devis v3 `864f3d27…`) : création, transfert des données, destruction par identifiant (R10) | 1 USD | 8 USD |
| Juge de nuisance | StrongREJECT (à fixer : version, commit, empreinte) : ~200 jugements sur les entrées adverses de la dernière époque | 5 USD | 10 USD |
| Surcoût | Configuration, épreuves préliminaires, reprise si erreur | 10 USD | 20 USD |
| **Total test (a)** | | **31 USD** | **74 USD** |

**Prérequis avant lancement** : préenregistrement de l'examen final v2 scellé (éléments à fixer : StrongREJECT, jeu bénin, préenregistrement de l'arène) ; GO de Lazar sur le présent devis.

**Plafond recommandé** : **75 USD** (le pire cas de 74 USD a une marge négligeable ; le poste « carte graphique » peut s'envoler si les époques sont plus longues que chez Bailey ou si une reprise complète est nécessaire).

---

## 2. Examen final — arène contre base « instances seules » au protocole de Bailey

**Objet** : comparer le rappel d'une défense sortie de l'arène P-041 (figée) avec celui de la base « instances seules » (réentraînée à chaque époque, protocole de Bailey). Préenregistrement : `prereg/P-041-examen-final-v2.md` (`877e1c7a…`). L'examen final inclut le test (a) comme bras de base.

**Composantes** :

| Poste | Description | Coût attendu | Coût pire cas |
|---|---|---:|---:|
| Bras de base (= test (a)) | Cf. section 1 ci-dessus | 31 USD | 74 USD |
| Bras arène | Inférence seule sur Llama-3-8B-Instruct avec la défense figée : ~2 à 4 heures de carte graphique (pas de réentraînement) | 3 USD | 8 USD |
| Mesure du débordement | Rappel sur les familles de l'arène versus rappel sur les activations du 8B : calcul sur processeur, ~0 USD | 0 USD | 1 USD |
| Bras de contrôle | « Identiques réétiquetés » (200 entrées adverses) : calcul sur processeur | 0 USD | 1 USD |
| Juge de nuisance (partagé) | Déjà compté dans le bras de base | 0 USD | 0 USD |
| Surcoût et analyse | Intervalles de Clopper-Pearson, Bonferroni sur 2 intervalles simultanés | 2 USD | 5 USD |
| **Total examen final** | | **36 USD** | **89 USD** |

**Remarques** : le bras de base et le bras arène partagent les mêmes entrées adverses et la même carte graphique louée ; la machine n'est créée qu'une seule fois. Si le test (a) est fait en premier et la machine gardée, le bras arène se fait dans la foulée (même session de location).

**Plafond recommandé** : **90 USD**. Si le test (a) seul est approuvé en premier, il suffit de 75 USD (section 1). L'examen final complet ajoute ~5 à 15 USD au-dessus du test (a).

---

## 3. Estimation de la malléabilité — carte graphique

**Objet** : estimer le nombre de directions indépendantes de camouflage dans chaque couche de Llama-3-8B-Instruct contre un moniteur de type sonde linéaire. Préenregistrement : `prereg/P-041-malleabilite-v2.md` (`877e1c7a…`).

**Composantes** :

| Poste | Description | Coût attendu | Coût pire cas |
|---|---|---:|---:|
| Carte graphique | A100 40 Go : optimisation par direction (20 époques × 10 couches × jusqu'à 1 000 directions ; les premières directions sont rapides, la convergence ralentit) ; estimation pilote d'abord (2-3 directions sur 1 couche pour calibrer la durée) | 15 USD | 40 USD |
| Contrôles négatifs | Moniteur trivial + artefact unidirectionnel (CL-M2) : même carte graphique | 2 USD | 5 USD |
| Analyse de sensibilité | Trois seuils de camouflage (50 %, 20 %, 5 %) : même carte graphique | 1 USD | 3 USD |
| Infrastructure | Machine jetable partagée avec l'examen final si les deux sont lancés ensemble | 0 USD | 5 USD |
| Surcoût | Essai pilote, reprise | 5 USD | 15 USD |
| **Total malléabilité** | | **23 USD** | **68 USD** |

**Plafond recommandé** : **70 USD**.

**Synergie** : si l'examen final et la malléabilité sont lancés sur la même machine, l'infrastructure est partagée. Le total combiné (examen final + malléabilité) passe de 59 à 157 USD (attendu ≈ 55, pire cas ≈ 145).

---

## 4. Collisionneur protocelles × programme × organisme — deux tours

**Objet** : croiser le papier de Lazar sur les protocelles (107 pages, `Ciric-protocells-fecundity-Nature-v0.19.2.pdf`, `b699fed4…`, non publié) avec le programme et l'organisme d'idéation. Question scellée par conv-audit (`question-collisionneur-protocelles-v1.md`, `f905cb93…`). Quatre espèces (Fable 5.1, Opus 4.6, Argon, Kimi K3.1 Pro) ; papier entier aux quatre (R-710).

**Comparable** : tour bisociation, lot complet (47 623 mots de faits) : pire cas 44,28 USD, réalisé ≈ 20 USD. Le papier de 107 pages (≈ 1,1 Mo, ~50 000 à 65 000 mots de texte ; en jetons PDF, ≈ 160 000 jetons) est du même ordre de grandeur.

**Composantes** :

| Poste | Description | Coût attendu | Coût pire cas |
|---|---|---:|---:|
| Tour 1 | 12 cellules (4 espèces × 3 étages III) ; entrée dominante : papier entier + question (~160 000 jetons) | 20 USD | 50 USD |
| Tour 2 | 12 cellules ; entrée : tour 1 + annexe (notes de conv-audit `da93800c…`, relectures Opus `cbc16af5…` et `8e566df1…`) | 22 USD | 55 USD |
| Synthèse | Lecteur neuf + sceptiques + v2 : processeur (session-depot) | 0 USD | 0 USD |
| Risque Kimi | Cinq coupures de connexion en une nuit (R-871) ; probabilité de coupure par cellule Kimi estimée à 0,3 ; relance bornée | inclus | 5 USD |
| **Total collisionneur** | | **42 USD** | **110 USD** |

**Recommandation** : plafond **50 USD séquencé** — tour 1 d'abord (plafond 25 USD) ; si le tour 1 dépasse 22 USD, le tour 2 est soumis à un GO supplémentaire (le pire cas de 110 USD est tiré par Kimi et par la taille du papier, qui peut être plus grande que les tours précédents).

---

## Récapitulatif

| Expérience | Attendu | Pire cas | Plafond recommandé |
|---|---:|---:|---:|
| Test (a) Bailey seul | 31 USD | 74 USD | 75 USD |
| Examen final (inclut test (a)) | 36 USD | 89 USD | 90 USD |
| Malléabilité | 23 USD | 68 USD | 70 USD |
| Collisionneur protocelles (2 tours) | 42 USD | 110 USD | 50 USD (séquencé) |
| **Total si tout est lancé** | **101 USD** | **267 USD** | **210 USD** |

**Note** : l'examen final et la malléabilité sont sur carte graphique ; le collisionneur protocelles est sur des appels d'interface de programmation. Les trois postes GPU (examen final, malléabilité, test (a)) partagent la même machine louée. Le collisionneur protocelles est indépendant.

**Aucune de ces dépenses n'est engagée avant le GO de Lazar sur le présent devis.**
