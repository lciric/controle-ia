# Pôle scientifique automatique — synthèse de la génération 0 (les hypothèses de l'organisme sur sa propre structure, testées) — v1

De : conv-audit, le 2026-10-26 18:13:27 UTC. Génération 0 : les affirmations du rapport de méta-conception v6.3 de l'essaim de Gemini
(`96d12112…`) testées par calcul indépendant, sur processeur, par deux expérimentateurs (brique 1 : `5b7011b1…` ; briques
2 à 4 : `929cbc32…`), runs déterministes relancés. Régime exploratoire (R-522), non opposable. **Pas encore vérifié par un
agent d'une autre famille** (étape suivante du pôle).

## Verdict

Sur dix-huit affirmations testées : **cinq survivent, dix sont éliminées, trois indécises.** Les deux briques
« mathématiquement fondées » du rapport (le noyau de tirage, la répulsion sur graphe de ligne) **tombent** ; les deux
idées qui survivent sont des correctifs, dont l'un est le mien et l'autre le contraire de ce que j'avais écrit. Surtout,
**le rapport décrit un code qui n'existe pas** : ni `_score_pertinence_texte`, ni la décomposition de Cholesky, ni le
log-déterminant qu'il prétend réutiliser ne sont dans la v6.2.1 — la refonte est bâtie sur une lecture fausse du code.

## Ce qui survit (à réutiliser dans le pôle)

- **La mémoire spectrale actuelle est aveugle aux textes réels** (rappel du plus proche voisin 0,000, hasard 0,038 ;
  accord 0,014). Vrai défaut, à corriger.
- **Normaliser la somme des hachages avant le relèvement** : meilleur gain mesuré (rappel +0,135 ; accord 0,014 → 0,48
  sur 27 textes réels).
- **SimHash sur n-grammes** préserve la morphologie au niveau du mot (aire 0,987 contre 0,458) ; indécis au niveau du
  texte.
- **Le correctif du noyau de tirage** (diversité de domaine dans le noyau, pertinence dans la qualité, opérateur
  réintroduit après tirage) : diversité 0,90 à 0,95 pour un hasard de 0,74, qualité gardée, pas de dégénérescence.
- **Le filtre de compatibilité des contraintes** : utile (fusions contradictoires 57 % → 0 % sur lexique propre), mais
  fragile sur du bruit réaliste (57 % → 34 %, rappel 0,61) ; à garder, à ne pas surestimer.

## Ce qui est éliminé

- Le noyau « PSD par produit de Schur » du rapport : **1 000 violations sur 1 000** (λ_min médian −0,715) ; réparé par
  γ ≥ 0,37, il repousse justement les paires qu'il visait.
- L'égalité « trace = 1 − ⟨d,d⟩² » : fausse (la trace vaut 14 + ⟨d,d⟩²) ; la forme trace récompense la similarité de
  domaine.
- « La répulsion détruit les pivots de Swanson » : réfutée sur l'organisme réel (les termes saturés de la génération 18
  sont des mots-outils, aucun pivot) ; le graphe de ligne proposé coûte C(d_B, 2) et bloque 78 % des ponts.
- Le diagnostic « v² écrase par explosion de variance » (σ1 est une direction moyenne, pas une variance) ; « Koopman sur
  bruit blanc amplifie la variance isotrope » ; « SHA-256 maximalement non informatif » ; le protocole P1 (un encodage
  nul le passe à 100 %) ; le critère d'arrêt par convergence du spectre (absent du code) ; mon propre correctif de
  recentrage (sans effet) ; le rang effectif 1,82 annoncé (vrai : 3,96).

## Ce que la génération 0 établit pour le choix du moteur

- La voie « perfectionner notre organisme » part d'une **refonte fausse sur le code** : à refaire sur le vrai code, avec
  les deux correctifs survivants seulement. Le moissonnage et le tri réels de la v6.2.1 ne sont pas ceux que le rapport
  décrit — à relire avant toute conception.
- La génération 0 a coûté 0 dollar (processeur) et a éliminé dix affirmations sur dix-huit par des tests qui pouvaient
  échouer : c'est le mode de fonctionnement visé pour le pôle.

## Suite

1. Vérification de ces verdicts par un agent neuf d'une autre famille (étape « vérificateur » du pôle).
2. Relecture v2 pour Gemini (corrigée par ces essais, mes erreurs comprises), sur une branche à part ; Lazar la lui
   transmet.
3. Génération 1 : recombinaison des cinq survivants en fiches filles + témoins plantés, dans l'orchestrateur du pôle.
