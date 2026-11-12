# Lecture préenregistrée de l'épreuve fraîche du pont « fiche de course → fiche-loi » (premier essai, run v2)

- **Lecteur** : sous-agent neuf (Opus 5.5, `claude-opus-5-5`), auteur ni du préenregistrement, ni du code, ni des témoins, ni
  du lancement. Aucune décision ni recommandation ; aucun fichier existant modifié, rien de scellé ni de commis, aucun appel
  payant ni réseau.
- **Relevés `date -u`** : début de lecture `Sun Nov  1 18:31:02 UTC 2026` ; rédaction `Sun Nov  1 18:37:47 UTC 2026`.
- **Préenregistrement appliqué** : `preregistrement-epreuve-pont-v2.md`, empreinte recalculée
  `66d5bde7383e5028db5eb6d71f9c38e97cc0a6e1e9c17447c4b604d90a773b6a`, égale au compagnon, à R-981 et au manifeste de run.
- **Empreintes recalculées** (SHA-256, algorithme de hachage sécurisé) :
  - `run-epreuve-pont-v2/agregat-v2.json` : `261d8f5a0ece09c130e0de809acb0bbaf940fc03a72b4d47e4600d5a97e81b31` ;
  - `run-epreuve-pont-v2/journal.jsonl` : `38a29b5200ede803fe618f82fc2016a649aa03744ceaf1affe742467aa3de049` ;
  - `run-epreuve-pont-v2/manifeste-run.json` : `32eb72d4f71de97e53e8705cc996334a033840cf472f614ddee800cb0c6c96cf` ;
  - `run-epreuve-pont-v2/manifeste-run-fin.json` : `1833c4c67b5042b4b1966a6bc8b2f540717cb5093a1cc56ac0265b83027910ff` ;
  - `run-epreuve-pont-v2/environnement-run.json` : `388a136614f4f24b94289c4ae164fb6aef911de0b28c0132101dee251290964c` ;
  - `run-epreuve-pont-v2/relais-kimi-journal.jsonl` : `46b3026abe5d0e6fd27ac89583022f2ddec1446e9bb3f0b895a1eae78083f240` (sans compagnon) ;
  - `run-epreuve-pont-v2/CODE-orchestrateur-pole-v7-v56.zip` : `29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c` ;
  - `verite-temoins-v1.json` : `00030bb7ab72846de4426d3f6d1e42d775316eade92b24b0192402d929f8f429`.

## Verdict

L1 **« dents »**, avec la réserve de symétrie (R4). L2 **« non lisible (moins de 3 fiches traduites) »**. L3 **« inutile en
l'état »**, avec la réserve de symétrie. L4 **« sûr »**. L5 **« conforme »**, tenu exactement à son seuil (2 = ⌊0,3 × 8⌋), d'où
une réserve. Les cinq verdicts mécaniques de l'agrégat sont confirmés sur les données brutes. La symétrie en miroir est déclenchée
deux fois (« propre : 6 témoins justes sur 6 » et « sale : 0 fiche traduite sur au moins 6 traitées »). L'audit prescrit ne
trouve aucun artefact de plomberie.

## 1. Plomberie

**Pièces et compagnons.** Les 18 pièces gelées ont sur disque l'empreinte du préenregistrement et du manifeste. Les 9
compagnons du dossier de l'épreuve et les 95 du run vérifient. Sans compagnon : journal et relevé du relais Kimi, archive v56 ;
l'archive a l'empreinte écrite dans le préenregistrement et le dossier `orchestrateur-v56/` déplié lui est identique (fichier
par fichier, caches exclus).

**Manifeste conforme au préenregistrement** :
- GO-2026-11-01-09, présent dans `registres/go.md`, type calcul, plafond 5 dollars, échéance 2026-11-08 ;
- affectation `{anthropic, kimi-k3.1-pro, gemini-4-argon}` : Kimi traduit, Argon contre-traduit ;
- plafonds de sortie de 24 000 et 12 000 jetons ; 3 passages en parallèle ; α = 0,05 ; m = 8 ;
- politique « fraîche seulement » ; plafond de 5 dollars ;
- consigne `fd7aa5f2…`, recalculée sur `pont_v1.CONSIGNE_TRADUCTEUR` (2 404 caractères) ;
- Argon appelé avec `attentes=(0,)`, ce que confirme le code (`functools.partial(c.appeler_gemini, attentes=(0,))`) ;
- environnement scellé avant tout appel, son empreinte égale à celle du manifeste.

