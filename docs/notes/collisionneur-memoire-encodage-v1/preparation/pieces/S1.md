# Pôle « scientifique automatique » — synthèse du tour du collisionneur (v1)

- **Pour** Lazar. Écrite le 26 octobre 2026 par la lignée « session-depot », à partir des neuf cellules du tour (GO-2026-10-26-06, R-524 ; `donnees/collisionneur-pole-scientifique-v1`, `0fbf92d`). Matériau de décision, jamais une consigne. Rien d'opposable (R7) ; les étiquettes RAPPORTÉ / HYPOTHÈSE sont celles des modèles.
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Trois tours (conception, équipe rouge croisée, riposte), neuf cellules valides, aucun refus, 7,82 USD.
- **Réserve forte** : la pièce C (méta-conception v6.3 et sa relecture) **n'a pas été servie** ; les trois modèles le signalent et refusent de conclure sur la recombinaison bisociative (point 3). Demandée à conv-audit (n° 76).

## Verdict en cinq lignes

1. **« Perfectionner le nôtre » et « adopter un système de la littérature » sont rejetés tels quels par les trois.** La réponse convergente est une **voie hybride ancrée sur notre noyau**.
2. Ce qui a de la valeur chez nous, ce n'est pas l'organisme, c'est **le noyau** : clés jamais exposées, bornes d'appels/temps/moisson, et surtout, depuis la correction C-17, l'agent ne peut plus soumettre de code brut (gabarit de trois paramètres bornés). C'est une sûreté acquise.
3. **La première expérience n'est pas « quel moteur », c'est « notre critère de sélection promeut-il du faux ? ».** Processeur seul, moins de 20 USD, cette semaine. Si le filtre laisse passer les paris couverts et les hypothèses à domaine étroit, **n'importe quel** générateur (le nôtre ou celui de la littérature) converge vers des artefacts de Goodhart.
4. **Agentic Scientist v3 est écarté** tant que ses agents héritent des clés (sûreté), malgré son évaluation finale scellée.
5. La capacité « réécrire son propre code » (point 4) **n'existe pas** chez nous aujourd'hui (C-17 l'a retirée pour la sûreté) : elle est à **concevoir sous bac à sable**, pas à « perfectionner ».

## Les points de convergence des trois modèles

- **Architecture recommandée** : garder le noyau (sûreté), y greffer l'idéation/mutation d'un moteur de la littérature **en conteneur sans clés** *si* la première expérience montre notre grammaire bornée insuffisante, et ajouter un **évaluateur figé tenu par le noyau, hors des agents** — absent des deux voies aujourd'hui.
- **Sélection darwinienne sans Goodhart** : sévérité *ex ante* — le test et le nul sont **figés par le noyau avant** l'expérience, les tirages sont **frais après** l'engagement de l'hypothèse. Nul **composite** (bibliothèque de prédicteurs aveugles au domaine ; inférence universelle de Wasserman–Ramdas) pour que l'inégalité de Ville tienne même si le nul n'est pas exactement connu. **Contenu** d'une hypothèse = risque déclaré (divergence à une référence) × couverture du domaine : un pari couvert est classé bas, une hypothèse qui ne prédit rien ne survit pas.
- **Qui écrit le test** : avec nul figé et tirages après dépôt, peu importe (Ville tient) — mais c'est **à vérifier**, et c'est l'objet de la première expérience.
- **Recombinaison bisociative** (sous réserve de la pièce C) : forme minimale = tirage (éloignement des domaines × similarité d'opérateur sur arbre syntaxique **canonisé**) + filtre mécanique de contraintes + fusion ; test sur des mondes à isomorphismes plantés **contre un tirage stratifié recevant exactement le même prompt et le même filtre** ; réfutée si l'écart < ~12 points.
- **Validité de construit des sondes** (B soulève, C adopte) : une sonde linéaire qui lit une **transcription** mesure la représentation du **lecteur**, pas forcément l'état interne de l'agent qui a agi. À garder pour tout le programme.

## La première expérience (convergente, chiffrée par les trois)

**Valider le critère de sélection**, avant tout choix de moteur. Processeur seul, activations réelles mises en cache, moins de 20 USD, deux à trois jours.
1. Étalonnage A/A : deux courses identiques pour fixer le plancher de bruit.
2. Duel sur une population à vérité connue (hypothèses vraies, biais de sous-population, **paris couverts**) : (bras 1) un sélecteur **mécanique** *ex ante* sans appel de modèle, qui choisit les instances où l'hypothèse et le nul divergent le plus ; (bras 2) le même, plus un agent « réfutateur » d'une autre espèce ; (bras 3) la sélection par score moyen (le témoin faible).
3. Contrôles **fatals** : parasite de Kelly et nul dans la bibliothèque → promotion ≤ α ; paris couverts promus seulement si leur part nette est vraie. Un échec invalide le critère et **arrête tout**.
4. Règle d'arrêt : si le bras 1 (mécanique, zéro appel) élimine ≥ 95 % des fausses hypothèses et égale le bras 2 (réfutateur modèle) à un bruit près, on **économise définitivement** les appels du réfutateur et on passe au duel « grammaire bornée contre Python libre sous prison du noyau », qui, lui, tranche la voie.

## Ce qu'aucun modèle n'a pu établir (tous en HYPOTHÈSE)

- Que l'organisme apprenne d'une génération à l'autre, ou que ses castes calibrent mieux qu'une auto-cohérence à budget égal, ou que la mémoire ISVD apporte quelque chose (aucune ablation dans les faits).
- Que la bisociation batte un tirage stratifié (pièce C absente).
- Que les critères de sélection corrigés résistent vraiment (écrits, non courus).
- Qu'un banc synthétique planté prédise le réel (B et A proposent un pont à mesurer).

## Pour toi, maintenant

- **Décision de voie** : hybride ancrée sur le noyau (recommandation des trois). Ce n'est pas un nœud bloquant tout de suite — la première expérience est faisable sans trancher la voie.
- **Dépense** : la première expérience est sur processeur, quasi gratuite (quelques appels de contrôle). Un préenregistrement minimal scellé (R1) suffirait à la lancer.
- **À débloquer** : la pièce C (méta-conception) pour le volet recombinaison.
