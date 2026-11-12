# Contrôle ciblé (R2, R13) : préenregistrement « mesure unanime » v15, plomberie v15, répétition v15 ; note « lectures possibles » v1 ; usages antérieurs de la donnée réelle

**Verdict A (paquet v15) : à sceller tel quel.** CV14-1, CV14-2 et CV14-3 sont corrigés exactement ; les six sections de
science sont identiques au bit près à la v14 ; le Plan d'analyse ne diffère que par les six noms de sortie ; la plomberie
v15 est celle de la v14 au renommage près ; la répétition rejouée est identique à l'octet et sa note cite `3a1651f4…`.

**Verdict B (note « lectures possibles ») : à retoucher avant scellement — liste courte, six points (NB-1 à NB-6).**
Aucun critère n'est modifié et les seuils cités sont justes ; mais la note vise encore la v14, ses faits de procédure sont
périmés d'une version, et trois phrases disent un peu plus que le verdict gelé.

**Point C (usages antérieurs de `scores-p3.npz`) : aucun travail antérieur n'a calculé une quantité que la mesure unanime
mesure** (ni taux de fausses alertes par épisode honnête entier hors échantillon d'un agrégateur séquentiel, ni r₀). Il
existe trois usages **voisins**, que le texte v15 ne déclare pas. Selon la règle que le coordinateur m'a donnée (déclaration
due si une quantité mesurée est touchée), ce n'est pas un point à corriger dans le texte ; je recommande une **déclaration
hors texte**, scellée et datée avec le préenregistrement avant la course (CV15-1, non bloquant). Dans l'autre sens, **oui** :
la course peut informer la conception de P3-bis, encore en brouillon (CV15-2, à traiter avant la course).

## A. Paquet v15

Fichiers : `sortie-sections-v14-v15-v1.json`, `sortie-plan-v14-v15-v1.txt`, `diff-texte-v14-v15.txt`,
`sortie-diff-plomberie-v14-v15-v1.txt`, `repetition-rejouee-v15.log`, `comparaison-repetition-v15-v1.txt`.

| vérification | résultat |
|---|---|
| empreinte du texte v15 | `3a1651f4b1bc7bda4da5001c32790b9daf9b1ab3509a303fbf2ba82ac144fc1c`, celle annoncée ; non scellé (aucun compagnon) ; `prereg.problemes` : aucun |
| CV14-1 (provenance) | corrigé, lignes 113 à 120 : « présent au moins depuis `9b7721c7`, qui n'est que la borne de l'historique du clone superficiel (commit d'entrée non recherché) » ; même objet `86ec9eaf…` sur `main`, la branche de travail, `calcul/p3-reel-v1` (`eb572dac`) et `4d1fa5c0` — les quatre vérifiés par moi à la passe v14 (arbres git) |
| CV14-2 (refus par chemin) | corrigé, ligne 101 : préfixe codé en dur nommé, chemin résolu et chemin relatif dits passants, fermeture par l'empreinte puis par le script |
| CV14-3 (versions) | corrigé, lignes 35 et 36 : numpy 2.5.4 comme en octobre, Python 3.13.17 → 3.13.18, sortie identique hors manifeste |
| six sections de science | identiques au bit près à la v14 (donc à la v13) |
| Plan d'analyse | six noms distincts, huit occurrences, tous v14 → v15 ; identique à la v14 après remplacement inverse ; aucune occurrence de « v14 » restante |
| reste du diff | titre ; bloc « Version 15 » (lignes 3 à 22), l'ancien bloc rétrogradé « pour mémoire » ; dates et branche ; noms et empreintes de la séquence et des deux tests ; témoin, sortie, sous-dossier ; lignes des trois constats ; traitement de la contre-lecture v14 ajouté **en fin** de section (la section Contre-lecture de la v15 commence par celle de la v14, inchangée). Rien d'autre |
| traitement de ma contre-lecture v14 (lignes 506 à 524) | fidèle : empreinte du rapport `11bc81ab…`, commit `ac858122`, verdict, trois constats, constat sur le test de garde « non bloquant, non rouvert », remarque sur le `rm -rf` |
| `commandes-lecture-reelle-v15.sh` (`ce8da552…`) | remis en v14 par remplacement inverse : identique au modèle v14 **sauf** le paragraphe d'en-tête de commentaire (lignes 4 à 7, « remplace la v14 »), comme le texte le dit (ligne 15) ; aucune ligne de code ne diffère |
| `test-garde-trace-v15.sh` (`055d486c…`), `test-lecture-seule-v15.sh` (`66e8b32c…`) | remis en v14 : **identiques à l'octet** à leurs modèles |
| `garde-trace-reelle-v14.sh` (`a0cf2c53…`) | réutilisée telle quelle ; appelée ligne 51 avec les trois variables ; son compagnon est dans `compagnons()` (ligne 45) |
| compagnons | 20 vérifiés (plomberie v15, `repetition-v15/`, mon dossier v14), aucun écart |
| répétition rejouée (copie isolée, 09:35 → 09:36:17 UTC, code 0) | effectifs, table en vigueur, sortie (manifeste compris), lecture : **identiques à l'octet** ; note : identique hors l'heure de la ligne 3 ; la note déposée cite `3a1651f4…` ; rien d'écrit au premier niveau |
| refus en répétition | par empreinte → code 4 ; par chemin (nom inexistant sous le préfixe) → code 4 ; `repetition-v15/` de la copie intact après les deux |
| v14 déposée / v15 déposée | effectifs et sortie identiques à l'octet ; lecture identique hors `sources.sortie` |
| traces réelles | aucun témoin, journal, sortie ni `.partiel` v15 au premier niveau |

Remarques sans constat : (i) le commentaire d'en-tête de la garde réutilisée dit encore « appelée par
`commandes-lecture-reelle-v14.sh` » : sans effet, elle est scellée et indépendante de la version. (ii) Ligne 119 : l'auteur
dit avoir empreinté le fichier de l'arbre de travail (« contrôle d'intégrité seul ») et remplace « jamais ouvert » par
« jamais chargé ni lu comme données » : formulation plus exacte que celle de la v14, rien à redire.

