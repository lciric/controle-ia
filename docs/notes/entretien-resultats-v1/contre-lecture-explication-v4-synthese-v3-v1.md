# Contre-lecture : explication v4 et synthèse v3, contre leurs versions précédentes

**Verdict : fidèle avec corrections.** Les dix écarts de la contre-lecture précédente sont traités (neuf traités, un sans objet). Aucun chiffre de calibration ne reste, ni dans les HTML ni dans les PDF. La liste « ce qui manque » est identique à l'octet entre anciennes et nouvelles versions. Aucun résultat de la mesure unanime n'apparaît. Restent un écart moyen (une cellule périmée de l'explication, section 7.1) et sept écarts mineurs. Aucun écart grave.

## Empreintes vérifiées (sha256sum)
Les sept empreintes fournies concordent : explication v4 `0f72894f…`, v3 `01a39935…` ; synthèse v3 `5f0b1e94…`, v2 `e460995b…` ; PDF explication `71e191a5…` (39 pages) ; PDF synthèse `70ebb4b5…` (14 pages) ; contre-lecture qui commande `2408947c…`.

## Changements exhaustifs (diff, lignes coupées par `sed 's/></>\n</g'`)
**Explication v3 vers v4** (13 blocs) : en-tête (version 4) ; statut (« fidèle en l'état » sourcé, version 3 dite « fidèle avec corrections ») ; cartouche (une phrase ajoutée) ; titre de l'encadré d'état ; point « mesure unanime » (liste de sections remplacée par l'état) ; point « calibration » (taux retiré, renvoi au recompte) ; point T0.3 ajouté ; ligne « sections mises à jour » ; encadré « Changements depuis la version 3 » (cinq points et source) ; section 3.5 (« scellé en quarantaine, non lu ») ; pastilles des sections 4.2, 4.6 (trois) et 7.1 ; cellule de calibration de 6.1, sa consigne (« Ne citer aucun taux ») et ses sources ; glossaire ; deux lignes ajoutées aux sources. Rien d'autre.

**Synthèse v2 vers v3** (16 blocs) : en-tête ; section 0 (verdict T0.3, mesure unanime) ; titre de l'encadré d'état ; points 1, 2, 4 et 5 de l'encadré ; encadré « Changements depuis la version 2 » ; section 2.4 (verdict T0.3) ; section 5.1 (verdict T0.3, cellule de calibration) ; section 5.2 (mesure unanime) ; section 6.1 (verdict T0.3 ; mesure unanime, deux cellules) ; section 9 (deux lignes de sources ajoutées, une ligne mise à jour). Rien d'autre.

Chaque bloc correspond à un écart de la contre-lecture précédente ou à une consigne donnée au rédacteur. Seul retrait non déclaré : trois renvois de sources de la cellule de calibration de l'explication (écart 4 ci-dessous).

## Table des écarts
| N° | Document | Passage | Écrit | Attendu | Gravité |
|---|---|---|---|---|---|
| 1 | Explication v4 | 7.1, ligne « Mesure unanime » du tableau | « Mesure unanime : verdict par un lecteur neuf, après le scellement des préenregistrements T0.7 et P3-bis » ; « session-dépôt pour le verdict » | Le verdict est déjà prononcé et scellé (encadré, pastille de la même ligne). Ce qui reste est la lecture du verdict après les deux scellements. Cellule périmée, que la pastille contredit | moyenne |
| 2 | Explication v4 | cartouche | « aucune pièce lue n'atteste la fin de la course », puis « Depuis la version 3, la mesure unanime est courue… » | Phrase ancienne gardée, contredite par la suivante et par la liste finale (« attestés depuis la version 3 ») ; la retirer ou la dater | mineure |
| 3 | Explication v4 | légende des états, partie 4 | « « lancé » : course lancée, résultats non lus » | Plus aucune pastille ne dit « lancé » ; la pastille « courue, verdict scellé en quarantaine, non lu » n'est pas définie | mineure |
| 4 | Explication v4 | 6.1, sources de la cellule de calibration ; table des sources | renvois retirés : « l. 264-267 », « préenr. audit de fuite, l. 92 », « verdict P3 v2, l. 476 », « verdict T0.4 v2, l. 4, 10 » | Retrait cohérent avec la consigne, mais non déclaré dans l'encadré des changements ; la ligne « Verdict T0.4 v2 (harnais, « non prouvé ») » de la table des sources n'est plus citée nulle part | mineure |
| 5 | Synthèse v3 | section 7, « Gel chez le tiers de la mesure unanime, dès son scellement : une registration sous embargo, puis publique… » | décision présentée comme à venir | La version 15 est datée chez le tiers depuis 09:44:58 UTC (encadré, section 6.1) ; reste « figer et rendre public ». Cellule ancienne non mise à jour, couverte seulement par « prime » | mineure |
| 6 | Les deux | « 31 prédictions sur 31 » : synthèse 5.1 et section 0 (« Les 31 prédictions… se sont vérifiées ») ; explication 6.1, et 7.1 (« simulation (31 sur 31, verdict prononcé) ») | compte de prédictions confirmées | Contenu exact du verdict T0.3 (l. 12), pas un taux de calibration du programme. Il peut pourtant se lire comme un score parfait là où la réserve n'est pas accolée : explication 7.1 et synthèse section 0. Dans la synthèse 5.1, il est deux lignes au-dessus de la ligne « Calibration », avec « vérifie surtout les instruments ». Ajouter « attendu par construction » aux deux endroits nus, ou trancher | mineure |
| 7 | Les deux | calibration (encadré et cellule) | « s'est révélé faux sur plusieurs lignes » ; « un recompte à la main, contre-lu, le remplace » ; « en attendant la décision du directeur » | Affirmations neuves non vérifiables ici (pièce interdite) ; dans l'encadré de l'explication, aucune source accolée (elle est en 6.1). Forme : majuscule après deux-points ; dans la synthèse, deux points de suite après « directeur » | mineure |
| 8 | Explication v4 | encadré, « Sections mises à jour par les versions 3 et 4 : … 6.3 … » ; point 2 des changements | « partout » = cartouche, 3.5, 4.2, 4.6, 7.1, glossaire | Les sections 6.3 et la liste finale disent la même chose avec d'autres mots (« la course est faite… son verdict scellé… restent en quarantaine » ; « n'est pas lu ici »), sans la formule. Compatible, mais « partout » n'est pas littéral | mineure |