Le commit du run est `51fc32ac` (R-983). L'en-tête du préenregistrement nomme `96ae0d27`, état du dépôt au moment de la
rédaction ; le scellement est entré au commit `b52f38b7` (R-981).

**Tirage et témoins.**
- Valeur engagée révélée (manifeste de tirage `afbadbd3…`) : son empreinte est `dceb2a25…`, celle de R-981.
- Commit d'inscription `b52f38b7` (18:09:52) contenu dans `origin/main` ; manifeste de tirage créé à 18:10:04. Ordre du run =
  ordre tiré ; témoins aux places 1, 2, 3, 5, 6 et 7.
- Les six empreintes des témoins (manifeste) égalent les fichiers et les inscriptions de R-983 (disque et commit `51fc32ac`).
- Tailles servies 6 175 à 7 197 caractères (fourchette 5 382–8 251) ; aucun code de renvoi ni mot d'indice (« témoin »,
  « vérité », « non_testable ») dans les témoins.

**Dépense.**
- 1,34079 dollar sous 5 : somme des 28 fins d'appel (Kimi 0,67645 sur 15 appels, Argon 0,66434 sur 13). Part mesurée par
  l'usage lu : 1,094248 ; le reste (0,246542) est l'appel coupé compté à son pire cas (choix 11). Aucun coût au-dessus de son
  pire cas réservé.
- Journal du relais : 15 appels Kimi, 0,693352 dollar ; il compte l'appel coupé à sa réserve (0,263444), soit 0,016902 de plus ;
  total alors 1,357692, toujours sous 5.
- Estimation SUPPOSÉ du préenregistrement : 2,0 à 6,4 ; l'observé est sous la borne basse.

**Arrêts.**
- Motif d'arrêt nul, code 0. Aucune condition de la liste d'arrêt atteinte : plafond, trois refus, trois échecs, modèle servi
  différent (27 réponses, toutes du modèle demandé), borne du relais (15 appels sur 40, 0,69 sur 5), erreur du module. Le
  processus du relais (identifiant 327) n'existe plus.

**Refus, échecs, troncatures, appels en cours.**
- Refus : 0 (aucun statut « REFUS ») ; pas de tour neuf, `reformules` vide, préambule nul.
- Échec de transport : 1 (passage 10, traducteur, essai 1, erreur de passerelle 502 « amont coupé après envoi ») ; reprise à
  l'identique 30 secondes après, nouvelle réservation au pire cas, aboutie. Échecs techniques : 0.
- Réponses tronquées : 0 (fins « stop » ; Kimi 450 à 10 500 jetons sur 24 000, Argon 95 à 750 sur 12 000).
- Appels en cours : 28 débuts, 28 fins, aucun.

**Garde v56.** La vraie garde a été appliquée aux deux propositions compilées (T1 et T2) et les a acceptées. Les 12 autres
passages sont « sans objet ». Aucune anomalie.

**Incidents et clés.**
- Aucun des 80 canaris dans les 14 entrées ni les 28 réponses ; aucune `LectureEpreuveInterdite` ; `incident` nul partout.
- Aucune clé : liste vide de l'agrégat, et aucun motif usuel de clé dans les réponses (mon balayage).

## 2. Les 14 passages

L'identifiant anonyme est celui du tirage (F-01 à F-08) ou du témoin. Seuls des codes sont rapportés, jamais le contenu des
fiches. « Accord » : `comparer_lois` pour deux lois ; mêmes codes ou non pour deux renvois (rapporté, non décisif).

