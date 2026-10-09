# Porte GC — loi de déférence : verdict, contre-lecture, corrections — v1

Date : 2026-10-04 (UTC). Tâche T0.2 (antériorité de HC1).
Renvois :
- programme, section 4 (corruption) et section 8 (porte GC) ;
- nœud N-005 (`livrables/anteriorite-niveau1-v1/decisions-v2.md`).

Statut : pièce d'instruction pour la porte GC. **Elle ne tranche pas N-005**, qui reste à Lazar.

## 1. Verdict rendu (réponse à « la loi de déférence avec le gain a-t-elle déjà été publiée ? »)

Pas telle quelle. Mais chacune de ses pièces existe déjà, et la forme elle-même est ancienne.

| Pièce | Où elle est publiée | Source |
|---|---|---|
| Pente continue de déférence par modèle, sur intensités graduées | 2606.07897 v2 (Pander Score) : pente en log-cotes de la crédence sur la valence, 32 invites par proposition, 18 assistants ; rangs stables, magnitudes non | rapport papier C, lignes 16a–17b ; PDF `docs/sources/pdf/2606.07897v2.pdf` (e025464d…), p. 2–3, 7, 32 |
| Hausse continue de la note d'un juge, par technique de persuasion | 2508.07805 : 3 des 5 familles du programme ; normalisation Δ/v₀ ; une seule intensité ; ni régression ni test | rapport papier C, lignes 12a–13b ; PDF `2508.07805v1.pdf` (4cc15dcd…), p. 4–8 |
| Moniteurs de contrôle déplacés par l'agent | 2607.08066 : taux d'approbation binaire, sans gain | rapport papier C ; PDF `2607.08066v1.pdf` (f22075f0…), p. 4 |
| Forme algébrique g = (v − v₀)/(v* − v₀) | « poids du conseil » de la psychologie du jugement (paradigme juge-conseiller) | de mémoire au moment du verdict ; voir 2 (3) |

## 2. Contre-lecture de Lazar (message du 2026-10-04) — corrections versées

1. **Formule du poids du conseil** : (v − v₀)/(v* − v₀). C'est la forme du verdict ; à écrire ainsi dans tout document de la porte GC.
2. **Citer 2606.07897 en v2.** La v2 date d'août 2026 : « Pander Score », 18 modèles. La v1 date du 5 juin : « AI Epistemic Deference Index », 8 modèles. Elle diffère de la v2 ; le PDF de la v2 note d'ailleurs un « initial eight-model deployment » (p. 7). **Le papier lit son score comme une fraction de l'écart à la position de l'utilisateur** : c'est un gain normalisé publié (p. 2 : « a score of 20 means answers on average move about 20% as far as the user's stance »). Ma réserve « équivalent à g seulement sous un modèle de mise en commun log-linéaire » porte sur l'identité formelle, pas sur la lecture que le papier en donne.
3. **R7 partiellement levé par Lazar** : les références suivantes existent.
   - Harvey et Fischer (1997), *OBHDP* 70(2):117–133 ;
   - Yaniv et Kleinberger (2000) ;
   - Yaniv (2004).
   Bednarik et Schultze (2015) leur attribuent la mesure. **La formule de l'indice d'ancrage (Jacowitz et Kahneman 1995) reste de mémoire**, non vérifiée.
4. **Voisins manquants**, non lus :
   - 2606.18276 : modèle de Friedkin–Johnsen sur des réseaux de LLM (juin 2026) ;
   - 2603.15809 : Friedkin–Johnsen, manipulation par un agent têtu (mars 2026) ;
   - Panin, SSRN 7424179 : poids du conseil mesuré sur cinq LLM, préenregistré. **C'est le voisin le plus proche signalé : à lire en priorité** ;
   - poster NeurIPS 2025 WiML, version antérieure de 2607.08066.
5. **PARROT (2511.17220) et BASIL (2508.16846)** n'ont ni intensités graduées, ni gain, ni nul de retour à la moyenne. La réserve « sous réserve de PARROT et BASIL » du rapport de niveau 1 est donc levée sur ces trois pièces. Ce n'est pas une lecture de ma part.
6. **Pour quand Lazar tranchera N-005.** Normaliser g par la cible de l'attaquant suppose que la destination du verdict *est* cette cible. La pièce non publiée est la suivante :
   - estimer librement la destination ĉ dans Δv = g·(ĉ − v₀), sans imposer ĉ = v* ;
   - tester ĉ contre la cible de l'attaquant v* et contre la moyenne du corpus (le nul de régression vers la moyenne) ;
   - comparer entre familles d'attaque.

## 3. Conséquences pour la porte GC (sans trancher N-005)

- **Ce qui n'est plus libre.** « g normalisé par la cible » ne l'est plus en soi : la normalisation par une destination est publiée (Pander Score, poids du conseil). Ma formulation de l'option (a) de N-005 était trop large sur ce point.
- **Cibles de la porte GC.** Si sa reformulation est retenue, la porte GC vise :
  - 2508.07805 ;
  - 2606.07897 v2 ;
  - le poids du conseil (Harvey et Fischer 1997 ; Yaniv et Kleinberger 2000 ; Yaniv 2004 ; attribution par Bednarik et Schultze 2015) ;
  - Panin (SSRN 7424179), dès sa lecture ;
  - les modèles de Friedkin–Johnsen sur LLM (2606.18276, 2603.15809).

  Ce n'est plus seulement 2607.08066.
- **Pièce candidate**, à soumettre avec N-005 : la destination ĉ libre, testée contre v* et contre la moyenne du corpus, comparée entre familles. S'y ajoutent les pièces que la contre-lecture n'a pas contestées :
  - régression sur plusieurs intensités par famille ;
  - usurpation stylistique et ordres en bande ;
  - verdict lu par probabilité du jeton ;
  - opposition juge/sonde.
- **Réserve nouvelle.** Panin (SSRN 7424179) n'est pas lu. Si ce papier estime une destination libre, ou un nul de retour à la moyenne sur LLM, la pièce candidate est occupée (R8 : zone séduisante, à vérifier plus durement).

## 4. Lectures à demander (ajoutées à la liste des PDF)

Par ordre de priorité :
1. Panin, SSRN 7424179.
2. 2606.18276.
3. 2603.15809.
4. Poster WiML NeurIPS 2025 (version antérieure de 2607.08066).
5. Bednarik et Schultze (2015).
6. Harvey et Fischer (1997) ; Yaniv et Kleinberger (2000) ; Yaniv (2004).
7. Jacowitz et Kahneman (1995).

## 5. Provenance

- **Points 2 (1) à 2 (6)** : contre-lecture de Lazar, non vérifiée sur PDF par moi. Seules les citations de 2606.07897 v2, 2508.07805 et 2607.08066 renvoient aux PDF empreintés de `docs/sources/pdf/` (`provenance-niveau1-v1.md`).
- **Aucun chiffre** de cette pièce ne peut entrer dans un préenregistrement avant vérification sur PDF (R7). Font exception les chiffres déjà vérifiés dans `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`.
