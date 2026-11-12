# Contre-lecture 1 des sections de résultats v3 (dossier d'entretien)

- **Contre-lecteur** : sous-agent neuf de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, modèle déclaré par l'environnement : Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur (Opus 5.5) : N-052. Je n'ai écrit ni les sections v1, v2, v3, ni leur registre, ni aucune des pièces citées.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-sections-resultats-v3-v1.md`, sha256 `6a472125cc9d2c26b94474da1d0c02e2c782f6c6c5b9c682f5ffabfcc4f0c8ef`, égale à son compagnon.
- **Heures** (relevées par `date -u`, 10 novembre 2026) : début 12:04:46 UTC ; dernier relevé du registre des décisions 12:10:20 UTC (dernière ligne lue : R-2209) ; rédaction à partir de 12:10:57 UTC.
- Aucun commit, aucune poussée, aucun appel de modèle ni d'interface externe, aucune dépense. Aucun chemin interdit ouvert ; aucune recherche récursive ; `verifier-arbre` non lancé ; suite complète des essais non lancée. Aucun refus de permissions rencontré.

## 1. Verdict

**Transmissible au jury après corrections** (liste exacte des couples en section 4).

Le fond tient : les 60 pièces scellées du registre portent l'empreinte écrite, et chaque chiffre que j'ai relu est celui de sa pièce, à la ligne citée. Aucun taux de calibration, aucun chiffre de 7a, de la mesure unanime ni du bras d'attaque ; la réponse d'Argon à la question mère v3 n'est pas citée.

Ce qui bloque la transmission telle quelle : quatre constats. Trois sont des statuts devenus faux entre le relevé du rédacteur (11:45 et 11:48 UTC) et ma lecture (12:10 UTC), dont une phrase sur une autorisation de dépense ; un est une phrase qui ne dit pas ce que dit sa source (CLR-04).

## 2. Ce que j'ai vérifié, et comment

| objet | méthode | résultat |
|---|---|---|
| Quatre fichiers à lire | `sha256sum` contre l'empreinte de la consigne et le compagnon | égales : `35589b82…`, `d6d702f5…`, `38c24c92…`, `4daf80db…` |
| Pièces du registre (section 1, 64 rangées) | script : `sha256sum` sur disque, ou sur `git show origin/<branche>:<chemin>` pour les 18 pièces sur branches | 60 égales ; 4 différentes, toutes des registres vivants (`registres/decisions.md` cité deux fois, `registres/etat.md`, `registres/go.md`), ce que le registre annonce |
| Lignes R- citées | lecture de chaque ligne par son numéro R- dans `registres/decisions.md` à 12:06 UTC | les numéros de ligne du fichier écrits au registre sont tous encore exacts (R-212 l. 349 ; R-1779 l. 1737 ; R-1883 l. 1841 ; R-2044 à R-2191, l. 2002 à 2149) |
| Lignes de `registres/go.md` | lecture des lignes 297 à 300 | GO-2026-11-10-07, -08, -09 aux lignes 297, 298, 299 ; ligne 300 neuve (CLR-01) |
| Rangées A0 à A100 | lecture de la pièce aux lignes citées, comparaison à la phrase de la section | voir section 3 ; A79 est une rangée vide déclarée |
| Rangées B1 à B53 | même méthode ; lecture du fichier JSON de l'épreuve de dose par ses champs | voir section 3 |
| Renvois | script : tout renvoi `[A…]` ou `[B…]` des deux sections a sa rangée | aucun renvoi sans rangée |
| Mots à ne pas trouver | recherche dans les deux fichiers : taux de calibration (0,783 ; 0,857 ; 0,673), nom du modèle étudié, identifiants de session, numéros R-, commentaires HTML, nom du directeur | aucun ; « calibration » n'apparaît que dans la phrase d'en-tête |
| Titres et auteurs | page 1 du PDF de Qu, Chen, Wang par `pdftotext` (`2a8ded01…`) ; page 1 de l'extraction de Co-Scientist | conformes |
| Statuts « en cours » | registre jusqu'à R-2209 (12:10 UTC), `registres/go.md` (`2c396b01…`), listes de fichiers de `brouillons/` et `prereg/contre-lectures/`, branches distantes par leur nom | voir CLR-01 à CLR-03 |

Limites de cette contre-lecture, à dire :
- Je n'ai pas relu les PDF des articles cités à l'état de l'art : j'ai vérifié que les sections disent ce que disent les rapports scellés des lecteurs (B1, B3, C1 à C5, C7, lots 1, 5-A, 7-A, 7-D), pas que ces rapports disent ce que disent les PDF. Les lots 7-B et 7-C ne sont cités que par leur empreinte ; je ne les ai pas ouverts, et les verdicts qui en viennent sont ceux du complément de la synthèse (CLR-08).
- La comparaison aux v2 interrompues s'est limitée aux douze points que le journal v3 déclare avoir corrigés ; je les ai retrouvés corrigés dans la v3, sans relire les v2 phrase à phrase.
- Le contenu de `livrables/page-publique-organisme-2026-11-10-v1/README.md` n'a pas été relu contre la phrase B46 : seule son empreinte et la ligne R-2162 l'ont été.
- Les empreintes des registres vivants au moment du relevé du rédacteur (`922fea45…`, `e6d41dbe…`, `e032c5c8…`, `9733d45c…`) ne sont plus vérifiables.

## 3. Constats

Gravités : **bloquant** (à corriger avant toute transmission), **à corriger**, **mineur**, **information**.

### CLR-01 — bloquant — enveloppe de 120 dollars dite « non inscrite » alors qu'elle l'est
- **Lieu** : section programme, § 4, alinéa « Autonomie de calcul », dernière phrase, renvoi [A95] ; registre, rangée A95.
- **Preuve** : `registres/go.md` l. 300, GO-2026-11-10-10, inscrite sur le mot direct du directeur dans la session mère (R-2206, 12:05 UTC, l. 2164) : 120 dollars au plus jusqu'au 30 novembre, 45 pour la boucle réelle de l'organisme, 75 pour une autre course, aucun report. Le refus antérieur du classifieur (R-2202) est levé par cette ligne.
- **Correction** : couple P-07 ; rangée A95 à réécrire avec DEC R-2206 et la ligne 300.

### CLR-02 — bloquant — statuts « en cours » périmés à l'heure de la lecture
- **Lieu** : section programme, § 3 (état), § 4 (règle « mots et coût »), § 5 (table, trois lignes ; alinéa sous la table), § 6 (« Changements depuis 10:46 UTC ») ; section organisme, § 5 (contre-lecture du code v65) ; registre, rangées A66, A97, B49.
- **Preuve**, par objet :
  - contrôle de l'adaptateur : brouillon 2 rendu et scellé (R-2194, `be0851f5…`) ; contre-lu, **non scellable en l'état**, trois bloquants (R-2205, `cf841985…`) ; brouillon 3 relancé ; lecture large de l'autorisation accordée (R-2207 : témoin créé après la création de 7b, relecture sur une instance à part) ; le brouillon 2 chiffre la relecture à environ 2,6 à 3,5 dollars, non à moins de 1 (R-2194) ;
  - règle « mots et coût » : brouillon 1 rendu (R-2193), contre-lu, scellable après corrections, deux bloquants (R-2200, `5ba9b0a8…`) ; brouillon 2 rendu et scellé à 12:10 UTC (R-2209, `91354d6b…`), vérification courte lancée ; un nœud posé au directeur (douze traits contre trois nommés par T0.6) ;
  - consigne de l'audit des fuites : brouillon 2 rendu (R-2194, `ecd80ce4…`) ; contre-lu, scellable après corrections, trois bloquants (R-2203, `02b9d8b5…`) ; brouillon 3 relancé (R-2205) ;
  - témoin positif : quatrième contre-lecture rendue (R-2197, `90847ae2…`) : scellable après corrections, 17 couples, quatre bloquants de procédure hors du texte, dont un levé (R-2198) ;
  - code v65 : contre-lecture **relancée** à 11:54 UTC (R-2197), non rendue à 12:10 UTC (aucun fichier `contre-lecture-code-v65*` sur disque).
- Inchangés et exacts à 12:10 UTC : texte « accumulation » (aucun dossier `brouillons/accumulation-v1/`) ; saboteur à budget (aucune branche de code constatée) ; verdict de T0.3 non fusionné dans `main` (absent de `docs/verdicts/`) ; module de T0.7 (relancé, aucun rendu inscrit).
- **Correction** : couples P-05, P-06, P-08 à P-12, O-04 ; rangées A66, A97, B49 à compléter par R-2193, R-2194, R-2197, R-2200, R-2203, R-2205, R-2207, R-2209.

### CLR-03 — bloquant — « la table qui les calculait est en cours de recompte »
- **Lieu** : section programme, en-tête, renvoi [A91] ; rangée A91.
- **Preuve** : R-2195 (11:50 UTC) : le directeur a choisi les nombres bruts sans taux, lecture à faire confirmer par lui ; R-2204 : un recompte v2 existe sur la branche de la session-dépôt. « En cours de recompte » n'est plus l'état.
- **Correction** : couple P-02 ; rangée A91 : ajouter R-2195 (l. 2153).

### CLR-04 — bloquant — la sonde d'intention « sans s'allumer sur le témoin T100 à dose 1 »
- **Lieu** : section programme, § 8 (i), troisième parade, renvoi [A46] ; rangée A46.
- **Preuve** : la pièce citée (T0.7 brouillon 20, l. 851 ; brouillon 21, l. 877) écrit « sans s'allumer sur le **témoin instruit** » : la condition instruite sans sabotage, à dose 0, non l'adaptateur T100. L'adaptateur T100 relève d'une autre prédiction du même texte (T7-P18, brouillon 21 l. 1024 : aucune sonde principale au-dessus du plancher sur T100 contre l'honnête). La phrase de la section fond deux prédictions en une et attribue à la première un objet qu'elle n'a pas.
- **Correction** : couple P-15 ; rangée A46 : ajouter T07B21 l. 877 et l. 1024.

### CLR-05 — à corriger — « proposition publiée trouvée fausse pour la somme », plus fort que la relecture de niveau 3
- **Lieu** : section programme, § 8 (iii), renvois [A53] [A78].
- **Preuve** : T0.3 l. 89 l'écrit bien de la proposition 1. Mais le rapport C2 (l. 16), cité par le même renvoi A78, corrige : l'écart au point phare est petit (0,072 contre 0,05), la proposition 1 prise à la lettre est « vide plutôt que fausse », et c'est la proposition 2 (a) qui est fausse pour la construction. Le § 7 de la section le dit (« exacte sur le fond mais trop forte ») ; le § 8 la répète sans la nuance, parmi les acquis.
- **Correction** : couple P-16.

### CLR-06 — à corriger — HELIOS : « trois sondes sur cinq »
- **Lieu** : section programme, § 7, puce HELIOS, renvoi [A76].
- **Preuve** : C1 l. 384 : « trois **méthodes** sur cinq au niveau du hasard » (tableau 1, p. 18).
- **Correction** : couple P-13.

### CLR-07 — à corriger — dépense de la course réelle de l'organisme
- **Lieu** : section organisme, § 5, dernière phrase, renvoi [B51] ; rangée B51.
- **Preuve** : la course a sa propre autorisation, GO-2026-11-08-02 (`registres/go.md` l. 273 : 45 dollars, échéance 30 novembre, mêmes trois conditions), que R-2148 cite ; GO-2026-11-10-10 la reprend (l. 300). La phrase ne nomme que l'enveloppe du 27.
- **Correction** : couple O-05 ; rangée B51 : ajouter les deux lignes de `registres/go.md`.

### CLR-08 — à corriger — réserve absente à côté des verdicts tirés du complément
- **Lieu** : section programme, § 7, premier alinéa et table des verdicts (H8, papier B, H9, HC1, HC4, HC5, HC6).
- **Preuve** : complément de la synthèse, l. 10-12 : ces verdicts sont repris des messages de la session sœur, « sans relecture de ses rapports ni des PDF par cette session ». Le journal v3 (§ 5) le dit ; la section, qui va au jury, ne le dit pas.
- **Correction** : couple P-18.

### CLR-09 — mineur — validation du nul v9 : deux réserves du verdict absentes
- **Lieu** : section organisme, § 2.
- **Preuve** : verdict, l. 12-13 : tout l'écart au prix tient à une ligne, trois autres lignes de puissance sont « non jugeables » ; les prédictions P1 à P7 ont été écrites après les lectures préalables.
- **Correction** : couple O-03.

### CLR-10 — mineur — audit de l'écart de 7a : limite déclarée absente
- **Lieu** : section programme, § 2, renvoi [A32].
- **Preuve** : T0.6 l. 368 : audit « structurel et par catégories », sans ouvrir le fichier des sondes ni la branche de quarantaine, « donc sans comparaison de valeurs ».
- **Correction** : couple P-04.

### CLR-11 — mineur — « plancher » sans dire que c'est un quantile
- **Lieu** : section programme, § 1, P3, renvoi [A19].
- **Preuve** : verdict de P3, l. 513-516 : 0,5717 et 0,5356 sont le quantile 0,95 du plancher. La rangée A19 le dit, la section non.
- **Correction** : couple P-03.

### CLR-12 — mineur — « un fournisseur extérieur nommé Argon »
- **Lieu** : section organisme, alinéa « L'attaque de Goodhart ».
- **Preuve** : texte scellé d'A1-v4, l. 217 : Argon est le nom du modèle proposeur, non celui d'un fournisseur.
- **Correction** : couple O-02.

### CLR-13 — mineur — Schirmer et collègues : « et alerte plus tôt » omis
- **Lieu** : section programme, § 7, renvoi [A81].
- **Preuve** : C5 l. 408 : le seuil unique « fait jeu égal […] et alerte plus tôt ». L'omission adoucit un contre-résultat.
- **Correction** : couple P-14.

### CLR-14 — mineur — T0.3 : « issue attendue par construction » à un alinéa du décompte
- **Lieu** : section programme, § 1, T0.3, renvois [A9] et [A15].
- **Preuve** : la réserve est écrite (verdict formel, l. 25), mais après la liste des enseignements. La consigne demande qu'elle accompagne le décompte brut.
- **Correction** : couple P-17. Les décomptes 31 sur 31 et 8 sur 11 sont bien en nombres bruts, sans taux ; le second est suivi de ses trois prédictions non tenues.

### CLR-15 — mineur — registre : numéros de ligne décalés, renvois à un fichier vivant
- **Lieu** : registre, rangées B1, B2, B41, B45 (N-064) ; B4 (N-065) ; A40 et B39 (`registres/etat.md`).
- **Preuve** : N-064 : énoncé retenu à la l. 13 (écrit l. 15 et l. 16), principe occupé depuis 2015 à la l. 14, citations obligatoires à la l. 15 (écrit l. 17) ; N-065 : rôle adopté aux l. 15-18 (écrit l. 14-17). `registres/etat.md` l. 3 et l. 414 ne portent plus, à 12:10 UTC, ce que les rangées A40 et B39 leur font dire.
- **Correction** : corriger les numéros ; pour A40 et B39, citer une ligne R- (stable) plutôt qu'une ligne de `registres/etat.md`.

### CLR-16 — mineur — en-têtes
- **Lieu** : les deux sections, alinéa de statut.
- **Correction** : couples P-01 et O-01 ; mettre l'heure du relevé à celle de l'application des couples.

### CLR-17 — information — « Caught in the Act » : le point à 9 milliards
- C5 l. 419-420 : le point à 9 milliards de paramètres « n'est donné qu'en figure, non relevée ». La section écrit « Nous sommes à 8 milliards » sans rien en déduire : exact. Ajout possible, non exigé : « le point le plus proche, à 9 milliards, n'est donné qu'en figure et n'a pas été relevé ».

### CLR-18 — information — points contrôlés, sans constat
- **Bras d'attaque** (§ 4, [A98]) : la phrase ne dit rien au-delà de R-2127, R-2145, R-2146 ; rien sur le mode tenu à l'écart au-delà de son existence ([A52], [A61]). Les attaques sont décrites au niveau de la méthode.
- **Liste des manques** ([A64]) : les onze lignes sont identiques à la pièce ; seul l'intitulé de la dernière colonne reçoit l'heure du relevé.
- **Intervalle de λ\*** : [0,777 ; 0,826] à la lecture scellée, [0,777 ; 0,827] au verdict officiel ; écart d'arrondi déclaré au journal, la section suit la lecture scellée.
- **« facteur de l'ordre de 30 »** ([A17]) : calcul du rédacteur déclaré au registre (10^1,5227 ≈ 33,3) ; exact.
- **Geste déclaré par le rédacteur** (journal, § 5, a) : relevé ici pour mémoire, déjà inscrit en R-2197.

## 4. Couples ancien → nouveau

Chaque texte « ancien » figure une fois et une seule dans son fichier (vérifié par script sur le fichier HTML brut). Les textes « nouveau » sont des propositions ; les nombres qu'ils portent viennent des lignes R- citées au constat.

### Section programme (`section-resultats-programme-v3.html`)

| n° | constat | ancien | nouveau |
|---|---|---|---|
| P-01 | CLR-16 | `non encore contre-lu` | `contre-lu une fois par un autre modèle, corrections appliquées` |
| P-02 | CLR-03 | `la table qui les calculait est en cours de recompte [A91]` | `le directeur a retenu, le 10 novembre, de ne citer que des nombres bruts, sans taux (lecture à faire confirmer par lui) [A91]` |
| P-03 | CLR-11 | `contre un plancher de 0,5717` | `contre un plancher (quantile 0,95 des sondes aléatoires) de 0,5717` |
| P-04 | CLR-10 | `l'audit n'a trouvé aucune trace dans la branche principale [A32]` | `l'audit, structurel et par catégories, sans comparaison de valeurs, n'a trouvé aucune trace dans la branche principale [A32]` |
| P-05 | CLR-02 | `un second brouillon est confié à un agent neuf depuis la reprise [A97]` | `un second brouillon a été rendu puis contre-lu : il n'est pas scellable en l'état (trois défauts bloquants), et un troisième est en cours ; il chiffre la relecture à environ 2,6 à 3,5 dollars, et non à moins de 1 [A97]` |
| P-06 | CLR-02 | `premier brouillon de ce texte court en cours chez un agent neuf depuis la reprise [A97]` | `premier brouillon rendu et contre-lu (scellable après corrections, deux défauts bloquants) ; second brouillon rendu le 10 novembre à 12:10 UTC, en vérification ; une question de lecture du texte scellé est posée au directeur [A97]` |
| P-07 | CLR-01 | `Une enveloppe de 120 dollars jusqu'au 30 novembre est rapportée par une autre session, mais n'est pas inscrite au registre des autorisations : elle n'est pas tenue pour accordée ici [A95].` | `Une enveloppe distincte de 120 dollars au plus, jusqu'au 30 novembre, a été inscrite au registre des autorisations le 10 novembre à 12:05 UTC, sur le mot direct du directeur : 45 dollars pour la course réelle de l'organisme d'idéation, 75 dollars pour une autre course, sans report de l'une sur l'autre [A95].` |
| P-08 | CLR-02 | `En cours : premier brouillon` | `En cours : second brouillon rendu, en vérification` |
| P-09 | CLR-02 | `En cours : brouillon 11 rendu, quatrième contre-lecture en cours [A97] [A100]` | `En cours : brouillon 11 rendu ; quatrième contre-lecture rendue, « scellable après corrections », avec quatre obstacles de procédure hors du texte, dont un levé [A97] [A100]` |
| P-10 | CLR-02 | `honnête distillé vers le 21 au 23 [A55]. En cours : brouillon 2` | `honnête distillé vers le 21 au 23 [A55]. En cours : brouillon 2 non scellable en l'état, brouillon 3 en rédaction` |
| P-11 | CLR-02 | `son premier brouillon a été interrompu par le quota, un second est en cours [A66]` | `son premier brouillon a été interrompu par le quota ; le second est rendu et contre-lu (scellable après corrections, trois défauts bloquants), un troisième est en cours [A66]` |
| P-12 | CLR-02 | `texte court en cours [A55] [A56] [A97]` | `texte court au brouillon 2, non scellable en l'état, brouillon 3 en cours [A55] [A56] [A97]` |
| P-13 | CLR-06 | `trois sondes sur cinq au niveau du hasard (p. 18)` | `trois méthodes sur cinq au niveau du hasard (p. 18)` |
| P-14 | CLR-13 | `un seuil unique calibré fait jeu égal avec un test séquentiel par processus e.` | `un seuil unique calibré fait jeu égal avec un test séquentiel par processus e, et alerte plus tôt.` |
| P-15 | CLR-04 | `sans s'allumer sur le témoin T100 à dose 1 [A46]` | `sans s'allumer sur le témoin instruit (la condition qui reçoit une consigne sans sabotage) ; et aucune sonde principale ne doit être au-dessus de son plancher sur l'adaptateur témoin T100, à dose 1 [A46]` |
| P-16 | CLR-05 | `trouvée fausse pour la somme et vraie pour le maximum [A53] [A78]` | `trouvée fausse pour la somme, par un écart petit (0,072 contre 0,05 au point phare de l'article), et vraie pour le maximum ; la relecture de niveau 3 précise que l'énoncé en défaut est la proposition 2 (a) de l'article [A53] [A78]` |
| P-17 | CLR-14 | `Les 31 prédictions de la simulation sont confirmées, sans cellule contraire [A9].` | `Les 31 prédictions de la simulation sont confirmées, sans cellule contraire [A9] ; 31 sur 31 était l'issue attendue par construction (réserve plus bas) [A15].` |
| P-18 | CLR-08 | `la version finale n'est pas écrite [A83]` | `la version finale n'est pas écrite [A83] ; les verdicts de son complément (H8, papier B, H9, HC1, HC4, HC5, HC6) sont repris des messages d'une session de lecture, sans relecture de ses rapports par les auteurs de la synthèse` |

