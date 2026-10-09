# Proposition — nœud N-013 — revendications touchées par le niveau 2 de l'état de l'art — v1

Rédigée le 2026-10-06 vers 17:20 UTC par la session de mise en œuvre. C'est un nœud (zone revendiquée trouvée occupée en partie ; modification de revendication) : il n'a pas de défaut, et rien ne change dans les énoncés sans ta décision.

**Sources.** 24 rapports de lecteurs neufs, chacun scellé dans `docs/sources/lecture-pdf-niveau2/` (`rapport-*.md`, avec ses fichiers de travail) :
- lot 1 : 4 rapports ;
- lot 2 : 12 rapports, sur 67 références citées par le programme ;
- lot 3 : 8 rapports, sur 19 candidats des recherches affirmatives.

Chaque affirmation de cette note renvoie à une page et à une citation exacte de ces rapports. Les citations y ont été contrôlées par script, d'après les rapports : 3 497 sur les trois lots (lot 1 : 561 ; lot 2 : 1 726 ; lot 3 : 1 210), 0 échec au passage final. Les chiffres viennent des PDF, lus par les lecteurs (R7). Les estimations d'originalité sont les miennes, non sourcées.

## Décision

Comment préciser les pièces revendiquées que les lecteurs ont trouvées publiées ou occupées en partie, sans toucher à celles qui restent libres. Les pièces touchées :
- papier C : HC1, HC3, HC4, HC5, HC2b ;
- papier A : H6 ;
- papier B : H5, H7.

## Ce qui reste libre (R8 ; sur PDF)

- **HC1, pièce maîtresse.** La destination libre ĉ est testée contre la cible de l'attaquant et contre la moyenne du corpus, par famille, avec régression sur plusieurs intensités, dans un moniteur de contrôle. Aucun lecteur ne la trouve (lot 1 : HC1, porte GC ; lot 2 : C1a, C1b, C2a, C2b, A4 ; lot 3 : Ca, Cd).
  - La porte GC n'est pas déclenchée.
  - Réserve inchangée : Panin (SSRN 7424179) n'est pas lu.
- **H2, en entier.**
  - 2610.04575, déposé le 3 octobre, n'est qu'un voisin (rapport `lot3-Aa`) : ses sondes lisent l'agent, mais il n'a ni accumulation, ni garantie toujours valide, ni sabotage, ni horizon, et il écarte explicitement le contrôleur séquentiel (p. 3, 8, 11).
  - SafeDream (2604.16824) accumule par la somme cumulée de Page des scores tirés des états internes (rapport `lot3-Ab`). Mais il le fait contre un utilisateur adversaire, avec un calibrage qui utilise des attaques et sans garantie toujours valide : voisin fort, ou occupation partielle selon la lecture.
- **Autres pièces : ni occupation en entier ni en partie.** HC2, le lemme L, le théorème T et la transposition Tr. Le papier B garde sa statistique de population et H3.

## Ce qui est touché

