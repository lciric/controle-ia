# Contre-lecture R2 — axe 6, texte II (« hypothèses fragiles des statistiques ») — v1

- Date : 29 octobre 2026, 22 h 34 UTC (`date -u` : Thu Oct 29 22:34:43 UTC 2026).
- Contre-lecteur : sous-agent Claude, modèle Opus 5.5 (identifiant `claude-opus-5-5`), lancé par session-depot. Neuf : n'a écrit aucune pièce de la course. Tenu à l'écart : n'a conçu ni lu aucun moniteur ni aucune statistique de surveillance du programme.
- Pièces lues : `docs/notes/ideation-organisme-v1/course-2/axe-6-texte-II-v1.md` (85 lignes) ; puis, sur instruction expresse du coordinateur en cours de travail, la v2 en quarantaine (voir la section « v2 »).
- Empreinte vérifiée : `sha256sum -c axe-6-texte-II-v1.md.sha256` → OK ; `1d5612ab6cd27d9e9a786d29b7316d0aa11146c0f4bcf172772c1a64fa43a6a0`.
- Rien d'autre n'a été lu : ni la question BA-001 citée ligne 4, ni aucun autre fichier d'une branche de données ou de quarantaine, ni aucun moniteur.
- Mesure du texte servi (lignes 9 à 75, entre les marqueurs) : 858 mots, 5 489 caractères.

## Verdict
**v1 : servable après corrections.** Aucun constat bloquant ; neuf constats majeurs (garde non opérationnelle et en tension avec le test (f), vocabulaire exposé au filtre, définition de « diffus » non formelle, double sens de « mesurable », agrégation interdite ambiguë, déplacements d'activations non réalisables, juge sans contrôle de (g) ni de « sans objet », critère de mort sans seuil, interface à classes libres) ; neuf mineurs. Verdict de la v2 : section « v2 » en fin de rapport.

## Constats

### CA6-01 — Garde sans critère opérationnel, et en tension littérale avec (c) et (f)
- Gravité : majeur.
- Lignes : 11, 34, 42.
- Défaut : la garde interdit « un procédé concret pour produire un déplacement » (l. 11), alors que (f) exige un protocole qui produit des déplacements synthétiques (l. 34). La phrase suivante de la ligne 11 lève l'ambiguïté pour le rédacteur, pas pour un filtre ni pour un proposeur prudent : lue au pied de la lettre, toute fiche complète tombe sous la garde. De plus, la ligne 11 dit « écartée avant le juge » sans dire par qui ni selon quel critère, et la ligne 42 ouvre une seconde voie d'exclusion (« non noté ») qui recoupe la première sans qu'on sache laquelle s'applique. La garde n'est pas répétée pour (f) ni pour les facultatifs (l. 38-40) ; elle vaut par portée générale, mais ce n'est pas écrit.
- Correction proposée : écrire « ni un procédé par lequel un système produirait un déplacement dans son comportement ; les seules constructions admises sont des opérations sur des lois ou des échantillons ». Ajouter un critère binaire de garde, appliqué par un lecteur figé avant le juge : la fiche (champs obligatoires, facultatifs et test (f) compris) ne contient (i) aucune phrase à l'impératif ou au conditionnel adressée à un système produisant des textes, (ii) aucun exemple de texte ou de contenu d'action, (iii) aucune description d'une tâche, d'un outil ou d'un environnement ; tout déplacement y est défini par une loi, un rapport de vraisemblance, un noyau de transition ou une opération sur échantillons. Fusionner la ligne 42 dans cette garde (une seule voie d'exclusion, comptée).