## B. Note `docs/notes/entretien-resultats-v1/lectures-possibles-mesure-unanime-v1.md`

Ce qui est juste : elle ne modifie aucun critère ; les seuils de M4 sont ceux du Seuil gelé (r₀ < 0,5 ; excès apparié
> 0,02 et borne basse > 0 ; médiane du maximum ≤ 0,08 ; non lisible si r₀ ≥ 0,5) ; les six audits de la ligne 27 sont
exactement les six du Seuil ; la ligne « non concluante ou réfutée » reprend le verdict gelé (« pas de dépassement établi…
pas de conclusion sur le théorème négatif ») ; les phrases des feuilles (1), (4a) et (3a) n'ajoutent rien ; la première mesure
n'est jamais mise en tête ; trente sondes réelles, quatre cents placebo, épisodes honnêtes du premier test,
Llama-3.1-8B-Instruct (préenregistrement de P3, ligne 122) : exacts.

À retoucher :

- **NB-1** — lignes 4, 11 et 25 : « préenregistrement v14 » → **v15** (sections gelées identiques au bit près de la v13 à
  la v15).
- **NB-2** — ligne 18 : « quatorze versions, contre-lue treize fois » est périmé. État exact après ce contrôle : **quinze
  versions ; quinze contre-lectures** (treize rapports entiers, v1 et v3 à v14 ; un complément sur la v2 ; ce contrôle ciblé
  de la v15). « Instances neuves de plusieurs modèles » : vrai (Opus 5.5, Fable 5.1, Fable 5.2).
- **NB-3** — ligne 28 : « Nous avions prédit, **avant les données** » dit plus que le vrai. Les données existent depuis le
  20 octobre et ont servi à d'autres analyses (point C). Écrire : « avant toute lecture de ces scores pour cette mesure ».
  De même, « à une date posée par un tiers » et, ligne 18, « figée chez un tiers » ne sont vrais que si le gel chez le
  tiers a eu lieu avant la course : à dire ainsi, ou à retirer sinon.
- **NB-4** — ligne 28 : « Sur les scores réels de trente sondes, c'est ce que nous mesurons » laisse entendre une dépendance
  naturelle ; M4 mesure l'effet d'une dépendance **injectée**. La limite est dans la troisième colonne, mais elle doit être
  dans la phrase : « sur les scores réels de trente sondes, en y injectant cette dépendance, c'est ce que nous mesurons ».
  Dans les limites : « à marges préservées » → « à moyenne et variance marginales préservées » (le Seuil dit « mêmes deux
  premiers moments » ; la forme des marges change) ; ajouter « une seule intensité d'injection (τ = 2) », que le verdict gelé
  de la ligne voisine cite.