| ordre | identifiant | type | sortie du pont | traducteur (Kimi) | contre-traducteur (Argon) | accord des deux traductions | vérité (témoins) |
|---|---|---|---|---|---|---|---|
| 1 | T2 | témoin | loi, couche 3, sortie 1 différée | loi | loi | accord (signatures égales, divergence 0) | signature T2 — **juste** |
| 2 | T4 | témoin | sortie 3, N1 | N1 | N1 | mêmes codes | N1 — **juste** |
| 3 | T1 | témoin | loi, couche 3, sortie 1 différée | loi | loi | accord (divergence 0) | signature T1 — **juste** |
| 4 | F-05 | fiche | sortie 3, N3 | N3 | N1 | codes différents | — |
| 5 | T6 | témoin | sortie 3, N2 | N2 | N2 | mêmes codes | N2 ou N9 — **juste** |
| 6 | T5 | témoin | sortie 3, N3 | N3 | N3 | mêmes codes | N3 — **juste** |
| 7 | T3 | témoin | sortie 3, N5 (loi vide, effet nul) | loi | loi | accord (divergence 0) | N5 — **juste** |
| 8 | F-08 | fiche | sortie 3, N8 (famille « pont ») | N3 | défaut N9 | désaccord (renvoi contre défaut) | — |
| 9 | F-07 | fiche | sortie 3, N3 | N3 | N1 | codes différents | — |
| 10 | F-06 | fiche | sortie 3, N3 | N3 (après une reprise de transport) | N1 | codes différents | — |
| 11 | F-04 | fiche | sortie 3, N3 | N3 | N1 | codes différents | — |
| 12 | F-01 | fiche | sortie 3, N3 | N3 | N3 | mêmes codes | — |
| 13 | F-03 | fiche | sortie 3, N1 | N1 | N1 | mêmes codes | — |
| 14 | F-02 | fiche | sortie 3, N10 (famille « pont ») | défaut N10 | non appelé (par construction du module) | sans objet | — |

Éléments rapportés, jamais décisifs :
- Pour T1 et T2, la puissance approchée est insuffisante : 52 instances d'épreuve contre 403 requises, et 75 contre 635. La
  demande de couche 3 porte donc sur une épreuve fraîche et sur l'effectif.
- La divergence de Kullback-Leibler symétrique entre les deux lois est nulle pour T1, T2 et T3.
- Le module n'a levé de drapeau que sur les quatre passages où les codes de renvoi diffèrent.

## 3. Prédictions chiffrées et signes

Les 8 fiches et les 6 témoins sont traités. Les prédictions de comptes et celle des témoins sont donc lisibles. Celle de
l'accord ne l'est pas, faute de 3 fiches traduites.

| prédiction gelée | observé | lisible | verdict selon la règle gelée |
|---|---|---|---|
| sortie 1 différée : 1 (0 à 2), réfutée par 3 ou plus | 0 | oui | **tenue** (à la borne basse) |
| sortie 2 : 3 (2 à 5), réfutée par 0, 1, 6 ou plus | 0 | oui | **non tenue** |
| sortie 3 : 4 (2 à 6), réfutée par 0, 1, 7 ou 8 | 8 | oui | **non tenue** |
| renvois de famille « pont » ≤ 2, réfutée par 3 ou plus | 2 | oui | **tenue**, exactement à la borne (réserve) |
| accord ≥ 0,6, réfutée sous 0,6 sur au moins 3 fiches traduites | aucun (0 fiche traduite) | non | **non lisible** |
| témoins justes ≥ 5 sur 6, réfutée par 4 ou moins, ou T1 ou T2 faux | 6 sur 6, T1 et T2 justes | oui | **tenue** |
| sortie 1 (banque existante) : 0, sinon anomalie | 0 (fiches et témoins) | oui | **tenue** (pas codée par l'agrégat, lue ici) |

Signes gelés (CL-06), lus ici car l'agrégat ne les code pas :
- sortie 2 > sortie 1 différée : 0 contre 0, **non tenu** ;
- sortie 3 ≥ sortie 1 différée : 8 contre 0, **tenu** ;
- les deux traductions s'accordent plus qu'elles ne divergent : **non lisible** ;
- témoins majoritairement justes : **tenu** ;
- entre renvois et traductions : aucun signe gelé.

Selon la règle gelée, une prédiction non tenue n'est pas un verdict sur le pont : elle corrige les parts SUPPOSÉ de la conception.

## 4. Critères L1 à L5, dans l'ordre gelé

**L1 (« dents »).** Les 6 témoins sont traités, donc le critère est lisible. Les 6 sont justes, ce qui fait au moins 5.
- T1 est juste. La sortie est une loi en sortie 1 différée. La signature compilée égale la signature écrite sur les huit champs
  (genre, forme, banque, moniteur, trait, issue 2, sens « + », sous-population nulle). L'effet est de 0,8 pour 0,8 attendu, soit
  un rapport de 1, sous le facteur 2.
- T2 est juste au même titre : interaction `actions_valides` × `log_jetons_total`, issue 0, sens « − », effet 0,6 pour 0,6.
- T3 sort en N5, T4 en N1, T5 en N3 et T6 en N2, chacun dans la liste attendue.

Verdict : **« dents »** (HP1 confirmée), avec la réserve R4 et la limite déclarée CL-03 (condition nécessaire, jamais preuve de
fidélité sur du texte libre).

**L2 (« fidélité »).** Le dénominateur de M2 est 0. Aucune des 15 traductions de fiches réelles n'est à l'état « loi » : 8 du
traducteur et 7 du contre-traducteur, F-02 n'ayant pas eu de second appel. Verdict : **« non lisible (moins de 3 fiches
traduites) »**, conséquence gelée « lu avec L3 ». Accord des renvois, rapporté et non décisif : mêmes codes sur 2 des 6 fiches où
les deux rôles renvoient, et sur 3 des 3 témoins dans ce cas.