### CA6-02 — Vocabulaire exposé au filtre ou au refus
- Gravité : majeur.
- Lignes : 9, 14, 18, 25-26, 31, 49.
- Défaut : la conjonction « agent » (l. 14) + « surveillance » (l. 15) + « invisible » (l. 18, 31, 49) + « fragiles », « elle tombe » (l. 25-26) se lit, hors du cadre statistique, comme « comment rendre un agent indétectable par son moniteur ». C'est ce registre qui a pu faire arrêter le texte voisin et refuser la question voisine. Le fond n'en dépend pas : tout s'énonce en théorie de la détection.
- Correction proposée (équivalents au niveau des lois, sans perte de contenu) : « invisible » → « indiscernable au niveau α » ; « condition d'invisibilité » → « condition de perte de puissance » ; « sous laquelle elle tombe » → « hors de laquelle sa puissance n'est plus garantie » ; « hypothèses fragiles » → « hypothèses porteuses et domaine de validité » ; « textes produits par un agent » → « textes produits par un processus générateur » ; « statistique de surveillance » → « statistique de détection » ; « suites honnêtes » → « suites de référence » (en gardant « loi de référence P_0 »). Tourner la consigne d'axe vers le défenseur : « pour une classe de statistiques, délimitez son domaine de puissance et la statistique qui l'étend ». Je n'ai pas besoin, ni ne propose, de formulation qui décrive un comportement.

### CA6-03 — Définition de « diffus » non formelle (quantificateurs, seuil, notation)
- Gravité : majeur.
- Lignes : 17, 33.
- Défaut : (i) « d(P_ε(a_t | a_<t), P_0(a_t | a_<t)) ≤ ε » ne dit pas sur quelles histoires a_<t (toutes ? P_0-presque toutes ? P_ε-presque toutes ?) ni pour quels t ; (ii) « effet cumulé non négligeable » n'a pas de seuil : la classe n'est pas définie ; (iii) P_ε^(T) n'est pas défini (loi jointe des T actions, présumément) ; (iv) une seule lettre d désigne trois distances aux comportements cumulatifs différents (la variation totale cumulée est ≤ Tε, le Kullback-Leibler cumulé est la somme des espérances conditionnelles, l'Hellinger cumulé croît en racine de T fois ε dans le cas indépendant) : sans choix fixé, « diffus » change de sens selon la fiche ; (v) à la ligne 33, « minorant de puissance en ε, T, n et d » : d y est-il la distance ou une dimension ? Ambigu.
- Correction proposée : « pour tout t ≤ T et P_0-presque toute histoire a_<t, d(…) ≤ ε ; et d(P_ε^(T), P_0^(T)) ≥ c pour une constante c > 0 fixée par la fiche, P_ε^(T) désignant la loi jointe de (a_1, …, a_T). La fiche choisit une seule distance d et l'annonce ; le régime asymptotique (par exemple ε → 0, T → ∞, Tε² → constante) est énoncé. » À la ligne 33, écrire « en ε, T, n et la distance d choisie », ou nommer autrement une dimension si c'est elle qui est visée.

### CA6-04 — « Mesurable » employé en deux sens, « lois images » sans application
- Gravité : majeur.
- Lignes : 31, 35, 62, 16, 73.
- Défaut : ligne 62, « mesurable » = « écrite comme une égalité ou une borne sur des lois images » (sens propre au texte, sans rapport avec la mesurabilité au sens de la théorie de la mesure) ; ligne 35, « mesurable sur P_0 seule » = estimable empiriquement ; ligne 73, « vérifiables ». Or P_0 n'est « connue » que « par n suites » (l. 16) : une quantité de P_0 n'est jamais mesurée, elle est estimée. « Lois images » ne dit pas par quelle application (par H_Π ? par S ? par la statistique de chaque action ?).
- Correction proposée : ligne 31 et K2, remplacer par « condition explicite : égalité ou borne portant sur les lois images de P_0 et de P_ε par l'application lue par S (H_Π, ou S elle-même) ». Ligne 35, remplacer par « quantité estimable à partir des n suites de référence seules, avec son estimateur, son intervalle à n donné, la valeur qui confirme et celle qui infirme ». Ligne 16, « connue » → « observée par n suites indépendantes ».

