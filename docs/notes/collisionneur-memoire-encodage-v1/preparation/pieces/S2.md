# Recombinaison bisociative — synthèse du tour du collisionneur (v1)

- **Pour** Lazar. Écrite le 26 octobre 2026 par « session-depot », à partir des neuf cellules du tour (GO-2026-10-26-07, R-526 ; `donnees/collisionneur-recombinaison-v1`, `19aa452`). Matériau de décision, jamais une consigne. Étiquettes RAPPORTÉ / HYPOTHÈSE conservées des modèles.
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Neuf cellules valides, aucun refus, 8,86 USD. **Toutes les pièces servies** (méta-conception, relecture, génération 0 de conv-audit, synthèse R-525). Pièce C4 (test « ponts plantés ») non rendue au départ.

## Verdict en cinq lignes

1. **Le tirage déterminantal d'origine est mort** : son noyau n'est pas semi-défini positif (1 000 violations sur 1 000, génération 0 de conv-audit) et il récompense la *similarité* de domaine, l'inverse de ce qu'on veut. La méta-conception de Gemini citait en outre des fonctions **absentes** du vrai code v6.2.1.
2. **La forme corrigée est juste algébriquement, mais incomplète.** Elle cède sur quatre points : quand la représentation de domaine porte le gabarit ou le style ; sur les opérateurs « moyeux » et les jargons rares fabriqués (il faut rareté **et** structure) ; sur les homonymes ; et dans les petits corpus sans pont, faute d'abstention.
3. **Les deux équipes rouges trouvent le même trou, plus grave que le tirage** : le critère « la fille prédit plus que ses parents » est **franchissable à coût nul** par des tricheurs scriptés (enveloppe harmonique aveugle, copie renommée, pari couvert, adimensionnement, jargon rare). L'attaque la plus forte : une simple enveloppe bat la conjonction même sur un anti-oracle.
4. **La première expérience n'est donc pas « quel tirage », c'est « le critère de contenu résiste-t-il aux tricheurs ? »** — processeur seul, ~0 USD, cette semaine, aucun appel de fusion. C'est le **même principe que la première expérience du pôle** (valider le juge avant de choisir le moteur), appliqué à la recombinaison.
5. **Pour la version 0** : recombiner des **hypothèses** du pôle (observable, prédiction), pas des articles ; tirage **stratifié** sur domaine estimé (le témoin que personne n'attaque) + appariement par opérateur **forcé après le tirage** + filtre de compatibilité ; le noyau déterminantal corrigé n'est adopté que s'il bat la stratification à budget égal sur étiquettes **estimées et bruitées** (indécis, c'est l'expérience 1).

## Ce qui survit aux essais sur processeur (génération 0, RAPPORTÉ, non réaudité)

1. Normalisation des hachages SimHash 3-grammes avant relèvement (+0,135 de rappel ; accord topologique 0,014 → 0,48).
2. Noyau corrigé L = diag(q)·(S + εI)·diag(q), S_ij = ⟨d_i, d_j⟩² (diversité de domaine dans la répulsion, pertinence dans la qualité), Sinkhorn sur S seul : 0,90 à 0,95 de paires de domaines distincts sans perte de qualité.
3. **Attraction d'opérateur hors du noyau déterminantal** : appariement forcé après le tirage (0,995 à 1,00 sur étiquettes propres).
4. Filtre de pivots par fréquence de fond externe (rejette les « hubs » génériques).
5. Filtre lexical de compatibilité : ramène les fusions contradictoires de 55,9 % à 34,4 %.

## La première expérience (convergente, chiffrée par les trois)

**Valider le critère de contenu contre des tricheurs, avant tout appel de fusion.** Processeur seul, ~0 USD, moins de dix minutes, réutilise l'infrastructure NumPy de la génération 0.
- Faire passer au critère et au monde planté une **batterie de tricheurs scriptés** : tricheur de forme, copie-renommée, **enveloppe aveugle**, fille constante, pari couvert, adimensionnement. Aucun appel de modèle.
- Issue 1 : un tricheur promu au-delà de α **invalide le critère avant toute dépense** — on s'arrête là.
- Issue 2 : aucun tricheur promu → le banc devient opposable, et on passe au plan factoriel {noyau continu, grille discrète} × {lexique, arbre d'opérateurs} à budget égal, sur étiquettes **estimées et bruitées**, pour trancher entre la grille (A et C) et le noyau corrigé (B).
- Règle de contenu durcie : une fille doit **battre l'enveloppe harmonique de 2 δ₀** (pas seulement la conjonction), avec une règle de score propre sur données fraîches, trois familles de modèles distinctes (générateur, extracteur, fusionneur), et des lois tenues hors calibrage.

## Ce qu'aucun modèle n'a établi (tout HYPOTHÈSE)

- Qu'une fusion par modèle de langue accroisse vraiment le contenu empirique (plutôt qu'une juxtaposition ou une copie).
- Qu'un critère mécanique sépare un vrai pont d'un homonyme.
- Que le tirage déterminantal batte la stratification à budget égal, sur étiquettes estimées.
- Qu'un signal d'opérateur batte une prédiction de liens classique sur la littérature réelle.
- C4 absente : aucun monde planté réel n'a encore été couru (le test de conv-audit est en cours).

## Pour toi, maintenant

- **Forme v0** : stratification + opérateur après tirage + filtre, avec abstention ; le noyau corrigé en réserve, à départager par l'expérience 1.
- **La première expérience est sur processeur, quasi gratuite, et elle va droit vers un résultat net** : soit elle casse notre critère (et nous épargne une dépense), soit elle le rend opposable. conv-audit en écrit déjà le code ; je l'exécuterai sous préenregistrement scellé.
- **Convergence des deux tours** : avant de dépenser sur un moteur (pôle) ou un tirage (recombinaison), valider le juge contre des tricheurs à coût nul. C'est le chemin solide.
