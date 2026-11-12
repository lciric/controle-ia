# Traitement des deux contre-lectures du code de l'addendum 2 de P3 — v1

Session 14, 2026-10-20 vers 11:55 UTC. Module relu : `module/audit_verdict_p3_v1.py` (`0b991450…`), tests
`module/test_audit_verdict_p3_v1.py` (`ecbb8972…`, 42 tests), écrits par un rédacteur neuf sur le brouillon 2
(`641b36c2…`). Rapports : `revue-texte/contre-lecture-code-addendum2-texte-v1.md` (`8a2a92d2…`, « scellable après
corrections ») et `revue-mutants/contre-lecture-code-addendum2-mutants-v1.md` (« scellable après corrections » ;
107 mutants, 66 tués, 41 survivants dont 4 équivalents). Aucun défaut de calcul trouvé dans le module ; les corrections
portent sur le texte (brouillon 4) et sur les tests. La session n'a calculé aucune grandeur de B1 ni de B2.

## Texte (brouillon 4, `P3-addendum2-audit-verdict-v1-brouillon4.md`)

| constat | décision |
|---|---|
| CC-texte-06 (information) : règles tranchées par le module là où le texte se taisait | accepté : section « Précisions d'application (brouillon 4) », points 1 à 10 |
| CC-texte-07 (information) : drapeau T2 et table du verrou | accepté : « sauf par la table du verrou… qui ne le consulte que si `P3-P4/<p>` est établie » |
| CC-texte-08 (information) : différences de forme | le module s'aligne sur le texte (libellé « abaissent », phrase de B3 complétée) ; la consigne « cité et soumis à Lazar » reste hors de la phrase de lecture |
| CC-texte-09 et CC-mutants-10 (information) : le module suit le brouillon 2 | accepté : module et tests mis au brouillon 4, puis nouvelle contre-lecture texte face au code et nouvelle campagne de mutants |

## Module (mise au brouillon 4)

- Garde 7 : même état que [L] (calculable, non calculable, en échec), même motif, sinon arrêt ; nombres comparés pour une
  entrée calculable seulement (VB2-01, CC-texte-01, CC-mutants-04 F23).
- Phrase de lecture de B3 complétée ; libellé « abaissent » ; `nombre_de_controles` : 13 écrits, et les lus et sans objet
  par ligne (VB2-06).
- Aucun autre changement de règle.

## Tests (tous acceptés)

| constat | tests à ajouter |
|---|---|
| CC-mutants-01 (majeur) | recalcul indépendant des bornes de `E_sf`, `D`, `E0`, `M`, M7, `E_-f`, M8 hors du module (`manifeste.generateur(graines[clé])`, `effet_cout_apparie`, `np.quantile` à (1 − 0,95)/2), à deux nombres de tirages au moins, comparaison exacte |
| CC-mutants-02 | `conclusions_etablies` sur des [L] construites, chaque ligne de la table du verrou des deux côtés ; run synthétique « aucun signal » : conclusions vides, contrôles « sans objet » |
| CC-mutants-03 | `_lecture_de` sur des nombres donnés (phrases de `au_dela`, de B3, de `portee`, cibles P3-P4 et T3) ; `synthese` : une réserve par couple (nom, cible), motifs joints |
| CC-texte-01, CC-mutants-04, VB2-01 | entrée non calculable ou en échec produite par `lecture.lire` sur des tables qui la causent ; artefact d'état différent (arrêt) ; artefacts des comptes (`actions_nulles_b`, actions par condition) et du quantile du plancher (« P3-P3/<p> ») ; run synthétique avec des actions non notées, qui passe |
| CC-texte-02, CC-mutants-05 | `GardeArret` dans une analyse → « échec », contrôle « non lu » ; `ValueError`, `KeyError`, `DefautDuModule` → arrêt écrit ; NaN et ±inf → arrêt de `_propre` avec le chemin ; haut infini dans P3-P3 → garde 9 ; [L] modifiée pendant l'analyse → arrêt |
| CC-texte-03 | artefacts de la garde 7 sur les seuls comptes et sur le seul plancher, messages attendus |
| CC-texte-04, CC-mutants-07 | déclencheur 2 avec un `E_sf` non calculable et trois intervalles décisifs lus (« non calculé ») ; bords de la garde 15 (1 %), des cas « conforme » de l'audit, de « instable » (borne basse de `E0` égale à 0), du classement contre 0,48 |
| CC-texte-05 | test paramétré d'artefacts pour les 28 `raise` jamais déclenchés (gardes 9, 7, 12, 6, 8, `_propre`) ; les invariants (`DefautDuModule`) testés ou sortis de la liste des gardes dans les notes |
| CC-mutants-06 | lancement sur dépôt jouet : garde 7 ou 13 simulée en arrêt avant le manifeste → rien d'écrit ; fichier non commité → « arbre de travail non propre », rien d'écrit |
| CC-mutants-09 | garde 2 : rétablir [R] avant d'altérer [T], n'attendre que `[T]` |
| VB2-02 | les six cases de la table des cas de B1, la borne décisive ≤ log10 3, les réserves du témoin et de la mention sur leurs deux cibles, `reserve_B1_non_lue`, la part « instable », les comptes de contrôles 13 / 9 / 4 |

Le nombre de tests et les empreintes du module et des tests changent : ils seront écrits en tête du texte au candidat.