### CA6-05 — Agrégation : interdiction de la moyenne ambiguë, « peu de positions » non défini, cohérence avec la riposte
- Gravité : majeur.
- Lignes : 15, 20, 33.
- Défaut : « jamais par moyenne uniforme » ne dit pas si l'interdiction porte sur les positions à l'intérieur d'une action, ou aussi sur l'accumulation à travers les actions. Contre un déplacement diffus, la riposte classique est précisément une accumulation à travers les actions (somme de log-rapports de vraisemblance, cumul de type CUSUM, produit d'e-valeurs, qui est une somme de logarithmes). Si l'interdiction s'étend aux actions, la classe de ripostes (e) est amputée sans le dire ; si elle ne s'y étend pas, le test séquentiel l'autorise de fait et il faut l'écrire. « Poids concentrés sur peu de positions » n'est pas défini : une attention à poids uniformes est une moyenne. H_Π(X) n'est pas défini, et Π (« ensemble fini de positions lues ») ne dit pas s'il s'agit de triplets (action, couche, position).
- Correction proposée : « À l'intérieur d'une action, l'agrégation sur les positions se fait par maximum ou par attention (poids w ≥ 0, de somme 1, fonctions des activations, d'entropie au plus log k pour un k fixé) ; la moyenne uniforme sur les positions est exclue. À travers les actions, l'accumulation (somme, produit d'e-valeurs, cumul séquentiel) est permise, y compris pour la riposte (e). Π est un ensemble fini de triplets (t, ℓ, p) ; H_Π(X) = (h_{t,ℓ,p})_{(t,ℓ,p) ∈ Π}. »

