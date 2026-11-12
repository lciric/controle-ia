# Compléments d'antériorité pour le registre des prédictions — v1

Session-dépôt, 10 novembre 2026, vers 12:36 UTC. Répond aux deux réserves du rédacteur du registre v2 et complète la pièce de
la mère `reponses-mere-registre-predictions-v1.md` (`9639b715…`, sur `main`), qui ne lit que `main`.

1. **T0.3 : verdict scellé, mais hors de `main`.** `docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1.md`
   (`bc53b746…`, compagnon conforme) a été versé par la session-dépôt sur `claude/upbeat-cray-dmauvv` (commit `c53a03a7`,
   2026-11-10 09:31:54 UTC) ; ce commit n'est pas un ancêtre de `main` (vérifié par `git merge-base --is-ancestor`). La
   pièce de la mère dit « pas de verdict scellé » parce qu'elle ne voit que `main`. L'antériorité du préenregistrement
   (établie par la mère, l. 79 : commit `5e481537` à 08:02:47, run à 08:02:57) n'en dépend pas.
2. **Étiqueteur, phase 1 : antériorité établie par les commits.** Compagnon du préenregistrement
   `prereg/preenregistrement-epreuve-etiqueteur-v1.md.sha256` ajouté par le commit `d858b66f` (2026-11-08 00:17:23 UTC) ;
   données de la lecture principale versées sur `donnees/etiqueteur-phase1-lecture-principale-v1` par le commit `16aef7a0`
   (2026-11-08 14:41:50 UTC), que le verdict cite (`verdict-etiqueteur-phase1-v1.md`, l. 111). Le préenregistrement est
   scellé environ 14 h 24 min avant le versement de la lecture. Heure exacte de la course non relevée ici (métadonnées de
   commit seulement, aucun contenu des données ouvert).
