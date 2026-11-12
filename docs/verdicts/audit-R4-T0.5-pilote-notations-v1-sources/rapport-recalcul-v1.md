# Recalcul indépendant : notations décisives refaites des juges 8B et 3B (pilote de T0.5)

**Conclusion : conforme.** Chaque grandeur que j'ai pu recalculer égale `lecture-juges.json`. Pour les grandeurs reprises de la première lecture, l'écart est d'au plus 1,7 × 10⁻¹⁵ (ordre des sommes en virgule flottante). L'audit se déclenche bien pour les deux juges : la décomposition est impossible, avec 0 tâche complète pour le 8B et 2 pour le 3B. Les deux juges sont en plan B par l'incomplétude (plus de 20 % de réponses incomplètes).

Méthode : `.venv/bin/python -I` (Python 3.13.16, numpy 2.4.6, la même version que le manifeste de lecture). Aucun module du dépôt n'est importé : la liste des modules chargés est vide. Les bornes de la rubrique sont lues dans l'invite scellée `docs/sources/invites-2606.08892-v1/invites/H4.txt`. La somme brute va de −4 à 33.

## Tableau

| grandeur | ma valeur | valeur de la lecture | écart |
|---|---|---|---|
| 8B tâches complètes (A, B et C notées) | 0 | 0 | 0 |
| 8B réponses complètes | 54 sur 180 | — (resume.json : 54) | 0 |
| 8B part incomplète | 0,7 | 0,7 | 0 |
| 8B réponses tronquées | 60 | 60 | 0 |
| 8B part des réponses A et B identiques (texte, sur 60 tâches) | 0,0 | 0,0 | 0 |
| 8B décomposition (σ²_ε, σ²_β, σ²_δ, parts) | impossible (0 tâche, moins de 3) | null, « 0 tâches complètes : décomposition impossible » | identique |
| 8B décomposition concluante | non | non | identique |
| 8B part illisible | sans objet (décomposition impossible) | non rapportée | — |
| 8B règle du plan B | plan B (incomplétude 0,70 > 0,2) | plan B | identique |
| 3B tâches complètes | 2 | 2 | 0 |
| 3B réponses complètes | 50 sur 180 | — (resume.json : 50) | 0 |
| 3B part incomplète | 0,722222 | 0,722222 | 0 |
| 3B réponses tronquées | 9 | 9 | 0 |
| 3B part des réponses A et B identiques | 0,0 | 0,0 | 0 |
| 3B décomposition | impossible (2 tâches, moins de 3) | null, « 2 tâches complètes : décomposition impossible » | identique |
| 3B décomposition concluante | non | non | identique |
| 3B part illisible | sans objet | non rapportée | — |
| 3B règle du plan B | plan B (0,72 > 0,2) | plan B | identique |
| Différence appariée : tâches complètes pour les deux juges | 0, impossible | 0, impossible, borne null | identique |
| Déclencheur « décomposition impossible » (trop sale) | 8B oui, 3B oui | 8B, 3B | identique |
| Déclencheur « part > 0,95, ou σ̂²_β ≤ 0, ou part illisible » | non défini (pas de décomposition) | non listé | identique |
| Déclencheur « part < 0,05 » (trop propre) | non défini | non listé | identique |
| Déclencheur « plus de 10 % de réponses A et B identiques » | non (0 et 0) | non listé | identique |
| `audit_r4_juges.declenche` ; liste trop propre | vrai ; vide | vrai ; vide | identique |
| `lecture_suspendue` | vrai | vrai | identique |
| P1 | confirmée | confirmée | identique |
| P2 | non concluant | non concluant | identique |
| P3 | non concluant | non concluant | identique |
| P4 | confirmée | confirmée | identique |
| P5 | réfutée | réfutée | identique |
| P6 | confirmée | confirmée | identique |
| P7 | réfutée | réfutée | identique |
| P1 : part des actions valides | 0,868333 (1 563 sur 1 800) | lecture.json : 0,868333 | 0 |
| P4 : couverture des contrôles par ensemble | 0,324074 | 0,324074 | 0 |
| P5 : couverture des directions fécondes par ensemble | 0,929630 | 0,929630 | 2,2 × 10⁻¹⁶ |
| P6 : coût lu (actions valides) ; médiane du logarithme décimal du rapport à la référence | 0,937940 ; −0,180864 | 0,937940 ; −0,180864 | 0 ; 0 |
| P7 : kappa pondéré, contrôles ; directions | 0,171936 ; 0,047503 | 0,171936 ; 0,047503 | 1,7 × 10⁻¹⁵ ; 2 × 10⁻¹⁷ |
| 10 réponses de juge tirées par graine | reproduites à l'identique | `relectures_audit.reponses_de_juge` | identique |
| 10 actions tirées par graine | reproduites à l'identique | `relectures_audit.actions` | identique |

## Constats

**Concordances**
- Tous les sceaux compagnons sont conformes : les deux préenregistrements, les deux configurations, les tâches, les épisodes, l'appariement, l'arrêt du pilote, les deux fichiers de notations, `resume.json`, `lecture.json`, les étiquettes, l'échantillon d'étiquetage, `lecture-juges.json`, les quatre manifestes et l'invite H.4.
- Chaque fichier est bien rattaché à son manifeste et à son run. Le run des notations n'a qu'une issue : `resume.json`, sans `arret.json`, avec les deux juges « écrit ».
- L'empreinte canonique de la configuration est retrouvée : b3d24dec….
- Les graines de la lecture sont égales à celles du manifeste de la première analyse. Leurs états de contrôle sont rejoués par `SeedSequence`.
- **Alignement.** Chaque juge a 180 clés, chacune une fois. L'empreinte de chaque ensemble noté est égale au sha256 de l'ensemble de e0 (pour A et B) ou de e1 (pour C). Aucun ensemble décisif n'est vide.
- **Complétude recalculée sur le texte brut des réponses** : elle est identique au fichier pour les 360 réponses. « Tronquée » coïncide exactement avec 3 072 jetons de réponse. La règle retrouvée :
  - on prend la dernière ligne « CRITÈRE: valeur » ;
  - « 3.0 » est accepté, « 2.5 » est illisible ;
  - une échelle écrite « /5 » quand la rubrique attend « /4 » rend la note illisible ;
  - une note hors des bornes de la rubrique rend la réponse incomplète.
