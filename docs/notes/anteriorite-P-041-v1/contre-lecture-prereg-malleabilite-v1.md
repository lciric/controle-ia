# Contre-lecture du préenregistrement P-041, estimation de la malléabilité (v1)

31 octobre 2026, 10:09 UTC. Contre-lecteur neuf (Opus 4.6, session-depot post-compaction), qui n'a pas écrit le brouillon (R2). Aucune dépense, aucun commit, aucun appel payant.

- **Brouillon relu** : `prereg/P-041-malleabilite-v1.md`, empreinte `063a9bdc6a2b7c2c3a2c3e3989ec93a7bb7401f8120688466131d83bceb4c0f4`
- **Documents croisés** :
  - `docs/decisions/proposition-P-041-organisme-coevolutif-attaque-defense-v3.md` (`72aec5322c61490d…`) — voie 2 : malléabilité comme paramètre borné
  - `docs/notes/anteriorite-P-041-v1/verification-bailey-2412.09565-v1.md` (`31eb1dde…`) — vérification du protocole Bailey sur PDF
  - `docs/decisions/decision-N-053-v1.md` — invariant N-053
  - `registres/decisions.md` : R-880, R-888 à R-891
  - `prereg/gabarit-preregistrement-v1.md` — gabarit des sections obligatoires

## Verdict

**9 points à traiter, dont 5 à corriger avant scellement et 4 à préciser.** Aucune erreur factuelle sur Bailey ; le rattachement au programme (voie 2, R-880) est correct. Les problèmes portent sur la confusion entre borne inférieure et finitude, l'absence de contrôle négatif, et le cadrage de la portée du résultat.

---

## Points à corriger (avant scellement)

### CL-M1. Confusion entre borne inférieure et preuve de finitude (lignes 17-19, 29, 92-96)