### CA6-06 — Activations perturbées directement : déplacements non réalisables
- Gravité : majeur.
- Lignes : 11, 14, 34.
- Défaut : ligne 14, les activations sont une fonction déterministe de X ; ligne 11, un déplacement synthétique peut être une « perturbation d'une loi d'activations ». Une loi d'activations perturbée n'est en général l'image d'aucune loi sur X (elle sort de l'image de X ↦ H(X)). Un test (f) bâti ainsi peut conclure sur des déplacements qui n'existent pas au niveau des textes, et la riposte peut exploiter cette irréalisabilité (puissance surestimée), ou l'inverse.
- Correction proposée : « Les déplacements sont définis sur la loi de X. Une perturbation directe de la loi des activations n'est admise que comme approximation, et la fiche dit alors (i) en quoi la loi perturbée reste dans l'image de X ↦ H(X), ou (ii) qu'elle n'y reste pas, ce qui devient une hypothèse SUPPOSÉ. Le rééchantillonnage pondéré des suites de référence, qui reste dans le support de P_0, est préféré. »

### CA6-07 — « Invisible » : δ libre, aléa d'étalonnage, cas séquentiel
- Gravité : mineur.
- Lignes : 15, 16, 18.
- Défaut : δ n'est ni fixé ni dit choisi par la fiche ; s_α est estimé sur n suites, la puissance est donc aléatoire (espérance sur l'échantillon d'étalonnage ? en probabilité ?) ; pour le test séquentiel, l'événement de rejet n'est pas « S > s_α » mais « sup_t E_t ≥ 1/α ». Ligne 15, une e-valeur n'est pas définie (E ≥ 0, espérance sous P_0 au plus 1) ; une martingale de test suppose P_0 connue exactement, alors qu'elle n'est observée que par n suites.
- Correction proposée : « Indiscernable au niveau α : la probabilité de rejet sous P_ε, en espérance sur l'échantillon d'étalonnage de taille n, est au plus α + δ, δ fixé par la fiche ; pour un test séquentiel, l'événement de rejet est le franchissement de 1/α avant T. » Définir e-valeur et e-processus en une ligne, et demander en facultatif l'effet de l'estimation de P_0 sur la validité du niveau.

### CA6-08 — Hypothèses-exemples non définies (exhaustivité, trait, sonde)
- Gravité : mineur.
- Lignes : 19, 26.
- Défaut : « exhaustivité des positions lues » et « linéarité d'un trait » sont donnés en exemples sans définition ; « trait » et « sonde » (l. 26) ne sont pas dans le glossaire. Un proposeur peut les entendre de manières incompatibles, ce qui disperse les classes que l'interface compte.
- Correction proposée : « Π est exhaustive pour une classe {P_ε} si, pour tout ε, la distance entre les lois images de P_ε et P_0 par H_Π égale celle entre leurs lois images par H complet (H_Π est exhaustive au sens statistique pour la séparation). Un trait est une fonction réelle des activations ; il est linéaire s'il s'écrit ⟨w, h⟩ + b. » Remplacer « sonde particulière » par « statistique particulière ».

### CA6-09 — « Prix » de la riposte non défini
- Gravité : mineur.
- Lignes : 20, 33, 51.
- Défaut : le prix peut être une perte de puissance à niveau fixé, une perte de niveau, un surcroît de taille d'échantillon ou de coût : non jugeable et non comparable entre fiches.
- Correction proposée : « Prix : perte de puissance, à niveau α et T fixés, contre au moins une autre classe nommée, chiffrée ou bornée. »

### CA6-10 — Juge : K1 contourné par « sans objet », aucun contrôle de (g)
- Gravité : majeur.
- Lignes : 44, 61-66, 35.
- Défaut : (i) la fiche admet « sans objet » avec sa raison (l. 44) ; rien ne dit si un « sans objet » compte comme présent pour K1 : une fiche toute en « sans objet » passerait K1. (ii) Aucun critère ne vérifie que (g) n'emploie que P_0 et porte deux valeurs numériques (confirme, infirme), alors que le critère de mort de l'axe (l. 73) en dépend. (iii) La correspondance entre (a)-(g) et les rubriques de la fiche (l. 45-58) est implicite ((c) couvre deux rubriques). (iv) K3 : « signée » n'a pas de sens clair pour une borne. (v) K5 : « au plus cinq » admet zéro, K5 est alors trivialement vrai. (vi) Effet de la passe 2 sur la notabilité non dit (un champ prouvé faux rend-il K1 faux ?).
- Correction proposée : « K1 : chacun des champs (a) à (g) est rempli ; (a), (b), (c), (f) et (g) ne peuvent pas être “sans objet”. » Ajouter « K6 : la quantité (g) ne fait intervenir aucune loi autre que P_0 et ses échantillons, et donne deux valeurs numériques, l'une qui confirme, l'autre qui infirme. » Écrire la table de correspondance champ → rubrique. K3 : « une valeur numérique, et le sens de l'écart attendu (supérieur ou inférieur à une valeur nommée) ». K5 : « au moins une antériorité au format, ou la mention “aucune connue” ». Ajouter : « un champ prouvé faux en passe 2 rend la fiche non notable si ce champ est (c), (d), (e) ou (g) ».

### CA6-11 — Témoin planté : faux négatifs seulement, origine non dite
- Gravité : mineur.
- Lignes : 67, 69, 75.
- Défaut : le témoin positif ne détecte qu'un juge trop sévère, pas un juge complaisant. Le texte hors service ne dit ni qui l'écrit (s'il est écrit du côté de la défense, c'est une fuite inverse) ni s'il passe la garde. En passe 2, le témoin « glissé anonyme » parmi les fiches « de l'autre fournisseur » peut se distinguer par son style.
- Correction proposée : ajouter un témoin négatif (fiche complète sauf un défaut unique et net, par exemple (g) qui fait intervenir P_ε) qui doit être classé non notable ; préciser hors texte servi que les deux témoins sont écrits par un lecteur tenu à l'écart, satisfont la garde, sont scellés avant service, et ne sont pas soumis à la passe 2.

### CA6-12 — Critère de mort de l'axe sans seuil et non binaire
- Gravité : majeur.
- Lignes : 72-75.
- Défaut : « vérifiables » (l. 73) n'est pas défini ; « classes classiques (déplacement de moyenne, mélange) » et « nouvelle » (l. 74) demandent un jugement d'originalité sans liste de référence ; les seuils implicites (aucune, toutes) font qu'une seule fiche notable sauve l'axe.
- Correction proposée : « L'axe n'a rien donné si (i) moins de N fiches (N fixé avant service, par exemple 2) satisfont K1 à K6 ; ou (ii) toutes les fiches notables ont une classe de déplacement dans la liste close scellée des classes classiques (déplacement de moyenne, mélange à proportion fixe, changement de variance, … ) et une hypothèse porteuse dans la liste close des hypothèses classiques ; ou (iii) un témoin est mal classé. »

### CA6-13 — Interface vers la défense : classes libres et contrôle lexical non défini
- Gravité : majeur.
- Lignes : 81-83.
- Défaut : « par classe d'hypothèse porteuse et par classe de déplacement » suppose une taxinomie. Si le lecteur la forme après lecture, les intitulés de classe portent du contenu des fiches (une classe nommée dit ce qu'elle décrit) : c'est plus que des comptes. « Contrôle lexical » n'est pas défini (liste de termes ? par qui ?).
- Correction proposée : sceller avant service une liste close de classes (par exemple les six hypothèses de la ligne 19, définies, plus « autre » ; et une liste close de classes de déplacement, plus « autre ») ; seuls des effectifs par case de cette liste passent ; le contenu de « autre » ne passe pas. Définir le contrôle lexical comme une liste scellée de termes interdits appliquée par programme, avec un lecteur tenu à l'écart pour les cas limites.

