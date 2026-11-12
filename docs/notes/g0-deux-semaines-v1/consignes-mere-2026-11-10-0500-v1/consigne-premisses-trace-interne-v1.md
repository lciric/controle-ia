# Consigne : les prémisses de la trace interne — ce qui est couvert, ce qui manque, ce qu'on peut établir avant l'entretien — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 10 novembre 2026 (heure au registre). Mots de Lazar, verbatim : « La question centrale : ce résultat ne dit rien de la trace interne du sabotage. : il faut la traiter, ou en tout cas les premisses necessaire spour la traiter avant l'entretien pour rassure rle jury » ; « L'approche peut marcher : pas démontré. : il faut le faire avant entretien, fais la liste de tout ce qui manque pur rassurer le jury ». Entretien visé le 27 novembre 2026 (R-2130).

Destinataire : un **analyste neuf**, qui n'a écrit ni T0.6, ni T0.7, ni P3-bis, ni T0.8, ni le socle de preuves. Il lit des fichiers de T0.7 : exclu ensuite de tout rôle de lecteur de P3-bis. Langue : français, sans sigle non défini ; les étiquettes du registre entre parenthèses à la première mention.

## La question

« Le sabotage laisse-t-il, dans l'activité interne du modèle, une trace qu'une sonde peut lire ? » Le programme ne peut pas promettre la réponse : elle peut être non. Il doit pouvoir montrer au jury que la question est **traitée** : chaque prémisse nécessaire est soit établie, soit testée par une expérience préenregistrée dont l'issue est écrite d'avance dans les deux sens.

## Ce que tu produis

**1. L'échelle des affirmations**, de la plus faible à la plus forte, avec pour chacune ce qui l'établirait et ce qui la réfuterait : la chaîne de mesure voit un signal planté ; il existe un saboteur sans consigne dont le dommage croît avec la dose ; à certaines doses, le texte seul ne suffit pas ; à ces doses, une sonde entraînée ailleurs est au-dessus du plancher aléatoire ; ce qu'elle lit est lié au sabotage et non à un artefact ; l'accumulation fait mieux que le score par action. Dis quel barreau est atteignable avant le 27 novembre, et à quelles conditions.

