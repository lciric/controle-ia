# Contre-lecture du script de puissance de la garde δ — v5

Contre-lecteur neuf (règle R2). Je n'ai écrit ni le script, ni le rapport, ni les contre-lectures précédentes.
29 octobre 2026, de 08:01 à 08:27 UTC (`date -u`). Processeur seul. Aucun réseau, aucune clé, aucune dépense.
Rien n'a été écrit dans `source/`, `source-v4/` ni dans l'arbre du pôle. Aucun dépôt git créé.

## Verdict

**Utilisable au préenregistrement, après corrections du rapport (mineures).** Le script est juste. Le rapport reste exact
sur ses chiffres. Mais sa conclusion « δ = 0,05 passe à 160 unités si K_h = 10 » ne vaut que dans le cas le plus doux.

- **La retenue e-BH simulée est celle du pôle.** Je l'ai vérifiée à l'identique, sur mes propres tirages : 30 000 familles
  (ex æquo, seuils exacts, pics non atteints), plus 72 lectures de bout en bout relues par `evaluer` et `Course`. Aucune
  différence. L'arrêt se fait au premier instant d'atteinte, comme dans `Course.ajouter_trajectoire`. Sans atteinte, on
  garde la valeur finale, jamais le maximum.
- **Les chiffres k = 8 se reproduisent.** À même graine, c'est identique champ pour champ : principale 5 829 champs,
  fiches nulles 883, rejeu v4 5 958 champs (contre la sortie de l'auteur). À graine neuve, les parts e-BH bougent d'au plus 0,03 et les lectures ne
  changent pas.
- **Les six constats v4 sont corrigés dans le script.** Il reste deux points mineurs : les doublons de valeurs sous un autre
  encodage (GD5-04) et le commit écrit au rapport (GD5-03).
- **La conclusion « 160 unités si K_h = 10 » est fragile (GD5-01, moyen).** Trois écarts plausibles la font tomber de
  0,99 à environ 0,65 à 0,83 (lecture A) :
  - une dispersion par unité **des comparateurs**, que la v5 ne simule pas ;
  - l'effet d'unité sur A, déjà simulé mais pas avec la lecture e-BH à k = 8 ;
  - un α_c partagé : avec le biais 0,0125, 0,76 tombe à 0,18.

  Avec 300 unités, la fiche reste ≥ 0,99 dans tous ces cas. Pour K_h = 3, « ≈ 400 » tient à peu près (0,76 à 0,83 dans
  les mêmes écarts), et il faut 650 unités pour atteindre ≥ 0,98.
- **Le contrôle d'erreur est crédible**, mais le rapport ne dit pas à quel α le comparer (GD5-02). La borne de l'e-BH est
  α_c·m₀/m : 0,025 en (A), 0,0056 en (B). Les proportions moyennes observées sont ≤ 0,0005. Le « 0 % » de (A) vient d'une
  fiche nulle facile, où les 8 contrastes sont nuls. Avec un seul comparateur nul, ce qui est le nul défavorable de
  l'intersection-union, j'obtiens jusqu'à 1,0 % de suites à nulle retenue. Cela reste sous la borne (proportion moyenne
  ≤ 0,0035).

