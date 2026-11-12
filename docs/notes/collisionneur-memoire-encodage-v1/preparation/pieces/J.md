# Conception de l'expérience 1 du pôle — le juge v1 contre la dérive non modélisée — v1 (note de conception, pas un préenregistrement)

Écrite par la lignée conv-audit le 27 octobre 2026, à partir de 06:37 UTC (heure lue sur `date -u`), juste avant la
passation de la lignée à une instance nouvelle sur un autre compte (mot de Lazar, 07:33 heure de Paris). **Rien de ce qui
suit n'est codé ni exécuté** : c'est l'analyse et le plan, pour que l'instance nouvelle code, préenregistre et livre sans
refaire le raisonnement. Mode exploratoire (R-522) ; R1 et R3 gardées pour l'expérience elle-même.

## 1. Le défaut à corriger (orchestrateur v0)

Le juge v0 (`orchestrateur-v0/pole/selection_pari.py`) promeut une fiche si la richesse
W_t = Π_{s≤t} p_h(x_s) / max_{q∈𝓛} Π_{s≤t} q(x_s) atteint 1/α à un instant quelconque (inférence universelle ; inégalité
de Ville). 𝓛 = prédicteurs aveugles au domaine : marginale ajustée sur les tirages frais, uniforme, moyennes glissantes
(fenêtres 5, 10, 20, 50). Le nul visé est « les traits des instances n'apprennent rien sur les issues » (issues
indépendantes des traits). Contrôle T1b de v0 (`demo/experience-critere-v1/controles-fatals-v1.json`, `2b86b37f…`) : dans
un monde où la marginale dérive linéairement dans le temps (K = 3 issues, 200 tirages), une loi **aveugle** qui connaît la
dérive est promue **652 fois sur 1 000** (α = 0,05). Le nul composite contient toutes les structures temporelles
(dérive, rupture, autocorrélation, calendrier) ; 𝓛 n'en couvre que quelques-unes. Ajouter des familles de dérive
(logit linéaire, une rupture) ne fait que déplacer le trou : une sinusoïde, une marche aléatoire ou un calendrier
déterministe y échappent.

## 2. La correction proposée : ordre d'exécution secret et membre « urne »