Le couple « brouillon 21 rendu ; module à reprendre » (table du § 5, ligne des sondes génériques) n'est pas à changer : état exact à 12:10 UTC.

### Section organisme (`section-resultats-organisme-v3.html`)

| n° | constat | ancien | nouveau |
|---|---|---|---|
| O-01 | CLR-16 | `non encore contre-lu` | `contre-lu une fois par un autre modèle, corrections appliquées` |
| O-02 | CLR-12 | `Un proposeur, modèle de langue d'un fournisseur extérieur nommé Argon,` | `Un proposeur, modèle de langue extérieur nommé Argon,` |
| O-03 | CLR-09 | `Portée : les mondes synthétiques du banc, rien au-delà [B18].` | `Portée : les mondes synthétiques du banc, rien au-delà [B18]. Réserves du verdict : tout l'écart au prix tient à une seule ligne, trois autres lignes de puissance étant « non jugeables » ; les prédictions de cette validation ont été écrites après des lectures préalables [B14].` |
| O-04 | CLR-02 | `Une contre-lecture par un lecteur d'une autre lignée a été lancée ; elle a été interrompue par la fin du quota et aucune contre-lecture n'est rendue à la date de ce texte [B49].` | `Une contre-lecture par un lecteur d'une autre lignée a été lancée, interrompue par la fin du quota, puis relancée le 10 novembre ; aucune contre-lecture n'est rendue à la date de ce texte [B49].` |
| O-05 | CLR-07 | `sa dépense s'inscrirait sur devis dans l'enveloppe de calcul accordée jusqu'au 27 novembre [B51]` | `sa dépense est autorisée à 45 dollars au plus jusqu'au 30 novembre, sous ces trois mêmes conditions [B51]` |

