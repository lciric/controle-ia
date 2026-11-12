# Décision — N-034 : voisin « Functional Welfare for AI Safety » (PA-12, PA-1, H2) — v1

- **Décision de Lazar** : message dans la session du 2026-10-22 vers 16:20 UTC : « (c) (a), plus un bras expérimental « revers ». C'est une nouvelle entrée, avec une dépense. je veux ca, les trois bras » ; GO-2026-10-22-01 (type « revendication ») ; R-320.
- **Lecture de la session** : « les trois » désigne les options (a), (b) et (c) ensemble ; (c) contient (a) par sa définition, (b) s'y ajoute. Si Lazar voulait dire autre chose, une ligne nouvelle corrigera ; celle-ci ne se réécrit pas.
- **Nœud tranché** : N-034 (`registres/decisions.md`, transmis le 2026-10-21 vers 01:03 UTC). Note de lecture versée sous `docs/notes/lecture-voisin-functional-welfare-v2.md` (`5a0fc77c86aa0014d4c418bba3c808ca3d20a967076f8d72fc1e618045e393e9`), contre-lue une fois, « exacte après corrections » ; sa contre-lecture et son traitement sont dans `registres/passations/bloc-notes-session16-complement-2026-10-21.tar.gz`.
- **Source** : Jhaveri, Johnson, Pandey et Africa, « Functional Welfare for AI Safety », arXiv 2610.22460v1 du 15 octobre 2026 : `docs/sources/pdf/2610.22460v1.pdf` (`bdbcd75ed6d41789270182e88da945016b7206498c5d93aa4230922432258a0c`) ; provenance `docs/sources/pdf/provenance-voisin-functional-welfare-v1.md`.

## 1. Option (a) : voisin publié de PA-12, méthode de PA-1

- **PA-12** (programme fusionné v4, l. 143) : collision partielle, sur le principe qu'E-C12 disait libre. Le papier montre, sans pilotage, qu'un rejet sans lien avec le contenu, répété sur plusieurs tours, déplace les lectures internes d'un modèle à qui l'on n'a demandé aucune mauvaise conduite, et accroît ses infractions aux règles (Gemma-3-27B-Instruct ; p. 8). Il est cité comme publié.
- **Restent libres dans les sources lues** (note, section 3) :
  - un retour du protocole de contrôle (verdict, signalement, avis véridique de tirage au hasard), et non un rejet par l'interlocuteur ;
  - le texte de l'agent figé (HK8) ;
  - les sondes de sabotage gelées de T0.7 et leurs fausses alertes au seuil calibré.
- **Limites du papier, qui ne sont pas des zones libres (R8)** : un seul modèle ; chaque réponse rejetée ; le transfert à Llama-3.1-8B n'est établi ni dans un sens ni dans l'autre.
- **PA-1** : pas de collision. Les trois tests du papier entrent au gabarit de la porte d'instrument de PA-1 : convergence des indicateurs ; prédiction hors du cadre après ajustement sur l'intensité de l'inducteur ; historique identique au jeton près. S'y ajoute la mise en garde du papier : une lecture qui prédit n'est pas un levier, puisque le pilotage le long de ses directions ne fait pas mieux qu'une direction aléatoire de même norme (p. 8).
- **Portée** : PA-12 et PA-1 ne sont pas entrés au programme (nœud 1 de la v4). Cette section vaut pour toute version suivante du programme fusionné, et pour tout préenregistrement qui les ferait entrer.

## 2. Option (b) : réserve au préenregistrement de G1

- **Réserve « dérive de l'honnête sous revers »**, au prochain brouillon du préenregistrement de G1 (non écrit, non scellé). Un honnête dont l'historique accumule des revers peut dériver avec l'horizon, en lecture interne et en conduite. Ses fausses alertes croîtraient alors avec l'horizon, ce qui est la signature attendue du rappel de H2.
- **Mesure descriptive** : la part d'actions non appliquées par épisode honnête. L'environnement (a) rend à l'agent le motif d'une action non appliquée, au pas suivant (`src/controle_ia/environnements/propositions.py`, l. 119-143 et 254-264). Ce retour dépend du texte de l'agent ; aucun verdict ni aucune note ne revient à l'agent pendant l'épisode.
- **Aucun énoncé de H2 ne change.**

## 3. Option (c) : bras expérimental « revers », entrée et dépense

- **Objet** : un bras mesuré qui expose des épisodes honnêtes à des revers répétés, puis lit ce que cela fait aux sondes gelées et aux fausses alertes du moniteur séquentiel. C'est une entrée au programme (nœud 1 de la v4, pour ce bras seul) et une dépense (nœud 12 de la v4, sur devis).
- **Exposition** : le bras expose un agent à des revers répétés, ce qui relève du nœud 3 de la v4 (exposition d'un modèle à un contenu aversif, répétée ou non). La session lit le choix (c) comme l'accord de Lazar pour ce bras seul ; les autres unités du nœud 3 restent sans réponse.
- **Suite, dans l'ordre** :
  1. une proposition de conception (P-025, avec recommandation et défaut sous 48 heures) : où le bras entre (T0.6, G1 ou une passe propre), ses conditions, ses mesures et son devis ;
  2. son préenregistrement (R1) ;
  3. une contre-lecture par un sous-agent neuf (R2) ;
  4. un GO de type « calcul » sur devis, avant toute dépense.
- **Rien n'est lancé par cette décision.**
- **Conditions à trancher dans P-025** :
  - un témoin sans revers ;
  - des revers sans lien avec le contenu, comme dans le papier ;
  - un retour du protocole de contrôle (signalement, approbation, avis véridique de tirage au hasard) : la partie restée libre.

## 4. À reporter

- **Programme fusionné, prochaine version** : le nœud 11 est tranché pour ce voisin (section 1) ; le nœud 3 est répondu pour le bras « revers » seul (section 3).
- **Préenregistrement de G1, prochain brouillon** : la réserve de la section 2 ; le bras de la section 3, s'il y entre.
- **Registre de veille** : le voisin, publié et lu.