L'hypothèse H-ML1 affirme une « abondance finie et bornée ». L'estimateur est explicitement une borne inférieure (ligne 36 : « L'estimateur est une **borne inférieure** »). Mais une borne inférieure ne peut pas démontrer la finitude : trouver 50 directions ne prouve pas qu'il n'y en a pas 50 000. La prédiction P-ML1 (« la malléabilité estimée est finie ») n'est pas falsifiable par une borne inférieure seule.

Le critère de lecture « M_couche ≥ 10 sur au moins une couche » (ligne 92) ne prouve pas la finitude, il prouve la non-trivialité. Seul le critère « la borne inférieure croît linéairement avec le budget sans saturation visible » (ligne 95) touche à la finitude, et il la contredit.

Le brouillon confond deux estimands :
- (a) une borne inférieure sur M (combien de directions l'optimiseur trouve à un budget donné) ;
- (b) la finitude de M (la saturation de la courbe M en fonction du budget).

**Recommandation** : séparer les deux prédictions. P-ML1a : l'optimiseur trouve au moins N_min directions (borne inférieure non triviale ; N_min à fixer, illustratif 10). P-ML1b : la courbe M(budget) sature (preuve de finitude). Les deux ont des critères de lecture distincts. La finitude doit porter sur la forme de la courbe (plateau, pente qui décroît vers zéro), pas sur un seuil ponctuel.

### CL-M2. Absence de contrôle négatif (tout le plan d'analyse)

Le brouillon ne prévoit aucun bras de contrôle. Sans contrôle, on ne peut pas interpréter la valeur de M : un M élevé pourrait être un artefact (optimiseur trop puissant, moniteur trop faible, seuil de camouflage trop généreux) plutôt qu'une propriété du modèle.

R5 exige : « Toute garde d'arrêt testée sur un cas sain et sur un artefact ; aucun repli silencieux. » Le protocole n'a ni cas sain ni artefact.

Deux contrôles s'imposent :
- **Moniteur trivial** (score aléatoire ou constant) : M doit être très grand (toute direction camouffle un détecteur qui ne détecte rien). Si le moniteur de base donne un M comparable, le protocole ne mesure rien.
- **Artefact d'une seule direction** : un espace de dimension 1 planté (une seule direction de camouflage connue analytiquement). L'optimiseur doit trouver exactement 1 direction. S'il en trouve 0 ou beaucoup plus, le comptage est défectueux.

**Recommandation** : ajouter ces deux contrôles. Le contrôle trivial est un garde-fou (M_trivial ≫ M_base, sinon arrêt). L'artefact est une validation de l'estimateur.

### CL-M3. Dépendance au moniteur non qualifiée (lignes 54, 82-86)

La malléabilité mesurée est une propriété conjointe (modèle, moniteur), pas du modèle seul. Une sonde linéaire, par construction, ne peut détecter que des déplacements dans le sous-espace engendré par les hyperplans séparateurs ; un moniteur non linéaire (réseau profond, ensemble) pourrait bloquer des directions que la sonde linéaire laisse passer. Le brouillon ne qualifie pas cette dépendance.

Conséquence pour la voie 2 : si M est élevé uniquement parce que le moniteur est faible, la borne versée comme paramètre de la classe déclarée est un surestimateur. L'arène prendrait en compte une diversité d'attaques qui n'existent que contre un moniteur linéaire.

**Recommandation** : écrire dans les hypothèses de travail que la malléabilité mesurée est conditionnelle au type de moniteur. Ajouter : « Un résultat sur une sonde linéaire constitue une borne supérieure de la malléabilité vis-à-vis de moniteurs plus puissants (toute direction qui camouffle un moniteur puissant camouffle aussi un moniteur plus faible). » Et dans les limites : « Le résultat ne se transfère pas directement aux moniteurs non linéaires. »

### CL-M4. Seuil de camouflage (rappel < 50 %) non justifié et trop généreux (ligne 34)

Chez Bailey, le rappel de la défense tombe à 0 % après réentraînement de l'attaque (figure 8a, p. 12) — c'est un échec total de détection. Ici, « rappel < 50 % » signifie que la moitié des entrées adverses sont encore détectées. Ce seuil gonfle M : une direction qui fait passer le rappel de 80 % à 49 % est comptée, alors qu'elle laisse la défense fonctionnelle.

Le choix du seuil change radicalement M. Si le seuil était « rappel < 5 % » (plus proche du phénomène observé par Bailey), M serait beaucoup plus petit. Le critère de lecture « M_couche ≥ 10 » et « M_couche < 10 » dépendent donc d'un choix arbitraire non discuté.

**Recommandation** : (a) justifier le seuil de 50 % par un argument de sûreté ou de comparaison avec Bailey ; (b) rapporter M pour plusieurs seuils (50 %, 20 %, 5 %) comme analyse de sensibilité gelée ; (c) noter que le critère « M < 10 sur toutes les couches » est conditionnel au seuil.

### CL-M5. Lien avec la voie 2 sous-spécifié (lignes 85-86)

Le brouillon dit : « Si M est grand, la classe doit être large ; si M est petit, la classe actuelle couvre peut-être déjà le phénomène. » Mais il ne dit pas *comment* M est traduit en paramètres de la classe déclarée. L'arène a besoin d'une borne numérique sur la dimension de l'espace de camouflage. Comment passe-t-on de M_couche à cette borne ? Quelle est la règle mécanique ?

**Recommandation** : ajouter dans la section « Lien avec la voie 2 » une spécification mécanique. Au minimum : M_max = max_l M_l ; la borne est versée au générateur de l'arène comme paramètre d_camouflage ; si M_max > M_plafond (à fixer, nœud de décision), la classe actuelle est déclarée insuffisante. Autrement, laisser le lien comme « information versée, non contraignante pour l'arène en cours » et le dire explicitement.

---

## Points à préciser (recommandés mais non bloquants)

### CL-M6. Bootstrap sur 5 initialisations (ligne 37)

Cinq graines pour un bootstrap est un nombre très faible : l'intervalle sera large et instable. Ce n'est pas bloquant si l'intervalle est rapporté tel quel (ce qui est prévu), mais le choix devrait être justifié (coût de chaque initialisation complète).

**Recommandation** : justifier au scellement, ou augmenter si le budget le permet.

### CL-M7. StrongREJECT non fixé (ligne 65)

Comme dans l'examen final (CL-5 de la contre-lecture de l'examen final v1), le juge de nuisance « StrongREJECT ou équivalent » doit être fixé avant scellement : nom, version, commit du dépôt public, empreinte.

### CL-M8. Budget d'époques par direction (20) non justifié (ligne 73)

Chez Bailey, l'optimiseur tourne pendant plus de 70 époques (p. 11). Ici, chaque direction reçoit 20 époques. Si la convergence est lente, 20 époques sous-estiment M (l'optimiseur abandonne des directions qu'il aurait trouvées avec plus de temps). Le brouillon reconnaît que c'est illustratif, mais ne propose pas de méthode de calibration.

**Recommandation** : prévoir un essai pilote (sur les 2-3 premières directions de la première couche) pour calibrer le nombre d'époques nécessaire à la convergence. Rapporter la courbe de convergence.

### CL-M9. R-891 (assemblage) non intégré (absent du brouillon)

R-891 dit que le pire cas certifié est revendiqué comme assemblage, pas comme méthode neuve. Le brouillon ne mentionne pas que la borne M est un ingrédient de cet assemblage. Ce n'est pas bloquant (la malléabilité est un préenregistrement séparé), mais le rattachement au programme serait plus clair avec une mention.

---

## Points conformes (vérifiés)

| # | Point vérifié | Source | Statut |
|---|---|---|---|
| 1 | Hypothèse rattachée au programme (P-041 voie 2, R-880) | registres/decisions.md R-880 | conforme |
| 2 | Invariant N-053 respecté (exécutant isolé, ligne 82) | docs/decisions/decision-N-053-v1.md | conforme |
| 3 | R3 respecté (pas de run visant un signe positif) | R3 | conforme |
| 4 | R9 respecté (SeedSequence, dérivées par couche et par direction, manifeste) | R9, ligne 78 | conforme |
| 5 | R-888, R-889, R-890 cités dans les documents qui font foi | registres/decisions.md | conforme |
| 6 | Gabarit complet (toutes les sections du gabarit sont présentes) | prereg/gabarit-preregistrement-v1.md | conforme |
| 7 | Section « Contre-lecture » contient « À REMPLIR » | attendu pour un brouillon | conforme |
| 8 | Cohérence avec Bailey p. 13 (« can't rule out convergence ») | vérification Bailey | conforme |
| 9 | Directions orthogonales : seuil ε = 0,05 raisonnable (dim ≈ 4096, produit scalaire attendu ≈ 0,016) | calcul | conforme |
| 10 | Arrêt mécanique à 1 000 directions (borne de calcul) | ligne 74 | conforme |
| 11 | Comptage itératif : méthode standard pour estimer la dimension d'un sous-espace | littérature | conforme |

---

## Résumé

| Catégorie | Nombre |
|---|---|
| À corriger (avant scellement) | 5 (CL-M1 à CL-M5) |
| À préciser (recommandés) | 4 (CL-M6 à CL-M9) |
| Conformes | 11 |

Le point le plus grave est CL-M2 (absence de contrôle négatif) : sans bras de contrôle, on ne peut pas interpréter M. Le R5 l'exige. CL-M1 (confusion borne inférieure et finitude) est le second par gravité : l'hypothèse et les critères de lecture doivent être cohérents avec l'estimateur.
