*Note de priorité — collision SPAR sur les questions « axe douleur / contrôle du moniteur ».*
*Lignée « programme-k », 13 octobre 2026, ~6 h 20 UTC. Document interne du dépôt de travail privé.*
*Rien d'opposable (R7). Aucun contenu opératoire : invariants seulement (R-161, R-162). Destiné à la*
*relecture de sûreté et au nœud de publication de Lazar — pas à une exposition publique en l'état.*

---

## 1. Objet

Documenter la priorité intellectuelle sur les questions de recherche en collision avec quatre projets
SPAR (*Supervised Program for Alignment Research*) d'automne 2026, et cadrer la seule parade propre à notre
stade — un préenregistrement public de **priorité** — **sans publier de résultat**, puisqu'il n'en existe
aucun : programme en Phase 0 (instruments), aucune porte franchie, pilote de T0.5 encore en re-notation
(N-021).

## 2. Ce que nous tenons réellement, daté — et ses limites

- **Aucun préenregistrement scellé ne porte encore sur les questions en collision.** Les préenregistrements
  scellés de `prereg/` portent sur les instruments (T0.3 simulation lemme/théorème, T0.4 validation modèle
  réel, T0.5 pilote 8B et revalidation). Rien n'y concerne la coercition du moniteur ni l'axe douleur.
- **Les seuls artefacts datés sur les questions en collision** sont : le document de travail (axe douleur →
  contrôle), la note de brainstorm R-152 (12 octobre, **explicitement non opposable**, PDF non versés), et
  les messages de canal (programme-conv n° 01–03, programme-k n° 01–02), horodatés par leurs commits du
  **12 octobre 2026** dans le dépôt de travail privé.
- **Conséquence, sans l'enjoliver** : notre antériorité interne sur ces questions est **récente (12 octobre
  2026) et non opposable**. Elle n'établit aucune priorité publique. C'est exactement le trou qu'un
  préenregistrement public daté vient combler — à la condition de **ne pas antidater** ce que nous tenons.

## 3. La collision SPAR, re-confirmée en direct le 13 octobre 2026

Pages `sparai.org` lues en direct ce matin ; littérature grise, **non opposable** (R7, pages de projet, pas
de PDF empreinté) ; à reconfirmer sur source stable avant tout chiffre opposable.

| Projet (titre exact) | Encadrement | Terrain | Nos idées | Modèles nommés |
| --- | --- | --- | --- | --- |
| « On the Fragility and Interpretability of Schelling Coordination » | Williams-King, Le, Tan | collusion tacite inter-instances sans canal ; la similarité des représentations prédit-elle la collusion mieux que la similarité comportementale | NK13 | **aucun** (« modèles », fine-tunes, LoRAs génériques) |
| « Disentangling persona vectors from emotion vectors in LLM activation space » | Cadile (U. Rochester) | géométrie persona vs émotion ; piloter l'un déplace-t-il l'autre | NK2, E-C15 | **Llama-3.1-8B *ou* Qwen2.5-7B** (exemple de modèle unique en phase 1, non verrouillé ; réplication sur un second ensuite) |
| « Building a Robust Activation Monitor » | Baldelli (Mila, MATS) | un moniteur d'activation entraîné sur plusieurs concepts/modèles généralise-t-il ; diagnostic « les sondes lisent le texte de surface plus que l'état interne » ; chute près du hasard quand la trace textuelle est retirée | E-C15 / stratification | **aucun en propre** (Llama/Qwen/Gemma seulement cités d'un autre papier) |
| « Does the Thermometer Change the Reading? Testing Whether AI Welfare Self-Reports Survive a Change of Frame » | Vishwarupe | les auto-rapports de bien-être tiennent-ils sous changement de cadre évaluation/déploiement ; la conscience d'être testé explique-t-elle l'écart | NK14 | **aucun** (« frontier », « open-weight ») |

## 4. Lecture de la collision (verdict)

- **Les quatre terrains recoupent les nôtres : réel.** Mais **trois des quatre ne nomment aucun modèle**, et
  le seul qui nomme nos modèles (Cadile) le fait comme **exemple non verrouillé**. « L'un utilise nos
  modèles » est donc vrai pour **un** projet, **au conditionnel**.
- **Les quatre sont des projets en cours ou des propositions** (recrutement de 2 à 4 mentorés, horizon de
  12 semaines). **Aucun résultat publié.** Au regard de la priorité, personne n'a encore planté de drapeau :
  la course se joue **au préenregistrement, pas au résultat** — et c'est une course que nous pouvons gagner
  proprement.
- **Aucun ne recouvre le cœur distinct de nos idées** tel que la revue d'antériorité l'a isolé : *lire ou
  déplacer une direction d'affect dans le moniteur ou le juge lui-même*. Les projets SPAR portent sur la
  géométrie des directions (Cadile), la robustesse d'un moniteur (Baldelli), la collusion (Schelling), les
  auto-rapports (Vishwarupe) — **adjacents, pas identiques**. Le trou commun nommé par la revue reste ouvert.

## 5. Parade recommandée (sans résultat, sans porte franchie)

- **Préenregistrement public de priorité** (OSF, comme le second programme ; ou court preprint « méthodes »),
  **au niveau des invariants**, **expurgé**, **horodaté**. Il plante le drapeau sur la *question et le plan*,
  pas sur un résultat.
- **Trois verrous avant toute exposition**, qu'un GO conversationnel ne lève pas :
  1. **expurgation** (`scripts/depot_expurge.py`) ;
  2. **relecture de sûreté par un sous-agent neuf** (R2/R13), qui tranche aussi l'aléa d'information (§6) ;
  3. **GO formel horodaté** dans `registres/go.md` (`GO-2026-10-…`), **exécuté par la session du dépôt** (qui
     tient `go.md` et le script d'expurgation).
- **Ce que le préenregistrement ne doit pas contenir** : chaînes déclencheuses, doses, recettes de pilotage,
  coordonnées de couche, invites d'attaque. Rien de cela n'est nécessaire à la priorité.

## 6. Aléa d'information — à trancher par la relecture de sûreté, pas par moi

Préenregistrer publiquement la question « peut-on lire ou déplacer une direction d'affect dans un moniteur
au point de dégrader sa fiabilité, et une défense le détecte-t-elle ? » a un aléa d'information **faible au
niveau des invariants** (la littérature constitutive — Pain Axis, Berg & Kaiser, Async Control — est déjà
publique) mais **non nul**. La relecture de sûreté décide : (a) si la question peut être posée publiquement
telle quelle ; (b) la formulation invariante exacte des hypothèses ; (c) ce qui reste **hors** du document
public.

## 7. Ce que je n'ai pas fait

Rien de public. Aucun fichier existant ni scellé touché. Aucune dépense. Aucun chiffre opposable produit.
**Les hypothèses sensibles ne sont pas rédigées dans un document destiné au public avant la relecture de
sûreté (§6)** : le cadre de préenregistrement joint (`preenregistrement-priorite-cadre-v1.md`) laisse ce
bloc explicitement à cette étape.
