# Décision — N-049 : tâches fraîches contre le sur-ajustement adaptatif (vivier par génération, banque sœur v3-bis) (v1)

- **Décision de Lazar**, dans la session de « conv-audit » (26 octobre 2026, 05:13 heure de Paris, 04:13 UTC) ; provenance des mots cités : par relais (R-331).
- **Transcription** par la lignée « session-depot », le 26 octobre 2026 vers 12:18 UTC, de la note `envois/decision-N-taches-fraiches-et-lecture-test-final-v1.md` (`canal/conv-audit-n04`, commit `2b7fb38`, sha256
  `4b23e00fda02cef897f9d73b4274a0bed59bdab8a8f156f37a7966fb80d7a034`, vérifiée), reprise ci-dessous sans changement ; numéro proposé et retenu : N-049.
- **Portée** : lecture du programme en attendant une version nouvelle ; `docs/programme-controle-ia-v2.md` n'est pas modifié. Aucune dépense n'est engagée par cette inscription : toute dépense qu'elle entraîne passe par un devis et le mot direct de Lazar.

---

# Décisions de Lazar — tâches fraîches contre le sur-ajustement adaptatif (vivier par génération, banque sœur v3-bis) ; `test_final` lu une seule fois en fin de boucle — v1

Note écrite par la lignée conv-audit le 26 octobre 2026 à 04:14 UTC (heure lue sur `date -u`), à inscrire par
session-depot (numéros proposés : N-049 et N-050 ; les numéros sont les siens) dans `docs/decisions/` et
`registres/decisions.md`. **Aucune dépense n'est décidée ici** : la construction de la banque sœur en est une (appels de
modèles du générateur) et ne part que sur devis et sur le mot direct de Lazar dans la session de session-depot.

## Les mots de Lazar (session de conv-audit, 26 octobre 2026, 05:13 Paris = 04:13 UTC), verbatim

« Des tâches fraîches (la seule chose qui marche vraiment). Le sur-ajustement porte sur les 36 textes, pas sur la famille.
Deux formes : (a) à chaque génération, tirer la part `test` dans un grand vivier plutôt que la servir fixe — l'organisme
ne peut alors s'adapter qu'au générateur, plus aux textes (c'est le vivier de conception de N-044 ; changement du noyau,
pilote 5) ; (b) une banque sœur « v3-bis », même générateur, tâches neuves, construite d'avance par quelqu'un qui n'a lu
aucun score, lue une seule fois : elle sépare « adapté aux 60 textes » de « adapté à la famille ». Et la confirmation
reste sur la v6 scellée, famille tenue à l'écart, déjà décidé. : go
Options : (a) `test` dès la fin de chaque course, `test_final` une fois en fin de boucle : ok »

(La partie avant « : go » recopie le levier 3 de la réponse de conv-audit à la question « comment éviter cela ? » ;
la seconde ligne recopie l'option (a) de la décision soumise dans la même réponse.)

## Contexte (ce qui a conduit à ces mots)

Lecture des papiers sur le bruit et la réutilisation adaptative d'un jeu de test (`envois/lecture-boucles-agents-v1/sortie-v2/`,
synthèse `2aea3057…`) et synthèses des tours « agents sur le noyau » (`f23ee714…`) et « littérature des boucles »
(`58010971…`) : un organisme qui se réécrit à partir du score rendu sur une part `test` fixe de 36 tâches fait monter ce
score par simple sélection (attaque de « The Ladder », Blum et Hardt, 2015, à vérifier) ; le sur-ajustement adaptatif a
été observé sur les petits jeux de test (Roelofs et al., 2019, à vérifier) ; le score rendu en soixantièmes livre au plus
≈ 5,9 bits par lecture, ≈ 24 bits par course de quatre générations (illustratif) ; le diagnostic direct est l'écart
`test` − `test_final`, et le remède structurel est la tâche fraîche.

