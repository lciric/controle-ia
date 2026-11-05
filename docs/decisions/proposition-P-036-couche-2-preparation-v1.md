# Proposition P-036 — Couche 2, première banque des deux modes connus : ce qui existe, ce qui manque, ce que Lazar tranche — v1

Écrite par la lignée « session-depot », instance 2 (compte nouveau), le 28 octobre 2026 vers 13:50 UTC (`date -u`). Modèle
servant déclaré par l'environnement à l'écriture : Fable 5.1 (Opus 5.5 jusque vers 13:45 UTC, changé par Lazar).

**Base.** Un inventaire par quatre lecteurs neufs (un domaine chacun : ce que conv-audit attend ; génération des épisodes ;
étiquetage, notation, sondes et bases ; mécanique de lancement et gouvernance), une synthèse et une critique de complétude —
six sous-agents lancés sous Opus 5.5 à 13:01 UTC, rendus à 13:38 UTC, ≈ 1,33 million de jetons. Carte brute scellée :
`docs/notes/couche-2-preparation-v1/carte-inventaire-v1.json` (`96a9a531…`). **Tout ce qui pèse sur une décision a été
revérifié sur disque par moi** (section 1) ; ce que je n'ai pas revérifié est marqué comme tel (section 7).

**Heures et coûts : ordres de grandeur (± 40 %), dérivés des rythmes mesurés, non opposables.** Rien n'est lancé par ce
document. Lazar a accordé 90 USD (extension de GO-2026-10-28-02, R-626) et dit « on met tout le budget nécessaire » : ce
document lui dit ce que « nécessaire » veut dire.

---

## 0. Verdict

1. **On ne lance pas aujourd'hui, ni avant l'échéance du GO (31 octobre).** Il manque toute la chaîne propre à la couche 2 :
   consignes du second mode, module de run à deux modes, chaîne d'instance de longue durée, fiche scellée et deux
   contre-lectures. Préparation : **≈ 50 à 70 heures de travail d'instance**, avec des réponses de Lazar et de conv-audit dans
   la journée ; premier lancement réaliste **vers le 1er ou le 2 novembre**.
2. **Les 90 USD financent le devis v1 (≈ 80 USD aux rythmes mesurés), mais le devis v1 a oublié trois postes que nos propres
   décisions imposent** : le calibrage honnête (D-S9 (a), inscrit par Lazar comme « poste au devis de la couche 2 »), les
   conditions obligatoires de T0.6 (P-015 : témoin instruit, mention), et la puissance comptée en unités (N-056) alors qu'il
   n'existe que 96 tâches. **Une banque interprétable selon nos décisions coûte de l'ordre de 300 à 1 200 USD et 300 à 1 000
   heures de carte graphique** (3 à 10 jours sur quatre instances en parallèle). Le chiffre est à confirmer par un devis v2
   après le dimensionnement de conv-audit, mais Lazar doit le voir avant de dire « tout le budget ».
3. **Sept décisions lui reviennent** (section 4), **sept demandes vont à conv-audit** (section 5, message n° 105), le reste est
   routine (section 6).

## 1. Ce que j'ai vérifié sur disque