- **NB-5** — ligne 30, feuille (2a) : « C'est la forme des scores, **non leur dépendance**, qui fait dépasser la règle »
  affirme une absence ; le verdict gelé dit seulement « D n'étant pas établie », avec une réserve si bb(D′) > 0. Écrire :
  « la règle dépasse par la forme des scores ; une contribution de leur dépendance n'est pas établie ». Même ligne : dire
  d'abord que la mesure principale n'était pas lisible (« la dépendance naturelle est déjà forte ; la quatrième mesure ne se
  lit pas »), sinon le jury n'apprend pas que l'issue annoncée n'a pas été rendue.
- **NB-6** — ligne 27 : « nous **publions** l'audit » engage une publication, qui est un nœud de Lazar : « nous rapportons
  l'audit ». Et la table n'est pas exhaustive : « quatrième mesure confirmée » avec première mesure non concluante ou
  réfutée, ou contrôle « fragile », n'a pas de phrase ; la règle de la ligne 12 (« toute autre formulation est un nœud »)
  couvre ces cas, mais le titre « une issue, une phrase » devrait le dire.

## C. Usages antérieurs de la donnée réelle (lecture de code et de textes seulement)

**(1) Ce que les travaux antérieurs ont calculé sur les scores de P3.**

| travail | ce qu'il calcule sur les épisodes honnêtes | touche une quantité mesurée ? |
|---|---|---|
| lecture décisive de P3 (`src/controle_ia/premier_test_ia/lecture.py`, `statistiques.py`) | aires saboteur / témoin / mention contre honnête ; corrélation score-coût sur l'honnête ; **P3-P5 `accumulation`** (lignes 258 à 296) : pour les deux sondes principales, scores réduits par la moyenne et l'écart type des actions honnêtes, somme et maximum par épisode, seuil = quantile 0,99 des 60 épisodes honnêtes **dans l'échantillon** (donc leur maximum), rappel sur le saboteur, `faux_positifs_observes` dans l'échantillon (nul par construction) | **non** : pas de taux hors échantillon, pas de règle de Ville, pas de seuil par action, pas de r₀. **Voisin** : le seuil réduit du maximum honnête est une valeur publiée dans le dépôt (rapport de préparation de P3-bis, ligne 39) ; il renseigne sur la queue des scores honnêtes d'une sonde principale, donc, de loin, sur la branche « marges » de M2 ter |
| addenda 1 et 2 de P3 | aires, strates de coût, corrélations de rang score-longueur sur l'honnête, puissance du nul | non |
| agrégation R1 v4 (`src/controle_ia/agregation_r1_v4/`) | charge de `scores-p3.npz` les identités et les scores des sondes de P3 (source G) ; calcule par épisode **les mêmes statistiques** que la mesure unanime (somme, maximum, Page k = 0,5, processus e ρ = 0,5, balayage w = 3) et leurs **aires** saboteur contre honnête ; D5 : part des épisodes témoins et « mention » au-dessus de la troisième valeur honnête | **non** : aires et rappels, jamais un taux de fausses alertes sur l'honnête hors échantillon, jamais r₀ ; l'effet d'épisode n'y est que simulé. **Voisin** : mêmes statistiques, mêmes 60 épisodes honnêtes |
| P3-bis (`puissance_p3_bis_v1.py`, `_v2.py`, rapport de préparation) | ne lit que des sorties sous `diag/` (lecture de P3, addendum 2, durées) ; reprend P3-P5 | non |
| `docs/notes/rapport-directeur-v1/recalcul-v1.py` | refait les aires de P3 et de R1 v4 depuis les objets git | non |
| `scripts/essai_fermeture_p3bis_v1.py`, tests | plomberie, empreintes | non |

Recherche de « intraclasse » et de ses variantes dans tout le code (`src`, `scripts`, `docs`, `prereg`, `brouillons`,
`tests`) : seulement la simulation T0.3, `bases/sequentiel.py` et ce paquet. Noms de clés (sans valeurs) des sorties
`lecture-p3.json`, `lecture-addendum-p3.json`, `lecture-addendum2-p3.json` : aucun taux par épisode autre que P3-P5, aucune
corrélation intra-épisode. Je n'ai lu aucune valeur de ces sorties et n'ai pas ouvert `diag/*/lecture-sondes-t06.json`.

**(2) Ce que le texte v15 déclare.** Rien : pas de section « valeurs déjà vues ». Seules phrases : ligne 78, « aucune
lecture des scores réels avant le scellement (R1) », dans la puce du code d'analyse (lue dans son contexte : ce code n'a
jamais tourné sur les scores réels — vrai) ; ligne 119, « jamais chargé ni lu comme données par les auteurs de la v14 et de
la v15 ».

