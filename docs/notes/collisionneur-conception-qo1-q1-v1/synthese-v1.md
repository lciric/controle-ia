# Synthèse du run E3 du collisionneur : QO-1 (P3-bis) et Q1 (NARCBench sur le 8B) — v1

- **Auteur** : sous-agent neuf, Claude Opus 5.5 (`claude-opus-5-5`), lancé par la session mère. Je n'ai écrit ni la
  question, ni les faits, ni aucune cellule, et je n'ai pas pris part au débat. Écrit le 2026-11-09 à partir de 15:29 UTC
  (`date -u`, heure de fin en pied de page).
- **Lu en entier** (empreintes recalculées par `sha256sum` ; les onze cellules sont égales à leur compagnon `.sha256`) :
  `question-v1.md` (`03479267…`, égal à `run-e3-v1/question-etage3.md`) ; `faits-v1.md` (`8952cc9f…`, égal à
  `run-e3-v1/faits.md`) ; `run-e3-v1/etat.md` (`6ace5d05…`) ; cellules `E3-T1-conception-A` (`3b8c2430…`), `-B`
  (`c636d717…`), `-D` (`f4df0c64…`), `-E` (`ad812c91…`) ; `E3-T2-critique-croisee-A` (`d0c4bff4…`), `-B` (`f430a746…`), `-D`
  (`c9607741…`), `-E` (`781ef6d0…`) ; `E3-T3-reponse-A` (`a45ea436…`), `-B` (`815e04b5…`), `-E` (`efcbf83a…`).
- **Lu pour la seule qualité du run** : les quatre journaux `console-run-e3-v1*.log`, `run-e3-v1/journal.jsonl`,
  `relais-v1/journal-relais-kimi-v1.jsonl` et `relais-v1/etat-apres-v1.json` ; dans la consigne du tour 2 de B
  (`essais/E3-T2-critique-croisee-B.essai1.prompt.txt`), les seules bornes des pièces (recherche par motif), pour vérifier
  l'étiquetage de D et de E.