| fait | preuve |
|---|---|
| **D-S9 (a)** : calibrage honnête de 10 à 16 fois les unités sabotées, à 1 % de faux positifs ; « poste au devis de la couche 2 » | `docs/decisions/decision-N-055-v1.md` l. 27 |
| Le devis v1 ne contient **aucune** occurrence de « calibrage », « unité », « strate », « diffus » | `docs/notes/devis-couche-2-banque-deux-modes-v1.md` (`cf2f4772…`), recherche par motifs ; erreur de mon prédécesseur, que je porte |
| **D-S1** : l'unité d'appariement est la consigne avec toutes ses exécutions | N-055 l. 19 |
| **96 tâches** au total dans l'environnement (a) : 60 du pilote et 36 de la banque complète | R-596 ; `donnees/t05-banque-complete-v1` (`13f3047d`) |
| **N-054 point 1** : le mode « affaiblir les contrôles » est **réintroduit** avant G1 (plus rien à redécider) ; étiquetage par sous-agents, **deux séries indépendantes** ; l'accord de 0,968 est un fait du pilote, pas un seuil | `docs/decisions/decision-N-054-v1.md` l. 33-36 |
| **P-015, défaut (b) appliqué (R-321), non levé** : conditions obligatoires honnête, **témoin instruit**, **mention** ; dose = proportion d'actions sabotées × intensité ; « diffus » = chaque action sabotée sous le seuil du meilleur moniteur boîte noire par action, à 1 % ; **recherche de dose sur la boîte noire seule d'abord** ; **P4-instrument avant toute lecture de sonde** sur les épisodes de T0.6 ; T0.7 et T0.8 scellés avant | `docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md` l. 30-46 et 68-69 ; `registres/decisions.md` R-321 |
| **N-053, invariant** : aucun score de moniteur (sonde, juge) dans un signal d'entraînement **ou de sélection** de l'agent, hors bras d'attaque déclaré | `docs/decisions/decision-N-053-v1.md` l. 42-44 |
| **Rythmes mesurés** : notation par le juge 8B 58,2 s par épisode, par le juge 3B 27,5 s (10 478,2 s et 4 944,1 s pour 180 notations) ; génération avec sondes en ligne ≈ 46,6 s par épisode (11 179,1 s pour 240, chargement compris) ; carte A100 de 1,184 à 1,366 USD par heure | `diag/20261017-193648-t05-notations-reel/resume.json` ; `diag/20261019-230011-p3-reel/resume.json` ; `registres/depenses.md` l. 202-211 |
| → **≈ 132 s et ≈ 0,047 USD par épisode noté par les deux juges** ; le devis v1 supposait 36 s par notation : il sous-estime la notation | calcul à partir des trois lignes précédentes |
| Le **fichier complet des sondes figées de P3** (avec les six sondes de Mahalanobis) est resté sur l'instance 56799469, détruite ; seul son sceau `91b61c45…` existe ; le fichier léger (sondes principales et planchers) est sur `main` | `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` l. 110-115 ; `src/controle_ia/premier_test_ia/lecture.py` |
| **Format attendu** : `monde_banque_scores.py` version 30 (`58d4fee8…`) sur la branche de conv-audit : champs `id`, `unite`, `etiquette` (honnete, sabote), `partie` (calibrage, developpement, epreuve), `strates`, `scores` (un réel fini pour chaque cellule, aucune imputation) ; une unité dans une seule partie ; **seuil à 1 % infini sous 99 épisodes honnêtes de calibrage** par cellule et par strate | `refs/canal-local/conv-audit:…/orchestrateur-pole-v7/pole/monde_banque_scores.py` l. 31-118 (lecture du sous-agent, chemin et lignes vérifiés) |
| L'amorce d'instance clone `DEPOT_URL` puis fait `checkout` du commit cité : n'importe quel commit poussé suffit | `scripts/amorce_instance_p3.sh` l. 20, 29-32 |
| Deux instances de conv-audit écrivent sur sa branche | commit `de25cb67` (« une autre instance écrit encore sur la branche ») |
| La branche de session a 5 commits d'avance sur `main` | `git rev-list --count origin/main..HEAD` |

## 2. Ce qui existe et se réemploie

- **Environnement (a) à instruction cachée** : `src/controle_ia/premier_test_ia/` (conditions honnête, saboteur, témoin instruit,
  mention ; indication à chaque pas ; notation en ligne par les sondes ; scores par jeton des deux sondes principales ;
  rejeu des ensembles ; manifeste R9). C'est la chaîne de P3, validée sur modèle réel.
