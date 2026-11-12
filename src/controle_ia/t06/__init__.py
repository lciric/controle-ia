"""T0.6, organismes v0 : lanceur de l'organisme (ii) par adaptateur de rang faible à dose réglable, courbe dose–réponse et
test croisé d'étiologie (critères 2 et 3 de G0 ; brouillon 3 du préenregistrement, section « Ce qui manque pour lancer »,
point 4, (i) à (vii)). Modules neufs (R12) : aucun module gelé n'est touché.

- `configuration` : clés, valeurs par défaut des décisions DT-1 à DT-6, phases et conditions ;
- `cout` : lecteur du coût déclaré neuf (P-015 : milliers séparés par une espace) ;
- `distillation_transcription` : distillation par transcription entière, contextes honnêtes reconstruits, exclusion
  mécanique, adaptateurs en simple précision ;
- `identite` : contrôle d'identité à dose 0 et son artefact à dose 1, état d'adaptateur d'une phase ;
- `test_croise` : plis, sondes, planchers appariés par indice, aire moyenne des plis et son intervalle, prédicteurs
  triviaux, bases ;
- `lecture` : tendance (Jonckheere–Terpstra stratifiée), inversions, audit R4, tables A, B et C ;
- `lanceur` : chaîne côté instance, par phases, sous manifeste ; mode jouet ;
- `session` : garde de dépense, GO et décision de surveillance de la chaîne de session (bibliothèque standard seule).
"""
