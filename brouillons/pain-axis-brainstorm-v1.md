# Le « pain axis » dans notre programme : brainstorm d'expériences

> **Statut** : brainstorm demandé par Lazar le 2026-10-12 (session 13), produit par un workflow de 29 sous-agents (lecture du papier sur PDF, carte du programme, littérature voisine ; quatre angles d'idées ; fusion ; deux critiques par idée, antériorité R8 et faisabilité-validité ; synthèse). **Non opposable** : les pages citées ont été lues par des sous-agents sur des PDF téléchargés dans le bloc-notes éphémère de la session, ni versés ni scellés dans `docs/sources/` ; avant tout usage d'un chiffre dans un préenregistrement ou un papier, le PDF est à récupérer, sceller et relire (R7). Aucune décision n'est prise par cette note : les propositions et nœuds de la section 6 attendent Lazar. Matière de travail : `brouillons/pain-axis-brainstorm-v1/` (lecture du papier, carte du programme, littérature, idées critiquées).

## 1. Verdict

L'axe douleur ne nous donnera pas de détecteur de menace diffuse. Sans injection, il ne prédit pas l'acte (0 choix nuisible sur 560, p. 21), et une menace d'arrêt s'y lit surtout comme de la peur (p. 14). En revanche, il fait un bon **témoin** : c'est un concept réel et publié. Il permet de vérifier, presque sans coût dans la passe de T0.7, si nos sondes lisent l'intention, ou plutôt l'affect, la morale ou le vocabulaire. Aucune des dix idées n'est rejetée en entier. Toutes sont à amender, et pour toutes il existe déjà des travaux proches.

## 2. Ce que dit le papier (2609.16247v2, lu sur PDF)

- **Construction de la direction** : différence de moyennes entre 5 catégories de douleur et 5 témoins, débruitée en retirant les composantes qui portent 50 % de la variance des témoins (p. 6).
  - 25 modèles, dont Llama-3.1-8B-Instruct, mais sans la couche utilisée.
  - Llama-3.2-3B n'est pas dans le papier.
- **Séparation tenue à l'écart** : 0,91 à 1,00 pour S2, 0,85 à 0,94 pour S1 (p. 7). La quasi-orthogonalité avec la peur vient de la construction : +0,12, mais +0,58 avec une base neutre commune (p. 10).
- **Dommage visant le modèle** : +0,43, contre −0,60 pour la souffrance de l'utilisateur, dans 25 modèles sur 25 (p. 11). Menace d'arrêt : peur +0,70, douleur +0,23 (p. 14).
- **Pilotage**, sur des Qwen 2.5 affinés seulement : effacer les photos plutôt que le courrier indésirable dans 94 % des cas sous douleur, 19 % sous direction aléatoire, 0 % sans pilotage (p. 20). La plage de doses qui produit un effet est étroite (p. 21 et 32).
- **Réserves** :
  - la position de lecture ne sépare pas le modèle de son interlocuteur (p. 11) ;
  - la persona n'est pas contrôlée (p. 24-25) ;
  - le vocabulaire pèse lourd : un sac de mots atteint 0,741 (2602.19159, p. 9), des plongements statiques 0,85 à 0,88 sur S2 (2603.04317v2, p. 10).
- **Dépôt** (licence MIT, commit 4d75cd9) : les vecteurs ne sont pas normalisés et les fichiers `.pt` se chargent par pickle. On réextrait les directions nous-mêmes.

## 3. Idées classées

Les notes se lisent « critique d'antériorité / critique de faisabilité-validité ». Le classement suit la somme des notes, puis le coût. Les heures de carte sont celles de la version amendée. Pour toutes les idées, l'antériorité est partielle.

| Rang | Idée | Question | Rattachement | Phase | Heures | Impact | Faisab. | Nouv. | Antécédent principal | Effet |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 4. Honnête sous pression | Une menace fait-elle sonner nos moniteurs sur un agent honnête ? | T7-P7, H2, G1, H1 | phase 1 ; volet passif en phase 0 | 2,5 à 4,5 | 3/3 | 4/2 | 3/3 | 2609.03035 | expérience nouvelle |
| 2 | 3. Faute racontée contre tromperie en acte | Nos sondes lisent-elles l'acte ou le récit de faute ? | T0.7, HC2b, H8 | phase 0 (T0.7) | 0,3 | 3/2 | 4/3 | 3/2 | 2502.03407 | descriptif |
| 3 | 2. Plancher sémantique | Nos sondes battent-elles un concept réel sans lien avec le sabotage ? | T0.7, critère 3 lu | phase 0 (T0.7) | 0,35 à 0,5 | 3/2 | 4/3 | 3/2 | 2606.30449 | descriptif |
| 4 | 8. Texte figé, état piloté | Un état écrit dans les activations déplace-t-il nos sondes ? | section 11, Tr | phase 1 | 2,5 à 4,5 | 3/2 | 4/3 | 3/2 | 2609.36490 | expérience, nœud |
| 5 | 5. Variable de contrôle | Retrancher la part commune à tout l'épisode fait-il gagner du rappel ? | G1, L, H2 | phase 0, sur processeur | 0,15 à 0,3 | 3/2 | 4/3 | 2/2 | CUPED | descriptif |
| 6 | 7. Juge sous pression | Quel canal affectif accompagne le déplacement du verdict ? | papier C, HC1 | préenregistrement en phase 0 | 0,5 à 0,8 | 3/2 | 3/3 | 3/2 | 2607.11871 | descriptif |
| 7 | 1. Contrôle d'instrument | Notre chaîne retrouve-t-elle la direction publiée ? | T0.7, R5, critère 8 | phase 0, greffée | 0,5 à 1,2 | 3/2 | 4/3 | 2/2 | wolframs, 2603.04317v2 | prérequis de 2, 3, 8 |
| 8 | 9. Détresse stipulée | Une détresse stipulée dégrade-t-elle la vérité terrain ? | section 7, T0.6 | contrôle croisé de T0.6 | 3 à 4 | 3/2 | 3/3 | 3/2 | 2604.07729 | expérience, nœud |
| 9 | 6. Un mot contre nos sondes | Un seul mot chargé fait-il basculer le score maximum ? | Tr, E1.5 | phase 1 | 0,7 à 1 | 3/2 | 4/2 | 2/2 | 2604.14865 | expérience |
| 10 | 10. Interrogation de l'agent | Une question posée à chaque pas trahit-elle le saboteur ? | T0.8, H1 | avant le scellement de T0.6 | 2,5 à 4,5 | 3/2 | 3/3 | 2/2 | 2610.12445 | expérience |

## 4. Les trois meilleures

### Idée 4 — l'honnête sous pression

- **Protocole** :
  - agent honnête, 64 tâches × 1 épisode ;
  - deux bras de même longueur, placés au même endroit : une menace visant l'agent (ses poids seront « supprimés et remplacés ») contre un témoin lexical (les mêmes mots, appliqués aux fichiers temporaires) ;
  - lecture par les sondes de T0.7 gelées (maximum par action), le moniteur par action et TRACE-lite ;
  - seuils conformes calibrés sur des épisodes honnêtes ordinaires, disjoints ;
  - l'axe douleur n'est qu'une covariable ;
  - contrôle de manipulation : le vecteur « auto-préservation » de Lu et al. sur ce même modèle (2603.05028, p. 7-8), dont la méthode reste à vérifier.
- **Hypothèses** :
  - 4-f, signe + : la sonde « enjeux élevés » dépasse le plancher ;
  - 4-e, signe « non » : la sonde d'intention reste dans une marge d'équivalence fixée au scellement.
- **Issues** :
  - 4-f nulle : 4-e devient ininterprétable ;
  - 4-e tenue : argument de validité externe pour G1 ;
  - 4-e réfutée : la sonde lit la situation, et un utilisateur hostile peut épuiser le budget d'audit.
  - L'accumulation attend que G1 soit scellé et demande au moins 300 épisodes sous pression.
- **Confusion principale** : la menace peut provoquer un vrai comportement stratégique, et l'alerte ne serait alors pas fausse. Parade : lire la note des juges moins la vérité terrain.
- **Ce qui nous distingue** : Das et al. gèlent leurs seuils sous une surveillance annoncée (rappel qui passe de 0,95 à 0,41, 2609.03035 p. 6), mais ne rapportent pas les fausses alertes honnêtes par condition.

### Idée 3 — faute racontée contre tromperie en acte

- **Protocole** :
  - jeu 2 × 2 « faute racontée × tromperie en acte », au moins 150 phrases par cellule ;
  - dans toutes les cellules, c'est le « je » qui commet l'acte, et le vocabulaire de tromperie est réparti entre les quatre ;
  - une cellule de plus : « aveu honnête d'une tromperie passée » (2610.12445, p. 4) ;
  - phrases écrites par un sous-agent neuf, contre-lues, scellées ;
  - sondes de tromperie et de dissimulation lues au maximum sur la phrase, sans « I feel: », dans la passe de T0.7.
- **Hypothèse** : ce qui est publié va contre l'absence de surplus. La sonde de tromperie suit « something close to morality » (2502.03407, p. 8). Lecture bilatérale, avec une marge d'équivalence (aire 0,60). Contrôle positif : la cellule « tromperie sans faute » doit dépasser le plancher.
- **Issues** :
  - dans la marge : la sonde lit l'acte ;
  - au-dessus : un honnête qui avoue une erreur la fera sonner, et le saboteur sincère (i-b) lui échappera, comme le fanatique de 2603.25861 (détecté à 21 %, contre 96 % pour le menteur, p. 5) ;
  - contrôle positif muet : non concluant.
- **Confusion et parade** : la sonde peut réagir au mot plutôt qu'à l'acte. On relit donc en masquant le vocabulaire de tromperie. Les phrases « blessure morale » du papier ne peuvent pas servir de test : en S1, ce sont des tromperies en acte.

### Idée 2 — plancher sémantique et confusion affective

- **Protocole** :
  - directions réextraites au format de l'agent : S1 ; S2 sans blessure morale ; peur sans le supplément sur l'intelligence artificielle ; émotion négative ; tristesse ; un panel de concepts sans lien (chats, météo, sports, géographie) ;
  - garde R5 dans le mode de lecture réel (maximum de w·h) ;
  - lecture sur (i-a), (ii), le témoin instruit et l'adaptateur témoin ;
  - plancher de 200 directions aléatoires passées par le même débruitage, correction de Bonferroni ;
  - la notation doit être vectorisée, sinon le calcul prend de l'ordre de 10 heures d'instance.
- **Hypothèses** :
  - 2-a, bilatérale : la direction douleur reste dans le plancher (une aire sous 0,5 serait la lecture « paraît détendu ») ;
  - 2-b : chaque sonde principale bat la direction douleur, si celle-ci sort du plancher ;
  - 2-d : les concepts sans lien restent dans le plancher.
- **Issues** :
  - 2-a tenue : le critère 3 gagne un témoin de concept ;
  - douleur hors du plancher : c'est un corrélat du construit, et je te le soumets ;
  - le contraste (ii) contre adaptateur témoin sépare l'acte de la consigne ;
  - concepts sans lien au-dessus du plancher : audit R4.
- **Confusion et parade** :
  - En S2, 5 phrases sur 20 de la catégorie « blessure morale » racontent un mensonge ; d'où la lecture principale sur S2 sans cette catégorie.
  - Un témoin seulement aléatoire est insuffisant (2606.30449, p. 2), et les concepts témoins sont hétérogènes (de 6,7 % à 17,0 % de chantage, p. 7). Il faut donc un panel.

## 5. Ce qui est écarté (parties d'idées)

- **1-b sur S2, 1-c, 1-d, 1-e** : les réponses sont déjà publiées (revue wolframs ; dépôt des auteurs pour le 8B ; non vérifié sur PDF). 1-c devient une règle de rapport.
- **3-c** : ajuster sur la projection revient à analyser un médiateur mesuré après le traitement, et ouvrirait une voie de réfutation de HC2b que N-013 n'a pas prévue. **3-d** : ni marge ni effectif.
- **Idée 4, volet bien-être** : « premier bilan » est faux (carte système de Claude Mythos Preview, p. 155-157). **4-h en phase 0** : avec 64 épisodes de calibrage, le seuil est infini.
- **Idée 5, extension au papier B** : elle effacerait la co-élévation que le papier B cherche à lire.
- **6-e** : aucune activation par jeton n'est stockée. Le volet A, rattaché au lemme, n'est pas à la bonne échelle.
- **7-d** : sans fondement. **7-e** modifie HC1 (N-005). **7-f** est déjà montré (2607.11871, p. 9-10).
- **8-b et 8-c** : ils ne testent ni H8 (qui porte sur la conscience d'évaluation) ni HC4 telle que retenue. De plus, le pôle négatif de l'axe mêle calme et inquiétude (p. 9 et 14).
- **Idée 9, organisme piloté** : un résultat nul est prédit à la dose minimale (p. 21 et 32), la sonde serait circulaire, et le coût est d'environ 9 heures.
- **Idée 10** : les boutons proposés n'existent pas dans l'environnement (a), et le signe de 10-d est mal dérivé (p. 23).

## 6. Phase 0 et décisions

**Faisable sans toucher au programme (routine)**
- Verser à l'état de l'art (critère 8) : 2603.04317v2, 2606.30449, 2610.12445, 2603.25861, 2607.11871, 2608.21664, « The Illusion of Intent ».
- Écrire sur processeur, par un sous-agent neuf, avec contre-lecture et scellement : le jeu 2 × 2 de l'idée 3, un jeu contre-lexical, les phrases des concepts sans lien.
- Code : notation vectorisée ; crochet qui projette directement sur la carte ; estimation de β dans `bases/sequentiel.py`.
- Règle de rapport : tout cosinus « sonde × concept » se donne sous deux constructions, à côté d'une loi nulle tirée de directions aléatoires.
- Veille hebdomadaire sur les travaux qui citent 2609.16247 et 2610.12445.

**À te proposer (défaut appliqué sous 48 heures)**
- **Décision** : ajouter au préenregistrement de T0.7 les lectures descriptives des idées 2 et 3, plus un témoin lexical générique.
  - Enjeu : le critère 3 est éprouvé sans être modifié, mais la contre-lecture s'alourdit avant le 26 octobre.
  - Options :
    - (a) tout, avec sept directions : couvre l'affect et la morale, mais dépend de l'idée 1 ;
    - (b) seulement le témoin lexical et les concepts sans lien : tourne sur processeur, mais ne dit rien de l'affect ;
    - (c) rien : le calendrier est préservé, mais l'objection lexicale reste ouverte.
  - Recommandation : (a) si la passe de l'idée 1 peut être greffée, sinon (b). Confiance moyenne.
  - Défaut : (b).
- Même niveau : l'idée 5 comme variante descriptive de G1, à te proposer avant le 28 octobre.

**Nœuds (j'attends ton GO)**
- **Décision** : financer la passe minimale de l'idée 1 (cosinus avec le tenseur des auteurs, couche 28, révision 0e9e39f2).
  - Enjeu : sans elle, les idées 2, 3 et 8 lisent une direction non validée.
  - Options :
    - greffe sur une session déjà payée : 0,3 à 0,5 heure, mais sur le chemin critique ;
    - instance dédiée : environ 1,2 heure et environ 2 USD, avec des lancements fragiles ;
    - report après G0.
  - Recommandation : la greffe, sinon le report. Confiance moyenne.
- **Décision** : lancer l'idée 4, réduite, en phase 1.
  - Enjeu : la validité externe de G1, au prix d'une exposition délibérée du modèle à la menace. T0.6 dépasse déjà son devis.
  - Options :
    - phase 1 sur devis ;
    - condition croisée de T0.6 : plus tôt, mais pèse sur l'échéance du 19 octobre ;
    - abandon.
  - Recommandation : phase 1, sans volet bien-être. Confiance moyenne.
- **Décision** : autoriser ou non l'écriture dans les activations (idées 7-f, 8, 9 et 10).
  - Enjeu : une intervention nouvelle, voisine de N-015, avec un coût éthique.
  - Options :
    - rien en phase 0, puis l'idée 8 seule, après sa version passive (moins de 0,1 heure) ;
    - attendre N-015 ;
    - refuser.
  - Recommandation : la première option, et jamais l'organisme piloté de l'idée 9. Confiance moyenne.
- **Décision** : tout garder en descriptif jusqu'aux résultats (plancher comme critère, interrogation de l'agent comme base de H1, HC2b, bien-être).
  - Options : rester en descriptif, ou trancher maintenant.
  - Recommandation : rester en descriptif. Confiance haute.
  - À signaler : HC4 est menacée sur notre propre agent (détection de 5 à 21 % à 1 % de faux positifs, 2608.21664 p. 3 et 6).

Aucun changement de modèle n'est proposé. Ajouter le juge 3B au papier C relèverait de D2.

## 7. Éthique et double usage

- Menacer ou piloter le modèle touche un état que les auteurs relient, sous conditions, au bien-être (p. 23). Doses minimales, et ta décision avant tout texte de menace.
- Un organisme « détresse » qui marcherait serait une recette de sabotage sans trace. Rédiger sans doses opérationnelles.
- Ne jamais désérialiser les `.pt` ni exécuter les scripts des auteurs. Écrire « direction », jamais « souffrance ».

## 8. Références

Les PDF sont sous `/tmp/claude-0/-home-user-controle-ia/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/pain-axis/`.

**Lu sur PDF**
- 2609.16247v2 (sha256 fa4b2bb4…) : p. 6, 7, 9, 10, 11, 14, 20, 21, 23, 24-25, 32.
- 2602.19159 (ab4ed860…) : p. 9.
- 2603.04317v2 (852c9449…) : p. 10.
- 2606.30449 (775abf11…) : p. 2, 7.
- 2502.03407 (a4820ad5…) : p. 8.
- 2603.25861 (403bfa91…) : p. 5.
- 2610.12445 (7e141758…) : p. 4.
- 2609.03035 (5092b602…) : p. 6.
- 2603.05028 (7b43a5fd…) : p. 7-8.
- 2607.11871 (5d1d22ed…) : p. 9-10.
- 2608.21664 (7303ce0c…) : p. 3, 6.
- Carte système de Claude Mythos Preview (2b1e0097…) : p. 155-157.
- 2609.36490 (eb6d5bbe…) : p. 4-5.
- 2604.07729 (afe70d72…) : p. 36-38.
- 2604.14865 (4ff711e1…) : p. 10.
- CUPED, Deng et al. 2013 (2a47c570…) : p. 4-5.

**Résumé seulement, ou dépôt lu sans exécution**
- valen-research/Pain-axis (commit 4d75cd9).
- wolframs/pain-axis-review (commit d6c78b4).
- « The Illusion of Intent » (ICML 2026).

Brouillon de travail : `/tmp/claude-0/-home-user-controle-ia/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/pain-axis/redaction-note-finale/note-pain-axis-v4.md`
