# Dossier de service de la course 2 — v1 (assemblage ; rien n'est servi)

Lignée session-depot (instance 2), 30 octobre 2026. Assemblage demandé par conv-audit (n° 224) : la question finale de la course 2 est la fusion des axes de défense de conv-audit (texte I) plus l'axe 6 de session-depot (texte II). **Les deux textes sont servis en sessions séparées, jamais ensemble** (n° 212).

## 1. Textes

| Texte | Pièce | Empreinte | Taille servie | État |
|---|---|---|---|---|
| I, défense (axes 1, 2, 3, 4, 5, 7 et boucle) | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/question-mere-course-v1/recoupement-v1/question-course-2-defense-fusion-v2.md`, branche `canal/conv-audit-n04` | `54804557…` | 11 482 caractères | Brouillon. Il porte encore les marques « [à trancher par Lazar] » ; non contre-lu. |
| II, axe 6 (domaine de validité des statistiques de détection) | `docs/notes/ideation-organisme-v1/course-2/axe-6-texte-II-v6.md` | `1b301c15…` | 10 356 caractères | Conforme et servable (R-796), sous réserve du choix de Lazar (R-793). |
| Listes closes de l'axe 6 | `docs/notes/ideation-organisme-v1/course-2/listes-closes-axe-6-v1.md` | voir son `.sha256` | hors texte servi | Écrites et scellées le 30 octobre. |

## 2. Ce qui manque avant le service, par ordre

1. **Décisions de Lazar** (points « proposer avec recommandation », défaut sous 48 heures ; ce ne sont pas des points de porte) :
   - texte I : Q1 à Q6, D13 et D14 (n° 224 de conv-audit) ;
   - texte II : R-793, option (a) v1 corrigée sans pistes (c'est la v6, défaut), (b) deux bras avec et sans pistes, ou (c) v2 corrigée.
2. **Texte I**, après les décisions :
   - retirer les marques ;
   - le faire contre-lire par un modèle d'un autre fournisseur (R2, demandé dans l'en-tête de la fusion v1) ;
   - le figer et le sceller sur `main`.
3. **Texte II**, pièces hors texte, à faire écrire par un **lecteur tenu à l'écart** qui n'a lu ni BA-002, ni la v2, ni aucun moniteur :
   - (a) les témoins positif et négatif ;
   - (b) les trois témoins de garde ;
   - (c) la liste lexicale.
   La liste lexicale comprend les noms des modes de sabotage du programme, celui du mode tenu à l'écart compris. **Question ouverte : d'où ce lecteur tient-il ces noms sans que session-depot ou conv-audit les lise ?** Elle est à poser à Lazar, qui détient la liste des modes (N-054).
4. **Pré-pilote d'étalonnage des instruments de la course** : juges, mémoire anti-redite et vérification d'antériorité, sur des témoins plantés. Il est recommandé par les trois modèles du collisionneur (synthèse `25e2d351…`, recommandation 1) et c'est Q1 (a) de conv-audit. Il s'écrit, se scelle et se contre-lit avant la course.
5. **Orchestrateur** :
   - v48 utilisable sans `--tests-de-mort` (CL13) ;
   - CL13-05 (modèle servi d'Argon non lu) à corriger avant la course, soit dans la v49 en cours chez conv-audit ;
   - CL14 de la v49 ici, où `bwrap` est présent.
6. **Réserve sur les 240 épisodes de P3** (n° 224, point 4) : sont-ils dans le calibrage de G1 ? Une note est en cours (`note-p3-episodes-calibrage-g1-v1.md`).
7. **Devis et GO** pour la course : sous GO-2026-10-29-19 jusqu'à ≈ 06:30 UTC le 30 octobre, puis sur nouveau mot de Lazar.

## 3. Règles de service (rappel)

- **Texte I** :
  - sessions de proposeurs : Claude et Argon, selon l'orchestrateur ;
  - l'axe 7 dans une sous-session neuve, sans les axes 1 à 5 (D1) ;
  - fiches : branches de la course.
- **Texte II** :
  - sous-sessions séparées, qui ne reçoivent que le texte II ;
  - fiches, juge, lecteur figé, listes et témoins : branche `donnees/course-2-axe-6-sorties-v1` ;
  - lecteur tenu à l'écart (N-054), qui n'est aucun des contre-lecteurs de l'axe 6 ;
  - vers la défense, seulement les comptes définis dans le hors-texte de la v6.
- **R-750** : un refus arrête le tour ; au plus trois questions de repli, différentes et plus étroites, scellées avant service.