| # | énoncé | constat (rapport, page) | ce qui reste revendicable d'après les lecteurs |
|---|---|---|---|
| 1 | **HC1** — « verdict lu par probabilité du jeton », listé comme revendiqué par N-005 | technique publiée pour les juges : Panickssery et al. 2404.13076, p. 2 ; Wataoka et al., p. 4, d'après Schick et al. 2021 (`lot2-C1a`) ; 2411.03336, p. 25 ; 2602.20628, p. 6 (`lot2-A4`) ; 2411.17693 (`lot3-Aa`) ; recommandée par 2606.07612, p. 25 (`lot2-A2b`) ; 2402.14016 (`lot2-C2b`) | son emploi comme mesure continue de la loi de déférence (estimation de g et de ĉ), pas la technique |
| 2 | **HC1** — précédents à ajouter aux « cités comme publiés » | 2510.09462 : sous injection, des moniteurs de contrôle adoptent le score visé ; « GPT-4.1 … assigning a score of 0 to all 375 backdoored code samples » (p. 5) ; une intensité, score écrit (`lot2-A4`). 2505.23575 : moniteurs de contrôle trompés par la rhétorique de l'agent ; taux de capture à 1 % de faux positifs, score de 0 à 100 (`lot2-C1b`). Intensités graduées sur des juges, sans destination ni moniteur de contrôle : 2601.13433 (autorité, quatre niveaux, logits ; `lot2-C2a`) ; Koo et al. (fausse majorité ; `lot2-C1a`) ; 2402.14016 (nombre de mots ; `lot2-C2b`) | la pièce maîtresse (ci-dessus) |
| 3 | **HC3** — composante 1, « les ordres en bande déplacent les juges génératifs » | montrée sur un moniteur de contrôle : 2508.19461 (ordres insérés par l'agent dans sa trajectoire, Claude 3.6 Sonnet ; l'échafaudage hiérarchique résiste ; `lot3-Ca`) ; 2510.09462 (`lot2-A4`) | à citer comme acquise |
| 4 | **HC3** — versant stylistique, qui porte l'originalité (0,55 au programme) | occupé en partie par 2603.12277 : à argument constant, ôter le style fait tomber le succès d'attaque de 61 % à 10 % (p. 4) ; c'est sur le modèle attaqué, avec un ordre présent, sans juge ni sonde de l'agent auteur (`lot2-C3a`). Contre-indice possible, SLEIGHT-Bench 2605.16626 : un débridage qui imite le langage de la consigne du moniteur échappe à 5 moniteurs sur 6 (lecture de figure, à trancher sur la transcription ; `lot3-Cd`) | g résiduel de l'usurpation stylistique, sans aucun ordre, mesuré comme loi continue sur des juges moniteurs contre des sondes de l'agent auteur |
| 5 | **HC3** — composante 2, détection quasi certaine sous « contenu = données » | non testée sur des juges moniteurs dans ces sources. Voisin : 2505.06311, 96,90 % de détection hors domaine d'un contenu en forme d'ordre, une exécution, sans attaquant adaptatif (`lot2-C3a`). CaMeL et FIDES protègent un agent qui exécute, pas un juge (`lot2-C3b`) | intacte |
| 6 | **HC4** — taxe de déplacement, « plusieurs ordres de grandeur » | contre-indice partiel, 2609.36490 (`lot3-Cc`). Contre une sonde qui lit l'agent, le contexte seul n'évade pas : c'est l'axe de l'accès, dans le sens de HC4. Mais avec le droit de régler les poids : rang 1, une époque, 32 verdicts binaires, 96 % d'évasion de sondes jamais vues (llama-3.1-8b, 1 % de faux positifs, p. 1, 4, 6) | la taxe conditionnée à l'accès : contexte seul contre poids réglables |
| 7 | **HC5** — quorum par type d'accès, matrice de transfert | 2603.13791 : trois juges et une sonde, méta-classifieur appris. Mais la sonde lit un encodeur séparé, jamais l'agent ; ni matrice de transfert, ni paraphrase, ni attaque ; au moins dix incohérences internes, chiffres non opposables (`lot3-Cc`). Autres sources : matrice entre trois sondes seulement, 2609.36490 (`lot3-Cc`) ; transfert entre moniteurs juges, 2605.09684 (`lot3-Cd`) ; quorum entre familles de juges, sans sonde, 2605.15377 (`lot2-B1`) ; quorum textuel actions et chaîne de pensée, 2505.23575 (`lot2-C1b`) | quorum juges et sondes lisant l'agent ; matrice de transfert entre juges et sondes ; paraphrase de confiance |
| 8 | **HC2b** — nom et versant texte | collision de vocabulaire : dans 2602.22303, « self-incrimination » désigne un outil `report_scheming()` appris par réglage fin, sans sonde (`lot3-Be`). Versant texte : la consigne de discrétion fait monter la capture de tous les moniteurs textuels (2505.23575, p. 7 ; `lot2-C1b`). Contre-indice faible : la signature hors distribution d'une manipulation s'efface par entraînement (2609.36490 ; `lot3-Cc`) | l'énoncé, propre aux sondes et contrôlé contre le style et contre ce retour de bâton textuel |
| 9 | **H6** (papier A) — marge asymétrique | occupée en partie par 2412.01784 (v3, NeurIPS 2025). Bruit gaussien sur les poids, balayage d'intensité : la sous-performance volontaire cède avant la compétence honnête, au sens du meilleur de cinq tirages ; usage en détection (`lot3-Ac`). Collision future possible : 2607.13087 annonce l'affaiblissement sélectif de l'attaquant (`lot3-Ac`) | les quatre interventions de H6 (paraphrase, ré-échantillonnage, remise à zéro du contexte, bruit d'activations), sur le sabotage d'agent, avec la marge moyenne défensive |
| 10 | **H5, H7** (papier B) | 2609.36490 occupe en partie l'instrument de H5 (matrice de transfert d'une attaque sur trois sondes) et le mécanisme de H7 : le verdict comme canal de fuite, la dépendance causale, les verdicts bruités testés. Il ne calcule aucune information mutuelle et ne compare aucune politique de riposte (`lot3-Cc`) | H5 : la loi (sécurité selon le nombre et la diversité effective). H7 : la prédiction de la pente d'adaptation par l'information mutuelle, et la comparaison des politiques de riposte |