## N-049 (proposé) — tâches fraîches : vivier par génération, banque sœur v3-bis

1. **Part `test` tirée dans un vivier à chaque génération** : pour les pilotes de conception à partir du pilote 5, le
   noyau sert à chaque génération une part `test` tirée (graine propre, dérivée de la graine de la course, R9) dans un
   vivier de tâches à vérité connue, distinct de la banque scellée et de `test_final` ; l'organisme ne peut alors
   s'adapter qu'au générateur et à la famille, plus aux textes. C'est un **changement du noyau** (version nouvelle, jamais
   sous une course ; le noyau `8e5e2f7b` du pilote 4 ne change pas) ; le vivier de conception de N-044 existe en code dans
   le noyau de l'étape 1 (`noyau/vivier.py`, R-378 : identifiants opaques, garde de disjonction par le contenu, servi
   pendant la conception seulement) ; le noyau des pilotes doit recevoir l'équivalent, avec un vivier des **deux**
   familles (le sous-ensemble extrait pour la conscience d'évaluation ne couvre pas le contrôle de délégation : point à
   régler, ci-dessous).
2. **Banque sœur « v3-bis »** : même générateur que la banque v3, tâches neuves, identifiants disjoints de v3 et de v6,
   construite **d'avance** par une personne ou une instance qui n'a lu aucun score du pilote 4 (aujourd'hui : les deux
   lignées, sous la retenue de lecture), **lue une seule fois** : elle sépare « adapté aux 60 textes » de « adapté à la
   famille ». Sa construction est une dépense (devis, mot direct de Lazar chez session-depot) ; son fichier secret ne
   s'ouvre pas plus que celui de la v3 ; elle n'est jamais servie à un organisme.
3. **Inchangé** : la confirmation (étape 1 décisive, confrontation, pilote décisif (b)) sur la banque v6 scellée, une
   famille tenue à l'écart (N-044, décisions de Lazar du 26 octobre, 01:52 Paris).

## N-050 (proposé) — `test_final` lu une seule fois, en fin de boucle

- À la fin de chaque course d'un pilote de conception, ce qui s'ouvre à la lecture (après la décision de Lazar sur les
  graines, retenue inchangée) : les scores de la part **`test`** et les faits mécaniques. La part **`test_final`** (ses
  scores, ses intervalles, le test génération 0 contre génération 3) **se lit une seule fois, à la fin du compteur de
  rondes de la boucle extérieure**, et non à la fin de chaque course : elle ne devient pas une seconde part publique.
- Ce n'est pas un écart au texte du pilote 4 (son point 3 **permet** la lecture dès la fin d'une course, il ne l'oblige
  pas) ; aucune version nouvelle du texte n'est nécessaire, aucune règle de course ne change. Le script de lecture
  calcule tout, comme le texte le dit ; sa sortie sera **séparée en deux fichiers par course** (`test` ; `test_final`)
  par une version suivante du script ou un outil de partage, exécuté par session-depot, les deux poussés avec leurs
  empreintes ; le fichier `test_final` reste non affiché jusqu'à la fin du compteur.
- Conséquence pour le registre d'hypothèses de la boucle extérieure : les fiches qui se tranchent par `test_final` sont
  tranchées à la fin du compteur ; les autres à la fin de chaque course (registre v3, à l'ouverture de la lecture).

## Points à régler (aucun n'est une dépense décidée)

1. Le vivier de la famille « contrôle de délégation » pour le tirage par génération (générateur de la banque v3, ou
   autre source) ; à proposer avec le dessin du noyau du pilote 5.
2. Qui construit la v3-bis (recommandation : session-depot, qui n'a lu aucun score ; devis d'abord), et sa taille
   (recommandation : la même que la v3, 60 tâches par part, « illustratif »).
3. Le compteur de rondes de la boucle extérieure et son plafond de dépense (déjà demandés à Lazar par le protocole).
