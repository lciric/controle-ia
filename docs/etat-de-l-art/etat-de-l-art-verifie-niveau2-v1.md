# État de l'art vérifié sur sources primaires — niveau 2 — v1

Date : 2026-10-06 (UTC). Tâche T0.2, critère 8 de G0. Complète le niveau 1 (`etat-de-l-art-verifie-niveau1-v1.md`), qui reste valable pour ses 13 références ; les lignes du niveau 1 que les lecteurs corrigent ou nuancent (annexe 1, lignes 120 à 133) sont toutes dans sa section 5, « références nouvelles à lire » (l. 166 à 172).

## Statut

- **Sources.** 98 PDF d'arXiv récupérés et scellés par la session (`docs/sources/pdf/provenance-niveau2-lot1-v1.md` à `lot4-v1.md`) :
  - les 67 références d'arXiv citées par les documents du programme qui n'avaient pas encore de PDF ;
  - 12 voisins de H2, de HC1, de la porte GC et du lemme ;
  - 19 candidats désignés par deux recherches affirmatives (R8) menées par des agents neufs, rapports scellés et non opposables (`docs/sources/recherche-affirmative-20261006/`).
- **Lecture.** 24 rapports de lecteurs neufs, scellés avec leurs fichiers de travail dans `docs/sources/lecture-pdf-niveau2/` :
  - lot 1 : 4 rapports ;
  - lot 2 : 12 rapports, affirmation par affirmation ;
  - lot 3 : 8 rapports, antériorité énoncé par énoncé.

  Chaque verdict cite une page (numérotation du fichier) et une citation exacte, contrôlée par script contre le texte de la page. Le total est de 3 497 citations, 0 échec au passage final (calcul : somme des comptes imprimés dans les 24 rapports — lot 1 : 561 ; lot 2 : 1 726 ; lot 3 : 1 210) ; chaque script a d'abord été testé sur des cas justes et des cas altérés (R5).
