# Proposition P-036 v2 — couche 2 : préparation, après la comparaison des deux dimensionnements et le collisionneur

Lignée « session-depot » (instance 2), 28 octobre 2026, ≈ 23:20 UTC. **Remplace P-036 v1** (`a8c41681…`, gardée, R12) sur
les points ci-dessous ; le reste de la v1 (inventaire, chaîne à construire, gouvernance) vaut. Tout chiffre est
exploratoire et non opposable (R7) ; il n'entre dans une décision que par le préenregistrement scellé de G1.

## 1. Les décisions à prendre passent par le format décision de conv-audit

Les cinq divergences sont portées à Lazar par conv-audit (`…/couche-2-conv-audit-v1/decision-cinq-divergences-couche-2-v1.md`,
`857b501c…`), sur la synthèse du collisionneur (`docs/notes/couche-2-preparation-v1/collisionneur-cinq-divergences-v1/
synthese-collisionneur-couche-2-v1.md`, `37f85388…`). **session-depot s'y range** et retire ses options divergentes de la
v1 : D2 de la v1 (tâches) → D2 de conv-audit ; **D3 (c) de la v1 (lâcher « mention », strates de dose écrites sans
recherche) est retirée** : la synthèse montre que la dose diffuse avec dommage n'y serait jamais mesurée, et lever
« mention » est un nœud, non un défaut. Le « go défauts D2 D3 D5 D6 » de Lazar (R-645) portait sur la v1 : sur D3, il est
**à reconfirmer** au vu du format décision (D4 de conv-audit).

## 2. Erreurs de la v1 reconnues (comparaison `a2450b51…`, section 3)

1. Total bas « ≈ 10 100 épisodes » : compte la tranche A deux fois ; **8 400**.
2. Scénarios C1 et C2 calculés sur **280** unités sabotées, impossibles avec 96 tâches (D2 de la v1 elle-même) : retirés.
3. Total haut « ≈ 26 100 » sur 384 unités et 3 épisodes non définis : retiré.
4. Prix 1,184 à 1,366 USD/h cités sans empreinte : **SUPPOSÉ** ; prix relevés le 28 octobre à l'offre : 1,08 à 1,43 USD/h
   (A100 SXM4 80 Go), à consigner avec empreinte au devis v2.
5. Citation de N-056 : « plusieurs centaines de **tâches** sabotées de plus par mode », non « d'unités ».
6. D-S8 : la v1 suivait N-055 ; **N-056 prime** (variantes noires et bases (ii), (iii)) — note
   `note-alignement-N-055-D-S8-v1.md`.

## 3. Ce que session-depot fait maintenant, sans dépense (D5 (0) et (1) de conv-audit)

1. **Simulation du contrôle 12 joint** (cellules critères × deux modes × strates), lue dans les deux sens : c'est elle qui
   tranche 9 600 + seuil 40 contre 12 800 (D1). Rédacteur : un sous-agent neuf, sur la simulation de la pièce A.
2. **Chaîne de la banque** (P-036 v1, section 3) : module de génération à deux modes dérivé de P3, captures complètes,
   calibrage commun coupé dans les tâches, jumeaux partagés avec sentinelle, campagne entrelacée — paramétrée pour que
   D1 à D5 se fixent par configuration, non par code.
3. **Sondes figées de P3** : la régénération du fichier complet est en cours (instance 58162997, GO-2026-10-28-11) ;
   la couche 2 lira le fichier versé en morceaux et son verdict.
4. **Rejeu du juge sur les 180 textes du pilote** (≤ 4 USD) : devis séparé, nœud.

## 4. Coût

Ordre de grandeur inchangé : **300 à 1 400 USD** pour la banque complète, au-delà du plafond de la phase 0 et des 90 USD
accordés (D1 (b) de Lazar) : **nœud, devis v2 par étape**, chaque lancement sous son GO.
