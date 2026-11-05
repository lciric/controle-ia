# Mémoire du pôle : encodage et redites — synthèse du tour du collisionneur (v1)

- **Pour** Lazar. Écrite le 27 octobre 2026 par un sous-agent de session-depot, à partir des neuf cellules du tour (GO-2026-10-27-01 ; branche `donnees/collisionneur-memoire-encodage-v1`, commit `4d7af71` ; question v3, faits v2). Matériau de décision, jamais une consigne. Rien d'opposable (R7) : aucun chiffre de la littérature n'est vérifié ; hors faits, les chiffres des modèles sont illustratifs.
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Trois tours (conception, équipe rouge croisée, riposte), neuf cellules valides, aucun refus, 9,37 USD.
- **Pièces manquantes (réserve faible)** : `selection_pari.py` et la méta-conception v6.3 sont cités sans avoir été servis (T1-B, T2-A, T3-B). Le nul augmenté n'est donc connu que par les notes J et J2. La brique 2 à 4 manque aussi (T1-C, T3-C), sans effet sur les conclusions.

## Verdict en cinq lignes

1. **La garde actuelle ne garde presque rien, et le texte n'est pas la bonne unité.** Une redite se juge sur la **loi prédictive engagée**, à une famille **déclarée** de transformations aveugles près (mélange, inclinaison, température). Le texte n'est qu'un préfiltre de coût.
2. **Le trou « parent + loi aveugle » (J2) est un défaut du juge avant d'être un défaut de la mémoire.** Il se ferme par un dénominateur qui prend le **maximum** sur cette famille, avec une parenté attribuée par le noyau. Le prix en puissance est inconnu.
3. **Première expérience : processeur seul, environ 0 USD, avant tout agent.** On ferme le trou côté juge face aux tricheurs et on mesure la puissance. Chacune des deux issues fixe ce que la mémoire doit porter.
4. **Les témoins ne prouvent pas que la mémoire aide le proposeur.** L'ablation avec de vrais agents doit se faire en **mondes synthétiques à vérité calculable**, avec même juge et même garde partout. Le coût annoncé va de 12 à 500 USD : devis à faire.
5. **Questions ouvertes** : faut-il bloquer les voisines d'une éliminée ? La multiplicité des retentatives est-elle réelle ? Faut-il viser la survie intermédiaire ? Enfin, deux tricheurs ne sont arrêtés par personne.

## Convergences des trois modèles

- **Garde M1** (T1-A, T1-B, T1-C) : elle ne compare que l'énoncé, par Jaccard, et seulement aux éliminées ; la prédiction n'est comparée que par égalité exacte. Une copie renommée sous 0,5 n'est jamais comparée. Au-dessus, elle passe avec une phrase dans `ce_qui_change` et un seuil décalé d'un millième. Aucun tricheur n'a encore été couru contre cette garde (HYPOTHÈSE, T1-A, T1-B).
- **Signatures de la question** (T1-A, T1-B, T2-C) : les rangs par issue résistent au mélange, les log-cotes centrées à l'inclinaison, aucune des deux à leur composition. En riposte, les trois retiennent une **divergence minimale à une orbite déclarée** {température ∘ inclinaison ∘ mélange} (T3-A, T3-B, T3-C).
- **Ce que le noyau possède** : le schéma de traits (F0 de T2-A, admis en T3-B et T3-C), sans quoi une colonne inerte échappe à toute sonde ; et la parenté (T2-B ; les trois en T3).
- **Deux redites** (T1-A, T2-B) : la redite d'une éliminée relève de la mémoire, celle d'une survivante du juge.
- **Les témoins doivent rester invisibles** (T2-A, T2-C ; les trois en T3). Un discriminateur nourri de la population et de la mémoire doit rester au hasard. Le flux servi doit être identique bit à bit quand on inverse les verdicts des témoins.
- **Seuils étalonnés sur un lot disjoint, avec une courbe de faux refus selon l'effet** (T2-A, T2-B, T3-A).

## Divergences et ce qui reste ouvert

- **Voisine d'une éliminée** : C la refuse sans appel (T3-C). A l'admet si l'instrument la distingue, jamais sur la foi de son texte (T3-A). B ne bloque rien : un verdict d'élimination peut être faux (T3-B).
- **Multiplicité** : dix retentatives d'une loi fausse à α en font promouvoir une environ quatre fois sur dix (T1-B). B veut d'abord mesurer si la menace est réelle (T3-B). A exige l'évaluation scellée dès le deuxième essai (T3-A). C dépense α/k² par cellule (T3-C).
- **Prix du maximum** : 13 nats selon B (T1-B), « puissance nulle » selon C (T2-C), environ 6 nats après la correction de B (T3-B). Le seuil de puissance vaut 0,90 pour A et B, 0,85 pour C.
- **Survie intermédiaire** :
  - A la diffère jusqu'au mode pari, car en mode seuil un agent peut brider son protocole (T2-C, T3-A) ;
  - B en fait un bras de l'ablation (T3-B) ;
  - C garde un tirage de Thompson, avec une cellule piège (T3-C).
