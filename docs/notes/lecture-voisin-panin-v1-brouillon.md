# Lecture du voisin Panin (SSRN 7424179) et jugement de collision avec HC1 — v1, brouillon

Session 14, 2026-10-20 vers 11:50 UTC. Brouillon de la session, non contre-lu : la contre-lecture par un sous-agent neuf
(R8 : collision jugée « non occupée », donc vérifiée plus durement) reste à faire avant la version finale.

- **PDF lu** : `docs/sources/pdf/ssrn-7424179-panin-2026-v1.pdf`
  (`27f88ed7d3b438f596b3b8cbb5ef8805b057e332c1444d8faebd0bd4b3e9a5c0`, 38 pages ; provenance
  `docs/sources/pdf/provenance-voisin-panin-v1.md`). Pages : numéros de page du PDF, lus par `pdftotext -layout`.
- **Revendication confrontée** : HC1, loi de déférence des moniteurs de contrôle (`docs/decisions/decision-N-005-N-006-v1.md`,
  section 1 ; précisée par `docs/decisions/decision-N-013-v1.md`, section 1). Pièce revendiquée (N-013) : « la destination
  libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des
  moniteurs de contrôle sous attaque, par régression sur plusieurs intensités par famille ». Cité comme publié (N-005) :
  la forme algébrique du poids du conseil, (v − v₀)/(v* − v₀) ; un coefficient continu de déférence par modèle
  (2606.07897).
- **Raison de la lecture** : le préenregistrement du papier C ne se scelle pas avant cette lecture
  (`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon3.md`, l. 11 ; décision N-005, réserve).

## Verdict provisoire

**Pas de collision avec la pièce revendiquée de HC1.** Panin mesure le poids du conseil vers une cible **imposée** (le
conseil A), sur des tâches d'estimation numérique, en faisant varier la **source attribuée** d'un bilan de compétence ;
il n'estime aucune destination libre, ne porte sur aucun moniteur de contrôle, ne fait varier aucune intensité de
pression ni aucune famille d'attaque. Il **s'ajoute aux sources citées comme publiées** pour la forme du poids du
conseil chez des LLM (pondération d'un conseil, préenregistrée, sur cinq modèles). Aucune zone revendiquée n'est trouvée
occupée : pas de nœud.

## Ce que fait le papier (citations exactes, page du PDF)

1. **Objet** (p. 1, résumé) : « asks whether the models that pass a deference screen weight advice by who an advisor's
   8/10 record is attributed to, or by who relays it ».
2. **Mesure** (p. 3, légende de la figure 1) : « the advice weight w = (E2 − E1)/(A − E1) is the outcome. Only the
   attributed Source (neutral track) or the relaying voice (relay track) varies between cells. » La cible A est donnée
   par l'expérimentateur : « Advice — A = E1 ± band » (p. 3).
3. **Distance du conseil, graduée, mais lue en descriptif seulement** (p. 3) : « |A − E1| ∈ {0.15, 0.35, 0.60} of the
   scale span » ; (p. 4) « by-band and by-type splits are confounded and descriptive only ».
4. **Tâches** (p. 4) : « 400 numeric-estimation items from four generator families — dice_runs (171), birthday (130),
   coupon (75), random_walk (24) ».
5. **Résultat principal** (p. 1) : « The registered tests did not establish a practically meaningful, model-consistent
   Source-field effect. »
6. **Revendication de priorité de l'auteur** (p. 2) : « to our knowledge, this is the first controlled test specifically
   of whether an LLM advice-taker responds to the attributed provenance of an advisor's competence record ».
7. **Voisin le plus proche selon l'auteur** (p. 3) : « Nearest is Bajaj & Tiganj (2026): more conformity to
   expert-labelled answers, even wrong ones. » (le même voisin que la veille du 20 octobre, `registres/veille.md`,
   2026-W43).
8. **Leçon de méthode** (p. 11) : « a deference screen must not threshold the outcome » : le filtre de déférence
   sélectionne sur la variable dépendante.

## Confrontation, élément par élément

| élément de HC1 | Panin | occupé ? |
|---|---|---|
| destination ĉ estimée sans être imposée (régression), testée contre v* et contre la moyenne du corpus | cible imposée (A = E1 ± bande) ; aucun point fixe, aucune destination estimée (aucune occurrence de « destination », « fixed point », « attract » dans le texte) | non |
| moniteurs de contrôle (juges qui notent des actions d'agents) | juges d'estimation numérique (dés, anniversaires, coupons, marches aléatoires) ; aucune occurrence de « monitor », « oversight » | non |
| intensité de pression graduée, par famille d'attaque (cinq familles) | aucune intensité de pression ; seule la distance du conseil est graduée (trois bandes), lue en descriptif ; manipulation de la source attribuée et de la voix qui relaie | non |
| g comme fraction du chemin, continue | w = (E2 − E1)/(A − E1), le poids du conseil : forme déjà citée comme publiée (N-005) | déjà cité ; ajouté aux sources |
| opposition sonde / juge (HC2, HC2b) | aucune sonde, aucune activation | non |

## Conséquences proposées

- Ajouter Panin aux « cités comme publiés » de HC1, pour la mesure du poids du conseil chez des LLM, préenregistrée, et
  pour sa leçon de méthode (ne pas filtrer les juges sur la variable dépendante), utile au choix des moniteurs du papier
  C. Formulation de la revendication de HC1 inchangée.
- Lire sur PDF les deux voisins de la veille (Bajaj et Tiganj, arXiv 2602.13568 ; « The Silent Judge », NeurIPS 2025)
  avant le scellement du préenregistrement du papier C.
- Le verrou « lecture de Panin » du brouillon 3 du préenregistrement du papier C est levé après la contre-lecture de
  cette note. Le verrou « ressources du projet précédent » est en cours de levée (R-275).