- **CV15-1** (déclaration ; **non bloquant, hors texte**) — aucun usage antérieur ne touche une quantité mesurée : le texte
  n'est pas à corriger, et la prédiction de M4, conditionnelle au r₀ mesuré, n'en dépend pas. Mais le fichier a été lu par
  quatre analyses du programme, deux d'entre elles sur des quantités voisines, et un lecteur extérieur qui lirait « aucune
  lecture des scores réels » sans son contexte serait trompé. **Recommandé** : une courte note « usages antérieurs de la
  donnée de la mesure unanime », scellée et datée par le tiers avec le préenregistrement, **avant la course**, qui reprend le
  tableau ci-dessus (ou renvoie à ce rapport par chemin et empreinte) et dit que la valeur de P3-P5 était connue du
  programme. Si une v16 devait exister pour une autre raison, y porter cette déclaration.
- **CV15-2** (sens inverse ; **à traiter avant la course**, décision de Lazar) — P3-bis n'est pas scellé
  (`P3-bis-preenregistrement-v1-brouillon9.md`). Son hypothèse H-B2 et ses prédictions PB-2 et PB-14 (lignes 370 à 372, 392,
  404, 441 à 451) reposent sur un critère par épisode : statistique « maximum », seuil au maximum des 60 épisodes honnêtes,
  test exact sous échangeabilité, seuil k ≥ 6 ; la ligne 457 note que « rien ne contrôle » la croissance du maximum avec la
  longueur. La mesure unanime rendra, sur les mêmes sondes et les mêmes épisodes honnêtes : le taux hors échantillon du
  maximum conforme par épisode (M3), le taux du seuil par action (M1), r₀ brut et centré par pas, l'effet des marges et de
  la dérive avec le pas (M2 ter). Ces valeurs peuvent orienter le choix de la statistique, du seuil et de k de P3-bis.
  Trois façons de fermer : sceller P3-bis avant la course ; ou inscrire les sorties de la mesure unanime dans les « valeurs
  déjà vues » de P3-bis et geler dès maintenant H-B2, PB-2 et PB-14 tels qu'ils sont ; ou tenir l'auteur de P3-bis à l'écart
  des sorties jusqu'à son scellement. C'est une contrainte sur P3-bis, pas un défaut de la v15.

## Ce que j'ai fait et pas fait

- Aucun fichier de `donnees/` ouvert, lu, listé, empreinté ni passé en argument. Mode réel jamais lancé ; `LECTURE_SEULE`
  seulement par le test déposé, dans son dossier temporaire, avec des commits factices. Aucun fichier existant modifié ; seul
  `contre-lecture-v15/` est écrit. Ni le préenregistrement ni la note ne sont scellés par moi. Aucune dépense.
- Incident : ma première commande commençait par `git pull` et a été mise en arrière-plan par l'environnement ; je l'ai
  arrêtée par son identifiant de tâche (R10) avant qu'elle n'écrive quoi que ce soit dans le paquet, puis j'ai relancé les
  vérifications sans `pull` (la branche était déjà à `939a27de`).
- **Contre-lecteur** : sous-agent **Fable 5.2** (`claude-fable-5-2`), modèle différent de l'auteur (Opus 5.5) ; le même
  que pour la v14, donc neuf pour le texte v15 mais pas pour le dossier. Je n'ai écrit ni le préenregistrement, ni la
  plomberie, ni la note ; la v15 reprend des corrections que j'ai proposées dans mon rapport v14.
- Heures (`date -u`) : début 09:33 UTC le 10 novembre 2026 ; répétition rejouée finie à 09:36:17.

## Mes fichiers (dans ce dossier, chacun scellé)

| fichier | contenu |
|---|---|
| `heure-debut.txt` | relevé `date -u` |
| `diff-texte-v14-v15.txt` | `diff` brut des deux textes |
| `sortie-sections-v14-v15-v1.json` | six sections au bit près (script de la passe v14 ; son volet « Plan » cherche les noms v14 et ne vaut pas ici) |
| `sortie-plan-v14-v15-v1.txt` | Plan d'analyse par remplacement inverse v15 → v14 ; section Contre-lecture en ajout seul |
| `sortie-diff-plomberie-v14-v15-v1.txt` | séquence et deux tests remis en v14, comparés à leurs modèles |
| `repetition-rejouee-v15.log`, `comparaison-repetition-v15-v1.txt` | répétition rejouée, deux refus, comparaison au dépôt et à la v14 |
