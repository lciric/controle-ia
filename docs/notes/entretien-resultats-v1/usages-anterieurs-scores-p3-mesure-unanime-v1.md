# Usages antérieurs des scores du premier test boîte blanche — annexe de déclaration de la mesure unanime v15 (v1)

Session-dépôt `session_01QPDgKgcLdggoVJfGC5cBw8`, 10 novembre 2026. Annexe du préenregistrement
`preenregistrement-mesure-unanime-v15.md` (`3a1651f4…`, scellé). **Scellée et datée par le tiers avec lui, avant la course.**
Elle ne modifie pas le préenregistrement ; elle déclare ce que la contre-lecture v15 a établi (point C, CV15-1 :
`contre-lecture-v15/rapport-contre-lecture-mesure-unanime-v15.md`, `18ef0083…`).

## Le fichier

`donnees/20261019-230011-p3-reel/scores-p3.npz`, empreinte `968414fc…`, présent depuis le 20 octobre (même objet git
`86ec9eaf…` sur `calcul/p3-reel-v1`, sur `4d1fa5c0` et sur `main`). Pour cette mesure, il n'a jamais été ouvert : seule son
empreinte a été contrôlée.

## Ce que d'autres travaux en ont déjà tiré

| Travail | Ce qu'il a calculé sur ces scores | Touche-t-il une quantité de la mesure unanime ? |
|---|---|---|
| Premier test boîte blanche (P3), accumulation | somme et maximum par épisode pour les deux sondes principales, seuil pris dans l'échantillon des 60 épisodes honnêtes ; le seuil réduit du maximum honnête est une valeur connue du dépôt | voisin, pas identique : aucun taux de fausses alertes **hors échantillon**, aucune dépendance intra-épisode |
| Agrégation sur les sondes de R1 v4 | les mêmes statistiques que la mesure unanime, sur les mêmes 60 épisodes honnêtes, mais seulement en aires sous la courbe saboteur contre honnête | non : aucun taux de fausses alertes par épisode, aucune dépendance |
| Addenda de P3 ; scripts de puissance de P3-bis ; recalcul du rapport au directeur | des aires, des corrélations au coût, de la plomberie | non |

**Conclusion** (contre-lecture v15, point C) : aucun travail antérieur n'a calculé le taux de fausses alertes hors échantillon,
par épisode honnête entier, d'un agrégateur séquentiel, ni la dépendance naturelle r₀. La prédiction de la quatrième mesure
est de toute façon conditionnelle à r₀ (table gelée).

## Le sens inverse : protéger P3-bis

La course de la mesure unanime rendra le taux du maximum conforme, la dépendance r₀ et l'effet des marges sur ces mêmes
épisodes honnêtes. Le préenregistrement de P3-bis, encore en brouillon, repose sur le maximum par épisode, un seuil au maximum
des 60 épisodes honnêtes et l'échangeabilité. Pour ne pas l'informer avant son scellement, **la course n'a lieu qu'après le
scellement du préenregistrement de P3-bis** (rendez-vous du 11 novembre vers 16:03 UTC), sauf autre fermeture décidée par
Lazar ou la session mère : inscrire ces sorties dans les « valeurs déjà vues » de P3-bis en gelant ses énoncés concernés, ou
tenir son auteur à l'écart des sorties.