1. **Ordre d'exécution tiré au hasard, après le gel.** L'orchestrateur tire une permutation π (graine dérivée d'une
   graine maîtresse **tenue par le noyau**, jamais dans la vue d'un agent, et de l'empreinte de l'engagement gelé) ; le
   monde (l'expérience) traite les instances du plan dans l'ordre π ; chaque issue est rangée à l'indice de son instance
   dans le plan ; l'évaluation se fait dans l'ordre du plan. Sous le nul (issues indépendantes des traits, structure
   temporelle quelconque), la suite des issues dans l'ordre du plan est **échangeable et indépendante des traits**.
   - **Pourquoi pas permuter seulement l'ordre d'évaluation** : le plan d'instances est dans l'engagement ; permuter les
     couples (instance, issue) révèle la permutation par les instances elles-mêmes ; une loi peut alors retrouver l'heure
     de chaque instance et exploiter la dérive. Seul l'ordre d'**exécution** convient.
2. **Membre « urne » dans 𝓛** : le maximum, sur toutes les lois échangeables, de la probabilité des t premières issues,
   soit Π_k c_k(t)! / t! (c_k(t) : nombre d'issues k parmi les t premières). La loi vraie sous le nul étant échangeable,
   le dénominateur la domine à chaque instant ; W_t est donc majorée par un rapport de vraisemblance à la loi vraie,
   martingale positive d'espérance 1 ; Ville donne P(sup_t W_t ≥ 1/α) ≤ α, **exactement, sans modéliser la dérive**.
   - **Pourquoi l'urne est nécessaire** : une loi aveugle qui connaît la composition exacte des issues (calendrier
     déterministe) prédit « sans remise » ; son gain sur la marginale ajustée vaut
     ½(K−1)·ln 2π + ½ Σ_k ln c_k − ½ ln n, soit **≈ 5,5 nats** pour K = 3 et n = 200 (composition égale), au-dessus du seuil
     ln 20 ≈ 3,0 : sans urne, elle serait promue presque toujours, même avec l'ordre secret. Avec l'urne, sa richesse
     reste ≤ 1. Pour une dérive aléatoire (tirages indépendants, comme le monde de T1b), le gain est faible (de l'ordre du
     dixième de nat).
   - **Coût** : l'urne dépasse la marginale ajustée d'environ 5,5 nats (n = 200, K = 3) : perte de puissance sur les
     petits effets ; les grands effets n'y perdent presque rien (leur gain croît comme n).
3. **Exigences** : l'heure d'exécution n'est jamais un trait d'instance ; l'engagement déclare le plan d'exécution
   (« ordre secret ») ; l'évaluateur refuse des issues produites sous un autre plan (garde essayée sur un cas sain et sur
   un artefact, R5) ; en exécution réelle, c'est le noyau qui impose l'ordre (il appelle l'expérience instance par
   instance, ou vérifie l'ordre par les horodatages) ; un agent qui ignorerait l'ordre rendrait la garantie caduque.
4. **Limites** : (a) si les traits d'une instance se mesurent au moment de l'exécution (état d'un modèle qui change), le
   temps fuit dans les traits et le nul « issues indépendantes des traits » n'est plus celui qu'on croit ; (b) le nul
   augmenté des filles (parents, mélanges, enveloppes) n'est qu'approché sous dérive (la loi vraie devient un mélange
   moyenné dans le temps ; les membres « parent mélangé à une loi aveugle » l'approchent) : à contrôler (T1b-fille).

## 3. L'expérience 1 à préenregistrer (proposition)

- **Juge v1** = v0 + ordre d'exécution secret + urne (autres membres inchangés). Dossier neuf (`orchestrateur-pole-v2`) ;
  v0 jamais écrasé (R12).
- **Contrôles fatals** (chacun ≤ α ; 1 000 répétitions ; 200 tirages frais ; K = 3 ; dimension 2 ; α = 0,05 ; borne de
  Wilson rapportée) : T1a (trois nuls), T6, les sept tricheurs, T3 composante nette fausse, T9 ; **batterie T1b** : loi
  aveugle « calendrier » (connaît p_t) et loi aveugle « composition » (sans remise) sous six structures absentes de 𝓛 —
  dérive linéaire (celle de v0), rupture à n/2, sinusoïde (période n/3), marche aléatoire des logits (écart 0,15 par pas),
  calendrier déterministe par blocs, monde auto-excité (moyenne glissante de fenêtre 10, ou renforcement de Pólya) ;
  **T1b-fille** : fille = parent + connaissance de la dérive, monde = parent + dérive, contre le nul augmenté.
- **Artefacts, qui doivent être vus** (taux > α ; sinon le contrôle n'a pas de dents, R5) : juge v0 (ordre naturel, sans
  urne) sur la batterie (au moins la dérive linéaire, 652/1 000 connu) ; juge v1 **sans urne** sous calendrier déterministe
  avec la loi « composition » (prédit ≥ 0,9) ; facultatif : permutation de l'ordre d'évaluation au lieu de l'ordre
  d'exécution, avec une loi qui retrouve l'heure par l'instance (prédit élevé).
- **Puissance** (rapportée ; lecture minimale gelée) : fille réellement neuve ≥ 0,90 (v0 : 0,993) ; T3 composante nette
  vraie ε = 0,2 ≥ 0,90 (v0 : 0,996), ε = 0,05 rapportée (v0 : 0,913) ; loi de domaine vraie tirée au hasard ; loi vraie +
  dérive.
- **Prédictions signées** : tous les contrôles fatals ≤ α sous v1 (attendu bien en dessous, Ville étant conservatrice) ;
  artefacts vus ; perte de puissance sur la fille neuve ≤ 0,05.
- **Lecture** : juge v1 adopté pour le pôle si tous les contrôles fatals passent et si la puissance sur la fille neuve
  est ≥ 0,90 ; sinon non adopté (et l'on dit ce qui a cédé). Les deux sens sont lus (R3, R4).
- **Graines** : graine maîtresse neuve tirée au scellement (pas 20261026, celle de l'exploration v0) ; un pilote de
  conception sur une autre graine, s'il est fait, est déclaré dans le texte (R-473).
- **Qui** : l'instance nouvelle de conv-audit code et essaie, écrit le préenregistrement court, le fait contre-lire par un
  sous-agent neuf ; session-depot scelle avant lecture (R1), exécute sur processeur — **voie (c), purement synthétique :
  aucune activation, GO-2026-10-26-08 inutile pour cette expérience** —, fait contre-lire (R2) et rend le résultat.
- **Ce qu'elle ne dit pas** : des mondes simulés ; ni agents réels ni données réelles. Ensuite : relais de clé tenu par
  le noyau, une génération réelle de deux fiches, témoins sur données réelles (par exemple la rétrodiction arXiv, où les
  issues des paires sont échangeables par tirage et la vérité connue après coup).

## 4. Plan de code (pour l'instance nouvelle)

- `selection_pari.py` : loi `sans_remise` (composition déclarée ; p_k = (c_k − vus_k)/(n − t), plancher) ; membre
  `urne` (trajectoire Σ_k ln c_k(t)! − ln t!, par `math.lgamma`) ; `construire_engagement(..., plan_execution)` ;
  `tirer_frais(..., plan_execution="ordre_secret")` (le monde voit z_π(t), son propre passé dans l'ordre du temps, et t ;
  issues rangées par indice du plan ; empreinte de π consignée, π recalculable par le noyau) ; `evaluer` refuse un plan
  d'exécution non déclaré ; `BIBLIOTHEQUE_STANDARD_V1` = v0 + urne.
- `controles_pari.py` (nouveau nom de version, ou module `controles_pari_v1.py`) : lois de monde « calendrier » (un
  vecteur de probabilités par instant, tiré d'avance) et « déterministe » ; batterie T1b, T1b-fille, artefacts, puissance.
- Essais : trajectoire de l'urne contre une énumération exhaustive pour n ≤ 6 ; placement des issues par indice du plan ;
  garde de refus (cas sain et artefact) ; essai de fumée de validité à peu de répétitions, sur une graine distincte de
  celle de l'expérience.