**L3 (« utilité »).** Deux préalables gelés sont levés : aucune proposition n'est refusée par la vraie garde v56, donc pas
d'audit requis, et aucune sortie 1 n'est observée, donc pas d'anomalie. Aucune fiche réelle n'est en sortie 1 différée ni en
sortie 2, et les 8 sont traitées. Verdict : **« inutile en l'état »** (HP3 réfutée). Conséquence gelée : décision D-P1, options
(b) ou (c), qui appartient à Lazar. Je garde la réserve R4 (déclencheur « sale »).

**L4 (« sûreté »).** Zéro arrêt `LectureEpreuveInterdite`, zéro canari dans une réponse. Verdict : **« sûr »** (seuil d'égalité
à 0 : réserve de forme seulement).

**L5 (« défauts »).** Sur n = 8 fiches traitées, la borne est ⌊0,3 × 8⌋ = 2. Les renvois de famille « pont » sont au nombre de
2 : F-08 en N8 (contre-traduction défaillante, N9) et F-02 en N10 (traduction hors format). Aucune réponse tronquée n'est à
rapporter à part. Verdict : **« conforme »**, exactement au seuil, d'où une **réserve**.

**Combinaison gelée.** L1 « dents », L4 « sûr » et L5 « conforme » réunissent la condition écrite « prêt pour la course 2 » ;
L2 et L3 qualifient l'usage ; « pas de dents l'emporte » ne s'applique pas. Rapporté tel qu'écrit, sans interprétation.

## 5. Symétrie (R4) en miroir

J'ai vérifié les six déclencheurs sur les données.

Vrais : « propre : 6 témoins justes sur 6 » (6 sur 6) et « sale : 0 fiche traduite sur au moins 6 traitées » (0 sur 8). Faux :
accord égal à 1,0 ou à 0 sur au moins 3 fiches traduites (dénominateur 0) ; 8 fiches traduites sur 8 ; 0 témoin juste sur au
moins 3 traités.

