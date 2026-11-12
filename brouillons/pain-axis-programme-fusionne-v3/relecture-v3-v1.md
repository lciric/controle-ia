# Relecture de la v3 du programme fusionné « pain axis » — rapport du sous-agent neuf — v1

Versé par la session 15 le 2026-10-17, tel que rendu par le sous-agent neuf `a361dd746048764d1` (lancé à 09:21 UTC, rendu
vers 09:47 UTC ; ni auteur de la v3 ni du traitement ; aucun accès réseau). Texte du rapport recopié sans modification de
fond (mise en page seule). Pièces relues : `programme-fusionne-v3.md` et `traitement-verification-v1.md` (empreintes en
section 1). Traitement des constats : en v4, par la session (R-194). Aucune diffusion sans GO (DI-26).

## 1. Empreintes des deux textes relus

Calculées par `sha256sum` au début de la lecture. Chacune est égale à son sceau `.sha256`.
- `294e8afe22dfc0a81c56476ec022d6d8e1ecfe59ce2884f3a6f8b129c0930bb1` /home/user/controle-ia-travail/brouillons/pain-axis-programme-fusionne-v3/programme-fusionne-v3.md
- `dd9bb0edc029d240dec57e6cf6b6ebeb4ab39ac475b8bd7da5ebf00cf321dfcb` /home/user/controle-ia-travail/brouillons/pain-axis-programme-fusionne-v3/traitement-verification-v1.md

## 2. Verdict

La v3 fait ce que le traitement annonce, aux endroits annoncés, pour les 20 constats : 19 sont bien portés et VT-01 l'est en
partie. Je ne trouve aucune empreinte, page, ligne, commit, décision ni renvoi « nœud n » faux, et aucune dose ni texte
d'attaque.

Il reste un point majeur à corriger avant la transmission : la « règle unique » de niveau range la préparation (code, plan
écrit) au niveau « proposition ». Cela contredit `CLAUDE.md` et la v3 elle-même, qui classe ce même code en « routine ».

Il y a aussi huit points mineurs. Les principaux :
- le nœud 14 oublie des fichiers : les deux doses retirées au titre de VT-03 restent dans la v1, dans la v2 et dans le
  rapport de vérification ;
- l'état au 17 octobre était déjà incomplet au scellement, et il est périmé depuis GO-2026-10-17-01 ;
- le nœud 2 est incomplet côté agent.

## 3. Constats

Abréviations : « v3 » désigne programme-fusionne-v3.md, « T » désigne traitement-verification-v1.md.

