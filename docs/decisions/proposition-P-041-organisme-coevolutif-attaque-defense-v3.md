# Proposition P-041 — attaque et défense en un seul organisme coévolutif : revendication restreinte après Bailey et collègues — v3

Lignée session-depot, 31 octobre 2026, ≈ 08:56 UTC. Remplace pour la lecture la v2 (`2df36f87…`, inchangée, R12), qui remplaçait la v1 (`254b1782…`). Rien n'est lancé ni dépensé.

**Ce qui change par rapport à la v2** (contre-lecture neuve par Sonnet 5.5, six points, rien d'autre) : (1) §1.2, introduction et trait 3 : la note d'antériorité ne range « non trouvé » que le passage aux activations réelles d'un grand modèle de langage ; sur lois synthétiques, le trait 3 est contingent ; (2) voie 2 : « produite par un exécutant isolé, scellée » marqué comme garde proposée par le programme ; (3) voie 1 : « réunion des classes » marqué comme proposition du programme ; voie 3 : « mesure rapportée » (texte de R-880) au lieu de « jamais critère » ; (4) examen final : « signe négatif permis » rattaché à R-879 ; (5) les corrections 4 et 5 de la v2 (§4, « Corrections de la v1 ») sorties de cette liste et rangées sous « à ne pas reprendre (erreurs de lecteurs de la note) » ; (6) réserve 1 : « vraisemblablement » et portée de R-611 précisée, qualification laissée à Lazar.

## 0. Ce qui change, et pourquoi

- **Zone trouvée occupée** (nœud, R-861) : la boucle de la v1 (défense réentraînée contre l'archive, moniteur sur activations, rappel à 1 % de fausses alertes) est publiée avec un résultat négatif (Bailey et collègues, arXiv 2412.09565v2, §3.5, p. 11–13 ; vérifié sur PDF, `verification-bailey-2412.09565-v1.md`, `31eb1dde…`).
- **Décision de Lazar R-867 D1, appliquée par R-878** (« go recos ») : restreindre la revendication à ce que Bailey et collègues ne couvrent pas, après vérification sur PDF (faite, R-874).
- **Décision de Lazar R-880** (« go » sur R-879) : voies 1 et 2, examen final au protocole de Bailey, voie 3 en mesure rapportée ; P-041 v2 écrite après la synthèse du tour 1 de l'arène (faite, `synthese-organisme-coevolutif-v2.md`, `062f4dd6…`).
- Gardé de la v1 : trois paliers d'information, niveau des lois sur activations synthétiques, garde de l'invariant N-053 par code, puissance calculée sur processeur d'abord.

## 1. Revendication restreinte

### 1.1 Ce qui n'est plus revendiqué

| Élément de la v1 | Occupé par (pages lues sur PDF) |
|---|---|
| La boucle coévolutive en soi (alternance où chaque camp s'adapte au dernier état de l'autre) | Bailey p. 11 ; en contrôle, au niveau des invites : Diffuse AI Control `2606.08892v2` p. 7, 25, 28 ; autres occupants : note v2, §1.2 |
| L'archive des attaques passées | Bailey p. 11, 42 (ensemble incrémental de sondes) ; ARLAS `2510.05442v1` p. 5 |
| Le réentraînement itéré de la défense | Bailey p. 11–13 : rappel parfait sur l'archive, la nouvelle attaque passe encore après plus de 70 époques |
| Le rappel à 1 % de fausses alertes comme métrique | Bailey p. 6, 12. Gardé comme unité de mesure, non revendiqué |
| La prémisse « avantage du terrain » comme acquise | Contrainte dans un cadre voisin par Bailey (p. 13, convergence laissée ouverte) ; contestée en contrôle : Terekhov et collègues `2510.09462v2` p. 10 ; Nasr et collègues `2510.09023v1` p. 7, 9 |
| Les diagnostics de cyclage, trois des quatre bases, l'hypothèse héritage contre redémarrage | Note lecteur neuf v1 (`618c7c48…`), points 5 à 7 : MAGIC p. 10–12, AgentSafeEvo p. 7–10, Self-RedTeam p. 2 ; Dai et collègues `2502.04248v1` p. 6 |

### 1.2 Ce qui est revendiqué, et ce qui l'entoure

Les traits 1, 2, 4, 5 et 6 sont rangés « non trouvé » par la note d'antériorité v2 (`note-anteriorite-P-041-workflow-v2.md`, `900db290…`, §1.3) ; la vérification de l'absence y est dite **moyenne**, sauf mention. Le trait 3 ne l'est pas tel quel : la note ne range « non trouvé » que le passage aux activations réelles d'un grand modèle de langage (§1.3) ; sur lois synthétiques, le trait est contingent : la nouveauté disparaît si les activations ne sont que des vecteurs tirés de lois déclarées (§1.2, triplets). Aucun trait n'est un mécanisme neuf ; la revendication porte sur l'assemblage et sur la mesure.

1. **Familles adverses définies comme lois de probabilité sur des activations synthétiques**, à plages déclarées, face à un générateur. Voisins sans adversaire : SynthSAEBench `2602.14687v2`, Sanity Checks `2602.14111v1`. Chez Bailey, l'attaque porte sur les plongements d'entrée d'un vrai Llama-3-8B (p. 7, 9), sans loi déclarée.
2. **Défense informée des paramètres des familles**, non des seules instances. Chez Bailey, la défense ne voit que des instances (p. 11, 42). Réunion avec le contrôle non trouvée, vérification **forte** ; c'est un choix doctrinal du champ, pas un oubli (R8).
3. **Pire cas certifié sur une boîte de paramètres déclarée**, exprimé en détection à 1 % de fausses alertes. Le principe est occupé par le test d'hypothèses robuste sur lois gaussiennes ou alphabets finis (Goldenshluger, Juditsky et Nemirovski `1311.6765` p. 4–7 ; Tondi, Merhav et Barni `1802.02850` p. 8, 13–14) ; la note ne range « non trouvé » que le passage aux activations réelles d'un grand modèle de langage (§1.3) ; sur lois synthétiques, le trait est contingent : la nouveauté disparaît si les activations ne sont que des vecteurs tirés de lois déclarées (note v2, §1.2, triplets, complément 1). À trancher par Lazar : nœud du pire cas certifié (section 5, ligne « Trait 3 »).
4. **Cadre du contrôle avec moniteur boîte blanche** (agent non fiable, budget d'audit). Non trouvé, vérification moyenne à forte ; absent de Bailey.
5. **Familles tenues à l'écart conçues par des instances tierces de plusieurs fournisseurs, scellées, lues une seule fois** (N-050). Antécédents de la lecture unique : REUSE `2609.33180v2` p. 2–4 ; Blum et Hardt `1502.04585` p. 1 ; la coupure temporelle de Dabas et collègues `2510.21910v3` est un dispositif plus fort.
6. **Mesure de la boucle elle-même** (juge figé, témoins plantés, fausses promotions) **dans un cadre adverse**. Comme méthode, elle est publiée hors cadre adverse (REUSE ; PACE `2606.08106v1` p. 3–8 ; « Propose, Don't Judge » `2609.27051v1` p. 10–16) : seule l'application est revendiquée.

**Portée dans les deux sens** (vérification Bailey, question 4) : le mécanisme invoqué par Bailey pour son résultat négatif (« obfuscated activations are abundant in the latent space », p. 13) n'existe pas dans un espace de lois à paramètres bornés ; un résultat positif de P-041 sur lois synthétiques ne contredirait donc pas Bailey et ne dirait rien seul des vrais modèles. D'où les voies de la section 2.

## 2. Les voies retenues par Lazar (R-880)

**Voie 1 — certificat sur la classe déclarée ; transfert aux vrais modèles mesuré comme débordement.** La barrière est certifiée sur la classe déclarée (R-880) ; l'étendre à la réunion des classes à plages déclarées est une proposition du programme, absente de R-880 ; hors de la classe, elle n'est pas revendiquée mais mesurée : le débordement (écart entre le certificat et la détection sur familles tenues à l'écart, puis sur activations réelles) est une quantité préenregistrée avec son signe, **signe négatif permis**. « Certificat non délivré » est un résultat prévu, rapporté, si la borne de continuité fait défaut (tour 1 : C-T1, D-T3, A-T3). Le tour 1 la rejoint ; aucune cellule ne signe le transfert réel.

**Voie 2 — malléabilité comme paramètre borné de la classe.** L'abondance d'activations non signalées, cause du négatif de Bailey, entre dans la classe comme un paramètre borné, au lieu d'être absente par construction. Sa borne est estimée par un substitut : un modèle public de 8 milliards de paramètres (choix du modèle sur GO, interdit « changer de modèle sans GO »). **Le générateur reste au niveau des lois et des bornes, jamais d'une recette d'entrée** (N-053, N-054) : l'estimation ne rend qu'une borne ; qu'elle soit produite par un exécutant isolé et scellée est une garde proposée par le programme, absente de R-880 ; aucune entrée ni aucun score de moniteur réel n'entre dans le générateur. Apports du tour 1, qui ne l'a pas rejointe (synthèse v2, section 3) : elle rend testable l'issue réfutante de A-T1 (l'abondance existerait aussi dans un espace borné) ; elle met en tension la distinction de B ; la grille reste délivrable si l'information de Fisher est bornée (C-T2, A-T3 point 7).

**Examen final au protocole de Bailey.** Défense **figée**, sortie de l'arène ; optimiseur sur les entrées d'un modèle de 8 milliards de paramètres, au protocole publié (p. 11) ; comparaison à la base « instances seules » (défense entraînée sur instances, au sens de Bailey p. 11, 42). Préenregistré (R1, R-880), **signe négatif permis** (R-879, approuvé par R-880). L'avantage du terrain sert à apprendre ; l'attaque joue en dernier pour mesurer (fusion v3, point 1). Dépense de carte graphique : **devis à part**, rien n'est engagé. Le tour 1 n'en donne que le support synthétique (A-T2, C-T3 : bras informé dans la boucle) ; aucune cellule ne le propose (synthèse v2, correction 7).

**Voie 3 — couple détection et coût, en mesure rapportée.** Mesure rapportée (texte de R-880). Absente des douze cellules ; matériaux voisins : budget en calcul (C-T1, D-T1), coût d'une grille (A-T1, B-T2), arbitrage coût–précision (D-T3 point 4).

## 3. Ce que les tours du collisionneur ont établi

**« L'idée P-041 est-elle bonne ? »** (`synthese-idee-p041-bonne-v2.md`, `6817266c…`) : verdict **divergent** au sens du critère 1, corrigé de « commun » après trois sceptiques. Opus 4.6, Argon et Kimi disent « bonne pour les deux », avec un noyau commun de contrastes (paramètres contre échantillons), mais des conditions qui divergent sur le régime et le test de reparamétrisation ; Fable écrit deux conditions séparées. En support disjoint, seul Argon chiffre la condition d'évaluation remplie. Rien n'est construit ni mesuré. Appliqué (R-878) : D3, support disjoint à difficulté appariée, reparamétrisation non linéaire à l'entraînement, isométrie en contrôle nul ; D4, pas de rejeu avec Bailey servi.

**Tour 1 de l'arène** (synthèse v2, `062f4dd6…`, sept affirmations, aucune réfutée à deux sceptiques sur trois) :
- **un générateur aveugle, sans score, fait de la boucle un plan d'échantillonnage de la boîte (un curriculum), pas un jeu** — accord né de la critique croisée (A-T2, accepté par B, C, D). Conséquence : la « coévolution » n'existe que dans le bras informé de N-056, déclaré d'avance et rapporté à part ; le bras aveugle est une arène d'évaluation ;
- **la rechute du régime de Bailey n'est pas réfutable en bras aveugle** (mêmes cellules) : seul le bras informé, puis l'examen final, peuvent la réfuter ;
- **héritage positif prédit par les quatre espèces** (illustratif, sans poids de preuve), contre le signe de la v1 (« héritage < redémarrage ») et dans le sens de N-045 v2 ; accord trop propre, avec quatre seuils de certificat identiques : **réserve R4** ;
- **voies 2 et 3 absentes des réponses** ; l'examen final proposé par aucune cellule : à instruire à part (section 5).

## 4. Corrections de la v1

1. **SafeCoEvo `2609.36580v2` n'est pas un occupant** de la défense coévolutive : il coévolue deux composants de défense contre des bancs fixes (p. 1–6).
2. **Terekhov et collègues `2510.09462v2` non plus** : attaque adaptative contre un protocole figé. La coévolution du même groupe est Diffuse AI Control `2606.08892v2`, boucle automatique de dix cycles en contrôle, au niveau des invites (p. 7, 25, 28).
3. **« Kang et collègues 2019 »** : les chiffres sont dans la version 4 d'octobre 2023 signée Kaufmann et collègues (`1908.08016v4` p. 4, 7–8). Elle écrit que l'entraînement adverse en norme Lp *augmente* la robustesse aux attaques imprévues (p. 8) : citée pour « transfère mal », elle est mal citée ; signe publié **mitigé** (Tramèr et Boneh `1904.13000v2` p. 1 et Casper et collègues `2403.05030v6` p. 7, 9 vont dans le sens de la v1).
4. **Liste des occupants** : Bailey en tête, puis Diffuse AI Control, AgentSafeEvo, EvoSafety, RvB, MAGIC, Self-RedTeam, EvoDefense, Peer Pressure `2610.24896v1`, « Now You (Still) See Me » `2606.09411v1` (signe défavorable, p. 6).
5. **Diffuse AI Control**, base de l'environnement (a), n'est décrit nulle part dans le dépôt comme coévolution attaque–défense : à corriger.
6. **Revue de sécurité extérieure** : la v1 la rattachait à N-053 ; elle vient de R-611 (et N-057). N-053 fixe l'invariant « aucun score de moniteur dans l'entraînement ou la sélection de l'agent, hors bras d'attaque déclaré » (`decision-N-053-v1.md`, l. 42–44).
7. **Formules du dépôt surévaluées** (R-861) : « réfutée dans le cadre même de P-041 » devient « contrainte dans un cadre voisin » ; « le cœur technique est publié » devient « la boucle est publiée » (vérification Bailey, verdict).

### À ne pas reprendre (erreurs de lecteurs de la note)

Ces deux erreurs ne sont pas dans la v1 ; elles viennent des lecteurs c4 et c7 de la note d'antériorité v2, qui les corrige elle-même (§1.2, ligne 5+7 ; §2, corrections) :

- **ARLAS** est de Wang, Li, Keshava et collègues (`2510.05442v1`), non de « Lehre et collègues » ; erreur du lecteur c4.
- **Le jeu itéré en contrôle n'est pas seulement humain** : `2606.08892v2` le fait automatiquement (p. 5, 20, 25), contre ce qu'affirmait le lecteur c7.

## 5. Prochaines étapes

| Étape | Statut |
|---|---|
| Préenregistrement de l'arène d'évaluation : le tour 2 (lancé à 08:43 UTC, GO-2026-10-31-02, en cours) en propose un ; le programme le rédige à partir de sa synthèse, aux voies 1 et 2 et aux décisions D3, puis contre-lecture par un sous-agent neuf (R2), scellement (R1) | rédaction et contre-lecture : routine ; écart à la revendication fixée ici : nœud |
| Générateur en régime informé : ce qu'il reçoit (R-882 D3) | proposer avec recommandation ; défaut (a), bras informé de N-056 tel quel (fait 9 de la question v5 : ni poids, ni scores, ni seuils) ; scores synthétiques seulement sur ton mot |
| Calcul du budget fixé par le préenregistrement (R-882 D5) | proposer avec recommandation ; défaut (a) |
| Pilote de jugeabilité sur processeur (tête, générateur, test de reparamétrisation, deux budgets totaux) : rédigé, non scellé, non lancé (R-867 D2, R-878). Aucun brouillon trouvé dans `prereg/` à cette heure (recherche faite) | rédaction : routine ; scellement et lancement sur processeur, la décision D1 étant tranchée : proposer avec recommandation (recommandation : sceller après contre-lecture et lancer ; confiance moyenne ; défaut sous 48 heures) |
| Question séparée sur les voies 2 et 3 et l'examen final, écrite par le programme, contre-lue, versée à une v3 (R-882 D4) | rédaction : défaut (a) ; envoi au collisionneur : nœud (dépense sous GO) |
| Devis de carte graphique : examen final et estimation de la borne de malléabilité sur le substitut de 8 milliards de paramètres | nœud (dépense) ; et nœud de gouvernance : voir réserve 1 |
| Trait 3, nœud du pire cas certifié (§1.2) : activations synthétiques = vecteurs de lois déclarées, ou non | nœud (revendication) ; recommandation : garder le trait comme assemblage, l'occupation du principe écrite en clair ; confiance moyenne |
| Restes d'antériorité (note v2, §5) : pages décisives relues sur l'image, venue de Bailey, Huber 1965, citants d'octobre 2026 | routine |
| Contre-lecture de cette v2 par un sous-agent neuf, d'une autre famille si possible | routine |

## 6. Réserves

1. **Examen final et voie 2 face à R-611.** L'examen final fait tourner un optimiseur d'entrées contre une défense figée sur un vrai modèle ; l'estimation de la borne de malléabilité touche vraisemblablement le même objet. R-611 gèle toute construction ou exécution d'un pipeline opérationnel d'évasion en phases 1–2 (organismes évadeurs, démonstration en conditions réelles) jusqu'à une revue de sécurité extérieure. Un optimiseur au protocole publié de Bailey sur un modèle public de 8 milliards de paramètres n'est pas évidemment « opérationnel » au sens de R-611 : la qualification revient à Lazar. R-880 décide la voie, pas son exécution : **je propose que conception et préenregistrement continuent au registre de gouvernance, et que l'exécution attende la revue extérieure ou ton mot explicite.** Un refus de classifieur (R-597) ne se contourne pas.
2. **Argument a priori contre la voie 1 dans la classe** : à l'optimum, l'information au-delà du paramètre de classe ne vaut qu'hors de la classe (Barni et Tondi `1304.2172v1` p. 17–18 ; `1802.02850` p. 13–14 ; note v2, §1.1) ; un gain intra-classe serait un effet de budget fini, contre les quatre espèces du tour « idée bonne ».
3. **Transfert du synthétique au réel** : résultats publiés mitigés (Sanity Checks p. 13 ; SynthSAEBench p. 2, 10). Le certificat de Goldenshluger et collègues n'est quasi optimal qu'à un facteur près (`1311.6765` p. 4) : il peut être lâche à 1 % de fausses alertes.
4. **Zone séduisante, absence vérifiée moyennement** (R8) : un seul travail d'octobre 2026 réunissant coévolution par générations et moniteur sur activations en contrôle ferait passer la collision à totale.
5. **Chiffres** : aucun n'est un résultat du programme ; pages relevées sur le texte extrait, seules les pages 12 et 45 de Bailey relues sur l'image (R7).
6. **Même famille** : notes, vérification, synthèses et cette v2 sont d'Opus ; contre-lecture du tour 2 par Sonnet 5.5, écart à N-052 (R-883).
7. **Tour 2 en cours** : sa synthèse pourra demander une v3.
8. **Accords trop propres** du tour 1 : audit R4 avant tout préenregistrement qui les reprendrait.

Sources (sous `docs/notes/anteriorite-P-041-v1/`, empreintes ci-dessus) : note d'antériorité v2, note du lecteur neuf v1, vérification de Bailey, fusion v3 (`343617ca…`), les deux synthèses v2 ; registre R-843 à R-885, R-611 ; N-053.