## Suivi des dix écarts antérieurs
| N° | Écart antérieur | Suite | État |
|---|---|---|---|
| 1 | Synthèse, point « bras d'attaque » non annoncé | Annoncé dans le titre de l'encadré (cinq mises à jour) ; réduit à la règle scellée `88418df0…` ; courriel et « ton geste » retirés ; retrait déclaré | traité |
| 2 | Synthèse, point T0.3 non annoncé, absent de l'explication | Annoncé dans le titre de l'encadré ; point 5 ajouté à l'encadré de l'explication ; même citation et même ligne (verdict, l. 10) dans les deux | traité |
| 3 | Synthèse, cellules périmées (verdict formel « en cours », « Version 15 en cours », v14) | Sections 0, 2.4, 5.1, 5.2, 6.1 et 9 mises à jour. Reste une cellule non citée alors : section 7 (écart 5 ci-dessus) | traité |
| 4 | Synthèse, comptes bruts de calibration en 5.1 | Comptes retirés, renvoi sans chiffre | traité |
| 5 | « 0,783 » répété dans les encadrés | Retiré des deux documents | traité |
| 6 | Explication 6.1, « gonflent les confirmations » et détails | Retirés | traité |
| 7 | Explication, en-tête « quatre mises à jour » | L'encadré en compte désormais quatre (mesure unanime, calibration, dépôt, T0.3) ; titre et en-tête concordent | traité |
| 8 | Explication, « fidèle en l'état » sans pièce | Sourcé : contre-lecture de fidélité v2 (`dd34becd…`), l. 3 ; vérifié | traité |
| 9 | Explication, liste de sections incomplète | Liste complétée ; erreur « 3.6 » pour 3.5 déclarée | traité |
| 10 | PDF, chemins et empreintes « tronqués » | Sans objet : en extraction brute, chemins et empreintes sont entiers, coupés sur deux lignes dans leur cellule (retour à la ligne, pas troncature) | sans objet |

