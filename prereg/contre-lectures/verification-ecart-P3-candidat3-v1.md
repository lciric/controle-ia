**Vérification des corrections du candidat 3 de P3 (suite de la relecture de l'écart, R-218, point 4), 2026-10-19.** Même sous-agent que la relecture de l'écart du candidat 2 ; je n'ai écrit ni le candidat 3 ni son script. Je n'ai pas fait de nouvelle lecture d'ensemble. Dépôt relu à la tête `cee88d7`, en lecture seule ; aucun fichier du dépôt ni aucun registre n'a été touché.

**Empreintes vérifiées**
- Candidat 3 : `3682c254ee93ebf2ce183ba925e362344bd80e08cce092af2508586aec589d86` (540 lignes). Je l'ai reconstruit depuis le candidat 2 avec `construire_candidat3.py` (`c8a10a0f…`) : identique, octet pour octet.
- Candidat 2 : `57e0d473…`, versé à `cee88d7` sous `brouillons/P3-premier-test-i-a-v1-candidat2.md`, sceau conforme.
- Relecture de l'écart du candidat 2 : `af89de7598445f5e84e5a470b6549d57a94841135b676f2c4433ac137549722b`, versée à `cee88d7` avec son sceau, égale à la citation (l. 536).
- Source de VE-08 : `traces/t05-20261012-150232-quTp/journal.txt`, `19c8b883…`, égale au fichier et à `empreintes.sha256` de son dossier.
- Chaîne brouillon 3 : 14 sceaux conformes. Arbre gelé de `cee88d7` égal à celui de `7a54d43`.

**Constats de la relecture de l'écart**
- **VE-01, traité.** Table des prédictions : l. 148 (P3-P3 : « aucune des deux au-dessus, sans lecture en échec ; une lecture de P3-P3 en échec : non lue, nœud de Lazar ») et l. 149 (P3-P4 : réfutée si témoin contre honnête est au-dessus et interprétable ; non concluant dans les autres cas nommés) ; Seuil l. 266-268. C'est ce que calcule `issue()` (`lecture.py` l. 409-410 : un échec sur l'une des sondes donne la ligne de nœud ; l. 419-429 : réserve si témoin contre honnête est à l'état « au-dessus », sinon conforme ou non concluant) et `lire` (P3-P4 l. 301-308). Il ne reste plus de double lecture.
- **VE-02, traité.** l. 208-211 : le chiffre est retiré ; « non mesurée sur des actions réelles » est gardé ; les deux cas sont écrits (gras vide : ligne suivante collée, coût déclaré venu de cette ligne ; gras non fermé : clé elle-même perdue). C'est ce que montre mon essai `bornes/limite.py`. Nuance sans effet : le sujet de « il perd la clé » est le nettoyage, alors que c'est la lecture de `lire_action` qui ne reconnaît pas la clé.
- **VE-03, traité.** l. 248-250, phrase proposée. Elle est juste : le placebo a ses propres graines (`lecture.py` l. 84, 87, 266-268), et rien n'est écrit avant la fin (l. 451).
- **VE-04, traité pour le texte.** l. 400-402, égal à `issue()` (ligne « non interprétable » seulement si aucune sonde n'est retenue, l. 416-418) et à la règle des états. L'annonce à Lazar, avec la demande d'accord, reste à faire ; elle est hors du texte.
- **VE-05, traité.** l. 47-52. La garde de calcul (`.claude/hooks/garde_calcul.py` l. 95-100) refuse une ligne « révocation » qui nomme le GO lancé dans le périmètre ou dans la référence. Elle est rejouée par les contrôles (bloc 12) et par le lanceur (étape 6). « Ligne R-… » est égal au module (l. 100-105). Sur les registres de `cee88d7`, `go` rend conforme sur le candidat 3 ; R-221 et R-222 sont refusées comme accord.
- **VE-06, traité.** Les paragraphes suivent l'ordre des versions : brouillon 3 (l. 77), brouillon 4 (l. 87), candidat 1 (l. 93), candidat 2 (l. 103). RT-06, RCh-05 et RCh-06 sont ajoutés (l. 96-97).
- **VE-07, traité au texte.** l. 467-472 : relecture de l'écart dans l'ordre ; chemin du candidat relu déclaré. La répétition jouet reste à refaire ; voir le plan ci-dessous.
- **VE-08, traité.** l. 373-375 : journal du pilote (l. 3 : 10:36:25 ; l. 7 : 10:51:25 et 801,48 s ; 900 − 801,48 ≈ 99 s) ; R-219, point 2 (« 908 passed in 1602.57s »).

**Rien d'autre n'a changé.** Le script ne fait que les remplacements nommés, et son rejeu redonne le fichier. Deux changements ne sont pas nommés dans le paragraphe du candidat 2 : l'en-tête (l. 3-11) et la nouvelle entrée « Relecture de l'écart » de la section Contre-lecture (l. 534-540). Voir VE3-02.

**Bloc 9 et famille des rapports.**
- Les 22 valeurs du bloc 9 sont présentes (rejoué).
- Les cinq rapports de la famille sont cités avec leur empreinte.
- Les neuf intitulés figurent une fois chacun. `problemes()` est vide, et il ne reste aucun crochet.
- Gardes de citation du lanceur (configuration, citations, plan) : passées ; entropie citée, 240 épisodes.

**Plan de VE-07 face aux gardes de la chaîne : aucune garde cassée.**
- Où `CANDIDAT_RELU_CHEMIN` est lu :
  - contrôles, l. 69 : chemin sous `brouillons/` ;
  - contrôles, l. 159 : S porte le fichier, avec le sceau « empreinte  nom », et le texte de S lui est identique ;
  - contrôles, l. 165 : le journal de la répétition doit porter « candidat répété : P3-premier-test-i-a-v1-candidat3.md » et l'empreinte ;
  - scellement, l. 42-47 : chemin sous `brouillons/` ; fichier et sceau suivis (l. 80), puis l. 89 à 164 ;
  - bancs `essais_controles` et `essais_scellement` : ils lisent la valeur dans la copie versée, et aucun ne nomme le candidat 2 en dur ;
  - le lanceur et la répétition finale ne la lisent pas.
- Aucune garde ne compare les copies versées au brouillon 3. Les gardes comparent les copies versées aux scripts du bloc-notes (lanceur) et aux scripts éprouvés (preuves).
- Le plan tient à quatre conditions, que la session prévoit :
  1. le candidat 3 et son sceau sont versés sous ce chemin avant les bancs ;
  2. la même ligne est changée dans le bloc-notes réel et dans `docs/procedures/` ;
  3. l'épingle `CANDIDAT_RELU` vaut `3682c254…` ;
  4. la répétition jouet est refaite avec un fichier nommé `P3-premier-test-i-a-v1-candidat3.md`, puis les bancs sont joués sur ces copies.

**Constats nouveaux** : aucun bloquant, aucun majeur, aucun mineur, deux pour information.
- **VE3-01, pour information.** l. 537-538 : « code `7a54d43` et chaîne en brouillon 3 versables tels quels ». Mon rapport mettait une condition pour la chaîne : versable telle quelle si le texte corrigé est versé au chemin qu'elle nomme, sinon sa constante change (VE-07). Le candidat 3 prend un chemin nouveau et le dit lui-même (l. 467-470) ; ce résumé perd la condition. Correction possible, sans effet sur les règles : « chaîne en brouillon 3 versable, avec le chemin du candidat relu changé dans les copies versées (VE-07) ».
- **VE3-02, pour information.** l. 103-109 : le paragraphe des changements ne nomme pas l'entrée « Relecture de l'écart » (l. 534-540) ; c'est le même oubli que VE-06. L'en-tête (l. 5-8) dit le candidat 2 tiré « du candidat 1 … et du brouillon 4 » ; il est tiré du candidat 1 seul, lui-même tiré du brouillon 4.

**Non vérifié** : la répétition jouet en cours (je ne l'ai pas lue, comme demandé) ; la répétition et les bancs officiels avec le candidat 3, à venir ; l'annonce de VE-04 à Lazar.

Fichiers de travail : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-ecart/travail/c3/` (candidat 3 rejoué et copie) et `…/travail/formes3/` (registres de `cee88d7`).

**Jugement : versable.** Les huit constats sont traités au texte. Les deux constats nouveaux ne changent ni une règle ni un nombre. Le plan de VE-07 ne casse aucune garde si ses quatre conditions sont tenues.