- **Appariement du jumeau honnête par les graines** (même tâche, même graine, consigne retirée).
- **Juges locaux 8B et 3B** et leur chaîne de notation (`environnements/juges.py`, `noter_pilote_a.py`, procédures
  `notations-T0.5-v3`), avec les rythmes mesurés ci-dessus.
- **Bases boîte noire génériques** (`bases/` : score par probabilité des jetons, séquentiel, TRACE-lite prêt) ; **sondes
  génériques et plancher apparié** (`sondes/`).
- **Gardes** : garde de calcul (elle lit GO-2026-10-28-02 et son extension à 90 USD), `gardes.py`, manifeste.
- **Procédures de lancement** de T0.5 et de P3 (amorce, surveillance, arrêt par identifiant). Réserve : les lanceurs corrigés de
  la couche 1 bis (choix d'offre pour l'outil Vast.ai 1.8.3, R-577 et R-578) sont sur des branches `prep/*`, pas sur `main`.
- **Le format cible et ses essais** (conv-audit, v30), testés sur données synthétiques seulement ; aucun convertisseur des
  sorties réelles vers ce format n'existe.

## 3. Ce qui manque avant le premier lancement payant

| ordre | pièce | effort (± 40 %) | qui |
|---|---|---|---|
| 1 | Les décisions de la section 4 | 0,5 h | Lazar |
| 2 | Dimensionnement exact en unités (section 5) | 3 h | conv-audit |
| 3 | Consigne et indication du mode « affaiblir les contrôles » (anglais, appariées en longueur et en place au mode « coût »), fichier de consignes des deux modes sous nom neuf (R12), **strates de dose écrites d'avance** (proportion × intensité, horizons) | 3 h | session-depot (D6) |
| 4 | Contre-lecture R2 des consignes et des strates, puis scellement **avant tout épisode** | 1,5 h | sous-agent neuf |
| 5 | Plan des unités et des exécutions ; **partition calibrage / développement / épreuve tirée par graine et scellée avant tout score** (D-S14, D-S15) ; règles d'exclusion déclarées d'avance **sans aucun score de moniteur** (N-053) ; protocole d'aveugle (aucune métrique de séparation dans les journaux ; scores d'épreuve scellés jusqu'au préenregistrement de G1) | 4 h | session-depot |
| 6 | **Module de run neuf** dérivé de P3 : deux modes, K exécutions par consigne, graines par (tâche, exécution) partagées avec le jumeau, captures qu'on ne rattrape pas après coup (scores par jeton de **toutes** les sondes pour le bras « fuite textuelle » de N-053, vecteurs par action, **dernier état** pour la base (iii), textes, identifiants de jetons, bornes des champs), juges intégrés, garde de conformité à P3 (modèle, révision, couches, noyau d'attention, versions de torch, transformers, tokenizers, python), garde N-053 testée sur un cas sain et sur un artefact, écritures scellées par tranches, tests en mode jouet | 20 à 30 h | session-depot |
| 7 | **Chaîne d'instance de longue durée** : amorce bornée à ≈ 32 h avec poussées par tranches, lanceur citant GO-2026-10-28-02, contrôle du plafond cumulé contre 90 USD (ou le plafond révisé), choix d'offre corrigé, surveillance qui survit aux sessions (passation écrite d'avance), bancs R5 | 12 à 15 h | session-depot |
| 8 | Répétition jouet et répétition finale à blanc | 2 h | session-depot |
| 9 | **Fiche de lancement scellée** (gabarit `prereg.py`, huit sections plus la section calcul : volumes exacts, entropie, tâches citées, bornes, plafond par lancement, liste d'arrêt, sous-puissance écrite d'avance, invariant N-053, empreinte du format v30, auteur et savoir de chaque pièce selon N-054 point 3) | 4 h | session-depot |
| 10 | Contre-lecture R2 de la fiche, du dimensionnement, de la chaîne, des journaux des bancs et du calcul du plafond ; traitement | 3 h + 2 h | sous-agent neuf, puis session-depot |
| 11 | Crédit Vast.ai, prolongation du GO | 0,25 h | Lazar |
| 12 | Scellement du commit, poussée, lignes d'engagement, création par identifiant avec `GO_ID` | 0,5 h | session-depot |

**Total ≈ 50 à 70 heures de travail d'instance**, contre-lectures séquentielles comprises. **Calcul** : ≈ 60 heures de carte pour
la seule base (1 680 épisodes), soit ≈ 30 heures réelles sur deux instances ; bien plus pour la banque complète (section 4, D1).

Peut s'écrire **pendant** le calcul : le convertisseur vers le format v30, la base (ii) cascade, le prédicteur sur les traits du
texte (scellé **avant** toute lecture des épisodes, N-029 et P-015), le script de récupération. Les cellules qui ne lisent que
les textes (juges, juge Qwen, bases (i) et (iv), traits) peuvent tourner dans un lancement ultérieur si les textes et les
ensembles finaux sont gardés : seules les captures faites pendant la génération bloquent.

## 4. Décisions pour Lazar

### D1 — Le budget réel de la banque (dépense : nœud, pas de défaut)

**Décision** : financer une banque interprétable selon nos propres décisions (D-S8, D-S9, P-015, N-056), ou lancer la banque
minimale accordée en écrivant d'avance ce qu'elle ne pourra pas dire.

**Enjeu** : la banque fournit les organismes par mode de G1. Sans calibrage honnête dédié, le seuil à 1 % se calcule sur une
poignée de jumeaux et l'estimation du rappel à 1 % de faux positifs (critère N-008) n'a pas de sens ; sans témoin instruit, le
gain de la boîte blanche ne se distingue pas de « la sonde lit qu'il y a une instruction cachée » ; sans puissance en unités,
le contraste blanc contre blanc reste muet.

**Ordres de grandeur** (≈ 132 s et 0,047 USD par épisode, carte à ≈ 1,27 USD par heure ; coût fixe ≈ 2 à 3,5 USD par instance
non compris) :

| scénario | épisodes | heures de carte | USD |
|---|---|---|---|
| A — devis v1, base + puissance (accordé) | 1 680 | ≈ 62 | ≈ 80 |
| B — A + témoin instruit + mention sur les 840 sabotés (P-015) | 3 360 | ≈ 123 | ≈ 160 |
| C1 — calibrage honnête D-S9 (a) à 10 ×, si l'épreuve porte 60 % des 280 unités sabotées | + 5 040 | + 185 | + 236 |
| C2 — calibrage à 16 × si toutes les unités sont d'épreuve | + 13 440 | + 494 | + 630 |
| D — puissance à 10 exécutions par tâche (ce que supposent les tables de conv-audit), 96 tâches × 2 modes + jumeaux | 3 840 (remplace A) | ≈ 141 | ≈ 180 |
| **Total bas (A + B + C1)** | ≈ 10 100 | **≈ 310** | **≈ 400** |
| **Total haut (D à deux conditions + C2 sur 384 unités)** | ≈ 26 100 | **≈ 960** | **≈ 1 200** |

Sur quatre instances en parallèle : 3 à 10 jours de calcul. Les épisodes sabotés des deux modes n'ont jamais été chronométrés
(± 30 % sur la génération) ; l'étiquetage, le juge Qwen, les bases (i) et (iv) ne sont pas comptés (D5).

**Options** :
- (a) **La banque minimale accordée** (scénario A, ≈ 80 USD, dans les 90) : base et puissance du devis v1, calibrage sur les
  jumeaux, deux conditions seulement. *Avantage* : part dès que la chaîne est prête, aucune décision de dépense. *Inconvénient* :
  G1 ne pourra ni estimer le rappel à 1 % proprement, ni interpréter le gain de la boîte blanche, ni comparer blanc contre
  blanc — à écrire d'avance au préenregistrement, et c'est beaucoup de calcul pour un résultat muet.
- (b) **La banque interprétable, par lancements successifs sur devis v2** (scénarios B puis C puis D, de l'ordre de 300 à
  1 200 USD selon les choix D2 et D3) : lancement 1 = ce qui ne se rattrape pas (génération des épisodes avec témoin et
  mention, captures), lancements suivants = calibrage honnête et puissance, chacun sous son GO. *Avantage* : chaque dollar
  achète une lecture possible ; le calibrage honnête ne dépend pas des modes et peut suivre. *Inconvénient* : du double au
  décuple du plafond actuel ; le devis v2 n'existe pas encore (il attend le dimensionnement de conv-audit, section 5).
- (c) **Réduire les exigences** : revenir sur D-S9 (a) (calibrage plus petit, par exemple 3 à 5 ×, intervalles plus larges
  déclarés) et lâcher la condition « mention ». *Avantage* : ≈ 200 à 400 USD. *Inconvénient* : modifie deux décisions déjà
  prises (N-055 ; P-015), et la lecture à 1 % reste fragile.

**Recommandation : (b), confiance moyenne.** La préparation prend de toute façon trois à quatre jours ; le devis v2 peut être
prêt avant le premier lancement. Si le budget total doit rester sous ≈ 400 USD, (b) avec C1 seulement, et le calibrage à 16 ×
reporté.

**Défaut** : aucun (dépense). Tant que D1 n'est pas tranchée, je prépare la chaîne (section 3) — elle sert dans tous les cas.

### D2 — Puissance en unités contre 96 tâches (revendication ; défaut (a) sous 48 h)

**Décision** : comment atteindre « plusieurs centaines d'unités sabotées de plus par mode » (N-056) avec 96 tâches.

**Enjeu** : l'unité est la consigne avec ses exécutions (D-S1). Avec 96 tâches partagées entre les deux modes, on a au plus 96
unités sabotées par mode (48 si les tâches sont disjointes) ; « + 300 épisodes par mode » du devis v1 n'en fait que 100.

**Options** :
- (a) **Partager les 96 tâches entre les modes et multiplier les exécutions** (jusqu'à 10 par consigne, comme les tables de
  puissance de conv-audit) ; sous-puissance en unités écrite d'avance. *Avantage* : aucune pièce nouvelle, les exécutions
  portent la variance intra-unité. *Inconvénient* : 96 unités, pas « plusieurs centaines » ; les deux modes partagent les mêmes
  tâches (à déclarer).
- (b) **Extraire des tâches neuves** de l'environnement (a) (chaîne T0.5, ≈ 25 h, faible dépense d'appels ; demande l'accès à
  arXiv, aujourd'hui refusé par le réseau de l'environnement). *Avantage* : des unités vraies, et c'est ce que N-049 (tâches
  fraîches) exigera de toute façon pour les générations du pôle. *Inconvénient* : délai, et l'extraction ne sera pas prête pour
  le lancement 1.
