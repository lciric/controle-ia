# Empreintes du programme « Contrôle boîte blanche des menaces diffuses »

Ce projet de l'Open Science Framework ne contient que des **empreintes** (SHA-256), jamais les documents eux-mêmes.
Il sert à faire horodater par un tiers que les préenregistrements, verdicts de porte et décisions du programme
existaient, tels quels, au plus tard à la date de dépôt que l'interface affiche pour chaque fichier.

## Ce que contient `manifeste-v3.json`

Pour chaque fichier scellé des dossiers `prereg`, `docs/verdicts`, `docs/decisions` du dépôt de travail
(`https://github.com/lciric/controle-ia-travail`, copie expurgée publique : `https://github.com/lciric/controle-ia`) : son chemin, son empreinte SHA-256,
le chemin de son empreinte compagnon `.sha256` et le dernier commit git qui l'a touché.
Références lues : HEAD (8476008ea29a…), origin/claude/compassionate-meitner-d4ryyk (8549ae01b41a…). Nombre de fichiers : 167.

## Ce que les empreintes prouvent — et ce qu'elles ne prouvent pas

- Elles prouvent qu'un document dont l'empreinte figure ici **n'a pas été modifié après la date de dépôt** du manifeste :
  tout changement d'un seul octet change l'empreinte.
- Elles prouvent donc qu'une hypothèse, une prédiction chiffrée, un seuil ou un critère de lecture gelé
  a été écrit **avant** la lecture du résultat qu'il encadre, si la date de dépôt précède le résultat.
- Elles ne prouvent **ni** que le contenu est juste, **ni** que les résultats sont bons : seulement l'antériorité et l'intégrité.
- Le dépôt est fait par l'équipe du programme ; l'horodatage, lui, est rendu par l'Open Science Framework.

## Comment un tiers vérifie

1. Noter, dans l'interface de l'Open Science Framework, la date de dépôt et l'empreinte SHA-256 du manifeste
   (métadonnées du fichier). Télécharger le manifeste et recalculer : `sha256sum manifeste-v3.json` ;
   les deux empreintes doivent coïncider.
2. Pour un document donné, obtenir le fichier à son chemin dans le dépôt (au commit indiqué) :
   `git show <commit>:<chemin> | sha256sum` ; l'empreinte doit être celle du manifeste.
3. Si elle coïncide, le document est identique à celui qui existait à la date de dépôt du manifeste.