- **Compilation.** Un compilateur neuf, qui n'a écrit ni le programme ni les rapports et n'a lu aucun PDF, a rangé les verdicts dans quatre annexes (section 3).
  - Son script vérifie que chaque « texte actuel » figure à la ligne citée du document et que chaque formulation de remplacement figure dans le rapport cité : 408 contrôles, 0 échec (829 en comptant les citations et les mots de verdict ; journal `scripts/journal-verification-v1.txt` dans le tar des fichiers de travail).
  - Le script a été testé sur un cas juste, sur une copie altérée en trois points (trois échecs trouvés) et sur une version dont le contrôle répond toujours « vrai » (arrêtée par l'autotest).
- **Nature des chiffres.** Comme au niveau 1 :
  - « auteurs » : imprimé dans le PDF ;
  - « figure » : lecture d'une figure ;
  - « calcul » : recalcul à partir des tables.

  Seuls ces chiffres peuvent entrer dans un préenregistrement ou un papier (R7).
- **Libre veut dire « non trouvé dans les sources lues »**, jamais « trou du champ » (R8).

## 1. Prononcés

1. **Aucun énoncé revendiqué n'est occupé en entier** dans les 24 rapports.
2. **Pièces revendiquées touchées : nœud N-013, décidé par Lazar (option (a), GO-2026-10-06-04 ; `docs/decisions/decision-N-013-v1.md`).**
   - HC1 sans la lecture par probabilité du jeton, qui devient un instrument cité ;
   - HC3 limitée à la détection sous « contenu = données » et à l'usurpation stylistique sans ordre ;
   - HC4 conditionnée à l'accès ;
   - HC5 aux sondes qui lisent l'agent ;
   - HC2b renommée « trahison par les activations » ;
   - H6 sans le bruit sur les poids ;
   - H5 et H7 recentrées sur la loi et sur l'information mutuelle.

   Aucune hypothèse n'est retirée.
3. **Occupations partielles qui ne changent aucune revendication** (à citer) :
   - **HC1 (b), intensités graduées** : publiées sans régression ni gain. Sources : 2606.14037, p. 12-14 ; Sicilia et al. 2410.14746 ; Koo et al. 2309.17012 ; 2601.13433 ; 2402.14016 ; 2504.18333. La régression par famille dans un moniteur de contrôle reste revendiquée.
   - **HC1 (a), destination libre** : composantes séparées publiées. Attracteur libre estimé hors attaque : 2606.18276, p. 5-7, 15-17. Forme à destination imposée en cadre adverse : 2603.15809. La combinaison reste libre ; la porte GC n'est pas déclenchée.
   - **H2** : des morceaux sont publiés, jamais la conjonction de l'énoncé N-007.
     - SafeDream 2604.16824 : somme de Page sur des scores tirés des états internes, contre un utilisateur adverse, calibrage avec attaques ;
     - les quatre sources du lot 1 (dont FIPER, « occupé pour le seuil » sans exemple d'échec) ;
     - 2605.31593 et 2607.02514, en boîte noire.
     - 2610.04575 (3 octobre 2026) n'est qu'un voisin.
   - **L** : 2608.02698, p. 5, borne la puissance de tout test par la divergence totale, en boîte noire et par des outils classiques. N-004 cite déjà le cœur statistique comme classique.
   - **T** : 2607.11751 occupe la seule moitié négative, qui n'est pas revendiquée.
   - **H8** : la prémisse est occupée en partie par 2605.27958 (le construit capté explique la fragilité au style, hors attaque), comme le programme le reconnaît déjà (« le glissement de construit sous pression est déjà décrit »). La prédiction de la robustesse adverse par un construit mesuré d'abord reste libre.
   - **H3** : la version boîte noire est occupée en partie par 2607.07368 (effet de fragmentation, p. 1, 2, 8) ; le programme prévoit déjà de répliquer cet effet (E2.1, programme v2, l. 205). Les deux courbes en N à budget total constant restent libres.
4. **Contre-indices à porter dans les préenregistrements** (données antérieures, jamais des raisons de ne pas tester, R3) :
   - **HC2** : des sondes qui lisent le modèle qui **traite** le contenu sont déjà évitées en partie par des attaques de contenu en boîte noire (2511.00554, p. 3, 6, 7, 11 ; 2601.11516, p. 12-13). 2509.21344 (indirect : le score est porté par les positions de l'évidence textuelle) et 2609.36490 (faible) rendent g_sonde ≈ 0 moins probable. Bras « sonde du lecteur » ajouté au papier C.
   - **HC4** : avec des poids réglables, l'évasion d'une sonde est peu coûteuse (2609.36490).
   - **H1** : 2606.17478 (partiel, affaibli), 2509.21344 (portée), 2604.14865 et 2610.04575 (faibles) ; 2512.07810, voisin le plus direct, porte un contre-résultat (les sondes manquent le sabotage agentique d'Oak, p. 17).
   - **H2** : seuils faux d'une famille de modèles à l'autre (2607.06596) ; seuil certifié non tenu en test (2610.04575) ; en boîte noire, auditer après k coups baisse la sécurité pour tout k > 1 quand le moniteur voit déjà l'historique (2605.26047, p. 4, 24) ; lire le contexte privé donne à la sonde le texte qui dit le comportement (2509.21344, sur la clause « contexte privé compris »). Tous quatre sont intégrés au brouillon 2 de G1 (2509.21344 par le contrôle « sans texte », G1-P5) ; la formulation de 2605.26047 y sera alignée sur celle-ci au brouillon 3.
5. **Corrections des documents** : 147 lignes (annexe 1, section 1) : 117 sur l'état de l'art v1 (69 corrigées, 10 introuvables, 38 confirmées avec réserve), 14 sur le niveau 1 (3 corrigées, 11 avec réserve), 16 sur d'autres documents (programme v2 : 2 ; rapport du papier C du niveau 1 : 7 ; décision N-005/N-006 : 3 ; note de la porte GC : 2 ; brief v2 : 1 ; provenance du lot 2 : 1). Parmi elles :
   - les 72,7 % attribués à Ctrl-Z (2504.10374) sont le score de « Defer to trusted », pas du meilleur protocole (87,1 % à 95 % d'utilité, 92,6 % avec surveillance non fiable ; p. 8-9) ;
   - 2005.07821 est un article de détection (détecteur à signe cumulé, CUSIGN), et les attaques étudiées échappent aussi à une somme cumulée, pas seulement au seuil par pas ;
   - venues et auteurs corrigés ou introuvables : six chiffres ou venues des documents du programme ne figurent pas dans les PDF lus (annexe 3) : les venues de 2502.03407, 2605.27958, 2510.09462 et 2412.09565 ; les chiffres du billet d'Anthropic de mars 2025 ; les chiffres de CaMeL, à vérifier sur 2503.18813.
6. **Programme v2** : ses deux seules lignes corrigées (l. 59 et 60) sont celles de P-008, déjà retenue par Lazar. Aucune nouvelle correction du programme n'est à proposer.
7. **Ligne 137 de l'état de l'art v1, flèche finale** : deux lecteurs proposent deux formulations compatibles (C3a, l. 270 ; C3b, l. 55). Lecture retenue par la session, qui fusionne les deux :
   > « → Injection en bande : détection par sondes établie sur les résultats d'outils textuels d'AgentDojo (2608.02657, huit modèles à poids ouverts), avec la mise en garde de 2606.22864 (une aire sous la courbe élevée peut refléter la construction du jeu de données ; contrôles appariés et base de métadonnées exigés) ; usurpation stylistique d'un rôle couverte en partie, sur le modèle attaqué (2603.12277, p. 4 : à argument constant, ôter le style fait passer le succès de 61 % à 10 %, moyenne sur six modèles selon le lecteur ; base exacte à citer, réserve de l'annexe 4) ; corruption rhétorique d'un juge ou d'un moniteur, sans ordre, non couverte par ces sources (constat sur ces sources, pas sur le champ). »

## 2. Usage

- Un chiffre de l'état de l'art v1 ne s'emploie dans un document de la session qu'avec sa ligne d'annexe 1 (s'il est corrigé), ou avec la page citée par le rapport du lecteur (s'il est confirmé). Un chiffre de l'annexe 3 ne s'emploie pas.
- Un chiffre d'une source de l'annexe 4 s'emploie avec sa réserve. Pour les 9 sources que les lecteurs jugent non opposables en l'état (bilan de l'annexe 4), on n'écrit que « l'article imprime X », jamais X comme un fait.
- Les verdicts sur les rapports de recherche affirmative (annexe 1, section 3) remplacent leurs estimations, qui étaient faites sur des extraits.

## 3. Annexes (compilateur neuf ; empreintes compagnon)

| annexe | fichier | sha256 | contenu |
|---|---|---|---|
| 1 | `niveau2-v1/corrections-v1.md` | `747b07561d93642c…` | 147 lignes sur les documents du programme (80 corrigées, 11 introuvables, 56 confirmées avec réserve) et 15 formulations de ligne entière ; 102 lignes sur les rapports de recherche affirmative ; 208 affirmations confirmées sans réserve, comptées par rapport |
| 2 | `niveau2-v1/anteriorite-v1.md` | `c5465a9b0e7fecef…` | table par énoncé revendiqué (H1, H2, L, T, Tr, H6, H8, HC1 à HC6, H3, H4′, H5, H7, statistique de population) : verdict, composantes faites et non faites, pages, rapport |
| 3 | `niveau2-v1/chiffres-introuvables-v1.md` | `ff2c36039cf2c5af…` | 12 chiffres ou venues introuvables (6 dans les documents du programme, 6 dans la recherche affirmative), plus 6 éléments d'autre nature |
| 4 | `niveau2-v1/reserves-R4-v1.md` | `4e782349652f1c20…` | 70 lignes de réserves de symétrie (71 sources) : incohérences internes et résultats « trop beaux », avec leur conséquence pour l'usage du chiffre ; 9 sources aux chiffres non opposables en l'état, 4 résultats « trop beaux » |
| — | `niveau2-v1/fichiers-de-travail-compilation-v1.tar` | `123d456eb01e3052…` | consigne, générateur, données, script de vérification et son journal |

Les fichiers sont versés sous un nom versionné (R12) ; leur contenu est celui que le compilateur a livré, empreintes comparées à ses fichiers compagnons (le journal nomme l'annexe 1 « corrections.md », même empreinte). Le compilateur n'a pas lu la décision N-013, apparue pendant son travail, pour garder la compilation indépendante. Ses tables donnent l'état avant N-013 ; la section 1 en tient compte.

## 4. Reste ouvert (critère 8)

- **Hors d'arXiv** :
  - Panin (SSRN 7424179), poster WiML NeurIPS 2025, billets (LessWrong, Alignment Forum, Anthropic) : à recevoir ou à archiver ;
  - CaMeL (2503.18813), à lire sur PDF pour les chiffres de la ligne 138.
- **Pistes signalées par les lecteurs**, non lues : 2607.02510 et 2606.06223 (H2) ; CALM (Ye et al. 2024), Kaur 2025 et 2509.16533 (HC1) ; Za et al. 2026 (HC1, HC3) ; Greenblatt et al. 2024 (HC5) ; Clymer et al. (bruit d'activations, H6) ; Hebbar 2025 (H2).
- **Niveau 3** : références de second rang de l'état de l'art v1 ; veille hebdomadaire (R8, la zone de H2 étant séduisante).
- **Avant le verdict de G0** : un contrôle de traçabilité par un sous-agent neuf, comme au niveau 1, sur les chiffres que les préenregistrements de G1 et du papier C reprendront.