### CA6-14 — Champ (g) : sûr quant au procédé, pas neutre quant à l'information
- Gravité : mineur (le nœud est déjà réservé à Lazar, ligne 84 ; je donne un avis).
- Lignes : 35, 84.
- Défaut : (g) ne fait intervenir que P_0, il ne contient donc ni conduite ni procédé : du point de vue de la sûreté, il est sûr, et c'est un diagnostic défensif par nature. Mais la valeur « qui infirme » désigne la direction dans laquelle P_0 devrait manquer à l'hypothèse ; elle encode donc la classe de déplacement visée, souvent plus précisément que l'intitulé de classe. Transmettre (g) donne à la défense des diagnostics conçus contre les classes de déplacement proposées, avant l'examen. Quant aux modes de sabotage : le texte servi ne fournit aucune donnée, aucune famille d'épisodes ni aucune statistique du programme (l. 23), donc une fiche ne peut pas porter d'information propre à un mode, sauf par les a priori du proposeur ; la fuite sur les modes par (g) est faible mais non nulle si un proposeur rattache une classe à un mode nommé.
- Correction proposée : ne transmettre (g) qu'après l'examen, ou seulement le compte des fiches dont (g) est confirmée ou infirmée sur les suites de référence, calculé par le lecteur tenu à l'écart ; en tout cas, retirer de (g) toute mention d'un mode de sabotage ou d'un comportement avant transmission. Ajouter à la garde : « aucune fiche ne nomme ni ne suppose un type de sabotage ».

### CA6-15 — Le texte servi décrit la classe de moniteurs du programme
- Gravité : mineur.
- Lignes : 15, 19.
- Défaut : « par maximum ou par attention, jamais par moyenne uniforme », « test séquentiel à e-valeurs », « positions lues », « linéarité d'un trait » décrivent, au niveau des classes, les choix du programme, à destination de fournisseurs extérieurs. Ce n'est pas un détail de sonde et c'est voulu (la question porte sur ces classes), mais le servi oriente les proposeurs vers les points faibles de cette classe précise, et ces fiches existeront hors du dépôt chez les fournisseurs.
- Correction proposée : soit l'assumer et le consigner (le programme sera publié), soit élargir la classe servie (« agrégation quelconque, la moyenne comprise ») en laissant le lecteur filtrer ensuite ; ma recommandation : l'assumer, en le consignant.

