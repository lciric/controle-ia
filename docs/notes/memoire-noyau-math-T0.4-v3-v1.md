# Note — mémoire de la carte au noyau d'attention « math » (T0.4, version 3) — v1

Rédigée le 2026-10-06 par la session de mise en œuvre, avant le préenregistrement v3. Elle vérifie que les deux configurations nouvelles de la v3 tiennent sous la garde de mémoire de la carte (130 Gio, soit 139,6 Go) : la phase de chemin (simple précision) et le débit au noyau « math » (demi-précision). Elle ne lit aucun écart ni aucune équivalence : seulement de la mémoire.

## Entrées

- Note de mémoire de la v2 : `docs/notes/memoire-double-precision-T0.4-v1.md`, sha256 `b013428ab8502a61a3ea19404ea3a6cdc64ea6a587010c45627e33f13ef29148` (borne théorique de la longueur remplie d'un lot : 3 097 jetons ; poids : 64,2 Go en double précision, donc 8,03 milliards de paramètres).
- Run A de la v1 : `diag/20261005-102042-validation-reelle/arret.json`, sha256 `4eb2d92069e270631bf3e4d25345b44191cbe419d71a4f06725659c32846aeed` : phase de logique en simple précision, noyau « math », lot de 8, plus long contexte rempli 2 329 jetons ; pic de la carte 51,912 Go.
- Mesure sur processeur du pic du noyau « math » : `docs/notes/memoire-T0.4-v3/pic_noyau_math_v1.py` et sa sortie `pic_noyau_math_v1.sortie.txt` (empreintes compagnons), torch 2.14.1, réduction en demi-précision non permise dans « math » (défaut, relu).

## Mesure : pic du noyau « math »

- Le noyau « math » est une composition d'opérations de la bibliothèque, la même sur processeur et sur carte. En demi-précision, il calcule en simple précision (la réduction en demi-précision n'y est pas permise par défaut) : il matérialise les matrices d'attention de forme (lot, têtes, L, L) en simple précision.
- Mesure : pic de la mémoire résidente pendant un préremplissage en bfloat16, avec un masque de remplissage à gauche et causal, rapporté à la taille d'une de ces matrices. Résultat : 2,74 fois (lots de 4 et de 8, L = 1 024) et 2,48 fois (lot de 2, L = 2 048). Retenu : 3 fois, par marge.

## Débit, au noyau de production

- Lot de 32 contextes de 2 048 jetons (plus 128 jetons générés) ; 32 têtes.
- Une matrice d'attention en simple précision : 32 × 32 × 2 048² × 4 octets = 17,2 Go ; trois fois : 51,5 Go, pendant le préremplissage d'une couche.
- Poids en bfloat16 : 16,1 Go. Cache : 32 lignes × 2 176 positions × 32 couches × 2 (clés et valeurs) × 8 têtes × 128 × 2 octets = 9,1 Go. Activations des couches denses du préremplissage (32 × 2 048 jetons, largeur intermédiaire 14 336, bfloat16) : environ 2 Go par tableau, quelques-uns à la fois : moins de 8 Go. Seuls les logits du dernier jeton sont calculés (`logits_to_keep=1`).
- Pic estimé : environ 85 Go, sous 139,6 Go.

## Chemin, en simple précision

- La configuration du chemin est celle de la logique de la v1 : simple précision, noyau « math », lot de 8, mêmes tailles. Pic mesuré dans la v1 : 51,9 Go, pour une longueur remplie de 2 329 jetons.
- À la borne théorique de 3 097 jetons : le surcroît de la note de la v2, divisé par deux (simple au lieu de double précision), donne (129,0 − 64,2) / 2 = 32,4 Go, plus 32,1 Go de poids : environ 65 Go.

## Autres phases

- Logique : celle de la v2, inchangée (pic de 78,3 Go mesuré dans la v2 à 1 226 jetons ; 129 Go estimés à la borne, dans la note de la v2).
- Production : lot de 8 en bfloat16 ; dans la v2, aux noyaux par défaut, 19,0 Go. Au noyau « math », à la borne de 3 097 jetons : trois matrices de 8 × 32 × 3 097² × 4 octets = 9,8 Go, soit 29,5 Go, plus 16,1 Go de poids et moins de 10 Go de cache et d'activations : moins de 60 Go.

## Limites

- Mesure sur processeur : l'allocateur de la carte peut garder des blocs en plus (fragmentation). La marge (plus de 50 Go pour le débit) la couvre largement.
- Si le débit manquait malgré tout de mémoire, le run A s'arrêterait en phase de débit, après toutes les gardes décisives : cause déterministe dans la table du préenregistrement (non concluant, nœud), sans relancement.