| Id | Fichier et ligne | Ce que dit le texte | Ce qu'il devrait dire, et pourquoi (source) | Gravité | Correction proposée |
|---|---|---|---|---|---|
| RL-01 | v3 l. 3 (statut), l. 76 et 81 (§ 3, PA-3 et PA-8), l. 120 et 130 (§ 5), l. 187 (§ 8), l. 197 (nœud 1) ; T l. 9 | « le niveau « proposition » (défaut sous 48 heures) ne sert ici qu'à la préparation (code, plan écrit) ». Pour PA-3 : « sa préparation (plan écrit, code) est une proposition ». Au § 8 : « Proposition seule : … préparation (code, plan écrit) de toute unité ». | Dans `CLAUDE.md` (l. 51-52), le code, les tests et les fichiers sont de la routine ; un plan écrit est donc aussi de la routine. Le niveau « proposition » n'y couvre que les couches et concepts de sondes, le portage des environnements, le périmètre interne d'une phase et D1 à D3. La v3 se contredit : le code de PA-1 est « routine » (l. 74, l. 100), et le même § 8 écrit « Phase 0, sur processeur, routine : code … » (l. 186) puis « Proposition seule : … préparation (code …) » (l. 187). La règle annoncée comme unique ne l'est donc pas. L'erreur vient de la formule de VT-01, reprise telle quelle. | majeur | Écrire partout : « routine : la préparation (code, tests, plan écrit), qui n'engage l'entrée d'aucune unité ; proposition : les seuls choix que `CLAUDE.md` met à ce niveau (ici la coupe, au titre du périmètre interne d'une phase ; une conclusion sur D1) ; nœud sans défaut : toute entrée dans un préenregistrement ». Lignes 3, 76, 81, 120, 130, 187, 197. |
| RL-02 | v3 l. 3, à comparer avec l. 118 (PA-2), l. 120 (PA-3), l. 187 et l. 197 | Le statut écrit « toute entrée dans un préenregistrement est un nœud (nœud 1) », sans exception. Ailleurs, deux choix restent au niveau « proposition » : le lecteur du bras C-P4b, « fixé au scellement » (l. 118, donc inscrit dans le préenregistrement), et une conclusion sur D1 (l. 120). | Les deux exceptions sont fondées : DI-01 pour C-P4b ; D1 est au niveau « proposer » (programme l. 153). Mais le statut ne les annonce pas. Le fondement donné par T l. 9 pour C-P4b (« niveau des concepts de sondes ») est faible : un concept est ce que la sonde détecte (programme § 8.1, l. 143). Le vrai fondement est N-013 § 8 (« sonde sur le modèle qui traite le contenu ») et DI-01. | mineur | Annoncer dans le statut deux exceptions au niveau proposition : le lecteur du bras C-P4b (le juge, imposé par N-013 § 8 ; DI-01), s'il n'est lié à aucune lecture d'affect ; une conclusion sur D1 qui ne change aucun modèle (sinon nœud 5). À traiter avec RL-01. |
| RL-03 | v3 l. 198 (nœud 2) ; T l. 10 | « Côté agent, le programme prévoit les organismes par réglage fin léger (… section 7, (ii) ; T0.6) et le bruit d'activations de H6 (E1.6 …) » | La liste est incomplète. Le programme prévoit aussi, côté agent : E1.5 (b), attaques adaptatives « pondérales (réglage fin, puis apprentissage par renforcement au niveau action, sous GO) » (programme l. 187) ; EC.4, obfuscation d'activations portée sur 8B, pour HC4 (l. 197 ; régime « poids réglables » de N-013 § 3). L'erreur vient de la correction proposée par VT-02. Par ailleurs, « d'un moniteur » est trop large : le programme réentraîne les sondes (l. 146, l. 170), et les sondes sont des moniteurs au sens de son § 8. | mineur | « Côté agent, le programme prévoit les organismes (section 7, (ii) ; T0.6), les attaques pondérales de E1.5 (b), sous GO, l'obfuscation d'activations de EC.4 et le bruit d'activations de H6 (E1.6 ; N-015) ; les écritures listées ici n'en font pas partie. » Écrire aussi « d'un moniteur génératif (juge) ». |
| RL-04 | v3 l. 17 (§ 0) et l. 265 (§ 13) ; T l. 23 (VT-15) | « veille reprise par la session 15 le 17 octobre (R-184) » ; « dans leur état du 17 octobre (R-184) » | Au scellement de la v3 (commit `72ee91f`, 08:34:08 UTC, d'après `.git/logs/HEAD`), deux décisions étaient déjà consignées. R-185 (commit `d6963f2`, 08:04 UTC) : le sixième appel du lanceur a été arrêté par la session avant la création, sans dépense. R-186 (commit `6593a49`, 08:22 UTC) : Lazar a donné son accord dans la session et le septième appel a été engagé (`registres/decisions.md` l. 321-323). L'état « au 17 octobre » les omet. T a été écrit à 08:23 et les omet aussi. | mineur | § 0 : « sixième appel engagé (R-184), arrêté par la session avant la création, sans dépense (R-185) ; accord de Lazar dans la session 15 (R-186) ; septième appel engagé à 08:22 UTC ». § 13 : « (R-184 à R-187) ». |
| RL-05 | v3 l. 3, 17, 20, 21, 22, 110, 160, 188, 189, 197, 208 (mise à jour pour la v4) | « pilote T0.9 … soumis à un GO séparé, non accordé » (l. 21) ; « qui attend un GO séparé » (l. 188, l. 189) ; « GO du pilote T0.9 » est compté comme nœud de PA-2 et PA-5 (l. 160) ; « T0.7 en brouillon 3 » (l. 20) ; dépense ≈ 54,6 USD (l. 22) | Depuis le scellement : R-188 et R-190 (septième et huitième appels arrêtés ; lanceur v2 de l'option (c) décidé par Lazar) ; R-189 (brouillon 4 de T0.7) ; R-192 et `registres/go.md` l. 26 (**GO-2026-10-17-01** : pilote T0.9, 4 heures au plus, après le scellement du préenregistrement de HC1 à HC3 contre-lu ; P3, nouveau préenregistrement réduit) ; `registres/depenses.md` l. 81 (cumul ≈ 54,7 USD à 09:10 UTC). « Non accordé » est désormais faux. Greffer PA-2 ou PA-5 sur le pilote reste un nœud (nœud 1, et nœud 12 au-delà des 4 heures). | mineur | Mettre à jour ces lignes dans la v4. Ajouter la passe de P3 aux greffes possibles (l. 110, l. 188), qui sont des nœuds. Ajouter son préenregistrement à la liste des l. 3 et l. 197. |
| RL-06 | v3 l. 210 (nœud 14) | Le nœud ne nomme que VP-12 et VP-14, la revue croisée, trois fichiers de `travail/` et la ligne de la fenêtre d'effet de la v1. | Des fichiers scellés recopient aussi des paramètres publiés de pilotage (recherche faite chiffres masqués ; je ne recopie pas les valeurs). Les **deux doses de Berg et Kaiser** retirées par VT-03 restent dans : `programme-fusionne-v1.md` l. 55 ; `verifications-citations-v1.md` l. 46 (VP-25) ; `travail/citations.md` l. 38 ; `programme-fusionne-v2.md` l. 55 ; `verification-v2-v1.md` l. 31 (citation de VT-03). Le **coefficient de pilotage** du papier source figure dans `reconciliation-v1.md` l. 88 et l. 168 (`bfc9f9df…`), donnée de même nature que les « coefficients par taille de modèle » de DI-07. La recherche de T sur VT-03 n'a porté que sur la v3. | mineur | Compléter la liste du nœud 14 avec ces fichiers et lignes, sans valeurs. L'option (a) reste valable, car tous sont sous `brouillons/pain-axis-*`. |
| RL-07 | v3 l. 211 (nœud 15) ; l. 89 (PA-16) | « Ni le programme ni les décisions N-005, N-006 et N-013 ne nomment un attaquant en boîte grise contre le juge ou une copie du juge (aucune occurrence…) ; les y ajouter étendrait le modèle de menace » | Le nœud est justifié : modifier une revendication est un nœud (`CLAUDE.md`, R-147). Le numéro 15 préserve bien les renvois. Mais le contrôle n'est que lexical. Le programme mesure déjà des attaques « optimisée[s] contre A » (l. 146), et HC6 et EC.6 parlent d'« attaque optimisée » (l. 108, l. 199), sans préciser l'accès de l'attaquant. Le juge Llama-3.1-8B du panel de D2 a les poids de l'agent (brief v2 l. 38 et l. 69) : la « copie du juge » existe donc déjà. Enfin, la ligne de PA-16 dit « nœud (invariant, modèle de menace) », mais le nœud 15 ne cite pas PA-16. | mineur | Poser la question : ces cellules relèvent-elles de EC.5 ou EC.6 (entrée seule, nœud 1) ou étendent-elles le modèle de menace et les revendications de C (nœud 15) ? Ajouter PA-16 (calibrage empoisonné), ou écrire à sa ligne « nœud 8 ». |
| RL-08 | T l. 49 (§ 4) | « La v3 attend sa relecture avant scellement par un quatrième sous-agent neuf (R2, R-183). » | Contredit v3 l. 7 et R-187 : la v3 est scellée avant sa relecture, ce que R-187 déclare comme écart au plan de R-183. T a été scellé avec la v3 dans le commit `72ee91f`. | mineur | Dans le prochain traitement (T est scellé, R12) : « v3 scellée avant sa relecture (R-187) ; constats en v4 ». |
| RL-09 | v3 l. 83 (§ 3, PA-10), l. 134, l. 136 point (5) ; l. 187, l. 197 | PA-10 n'a pas de niveau pour ses ajouts à l'intérieur de HC5 : le « Prix mesuré » (l. 134) et « Désaccord d'ensemble : à fusionner avec le quorum hétérogène déjà accordé (GO-2026-10-04-07) » (l. 136). | Selon la règle unique, faire entrer cette mesure et cette fusion dans le préenregistrement du papier C est un nœud sans défaut (nœud 1). GO-2026-10-04-07 accorde le quorum, pas cette fusion. La formule « à fusionner » se lit comme une décision déjà prise. PA-10 manque au nœud 1 et au § 8. | mineur | Ajouter à PA-10 (tableau et fiche), au nœud 1 et au § 8 : « entrée du prix de la défense et du désaccord d'ensemble dans un préenregistrement : nœud sans défaut (nœud 1) ». |
| RL-10 | v3 l. 44 | « Sous pilotage douleur » | Même cas que VT-20, deux lignes plus haut dans le même tableau : `LISEZMOI-v2.md` l. 29 impose le vocabulaire « direction ». La l. 28 l'applique déjà. | pour information | « Sous pilotage de la direction douleur ». |
| RL-11 | v3 l. 130 | « la cellule Llama 3 8B de la sonde « moyenne », à 2,8 » ; « la moyenne cède » | Le tableau 1 (2506.14261v4, p. 7, `4b096062…`, sceau conforme) a deux lignes « (mean) ». Seule « Linear (mean) » donne 2,8, 3,1 et 3,85 (valeurs justes). « Attention (mean) » tient : évasion de 0,01 à 0,02. Le papier le dit p. 7 : « attention probes and max aggregation remain robust ». Précision de symétrie (R4). | pour information | « la sonde linéaire à moyenne (« Linear (mean) ») » ; ajouter que la sonde à attention agrégée par la moyenne tient (0,01 à 0,02). |
| RL-12 | v3 l. 251-252 | « lu au commit `197e909` (VT-10) » | `197e909` n'était que la racine du clone partiel de la session 14 (VT-10) ; il est absent du clone actuel. Les PDF sont identiques à tous les commits depuis le 6 octobre. La mention garde un artefact du clone partiel, sans contenu. | pour information | Retirer la mention, ou écrire « `197e909` : racine du clone partiel de la session 14, sans rapport avec le versement ». |
| RL-13 | v3 l. 207 (nœud 11) | La recherche du 17 octobre vers 08:30 UTC est citée sans renvoi au registre ; « la page de conférence ne renvoie qu'à la page OpenReview `jg5ptjnU6J`, ni PDF ni version arXiv ». | Cette recherche est consignée dans R-187 (« page de conférence relue : aucun PDF »). Le détail sur OpenReview et arXiv n'y figure pas, et aucune provenance n'est versée pour cette recherche. | pour information | Ajouter « R-187 ». |
| RL-14 | v3 l. 193 | « selon la vérification de la v2 (VT-01 à VT-18) » | Seuls VT-01, VT-02, VT-04 à VT-07, VT-14 et VT-16 à VT-18 modifient le § 9. VT-03, VT-08 à VT-13 et VT-15 n'y touchent pas. | pour information | Donner la liste exacte. |
| RL-15 | v3 l. 187 (§ 8) ; l. 74, l. 160, l. 197 | Le § 8 (« Avant le scellement du papier C ») omet base-3, que le nœud 1 cite. L'entrée de PA-1 n'est listée ni au § 3, ni au § 6, ni au nœud 1. | La passe de PA-1 est une expérience nouvelle (R-167) et exige son propre préenregistrement (R1) : son entrée est un nœud sans défaut. Aujourd'hui, elle n'est couverte que par la formule générale du nœud 1. | pour information | Ajouter base-3 au § 8. Ajouter « entrée de PA-1 et de son préenregistrement (nœud 1) » aux l. 74, 160 et 197. |
| RL-16 | v3 l. 105, l. 138, l. 186 | « proposée à Lazar (VF-12) » ; « proposition soumise à un nœud » ; « Hors routine » | Ce sont des restes d'étiquettes hors des trois niveaux (DI-24). « Proposition » y est pris au sens courant, ce qui brouille la règle unique. | pour information | « nœud 1 (lecture au dernier jeton dans le préenregistrement de PA-1) » ; « idée soumise au nœud 8 » ; « Hors routine : nœud 13 (e) ». |
| RL-17 | v3 l. 168, à comparer avec l. 33 et l. 234 | RP-PA-11 « s'applique dans ce texte à partir de la v3 » | Deux citations du papier source restent sans version ni page. L. 33 : la phrase sur la séparation figure en v2 p. 11. L. 234 : le lien au bien-être du modèle figure en v2 p. 23, relue (« would track an important constituent of AI welfare »). | pour information | Ajouter « v2 p. 11 » à la l. 33 et « v2 p. 23 » à la l. 234. |

## 4. Ce que je n'ai pas pu vérifier, et pourquoi

- **Faits qui demandent le réseau** (aucun accès réseau) :
  - numéros et état des demandes de fusion n° 9 à 11 relus sur l'API (T § 3, v3 l. 23) ;
  - branche distante `donnees/t05/…` à la tête `361a9f6` ;
  - recherches de « Where Empathy Goes Wrong » des 15 et 17 octobre, et ce que renvoie la page de conférence (v3 l. 207).
- **Commit `197e909` et date du commit qui a versé les deux PDF.** Ils sont absents du clone partiel actuel. Seules les
  provenances (lot 2 l. 63, lot 3 l. 11 : 6 octobre) l'attestent.
- **« Aucun refus du filtre pendant la rédaction de la v3 »** (l. 237) : c'est une déclaration de la session, que je ne peux
  pas vérifier.
- **Paramètres des annexes v1 et v2.** Je les ai repérés par comptage et par recherche chiffres masqués, sans lire ni
  recopier les valeurs. Je n'ai pas cherché les esquisses de grilles sans chiffre au-delà des motifs demandés.
- **Lignes inchangées de la v3.** Je les ai revues par sondage seulement. Le contrôle complet porte sur les 37 blocs modifiés
  depuis la v2.
- **Méthode.** Aucune commande git. J'ai lu les objets de `.git` avec un petit lecteur Python en lecture seule, placé dans le
  bloc-notes ; il m'a servi à vérifier les commits `3484d11`, `11f8b2a` et `72ee91f` et le contenu de `registres/etat.md` à
  `11f8b2a`. J'ai lu la figure 10 (p. 22) sur l'image de la page avec l'outil de lecture de fichiers, car `pdftotext` n'en
  donne que la légende. Le filtre de sûreté n'a refusé aucune lecture ni aucune rédaction.

## 5. Bilan chiffré

**17 constats** : 0 bloquant, 1 majeur (RL-01), 8 mineurs (RL-02 à RL-09), 8 pour information (RL-10 à RL-17).

**(a) Portage des VT : 19 bien portés, 1 porté en partie (VT-01), 0 non porté.**
- VT-01 est porté en partie : tout ce que T annonce est fait aux endroits annoncés, mais la règle unique telle qu'écrite se
  contredit (RL-01, RL-02).
- Les sorts sont justifiés : 18 retenus ; VT-14 retenu en partie, à juste titre, puisque R-183 est postérieur au rapport de
  vérification ; VT-19 déjà fait, vérifié sur l'objet du commit `11f8b2a` (15 octobre, 13:23 UTC), dont `registres/etat.md`
  contient « Aucune diffusion sans GO ».
- Les quatre constats des contre-lectures sont couverts : DI-02 par VT-04 ; DI-24 par VT-01 et VT-06, avec des restes
  d'étiquettes (RL-16) ; EX-20 par VT-02 ; DI-26 par VT-19.

**(b) Aucune erreur nouvelle sur les chiffres et les références.**
- Empreintes de la section 13 : 12 sur 12 égales à leur sceau. Les 37 PDF de l'annexe sont conformes. Les fichiers aux
  commits cités (`3484d11`, `11f8b2a`, `72ee91f`) ont les empreintes annoncées.
- Les 66 renvois « nœud n » pointent le bon nœud.
- Les pages et chiffres ajoutés sont justes : figure 10 relue sur l'image ; 2609.35591v2 p. 10 ; 2506.14261v4 p. 6, p. 7 et
  p. 18. Les lignes citées (revue croisée l. 256, 317, 453 ; correspondance l. 78 ; programme l. 97, 132, 188 ;
  provenances) et les décisions sont justes.
- Section 0 : la dépense concorde avec les registres (≈ 54,6 USD ; `registres/depenses.md` l. 76, `registres/etat.md`
  l. 67). L'état était incomplet au scellement (RL-04) et il est périmé depuis (RL-05).

**(c) Niveaux.** La règle d'entrée est appliquée au § 3, au § 5, au § 6, au § 8 et au nœud 1. La préparation a deux niveaux
contraires (RL-01), les exceptions ne sont pas annoncées dans le statut (RL-02), et PA-10 n'a pas de niveau d'entrée
(RL-09). Le nœud 15 est justifié, mais sa formulation est à compléter (RL-07).

**(d) Discipline.** Dans la v3 et dans T :
- motifs demandés : « d = » 0 dans la v3 (1 dans T, simple liste des motifs cherchés) ; « coefficient » 0 ; « fois » 0 ;
  « dose » 6, toutes des mentions de discipline ou « deux doses négatives publiées, non recopiées » ; « norme » 3, toutes
  « même norme » ; « couche » 8, toutes des positions de lecture ;
- aucun texte d'attaque ni aucune chaîne déclencheuse ;
- les gestes d'intervention n'apparaissent que comme nœuds, et rien ne va vers une publication ;
- le vocabulaire « direction » est respecté, sauf RL-10 ;
- les paramètres qui subsistent sont dans des fichiers scellés oubliés par le nœud 14 (RL-06).
