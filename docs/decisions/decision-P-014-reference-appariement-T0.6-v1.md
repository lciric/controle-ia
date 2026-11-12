# Décision P-014 — référence d'appariement de T0.6 : étiquetage par sous-agents de « tout ce qui compte » — v1

Date : 2026-10-12 (UTC), session 13. **Retenue par Lazar** (message vers 18:00 UTC : « Ma recommandation : étiqueter tout ce qui compte, mais pas tout : go »), sur la recommandation de la session faite dans la conversation après R-156 ; N-020, point 4 (R-155). Modification du dispositif de mesure de T0.6 : décision de Lazar (CLAUDE.md, hiérarchie de décision).

**Motif.** Au pilote, l'appariement par le juge 8B est peu fiable (kappa pondéré 0,17 pour les contrôles, 0,04 et 0,07 pour les directions ; verdict `docs/verdicts/verdict-T0.5-pilote-v1.md`) ; deux séries de sous-agents étiqueteurs, indépendantes et à l'aveugle, s'accordent à 0,968 (R-156, `brouillons/T0.5-pilote-double-etiquetage-v1/`). Contrôle par deux autres modèles en cours (plan scellé `brouillons/T0.5-pilote-etiquetage-autres-modeles-v1-plan.md`).

**Ce qui est retenu, pour le préenregistrement de T0.6 :**
1. **Référence d'appariement** : l'étiquetage par sous-agents neufs, sous une consigne figée, remplace le juge 8B comme vérité terrain de l'appariement des **contrôles** ; le 8B peut rester rapporté à titre descriptif.
2. **Périmètre** : **toutes** les paires « proposition × contrôle semé » des ensembles finaux, sur **tous** les épisodes des comparaisons décisives de T0.6 ; pas d'échantillon de paires (une estimation par échantillon corrigé n'apporte rien quand le juge bon marché est presque sans information). Les directions (fécondes, stériles), trop rares pour une réponse à la dose et non retenues au pilote, sortent de la vérité terrain ; le coût reste la seconde mesure.
3. **Forme** : un élément = une proposition avec la liste de ses contrôles (texte lu une fois) ; cette consigne regroupée est figée, puis **validée sur les 480 paires du pilote** avant tout usage (accord ≥ 0,8 avec les séries existantes ; sinon, consigne par paire).
4. **Fidélité suivie** : double étiquetage d'environ 10 % des éléments, tirés par graine, pendant T0.6.
5. **Débit** : plusieurs workflows en parallèle (chacun limité à deux agents sur cette machine) ; aucune dépense de carte graphique.
6. **Repli** si le volume l'impose : échantillon d'**épisodes entiers** (toutes leurs paires), tiré par graine, jamais de paires isolées.

**Réserves.** Étiqueteurs non humains, du même fournisseur pour les séries de contrôle : la validité se juge sur le contrôle par d'autres modèles, et, au besoin, par un modèle ouvert d'une autre famille greffé sur une session de calcul payée (sous GO). Les textes à étiqueter restent hors du dépôt ; seules les étiquettes, les identifiants et les empreintes y entrent.
