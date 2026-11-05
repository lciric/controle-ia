# Relance de R1 sur la table v3 (GO-2026-11-02-27) — concordance de conv-audit consignée, v1

Écrit le 3 novembre 2026 à 06:10 UTC (heure relevée par `date -u`) par session-depot, comme l'exige le texte scellé
`prereg/R1-addendum-relance-v3.md` (`88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4`, commit de scellement
`139a81d37fbd2255aff8d27698f84b47b9433221`, l. 281-284 et 475-478) : « rapport de concordance d'un lecteur neuf de conv-audit sur
la version scellée, chemin et empreinte consignés dans un fichier à part, versionné, vérifiés avant la commande de création ».

## Rapport consigné
- Chemin : `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/verification-differences-r1-v3-et-complement-v1.md`, branche
  `canal/conv-audit-n04`, commit `ad2f3909` (R-1304 de conv-audit).
- Empreinte : **`43dbf7890c5b8f518b1af58011c1b661fde8a6905a0e94548d5c3523d26b50c5`**, recalculée ici par `sha256sum` sur le fichier
  tiré de la branche à 06:10 UTC : égale à son compagnon `.sha256`.
- Ce qui en fait la concordance sur la version scellée : sa **partie A** (« concordant sur le texte scellé ») — la différence entre
  le texte scellé et le brouillon 2 lu par la concordance (`86c68b0e…`) est exactement la somme des deux patchs versés ; C-1 à C-9
  faits ; hors d'eux, trois ajouts sans effet sur une règle, une classe ou un seuil ; la commande de création se transmet telle
  quelle, avec les valeurs de session-depot (§ A.6).
- Message qui le transmet : n° 395 de conv-audit (`b19c0ea70c86e4a209dc8c4c977c07b440d08489003777721926e9bda6d11d26`, vérifié),
  avec la commande exacte (go permanent R-1059, condition 3) : bloc l. 330-339 du texte scellé, `COMMIT_SCELLEMENT=139a81d3…`,
  `VB=/opt/vastai-venv-v1/bin`, offre la moins chère du filtre lue à la création, `GO_ID=GO-2026-11-02-27`, `--label r1-relance-v3`,
  `BRANCHE=calcul/r1-relance-v3-reel-v1`, `PLAFOND_AMORCE_MIN=720`, `DELAI_REJEU_MIN=600`.

## Conditions vérifiées avant la commande (§ A.6 du rapport)
1. Concordance consignée : ce fichier, scellé avant la commande.
2. Ligne GO-2026-11-02-27 présente dans `registres/go.md` du dépôt d'où part la commande (`main`, l. 215 : 60 USD, échéance
   2026-11-16, aucune révocation) ; la commande part de `/home/user/controle-ia-travail` sur `main`.
3. Dépenses déjà engagées sous GO-27 dans `registres/depenses.md` : **aucune** (relevé à 06:10 UTC).
4. Branche `calcul/r1-relance-v3-reel-v1` absente du dépôt distant (revérifiée avant la création ; le script la revérifie).
5. Fiche de réception de conv-audit : condition de la **récupération**, non de la création ; rien ne sera récupéré avant son
   message (chemin et empreinte).

Garde de secours de session-depot (hors du texte, remarque A.7-6) : tâche planifiée unique à **`T0 + 12 h 45`** (au-delà du pire
cas de 755 min), qui ne détruit par identifiant que si l'instance existe encore **et** que le journal montre la fin de l'amorce,
ou que l'instance ne répond plus ; sinon elle alerte et ne détruit rien.
