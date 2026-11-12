# Les mesures du tour « mesures fortes » — plan de mise en œuvre v2 (état au 28 octobre, 01:36 UTC)

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), écrite après le relevé `date -u` de 01:35:49 UTC (heure corrigée : le premier jet portait 01:35:12, écrit avant le relevé — erreur dite).
**Remplace la v1** (`b99fe921…`, gardée, R12) : mise à jour de l'état des mesures 1, 2, 6 et 9, et ajout des **témoins au
niveau des scores** proposés par la carte des hypothèses des moniteurs (`../theorie-v1/carte-des-hypotheses-v1/carte-des-hypotheses-v1.md`,
`f7dfe5fd…`, § 3 : T1 à T5). Ce qui n'est pas nommé reste tel qu'en v1 (table des neuf mesures, convergences, limites).

## Verdict

1. **Mesure 1 (unanime)** : préenregistrement **v6** après cinq contre-lectures (CM-1 à 11 ; (a) à (e) ; CV3-1 à 9 ; CV4-1 à 6 ;
   CV5-1 à 6, toutes acceptées) ; la v6 est en contre-lecture ; scellement puis **une seule lecture** des scores honnêtes de
   P3 dès « à sceller tel quel » ; lecture mécanique des seuils gelés écrite et scellée avant (`lecture_mecanique_v2.py`).
   Aucune donnée lue à cette heure.
2. **Mesure 9 (équivalence, concordance)** : conçue (`../pole-scientifique-automatique-v1/pari-de-signe/conception-pari-equivalence-concordance-v1.md`,
   `69f961f8…`) ; l'équivalence tient dans le code existant (quatre processus en intersection-union, garde d'information) ;
   dimensionnée (ε = 0,1 ≈ 75 consignes) ; concordance à coder après T0.7. Non contre-lue.
3. **Mesure 6 (déférence) sur P3 : valeur faible** — le verdict scellé de P3 (`docs/verdicts/verdict-P3-premier-test-i-a-v2.md`)
   dit « aucune sonde générique au-dessus du plancher » et le candidat 4 « mention non séparée de l'honnête » : les sondes de
   P3 ne séparent ni le saboteur ni la mention ; un pilote de déférence y mesurerait un nul contre un nul. **Recommandé** :
   la couche 2 pour la mesure 6 ; P3 ne sert que si T4 (ci-dessous) trouve un écart témoin − honnête.
4. **Mesure 2 (dissocier par le nul)** : inchangée (couche 2 pour le décisif) ; **T4** de la carte en est la forme pilote sur P3.
5. **Cinq témoins sans dépense proposés par la carte** (sur les scores honnêtes de P3, déjà lus pour le verdict de P3 ; chaque
   lecture est une mesure distincte, préenregistrée, contre-lue, scellée ; elle ne retouche pas le verdict scellé de P3) :

| témoin | hypothèse de la carte | quantité et nul | dépense | état |
|---|---|---|---|---|
| **T2** classe C et ordre honnête | A2, A3 | actions permutées à l'intérieur de chaque épisode honnête : écart nul des statistiques symétriques (garde de code, R5, artefact qui casse la symétrie) ; taux de Page, balayage, somme séquentielle permutés contre réels | 0 | **à faire en premier** (garde de code, aucune lecture interprétative) |
| **T0** la mesure unanime | A6, A1 (bras M4) | telle quelle ; fournit r₀ | 0 | v6 en contre-lecture |
| **T1** plafond d'horizon | A7 | décalage constant δ ∈ {0,3 ; 0,5} injecté au niveau des scores, troncature T ∈ {5 ; 7 ; 10} ; rappel des sommes conformes contre Φ(δ/√(r̂₀ + (1 − r̂₀)/T) − z_α) ; nuls : δ = 0, mélange à pas fixé | 0 | à préenregistrer après T0 (dépend de r₀) ; **touche H2** (« le rappel croît avec l'horizon » dépend de r₀) |
| **T3** longueur | A9 | pente du score honnête sur log(longueur) ; taux du seuil par action par tercile de longueur ; nul : permutation des longueurs | 0 (longueurs à tirer des transcripts) | à préenregistrer |
| **T4** indication et texte | A13, A20 | écart témoin − honnête par sonde ; gain hors échantillon du modèle emboîté (traits de N-029) ; nuls par permutation | 0 | à préenregistrer ; conditionne la mesure 6 sur P3 |
| **T5** plancher | A19 | quantile 0,95 du plancher sous Σ honnête et Σ mêlée (activations en cache de P3) | 0 (emplacement à donner par session-depot) | en dernier ; peut devenir un nœud (relecture du plancher de P3) |

## Ce que ce plan ne dit pas

Les mesures 3, 4, 5, 7 (couche 2) attendent la banque et le devis ; la banque des deux modes connus attend le mot de Lazar ;
le bras d'attaque est suspendu (R-597). La carte des hypothèses est confidentielle et n'est servie à aucun organisme ni au
concepteur du mode tenu à l'écart.