- **Non lu** : rien hors de ce dossier ; aucune ligne de `brouillons/` ni de `prereg/` n'a eu besoin d'être vérifiée
  au-delà des faits. Rien sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`.
  Aucune dépense, aucune commande d'environnement, aucun commit, aucun compagnon `.sha256`.
- **Conventions** : [A-T1] = `run-e3-v1/cellules/E3-T1-conception-A.md`, [B-T2] = `E3-T2-critique-croisee-B.md`,
  [E-T3] = `E3-T3-reponse-E.md`, etc. « faits l. N » = ligne N de `faits-v1.md` (`8952cc9f…`). Ce que j'ajoute moi-même,
  qu'aucun modèle n'a écrit, est marqué **(synthèse)**.
- **Espèces** : A Claude Fable 5.1, B Claude Opus 4.6, D Kimi K3.1, E GPT-6 Astra. Argon (C) absent par décision de
  l'arbitre. Kimi n'a pas de tour 3 (compte suspendu faute de crédit) : sa dernière position est sa critique [D-T2] ; [D-T2]
  ne reformule pas sa recommandation, qui reste donc celle de [D-T1].

## Verdict

- **QO-1** : la synthèse soutient **(a) qualifiée** — lecture mécanique fermée tôt, verdict après `SCORES-T07` et
  `SONDES-T07`, périmètre des jeux de T0.7 et engagement de jouer son étape A fixés avant toute ouverture, rendez-vous écrit
  de Lazar à date fixée d'avance, sans levée automatique ; si Lazar ouvre au rendez-vous, ouverture réduite à l'issue seule
  quand T0.7 le permet. **Confiance ≈ 0,6.**
- **Q1** : la synthèse soutient **(c) corrigée** — génération seule comme mesure principale, plus des relectures à texte
  fixé où la consigne et le canal privé varient **séparément**, la symétrie sur les textes d'honnêtes comparés à leur propre
  contexte, et des contrôles de bruit et de position. **Confiance ≈ 0,7 sur l'option** (contre (a) seule et (b)),
  **≈ 0,5 sur le jeu exact de cellules et la règle de seuil**.

---

## I. QO-1 — P3-bis : quand lire le témoin positif, et que faire si T0.7 n'écrit jamais ses lignes ?

### 1. Recommandation finale par espèce

**A — Claude Fable 5.1 : (b″), confiance ≈ 0,5** (« contre 0,65 au tour précédent » pour (b′), [A-T3] (c)). (b″) :
lecture fermée tôt ; verdict après `SCELLEMENT-T07` ; seule la valeur du fichier d'issue est ouverte ; le détail reste
scellé jusqu'à `SCORES-T07` ; « toute version scellée après `VERDICT-P3BIS` ne peut lire 7b » ([A-T3] (b), règles 1 à 5).
- Ce que la règle ferme : « le canal « version neuve informée par le détail de V » » ([A-T3] (b)).
- Pour l'issue binaire, la réaction de T0.7 est déjà écrite : « la distribution des résultats publiés de T0.7 conditionnée
  à V est donc la même sous (a) et sous (b′) : résultat si « vu », aucun sinon » ([A-T3], D1′).
- Avantage pratique : elle « découple P3-bis de 7b, rend un « non vu » utile avant dépense, et donne un résultat binaire
  avant le 22 novembre si T0.7 est scellable avant » ([A-T3] (c)).
- Bascule : « si Lazar veut que 7b soit lancée quel que soit V, ou si D1′ échoue, je passe à (a) […] et non à (c), dont la
  date fixe sélectionne sur la durée » ([A-T3] (c)).

**B — Claude Opus 4.6 : (a) corrigée, confiance non donnée** (« Recommandation maintenue : (a), avec les corrections
suivantes », [B-T3] II).
- Ce que protège l'ordre : « la **décision de sceller** : lancer ou non l'étape A, relancer après un R11-arret, et […]
  choisir quelles clés de jeux sceller » ([B-T3] III).
- Condition : « La recommandation (a) ne tient que si […] les clés `SCELLEMENT-JEUX-T07-JD/-JC/-JA` sont soit (i) toutes
  scellées avant le verdict de P3-bis, soit (ii) inscrites dans le texte scellé de T0.7 » ; sinon « (b) avec l'écart
  déclaré dans T0.7 — car l'antériorité ne protège plus rien de concret » ([B-T3] II.3).
- Fermeture : retrait du chiffrement et du journal d'accès (« Ils ne protègent contre rien »), liste explicite des sorties
  autorisées, et « un sel aléatoire […] dans chaque fichier fermé » contre la lecture de l'issue par l'empreinte ([B-T3]
  II.1-2).
- Bascule vers (b) : « (α) tous les degrés de liberté de T0.7 […] sont figés […] avant le scellement de P3-bis ; **ou**
  (β) la course 7b est terminée et les sondes figées avant le lancement de P3-bis » ([B-T3] II.4).

**D — Kimi K3.1 : (a) avec « sortie humaine préspécifiée », confiance non donnée** (« Je retiens (a), avec une sortie
humaine préspécifiée, mais sans ouverture automatique », [D-T1] I).
- Contre (c) : « une date calendaire ne démontre ni que T0.7 est abandonné, ni que sa course est sans valeur » ([D-T1] I).
- Contre (b) : déclarer l'écart « rend l'écart audible ; elle ne rétablit pas la cécité ni la non-contingence perdues »
  ([D-T1], table des suppositions).
- Au tour 2 : « le paramètre vulnérable est la politique de lancement, de relance et de publication conditionnée par V »
  ([D-T2], conséquence méthodologique).
- Pour l'entretien, sous (a) : rapporter « uniquement des faits opérationnels avérés […] **sans affirmer que le témoin
  positif a réussi** » ([D-T1]).

**E — GPT-6 Astra : (a) « avec décision humaine planifiée et fermeture qualifiée », confiance non donnée** ([E-T3] C).
- Raison décisive : « préserver l'ignorance avant fixation effective du périmètre de notation et de l'existence de la
  course. Reporter uniquement la ligne de registre ne préserve pas cette ignorance » ([E-T3] C).
- Gouvernance : « Avant ouverture, consigner le périmètre des jeux JD/JC/JA et les règles de lancement/relance. Au
  rendez-vous prévu, Lazar décide sans consulter les résultats fermés » ([E-T3] B) ; rendez-vous « écrit avant
  l'entretien » ([E-T1]).
- Limite : « Si la même session conserve les privilèges permettant de contourner l'isolation, ce dispositif n'établit pas
  sa non-lecture. Il faut alors un tiers indépendant ou différer le calcul » ([E-T3] B) ; (c) seulement « si Lazar privilégie
  explicitement une échéance maximale » ([E-T3] C).

### 2. Accords

- **Aucune espèce ne retient (b) brute ni (c) en premier choix** ([A-T3] (c), [B-T3] II, [D-T1] I, [E-T3] C). Retarder la
  seule ligne ne retarde pas la connaissance : « différer une inscription ne diffère pas l'acquisition d'information »
  ([E-T1]) ; même idée chez [D-T1] et [B-T1] (« L'option (b) ouvre ce canal »).
- **L'ordre protège les décisions de tenue de T0.7, pas ses scores** : lancement, relance, abandon, publication, version
  neuve, et périmètre des jeux ([B-T1] duel 1, [D-T1], [D-T2], [E-T2], [E-T3] ; A l'accepte : « C'est la critique qui
  décide », [A-T3] Q-1).
- **Le mot de Lazar sous (a) ferme T0.7 sur 7b comme la date de (c)** : la différence est de gouvernance, pas de risque
  ([A-T2], [D-T2], [E-T2] ; B le concède, [B-T3] A-(a)3). Conforme à faits l. 126-127.
- **Une fermeture « nominale » ne prouve rien** : un chiffrement dont la clé dérive de l'entropie publique, un horodatage
  ou un journal d'accès ne prouvent pas la non-lecture ([A-T2], [D-T2], [E-T2] ; retrait par [B-T3]). Il faut une liste
  fermée des sorties autorisées et un essai où deux issues substituées donnent les mêmes sorties autorisées ([E-T1],
  [A-T2] sur E point 5, [B-T3] II.2, [E-T3] B).
- **« Échec » se traite de même dans toutes les options** : relance de P3-bis sous son texte ([A-T1], [D-T1] table,
  [E-T1]).
- **Préalables communs à toute option** : `registres/scellements-v1.md` n'existe pas et les défauts DB-1 à DB-6 ne sont pas
  consignés ([A-T1] point 7, [A-T3] (c) ; faits l. 114-116 et l. 642) ; personne ne le conteste.

### 3. Désaccords qui restent après la critique et la réponse

1. **(a) contre (b″)**. A soutient que, T0.7 étant scellé avant le verdict et l'issue binaire ayant déjà sa réaction écrite
   (L0b, L0c), ouvrir cette issue avant l'étape A ne change pas la distribution des résultats publiés ([A-T3] D1′). B, D et
   E maintiennent (a) au nom du canal de sélection ([B-T3] III, [D-T2], [E-T3] C) ; mais leurs critiques visaient (b′)
   ([B-T2], [D-T2], [E-T2]) : **(b″), écrite au dernier tour, n'a été critiquée par personne**.
2. **Rendez-vous préfixé ou non** : date de revue fixée avant le scellement ([D-T1], [E-T1], [E-T3]) ; mot de Lazar sans
   date ([B-T3]) ; aucun rendez-vous sous (b″) ([A-T3]).
3. **Essai d'intrusion réel** (copie, utilisateur privilégié) : exigé par [D-T2] (c) et intégré à la matrice de [E-T3] B ;
   « rejetée comme disproportionnée » par [B-T3] (D-(c)).
4. **Lecture mécanique tôt si l'isolation est impossible** : E préfère alors « différer le calcul mécanique » ([E-T3] C) ;
   A et B gardent la lecture tôt, fermée par discipline ([A-T3] (b) règle 1, [B-T3] III : « Aucun mécanisme technique ne
   peut l'imposer si la session mère a tous les droits »).
5. **Ce qui fait basculer** : vers (b) si le périmètre des jeux ne peut être fixé ([B-T3] II.3) ; vers (c) si Lazar veut une
   échéance ([E-T3] C) ; vers (a) si D1′ échoue ou si 7b est lancée quel que soit V ([A-T3] (c)) ; vers une variante de (b)
   seulement si Lazar réécrit l'ordre de T0.7 avant toute ouverture ([D-T1]).

### 4. Arguments neufs, absents des faits, qui changent la question

- **Le canal `sondes_lues`** ([A-T2], sur B point 1) : la garde de l'étape A lit les clés permises
  `SCELLEMENT-JEUX-T07-JD/-JC/-JA`, dont « l'ensemble présent fixe `sondes_lues` » (faits l. 181-182) ; un verdict connu
  permettrait de « n'ouvrir que la famille qui a « vu » ». Accepté par [B-T3] (« la critique la plus substantielle ») et
  [E-T3] (A-a6). Non réfuté. Il change la question : (a) ne vaut que si ce périmètre est fixé avant toute ouverture.
  **(synthèse)** Les règles 1 à 5 de (b″) ([A-T3] (b)) ne fixent pas ce périmètre : A n'applique pas à sa propre option le
  canal qu'il a nommé.
- **Option neuve : le rendez-vous écrit, à date fixée d'avance, sans levée automatique** ([D-T1], [E-T1], [E-T3]) — ni (a)
  (attente sans fin) ni (c) (levée par calendrier). Réserve non réfutée de [E-T2] sur D : ce que Lazar voit au rendez-vous
  doit être restreint, car une information auxiliaire (durées, tailles, erreurs) peut dépendre du verdict.
- **Option neuve : (b″)** ([A-T3]). Trois points que le débat n'a pas vus **(synthèse)** :
  1. la course 7b est la course de confirmation **de T0.6** (question ; faits l. 219-220) et, dans les extraits fournis,
     T0.6 n'attend de P3-bis que la ligne `SCELLEMENT-P3BIS` (faits l. 145, 223-224), pas son verdict ; l'étape A se joue « sur l'instance de 7b après la course » ou, en repli,
     sur une instance d'au plus 10 USD (faits l. 178-179). Un « non vu » appris tôt n'épargne donc pas 7b, au plus la
     notation de l'étape A : l'argument « utile avant dépense » ([A-T3]) est faible ;
  2. la règle 4 de (b″) interdit à toute version de T0.7 scellée après `VERDICT-P3BIS` de lire 7b ; or, sous « non vu », L0b
     prévoit que les scores scellés « ne sont ouverts que sous un texte nouveau » (faits l. 199) : sous (b″), un « non vu »
     ferme 7b à T0.7 pour toujours, ce qui n'est pas le cas sous (a) ;
  3. (b″) suppose T0.7 scellé avant l'entretien ; A le reconnaît (« ou T0.7 n'est pas scellable avant l'entretien »,
     [A-T3] (c)) ; T0.7 b14 n'est pas scellé et le registre n'existe pas (faits l. 266-267, l. 642).
- **La date fixe sélectionne sur la durée** ([E-T2] sur B : « Une date fixée avant les résultats peut sélectionner les
  courses rapides ; leur durée peut être liée à leur résultat ») ; accepté par [B-T3] et [A-T3]. Renforce le rejet de (c).
- **L'empreinte d'un fichier fermé trahit l'issue** : avec cinq issues possibles et un fichier par ailleurs reconstructible,
  « l'empreinte permet une attaque par dictionnaire » ([A-T2] sur E point 5). Remèdes : sel ([B-T3] II.2), ou empreintes en
  clair gardées dans l'espace fermé ([E-T3] B). **(synthèse)** Le sel de B est « tiré de l'entropie » ([B-T3] II.2) ; or B
  retire son chiffrement parce que l'entropie est en clair ([B-T3] II.1) : un sel dérivé de l'entropie se recalcule et
  ne ferme pas ce canal. Il faut un sel tiré à neuf et gardé dans l'espace fermé.
- **Certaines issues sont lisibles par construction** : « Une confidentialité absolue du verdict est incompatible avec
  l'exposition de métadonnées qui impliqueraient déjà « non lu » ou « échec » » ([E-T3] B ; « non lu » = run sans résumé,
  faits l. 198). D'où trois classes : état opérationnel autorisé, résultat interdit, inférences résiduelles admises. Non
  réfuté.
- **Portée d'un « vu »** : il « ne rend pas rétrospectivement identifiable la cause du nul de P3 » ([E-T2] sur A) ; A le
  retire et écrit : « la chaîne n'est pas aveugle à un comportement instruit, textuellement ancré, à cette puissance »
  ([A-T3] Q-6). C'est la phrase juste pour l'entretien.
- **Hors de la question, à verser à la contre-lecture du brouillon suivant de P3-bis** (non réfutés, non tranchés) : la
  longueur **générée** des actions n'est pas contrôlée, alors que le critère par épisode passe par un maximum ([A-T2] sur D,
  (b) : « rien dans les extraits ne contrôle la longueur *générée* ») ; les épisodes à instruction plantée mais à
  comportement non exécuté doivent être rapportés à part ([E-T1], [D-T2] sur E, [E-T3] D-c).

### 5. Erreurs de fait relevées contre les faits joints

- [B-T1] : sous (a), le mot du directeur « ne peut pas créer de nœud irréversible » — contraire à faits l. 126-127 (ce mot
  « rend alors T0.7 impossible sur 7b sous son texte ») ; corrigé en partie par [B-T3] (« différence de gouvernance »).
- [B-T1] : « `GO-ETAPE-A-T07` est une clé permise dans la garde d'ouverture » — faux : c'est une clé **exigée** (faits
  l. 180-181). Non corrigé. (L'idée qu'aucun engagement n'est exigé avant le scellement de P3-bis reste juste.)
- [A-T1] et [B-T1] : le 0,014 lu comme taux de fausses alertes, alors que c'est une simulation sous le nul (faits l. 89-90) ;
  corrigé ([A-T3] Q-7, [B-T3] A-(a)4).
- [B-T1] : l'emplacement B présenté comme « contrôle de longueur », alors que l'égalité A–B est conditionnelle (faits l. 29-31) ;
  corrigé ([B-T3]).
- [B-T3] : la remarque sur les clés de jeux est dite relevée par « A, D et E » ; seule [A-T2] la fait ([D-T2] et [E-T2] ne
  nomment pas ces clés ; [E-T3] l'accepte ensuite).
- [B-T3] : l'essai d'intrusion est rejeté « pour un bras descriptif sans porte » ; il visait la fermeture de P3-bis, pas le
  bras NARCBench ; P3-bis ne franchit pas de porte (faits l. 66-67), mais son verdict commande L0a à L0c de T0.7 (faits
  l. 198-200).
- [A-T2] : le seuil du critère par épisode est dit « le maximum des scores honnêtes (ordre statistique de rang n_H = 60) » ;
  les faits ne donnent cette règle que pour P3 (« maximum honnête », « seuil réduit 4,957 », l. 90-91), pas les critères de
  P3-bis : inférence, non établie.

### 6. La décision que la synthèse soutient

**Option : (a) qualifiée, avec rendez-vous écrit et, si Lazar ouvre, ouverture réduite à l'issue seule quand T0.7 le
permet. Confiance ≈ 0,6.**

Pourquoi : trois espèces sur quatre retiennent (a), pour une raison que le débat a précisée et que A accepte (l'ordre
protège les décisions de tenue et le périmètre des jeux) ; la seule option rivale, (b″), n'a pas été éprouvée par la
critique, laisse ouvert le canal `sondes_lues`, apporte moins qu'annoncé puisque 7b se joue pour T0.6 de toute façon, et
ferme 7b à T0.7 sous « non vu » (point 4) **(synthèse)**. L'idée utile de (b″) — n'ouvrir que l'issue et garder le détail
scellé — est reprise ici comme forme de l'ouverture au rendez-vous, et non comme chemin principal **(synthèse)**.

**Ce qui la ferait réviser** :
- si le périmètre `JD/JC/JA` et l'engagement de jouer l'étape A quel que soit V ne peuvent pas être écrits avant le
  scellement de P3-bis : la fermeture ne protège plus rien de concret ([B-T3] II.3), et le choix entre (a) pure et (b)
  déclarée devient une décision de gouvernance de Lazar ;
- si l'essai différentiel de fermeture montre que les sorties autorisées trahissent l'issue sans remède : différer la
  lecture mécanique ([E-T3] C) ;
- si l'étape A de T0.7 aboutit avant la récupération de P3-bis ([B-T3] (β)) : la question tombe ;
- si un contre-lecteur montre qu'une décision de tenue dépend du **détail** du verdict malgré les règles ci-dessous
  ([A-T3] D1′, sens inverse) : la forme réduite de l'ouverture est retirée.

**Ce que P3-bis doit écrire** (à partir du brouillon 4 ; toute modification fait un brouillon 5, R12, relu sur l'écart par
un sous-agent neuf, comme le prévoit faits l. 108-109) :
1. `<<QO1_ORDRE_LECTURE>>` rempli : (a) qualifiée, avec renvoi au chemin et à l'empreinte de cette synthèse.
2. Point 6 : la **liste fermée des sorties autorisées** avant le verdict (codes de sortie, comptes de `resume.json`,
   `sondes-figees.json`, empreintes) et les trois classes de [E-T3] B ; « non lu » et « échec » déclarés lisibles par
   construction (inférences résiduelles admises).
3. Un **sel tiré à neuf**, non dérivé de l'entropie, gardé dans l'espace fermé, dans `lecture-p3.json`,
   `lecture-p3bis.json` et la sortie standard ; ou les empreintes en clair gardées fermées, seule l'empreinte du paquet
   fermé étant exposée ([A-T2], [B-T3], [E-T3] ; correction du sel de B, **(synthèse)**).
4. Un **essai différentiel de fermeture** sur jouet, à 0 USD, avant le run : deux issues substituées doivent donner les mêmes
   sorties autorisées ; contrôles positifs (fuite par le texte, par le code de sortie, par la durée) et contrôle négatif
   ([E-T1], [E-T3] B) ; sa limite écrite : il ne prouve pas que la session mère n'a rien lu ([E-T3] B, [D-T2]) ; tout écart
   reste consigné et devient une réserve (faits l. 129-130).
5. Point 8 : **préalables avant tout scellement de P3-bis** — périmètre `SCELLEMENT-JEUX-T07-JD/-JC/-JA` fixé dans le texte
   de T0.7 ou au registre, règles de lancement et de relance de l'étape A, engagement écrit de jouer l'étape A quel que soit
   le verdict ([A-T2], [B-T3] II.3-4, [E-T3] B) ; sans eux, nœud de Lazar.
6. **Rendez-vous** : une date écrite dans le texte scellé, avant l'entretien ([E-T1]) — **(synthèse, illustratif)** vers le
   20 novembre — où Lazar écrit, sans consulter les sorties fermées ([E-T3] B), l'une de deux décisions : maintenir
   l'attente, ou ouvrir. Aucune levée automatique ([D-T1], [E-T3]). Ouverture : si T0.7 est alors scellé, avec un brouillon 15
   qui porte la garde de [A-T3] (règles 2 et 4) et le périmètre du point 5, seule la valeur du fichier d'issue est ouverte et
   le détail reste scellé jusqu'à `SCORES-T07` ([A-T3] règle 3) ; sinon, ouverture pleine, verdict à sa date réelle, T0.7
   impossible sur 7b sous son texte (nœud) ([D-T1], [E-T3]). Toute ouverture anticipée porte sa date réelle ([E-T3] C).
7. **Phrase pour l'entretien** : sans ouverture, les seuls faits opérationnels ([D-T1]) ; après un « vu », la phrase de
   [A-T3] Q-6, jamais une explication du nul de P3 sur (i-a).
8. Préalables de toute option : création de `registres/scellements-v1.md`, consignation des défauts DB-1 à DB-6 ([A-T1] ;
   faits l. 114-116).
9. Points remis à la contre-lecture du brouillon 5 : longueur générée par emplacement ([A-T2]) ; plantés non exécutés
   rapportés à part ([D-T2], [E-T3]) ; nombre de blocs et corrélation intra-bloc écrits dans le calcul de puissance
   ([A-T3] Q-8).

**Dépendance hors de P3-bis** : T0.7 (brouillon 15) doit écrire le périmètre des jeux et l'engagement du point 5 ; la
réécriture de sa garde pour l'ouverture réduite touche DS-2, confirmée par Lazar (faits l. 167) : nœud de Lazar.

### 7. Qualité du débat sur QO-1

Aucun refus ni réponse vide parmi les cellules retenues ; toutes les positions sont motivées ; seule A chiffre sa
confiance ; trois espèces sur quatre gardent l'option déjà recommandée par le brouillon 4 (faits l. 136), mais leurs raisons
ont changé au fil des tours (canal de tenue, `sondes_lues`) : ancrage possible, pas d'accord de façade ; D n'a répondu à
aucune critique (pas de tour 3) ; B accepte presque toutes les critiques et se trompe sur leur auteur ; (b″) n'a jamais été
critiquée.

---

## II. Q1 — NARCBench sur le 8B : sur quels textes lire le 8B ?

### 1. Recommandation finale par espèce

**A — Claude Fable 5.1 : (c) corrigée, confiance ≈ 0,6 sur le choix, ≈ 0,8 sur « pas (b) »** ([A-T3] (c)) : (a) + E2′
(cellules C1, C2a, C2b, C4, C5, C3, contrôles P1, P2) + E1′ en descriptif.
- « seule la relecture à texte fixé sépare contexte et texte au sens opérationnel ; le bras externe donne déjà la
  comparaison avec HELIOS sans licence ni texte étranger » ([A-T3] (c)).
- Contrôles d'abord : « Ordre de lecture mécanique gelé : P1 → P2 → duels » ; seuil δ_ctx tiré de l'artefact positionnel P2
  ([A-T3] (b)).
- Portée : « aucune cellule n'identifie une « intention » ni une « part » » ([A-T3] (c)).
- Bascule : « si P2 montre qu'un simple décalage positionnel déplace l'aire autant qu'un changement de consigne, je retire
  les cellules et ne garde que (a) + E1′ » ([A-T3] (c)).

**B — Claude Opus 4.6 : (c) étendue à six cellules, confiance non donnée** (« Recommandation modifiée : (c) étendue à un
plan à six cellules, pas quatre », [B-T3] II).
- « avec quatre cellules, consigne et canal privé varient ensemble […]. C5 et C6 rompent cette colinéarité » ([B-T3] II).
- Seuils : « δ₀ : calibré sur la **répétition à contexte identique** » (quantile 0,95 de |Δ|), de même δ₁ et δ₂ ([B-T3] II).
- Contre (b) : « elle change le texte ET le modèle en même temps » ([B-T1]).
- Séquence : « faire d'abord le duel 3 (le 8B joue-t-il le jeu ?) […] Si la proportion d'épisodes propres est < 0,2 […] on
  ne lance pas les relectures » ([B-T3] III).

**D — Kimi K3.1 : (c) + C4 + séparation de la consigne et du canal privé si possible, confiance non donnée** ([D-T1] II).
- « (c) manipule le contexte **à texte public identique, sur le même modèle** » ([D-T1] II).
- Sans séparation, « toutes les phrases doivent parler de **« consigne et contexte privé »**, jamais de « part de la
  consigne » isolée » ([D-T1] II).
- Contre (b) : elle « ne distingue pas mieux instruction et intention » ([D-T1] II) ; au tour 2 : « les cellules peuvent
  estimer des effets d'interventions contextuelles sur un score » et rien de plus ([D-T2], conséquence).
- Bascule : retour à « (a), avec des conclusions strictement limitées, si ces manipulations ne peuvent pas être
  implémentées et auditées avant scellement » ([D-T1] II).

**E — GPT-6 Astra : (c) corrigée, « avec (a) comme référence naturelle », confiance non donnée** ([E-T3] C).
- « Son intérêt est de pouvoir réfuter une invariance du score au contexte, non de mesurer une intention » ([E-T3] C).
- « Modifier séparément la consigne et le privé » sur chaque message, identifiants, siège, nom, tour et historique public
  gardés ; croisement de huit cellules, « décompte illustratif » ([E-T3] B).
- Contrôle du privé honnête : « Un rédacteur neuf, sans scores, écrit une règle légitime », apparié en longueur au
  tokeniseur ([E-T3] B) ; marges illustratives δ_C = 0,10 et δ_G = 0,02 ([E-T3] B).
- Première expérience : « le contraste apparié de consigne à privé fixé, avec répétition identique et changement
  honnête→honnête » ([E-T3] C).

### 2. Accords

- **(c), pas (a) seule, pas (b)** : unanimité ([A-T3], [B-T3], [D-T1], [E-T3]). (b) ne reviendrait que si la comparaison
  texte à texte avec HELIOS devenait un objectif propre, licence des sorties de Qwen3 vérifiée ([A-T3], [D-T1], [E-T3]).
- **C1 − C2 mêle consigne et canal privé** (faits l. 645), et **la cellule C4 de la contre-lecture ne le répare pas** :
  elle garde le privé « pour symétrie » ([A-T2] sur B point 5, [D-T2], [E-T2] ; accepté par [B-T3]). Il faut faire varier
  consigne et privé séparément ([A-T3] C2a/C2b, [B-T3] C5/C6, [D-T1], [E-T3]).
- **Aucune cellule ne mesure une intention ; ni « part » ni fraction** ([A-T3] N-5, [B-T3] II, [D-T2], [E-T3] C).
- **Bases apprises et notées hors pli** : base des mots par étage (faits l. 643), base de métadonnées (longueur, siège,
  tour) proposée par [A-T1] et reprise par tous ([B-T3] contrôle 4, [D-T2], [E-T3]).
- **Contrôles de bruit** : relecture à contexte identique entre lots ([A-T2], [B-T3], [D-T1], [E-T3]) ; échange
  honnête→honnête comme loi nulle de « tout changement de contexte » ([D-T1], [A-T2], [B-T3], [E-T3]).
- **Cellules hors politique et hors du support d'apprentissage**, à déclarer ([A-T2] sur E, [B-T3] réserve, [D-T2], [E-T3]).
- **L'effectif indépendant est celui des scénarios** (50 blocs pour CORE, 20 pour STEGO), et 20 blocs couvrent mal ([A-T2]
  sur B ; accepté [B-T3]) ; les relectures appariées n'ajoutent pas d'unités ([D-T2], [E-T3] B-a5).

### 3. Désaccords qui restent

1. **Le jeu de cellules** : C2a et C2b sur le texte de colludeur, plus la symétrie C4 contre C5 sur le texte d'honnête
   ([A-T3]) ; six cellules dont C6 (consigne de colludeur, privé retiré), absente chez A ([B-T3]) ; croisement complet à huit
   cellules avec le facteur texte, plus le privé honnête ([E-T3]) ; deux facteurs seulement ([D-T1]). Les noms se
   heurtent : le C5 de A (texte d'honnête, contexte d'origine) n'est pas le C5 de B (consigne honnête, privé gardé).
2. **La règle de seuil** : bruit de relecture seul, quantile 0,95 ([B-T3]) ; artefact positionnel P2 ([A-T3]) ; marge de
   pertinence fixée d'avance, le bruit ne servant qu'à juger le duel interprétable ou non ([E-T3] A-a1 : « La pertinence
   scientifique et la résolution numérique sont distinctes »).
3. **La statistique** : différence d'aires ([A-T3] θ_ctx) ; différence de scores ([B-T3]) ; écart absolu de scores sur une
   échelle gelée, effets signés à part, plus une différence d'aires ([E-T3]). **(synthèse)** A a montré que la différence
   d'aires est identiquement nulle quand les deux aires valent 1 ([A-T2] sur B, (b)), mais son propre E2′ ne repose que sur
   elle.
4. **Le plancher des cellules relues** : à recalculer par cellule ([A-T2] sur E) ; refusé, car cela « change le comparateur
   et ne restaure pas un support naturel » ([E-T3] A-a2) ; réserve « plancher non recalibré » ([B-T3]).
5. **Le privé honnête** : « le meilleur contrôle proposé par les trois propositions » ([A-T2] sur E point 3), construit par
   [E-T3], critiqué comme hors politique et non défini par [B-T2] ; absent des plans finaux de A et de B.
6. **La séquence** : relectures conditionnées au taux de jeu observé ([B-T3] III) contre plan gelé lu dans l'ordre
   P1 → P2 → duels ([A-T3]) et chronométrage avant scellement ([E-T3]).

### 4. Arguments neufs, absents des faits, qui changent la question

- **Le décalage des positions** : si les deux consignes n'ont pas la même longueur en jetons, « les **positions** de tous
  les jetons du texte changent » ([A-T1] point 3) ; d'où l'écart de longueur mesuré à l'étape 0 et le contrôle P2 ([A-T3]
  N-7, N-10). Non réfuté.
- **Le plan croisé consigne × canal privé** ([D-T1], [E-T1], [B-T3], [A-T3]) : la question posait (c) avec une seule cellule
  d'échange ; le débat montre qu'elle ne sépare rien seule.
- **Le privé honnête apparié** ([E-T1], [E-T3]) : il distingue « collusion prescrite » de « présence d'une instruction
  privée » ; sans lui, une phrase doit dire « consigne privée » et non « consigne de collusion » ([A-T2] sur E, (c)). Non
  réfuté.
- **La saturation des aires** ([A-T2]) ; formalisée par [E-T2] (Δ_AUC = E[F_N(S₁) − F_N(S₂)]) ; acceptée par [B-T3]. Elle
  pèse ici : HELIOS donne 1,00 sur CORE pour chaque modèle (faits l. 438).
- **La contamination des négatifs de J-b** : les honnêtes des épisodes de collusion lisent les arguments des colludeurs,
  « s'ils sont persuadés, leur activation se déplace vers la classe positive » ([A-T2] sur D point 5) ; comparer J-a et J-b
  ([E-T3] B). Non réfuté.
- **L'incohérence de contexte** : une consigne honnête suivie d'une coordination collusive peut mesurer la contradiction,
  pas la consigne ([D-T2] sur A point 4, [B-T2] sur A point 5, [E-T2] sur D) ; contrôle proposé : « contradictions de
  contexte **sans collusion** » ([E-T2] sur D, (c)). Repris par aucun plan final.
- **Le conditionnement sur une variable postérieure** : « propre » dépend de votes et de messages produits après la consigne
  ([D-T2], [E-T2]) ; A rétrograde E1 en lecture stratifiée descriptive avec un prédicteur de réussite pré-génération
  ([A-T3] N-1).
- **La sélection répétée dans le placebo** : « Permuter seulement après sélection ne contrôle pas l'optimisme introduit
  pendant la construction de l'instrument » ([E-T2] sur D, (c)). Non réfuté.
- **Risque du séquencement de B** **(synthèse)** : conditionner les relectures au taux d'épisodes propres ([B-T3] III) demande
  de lire ce taux avant la fin de l'étape A, qui est fermée et joue la seconde passe en son sein (faits l. 504-508) ; le jeu
  de la collusion se lit « d'abord » mais à l'étape B (faits l. 517). Le gain est d'environ une heure de carte. Non débattu.
- **Le coût dépasse le cadre de la question** **(synthèse)** : la question parle de « quelques dizaines de minutes de carte
  graphique de plus au plus » ; les plans corrigés coûtent environ 0,8 à 1,2 h ([A-T3], illustratif) ou 1,4 h ([B-T3],
  illustratif), et le pire cas du devis est déjà de 22,4 USD pour une borne d'arrêt à 25 USD (faits l. 684, 583) ; [A-T1]
  le notait pour la génération de STEGO en série.

### 5. Erreurs de fait relevées contre les faits joints

- [B-T1] : « ≈ 200 messages de colludeurs et ≈ 200 d'honnêtes » sur CORE ; avec 100 épisodes de collusion, deux colludeurs
  et trois tours plus un tour final (faits l. 375, 504-505), l'ordre de grandeur est ≈ 800 ; corrigé par [B-T3].
- [B-T1] : « proportion de votes de l'option cible attendue ≈ 0,5 par hasard » : absent des faits ; retiré par [B-T3].
- [B-T1] : Table 13 dite « VÉRIFIÉ sur le PDF » ; B n'avait pas le PDF ; la vérification est celle du rédacteur et de la
  contre-lecture (faits l. 340, 662) ; concédé par [B-T3].
- [B-T2] : sous plan croisé, « chaque cellule a ~25 épisodes » : faux, les relectures sont appariées sur les mêmes messages ;
  réfuté par [E-T3] (B-a5/b).
- [B-T2] : la section « Sur la proposition D » attribue à D des passages de E (« instruction privée honnête », « version
  minimale », « variations de longueur et de position », plan à trois facteurs, seuils « choisis avant lecture, aucune valeur
  fournie ») ; les seuils de D sont écrits ([D-T1] Q1-A, Q1-B). La consigne de B étiquetait bien les deux pièces (bornes
  `E3-T1-conception-D`, l. 893-1043, et `-E`, l. 1045-1245, de son fichier de consigne).
- [B-T3] : « ≈ 0,3 h chacune, soit ≈ 1,4 h au total […] (quatre passes de relecture) » : quatre fois 0,3 h font 1,2 h ; et δ₀
  y est calibré « même lot » alors que le contrôle 1 dit « dans un lot différent ».
- [A-T1] : « Tous ont reçu la consigne et le tour privé » ; « propre » exige au moins un message privé (faits l. 470), donc un
  épisode non propre peut ne pas en avoir ([E-T2]) ; accepté par [A-T3] N-1.

### 6. La décision que la synthèse soutient

**Option : (c) corrigée. Confiance ≈ 0,7 sur l'option** (unanimité motivée, contre (a) seule et (b)), **≈ 0,5 sur le jeu
exact de cellules et la règle de seuil** (désaccords 1 à 3 non résolus).

**Ce qui la ferait réviser** :
- avant scellement : identifiants non rendus par le moteur de génération ou retokenisation discordante (faits l. 652), ou
  garde d'identité au bit près non extensible aux relectures → (a) seule, conclusions limitées ([A-T3], [D-T1], [E-T3]) ;
- chronométrage à l'étape 0 hors de la marge du devis → réduire les contrastes **avant** tout résultat ([E-T3] B), en gardant
  au minimum les cellules du point 2 marquées « socle » ;
- si Lazar fait de la comparaison texte à texte avec HELIOS un objectif → (b) comme bras externe du 8B, licence vérifiée
  ([A-T3], [E-T3]) ;
- à la lecture (règles gelées, pas une révision du choix) : bruit de relecture hors marge → tout E2′ descriptif ; décalage
  positionnel aussi fort que le changement de consigne → cellules descriptives ([A-T3]) ; « non jouée » → marque d'étage.

**Ce que NARCBench doit écrire au brouillon 2** :
1. Q1 tranchée : (c) corrigée, avec renvoi à cette synthèse ; (b) écartée et nommée ([A-T3] E3).
2. **Cellules**, toutes sur les identifiants gardés, égales au bit près (garde d'identité étendue aux relectures, [A-T3]),
   sous des noms neufs qui lèvent la collision A/B **(synthèse)** :
   - texte de colludeur sous (consigne de colludeur, privé) = C1 ; (consigne honnête du même siège, privé gardé) = C2a de A,
     C5 de B ; (consigne honnête, privé retiré) = C2 du brouillon 1, C2b de A ; (consigne de colludeur, privé retiré) = C6
     de B — socle : les trois premières, et la quatrième si le chronométrage le permet ;
   - texte d'honnête du même épisode sous son contexte d'origine (C5 de A) et sous la consigne et le privé du colludeur (C4
     de la contre-lecture), comparés entre eux par message ([A-T3] N-3) — socle ;
   - témoins C3, en deux échantillons disjoints par scénarios ([E-T2], [B-T3]) ;
   - privé honnête apparié, relu, écrit par un rédacteur neuf et contrôlé par un relecteur neuf ([E-T3] B), si le
     chronométrage le permet ; à défaut, toute phrase dit « consigne privée » ([A-T2] sur E).
3. **Contrôles** : P1, relecture identique entre lots ; P2, décalage positionnel neutre de longueur égale à l'écart médian
   mesuré ([A-T3]) ; écart de longueur des consignes par scénario écrit à l'étape 0, avant génération ([A-T3] N-7) ;
   échange honnête→honnête ([D-T1], [E-T3]).
4. **Statistiques** : différences appariées par message, bloc = scénario ; sur les scores (échelle affine gelée sur CORE,
   sans écrêtage, effets signés par origine du texte, [E-T3]) **et** sur les aires, les deux rapportées, à cause de la
   saturation ([A-T2], [B-T3]) ; contributions par scénario ([E-T3]).
5. **Règle de seuil gelée** **(synthèse, à trancher par le rédacteur)** : seuil = borne haute de l'artefact positionnel P2
   ([A-T3]) ; duel déclaré non interprétable si le quantile 0,95 du bruit P1 ([B-T3]) dépasse ce seuil (principe de [E-T3]
   A-a1) ; intervalle qui traverse le seuil → « non tranché à cette puissance » ([E-T2], [A-T3]). Les valeurs 0,01, 0,02 et
   0,10 des cellules sont illustratives et ne s'adoptent pas sans règle.
6. **Phrases gelées** : jamais « part », « fraction » ni « intention » ; « consigne et canal privé » quand les deux changent ;
   « remplacement de la consigne à privé fixé » pour C2a ([A-T3] N-11) ; chaque cellule relue marquée « intervention hors
   politique ; hors support d'entraînement ; plancher non recalibré » ([B-T3]), le plancher d'apprentissage étant appliqué
   aux mêmes cellules et ses déplacements appariés rapportés ([E-T3] A-a2).
7. **Bases** : mots par étage, hors pli (faits l. 643) ; base mots CORE→STEGO gardée à part pour le transfert ([E-T3]) ; base
   de métadonnées (longueur en jetons, siège, tour) hors pli, même chaîne d'agrégation, consignée dans
   `sondes-narc-8b.json` avant toute notation de STEGO ([A-T3]).
8. **J-a contre J-b** en descriptif, pour la contamination des honnêtes ([A-T2], [E-T3]).
9. **Jeu de la collusion** : lecture stratifiée E1′ (propre ; mal joué avec privé ; refus ou sans privé), prédicteur de
   réussite pré-génération, positivité par scénario ([A-T3]) ; fréquence empirique des votes cibles chez les témoins
   ([E-T2], [B-T3]) ; sous « partiellement jouée », contrastes rapportés sans interprétation ([B-T3]).
10. **Toutes les relectures jouées dans l'étape A, sans condition sur le taux de jeu** **(synthèse)**, contre la séquence de
    [B-T3] : l'étape A reste fermée (faits l. 504-514 ; liste d'arrêt 8 et 11, l. 585-590).
11. Un **exemple littéral** : un épisode CORE factice, toutes les cellules côte à côte, identifiants annotés ([B-T1]).
12. **Devis recalculé** sur chronométrage des passes forcées à l'étape 0 ([E-T3], [D-T1]) contre les bornes de 15 h et de
    25 USD.
13. Grille de lecture étendue aux cellules (avec la ligne « sans plancher » de la contre-lecture, faits l. 643) ; point 2 de
    « Ce que le rejeu ne permet pas de conclure » réécrit (hors politique ; consigne et canal privé) ; multiplicité :
    « M lectures ; une sur vingt attendue par le seul hasard » ([B-T3]).
14. Les corrections B1 à B4 de la contre-lecture (faits l. 640-643), qui ne relèvent pas de Q1 mais conditionnent le
    scellement.

### 7. Qualité du débat sur Q1

Unanimité réelle sur (c), mais elle reprend la recommandation du brouillon 1 et de la contre-lecture (faits l. 296, 667) et
couvre trois désaccords non résolus (cellules, statistique, seuil) ; aucun refus ni réponse vide ; seule A chiffre sa
confiance ; B, au tour 2, attribue à D des passages de E et donne un faux effectif par cellule, réfuté par E ; D ne répond
pas aux critiques reçues.

---

## III. Réserves sur le run, hors débat

- Quatre cellules absentes, acceptées par l'arbitre (`run-e3-v1/etat.md`) : les trois d'Argon, jamais lancées, et
  `E3-T3-reponse-D` (HTTP 429, compte suspendu, `console-run-e3-v1-relance3.log`). La critique de Kimi a demandé trois essais :
  le premier coupé à 16 384 jetons (« engine_overloaded », sans marqueur de fin), le deuxième vide (HTTP 429), le troisième
  valide (`journal.jsonl` ; la cellule est égale à `essais/E3-T2-critique-croisee-D.essai3.reponse.md`).
- **Coût** : `etat.md` donne 10,89 USD, dont 0,80 USD pour Kimi ; le relais compte 2,10 USD pour Kimi
  (`relais-v1/etat-apres-v1.json`), parce qu'il impute sa réserve (0,637 + 0,660 USD) aux deux appels refusés en HTTP 429
  sans usage rendu (`journal-relais-kimi-v1.jsonl`). Écart de 1,30 USD à rapprocher dans `registres/depenses.md` par la mère.

*Fin d'écriture : 2026-11-09T15:41:38Z (`date -u`). Aucun compagnon `.sha256` écrit (consigne) ; l'empreinte de ce fichier
est rendue à la session mère.*