## Chiffres de calibration (point 3)
Recherche dans les deux HTML et dans `pdftotext` des deux PDF (motifs : 0,78, 0,85, « tranchées », « confirmées », « réfutées », « non concluantes », 235, 47, « taux », « calibration », « prédictions sur »). Aucun taux de calibration, aucun compte de prédictions tranchées, confirmées ou réfutées du registre ne reste. Seul compte de prédictions confirmées restant : « 31 sur 31 » de la simulation T0.3 (écart 6).

## Liste « ce qui manque » (point 4)
Bloc extrait de chaque HTML, du titre de la liste au titre suivant : 96 lignes, même empreinte dans les quatre fichiers (`22afe022…`). Les PDF portent toute la liste (551 groupes de trois mots contrôlés ; les huit groupes non retrouvés dans la synthèse sont des cellules de tableau lues en colonnes).

## Affirmations neuves vérifiées (point 5)
- « T0.3 : confirmé avec réserves », verdict T0.3 v1, l. 10 : exact. Empreinte du verdict `bc53b746…`, égale à celle citée par la synthèse.
- « fidèle en l'état », contre-lecture de fidélité v2, l. 3 : exact ; empreinte `dd34becd…` exacte.
- « fidèle avec corrections », contre-lecture des ajouts, l. 3 : exact ; `2408947c…` exact ; renvoi « l. 18-20 » : lignes de la calibration, exact.
- Version 3 de l'explication `01a39935…` : exact.
- Heures et empreintes courtes de la mesure unanime (10:01:43, 10:33:16, 09:44:58, `7d19704d…`, `3a1651f4…`) : identiques entre les deux documents et à leurs versions précédentes ; non vérifiées dans les passations.

## À vérifier par la session-dépôt
- « un recompte à la main, contre-lu, le remplace » ; « Le registre automatique des issues s'est révélé faux sur plusieurs lignes » ; « en attendant la décision du directeur » ; empreinte courte `bd994163…` (pièce non ouverte, par consigne).
- « la session « attaquant informé » existe et a scellé la règle du bras (`88418df0…`) », index du bras v3, l. 14-23 (dossier interdit).
- « 10:01:43 → 10:33:16 UTC, code de sortie 0 » ; « verdict… scellé en quarantaine (`7d19704d…`) » ; « version 15 scellée (`3a1651f4…`), datée chez le tiers à 09:44:58 UTC » ; « reste à figer et rendre public » (passations de 09:46, 10:36, 10:46, non ouvertes).
- « Sections mises à jour par les versions 3 et 4 : … 6.3 … » et « citée « 3.6 » par erreur en version 3 » : l'explication v2 n'était pas dans les fichiers à lire.
- Pieds de page : absents du HTML, donc produits à la conversion ; à garder alignés à la prochaine version.

## Points vérifiés sans écart
- En-têtes : version 4 et version 3. Pieds de page des PDF : « version 4 » sur les 39 pages, « v3 » sur les 14 pages.
- Encadrés « Changements depuis la version précédente » présents dans les deux documents, avec leur source.
- Mesure unanime : aucun résultat ; formule « courue, verdict scellé en quarantaine, non lu » dans la cartouche, 3.5, 4.2, 4.6, 7.1 et le glossaire de l'explication, et dans les sections 0, 5.2, 6.1 et 9 de la synthèse.
- T0.3 : même verdict cité dans les deux documents ; sections 0, 2, 5 et 6 de la synthèse mises à jour comme annoncé.
- Bras d'attaque : la synthèse ne garde que la règle scellée ; plus de courriel ni de geste dans l'encadré.
- PDF : tout le texte ajouté est présent (90 et 73 fragments contrôlés ; les neuf non retrouvés sont des titres mis en capitales ou des cellules lues en colonnes).

## Fichiers ouverts
Les deux HTML de l'explication (v3, v4) ; les deux HTML de la synthèse (v2, v3) ; les deux PDF ; la contre-lecture qui commande ; `docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1.md` (l. 1-30) ; `docs/notes/entretien-resultats-v1/contre-lecture-fidelite-depuis-zero-v2.md` (l. 1-8). Fichiers intermédiaires dans le dossier temporaire de session seulement. Aucune recherche récursive, aucun fichier interdit, aucune commande git.

## Heures et modèle
Début 11:49:07 UTC ; dernier contrôle 11:51:18 UTC ; écriture ensuite (`date -u`). Modèle : Fable 5.2 (`claude-fable-5-2`).