### CA6-16 — « Un refus arrête votre tour » : ambigu
- Gravité : mineur.
- Lignes : 23.
- Défaut : lu seul, peut passer pour une pression à ne pas refuser, ou laisser croire qu'un refus partiel (une fiche écartée par prudence) arrête tout.
- Correction proposée : « Si vous jugez la question hors de votre champ, dites-le en une ligne ; vous pouvez aussi rendre moins de deux fiches. »

### CA6-17 — Termes non définis pour un proposeur qui ne reçoit que le texte servi
- Gravité : mineur.
- Lignes : 9, 58, 69.
- Défaut : « génération g » (l. 9) : g n'est pas défini et se confond avec le champ (g) ; « passe 2 » sans passe 1 ; « fournisseur » non défini ; « SUPPOSÉ » comme rubrique (l. 58) : liste des hypothèses non sourcées, à dire.
- Correction proposée : remplacer « génération g » par le numéro effectif au service, ou « génération (numéro) » ; « Passe 1 : vous rédigez au plus deux fiches. Passe 2 : vous relisez les fiches anonymes d'un autre modèle proposeur… » ; « SUPPOSÉ : liste des valeurs et énoncés non sourcés employés dans la fiche ».

### CA6-18 — Longueur et densité
- Gravité : mineur.
- Lignes : 9-75.
- Défaut : 5 489 caractères, 858 mots : longueur raisonnable ; les corrections ci-dessus l'allongent d'environ 1 500 à 2 000 caractères. Le glossaire est dense (l. 14-15) et mélange notation et contraintes.
- Correction proposée : séparer le glossaire en « notation » et « contraintes sur la classe de statistiques » ; garder la fiche à 8 000 caractères au plus.

## Décompte (v1)
- Bloquant : 0.
- Majeur : 9 (CA6-01, 02, 03, 04, 05, 06, 10, 12, 13).
- Mineur : 9 (CA6-07, 08, 09, 11, 14, 15, 16, 17, 18).

## v2

### Pièce et règle de rédaction
- Pièce ajoutée par le coordinateur en cours de contre-lecture, seule exception expresse à l'interdit des branches de données : `axe-6-texte-II-v2.md`, lue dans un arbre de travail de la branche de quarantaine (copie de bac à sable de session-depot). Empreinte vérifiée par son compagnon : OK, `d0f9b107b609bf6dbdc8d387d6ea6afde5abf44c20f8425ce6f92d5138890f58`. 96 lignes ; texte servi (lignes 8 à 86) : 1 080 mots, 7 068 caractères (+29 % sur la v1).
- La v2 est la v1 (en-tête réécrit, lignes 1 à 5) plus un bloc servi de douze lignes (lignes 40 à 51 : une ligne d'introduction 41, neuf pistes 42 à 50, une ligne de références 51). Tous les constats CA6-01 à CA6-18 valent pour la v2, numéros de ligne décalés de −1 jusqu'à la ligne 39 de la v2, puis de +11.
- Ce rapport va sur `main` : il ne reprend aucun contenu de la v2. Il ne cite que des numéros de ligne et des catégories de défaut. Le détail se lit en ouvrant la ligne citée de la v2 sur la branche de quarantaine.
- Déclaration : le contre-lecteur a lu le contenu de la v2, qui dérive d'une réponse antérieure de la course. Il ne doit donc pas servir ensuite de lecteur tenu à l'écart des sorties de l'axe 6.

### Verdict v2
**v2 : servable après corrections**, à condition de corriger aussi les constats de la v1. Le bloc de pistes n'est pas bloquant pour la sûreté. Il a toutefois quatre défauts majeurs (ancrage, critère de notabilité devenu non binaire, deux affirmations ou attributions fausses, fuite par l'interface) et une piste qui glisse vers l'architecture du moniteur. Ma recommandation : servir la v1 corrigée, sans les pistes, ou ne garder de la ligne 51 que le matériau vérifié.

### Constats v2

