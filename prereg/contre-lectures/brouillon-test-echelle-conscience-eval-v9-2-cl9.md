# Contre-lecture R2 du préenregistrement « fuite du format et échelle, Llama-3.1 8B contre 70B » (brouillon v9-2) — cl9

- **Rôle** : sous-agent neuf, neuvième contre-lecteur au sens de R2. Je n'ai écrit ni le brouillon v9-2, ni les versions précédentes, ni le code, ni les tests, ni les contre-lectures n° 1 à 8.
- **Consigne** : `docs/notes/echelle-conscience-eval/v9/consigne-contre-lecture-cl9.md` (`2d6a473e99c961f08080df1e71599feb8113b277d87a9598948609285384e203`), conforme à son compagnon ; suivie à la lettre.
- **Heure** (`date -u`) : 27 octobre 2026 ; lecture commencée à 12:28:33 UTC ; essais finis à 12:46:27 UTC ; contrôles de fin à 12:46:41 UTC ; rapport achevé à 12:50 UTC.

## Empreintes des pièces lues (sha256)

| pièce | sha256 |
|---|---|
| `prereg/brouillon-test-echelle-conscience-eval-v9-2.md` (texte relu ; conforme à son compagnon au début, 12:28, et à la fin, 12:46, de ma lecture) | `3efab8e4f42b5059da8da7b1d91a5055a7e9c9957e82684461e1c54494117a49` |
| `prereg/brouillon-test-echelle-conscience-eval-v9.md` | `27026f1a25e2ab2c19d5bdd0a829aef8d2b99ce36c9480c15c4155d18ce7e0f9` |
| `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v9-cl8.md` | `260ec939e9dc27795ee2779f6188ad294bc4767955f73c83087da4807b3914ff` |
| `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v8-cl7.md` | `0093def46360e36d96c44e4bfc961a024db8d1069a1a7fdf9a6ca3671a09a8d6` |
| contre-lectures n° 1 à 6 (`test-…-v2-cl1.md`, `…-v3-cl2.md` à `…-v7-cl6.md`) | `70afa519…`, `9b476cf4…`, `a2f330f0…`, `5728de4c…`, `4ea69784…`, `3d7a60fc…` (conformes à leurs compagnons) |
| les 20 outils du tableau du texte (`echelle-v8/…`) | les 20 empreintes concordent avec le fichier et son compagnon ; chaque fichier de `echelle-v8/` (hors stimuli) est identique à l'objet du commit `9ccc383…` |
| les 69 traces du tableau « Traces » | toutes conformes au fichier et à leur compagnon |
| les 29 empreintes abrégées du corps du texte | toutes conformes, chacune rapprochée du chemin qui la précède |
| `src/controle_ia/prereg.py`, `scellement.py`, `.claude/hooks/garde_calcul.py` | `3b2e3ee5…`, `93beeb1c…`, `84512d4a…` (inchangés depuis cl4 à cl8) |
| `registres/go.md` (en-tête lu ; aucune ligne ne cite `test-echelle-conscience-eval`) | `0d0a198dc868d80ed5ce3d58171157de0283f45ad61d12d3c902db1d371375fa` (celle que cl8 a lue) |
| cartes `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md`, `-v2.md`, `-v3.md` | `134040bd…`, `fe1e93c1…`, `9d03d3b2…` |
| générateur de cl8 recopié dans mon bac à sable (`banc_cl8_commun.py`) | `20835d6e967eca8b…`, identique à la trace versée |

## Ce qui a été lu et essayé