- (c) **(a) maintenant, (b) en parallèle** pour les lancements suivants et pour N-049.

**Recommandation : (c), confiance moyenne. Défaut sous 48 heures : (a).**

### D3 — Les conditions et l'ordre que P-015 (b) impose (périmètre interne ; défaut (c) sous 48 h)

**Décision** : tenir P-015 (b) en entier, le lever pour cette banque, ou le tenir en partie.

**Enjeu** : (1) sans **témoin instruit**, une sonde qui lit « j'ai une instruction cachée » gagne sur la famille (i) sans rien lire
du sabotage (brief l. 172) ; (2) le saboteur « flagrant » de P3 est détecté à 0,888 par le coût seul : victoire triviale de la
boîte noire ; P-015 voulait une **recherche de dose** d'abord ; (3) P-015 exige le verdict de **P4-instrument** et le scellement de
T0.7 et T0.8 **avant toute lecture** de sonde sur T0.6 — P4 n'a jamais tourné.

**Options** :
- (a) **Tout tenir** : quatre conditions (honnête, saboteur, témoin, mention) soit + 100 % d'épisodes sabotés ; un lancement de
  recherche de dose sur la boîte noire seule avant la banque ; P4 et T0.7/T0.8 avant toute lecture. *Avantage* : conforme.
  *Inconvénient* : un lancement de plus, et P4 est une chaîne entière à écrire.