Sources relues : `sha256sum -c` donne « OK » pour les 30 fichiers `.sha256` de `source/`. Script `7d1239e1…`, rapport
`8e31a1e3…`, pôle `pari_apparie.py` `ec6c2cf6…` (inchangé depuis la contre-lecture v4). J'ai fait des copies conformes dans
`cl/outils/copie_script/` et `cl/outils/copie_pole/`. Environnement : Python 3.13.17 (l'auteur avait 3.13.18), numpy 2.5.3.

## 1. GD4-01 à GD4-06 : corrigés ou non

| constat v4 | état en v5 | preuve |
|---|---|---|
| GD4-01 (moyen) « l'effet d'unité ne touche presque pas la garde » | **corrigé** | La lecture 3 est réécrite. L'échelle logit et le minimum des k gardes sont nommés. Le passage `--effet-unite-beta 0.17` existe. La garde seule est donnée à côté du minimum. J'ai vérifié chaque chiffre du § 3 dans les sorties (`verif_section3.py`) : garde seule 0,893 / 0,890 / 0,880 / **0,770** et 0,456 / 0,421 / 0,362 / **0,301** ; contraste 0,985 / 0,95 / 0,82 / 0,83 ; minimum 0,36 / 0,18 / 0,09 |
| GD4-02 (mineur) lien non séparé, E[f_A] non écrit | **corrigé** | `moments_tires` donne E[f_A], E[f_B], E[g], E[r_A], E[v], les écarts-types et la corrélation des p de A dans l'unité (0,75 et 0,88). La formule de `decomposition_effet_unite` est juste : Var f = p₀(1 − p₀)/K + Var p·(1 − 1/K) ; parts ajoutées 0,12, 0,45 et 0,61. `--lien-coupe` existe. L'écart coupé − tenu monte jusqu'à 0,064 (K = 10, τ = 0,10, k = 3), comme écrit |
| GD4-03 (mineur) souligné lu dans les CSV | **corrigé** | `lire_nombre` et `lire_entier` servent partout. Mes 27 essais de nombres refusent : pleine chasse, espace insécable, `Infinity`, `-nan`, hexadécimal, saut de ligne, 73 caractères, point-virgule, latin-1, chaîne, `true` et liste en JSON, `6.0` pour un entier, `,,`. Sont acceptés comme il faut : guillemets, BOM, CRLF, `.05`, `5e-2`, `+5`. Note : `1e-400` est lu 0 (sous-flux), sans conséquence |
| GD4-04 (mineur) doublons par le nom seulement | **corrigé, avec un reste** (GD5-04) | Refusés : lien dur (même empreinte), lien symbolique, `../`, `./`. Acceptés : les mêmes valeurs sous un autre encodage (JSON réindenté, CSV contre JSON, `0.100` contre `0.1`) ; la forme `ecarts` en contraste (déclaré) |
| GD4-05 (mineur) git, manifeste | **corrigé dans le script ; en partie au rapport** (GD5-03) | 11 cas à git simulé, plus git absent : tous conformes. « inconnu (motif) » à chaque échec, « hors dépôt git », « ?? », « non suivi », « commité, non modifié ». Le script écrit la sortie, le journal et le manifeste, et refuse d'écraser (sortie existante, ou journal seul d'un passage interrompu). Les empreintes des 7 manifestes de l'auteur sont justes, et chaque sortie porte le commit de son manifeste. Mais le rapport écrit un seul commit `7ff46b74…` pour les sept passages |
| GD4-06 (mineur) replis, erreurs brutes | **corrigé** | Refus nommés : `--ecarts " "`, `,g1.json`, dossier, identifiant « », identifiants doublés, ordre différent, identifiants sur un seul fichier, secours avec contraste réel, τ = 0, effet logit à τ + biais = 1. Les messages JSON gardent leur motif. 0 erreur brute sur 53 essais. Note : un identifiant « espace de largeur nulle » passe (négligeable) |