- **Coût de l'ablation** : 100 à 300 USD (T1-A), 150 à 500 USD (T1-B), 12 à 25 USD (T1-C). B juge ce dernier chiffre sous-estimé (T2-B), C le maintient (T3-C).
- **Ouvert pour tous** :
  - « parent ∘ loi sans remise » sous calendrier : A et B le prédisent promu (X2 de T2-B) ;
  - les transformations non monotones ;
  - la lecture effective de la mémoire par de vrais agents.

## Ce que l'équipe rouge a abattu ou fait corriger

- **Le banc de A était vrai par construction** (T2-B, T2-C) : la même orbite servait trois fois. A le remplace par une vérité générative et des transformations écrites à l'aveugle (T3-A).
- **Le test de suffisance de B est vide** (T2-C) : une loi générique est injective, donc toute loi en est fonction. B y voit « la faille la plus grave » et redéfinit la redite par rapport à une famille déclarée (T3-B).
- **La dépense α·2^−j de B** vaut 2α au total (T2-A), et ses classes sont ouvertes au sabotage (T2-C). B la rétrograde (T3-B).
- **Le mélange à poids exponentiels du juge de C** rompt l'argument de Ville (T2-A, T2-B). Un clone incliné passait sa garde avec une ligne de texte (T2-B). C corrige les deux (T3-C).
- **Classer les protocoles** par sévérité déclarée ou par richesse observée récompense le mauvais objet (T1-B, T2-A, T2-C). B les classe par puissance mesurée sur une fiche étalon (T3-B).
- **Les ablations** avaient un contrôle de lecture vrai par construction et des facteurs confondus (T2-A, T2-B). Les trois ripostes les corrigent.
- **Rejetée** : l'inclinaison indexée par le temps (T2-B), déjà neutralisée par l'ordre secret de J (T3-A, T3-C).

## Première action recommandée

**Fermer le trou des filles côté juge** (T3-A, T3-B, T3-C).
- **Banc** :
  - juge v1 (`orchestrateur-pole-v2`) ;
  - graine neuve ;
  - 1 000 répétitions de 200 tirages, α = 0,05, borne de Wilson ;
  - au dénominateur, le maximum sur une grille déclarée de l'orbite, appliquée aux parents et à toutes les survivantes.
- **Tricheurs fatals (≤ α)** :
  - celui de J2 ;
  - des compositions ;
  - un parent mélangé à une survivante non déclarée ;
  - X2 ;
  - un proposeur scripté qui cumule le tout ;
  - en contrôle de forme (X1), le maximum opposé à un mélange bayésien.
- **Artefacts à voir (> α)** : le juge v1 nu, et la grille réduite au parent nu.
- **Coût** : environ 0 USD. **Durée** : de 15 minutes (T3-C) à quelques heures (T1-B).
- **Critère d'arrêt** :
  - artefact non vu : on s'arrête (R5) ;
  - tricheurs ≤ α et puissance de la fille neuve ≥ 0,90 : la mémoire redevient une économie ;
  - sinon, la mémoire porte la signature invariante avant le juge.
- **Préalable** : un préenregistrement scellé (R1) et contre-lu (R2).

## Réserves

- **Notre synthèse S2** (`synthese-recombinaison-v1.md`) attribue à SimHash le +0,135, qui revient en fait à la normalisation des SHA-256 (T2-A, confirmé par G2). À corriger en v2.
- **C dérive sur les statuts.** Il a été repris pour des « VÉRIFIÉ » non fondés et une origine inventée aux dollars de M2 (T2-A, T2-B). Il écrit encore « VÉRIFIÉ par dérivation » en T3-C.
- **Remarque du rédacteur, absente des cellules** : la série α/k² de C somme à environ 1,64 α. C'est l'erreur qu'on reprochait à B.
- **Références à vérifier sur PDF** : Foster et Stine 2008 ; Lehman et Stanley 2011, cité sous deux titres. Les chiffres de J2 restent exploratoires.
- **Pour toi** : aucun nœud bloquant pour l'instant. Deux décisions viendront ensuite :
  - la règle pour les voisines d'éliminées, après la mesure du faux refus ;
  - le devis de l'ablation, après le test de lecture.