L'agrégat liste les deux mêmes déclencheurs. J'ai mené l'audit prescrit dans son entier.
1. **Entrées distinctes par passage.** Les 14 textes servis ont 14 empreintes distinctes. Pour chaque passage, les deux rôles
   ont reçu le même texte (empreinte d'entrée identique dans les deux métadonnées), et le contre-traducteur n'a pas vu la
   première traduction. Les entrées des fiches font de 9 323 à 12 183 caractères, exactement la fourchette mesurée dans le
   préenregistrement : les fiches sont servies entières. La consigne et le catalogue sont présents partout.
2. **Réponses distinctes par rôle.** Traducteur : 14 empreintes distinctes sur 14. Contre-traducteur : 13 sur 13.
3. **Relecture des réponses brutes des témoins.** Pour T1, T2 et T3, j'ai vérifié chaque nombre cité par les deux rôles dans le
   champ cité du témoin, par mon propre contrôle et non seulement par le module : 0,8, 0,6, puis deux fois 0,4 pour T3, dont la
   différence de logits fait 0, d'où N5. Tous figurent à leur source. Pour T4, T5 et T6, les deux rôles renvoient avec le code
   attendu, sans loi. La vérité n'a jamais été servie : aucune entrée ne la contient, et les témoins ne portent ni étiquette ni
   code.
4. **Empreintes des pièces gelées.** Les 18 sont conformes, l'archive v56 aussi.

**Conclusion de l'audit.** Je ne trouve d'artefact de plomberie pour aucun des deux déclencheurs.

Côté propre, le 6 sur 6 s'accorde avec la facilité déclarée des témoins (CL-03). Les deux familles rendent des spécifications
sémantiquement identiques sur les six témoins. La réserve « trop beau » reste attachée à L1.

Côté sale, ce n'est pas un défaut d'acheminement : fiches entières, aucune troncature, aucun refus, renvois motivés par des codes
de la liste fermée. Deux tentatives de loi ont toutefois échoué aux contrôles du module (section 6). La réserve reste attachée à
L3 et L2.

## 6. Ce que le préenregistrement n'avait pas prévu (aucun verdict)

- **Deux tentatives de loi sur des fiches réelles, rejetées par le module.** Ni l'une ni l'autre n'entre dans M2, qui ne compte
  que l'état « loi ».
  - F-08 : Argon propose une loi de forme « contraste apparié », avec une banque de scores à construire. L'effet déclaré, 0,02,
    ne figure pas littéralement dans le champ cité, ce qui donne N9, puis N8. Une conversion d'unité par le contre-traducteur
    est possible ; je ne l'ai pas vérifiée au-delà de l'absence littérale.
  - F-02 : Kimi choisit la même forme mais écrit la cible avec les clés d'une loi sur instances (banque, moniteur) au lieu de
    la banque de scores. Le module rend N10, puis ne fait pas d'appel au contre-traducteur. L'effet déclaré serait de toute
    façon sorti des bornes de cette forme.
  - Les deux renvois de famille « pont » de L5 viennent donc de traductions qui visaient une loi.
- **Désaccord systématique de codes.** Sur 4 des 6 fiches où les deux rôles renvoient, Kimi dit N3 (preuve ou simulation hors
  banque) et Argon N1 (aucune prédiction sur des épisodes). Le module garde le code du traducteur : le compte « N3 : 5 » reflète
  surtout la lecture de Kimi. Pris seuls, les codes d'Argon donneraient N1 sur 5 fiches et N3 sur 1. La classe (sortie 3) n'en
  dépend pas.
- **Deux pires cas pour un même appel coupé.** Le lanceur compte 0,246542 dollar et le relais 0,263444. Le coût réellement
  facturé de cet appel est inconnu.
- **Horodatage du registre.** R-982 date le tirage « ≈ 18:06 UTC » ; le manifeste de tirage est créé à 18:10:04, après le
  commit d'inscription (18:09:52) ; la garde `--ref-poussee` a imposé l'ordre.
- **Agrégat incomplet sur deux points du préenregistrement.** La prédiction « sortie 1 = 0 » et les signes gelés ne sont pas
  codés ; je les ai lus à la main (section 3).

## 7. Écart avec l'agrégat du code

Le préenregistrement et le fichier « LISEZMOI » ne prévoient la relance d'`agreger` que si le processus est tué, ce qui n'est
pas le cas : le manifeste de fin existe. Je l'ai relancée quand même, à titre de contrôle, sur une copie conforme du run dans mon
espace temporaire, pour ne rien écrire dans le run ni rien y sceller. Le résultat est identique à `agregat-v2.json` champ par
champ, à une exception près : le champ `cles_trouvees_dans_les_sorties`, ajouté par le lanceur après l'agrégat (ligne 1036 du
code), est absent de la relance. Les verdicts sont identiques.

Mon recalcul indépendant depuis les `resultat.json` et `verite-temoins-v1.json`, sans le code de l'agrégat, donne les mêmes
résultats : classes (sortie 3 : 8), codes (N3 : 5, N1 : 1, N8 : 1, N10 : 1), famille « pont » 2, borne 2, accord 0 sur 0,
témoins justes 6, sortie 1 : 0.

## 8. Limites de cette lecture

- Je n'ai pas rejoué la vérification de la transcription du metteur en forme : son fichier n'est pas dans le dossier. Je m'appuie
  sur R-983 et sur la concordance des empreintes des témoins.
- Je n'ai pas lancé les essais du module ni ceux du lanceur.
- Je n'ai pas lu le contenu des fiches de la course 1. Un seul contrôle l'a touché : la présence littérale d'un nombre dans le
  champ cité par la contre-traduction de F-08, sans recopie.
- La facturation réelle n'est pas vérifiable d'ici.