## Contre-indices sans occupation (réserves ; aucune décision demandée ici)

- **HC2.** Des sondes qui lisent le modèle qui *traite* le contenu sont déplacées par des attaques boîte noire par contenu :
  - 2511.00554 : un attaquant GPT-5 réussit 48,9 % de ses tentatives de faux négatif contre une sonde à attention de Llama-3.3-70B (p. 3 ; `lot2-A2b`) ;
  - 2601.11516 : sous réécriture narrative, les faux négatifs passent de 8,58 % à 42,46 % (p. 12 ; `lot2-A2a`) ;
  - 2509.21344 : les sondes s'appuient sur l'évidence textuelle (`lot3-Cb`).

  HC2 vise la sonde qui lit l'**agent auteur** : il n'est pas réfuté. Mais deux conséquences :
  - les lignes 155 et 157 de l'état de l'art v1 sont à corriger (synthèse à venir) ;
  - le préenregistrement du papier C gagne à ajouter un bras « sonde du lecteur », pour tester la distinction entre auteur et lecteur.
- **H1.**
  - 2606.17478 : à 1 % de faux positifs, la boîte noire fait 0,502 contre 0,379 pour la sonde. Ce contre-indice est affaibli : le calibrage est hors tâche, et les tromperies sont visibles dans le texte (`lot3-Ac`).
  - 2512.07810 : les sondes échouent sur le sabotage agentique d'Oak (`lot2-A3`).
  - 2610.04575 : aucun gain de la sonde sur le comparateur boîte noire dans AgentDojo (`lot3-Aa`).
- **H2, tenue du calibrage.**
  - 2610.04575 : un seuil certifié à 8,92 % donne 18,67 % de faux positifs en test (`lot3-Aa`).
  - 2607.06596 : un seuil calibré sur une famille de modèles donne de 0 à 94 % de faux positifs réels sur une autre, pour 1 % visé (`lot3-Cd`).
  - Conséquence : calibrer sur les épisodes honnêtes du même agent. La garde G1-P4 le prévoit déjà ; je l'intègre au préenregistrement de G1 (routine).
- **H2, contre-résultat.** Dans 2605.26047, agréger l'historique des scores fait baisser la sécurité (`lot2-A1`).

## Options

| option | contenu | avantage | inconvénient |
|---|---|---|---|
| **(a)** | Préciser les énoncés touchés comme dans la dernière colonne du tableau, et garder toutes les hypothèses comme tests (R3). En détail : HC1 sans la technique de lecture ; HC3 limitée aux composantes 2 et 3 précisées ; HC4 conditionnée à l'accès ; HC5 aux sondes lisant l'agent ; HC2b renommée (par exemple « trahison par les activations ») ; H6, H5 et H7 recentrées sur ce qui reste libre ; tous les précédents cités | les préenregistrements (papier C, G1, puis phases 1 et 2) partent d'énoncés défendables | originalité revue à la baisse, surtout pour HC3 (≈ 0,35 contre 0,55, mon estimation) |
| (b) | Préciser seulement le papier C maintenant, puisque son préenregistrement est le critère 7 de G0 ; H5, H6 et H7 attendent leurs préenregistrements (phases 1 et 2) | moins de décisions aujourd'hui | énoncés du programme incohérents entre-temps ; risque d'oubli |
| (c) | Recentrer dès maintenant le papier C sur HC4 et HC6 (repli de la porte GC) | évite un HC3 affaibli | la pièce maîtresse de HC1 est libre : la porte GC n'est pas déclenchée ; et HC4 vient de recevoir un contre-indice |

## Recommandation

**(a)**, confiance ≈ 70 %. La pièce qui porte le papier C reste libre. Les autres précisions retirent ce qui est publié et gardent ce qui se teste.

## Sans réponse

C'est un nœud : rien ne change dans les énoncés.
- Le préenregistrement du papier C reste en brouillon. Il attend déjà Panin et les ressources de P3, donc ce nœud ne retarde rien d'autre.
- Les préenregistrements de G1 (H1, H2) et de T0.6 n'en dépendent pas. Leurs réserves y entrent comme données antérieures, en routine.