Rejeu v4 : `--repetitions 4000` à graine 20261029 contre la sortie v4 de l'auteur (`574d4c95…`) : 5 953 champs communs ; seules diffèrent la version et l'empreinte du script ; **0 écart numérique** sur les 216 cellules, les n₈₀ et les artefacts (`comparaison-rejeu-v4.json`). Contre le rejeu de l'auteur : 5 958 champs, 0 différence (`comparaison-rejeu-v5-auteur.json`). L'identité v4 = v5 annoncée est donc reproduite, pas seulement lue. Effet
σ = 0,5 et 1,0 (sorties de l'auteur v4 contre v5) : 809 champs communs. Seules diffèrent la version, l'empreinte et
`--comparateurs` (1,3 contre 1,3,8). Écart numérique nul.

## 2. La retenue e-BH simulée est-elle celle du pôle ? (démontré, `verif_ebh_pole.py`, `verif_ebh_chaine_puissante.py`)

**Oui, à l'identique.** Graines 77001 et 77002, différentes de celles de l'auteur.

- **Familles tirées par moi**, 30 000. f de 1 à 18 fiches, m de f à f + 4, α ∈ {0,01 ; 0,025 ; 0,05 ; 0,1},
  trajectoires de 1 à 39 instants. Le tirage force des ex æquo (valeurs quantifiées, copies exactes), des valeurs finales
  posées exactement au bord e-BH (score = −log r), des valeurs posées exactement au seuil d'arrêt puis redescendues, des
  pics sans atteinte au-dessus de la valeur finale (21 884 familles) et des fiches descendantes. `retenues_famille` de la
  v5 est comparé à `Course.entrer`, `ajouter_trajectoire` et `lire` du pôle ; les fiches non simulées sont déclarées
  « sans partie ». Résultat : **0 différence** de valeur arrêtée (à l'égalité exacte), d'atteinte et de retenue.
  Couverture : 144 017 atteintes, 200 150 retenues, dont 56 133 sans atteinte, et 6 297 familles à ex æquo au bord.
- **Chaîne entière**, 36 cellules (24 tirées au hasard et 12 puissantes) en (A) et (B), soit 72 lectures. k ∈ {1, 2, 3, 8},
  n ≠ n_garde, M de 1 à 3, N de 0 à 5 fiches nulles, σ logit ∈ {0 ; 1}. Je capture les tirages bruts de `cellule(…, ebh)`
  par une enveloppe autour de `tirer`. Je les relis avec `evaluer` (k gardes, k contrastes), puis avec `Course`. Résultat :
  **0 différence** sur les parts (première atteinte, retenue, fiches du sujet, toutes vraies, nulles retenues). L'écart
  entre `log_e_valeur` d'`evaluer` et la valeur de `Course` est nul : même seuil log(m/α_c). Les parts des cellules
  puissantes vont de 0,03 à 1, donc le test porte.
- **Arrêt** : quatre cas témoins.
  - Une trajectoire qui dépasse le seuil puis redescend est lue à l'instant d'atteinte (4,389, retenue).
  - Une trajectoire qui frôle le seuil (à 10⁻⁹ sous) puis redescend est lue à sa valeur finale (−1, non retenue), pas à
    son maximum.
  - Une valeur exactement égale au seuil arrête la trajectoire.
  - La v5 et le pôle donnent la même chose dans les quatre cas.

  **L'arrêt « au premier instant » est donc bien ce que fait `Course`. Ce n'est pas une lecture optimiste.** La lecture
  e-BH sur la valeur finale (non arrêtée) est elle aussi celle de `Course.lire`.
- Pourquoi `ebh_retenues` peut ignorer les m − f fiches non simulées (e = 1) : leur score log(α/m) est < −log k pour tout
  k ≤ m. Elles ne sont jamais retenues et ne changent pas k*. C'est confirmé par les familles où m > f.
- Hors de portée : la v5 simule **une** génération. La course réelle peut lire l'e-BH à chaque génération, avec une
  promotion acquise. Plusieurs lectures ne réduisent pas la puissance par rapport à une seule ; la simulation est donc
  plutôt prudente sur ce point. `engagement_apparie.jouer_generation`, qui passe la trajectoire à `Course`, n'a pas été
  relu (consigne).

## 3. Chiffres k = 8 : reproduction, graine neuve, contrôle d'erreur

**Même graine 20261029** (`lancer_repro.sh`, commandes des manifestes) :
- principale : **5 829 champs, 0 différence** (`comparaison-repro-principale.json`) ;
- fiches nulles : **883 champs, 0 différence** (`comparaison-repro-fiches-nulles.json`) ;
- rejeu v4 : voir § 1.

**Graine neuve 918273645** :
- parts e-BH : 1 152 champs, écart maximal 0,032. Il est atteint pour « toutes vraies » à K = 3, 300 unités : 0,51 contre
  0,48. À k = 8, pour « fiche du sujet » et « une fiche » : ≤ 0,023 ;
- parts de première atteinte : écart maximal 0,045 sur 1 157 champs (environ 2,8 erreurs types d'une différence) ;
- tableau du § 2 à graine neuve, A · B :
  - K = 10, δ = 0,05, biais 0 : 0,986 · 0,985 à 160 unités ; biais 0,0125 : 0,76 · 0,80 ;
  - K = 3, δ = 0,05, biais 0 : 0,15 / 0,68 / 0,90 / 1,00 (160 / 300 / 400 / 650) ;
  - fiches nulles : (A) 0, (B) ≤ 0,8 % ; proportion moyenne ≤ 0,0005.

  Les tailles minimales sont identiques : 111, 161, 128, 163, 75, 108, 86, 110. Je les ai aussi recalculées à la main.

**À quel α comparer le contrôle d'erreur.** La règle e-BH garantit FDR ≤ α_c·m₀/m, sous toute dépendance.
- (A), m = 4, m₀ = 2 : **0,025**. (B), m = 18, m₀ = 2 : **0,0056**. Pour un mode entier nul en (B) (m₀ = 8 sur 16) : 0,025.
- « Au moins une nulle retenue » n'est pas borné par l'e-BH en tant que tel. Une nulle n'est retenue que si e ≥ m/(α_c·k*)
  ≥ 1/α_c. Par fiche, la borne de Markov et de Ville donne donc au plus α_c·k*/m (≤ 0,047 en (B) quand k* = 17).

**Crédibilité (démontré, `verif_doutes.py`, plans `nulles` et `nulles2`, graine 918273645).**

| nul essayé (k = 8, δ = 0,05, 2 000 à 4 000 répétitions) | (A) au moins une / proportion moyenne / borne | (B) au moins une / proportion moyenne / borne |
|---|---|---|
| v5 : les 8 contrastes nuls, garde vraie | 0 / 0 / 0,025 | ≤ 0,0055 / 0,0003 / 0,0056 |
| garde à la frontière E[g] = δ, contrastes vrais | ≤ 0,0005 / 0,0002 / 0,025 | ≤ 0,0035 / 0,0002 / 0,0056 |
| un mode entier à la frontière (1 nulle en A, 8 liées en B) | 0 / 0 / 0,025 | ≤ 0,0055 / 0,0010 / 0,025 |
| **un seul comparateur nul sur 8** (nul défavorable de l'intersection-union) | **0,002 à 0,010** / ≤ 0,0035 / 0,025 | ≤ 0,0063 / 0,0004 / 0,0056 |

Les chiffres de l'auteur sont crédibles. Ils tiennent largement sous la borne, et je retrouve ses 0 et ≤ 0,8 % à même
graine et à graine neuve. Mais le « 0 % en (A) » tient à la forme de nulle choisie : avec 8 contrastes nuls, leur minimum
est très bas. Le nul qui compte pour une affirmation « bat chaque comparateur » est celui où un seul comparateur n'est pas
battu. Il donne jusqu'à 1 % de suites à nulle retenue en (A) (GD5-02). La valeur finale non arrêtée ne fait pas sortir de
la borne.

## 4. Les doutes déclarés : lesquels peuvent changer la conclusion ?

Conclusion examinée : « δ = 0,05 passe à 160 unités si K_h = 10 ; ≈ 400 si K_h = 3 » (k = 8, τ = 0,01, biais 0 ;
lecture A, fiche du mode 1 retenue ; B voisine).

| écart à l'hypothèse de la v5 | K = 10, 160 unités | K = 10, 220 / 300 | K = 3, 400 | K = 3, 650 | source |
|---|---|---|---|---|---|
| v5 (sujet partagé seul, corrélation entre comparateurs ≈ 0,51) | 0,99 | — / 1,00 | 0,89 à 0,90 | 1,00 | auteur ; ma base 0,987 et 0,896 |
| **corrélation positive entre comparateurs** : effet logit σ_B = 0,5 commun aux 8 B (corr. v 0,63) | 0,96 | | 0,88 | | plan `correlation` |
| idem, σ_B = 1 commun (corr. v 0,77) | **0,82** | 0,96 / 0,99 | **0,83** | 0,99 | `correlation`, `k10_tailles`, `k3_tailles` |
| même dispersion, **indépendante** par comparateur (σ_B = 1, corr. v 0,29) | **0,67** | 0,92 / 0,99 | 0,76 | 0,98 | idem |
| bêta ρ = 0,17 sur B, commun / indépendant | 0,82 / **0,64** | 0,93 / 0,996 (indép.) | 0,84 / 0,76 | 0,99 | idem |
| même effet logit 1 sur A et sur les B (« unité difficile pour tous ») | 1,00 | | 0,97 | | `correlation` |
| **effet d'unité sur A** (logit σ = 1, lien tenu / coupé), avec e-BH à k = 8 | **0,79** / 0,80 | 1,00 (400) | **0,81** | 0,99 | script, `--effet-unite-a 1.0 --lecture-ebh A,B` |
| bêta ρ = 0,17 sur A, avec e-BH à k = 8 | 0,83 | 1,00 (400) | 0,78 | 0,99 | script, `--effet-unite-beta 0.17` |
| **α_c = 0,025** (famille qui partage α) | 0,97 ; **biais 0,0125 : 0,18** (au lieu de 0,76) | 1,00 | 0,81 ; 0,83 (biais 0,0125) | 0,99 | script, `--alpha 0.025` |
| garde commune aux deux modes (mêmes unités honnêtes) | 0,99 | | 0,90 | | `nulles` |
| fiches nulles ajoutées (m = 4) | 0,97 | | 0,82 | | `nulles` |

Lecture, doute par doute :
1. **Corrélation des 8 comparateurs.** À dispersion fixée, une corrélation positive **aide** le minimum : 0,82 en commun
   contre 0,67 en indépendant, à K = 10 et 160 unités. Ce qui fait baisser la puissance, c'est la **dispersion par unité des
   comparateurs**. La v5 la tient à zéro (B binomiaux sans effet) et ne la déclare pas. C'est le doute qui peut changer la
   conclusion « 160 », de 0,99 à 0,64 à 0,82. Ce n'est pas un défaut de calcul : c'est une hypothèse de loi.
2. **Effet d'unité sur A à k = 8.** La v5 l'a simulé (fiche 0,59 → 0,32 à la première atteinte de 160), mais pas avec la
   retenue e-BH à k = 8. Avec elle : 0,99 → 0,79 (K = 10, 160 unités) et 0,89 → 0,81 (K = 3, 400 unités). La conclusion
   du § 2 est donc celle de σ = 0, et le rapport ne le rappelle pas à cet endroit.
3. **Une famille à α_c = 0,05.** Si α est partagé (α_c = 0,025), le seuil d'arrêt double. K = 10 à 160 unités tient sans
   biais (0,97), mais tombe à 0,18 avec le biais 0,0125 (au lieu de 0,76). K = 3 à 400 unités : 0,81. Ce doute peut changer
   la conclusion dès qu'un biais d'espérance existe.
4. **Modes indépendants et de même loi.** Mes deux essais ne bougent presque rien : garde commune aux modes, et un mode
   entier nul. Des modes de lois différentes ne sont pas essayés. Pour la fiche du mode 1, seul m compte.
5. **n₈₀ non calculés à k = 8.** Cela ne change pas la conclusion, car les tailles 160 / 300 / 400 / 650 encadrent.
6. **Un seul ensemble d'unités.** Aucun fichier réel, donc rien à vérifier ici (reste de GD3-02).

**Ce qui tient dans tous les essais : 300 unités à K_h = 10 (≥ 0,99) et 650 à K_h = 3 (≥ 0,98).** La phrase « 160 si
K_h = 10 » demande d'écrire ses hypothèses : aucune dispersion par unité des comparateurs ni de A, α_c entier, biais nul ou
faible. « ≈ 400 si K_h = 3 » donne 0,76 à 0,90 selon les écarts.

## 5. Le rapport dit-il ce que les sorties disent ? (démontré, `tableau_k8.py`, `verif_section3.py`)

**Les chiffres, oui.**
- Les 32 cases du tableau du § 2 sont dans `-sortie-principale.json` à l'arrondi près.
- On y trouve aussi : « toutes vraies » 0,04 / 0,03 ; 0,51 / 0,46 ; 0,81 / 0,79 ; 0,99 / 0,99 ; contrastes 0,18 / 0,67 /
  0,86 / 0,995 ; gardes ≥ 0,92 ; effet de k 0,88 / 0,76 / 0,59 et 0,94 / 0,84 / 0,70 ; tailles minimales ; la variante
  τ = 0,10 (12 nombres) ; les fiches nulles (0 ; ≤ 0,008 ; ≤ 0,0005 ; 0,89 → 0,81 ; 0,88 → 0,87).
- Lecture 4 : + 0,37 et ≤ + 0,05. Les artefacts : 0,8 × la borne de Ville ; tricheur 0.
- Tout le § 3 se retrouve aussi (voir la table du § 1).
- La « première atteinte de 40 » en (A) est bien la « fiche entière » de la cellule au seuil 40 : mêmes tirages, égalité
  vérifiée.

Inexactitudes, toutes mineures :
- en-tête et § 5 : « commit `7ff46b74…` » pour les sept passages. Quatre portent un autre commit : `0ac94e6b…` (bêta,
  fiches nulles), `87b3d40e…` (σ = 0,5), `43355d80…` (τ = 0,10). Le manifeste global n'écrit que `7ff46b74…` (GD5-03) ;
- lecture 3 : « écarts ≤ 0,04 ». Pour « toutes vraies », l'écart maximal (A) − (B) est 0,048 (K = 3, δ = 0,05, 300
  unités : 0,51 contre 0,46) ;
- § 4, lecture 1 : « la fiche passe à 300 unités dans les deux lectures » est exact, mais sans rappeler que c'est à σ = 0,
  avec B sans dispersion et α_c entier (GD5-01) ;
- § 5 : « corrélation réelle des 8 comparateurs inconnue ». Le doute qui compte est la dispersion des comparateurs, pas
  leur corrélation (GD5-01) ;
- § 2 : « au plus 0,8 % des suites en (B) » est exact, mais sans α de référence ni forme de nulle défavorable (GD5-02).

## Constats

### GD5-01 — moyen — La conclusion « 160 unités si K_h = 10 » n'est établie que sans dispersion par unité ; la dispersion des comparateurs n'est ni simulée ni déclarée

**Preuve (démontré, § 4).** k = 8, τ = 0,01, δ = 0,05, lecture A, 2 000 répétitions. La fiche du mode 1, retenue à 0,99
dans la v5, devient :
- 0,82 avec un effet logit σ_B = 1 commun aux 8 comparateurs ;
- 0,67 avec le même effet indépendant par comparateur ;
- 0,64 avec une bêta ρ = 0,17 indépendante ;
- 0,79 avec l'effet logit σ = 1 sur A (avec e-BH, que le rapport ne donne pas à k = 8) ;
- 0,18 au lieu de 0,76 avec α_c = 0,025 et le biais 0,0125.

À 300 unités, tous ces cas sont ≥ 0,99. À K = 3 et 400 unités : 0,76 à 0,84 au lieu de 0,89. La corrélation positive entre
comparateurs, elle, aide (0,82 contre 0,67).

**Correction.**
- Écrire la conclusion avec ses hypothèses : σ = 0 des deux côtés, B binomiaux, α_c = 0,05 entier.
- Ajouter une option « effet d'unité sur les comparateurs », commun ou indépendant, logit ou bêta, et la rapporter à k = 8
  avec la lecture e-BH, comme `--effet-unite-a`.
- Donner la lecture e-BH à k = 8 sous effet d'unité sur A, et sous α_c partagé.
- Au pilote : mesurer la surdispersion de f_B et r_B par comparateur, et leur corrélation entre comparateurs. Ce sont ces
  quantités qui décideront entre 160 et 300 unités.

### GD5-02 — mineur — Contrôle d'erreur : pas d'α de référence ; la fiche nulle de (A) est le nul le plus facile

**Preuve (démontré, § 3).**
- Le rapport donne 0 % (A) et ≤ 0,8 % (B) sans borne de comparaison. Les bornes sont FDR ≤ 0,025 (A) et ≤ 0,0056 (B).
- La fiche nulle de (A) a ses 8 contrastes nuls. Avec un seul contraste nul, ce qui est le nul défavorable de
  l'intersection-union : 0,2 à 1,0 % de suites à nulle retenue, et une proportion moyenne ≤ 0,0035, sous la borne 0,025.
- Garde à la frontière et mode entier nul : ≤ 0,55 %.

**Correction.** Écrire la borne α_c·m₀/m à côté de chaque part d'erreur. Ajouter les formes de nulle « un comparateur nul »
et « garde à la frontière E[g] = δ ». Dire que « au moins une nulle retenue » n'est pas la quantité garantie.

### GD5-03 — mineur — Le commit du rapport et du manifeste global n'est pas celui de quatre passages

**Preuve (démontré).** Les manifestes par passage, écrits par le script, sont justes : empreintes vérifiées, commit égal à
celui de la sortie. Mais le rapport et `manifeste-puissance-garde-delta-v5.json` (`commit_depot_au_lancement`) n'écrivent
que `7ff46b74…`. Les sorties bêta et fiches nulles portent `0ac94e6b…`, σ = 0,5 porte `87b3d40e…`, et τ = 0,10 porte
`43355d80…`. C'est le même type d'écart que GD4-05.

**Correction.** Mettre dans le manifeste global et dans le tableau du rapport le commit de chaque passage, lu dans son
manifeste.

### GD5-04 — mineur — GD4-04 : doublons repérés à l'octet près seulement ; forme `ecarts` admise en contraste

**Preuve (démontré, `verif_entrees.json`).** Sont acceptés comme deux comparateurs distincts :
- `g1.json` et le même JSON réindenté ;
- `g1.json` et `g1.csv` aux mêmes valeurs ;
- `0.1` et `0.100`.

Un fichier `{"ecarts": …}` est accepté en contraste (le reste est déclaré).

**Correction.** Comparer aussi les vecteurs lus (égalité des écarts, et des identifiants s'il y en a). Refuser ou écrire
« doublon de valeurs ». Exiger `rA,rB` en contraste, ou une clé de rôle.

### GD5-05 — mineur — Petites inexactitudes du rapport

**Preuve.** « écarts ≤ 0,04 » (lecture 3) : 0,048 pour « toutes vraies ». La conclusion du § 4 (lecture 1) ne rappelle
pas σ = 0. La réserve « corrélation des comparateurs » vise le mauvais paramètre (voir GD5-01).

**Correction.** Écrire 0,05. Rappeler les hypothèses près de chaque taille. Renommer la réserve « dispersion par unité des
comparateurs, et leur corrélation ».

## Non vérifié

- `engagement_apparie.jouer_generation`, ce qui passe réellement de `evaluer` à `Course` en production, n'a pas été relu
  (consigne). J'ai vérifié que les deux voies donnent la même valeur, pas que la production prend cette voie.
- `parametres-garde-delta-pour-G1-v1.md` (`db603750…`) n'a pas été lu. Je ne sais pas laquelle des lectures (A) ou (B)
  sera celle de G1, ni la valeur de M.
- La loi réelle : aucun fichier d'écarts réels n'est fourni.
- La lecture e-BH sur plusieurs générations n'a pas été simulée.
- Des modes de lois différentes, et des fiches nulles d'autres formes (garde et contraste nuls ensemble), n'ont pas été
  essayés.
- Les commits `7ff46b74…`, `0ac94e6b…`, `87b3d40e…` et `43355d80…` : il n'y a pas de dépôt ici. Les cas git ne sont
  démontrés qu'avec un git simulé.
- Python 3.13.18 : j'ai la 3.13.17. Les sorties sont identiques hors en-tête d'environnement.
- Les passages τ = 0,10, σ = 0,5, σ = 1,0 et bêta n'ont pas été relancés. J'ai lu leurs chiffres dans les sorties de
  l'auteur et comparé σ = 0,5 et 1,0 à la v4. Mes passages « effet A + e-BH » et « bêta + e-BH » à k = 8 sont neufs.
- Incident de mon côté : j'ai modifié `lancer_repro.sh` pendant que deux lots le lisaient. Bash a signalé une erreur de
  syntaxe **après** la fin des passages, et les lignes « code » de `nulles`, `neuve-nulles` et `rejeu` manquent dans `codes.txt`.
  Les journaux portent « fin : … sortie écrite », et les sorties existent et se comparent.

## Fichiers produits (sous `…/relecture-garde-delta-v5/cl/`)

| fichier | rôle |
|---|---|
| `outils/copie_script/sim_garde_v5.py`, `sim_garde_v4.py` | copies conformes (`7d1239e1…`, `5bf015b6…`) |
| `outils/copie_pole/pari_apparie.py` | copie conforme du pôle (`ec6c2cf6…`) |
| `outils/verif_ebh_pole.py` → `sorties/verif_ebh_pole.json` | Q2 : 30 000 familles, 48 lectures de bout en bout, arrêt |
| `outils/verif_ebh_chaine_puissante.py` → `sorties/verif_ebh_chaine_puissante.json` | Q2 : 24 lectures sur des cellules puissantes |
| `outils/lancer_repro.sh` → `sorties/repro/`, `sorties/neuve/`, `sorties/doutes-script/`, `sorties/codes.txt` | Q3, Q4 : même graine, graine neuve, effet A, bêta, α_c = 0,025 avec e-BH à k = 8 |
| `outils/comparer_sorties.py` → `sorties/comparaison-*.json` | Q1, Q3 : comparaisons champ à champ |
| `outils/tableau_k8.py` | Q3, Q5 : tableau du § 2 et lectures, depuis une sortie |
| `outils/verif_section3.py` | Q1, Q5 : chiffres du § 3 |
| `outils/verif_doutes.py` → `sorties/doutes-{correlation,k3_tailles,k10_tailles,nulles,nulles2}.json`, `.log` | Q3, Q4 : comparateurs dispersés et corrélés, nulles, garde commune |
| `outils/verif_entrees.py` → `sorties/verif_entrees.json`, `sorties/essais_entrees/` | Q1 : 53 essais d'entrées, git simulé, R12 |

Empreintes : `cl/EMPREINTES-contre-lecture-garde-delta-v5.txt`.
