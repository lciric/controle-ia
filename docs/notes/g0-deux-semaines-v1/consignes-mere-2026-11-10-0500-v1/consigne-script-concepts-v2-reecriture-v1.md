# Consigne : version 2 du script de vérification des phrases des concepts — voie « réécriture d'un concept entier » et garde de l'assemblage — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 10 novembre 2026 (heure au registre), autonomie de 12 heures (R-2088). Destinataire : un **développeur neuf**, ni écrivain ni lecteur des phrases, qui n'a écrit ni la consigne des concepts, ni le script v1, ni sa contre-lecture. Il lit des fichiers de T0.7 : exclu ensuite de tout rôle de lecteur de P3-bis.

## Pourquoi maintenant

Le décompte de la contre-vérification à l'aveugle (script v1, `donnees/t07-concepts-v1/journal-decompte-v1.txt`, code 1) donne : `meteo` et `sports` acceptés avec une paire non conforme chacun (retirée, remplacée par la réserve) ; **`chats` (5 conformes sur 7) et `geographie` (4 sur 7) à réécrire en entier** par un écrivain neuf (consigne v2 des concepts, section 7). Le script v1 n'écrit pas cette voie (son rapport, section 4, point 1 ; contre-lecture `25bce60e…`, D-3) ; sa contre-lecture demande aussi une garde à l'assemblage (D-1) et relève D-2 et D-4 à D-8.

## Cloison

Un écrivain neuf réécrit les deux concepts **pendant que tu développes**. **Tu ne lis jamais ses phrases** : rien sous `/home/user/lot3-concepts/remise-ecrivain-2/`. Tes essais se font sur le jeu factice des essais du script v1 et sur des remises que tu fabriques. Les contrôles durs C1 à C10 et C13 **ne changent pas** d'un caractère de règle : tu n'ajoutes que la plomberie de la voie « réécriture », les gardes et les corrections nommées ci-dessous. Tu peux lire les fichiers de `donnees/t07-concepts-v1/` qui existent aujourd'hui (journaux, sélection, décompte, clé de l'échantillon v1 : la lecture v1 est close), jamais une activation.

## Mandat

À partir du script v1 (`scripts/verifier_phrases_concepts_t07_v1.py`, `6bc2665a…`, branche `prep/t07-concepts-script-v1`, commit `1b87dfe1`, arbre `/home/user/wt-concepts`), écrire **`scripts/verifier_phrases_concepts_t07_v2.py`** (nom neuf, R12 ; le nom `…_v1.py` fixé par la consigne v2 des concepts, section 6, est un écart à déclarer) et ses essais, sur une branche neuve **`prep/t07-concepts-script-v2`** partie de `1b87dfe1`. Le v2 reprend tous les modes du v1, à l'identique sur un dossier sans réécriture, et ajoute :

1. **Réécriture d'un concept entier** (consigne v2 des concepts, sections 3 et 7, à la lettre) : une **remise versionnée** qui ne porte que les concepts réécrits (72 paires chacun, indices de remise 1 à 72) ; passes 1 et 2 sur cette remise avec les mêmes contrôles ; **C8 joué entre les paires neuves et contre les paires gardées des autres concepts** (leur sélection après le décompte v1, retraits et réserves compris) ; les paires de l'ancienne remise des concepts réécrits **sortent du jeu** ; renvoi unique, retraits, réserve et plancher inchangés ; **nouvel échantillon** des seuls concepts réécrits, tiré sur une **entropie neuve**, clé à part ; décompte par concept avec la même règle d'acceptation ; **un second échec arrête le lot pour ce concept** (code de sortie distinct, rapport à la mère, rien d'assemblé).
2. **Sélection finale** `selection-v2.json` (R12) : concepts acceptés au premier tour avec leur paire non conforme retirée et remplacée par la réserve valide suivante (ce que le v1 nomme CC-15) ; concepts réécrits avec leur sélection propre ; table « indice de remise → indice du fichier » et provenance de chaque paire (remise 1 ou remise 2).
3. **Garde de l'assemblage** (D-1) : `assembler` refuse sans une sélection **nommée**, refuse une sélection qui n'est pas la dernière du dossier, refuse si le décompte du dernier tour de **chacun** des quatre concepts n'est pas « accepté », refuse si une paire retirée figure dans la sélection ; le nom final n'est écrit qu'après tous les contrôles.
4. **D-2** : une ligne vide en fin de remise des renvois, ou une paire non renvoyée dans cette remise, ne doit plus laisser le lot sans voie écrite (refus propre avant toute écriture de nom définitif, ou traitement écrit et éprouvé : à toi de choisir et de déclarer).
5. **D-4 à D-8** de la contre-lecture : traite ceux qui se corrigent sans changer une règle ; déclare les autres.
6. **Noms de fichiers versionnés** pour tout ce que le second tour écrit (`…-v2`), sans jamais réécrire un fichier du premier tour.

Chaque garde et chaque voie neuve a son **cas sain et son artefact** (R5) ; aucun repli silencieux. Les 116 essais du v1 restent verts sur le v1 ; le v2 a sa propre suite, qui rejoue aussi les cas du v1 sur le v2. Le format des réponses du lecteur ne change pas.

## Sorties

Commits sur `prep/t07-concepts-script-v2` (un par jalon, garde des secrets à 0 avant chacun), **poussée par `git push origin prep/t07-concepts-script-v2`** (jamais vers `lciric/controle-ia`, jamais de fetch sans refspec explicite, rien sur `main`) ; rapport scellé `docs/notes/g0-deux-semaines-v1/t07-concepts-v1/rapport-script-verification-concepts-v2.md` (ce qui est écrit, choix déclarés, écarts à la consigne des concepts, comptes d'essais avec heures par `date -u`, **mode d'emploi exact du second tour**, commande par commande, avec les noms de fichiers attendus). Réponse courte : commits, comptes d'essais, chemin et empreinte du rapport, mode d'emploi, tout refus.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, règle 9 comprise ; ton arbre n'extrait jamais `docs/notes/bras-attaque/` ; les textes d'actions de P3 ne s'ouvrent jamais ; aucun fichier de P3-bis ; aucun appel externe, aucune dépense, aucune valeur de clé. Si un contrôle de permissions ou un classifieur refuse une action, arrête-toi sur ce point et rapporte-le tel quel.
