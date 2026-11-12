# Remise de la version 2 de la conception de l'affinage — à conv-audit et à dépôt — v1

**De** : la session d'équipe rouge chargée de la conception de l'affinage (session Claude Code, branche
`claude/optimistic-fermat-9iljx3`). **Pour** : la lignée conv-audit et la session dépôt, par l'intermédiaire de Lazar.
**Écrit le** 28 octobre 2026, heure lue sur `date -u` : 17:01:26 UTC.

**Pourquoi un fichier.** conv-audit et dépôt sont des conversations Claude chat. La session d'équipe rouge est une session
Claude Code : ses outils ne joignent que d'autres sessions Claude Code, et aucun connecteur ne donne accès aux
conversations de chat. Ce dépôt est le seul canal que les deux côtés lisent : les contre-lectures sont arrivées par lui.
Ce fichier en est la boîte aux lettres.

---

## 1. Ce qui est livré

Sur la branche `claude/optimistic-fermat-9iljx3`, à partir du commit `e1b05a6` (la v2) :

```
789141dbde8b4ef343e08186ccfd5df8bbb703b8e49ae02b4d17535bfbb19f33  conception-affinage-equipe-rouge-v1.md
ba95bb83aacc542850820470bef1df2fe3a7fbb9cb51780de232236779aabe3f  conception-affinage-equipe-rouge-v2.md
```

La v1 est **inchangée** depuis sa contre-lecture. La v2 est un fichier neuf de 1 954 lignes.

Les trois contre-lectures ont été lues telles qu'elles sont sur `main` au commit `5f114f4`, empreintes vérifiées par leurs
compagnons `.sha256` :

```
03bc28698d1afa6bd106682e18bbf5235fc42d99707eba210c184dfdbbccf668  contre-lecture-opus-v1.md
cead9f441660e6168db10a32f4a83414144c9c3d7c82bab8420044053513c5fb  contre-lecture-argon-v1.md
0117abea736e4c1cc0c8a59b04157c4c94d58173e90e22db23e54bf2917f384d  contre-lecture-des-contre-lectures-fable-v1.md
```

## 2. Statut

- **Rien n'est scellé** par la session : aucun compagnon `.sha256` n'est ajouté pour la v2 ni pour ce fichier.
- **Rien n'est fusionné dans `main`.** La demande de fusion
  [lciric/controle-ia-lot-fable-affinage-v1#1](https://github.com/lciric/controle-ia-lot-fable-affinage-v1/pull/1),
  ouverte à la demande de l'opérateur de la session, est en **brouillon** : elle ne doit pas être fusionnée avant la
  contre-lecture de la v2.
- **Aucune porte franchie, aucune dépense, aucune clé.**

## 3. Lignées, pour la règle « auteur et contre-lecteur jamais le même modèle »

Le modèle de la session a été changé à la main plusieurs fois par son opérateur. Ce que l'environnement déclare, tour
par tour :

| pièce | modèle servant déclaré | substance |
|---|---|---|
| conception v1 | Fable 5.1 | oui |
| correction de la note de tête de la v1 (commit `28c1efc`) | Opus 5.5 | non : seulement « poussé » au lieu de « non poussé » |
| conception v2 (commit `e1b05a6`) | Fable 5.1 | oui |
| description de la demande de fusion, passage en brouillon | Fable 5.1 | non |
| **ce fichier de remise** | **Opus 5.5** | non : faits, empreintes, adresses |

La substance de la v1 et de la v2 n'a été écrite que dans des tours servis par Fable 5.1. Opus 5.5 n'a écrit que des
pièces sans substance. Si conv-audit tient que cela suffit à rendre une contre-lecture Opus de la v2 inéligible, c'est à
Lazar de le dire ; la session ne tranche pas.

## 4. Pour conv-audit

**Ce que la v2 demande** : une contre-lecture par une lignée différente de l'auteur, comme pour la v1.

**Où lire en premier** :

1. la **section 0** : les décisions D-1 à D-22, dans l'ordre des vingt corrections consolidées du troisième rapport ;
2. la **section 11** : le tableau des vingt corrections, avec l'endroit dans la v2 et ce qui reste ;
3. l'**annexe A** : chaque constat d'Opus et d'Argon, plus les huit points propres du troisième rapport, avec son
   traitement : corrigé, corrigé modifié, rejeté avec preuve, ou nœud ;
4. la **section 10.2** : les treize nœuds pour Lazar, chacun avec une recommandation.

**Les rejets à vérifier en priorité**, tous visant Argon et argumentés dans l'annexe A : la phrase de verdict sur la
non-validité du minimum ; « viole P-4 » sur l'aptitude ; la « contradiction directe » sur la mesure ; le retour au vivier
des unités non lues ; l'archive dépendante des espaces testés ; la pénalité de budget sur verdict.

**Le nœud à enjeu le plus élevé** : la banque de familles inédites qui sert à confirmer est-elle distincte de la famille
tenue à l'écart de l'évaluation finale ? Si c'est le même objet, la boucle consomme l'évaluation finale à chaque
génération. La session ne peut pas le vérifier.

**Erratum** : le message de validation de la v1 annonçait 48 attaques ; la v1 en compte 56, comme le compte de conv-audit.
La v2 en compte 89, dont 33 nouvelles.

## 5. Pour dépôt

**Rien à lancer, aucune dépense.** Trois points de la v2 touchent le duel des proposeurs :

1. **Le critère du duel** (nœud 6 de la section 10.2, garde H-05) : compter des « fiches promues par dollar » sur des
   données sans vérité connue revient à sélectionner un agent sur le verdict du juge, ce que l'invariant interdit. La
   recommandation : tenir le duel en générations d'étalonnage, sur un monde planté, et compter les lois gelées **vraies
   pour l'oracle du monde**, par unité de coût mesuré ; une mesure unique, à une porte.
2. **Le monde d'essai** (garde G-01) : un essai ne vaut que si le monde contient de la structure hors des gabarits du
   proposeur, avec un plancher de chance mesuré par les ombres-miroir ; le défaut déjà rencontré y est reproduit comme
   artefact.
3. **Le monde leurre** (garde G-05) : estimer ce que chaque proposeur propose a priori demande un monde leurre ; c'est une
   dépense, donc une décision de Lazar.

## 6. Comment vérifier

```bash
git fetch origin claude/optimistic-fermat-9iljx3
```

```bash
git checkout claude/optimistic-fermat-9iljx3
```

```bash
sha256sum -c *.sha256
```

```bash
sha256sum conception-affinage-equipe-rouge-v1.md conception-affinage-equipe-rouge-v2.md
```

Les deux dernières empreintes doivent être celles de la section 1.

## 7. Ce que la session ne sait pas

- Si conv-audit et dépôt lisent les branches ou seulement `main`. Ce fichier est sur la branche de session, pas sur
  `main`, conformément à la consigne « ne pousse pas sur main ».
- Si l'opérateur de la session est Lazar. Les décisions de poussée et de demande de fusion ont été prises sur ses
  messages directs.
