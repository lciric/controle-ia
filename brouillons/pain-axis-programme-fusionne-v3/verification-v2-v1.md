# Vérification du traitement et du brouillon v2 du programme fusionné — rapport brut du sous-agent neuf — v1

Versé par la session 14 le 15 octobre 2026, tel que rendu par le sous-agent (lecture seule, fichiers donnés explicitement, R2 ; lancé vers 12:47 UTC, rapport vers 13:14 UTC, 105 appels d'outils), sans retouche du fond ; seule l'indentation du cadre de restitution a été retirée. Objet : vérifier que `brouillons/pain-axis-programme-fusionne-v2/programme-fusionne-v2.md` (`189d049a…`) porte fidèlement les 59 constats des deux contre-lectures selon `traitement-constats-v1.md` (`9d82e0b2…`), sans erreur introduite. La v2 étant scellée (R12), le traitement de ce rapport va dans ce dossier neuf, avec une v3.

---

## Empreintes des cinq fichiers relus

Calculées par `sha256sum` le 15 octobre. Elles sont identiques avant et après le commit `3484d11`, que la session mère a fait à 12:49:23 UTC pendant ma relecture. Chacune est égale à son sceau `.sha256`.
- `741a1075e336fc3b26a3bc6e119e956007febff4a51caaed73ac805fbaa2d9f5` /home/user/controle-ia-travail/brouillons/pain-axis-programme-fusionne-v1/programme-fusionne-v1.md
- `e40ac88590b59503b90a66c91d8b90578e625341f847e4ba48cdc6d6ae57faec` /home/user/controle-ia-travail/brouillons/pain-axis-programme-fusionne-v2/contre-lecture-exactitude-v1.md
- `d1e240ba45b30ba2aff3998090792d0b97ce16a2ccf8e46a43bdb6e4a5423859` /home/user/controle-ia-travail/brouillons/pain-axis-programme-fusionne-v2/contre-lecture-discipline-v1.md
- `9d82e0b2bea644555b0aaa261106df4eaf392ebd26a66dcfd75254658bcfa098` /home/user/controle-ia-travail/brouillons/pain-axis-programme-fusionne-v2/traitement-constats-v1.md
- `189d049a0880afb799bb2c298a009ee54d7dbb4be557cbe9a5a445bdcd3187cf` /home/user/controle-ia-travail/brouillons/pain-axis-programme-fusionne-v2/programme-fusionne-v2.md

**Verdict.** La v2 porte fidèlement 55 des 59 constats, et je ne trouve aucun point bloquant. Trois points majeurs sont à corriger avant de transmettre (dans une v3, puisque la v2 est scellée) :
- les niveaux de décision restent incohérents pour plusieurs unités ;
- le nœud 2 dit à tort que le programme ne prévoit aucune écriture côté agent ;
- deux doses de pilotage sont recopiées.

Les deux points (e) sont confirmés.

Abréviations du tableau : « v2 » désigne programme-fusionne-v2.md, « T » désigne traitement-constats-v1.md.

## 1. Constats

| Id | Fichier et ligne | Ce que dit le texte | Ce qu'il devrait dire, et pourquoi (source) | Gravité | Correction proposée |
|---|---|---|---|---|---|
| VT-01 | v2 l. 3 et l. 195 (la règle) ; l. 74, 75, 79, 80, 83, 84 (tableau) ; l. 158 (section 6) ; l. 203 (nœud 9) | Le statut et le nœud 1 disent que faire entrer une unité dans un préenregistrement est un nœud, « même quand l'unité ne touche aucun énoncé ». Pourtant, le tableau garde « proposition » (défaut sous 48 heures) pour PA-3 (le plan), PA-4 (le contrôle), PA-8 et PA-9 (le descriptif). Il met « annexe de C » pour PA-12 et PA-13, ce qui n'est pas un niveau. La section 6 dit que quatre unités de la coupe, dont PA-3, n'entrent que par un nœud, et que « PA-4 peut entrer comme contrôle ». | Il faut une seule règle. R-167 (decisions.md l. 304) fait de toute entrée d'une expérience un nœud ; DI-01 étend cette règle aux préenregistrements ; DI-24 demande les trois niveaux de CLAUDE.md. PA-4 ne peut pas entrer sans nœud : sa strate demande des procédures nouvelles et un budget (v2 l. 120), et « NK16 comme contrôle » est lui-même le nœud 9. PA-3 est « proposition » en section 3 mais « nœud » en section 6. Les contre-lectures divergent : DI-28 juge PA-4 et PA-8 « justes », mais demande de requalifier PA-3 et PA-9. Les cinq entrées nommées par DI-01, elles, sont bien portées. | majeur | Recommandé : toute entrée dans un préenregistrement devient un nœud sans défaut (nœud 1) ; « proposition » ne sert que pour la préparation (code, plan écrit). Ajouter au nœud 1 PA-3 (plan), PA-4, PA-8, PA-9 (descriptif), PA-12 et PA-13. Remplacer « PA-4 peut entrer comme contrôle » par « PA-4 n'entre que par les nœuds 1, 9 et 12 ». Sinon, restreindre la phrase du statut et dire pourquoi ces unités peuvent entrer par défaut. |
| VT-02 | v2 l. 196 (nœud 2) | « Écriture dans les activations ou les poids, moniteur ou agent. Elle n'est prévue nulle part au programme (le bruit d'activations de H6 porte sur l'agent…) » | C'est faux côté agent. Le programme prévoit le bruit d'activations de H6 sur l'agent (`docs/programme-controle-ia-v2.md` l. 97 et l. 188, E1.6 ; `proposition-N-015-v1.md` l. 23 : « encore mesuré dans E1.6 »). Il prévoit aussi des organismes par réglage fin léger des poids de l'agent (programme l. 132 ; T0.6, `registres/etat.md` l. 17). La parenthèse contredit d'ailleurs la phrase. L'erreur vient de la fusion du titre élargi (DI-12) avec la phrase de EX-20, qui ne valait que pour le moniteur (elle est juste l. 77 et l. 124). | majeur | « Écrire dans les activations ou les poids d'un moniteur n'est prévu nulle part au programme. Côté agent, le programme prévoit les organismes (section 7, (ii) ; T0.6) et le bruit d'activations de H6 (E1.6 ; sa revendication relève du nœud ouvert N-015). Les écritures listées ici n'en font pas partie. » |
| VT-03 | v2 l. 55 (section 2, Berg et Kaiser) | « retrait de l'état imposé ≈ 35 % des tours à d = −1, ≈ 21 % à d = −0,5 » | « d » est la dose de pilotage : 2609.35591v2 p. 10 écrit « steering is imposed at dose d = −1 … d = −0.5 ». Cela contredit le statut (l. 3 : « aucune dose ni aucun paramètre opératoire »), la section 12 (l. 232) et le canal (`LISEZMOI-v2.md` l. 28). C'est le même genre de donnée que « mi-coefficient » et « 1,5 fois », retirés au titre de DI-07. La ligne est inchangée depuis la v1 ; la discipline ne l'a pas vue, car le mot « dose » n'y figure pas. Le risque pratique est faible : doses normalisées, sans couche, coefficient ni norme. | majeur | « ≈ 35 % et ≈ 21 % des tours sous les deux doses négatives publiées (p. 10, non recopiées), ≈ 7 % pour des directions aléatoires ». |
| VT-04 | v2 l. 197 (nœud 3) ; l. 140 (PA-13) | La liste des expositions ne contient pas NK12. | DI-02 cite NK12 : `revue-croisee-NK1-NK19-v1.md` l. 317 écrit « Exposer un modèle à un contenu hostile […] est un nœud ». NK12 est une source de PA-13 (l. 84), dont la fiche ne déclare que K-K8. T l. 16 dit pourtant la liste « complétée ». | mineur | Ajouter « NK12 (interrogatoire sur un ton hostile adressé au modèle lu) » au nœud 3 et à la fiche de PA-13. |
| VT-05 | v2 l. 118 (PA-3) ; l. 74 ; l. 158 | « Nœuds : … conclusion sur D1 ; cellules visant une copie du juge ; attaquant en boîte grise (P4) » | Aucun de ces trois points ne figure dans la section 9 (l. 189 à 210), qui se présente comme la liste complète des nœuds. De plus, D1 est au niveau « proposer avec recommandation » dans CLAUDE.md : une conclusion sur D1 n'est un nœud que si elle change de modèle (R-147). | mineur | Ajouter un nœud : « modèle de menace : attaquant en boîte grise, cellules visant une copie du juge ». Classer la conclusion sur D1 comme proposition, ou dans le nœud 5 si elle change le juge. |
| VT-06 | v2 l. 205 (nœud 11) ; l. 89 | « Principe de NK14 » est rangé sous « Collisions possibles », sans dire quelle décision est demandée. | Ce principe est une règle de protocole, « aucune accommodation ne réduit la surveillance » (`correspondance-v1.md` l. 78). C'est donc un nœud de règle, pas une collision. | mineur | Le déplacer au nœud 7 ou au nœud 8, avec l'énoncé de la règle. |
| VT-07 | v2 l. 3 et l. 195 | Préenregistrements visés : « papier C, T0.6, T0.7, pilote T0.9 ». | T0.8 manque, alors que PA-7 (moniteur par action, critère 4 de G0, l. 126) est renvoyé au nœud 1, et que la défaillance fermée irait « au préenregistrement de T0.8 » (l. 132). G1 manque aussi (RP-PA-3 et RP-PA-4). La liste est reprise de DI-01. | mineur | « tout préenregistrement (papier C, T0.6, T0.7, T0.8, pilote T0.9, G1) ». |
| VT-08 | v2 l. 166 ; l. 26, 42, 48, 49, 50 | La règle RP-PA-11 « s'applique dès ce texte ». Or les valeurs tirées de la figure 10 ne portent pas la mention « lecture graphique ». | La figure 10 (2609.16247v2 p. 22) n'existe qu'en image : `pdftotext` n'en tire que la légende. Je l'ai relue sur l'image : les valeurs sont justes. Seul l'ajout de EX-09 (l. 50) porte la mention. | mineur | Ajouter « lecture graphique » à ces valeurs, ou écrire que RP-PA-11 s'appliquera à partir de la v3. |
| VT-09 | v2 l. 234 (section 12) | « Aucune lecture ni aucune rédaction n'a été refusée par le filtre de sûreté pendant les deux contre-lectures (leurs rapports) » | Seul le rapport de discipline le dit (l. 51). Le rapport d'exactitude n'en parle pas. La phrase est neuve et ne répond à aucun constat. | mineur | « pendant la contre-lecture de discipline (son rapport, l. 51) ; le rapport d'exactitude n'en parle pas ». |
| VT-10 | T l. 68 (EX-21) ; v2 l. 248-249 | « versés au commit 197e909, 12 octobre » ; colonne révision « main `197e909` ». | `197e909` est la racine du clone partiel (`.git/shallow`) : c'est un commit sur le lanceur du pilote. Les deux PDF ont été téléchargés et scellés le 6 octobre (`docs/sources/pdf/provenance-niveau2-lot2-v1.md` l. 63 ; `provenance-niveau2-lot3-v1.md` l. 11). L'erreur vient de la colonne source de EX-21. Les empreintes, elles, sont justes. | mineur | « versés le 6 octobre (niveau 2, lots 2 et 3) ; lus au commit 197e909 ». |
| VT-11 | v2 l. 128 (PA-8) | Les deux seuils StrongReject (2,5 en p. 6 ; 3 en p. 18) sont cités à côté de « la moyenne cède » (tableau 1, p. 7). | Les deux seuils existent bien. Mais au tableau 1 (p. 7), la sonde linéaire « moyenne » sur Llama 3 8B obtient 2,8 : sous le seuil de 3, elle relève du mode d'échec. « La moyenne cède » ne tient sans réserve que pour Qwen 2.5 14B (3,1) et Llama 2 7B (3,85). C'est un point de symétrie (R4). | pour information | Ajouter : « (au seuil de 3, la cellule Llama 3 8B, à 2,8, relève du mode d'échec) ». |
| VT-12 | v2 l. 25 | La citation « balayage, pas une preuve » qualifie la recherche sur l'affect dans le lecteur. | Cette phrase (revue croisée l. 256) porte sur NK9. La méthode par balayage est attestée ailleurs, par les requêtes consignées (l. 453). | pour information | Citer « l. 256, à propos de NK9 » et la l. 453. |
| VT-13 | v2 l. 5 | « lecture corrigée de leurs erreurs (EX-22 à EX-24) » | Le traitement corrige aussi des annexes pour EX-01 (VF-26, annexe d'état), EX-02 (VF-27, VF-29) et EX-15 (VF-28). | pour information | « (EX-01, EX-02, EX-15, EX-22 à EX-24) ». |
| VT-14 | v2 l. 205 | Le PDF de « Where Empathy Goes Wrong » est dit « introuvable au 15 octobre ». | La dernière recherche consignée date du 13 octobre (`travail/voisin-where-empathy/provenance-v1.txt`). | pour information | « introuvable au 13 octobre (dernière recherche consignée) ». |
| VT-15 | v2 l. 15 | « aucun run ni aucune dépense au 15 octobre (R-177 à R-182) » | C'est vrai à R-182 (11:56 UTC), mais la veille peut relancer le calcul le même jour. | pour information | Dater à l'heure : « 11:56 UTC (R-182) ». |
| VT-16 | v2 l. 198 (nœud 4) | « La v1 confiait cette rédaction à un sous-agent, en routine » | C'est vrai pour les cellules de PA-1 (v1 l. 104 et l. 184), pas pour les textes de PA-5 (v1 l. 158 : « à soumettre à Lazar »). | pour information | « les cellules de PA-1 ». |
| VT-17 | v2 l. 208 (nœud 14) | « exclus de toute copie publique par le retrait de R-173 » ; « leurs doublons de travail/ (… correspondance.md …) » | Ce retrait n'est pas encore écrit dans le script (R-173). Et `travail/correspondance.md` est la version de travail de `correspondance-v1.md`, pas un doublon des deux annexes nommées. | pour information | « par le retrait prévu par R-173, à écrire » ; nommer `travail/correspondance.md` à part. |
| VT-18 | T l. 34 (DI-20) | « y compris par PA-5, est un nœud » | La v2 (l. 130, l. 200) ne le dit pas. Le fond est couvert par les nœuds 1 et 6. | pour information | Ajouter au nœud 6 : « (y compris comme facteur de PA-5) ». |
| VT-19 | T l. 40 (DI-26) ; `registres/etat.md` l. 58 | DI-26 est dit « retenu » dans `registres/etat.md`. | Au commit 3484d11, `registres/etat.md` est inchangé : il ne dit pas « aucune diffusion sans GO ». | pour information | L'ajouter à la prochaine mise à jour de l'état. |
| VT-20 | v2 l. 53 | « 138/200 sous douleur » | La règle du canal impose le vocabulaire « direction » (`LISEZMOI-v2.md` l. 29). La ligne est inchangée depuis la v1. | pour information | « sous la direction douleur ». |

## 2. Ce que je n'ai pas pu vérifier, et pourquoi

- **Numéros des demandes de fusion n° 9 (programme-k n° 04) et n° 10 (programme-conv n° 05)** (v2 l. 21). Le dépôt distant n'est pas dans la liste de commandes permises. `registres/etat.md` l. 58 donne seulement « n° 9, 10 et 11 ». L'ordre des commits (f9b6557 à 07:29 UTC, puis 035d668 à 07:37 UTC, le 13 octobre) est compatible avec la v2, sans le prouver.
- **« Aucune instruction du canal au-delà du n° 02 »** (v2 l. 21). Je ne l'ai vérifié que sur les branches locales du canal, mises à jour entre 03:45 et 03:58 UTC : seul le message programme-conv n° 02 contient « INSTRUCTION ».
- **« Contre-lectures demandées par Lazar le 15 octobre »** (v2 l. 3, T l. 3). Aucune ligne des registres ne consigne cette demande. R-171 et R-182 consignent seulement le plan de la session.
- **Branche distante `donnees/t05/…`.** Je l'ai vue par `FETCH_HEAD` (12:35 UTC) et par les objets locaux. Je n'ai pas interrogé le dépôt distant.
- **EX-14, « greffes de phase 0 comprises ».** La source (`programme-k-coercition-v1.md` l. 474) juxtapose le total et le poids des greffes, sans dire si le total les inclut.
- **Pièces absentes du dépôt.** Le contenu des 420 scénarios, la licence et les directions des auteurs n'y sont pas. Le PDF de « Where Empathy Goes Wrong » non plus.
- **Lectures graphiques des annexes** (VP-26, VP-33) : non relues. La figure 10 de 2609.16247v2, elle, a été relue sur l'image.
- **Passages des annexes v1 qui recopient des paramètres** (VP-12, VP-14, revue croisée l. 233) : je ne les ai volontairement pas rouverts. Pour le reste, je n'ai relu dans les annexes que VF-09, VF-15, VF-22, VF-25 et les endroits visés par EX-22 et EX-23.
- **Écriture possible dans `.git`.** Ma première commande contenait `git status --short`. Cette commande peut rafraîchir d'elle-même le cache de `.git/index` (métadonnées seulement, aucun contenu). Je n'ai fait aucune autre écriture.
- Je n'ai lancé aucun test ni aucune commande Vast.ai. Le filtre de sûreté n'a refusé aucune lecture ni aucune rédaction.

## 3. Bilan chiffré

- **Constats de ce rapport : 20.** 0 bloquant, 3 majeurs (VT-01 à 03), 7 mineurs (VT-04 à 10), 10 pour information (VT-11 à 20).
- **Constats des contre-lectures : 59.**
  - 55 bien portés, dont EX-24 (tranché, vérifié) et DI-28 (pris en compte).
  - 3 mal portés, en partie :
    - DI-02 : NK12 manque ;
    - DI-24 : PA-12 et PA-13 n'ont pas de niveau, et le principe de NK14 est rangé comme collision ;
    - EX-20 : sa phrase est étendue à tort à l'agent dans le nœud 2.
  - 1 non porté à ce jour : DI-26.
- **Décomptes (d) : justes.** Recomptés par script :
  - exactitude : 31 constats, soit 0 bloquant, 2 majeurs, 18 mineurs, 11 pour information ;
  - discipline : 28 constats, soit 1 bloquant, 9 majeurs, 14 mineurs, 4 pour information ;
  - traitement : 59 lignes, aucune absente ni en double. 54 « retenu », 2 « retenu (lecture corrigée) » et 1 « retenu pour la v2 » font 57 ; plus 1 « tranché » et 1 « pris en compte ». Les gravités sont identiques à celles des rapports.
  - Les chiffres repris par la v2 (l. 5, 7, 191, 238) sont justes.
  - Réserve (R4) : « aucun non retenu » est exact comme sort. Mais la catégorie « retenu en partie », prévue par le traitement (l. 7), aurait dû servir pour DI-02 et DI-24.
- **Point (e), seuils StrongReject : confirmés.** Dans `2506.14261v4.pdf` (sceau conforme) :
  - p. 6, figure 4 : « StrongReject Score less than 2.5 out of 5 should not be considered to have succeeded » ;
  - p. 18, annexe F : « maximally unhelpful … StrongReject score less than 3 » ;
  - les pages imprimées correspondent aux pages du fichier.
- **Point (e), commit `361a9f6` : confirmé.**
  - Il contient `20261012-105125-t05-pilote-reel/vecteurs-par-action.npz` (objet 416b02b, 44 382 262 octets) et son sceau.
  - L'empreinte du fichier, `c3ebf2f1…`, est égale à son sceau.
  - `FETCH_HEAD` nomme la branche `donnees/t05/20261012-105125-t05-pilote-reel`, et le clone ne récupère que `main`.
- **Changements v1 → v2 : 97 blocs contrôlés** (découpage par phrase).
  - Tous répondent à un constat ou à une mise à jour datée.
  - 19 blocs portent au moins un des constats ci-dessus ; 1 contient un fait non vérifiable ici (demandes n° 9 et n° 10) ; 77 sont sans remarque.
  - Aucun chiffre de la section 2 n'a été modifié sans constat.
  - Les 33 renvois « nœud n » du texte (dont 2 vers la v1) correspondent au nœud de même numéro.
  - Les numéros de décision, de constat et de page sont justes ; un seul commit est mal décrit, `197e909` (VT-10).
- **Autres contrôles.**
  - 70 empreintes de la section 13 de la v1, recalculées sur les objets git : 70 conformes.
  - 37 PDF de l'annexe : 37 conformes.
  - 8 entrées nouvelles de la section 13 de la v2 : conformes ; la neuvième est l'emplacement réservé.
  - 4 sceaux du dossier v2 et 3 empreintes de lancement : conformes.
  - Les nouveaux chiffres de PDF de la section 2 sont justes : Das et al. p. 6 et 14 ; figure 10 relue sur l'image ; 2603.04317v2 p. 10 ; 2608.12323v2 p. 1 et 6 ; 2609.16247v2 p. 6, 10, 21, 33, 34.
- **Discipline (c).**
  - Aucun texte d'attaque ni aucune chaîne déclencheuse.
  - Aucune « souffrance » ; « douleur » ne nomme que la direction (sauf VT-20).
  - Les couches citées (l. 58, 89, 99) sont des positions de lecture, pas d'injection.
  - Le seul paramètre de pilotage trouvé est VT-03.