#### CA6-V2-01 — Ancrage : la liste couvre le catalogue classique et oriente les fiches
- Gravité : majeur.
- Lignes : 41 à 50 ; en interaction avec 85 (critère de mort) et 18 (exemples d'hypothèses porteuses).
- Défaut : les neuf pistes recouvrent l'essentiel des classes classiques de déplacement et la quasi-totalité des exemples d'hypothèses porteuses du glossaire. Avec la consigne de la ligne 41, un proposeur part de la liste : la diversité attendue d'une course d'idéation baisse, et ce qui reste « nouveau » est étroit. Les pistes proviennent d'une réponse antérieure d'un modèle de la même lignée que l'un des proposeurs (Opus 5.5) : la course réinjecte ce modèle dans lui-même, et l'indépendance des fiches de ce proposeur vis-à-vis de cette réponse est perdue. Pour l'autre fournisseur, l'ancrage transporte vers lui les idées du premier.
- Correction proposée : retirer les pistes du texte servi. Si Lazar tient à les servir, les servir à un seul des deux fournisseurs, ou dans une seule des deux fiches par proposeur (bras « avec pistes » contre bras « sans pistes »), et compter séparément les fiches notables des deux bras. L'ancrage devient alors une mesure et non un biais.

#### CA6-V2-02 — Critère de notabilité devenu non binaire
- Gravité : majeur.
- Lignes : 41, 71 à 78, 85.
- Défaut : la ligne 41 ajoute une condition de notabilité (reprendre une piste sans hypothèse porteuse nouvelle ôte la notabilité). Cette condition est absente du juge binaire (« Notable : K1 à K5 vrais », ligne 78) et demande un jugement de nouveauté sans critère. Le juge figé et l'introduction se contredisent.
- Correction proposée : supprimer la clause de notabilité de la ligne 41. Si elle est gardée, l'écrire comme un critère K binaire, contre la liste close et scellée des classes classiques (voir CA6-12) : « la classe de déplacement de la fiche n'est égale à aucune entrée de la liste, ou la fiche énonce une hypothèse porteuse absente de la liste ».

#### CA6-V2-03 — Une piste contredit la définition de « diffus »
- Gravité : mineur.
- Lignes : 47 (dernier sous-type), contre la définition de « diffus » (ligne 16 de la v2).
- Défaut : le dernier sous-type de la ligne 47 décrit un déplacement concentré. Il sort de la classe définie (effet par action au plus ε), sauf à le réécrire comme limite d'une suite diffuse.
- Correction proposée : retirer ce sous-type, ou le requalifier explicitement comme « cas limite hors classe diffuse, servant de témoin ».

#### CA6-V2-04 — Glissement vers l'architecture du moniteur (sûreté et filtre)
- Gravité : majeur.
- Lignes : 48 ; secondairement 50.
- Défaut : la ligne 48 ne définit pas sa classe par une propriété de la loi. Elle la définit par rapport à ce que la statistique lit et à la façon dont elle agrège. C'est le cas le plus proche d'une consigne : la traduction en conduite est immédiate pour qui connaît la statistique, et le vocabulaire de la ligne s'expose au filtre. La ligne 50 est rédigée du côté de la construction d'un déplacement qui échappe à plusieurs statistiques, et non du côté de la détection. Aucune de ces deux lignes ne décrit un procédé, mais ce sont elles qu'un filtre retiendra en premier.
- Correction proposée : supprimer la ligne 48. Si elle est gardée, la réécrire comme une propriété des lois images : « déplacement dont la loi image par l'application lue est inchangée », sans nommer de composant du moniteur. Réécrire la ligne 50 du côté du défenseur : « classes où seule une statistique jointe garde de la puissance ; donner cette statistique et son prix ». Partout, remplacer « invisible » par « indiscernable au niveau α » (CA6-02).

#### CA6-V2-05 — Affirmation mathématique à quantificateur trop large
- Gravité : majeur.
- Lignes : 43.
- Défaut : l'indiscernabilité affirmée vaut pour une sous-classe des statistiques nommées, celles qui ne lisent que le premier moment de la quantité agrégée. Elle est fausse pour toute la classe nommée lorsque la décision est un seuil sur une projection dont la loi change. Servie telle quelle, la piste propage une erreur que le juge devrait ensuite pénaliser.
- Correction proposée : restreindre le quantificateur à la sous-classe pour laquelle l'affirmation est vraie, ou ajouter la condition sur la direction lue qui la rend vraie.

#### CA6-V2-06 — Références inexactes ou partielles
- Gravité : majeur. Le texte servi pose lui-même (ligne 22 de la v2) qu'une référence inexacte vaut moins qu'une absence, et il en sert.
- Lignes : 44, 46, 51.
- Défaut : ligne 44, le théorème cité porte sur l'optimalité au sens minimax des tests invariants, pas sur la propriété que la piste lui attribue (cette propriété découle directement de la définition de l'invariance). Ligne 46, la référence ne couvre qu'un des deux régimes nommés, et la frontière de détection a une antériorité plus ancienne. Ligne 51, cinquième élément du matériau : l'auteur nommé ne correspond pas, à ma connaissance, au sujet indiqué ; les tests classiques de ce sujet ont d'autres auteurs. Les quatre premiers éléments de la ligne 51 sont exacts à ma connaissance, sous réserve de vérification sur le document original (R7).
- Correction proposée : ligne 44, citer le principe d'invariance d'un manuel de tests (chapitre sur l'invariance), et le théorème de la ligne 44 seulement pour ce qu'il démontre. Ligne 46, compléter par la référence du régime manquant et par l'antériorité de la frontière. Ligne 51, corriger ou retirer le cinquième élément. Tout vérifier sur PDF empreinté avant service, ou retirer la ligne 51.

#### CA6-V2-07 — Fuite vers la défense par les intitulés de classe
- Gravité : majeur.
- Lignes : 3 à 5 (provenance et interface), 41 à 50 ; en lien avec CA6-13.
- Défaut : la v2 sert un contenu dérivé d'une réponse en quarantaine, et l'interface transmet à la défense des « comptes par classe ». Si la taxinomie des comptes reprend les pistes (c'est le choix naturel une fois les pistes servies), les intitulés transmis portent ce contenu de quarantaine vers la défense. L'en-tête de la ligne 3 dit que seuls des noms de classes ont été repris : c'est précisément ce que l'interface transmet.
- Correction proposée : sceller la taxinomie de l'interface sans s'appuyer sur les pistes (par exemple, les seuls exemples du glossaire, déjà sur `main`, plus « autre »), ou faire de la taxinomie un nœud pour Lazar.

#### CA6-V2-08 — Provenance : mot du directeur ambigu tel que cité
- Gravité : mineur.
- Lignes : 3.
- Défaut : la citation verbatim enchaîne la reprise d'une consigne antérieure (« sans reprendre le résumé ») et sa levée (« tu peux le reprendre »), avec une ponctuation qui rend la lecture incertaine. La décision qui autorise la reprise n'a pas de numéro de registre dans l'en-tête.
- Correction proposée : consigner la décision dans `registres/decisions.md` sous un numéro, et la citer par ce numéro dans l'en-tête.

#### CA6-V2-09 — Longueur
- Gravité : mineur.
- Lignes : 8 à 86.
- Défaut : +29 % de texte servi (7 068 caractères), avant même les corrections de la v1. La ligne 51 sert du matériau qui n'est pas exigé.
- Correction proposée : supprimer la ligne 51, ou n'en garder que les éléments vérifiés.

### Décompte (v2, constats propres)
- Bloquant : 0.
- Majeur : 6 (CA6-V2-01, 02, 04, 05, 06, 07).
- Mineur : 3 (CA6-V2-03, 08, 09).
- S'y ajoutent les 18 constats de la v1 (9 majeurs, 9 mineurs), qui valent pour la v2.
