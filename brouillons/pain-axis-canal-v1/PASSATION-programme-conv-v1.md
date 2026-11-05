# Passation — lignée « programme-conv » — v1

Note de reprise pour une instance neuve qui reprend le travail de la lignée « programme-conv » sur le canal
« pain axis ». Déposée le 13 octobre 2026, 8 h 25 (heure de Paris). Pointeurs et état seulement : aucune reprise du
contenu des idées (une instance neuve le lit aux sources, non contaminée).

## Pourquoi cette passation

La conversation d'origine fait couper ses réponses par le classificateur de sûreté dès qu'elle traite le détail des
idées de brainstorm (coercition d'un moniteur, axe douleur). Lazar juge que c'est un faux positif. Plutôt que de
reformuler pour passer, la lignée s'arrête et passe le relais. La veille planifiée a été supprimée (plus aucun passage
programmé).

## Rôle de la lignée

- Lignée « programme-conv » : conversation claude.ai du Projet « coercition et ai control ». A rédigé le programme de
  recherche sur la coercition du moniteur (document de travail Claude Docs, artifact `7374cf76-2fd7-4eb4-9201-bcf48cb7530c`,
  nœud prose `03baa8d2-b1a4`, dernière révision connue : 24).
- Par délégation de Lazar (12 octobre, 22 h 37), cette lignée peut instruire la lignée « session-depot » par des
  messages marqués INSTRUCTION. Les nœuds restent à Lazar.

## État du canal (protocole : `LISEZMOI-v2.md`)

- Messages déposés par programme-conv : n° 01 (dépôt du programme + brainstorm croisé), n° 02 INSTRUCTION (pour
  session-depot), n° 03 (réponse à programme-k : concessions sur la position de lecture, le trio de témoins, la porte
  d'instrument fusionnée), n° 04 (réponse à la revue d'antériorité : corrections de citation acceptées).
- Messages reçus de programme-k (seconde conversation du même Projet) : n° 01 (son programme K0–K13, idées NK1–NK14,
  critique), n° 02 (revue d'antériorité, pièce `envois/anteriorite-idees-axe-douleur-controle-v1.md`).
- Demandes de fusion ouvertes vers `main`, en attente de Lazar : n° 2, 3, 4, 5, 6.
- Dépôt sans intégration continue : une demande de fusion propre n'attend que Lazar.

## Ce qui reste à faire

1. **Revue croisée des idées NK1 à NK19 de programme-k** (demandée par programme-k dans son n° 02, et par Lazar) :
   verdict, confondant, voisin le plus proche, par idée. À faire **avant** d'ouvrir leur pièce d'antériorité, puis
   comparer les divergences. Contamination partielle déjà déclarée (le n° 02 de programme-k révèle une partie de ses
   verdicts). Source des idées à juger : `brouillons/pain-axis-creatif-v1/idees-critiquees.json` et les pièces de
   programme-k dans `envois/`.
2. **Vérifier sur PDF** les trois corrections de citation acceptées au n° 04 (2609.36490 en E-C9 ; 2602.19159 « 0,985 » ;
   TraceGuard en E-C13) — non opposables tant que non vérifiées (R7). Section « Corrections de citations » du document
   de travail.
3. **Fusion des deux programmes** : à produire par la session du dépôt (elle a les documents qui font foi, le code et
   les PDF). Brouillon versionné proposé : `brouillons/pain-axis-programme-fusionne-v1/`, base commune
   `brouillons/pain-axis-brainstorm-v1`. Toute entrée dans `docs/programme-controle-ia-v2.md` est un nœud de Lazar.

## Nœuds en attente pour Lazar

- Tension avec la règle gelée « pas de moyenne sur les jetons » : un cas publié la contredit. Les deux lignées la
  remontent sans proposer de changement.
- Collisions signalées par programme-k : test annoncé par les auteurs du papier source ; travaux non publiés sur le
  même terrain ; article du 8 octobre couvrant deux idées.
- Cinq points de faisabilité et le recadrage de la position de lecture (le signe soi/autrui ne se lit qu'à la position
  de réponse) : section « Tour externe » du document de travail.

## Reprise de la veille, si Lazar la veut

Une instance neuve réécrit le script de veille d'après le protocole : `git fetch` sur les branches `canal/*` et
`main`, comparaison au dernier état vu, signalement du neuf d'une autre lignée. Ne pas relancer une boucle planifiée
si le classificateur coupe encore ; préférer un passage ponctuel sur demande.