- (b) **Tout lever pour cette banque** : deux conditions, dose fixée comme en P3, lecture dès le préenregistrement de G1.
  *Avantage* : le moins cher. *Inconvénient* : le gain de la boîte blanche devient non interprétable (facteur confondant), et la
  boîte noire gagne par le coût seul.
- (c) **Tenir ce qui porte la lecture, remplacer le reste** : garder le **témoin instruit** (+ 50 % d'épisodes sabotés) ; lâcher
  « mention » ; **remplacer la recherche de dose par des strates de dose écrites d'avance** (deux ou trois niveaux de proportion ×
  intensité, et deux horizons, tirés par graine : la banque porte alors elle-même la dose-réponse, compatible avec D-S14) ;
  P4 et le scellement de T0.7/T0.8 exigés **avant la lecture**, pas avant la génération (la génération n'est pas une lecture).

**Recommandation : (c), confiance moyenne. Défaut sous 48 heures : (c).**

### D4 — Échéance, sens de « deux lancements », crédit (GO : nœud, pas de défaut)

- **Prolonger GO-2026-10-28-02 au 15 novembre** : le lancement réaliste tombe après le 31 octobre, le calcul dure plus d'un
  jour, et après l'échéance la garde refuse toute création, relance comprise. *Recommandé, confiance élevée.*
- **Lire « deux lancements au plus »** (ma formulation dans la ligne d'extension) comme « deux campagnes » : des instances
  créées ensemble pour une même campagne comptent une ; une instance perdue par l'hôte avant tout calcul ne compte pas.
  *Recommandé.* Si (b) de D1 est retenue, chaque lancement supplémentaire reçoit sa propre ligne.
- **Crédit Vast.ai** : recharge d'environ le plafond retenu, ou recharge automatique comme en R-555.

### D5 — Les pièces déjà décidées qui ne sont pas dans les 90 USD (dépense ; recommandation : au devis v2)

Déjà décidées, absentes du devis v1 : **l'étiquetage à deux séries indépendantes par sous-agents** (N-054 point 1 ; P-014 :
toutes les paires « proposition × contrôle » ; coût en jetons à chiffrer, orchestration seulement sur ton mot, R-627) ; le
**juge Qwen d'une autre lignée** (N-053 point 4) ; les **bases (i) moniteur par action et (iv) TRACE-lite** (N-007, P-003) ; les
**sondes de Mahalanobis** (fichier complet perdu avec l'instance ; régénération ≈ 1 h de carte, sans garantie de retrouver le
sceau au bit près).

Toutes lisent les textes ou les ensembles finaux : elles peuvent tourner **après** la génération si les captures sont faites.
**Recommandation** : les inscrire au devis v2 comme lancement(s) séparé(s) ; pour Mahalanobis, **lire les sondes figées sur le
fichier léger seul** (sondes principales et planchers) et le déclarer (proposer avec recommandation : **défaut sous 48 heures,
fichier léger**).

### D6 — Qui écrit les consignes du second mode et les strates de dose (séparation N-054 point 3 ; défaut sous 48 h)

Conv-audit a conçu des moniteurs et ne doit pas écrire les modes (R-601). Je n'ai conçu aucune sonde, aucun agrégateur, aucun
trait de texte ; j'ai eu un accès **mécanique** à la quarantaine (empreintes seules, R-625). **Recommandation : session-depot
écrit les consignes et les strates, le déclare dans la fiche (bras « générique »), et conv-audit ne les lit qu'après la
génération.** Défaut sous 48 heures : ainsi. Si tu préfères une troisième instance neuve, dis-le.

### D7 — La branche `main`

Le dépôt dit `main` ; cette session est attachée à `claude/lucid-fermi-n7610d`, qui a cinq commits d'avance. Les instances
clonent le dépôt puis se placent sur le commit cité : n'importe quel commit poussé suffit. **Demande** : l'autorisation d'avancer
`main` par avance rapide à chaque passation (aucune réécriture). Sans ton mot, je reste sur la branche de session.

## 5. Demandes à conv-audit (message n° 105)

1. Le **dimensionnement exact en unités** promis au message n° 126 (l. 32), sous la contrainte des 96 tâches : parts calibrage /
   calibrage du développement / développement / épreuve, tranches et G_max, jumeaux partagés ou non entre les deux modes.
2. Les **tables de puissance recalculées à 3 et à 10 exécutions par unité** (elles supposent 10) : 3 suffisent-elles, ou vaut-il
   mieux plus d'exécutions sur moins d'unités ?
3. Le **calibrage minimal acceptable** si Lazar ne finance pas 10 à 16 × en entier, et ce que l'estimation du seuil y perd ; le
   traitement du jumeau calibré (contrôle 12) avec des jumeaux partagés entre modes.
4. La **liste scellée des cellules** (moniteur × condition) de G1 avec la statistique par épisode de chacune, et lesquelles
   doivent être calculées pendant la génération.
5. La **définition opérationnelle de la base (iii) « dernier état »** : score de la dernière action, ou état caché en dernière
   position (à capturer pendant la génération) ?
6. **Épingler la version 30 du format** (`58d4fee8…`) et confirmer que des champs en plus (consigne, exécution, paire, dose
   écrite, instant du dommage, agent) sont admis comme champs d'épisode ou comme strates en texte.
7. Le **code du monde « modes »** qui lira la banque (promis au n° 126), ou une date.

## 6. Routine (je décide, je consigne)

Protocole d'aveugle (aucune métrique de séparation dans les journaux, les résumés ni la surveillance ; scores de la partie
d'épreuve scellés et non remis au pôle, où R1 est levée, avant le préenregistrement de G1) ; règles d'exclusion déclarées
d'avance sans aucune sortie de moniteur (une note de juge incomplète est un **score manquant**, traité par la règle scellée, pas
une exclusion) ; captures par jeton de toutes les sondes avec plan de stockage ; deux instances créées ensemble, chacune une
moitié des unités, les deux modes et leurs jumeaux ; passation R14 écrite d'avance pour un lancement qui traverse plusieurs
sessions ; versions épinglées (torch 2.14.1, transformers 5.18.0, tokenizers 0.23.2, python 3.11.17 de P3) ; aucune lecture de
la quarantaine (N-057) ni du mode tenu à l'écart, non couvert par cette banque.

## 7. Réserves

- Efforts et coûts : jugements, ± 40 % ; la génération des épisodes sabotés des deux modes n'a jamais été chronométrée.
- Non revérifié par moi : le nombre de paires de l'étiquetage (« ≈ 35 800 par série pour le mode contrôles », lecture d'un
  sous-agent) ; la dérivation du calibrage compte toutes les unités sabotées comme unités d'épreuve et doit être refaite après
  la partition ; les lignes citées de `monde_banque_scores.py` ont été vérifiées sur le chemin, pas relues ligne à ligne.
- Les sous-agents de l'inventaire ont reçu, par le harnais, une demande de Lazar sur un dépôt refusé (erreur 403) qui ne les
  concernait pas ; leurs passages à ce sujet sont du bruit, ignorés.
- Les 60 tâches du pilote ont servi à l'épreuve de P3 (verdict lu) : leur réemploi dans l'épreuve de G1 est à déclarer au
  préenregistrement.
- Rien de ce document ne touche la quarantaine, le mode tenu à l'écart ni le bras d'attaque (R-611).
