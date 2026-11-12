# Consigne : mise à jour de la page publique de l'organisme d'idéation avec le résultat scellé d'A1-v4 — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 10 novembre 2026 (heure au registre). **Mot de Lazar**, verbatim : « depose les derniers resultats sur gthub pour le mentor kirhner ». Le mentor de l'organisme d'idéation attend le résultat de la reprise de l'attaque de Goodhart contre le nul v9 (R-1883). La publication est réglée d'avance par le texte scellé de la course, § 0.8 (« go par anticipation » de Lazar, R-1890) : **la mère pousse le résultat et le verdict scellés sur la page publique, chiffres du verdict scellé seulement**.

Destinataire : un **rédacteur neuf**, qui n'a écrit aucune pièce d'A1-v4 (texte, code, lecture, audit, verdicts). Il écrit en **anglais**, dans le style de la page existante. **Il ne pousse rien et ne committe rien** : la mère le fera après une contre-lecture par un autre modèle.

## Sources (empreintes à vérifier avant lecture)

- Texte scellé de la course : `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v5-v1.md` (`d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6`) : § 0.1, § 0.5 bis, § 0.6, § 0.8, § 6 (critères), § 3 (prédictions).
- Verdict officiel : `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md` (`e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda`), en entier, avec sa lecture bornée gelée et ses réserves (§ 4, § 5).
- Pièce d'intégrité : `…/verdict-a1-v4-v1/integrite-versement-a1-v4-v1.txt` (`f8af0257…`), pour l'empreinte de la liste des empreintes de la sortie scellée (`e72893ef…`) ; la sortie elle-même reste privée et **ne s'ouvre pas**.
- Validation du v9 : `docs/verdicts/verdict-validation-nul-v9-v1.md` (`1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea`), **pour son issue seulement** (« puissance perdue ») et le nœud qu'elle ouvre.
- Décision N-064 (`docs/decisions/decision-N-064-v1.md`) et la note d'antériorité `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-popper-evaluator-v1.md` (`d1ab7049…`), avec la note Co-Scientist qu'elle suit : références exactes des quatre travaux à citer, revendication resserrée (O2) et ce qui ne reste revendiqué que dans sa forme (O11, O12).
- La page et le README publics actuels, dans le clone `/home/user/lciric/ideation-organism` : d'abord `git -C /home/user/lciric/ideation-organism fetch origin refs/heads/main:refs/remotes/origin/main`, puis vérifier que `main` local égale `origin/main` (sinon, rapporter et s'arrêter).

## Ce qu'il faut écrire

1. **`resultats/attaque-goodhart-v2/README.md`** : une section neuve en tête, « Update (10 November 2026): the attack against v9 (A1-v4) », au-dessus de la mise à jour du 8 novembre, qui reste **inchangée** ; la ligne « Last updated » remise à l'heure par `date -u`. Contenu :
   - ce qui a tourné : v9 éprouvé **comme candidat** (le juge de production reste le v8) ; un fournisseur (Argon), une forme d'optimisation, 24 cartes par monde, 24 unités par case, au plus 16 tentatives, bras avec et sans les verdicts ; les deux mondes, décrits exactement comme le texte scellé les définit (W2 ; W2 gradué à la dose 0,40, à la frontière déclarée du v9) ; ce que chaque monde éprouve ; la dépense comptée par la course et son plafond ; empreintes du texte, de la liste des empreintes de la sortie, et du verdict ; le chemin de lecture (sortie scellée avant toute lecture, fonctions gelées, audit écrit par un auditeur neuf, verdict officiel par un lecteur neuf d'une autre famille de modèles ; écart déclaré : l'audit et le verdict provisoire sont du même lecteur) ;
   - **les deux issues**, avec leurs comptes, leurs intervalles, les dents (ancien juge) et **la lecture bornée gelée de chacune, traduite fidèlement**, avec ce qu'elle ne dit pas (« not "the rate is below 0.05" » ; « not "v9 has no price" ») ;
   - les prédictions : combien tenues sur onze, lesquelles ne le sont pas, avec observé et seuil ;
   - **les réserves du verdict** (§ 4 et § 5), toutes, en une ligne chacune ;
   - **la règle « jamais seul »** du § 0.5 bis : le résultat se lit avec A1 et les trois courses d'A1-v3 ; dire en une ligne chacune ce que sont ces courses, avec les seuls chiffres que le § 0.5 bis en donne ;
   - **les deux nœuds non tranchés** : le prix du v9 (sa validation décisive a rendu l'issue qu'elle attendait par écrit, « power lost », empreinte du verdict ; son adoption comme nul de production attend la décision du responsable du projet) ; le sens de « rien au-delà de l'archive » ; et ce que la course ne tranche pas (§ 0.5 bis, (c) à (f)).
2. **`README.md`** (racine) : la ligne d'état en tête et la ligne de la table qui décrit l'attaque de Goodhart, mises à jour en une ou deux phrases avec renvoi à la page ; et, **s'il manque**, un court paragraphe « Related work » qui cite les quatre travaux exigés par N-064 point 4 (POPPER ; Dwork et al. ; Blum et Hardt ; Co-Scientist), avec leurs références exactes tirées de la note d'antériorité, et dit ce qui est occupé et ce qui reste revendiqué (N-064 points 2 et 3). Rien d'autre ne change dans le README.

## Interdits de contenu

- **Aucune recette** : aucune consigne servie au proposeur, aucune loi promue, aucune réponse du proposeur, aucun extrait de la sortie.
- **Aucun chiffre** qui ne soit dans le verdict officiel, dans le § 0.5 bis du texte scellé, ou dans la page actuelle.
- Aucun identifiant de session, aucun chemin du dépôt privé, aucun nom de personne hors des auteurs des travaux cités (« the project lead » pour Lazar), aucune mention du programme de contrôle au-delà de ce que la page dit déjà.
- Aucun mot plus fort que la lecture gelée : jamais « validated », « robust judge », « secure », « proves ».

## Sorties

Dans `/home/user/page-a1v4/` (dossier neuf, hors des deux dépôts) : les deux fichiers modifiés aux mêmes chemins relatifs (`resultats/attaque-goodhart-v2/README.md`, `README.md`) ; `diff-page-a1v4-v1.patch`, produit par `git -C /home/user/lciric/ideation-organism diff --no-index` ou par `diff -u` contre les fichiers actuels ; `journal-page-a1v4-v1.md` (sources lues et leurs empreintes, chaque chiffre de la page avec sa source et sa ligne, choix, manques). Calcule le sha256 de chaque sortie et écris-le dans le journal. **Le clone n'est pas modifié** (hors du `fetch` à refspec explicite).

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, règle 9 comprise. Aucun appel externe hors du `fetch` nommé, aucune dépense, aucune écriture git, aucune poussée, aucune valeur de clé. Toute heure relevée par `date -u`. Si un contrôle de permissions ou un classifieur refuse une action, arrête-toi et rapporte-le tel quel.

## Réponse à la mère

Courte : chemins et empreintes des sorties ; le texte de la section neuve ; les chiffres et leurs sources ; les manques ; tout refus.