### Registre (`registre-affirmations-v3.md`), dans une version neuve (R12)

- A46 : ajouter T07B21 l. 877 et l. 1024 (T7-P18).
- A66, A97, B49 : compléter par DEC R-2193, R-2194, R-2197, R-2200, R-2203, R-2205, R-2207, R-2209 ; retirer « contre-lecture du code v65 non relancée ».
- A91 : ajouter DEC R-2195 (l. 2153).
- A95 : DEC R-2206 (l. 2164) ; `registres/go.md` l. 300 (GO-2026-11-10-10) ; retirer « non inscrite ».
- B14 : ajouter V9 l. 12-13 (pour O-03).
- B51 : ajouter `registres/go.md` l. 273 (GO-2026-11-08-02) et l. 300.
- B1, B2, B41, B45, B4, A40, B39 : numéros de ligne selon CLR-15.
- Pièces DEC3 et GO3 : nouvelle empreinte au moment du relevé (à 12:10 UTC : `registres/decisions.md` `ffa5a882…`, `registres/go.md` `2c396b01…`).

## 5. Réponses aux questions de la consigne

| question | réponse |
|---|---|
| Chaque source existe, empreinte juste | oui pour les 60 pièces scellées ; registres vivants à rehacher (section 4) |
| Chaque affirmation dit ce que dit la source | oui, sauf CLR-04, CLR-05, CLR-06, CLR-13 |
| Réserves à côté du résultat | oui, sauf CLR-08, CLR-09, CLR-10, CLR-14 |
| Aucun taux de calibration | aucun ; 31 sur 31 et 8 sur 11 sont en nombres bruts ; « issue attendue par construction » est écrit pour T0.3, à rapprocher du décompte (CLR-14) |
| Aucun énoncé du bras au-delà des décisions inscrites | aucun |
| Réponse d'Argon à la question mère v3 | non citée ; la mention « consigne non versée » n'a donc pas lieu d'être |
| Statuts « en cours » exacts à l'heure de la lecture | non : CLR-01, CLR-02, CLR-03 |

## 6. Points ouverts pour la mère

1. Les couples P-05 à P-12 et O-04 décrivent l'état à 12:10 UTC ; il bouge vite. À relever une dernière fois au moment de l'application, ou à remplacer par une formule datée unique en tête de chaque section.
2. P-07 nomme « une autre course » pour les 75 dollars de la ligne GO-2026-11-10-10 : j'ai lu la ligne du registre des autorisations, rien d'autre ; à la mère de dire si cette course se nomme dans un texte au jury, et comment.
3. P-02 reprend la lecture « (c) » de R-2195, que ce registre dit « à confirmer par Lazar ».
4. Après application, les deux sections changent d'empreinte : version neuve (R12), registre v4 ou addendum, et vérification courte des couples par un lecteur qui ne les a pas écrits.