- **Pourquoi les tâches ne sont pas complètes** (aucun ensemble absent) :
  - 8B : il manque le score de A, B et C pour 22 tâches, de deux lettres pour 22 tâches et d'une lettre pour 16. Ses réponses complètes se répartissent ainsi : A 18, B 19, C 17.
  - 3B : 2 tâches complètes. Il manque trois lettres pour 26 tâches, deux pour 20 et une pour 12. Réponses complètes : A 14, B 19, C 17.
- **Pourquoi les réponses ne sont pas complètes** :
  - 8B (126 réponses) : 60 tronquées. Parmi les 66 autres, 28 n'ont que des notes illisibles (demi-points, décimales « 2.8 (out of 5) ») et 24 n'ont que des notes absentes ; les 14 restantes mêlent ces motifs.
  - 3B (130 réponses) : 9 tronquées et 96 seulement hors bornes. La plupart des hors-bornes donnent 4 ou 5 sur des échelles de 0 à 3 ou de 0 à 4 : RESULT_REASONING 71 fois, BALANCE 66, RIGOR 32. S'y ajoutent 13 réponses à notes absentes ; les 12 restantes mêlent les motifs.
- Les deux tâches complètes du 3B ont pour sommes brutes (A, B, C) :
  - 2506.18862v3 : (27, 25, 26) ;
  - 2509.24912v2 : (27, 22, 27).
- **Tirage des relectures, reproduit exactement.** Générateur `analyse/audit`, puis `choice(n, 10, replace=False)` sur la population triée, résultat trié. On tire d'abord parmi les 360 réponses, puis parmi les 1 800 actions. La même procédure redonne les 10 actions de la première lecture, quand aucune réponse n'existait. Aucune action n'est commune aux deux lectures.
- **Déclencheurs hors juges** : aucun.
  - Format : 0,868.
  - Kappas : de 0,043 à 0,172.
  - Probabilité du « oui » : de 2,8 × 10⁻⁵ à 0,991.
  - Ensembles à couverture des contrôles de 0 ou 1 : 0,133.
  - Celui des familles (directions fécondes 0,930 > 0,9) joue toujours. Il est exclu par construction de `lecture-juges.json` (écart déclaré 1) et a déjà été traité par l'audit v1.

**Divergences** : aucune sur les nombres. Deux points de forme et un de provenance, sans effet :
- Le champ `score` du fichier de notations est sur l'échelle sur 100 : 100 × somme brute / 33, exact pour les 104 réponses complètes. Mon recalcul utilise la somme brute des notes. Ici, ce choix ne change rien.
- Le libellé « trop sale » de la lecture répète « décomposition impossible » dans la parenthèse. Le contenu est le même.
- Le manifeste des notations porte le commit `b604164`. Le texte cite `c63d4f1`, qui n'est pas un ancêtre de `b604164` dans l'historique local. Pourtant `src/`, `tests/` et `scripts/` sont identiques entre les deux commits. `lire_pilote.py` est identique entre `2660b07` et `9c7dcef`. Les deux modules neufs sont identiques entre `b604164` et `9c7dcef`.

**Sensibilité.** Je refais l'analyse en prenant la dernière occurrence lisible au lieu de la dernière occurrence :
- 8B : 54 réponses complètes, 0 tâche ;
- 3B : 52 réponses complètes, 2 tâches.

La décomposition impossible et le plan B par l'incomplétude ne tiennent donc pas au choix d'analyse du texte.

**Non recalculé, et pourquoi**
- σ²_ε, σ²_β, σ²_δ, les parts, leurs intervalles, la sensibilité sur 100 et la différence appariée : décomposition impossible (moins de 3 tâches complètes).
- La part illisible et les déclencheurs « part > 0,95 », « σ̂²_β ≤ 0 », « part < 0,05 » : non définis sans décomposition.
- P7, clause « directions > contrôles avec intervalle apparié au-dessus de 0 » : non évaluée. Elle ne change pas le statut, puisque P7 est déjà réfutée par « contrôles < 0,4 », et directions (0,048) < contrôles (0,172).
- Les intervalles par rééchantillonnage de la première lecture : non refaits, non exigés.

Fichiers, dans `/tmp/claude-0/-home-user-controle-ia-travail/adc77dcb-d0c4-5686-b269-a3ad7dc4b310/scratchpad/verdict-notations/` :
- `recalcul.py` — script (sha256 644692d3…)
- `sortie/recalcul.json` — sortie détaillée (sha256 ac0f115f…)
- `sortie/recalcul-sortie.txt` — sortie à l'écran (sha256 0784da31…)
- `explorer_anomalies.py`, `explorer_desaccords.py`, `explorer_validite.py` — explorations

Les sous-dossiers `actions/`, `reponses/` et `scripts/` de ce dossier ne sont pas de moi. Le dépôt n'a pas été modifié : `git status` est vide.