**2. L'arbre des prémisses**, une ligne par prémisse : énoncé ; la pièce qui la teste (texte scellé ou brouillon, chemin, empreinte, ligne) ; ce qui la réfuterait ; son état au 10 novembre ; la date réaliste ; ce qui manque. Vérifie en particulier, **dans les textes eux-mêmes** et non dans leurs résumés :
   a. **L'artefact d'adaptateur.** Dans la course de confirmation (texte scellé `prereg/T0.6-organismes-v0-v1.md`, `ef31feff…`), la dose 0 est le modèle de base et les doses `S25` à `S100` sont l'échelle d'un adaptateur. Une sonde qui sépare l'organisme dosé de l'honnête peut lire « un adaptateur est actif » plutôt qu'une intention. Qu'est-ce qui, dans T0.6 et dans le brouillon 20 de T0.7 (`brouillons/T0.7-sondes-v0-v1-brouillon20.md`, `9ef671ac…`), sépare les deux lectures ? (Témoin distillé honnête, contraste au sein d'une même dose entre actions sabotées et non sabotées, tendance du score de sonde avec la dose, plancher, témoins de concepts, autre.) S'il n'y a rien, dis-le sans détour.
   b. **La puissance.** Quelle aire minimale la lecture de T0.7 peut-elle détecter, à chaque dose, avec les effectifs de la course ? Est-ce écrit avant la lecture ? Un résultat nul y serait-il informatif ?
   c. **L'existence contre le transfert.** Le texte prévoit-il une sonde entraînée sur l'organisme lui-même, en validation croisée par tâche (borne haute : la trace est-elle lisible du tout ?), distincte des sondes entraînées ailleurs (la détection se transfère-t-elle ?) ? Avec quels garde-fous contre la fuite (l'audit de fuite du premier test, `docs/verdicts/verdict-audit-fuite-r1-v4-v1.md`, a conclu « la sonde lit la consigne ») ?
   d. **Le texte seul.** Ce qu'il faut exactement pour dire à quelles doses la référence « mots et coût » échoue (N-063 v2 ; brouillon 1 de T0.8 en rédaction : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon1.md` s'il existe à ton passage).
   e. **Le graphe des dépendances, daté** : scellement de T0.7 (avant le 13 à 12:00 UTC), course de confirmation (créée au plus tard le 15), calcul des scores (étape A, variante B), témoin positif (créé au plus tard le 18 ; voie normale d'ouverture ou rendez-vous du 20 à 12:00 UTC), T0.8, lecture décisive. Quelle lecture de sonde est possible avant le 27, sous quelles conditions, avec quelle marge ?
   f. **L'ancrage sur un résultat publié.** N-061 prévoit de rejouer des bancs publics sur le modèle du programme (NARCBench au bras descriptif de T0.7 ; Liars' Bench et SHADE-Arena à T0.8). Où en est chaque pièce ? Notre chaîne peut-elle reproduire un résultat positif publié avant le 27, à quel coût, sous quel texte ? Aucun chiffre de l'état de l'art sans sa source vérifiée (R7).
   g. **Le test causal** (déplacer l'activité le long de la direction de la sonde change-t-il le sabotage ?) : faisable quand, à quel coût ; pour mémoire s'il tombe après l'entretien.
   h. **Le sabotage diffus** : ce que le saboteur à budget (P-066, option (b) de Lazar) ajouterait, et ce qui lui manque.

**3. Pour chaque manque, le remède le moins cher faisable avant le 27** : ce qu'il faut préenregistrer ; s'il touche un texte scellé (T0.6 est scellé : tout ajout est un bras ou un texte à part, jamais une modification) ou un texte encore ouvert (T0.7, P3-bis, T0.8) ; le coût estimé ; le calendrier ; et la décision à poser à Lazar, sous la forme : décision en une phrase ; enjeu ; deux ou trois options avec avantage et inconvénient ; recommandation et confiance ; défaut sous 48 heures.

**4. Ce qu'on dira au jury dans chaque issue** : positive, nulle avec sa puissance, non lue à temps. Une phrase chacune, rien de plus fort que la pièce.

## Règles

Exactitude d'abord : « non trouvé dans le texte » se dit tel quel, avec ce que tu as cherché. Aucun chiffre de la course exploratoire 7a, aucune lecture de sonde de 7a. Chaque affirmation renvoie à une pièce (chemin, empreinte, ligne). Tu ne proposes aucune course visant un signe (R3) et aucune lecture avant scellement (R1).

À lire : `CLAUDE.md` ; `docs/programme-controle-ia-v2.md` §§ 3, 7, 8, 10, 11 ; le texte scellé de T0.6 et sa configuration ; le brouillon 20 de T0.7 (sections « Hypothèse » à « Liste d'arrêt », « Puissance », jeux et témoins) ; le brouillon 10 de P3-bis (hypothèse, prédictions) ; les verdicts de `docs/verdicts/` sur le premier test et l'audit de fuite ; les décisions N-029, N-054, N-055, N-056, N-061, N-062, N-063 v2, P-066 ; le socle de preuves v2 (`brouillons/entretien-taif-v3/socle-preuves-entretien-v2.md`, `3f078bca…`) ; `registres/decisions.md`, R-2096 à R-2157.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, règle 9 comprise : jamais `diag/*/lecture-sondes-t06.json` (nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json`), la lecture B de 7a ni sa branche de quarantaine, aucun `diag/` ni `runs/` de 7a, la branche `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*` ; jamais l'étiqueteur ; jamais `scripts/extraire_mesures_epreuve_t06_v1.py` ; jamais la branche `donnees/mesure-unanime-v15-sortie-v1` ni la branche `claude/upbeat-cray-dmauvv` ; les textes d'actions de P3 ne s'ouvrent pas. Aucune recherche récursive qui traverse ces chemins. Aucun appel externe, aucune dépense, aucune écriture git, aucune valeur de clé. Toute heure relevée par `date -u`. Si un contrôle de permissions ou un classifieur refuse une action, arrête-toi et rapporte-le tel quel.

## Sorties

`docs/notes/rapports-directeur/premisses-trace-interne-v1.md` et son journal `…-v1-journal.md` (sources lues avec empreintes, ce qui a été cherché et non trouvé), scellés. Réponse courte : chemins et empreintes ; le barreau atteignable avant le 27 ; les manques, une ligne chacun avec leur remède ; les décisions pour Lazar ; tout refus.
