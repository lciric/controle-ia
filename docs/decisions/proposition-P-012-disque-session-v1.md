# Proposition P-012 — disque de la session — v1

Date : 2026-10-10 (UTC), session 11 reprise. Hiérarchie : « proposer avec recommandation » (défaut sous 48 heures), parce qu'il s'agit de supprimer des fichiers et que la consigne de Lazar est « ne détruis aucun fichier ».

**Décision.** Libérer, ou non, de la place sur le disque de la session.

**Enjeu.** Le quota d'écriture de la session est presque épuisé : environ 980 Mo libres le 2026-10-10 vers 15:00 UTC, après suppression des seuls caches (dossiers temporaires des tests, caches de paquets). La suite complète de tests s'est arrêtée sur « No space left on device » (444 réussis, puis 3 échecs et 203 erreurs d'écriture). Les runs à venir, pilote et revalidation de T0.5, rapatrient des résultats sur ce disque.

**Ce qui occupe la place.** Le bloc-notes de la session pèse environ 21 Go. L'essentiel vient de copies de travail du dépôt à des commits passés, faites pour les répétitions, les essais de l'amorce et les contre-lectures de T0.4 (`essais-v2*`, `essais-v3*`, `essais-cl4*`, `contre-lecture-t04-*`, environ 15 Go). Leurs résultats sont scellés dans le dépôt, et ces copies se recréent depuis l'historique.

**Options.**
- **(a)** Supprimer ces copies de travail de T0.4, soit environ 15 Go. Avantage : la place revient, les tests et les runs repartent. Inconvénient : on perd ces copies ; c'est une exception à la consigne de tout garder.
- **(b)** Tout garder ; lancer les tests par morceaux. Avantage : rien n'est détruit. Inconvénients : le contrôle reste partiel, et le disque devient bloquant pour les runs.

**Recommandation.** (a), confiance environ 75 %.

**Défaut sous 48 heures.** (b), le 2026-10-12 à 15:10 UTC : la consigne « rien n'est détruit » prime tant que Lazar n'a pas répondu.
