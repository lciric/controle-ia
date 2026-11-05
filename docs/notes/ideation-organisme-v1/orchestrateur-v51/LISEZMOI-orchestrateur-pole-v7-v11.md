# Orchestrateur du pôle, version 0.7.0 — corrections des deux contre-lectures croisées du code — LISEZMOI v11

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1 pour cette version), v11 écrite à partir de 19:22 UTC
(heure lue sur `date -u`) ; v1 à v10 gardées telles quelles (R12). Deux contre-lectures (R2), neuves, d'un autre modèle que
l'auteur des versions lues (`../contre-lectures-code-v7/`) : **Fable 5.1 sur les versions 4 à 9 écrites sous Opus**
(« F », dix constats, `rapport-contre-lecture-v7-opus-v2.md`, `3a12a8f4…`) et **Opus 5.5 sur le socle écrit sous Fable**
(« O », treize constats, `rapport-contre-lecture-v7-fable-v2.md`, `a346778d…`). Les deux disent « à corriger avant le
duel payé ; pas à refaire ». Cette version corrige ce qui touche la garantie, les fuites et la lecture du duel ; ce qu'elle
laisse est dit en bas.

| constat | correction | fichiers |
|---|---|---|
| **F-C1** duel affamé : la réservation par fiche (1,5 USD) se faisait aux plafonds même pour les rôles simulés de l'adaptateur mixte, et le premier refus condamnait toute la génération | réservation **par rôle effectif** (`Generation._reserve_role` : 0 pour un rôle simulé du mixte, même règle que le règlement de la v10) ; plus de drapeau collant : chaque fiche tente sa réservation ; `arret_budget` = au moins une fiche hors budget ; le duel passe `--budget-generation-usd` explicite, et donne aux bras simulés le même budget fictif qu'aux références | `pole/cycle.py`, `demonstrations/duel_proposeurs_v7.py` |
| **F-C2** juge différent entre bras (8 contre 6 instants, 40 contre 12 de calibrage, 3 contre 2 paires) | `--instants-filles`, `--part-calibrage`, `--k-recombinaison`, `--max-paires` exposés en ligne de commande ; un seul dictionnaire `REGLAGES_JUGE` passé aux quatre bras ; la lecture relit les réglages dans le manifeste de chaque bras et écrit `meme_juge_dans_tous_les_bras` (vérifié vrai sur la répétition) | `pole/pole.py`, `demonstrations/duel_proposeurs_v7.py` |
| **F-C3 / O-C1** héritage de la preuve sur une banque sans tranches = produit d'e-valeurs sur les mêmes issues (classe nulle promue 9,5 % en trois générations contre 4,25 % avec tranches ; 0,49 % → 3,09 % après quatre redites) | **une tranche d'épreuve par génération exigée** dès que la mémoire hérite (`executer_pole`, donc aussi pour les bras lancés en mémoire ; et la ligne de commande) ; le duel joue `tranches = 3` (450 = 3 × 150) ; les démonstrations sur la banque T0.5 (trop petite pour des tranches) coupent l'héritage (`politique_redite="refus"`) | `pole/pole.py`, `demonstrations/*` , `essais/*` |
| **F-C4 / O-C9** signature de la mémoire sans moniteur (héritage entre moniteurs ; `transposition_moniteur` jamais jugeable) | le **moniteur entre dans la signature** ; divergence infinie entre moniteurs ; seuil de fusion inchangé (sa recalibration sur la grammaire reste à faire, voir plus bas) | `pole/memoire.py` |
| **F-C5 / O-C2 / O-C3** règle e-BH : filtre `delta0` des filles après la règle ; m compté après les issues ; **témoins vrais dans k\*** (découvertes sûres qui abaissent le seuil des fiches réelles : 16 % de fausses découvertes réelles avec 3 témoins vrais parmi 24) | e = 0 **avant le tri** pour une fille sans marge ; **m fixé avant toute issue** (fiches lancées, hors budget comprises, plus témoins faux sans agent ; refus si m < fiches jugées) ; **témoins vrais hors de la famille**, lus à part au seuil m/α (ils ne pèsent plus sur k\*) | `pole/cycle.py` (`appliquer_multiplicite`, `executer`) |
| **O-C4** sans urne, une loi « sans remise » avec la composition exacte de l'épreuve est promue sans aucun trait (log W 3,8 à 4,2) | les lois qui **lisent l'historique des issues** (`sans_remise`, `moyenne_glissante`) sont refusées au gel quand le membre « urne » est retiré | `pole/cycle.py` (`preparer_engagement`), `pole/selection_pari.py` (`types_de_la_loi`) |
| **F-C6 / O-C7** le bac à sable ne bornait que les écritures (« read access to the entire computer ») et tombait en « sans bac à sable » s'il ne démarrait pas ; la garde par motifs se contourne en une ligne ; banque et `mesures.json` des fiches sœurs lisibles | `sandbox.filesystem.denyRead` sur le dossier de la course **et** celui de la banque, `allowRead` sur le seul dossier de l'agent (idem pour les écritures), `failIfUnavailable: true` ; le dossier de l'agent doit être sous un chemin interdit, sinon refus | `pole/adaptateurs.py` (`construire_options`, `lectures_interdites_par_defaut`), `pole/pole.py` |
| **O-C5** témoins reconnaissables à leur énoncé (« Témoin vrai : … ») quand ils passent par un agent | préfixe neutralisé dans la **vue publique** de toute fiche (la vue gelée garde l'énoncé entier) | `pole/fiche.py` |
| **O-C6** canaux de texte : issues recopiées par un vérificateur dans la consigne de recombinaison, « log W cumulé » dans les leçons | **filtre du canal de texte** des leçons : lignes portant une liste d'au moins cinq nombres ou le vocabulaire du noyau (log W, richesse, issue, verdict, promu, tirages, e-valeur) retirées avant archivage | `pole/memoire.py` (`filtrer_canal_de_texte`) |
| **O-C10** « témoins sans agents » sans monde qui dépose les issues, accepté sans signal | refusé (`executer_pole`) | `pole/pole.py` |
| **O-C11** banque absente du manifeste | chemin, empreinte et tranches de la banque au manifeste | `pole/pole.py`, `pole/monde_banque.py` |
| **F-C9** « structure retrouvée » = intersection non vide des traits | **traits exactement ceux de la structure** (le devis) ; les promues partielles comptées à part | `demonstrations/duel_proposeurs_v7.py` |
| **F-C10** sorties du duel non scellées ; `par_sous_population` sans loi par défaut ; tout `/v1/` relayé (dont les lots, sans usage compté) | sorties scellées ; loi par défaut (marginale du développement) ; relais limité à `/v1/messages`, `/v1/messages/batches` refusé | `demonstrations/duel_proposeurs_v7.py`, `pole/proposeurs_references.py`, `pole/relais_reel.py` |
| **F-C8** bloc `unittest.main()` avant une classe | déplacé en fin de fichier | `essais/test_v7_proposeur.py` |
| essais | 12 nouveaux (`essais/test_v7_v11.py` : lectures du bac à sable, réservation par rôle, règle e-BH corrigée — fille sans marge, m fixé —, signature avec moniteur, chemins du relais, loi par défaut, canal de texte, vue publique) ; 4 essais et 3 démonstrations adaptés à « une tranche par génération » | `essais/` |

**218 essais passent** (208 de la v10, 12 nouveaux, 2 anciens fusionnés ou renommés dans le décompte). Répétition du duel
(2 mondes, moteur simulé, `--arret-apres 1`) : même juge dans les quatre bras, aucune fiche hors budget dans les bras
simulés, lecture écrite, règle d'arrêt déclenchée (le proposeur scripté n'est pas un modèle).

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v11.txt
$PY -I -B -m unittest                                                              # 218 essais, environ 3 minutes
$PY -I -B demonstrations/duel_proposeurs_v7.py DOSSIER_NEUF --mondes 2 --moteur simule --arret-apres 1   # 40 s
```

## Ce que la v11 ne corrige pas (dit, pas caché)

- **F-C7** : la clé du relais reste lisible dans `/proc/<pid>/environ` après `pop` (l'environnement initial du processus) :
  seul un autre utilisateur ou un conteneur pour le relais protège la clé — c'était déjà la recommandation du LISEZMOI v5 ;
  à passer par un descripteur à lecture unique dans une version suivante.
- **F-C4 (iii)** : le seuil de fusion de la mémoire (0,30 nat, calibré sur des lois de force 1,5 en dimension 2) est trop
  large pour les lois douces du duel en dimension 4 (21 propositions sur 26 refusées « classe déjà éprouvée ») : à
  recalibrer sur la loi de référence de la grammaire avant le duel, ou à mesurer dans la lecture du duel.
- **O-C8** : sur la banque T0.5 (couche 1), les témoins vrais ne sont pas établis (5 pour 4,35 attendus par hasard, valeurs
  p de 0,04 à 0,12 ; copies de fiches de la population) : la lecture « pas de dents, banque trop petite » ne tient pas
  telle quelle ; la banque v3 (couche 1 bis) doit planter des témoins établis. À dire dans la lecture de la couche 1.
- **O-C12** : les scripts nommés « v1 » qui produisent la banque v2, et les empreintes v1 à v8 qui ne se vérifient plus sur
  l'arbre courant : les `EMPREINTES-vN` décrivent l'arbre au commit de la version N (le code évolue en place) ; seule la
  dernière se vérifie sur l'arbre courant ; un renommage des scripts attend une version sans urgence.
- **F-C10 (R9)** : graines dérivées par SHA-256 (`graine_derivee`) et non par `numpy.random.SeedSequence` : déviation
  déclarée dans le code et les manifestes, inchangée.
- **O (relais)** : `test_artefact_plafond_atteint` est intermittent sous charge (8 échecs sur 64) : à rendre déterministe.
- **F-C8** : la frontière « arrêt à la moitié » (2 sur 4) et les huit commandes de contournement de la garde ne sont pas
  encore des essais ; la barrière est désormais le bac à sable (lectures interdites), pas la garde.
- **F-C10** : `mesures` cherche par (z, g) dans toute l'épreuve sans se restreindre à la tranche (soupçonné, sans effet sur
  les mondes de la grammaire) ; `--roles-reels experimentateur` en sélection « seuil » (hors duel).

## Limites connues

- Le duel reste une dépense qui attend le GO de Lazar sur le devis (`../demonstration-proposeurs-v7/devis-duel-proposeurs-v1.md`),
  à relire avec cette version : les bras à modèle ne réservent plus que le proposeur ; le seuil de fusion est à
  recalibrer ou à rapporter ; la clé du relais exige un autre utilisateur.
- Le reste : LISEZMOI v10.