- **Texte** : brouillon v9-2 en entier ; brouillon v9 et différence mot à mot (`sorties/diff-v9-v9-2.txt`) : seuls changent l'en-tête, H_0, « Rapport des Ec », la ligne de la réserve au tableau « Seuil », « D'où deux réserves », « Prix des réserves », « Pourquoi 1,15 », R3, l'audit (une parenthèse), le rejeu de cl7 (CLS-05), le paragraphe « modèle idéalisé », les deux réserves, les phrases obligatoires, la phrase du désaccord (cohérence), la limite « autour de ce centre », le prix sous H_0, le tableau des écarts et le tableau des traces. Liste d'arrêt, plan d'analyse, conditions P(s) et I(s), seuils et commandes : inchangés.
- **Contre-lectures** : cl8 en entier et ses pièces (scripts, sorties, résumés) ; cl7 (verdict, constats, traitement) ; constats et traitements de cl1 à cl6.
- **Code** : arbre de travail `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/`, branche `outils/echelle-conscience-eval-v8`, tête `9ccc383c02a08e58928368b23471f4c438e06cda` ; arbre propre avant et après mes essais ; index de l'arbre de travail inchangé (10:47:00 UTC) ; appels git en lecture seule, avec `GIT_OPTIONAL_LOCKS=0`. Lu en entier : `analyser_echelle_v8.py`, `lancer_echelle_v8.sh`, `verifier_go_v8.py` ; lus en partie : `simuler_atteignabilite_v8.py` (générateur), `test_analyser_echelle_v8.py` (générateur, substitution de `etat_scripts`). Stimuli lus par Python seulement.
- **Gardes héritées** : `exiger_prereg_scelle`, `problemes`, `sections` ; `garde_calcul.py` ; en-tête de `registres/go.md`. `problemes()` sur le brouillon v9-2 : un seul manque, « section vide ou à remplir : Contre-lecture », comme attendu. `prereg/test-echelle-conscience-eval-v9.md` est absent (nom libre). Le lanceur exige ce nom (`PREREG=…`, l. 43) et que le texte scellé cite le commit en entier (l. 60) : le brouillon le cite.
- **Essais** (scripts et sorties dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lecture-echelle-v9-2/`, avec `TMPDIR`, `HF_HOME` et `--basetemp` dedans, `-B`, `PYTHONDONTWRITEBYTECODE=1`, fils de calcul à un, bornes de durée explicites) :
  - tests du commit avec le modèle minuscule local : **401 passed in 500,29 s**, de 12:30:08 à 12:38:29 UTC (`sorties/tests-cl9.txt`) ;
  - contrôle de toutes les empreintes citées (`scripts/verif_empreintes.py`, `verif_abregees.py`) ;
  - **recompte de tous les chiffres nouveaux sur les fichiers bruts de cl8** (`scripts/recompter_bancs_cl8.py` sur `banc-cl8-BDC.jsonl`, `banc-cl8-Z.jsonl`, `banc-cl8-Z2.jsonl`, `banc-cl8-Z-n2000.jsonl` ; lecture de `sortie-largeurs-simulation.txt`, `sortie-Q-bande.txt` et de leurs scripts) et sur la sortie scellée de la simulation (`scripts/verif_simulation.py`) ;
  - **identité du rapport des Ec dans le modèle linéaire sans bruit**, et seuils de la bande des deux côtés (`scripts/formule_q.py`, `sorties/formule-q.txt`) ;
  - **banc nouveau, vérification indépendante d'un point que cl8 n'a pas couvert** : le vrai miroir en signe de la famille D sous une composante propre à un jeu (`scripts/banc_cl9_miroir.py` ; générateur de cl8 recopié, empreinte identique à la trace versée ; analyse v8 du commit telle quelle, mode répétition, `etat_scripts` remplacé par une constante pour qu'aucun appel git ne touche l'arbre) : 18 analyses à 300 tirages, puis trois confirmations à 2 000 tirages (`sorties/banc-cl9-miroir*.jsonl`, résumés `sorties/resume-banc-cl9-miroir*.txt`).
- **Interdits respectés** : aucun fichier interdit ouvert, lu ou haché (la liste du dossier `prereg/` a montré le nom de `P3-consignes-v1.md`, ni ouvert ni haché) ; aucune recherche récursive dans le dépôt (listes des dossiers nommés seulement) ; aucun réseau ; aucune commande vastai ; aucun lancement ; aucune écriture git ; rien de modifié hors de mon bac à sable (vérifié à 12:46 UTC : brouillon v9-2 conforme à son compagnon ; aucun fichier plus récent que mon départ dans `prereg/`, `prereg/contre-lectures/`, `docs/notes/echelle-conscience-eval/`, ses dossiers `v8/`, `v9/`, `v9/contre-lecture-cl8/` ; arbre de travail propre ; aucun `__pycache__` nouveau) ; aucune clé ni aucun jeton cherché, affiché ou écrit (adresse du dépôt distant lue avec masquage).

## Verdict

**Scellable après corrections.** Aucun défaut ne bloque. Le traitement de cl8 par le texte seul est juste sur le fond et ses chiffres sont exacts ; garder le code `9ccc383…` tel quel est défendable. Restent **cinq corrections du texte seul**, sans commit nouveau, avant le scellement :

- **CLR-01** (à corriger, prioritaire) : le vrai miroir de la famille D sous une composante propre à un jeu fabrique **« positif » sous H_0 sans aucune réserve**, tenu à 2 000 tirages. Le texte ne le dit que pour « inverse », et cite comme « miroir » un banc de cl8 qui n'en est pas un. « Positif » est le signe que l'auteur attend : R3 et R4 demandent que le texte ne le laisse pas croire mieux protégé.
- **CLR-02** (à corriger) : le mot « pureté » est pris en deux sens contraires. Le texte dit que q n'estime k qu'à puretés égales, puis appelle « puretés égales » le cas |s_a| = |s_b|, où les puretés diffèrent dès que k ≠ 1 : c'est précisément ce qui tire q vers 1.
- **CLR-03** (à corriger) : le seuil de k selon r n'est écrit que pour un jeu b plus fort. La phrase « la bande ne sonne que si k dépasse √(1,3225 + 0,3225·r) » est fausse pour k < 1, et la bande voit moins bien un jeu b plus faible.
- **CLR-04** (à corriger) : la phrase obligatoire « n'écarte pas cette part de H_0 » ne suit que la réserve « λ change ». Des issues fausses signalées par la seule réserve « contexte inégal » existent pourtant : la graine 3870 de la simulation scellée, la graine 41306 du banc de cl7. Elles perdraient cette phrase.
- **CLR-05** (à corriger) : la phrase « Ce tableau montre […] l'absence de faux positif sans réserve dans ces cas » est héritée des versions précédentes. Le tableau la dément lui-même (doubles signatures : un « positif » et quatre « inverse » sans aucune réserve), et l'ajout du v9-2 (« hors de ces cas ») la fait lire comme générale.

Remarques : CLR-06 à CLR-10. Après correction, une contre-lecture neuve et courte des passages changés (R2) suffit à mon avis.

**Sur la question de la consigne (le code inchangé est-il défendable ?)** : oui, au regard de R3, R4 et R5.

- **R3** : aucune réserve ni aucun seuil ne dépend des mesures, et la lecture reste mécanique et symétrique en signe. Rien ne permet de viser un signe. Le défaut de CLR-01 tient au texte, qui sous-estime un signe, et non au code.
- **R4** : les deux réserves s'appliquent de la même façon à « positif », « inverse » et « nul ». Le code émet des drapeaux, et le texte gelé en fixe la lecture, comme pour les phrases, qui ont toujours été écrites par le lecteur et non par le code. Le texte de la réserve « jeux de force de contexte inégale » affirme plus qu'il ne sait (CLS-01), mais le texte gelé dit comment le lire.
- **R5** : les réserves ne sont pas des gardes d'arrêt. Leurs bornes sont testées (cas sain, artefacts), et aucun repli n'est silencieux.
- Aucune garde fondée sur e(m) et q ne verrait les artefacts de CLS-01 ni celui de CLR-01 (e(m) près de 0, q près de 1 : vérifié dans mon banc). Un commit nouveau ne fermerait donc rien. Seul un troisième jeu de cadrages tenu à part le permettrait.

## Ce qui tient

- **Empreintes et commit** : 20 outils sur 20, 69 traces sur 69, 29 abrégées sur 29. La tête de la branche locale est le commit attendu, et l'arbre est propre. Les gardes héritées et le registre des GO sont inchangés depuis cl8. Le nom scellé est libre.
- **Tests** : 401 passent chez moi en 500,29 s (la trace versée dit 498,57 s, cl8 498,22 s).
- **Concordance du texte et du code** :
  - nom et texte de la réserve « jeux de force de contexte inégale » (`analyser_echelle_v8.py`, l. 572–573) : le texte les cite fidèlement (« nomme des « jeux de force de contexte inégale » et dit que la cohérence des deux sens et λ ne se comparent plus ») ;
  - bande `max(q, 1/q) > 1,15`, q non défini si un Ec ≤ 0 (l. 585–587, 761–765), comme au tableau « Seuil » ;
  - les deux réserves ne visent que « positif », « inverse » et « nul » (l. 606) ;
  - nom du texte scellé exigé par le lanceur : `prereg/test-echelle-conscience-eval-v9.md` (l. 43), celui que le brouillon annonce ;
  - commandes inchangées.
- **Formule de q** : q = |k·u + s_b| / |u + s_a| est juste dans le modèle linéaire sans bruit (et λ n'y dépend ni de s_a ni de s_b). À |s_a| = |s_b|, q = √((k² + r)/(1 + r)) est juste, ainsi que le seuil côté k > 1 : 1,167 à r = 0,12 ; 1,264 à r = 0,85 ; 1,403 à r = 2 (`sorties/formule-q.txt`). Voir CLR-02 et CLR-03 pour ce qui manque.
- **Chiffres nouveaux, tous recomptés sur les sorties brutes** (`sorties/recompter-bancs-cl8.txt`, `verif-simulation.txt`) :
  - banc BDC :
    - 186 analyses, aucune en arrêt ;
    - familles B : 15 cas, 90 analyses ; 21 « positif » ou « inverse », dont 19 avec « λ change » et 2 sans aucune réserve ;
    - graine 81002 : e(m) 0,070 [−0,072 ; 0,216] et 0,068 [−0,034 ; 0,170], q 1,025 et 1,027 ;
    - graine 102000 : e(m) −0,096 [−0,208 ; 0,021] et −0,131 [−0,305 ; 0,015] ;
    - familles D : 84 analyses, aucune issue prononcée ;
  - demi-largeurs médianes de l'intervalle de e(m) : 0,137, 0,211 et 0,357 ;
  - valeurs de q hors bande à contextes égaux : 0 sur 216, 6 sur 232, 8 sur 24 ;
  - banc Z :
    - à k = 1 sous une composante de norme 3 : 7 « nul » sur 7 avec « contexte inégal » ;
    - sous × 1,25 : 4 « nul », avec « λ change » seulement, q de 0,957 à 1,042 ;
    - famille D (Z et Z2, 18 analyses) : « inverse » 6, dont 2 sans aucune réserve (graines 145008 et 145118), 4 avec « λ change » ; q de 0,949 à 1,046 ;
    - graine 145008 à 2 000 tirages : « inverse » sans réserve, e(m) −0,025 [−0,152 ; 0,112] et 0,105 [−0,022 ; 0,241], q 0,998 et 1,014 ;
    - le « miroir » de cl8 : 4 « positif », tous avec « λ change » ;
  - banc Q : au tau 0,4 en dimension 256, sous × 1,333, 2 analyses sur 3 ont au moins un modèle hors bande ;
  - simulation scellée :
    - sous H_A avec la signature d'un seul jeu, 3 « positif » sur 3 portent « λ change » (graines 3190, 3192, 3766) ;
    - fausses alertes à contextes égaux : 3 sur 51 ;
  - rejeu de cl7 : graines 43202 et 43206, les deux réserves.
- **H_0 et les phrases obligatoires pour « λ change »** : elles disent vrai. Un « positif » ou un « inverse » qui porte cette réserve peut venir de la classe voisine (rejeu de cl7, 18 cas) comme de H_A (simulation, 3 cas). Un « nul » qui la porte peut venir de H_A compensé (familles C de cl7). La symétrie entre « positif » et « inverse » d'une part, et « nul » d'autre part, est respectée.
- **Lecture symétrique** : deux sens, deux modèles, mêmes règles ; les issues positives et négatives portent les mêmes réserves. La limite générale (« toute issue prononcée, avec ou sans réserve, se lit donc sous cette limite », l. 426) couvre tout ce que j'ai trouvé.
- **CLS-04** : « coûterait sans doute sous les H_A faibles ; ce coût n'est pas simulé » (l. 193) : conforme.

## Traitement des constats de cl8

| constat de cl8 | gravité | état | preuve ou réserve |
|---|---|---|---|
| CLS-01 le rapport des Ec mêle k et la pureté ; la famille D passe sans réserve sous une composante propre à un jeu | bloquant | **traité, trois restes du texte** | Le texte dit que q n'estime k qu'à puretés égales (l. 150), écrit la formule (l. 151), dit comment lire la réserve (l. 193, 365) et que son absence n'établit rien (l. 365). Il borne la bande à son réglage (l. 198), borne R3 au générateur (l. 282) et dit que la classe voisine passe sans aucune réserve (l. 288, 425–426). Formule juste et chiffres exacts. Garder le code est défendable (verdict). Restes : « pureté » en deux sens (CLR-02) ; seuil de k écrit d'un seul côté (CLR-03) ; le « miroir » cité n'en est pas un, et « positif » passe aussi sans réserve (CLR-01) |
| CLS-02 petite amplitude, R3 dit trop | à corriger | **traité, un reste** | R3 bornée au générateur et aux amplitudes simulées (l. 282). Les 2 cas du banc BDC sont chiffrés exactement, la demi-largeur de e(m) aussi (l. 424). Reste : la phrase du « modèle idéalisé » (l. 305), contredite par le tableau (CLR-05) |
| CLS-03 prix des réserves ; une issue réservée ne sépare pas H_A de la part de H_0 | à corriger | **traité en partie** | Prix sous H_A (3 sur 3), fausses alertes selon l'hétérogénéité (0 sur 216, 6 sur 232, 8 sur 24) et sous une composante (7 sur 7) : exacts. H_0, la réserve « λ change » et les deux phrases obligatoires s'accordent et disent vrai. Reste : rien de tel pour une issue signalée par la seule réserve « contexte inégal », qui existe dans la simulation scellée (CLR-04) |
| CLS-04 argument non chiffré | remarque | **traité** | l. 193 |
| CLS-05 petits écarts | remarque | **traité** | Graines 43202 et 43206 : les deux réserves, relu dans le résumé du rejeu ; « tiennent » (l. 391) ; branche poussée : affirmée, non vérifiable sans réseau (CLR-07 ; le lanceur la revérifie) |

Bilan : cinq constats traités, dont CLS-01 et CLS-03 avec des restes du texte seul.

## Constats nouveaux

### CLR-01 — À CORRIGER (prioritaire) — Le vrai miroir de la famille D sous une composante propre à un jeu fabrique « positif » sous H_0 sans aucune réserve ; le texte ne le dit que pour « inverse »

- **Localisation** : brouillon v9-2, l. 8 (en-tête : « famille D de cl7 sous une telle composante : « inverse » sous H_0, 2 fois sur 18 ») ; l. 288 (R3 : « Le miroir (« positif ») rend 4 « positif », tous avec « λ change » ; la construction est symétrique en signe ») ; l. 425 (limite : « même sous un écart de force de contexte de 25 à 40 % » ; « famille D : « inverse » sous H_0 sans aucune réserve ») ; l. 551 (traitement de CLS-01).
- **Constat** :
  - Le mécanisme de la famille D est le suivant. Sous une fuite égale α, le terme α(1/k − 1) de e(m) compense l'écart que créent des signatures croisées. Il est négatif quand k > 1 : la famille D de cl7 et de cl8 fabrique donc « inverse ». Pour fabriquer « positif », il faut k < 1 (jeu b plus faible). Et pour ramener q près de 1, il faut alors une composante propre au jeu b, puisque q = k × pureté_a / pureté_b (CLR-02) : une composante dans b abaisse la pureté de b et relève q.
  - Le « miroir » de cl8 (`ZD_ca4_k1.4_pos`) garde k = 1,4 et la composante dans le jeu a, et n'échange que les signatures. Le terme α(1/k − 1) s'ajoute alors à l'écart au lieu de le compenser, et « λ change » sonne (4 sur 4). Ce n'est pas le miroir en signe. Le texte cite pourtant ce banc comme le miroir, ce qui laisse croire « positif » protégé par la réserve.
  - « Positif » est le signe de la prédiction indicative de l'auteur (Δλ > 0, probabilité subjective 0,25 pour « positif »). R3 (aucun run visant un signe positif) et R4 (symétrie) demandent que le texte ne le présente pas comme mieux gardé que l'autre signe.
- **Preuve** (`scripts/banc_cl9_miroir.py`, `sorties/banc-cl9-miroir.jsonl`, `resume-banc-cl9-miroir.txt`) :
  - Réglage : générateur de cl8 recopié (empreinte `20835d6e…` identique à la trace versée ; sans composante, il rend la simulation scellée à l'octet, contrôle de cl8) ; analyse v8 du commit (empreinte `9bfc1aef…`, relue dans chaque sortie) ; dimension 256, tau 0,15, 300 tirages ; H_0, fuite égale 0,7 et 0,7 ; contexte du jeu b × 0,6 ; composante de norme 3,2 dans le jeu b (celle du contexte valant 4 ; norme choisie par la formule pour ramener q à 1) ; signature du jeu b +0,32 au 8B, du jeu a −0,8 au 70B.
  - **12 analyses** : « positif » 3, **tous sans aucune réserve** (graines 192004, 192006, 192020) ; « positif non confirmé » 5 ; « indécis » 4. Rapport des Ec de 0,954 à 1,087 ; e(m) de −0,07 à 0,09 ; spécificité positive dans les deux sens.
  - **À 2 000 tirages** (`sorties/banc-cl9-miroir-n2000-192020.jsonl`), la graine 192020 garde « positif », **aucune réserve**. Les mesures :

    | grandeur | a→b | b→a |
    |---|---|---|
    | λ (8B ; 70B), intervalles | [1,041 ; 1,420] ; [0,425 ; 0,822] | [1,027 ; 1,366] ; [0,397 ; 0,647] |
    | intervalle de Δλ | [0,371 ; 0,860] | [0,442 ; 0,890] |
    | intervalle de la spécificité | [0,231 ; 0,933] | [0,198 ; 0,844] |
    | certification (borne basse, 8B / 70B) | 0,803 / 0,854 | 0,794 / 0,874 |

    Cohérence tenue : e(8B) = 0,024 [−0,178 ; 0,219] et e(70B) = 0,089 [−0,121 ; 0,307]. Rapport des Ec : q = 0,985 [0,852 ; 1,145] et 1,000 [0,862 ; 1,149].
  - Les graines 192004 et 192006 deviennent « positif non confirmé » à 2 000 tirages, toujours sans réserve : la borne basse d'un Δλ tombe à 0,249 et 0,196.
  - Témoins : sans la composante, q vaut 0,65 à 0,76 (la réserve sonnerait ; aucune issue prononcée sur 3). Avec la composante seule, sans signature, q vaut 0,93 à 1,04 et la cohérence est rompue (e de 0,36 à 0,60 ; aucune issue prononcée sur 3). L'artefact demande donc les deux ingrédients, comme la famille D de cl8.
  - La trace lexicale du texte compte d'ailleurs une asymétrie dans le jeu b (« on » 0 contre 5), comme dans le jeu a (« how » 4 contre 0).
- **Correction** (texte seul) :
  - l. 8, 288 et 425 : écrire que la classe voisine fabrique sans aucune réserve **« positif » comme « inverse »**, selon que le jeu b est plus faible ou plus fort, avec la composante dans le jeu au contexte le plus fort ; chiffrer ce banc (3 « positif » sur 12, tous sans réserve ; 1 tenu à 2 000 tirages, graine 192020) ; remplacer « Le miroir (« positif ») rend 4 « positif », tous avec « λ change » » par ce qui précède, ou dire que ce banc de cl8 ne joue pas le miroir en signe ;
  - l. 425 : « sous un écart de force de contexte de 25 à 40 % » devient « sous un contexte du jeu b plus fort de 25 à 40 % ou plus faible de 40 % » ;
  - verser ce banc comme trace (scripts et sorties de mon bac à sable, empreintes en annexe).

### CLR-02 — À CORRIGER — « Pureté » en deux sens contraires : à |s_a| = |s_b|, les puretés ne sont pas égales, et c'est ce qui tire q vers 1

- **Localisation** : l. 150 (« Il n'estime k que si les deux directions apprises sont également pures ») contre l. 154 (« à puretés égales (|s_a| = |s_b| = |s|), q = √((k² + r)/(1 + r)) […] : q est tiré vers 1 ») ; aussi l. 195 (« à puretés égales (générateur de la simulation) »), l. 198 (« Même à puretés égales, la bande ne sonne que si… »), l. 284 et 292 (« deux jeux de même pureté », sous des contextes inégaux), l. 429 (« à puretés égales »), l. 542 (« le rapport des Ec montre k à puretés égales »).
- **Constat** :
  - Appelons pureté d'une direction apprise son cosinus avec le contexte commun u : pureté_a = |u|/|u + s_a| et pureté_b = k|u|/|k·u + s_b|. Alors, dans le modèle linéaire, **q = k × pureté_a / pureté_b**, exactement (`sorties/formule-q.txt` : écart maximal 1,1·10⁻¹⁵ sur 1 000 tirages au hasard).
  - q vaut donc k si et seulement si les deux puretés sont égales, au sens du cosinus : la l. 150 est juste dans ce sens.
  - Mais à |s_a| = |s_b| (même hétérogénéité des cadrages, le cas du générateur de la simulation), les puretés diffèrent dès que k ≠ 1. Le jeu au contexte le plus fort est le plus pur. À r = 0,12 : 0,945 contre 0,968 sous k = 1,333 ; 0,945 contre 0,866 sous k = 0,6. C'est exactement ce qui tire q vers 1.
  - Le texte appelle pourtant ce cas « puretés égales » (l. 154), et y voit q tiré vers 1, ce qui contredit la l. 150 deux lignes plus haut. Les phrases des l. 284, 292 et 429 (« deux jeux de même pureté » sous des contextes inégaux) sont fausses au sens de la l. 150.
  - Le défaut vient de cl8 (CLS-01 : « où cette pureté est presque égale entre les jeux » ; annexe A, cas s_a = s_b), mais il porte sur ce que la consigne demande en premier : dire exactement ce que mesure q.
- **Correction** (texte seul) : définir la pureté (cosinus avec le contexte commun) ; écrire q = k × pureté_a / pureté_b ; remplacer « à puretés égales » par « à hétérogénéité égale des cadrages (|s_a| = |s_b|) » partout où c'est le générateur qui est visé (l. 154, 195, 198, 284, 292, 429) ; ajouter qu'à hétérogénéité égale, le jeu au contexte le plus fort est le plus pur, d'où le tirage vers 1 ; garder « q n'estime k qu'à puretés égales » (l. 150, 429, 542) au sens du cosinus.

### CLR-03 — À CORRIGER — Le seuil de k selon r n'est écrit que pour un jeu b plus fort ; la bande voit moins bien un jeu b plus faible

- **Localisation** : l. 198 (« Même à puretés égales, la bande ne sonne que si k dépasse √(1,3225 + 0,3225·r) : 1,17 à r = 0,12, 1,26 à r = 0,85, 1,40 à r = 2 »).
- **Constat** :
  - À |s_a| = |s_b| et sans bruit, la bande sonne aussi quand q < 1/1,15. Cela arrive si k < √(0,7561 − 0,2439·r) : 0,853 à r = 0,12, 0,741 à r = 0,85, 0,518 à r = 2, et jamais au-delà de r ≈ 3,1 (`sorties/formule-q.txt`).
  - La phrase « ne sonne que si k dépasse… » est donc fausse pour k < 1 : sous k = 0,6, à r = 0,12, q = 0,655 et la bande sonne.
  - Surtout, la bande n'est pas symétrique en k. En facteur de contexte, il faut ×1,17 contre ×1/0,853 = 1,17 à r = 0,12, mais ×1,26 contre ×1,35 à r = 0,85, et ×1,40 contre ×1,93 à r = 2. Un jeu b plus faible passe donc plus facilement sous silence qu'un jeu b plus fort. Or les cas « contexte du jeu b × 0,6, × 0,75, × 0,8 » sont précisément ceux du prix de la cohérence.
- **Correction** (texte seul) : écrire les deux seuils, avec leurs valeurs, et dire l'asymétrie ; la phrase « jusqu'où vaut la bande » doit couvrir les deux côtés.

### CLR-04 — À CORRIGER — La phrase « n'écarte pas cette part de H_0 » ne suit que la réserve « λ change » ; des issues fausses signalées par la seule réserve « contexte inégal » la perdent

- **Localisation** : l. 99 (H_0 : « Une issue « positif » ou « inverse » prononcée avec la réserve « le λ du modèle M change… » n'écarte pas cette part de H_0 ») ; l. 364–365 (réserves) ; l. 386–388 (phrases obligatoires) ; à rapprocher des l. 300 (« la graine 41306 […] n'a que celle-ci ») et 423 (« Toute issue prononcée qui porte l'une de ces deux réserves se lit sous cette limite »).
- **Constat** :
  - La phrase obligatoire n'est attachée qu'à « λ change ». Or la famille D (fuite égale, contextes inégaux, signatures croisées) fabrique des issues fausses que **seule** la réserve « contexte inégal » signale :
    - **simulation scellée**, graine 3870 (« H0 (0,7 et 0,7), contexte du jeu b × 0,75, jeu b +1,0 au petit, jeu a −1,0 au grand, d 256 ») : « positif », deux réserves « contexte inégal » (q 0,791 et 0,771), aucune « λ change » (e(m) −0,095 [−0,26 ; 0,07] et −0,182 [−0,372 ; 0,011]) ;
    - banc de cl7, graine 41306 : « inverse », seulement « contexte inégal », tenu à 2 000 tirages (rejeu versé).
  - Selon les phrases du v9-2, ces deux issues seraient dites avec la phrase de « positif » ou d'« inverse », suivie du texte du code. Aucune phrase ne dirait qu'elles n'écartent pas la part de H_0 que la réserve signale, alors que la même issue, si e(m) sortait un peu plus de zéro, la porterait. C'est une asymétrie entre les deux réserves, que la consigne demande d'examiner (« ce qu'une issue réservée écarte ou n'écarte pas »).
  - De même, une issue sans aucune réserve n'est suivie d'aucune phrase, alors que le texte la dit sous la même limite (l. 426). Par contraste, la phrase obligatoire la fait paraître établie.
- **Correction** (texte seul) :
  - attacher la phrase obligatoire de « positif » et d'« inverse » à **l'une ou l'autre** des deux réserves (pour « contexte inégal », par exemple : « Cette issue n'écarte pas qu'elle tienne à des jeux de force, ou de composition, inégale sous une fuite égale, avec des signatures d'un seul jeu (part de H_0) ; elle ne la sépare pas de H_A. ») ;
  - accorder H_0 (l. 99) ;
  - ajouter, pour toute issue « positif », « inverse » ou « nul » prononcée, avec ou sans réserve, une phrase de renvoi obligatoire aux limites (doubles signatures ; classe voisine de cl6, y compris sous une composante propre à un jeu).

### CLR-05 — À CORRIGER — « Ce tableau montre […] l'absence de faux positif sans réserve dans ces cas » : le tableau la dément

- **Localisation** : l. 305 ; comparer avec les l. 220, 228 (tableau) et 285 (R3).
- **Constat** :
  - La phrase vient du brouillon v4, où elle se lisait « l'absence de faux positif dans ces cas ». Le v9 a ajouté « sans réserve ». Le v9-2 ajoute « Les bancs de la contre-lecture n° 8 montrent, hors de ces cas, des faux « positif » et « inverse » sans aucune réserve », ce qui fait lire la première phrase comme générale à tout le tableau.
  - Le tableau contient pourtant, sous α = 0 (H_0) :
    - « signatures des deux jeux au 8B (+2 et +2) » : « positif 3 (2) », soit un « positif » sans aucune réserve ;
    - « signatures des deux jeux au 70B (+2 et +2) » : « inverse 4 », sans réserve.
  - La l. 285 le dit elle-même (« « positif » 3, dont 2 avec la réserve « fuite non spécifique » ; « inverse » 4, sans réserve »).
- **Correction** : « l'absence de faux « positif » ou « inverse » sans réserve dans ces cas, doubles signatures mises à part (limite écrite plus bas) », ou retirer la proposition.

### CLR-06 — REMARQUE — Heure de l'auteur fausse

- l. 3 : « le 27 octobre 2026, vers 12:45 UTC (`date -u`) ». Le fichier a été écrit à 12:26:50 UTC et son compagnon à 12:27:41 UTC. Ma lecture a commencé à 12:28:33 UTC, et 12:45 était encore à venir. Corriger l'heure (R6 : un fait daté doit pouvoir se relire).

### CLR-07 — REMARQUE — Poussée de la branche d'outils affirmée sans trace

- l. 25 et 555 : « `git ls-remote origin refs/heads/outils/echelle-conscience-eval-v8` rend ce commit (27 octobre, 12:21 UTC) ». Aucune trace n'est citée. Je ne peux pas le vérifier sans réseau : le dépôt local n'a pas de référence distante pour cette branche, mais sa règle de récupération ne suit que `main`, ce qui rend cette absence muette.
- Sans risque de dépense : le lanceur refait `ls-remote` et refuse sans création si la tête diffère (l. 64–65). Verser la ligne de sortie de `ls-remote`, horodatée, comme trace.

### CLR-08 — REMARQUE — Le code dit encore « il estime k » ; ce que le lecteur doit écrire

- `analyser_echelle_v8.py`, l. 39–40 (« il estime k ») et l. 761 (commentaire « estime k »). Cela contredit la l. 150 du texte. C'est sans effet sur la sortie : la docstring dit que le texte scellé fait foi en cas de désaccord (l. 2–3). Inutile de committer.
- Quand q n'est pas défini, le texte de la réserve devient « Ec_a→b / Ec_b→a = non défini (un Ec ≤ 0), hors de [1/1,15 ; 1,15] ». C'est maladroit, mais la règle est juste.
- Pour que la lecture du texte voyage avec l'issue, il faudrait écrire dans « Phrases permises » que le lecteur cite cette réserve sous sa lecture : « rapport des Ec hors bande (force du contexte, ou composition, inégale des deux jeux) », et non comme un constat de « jeux de force de contexte inégale ».
- Hors du v9-2 (code inchangé) : `rapport_Ec_ic` divise sans garde (l. 765). Un Ec exactement nul dans un tirage lèverait une exception Python non rattrapée, donc un arrêt bruyant sans lecture et non un repli silencieux. C'est pratiquement inatteignable ; je le note sans demander de correction.

### CLR-09 — REMARQUE — Une trace versée de cl8 ne se rejoue pas depuis le dépôt

- `docs/notes/echelle-conscience-eval/v9/contre-lecture-cl8/scripts/confirmer_n2000.py` (`d00467a2…`, cité au tableau « Traces ») importe `banc_cl8_commun.py` depuis le bac à sable de cl8 (`…/scratchpad/contre-lecture-echelle-v9/scripts/`), et non depuis sa copie versée. Le rejeu demande donc de corriger ce chemin. La sortie versée (`banc-cl8-Z-n2000.jsonl`) reste conforme ; je l'ai recomptée.
- Le dire dans le texte, ou verser une copie corrigée sous un nom nouveau (R12).

### CLR-10 — REMARQUE — Deux précisions de lecture des bancs

- l. 425 : l'exemple « sous × 1,25 et une composante de norme 3, la réserve « contexte inégal » se tait sur les 4 « nul » prononcés » suit « ni la cohérence ni les deux réserves ne voient l'artefact ». Or ces 4 « nul » sont des lectures **justes** (H_0, fuite égale), et ils portent « λ change ». Ils illustrent le silence de q, pas un artefact non vu. Le dire.
- « Sans aucune réserve », dans les bancs et dans la simulation, veut dire sans réserve parmi les trois qui peuvent y sonner. Les activations synthétiques n'ont que deux couches, et la réserve « profondeur » exige quatre profondeurs appariées (`quatre = len(couples) == 4`, l. 779). Elle y est donc muette par construction. Le dire une fois, là où le texte chiffre les lectures « sans aucune réserve ». Sur le run réel, à quatre profondeurs, elle pourrait sonner ou non : rien ne le dit.

## Annexe — pièces de cl9

Dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lecture-echelle-v9-2/` :

| fichier | sha256 |
|---|---|
| `scripts/banc_cl9_miroir.py` | `046be84b8f9c86c6c3de649c9ce8c70e8db93537db3fe74d9c15180f6803f185` |
| `scripts/banc_cl8_commun_copie.py` (copie de la trace de cl8) | `20835d6e967eca8b84ff77e049e8642aea09e686cb92f50cf21014e1691022da` |
| `scripts/confirmer_cl9_n2000.py` | `860ed815d5d373174fdb107f7690140cb227312b0f8b08b46f1d3312dc67d2a1` |
| `scripts/resumer_banc_cl9.py` | `ecf1f4c3abd8203f4af21e526e39d665d83786b9cc38edd071b0a93dcddd0bbb` |
| `scripts/formule_q.py` | `206e3d0d91cb327a2da7cb84583d18b27699f3d8dea497fd27eb0aacd228654a` |
| `scripts/recompter_bancs_cl8.py` | `c4854639b03bec287b10002356b2cda1107b9d76f4d32c3699dc35543cfbcdf6` |
| `scripts/verif_simulation.py` | `67c5f8ec8801e9e427ded4bed20a7aaf865297773bea2839515bd5506f458b10` |
| `scripts/verif_empreintes.py` | `5aeccc6f1bc8f0dc347b1e7007aea62a539742ba24a7a6f21480ecf3e624d59f` |
| `scripts/verif_abregees.py` | `c9d773ccee5bd650bb3761e493dc7dd0c3e6620bc7ef34c97e265ad08b26daac` |
| `scripts/diff_phrases.py` | `6fb5b286a8e88d015491548ad7ba3946b0ce01f32269bac63cf26e44a19b5bf2` |
| `sorties/banc-cl9-miroir.jsonl` (18 analyses, 300 tirages ; 12:40:34 → 12:42:09 UTC) | `986a66ca8690ddd9f43377e7be7b581f1adad9ebd80c4554a6ce669f142fbba3` |
| `sorties/resume-banc-cl9-miroir.txt` | `752a3431f9a32a9ccd4eafdda981bacd2051db14341afa89348107163b7f7a16` |
| `sorties/banc-cl9-miroir-n2000.jsonl` (graine 192004, 2 000 tirages ; deux lignes, la dernière est celle du banc) | `45e3e8e0ce180e319b8a20da62dbc97241b8d36f0b8c3330000f0d1dc184ab31` |
| `sorties/banc-cl9-miroir-n2000-192020.jsonl` | `b4af3a1f838908cc517e3421719ff3688b2ebe10cf60c2e8f09ff10c52a11745` |
| `sorties/banc-cl9-miroir-n2000-192006.jsonl` | `2390eb7f74147c60bfda1f22fc892e79f0778fe22e63cf9e6441ba6321dd6c36` |
| `sorties/resume-banc-cl9-miroir-n2000.txt`, `…-n2000-suite.txt` | `ff18ef8fc78cf21a…`, `8b6283ea1d56a806…` |
| `sorties/formule-q.txt` | `f6ac2c8555f7755c97f2281416fe197668c96bf3ab53a90338b97d13d1b31f2a` |
| `sorties/recompter-bancs-cl8.txt` | `3dabe2426ba4c73c16d9d441dbecd7c5685b73667df9622217a013b3a7556ba2` |
| `sorties/verif-simulation.txt` | `b435f78030902173956767a44b575b86817a17ba78c9f796ff85e991de748df3` |
| `sorties/verif-empreintes-tableaux.txt` (89 sur 89) | `25471b7476e381985a1fdd58c8f0b60c3a6d9558008772c1778affe0708ef325` |
| `sorties/verif-abregees.txt` (29 sur 29) | `447ff095c309b2b6daef9f4c611983bb9844c379816ac23318a53bd01ebd7be1` |
| `sorties/tests-cl9.txt` (401 passed in 500,29 s) et ses heures | `9e873b34abc95e2756991903e5a480e27f730b6320423bc06f62c5d5e6c07d85`, `27a9a7c3665f7de8…` |
| `sorties/diff-v9-v9-2.txt` | `4fdf32f3e7aee0f2dd06cde3de37d3d5bd79ec0e85269aa2edc2e1804c47d1f0` |
