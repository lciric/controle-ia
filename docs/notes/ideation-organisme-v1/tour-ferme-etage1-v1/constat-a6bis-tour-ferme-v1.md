# Tour fermé, étage 1 — constat de l'annexe A.6 bis, à jouer chez la fille avant le premier appel, v1

Écrit le 3 novembre 2026 à 01:47 UTC (heure relevée par `date -u`) par session-depot. Il tient lieu des corrections sans code
demandées par la contre-lecture courte des commandes v4
(`docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/contre-lecture-v4/contre-lecture-commandes-tour-ferme-v4-v1.md`,
`e8f3a4afc40d1d56dfe986f280fd3fcb3a7cc203ac0fd0827f0195fcefe77111`, branche `outils/commandes-tour-ferme-v1`). Chaque point est
relevé chez la fille et écrit dans son rapport de lancement scellé **avant** le premier appel de modèle ; un point non tenu arrête
le lancement (rien n'est appelé).

## 1. Fichiers et empreintes (mineur 7 ; A.2)
- Configuration gelée : `docs/notes/ideation-organisme-v1/tour-ferme-etage1-v1/configuration-tour-ferme-v3.json`
  `642b3c5f30a99dcc50f30ada8d53b1a55e05f9e1a65dc310505bcba34f6a4826` (octets égaux au brouillon 2 ; pièces sous `pieces/`, à côté,
  empreintes déclarées dans le fichier).
- Commandes, extraites de `outils/commandes-tour-ferme-v1` à leur chemin absolu, empreintes égales :
  `/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_kimi_v4.py` `10afdab5…`,
  `…/commande_argon_v56_nuit_v4.py` `5c6d5149…`, `…/registre_depense_cumulee_v1.py` `8ba92066…` ; interpréteur `/usr/bin/python3`
  (empreinte relevée au manifeste).

## 2. Relais dédiés, neufs, sans autre usage pendant la course (important I1)
La v64 lit tout code 4 « rien envoyé » comme une fin des tours de la carte ; un refus propre d'un relais (402 plafond, 429 nombre
d'appels) n'est connu d'aucune garde de l'orchestrateur et viderait les cartes restantes en silence. Il faut donc qu'il ne puisse
pas arriver :
- **relais Kimi** (`relais_kimi_v3.py`, port 8804), démarré pour cette course seule : `--plafond-usd 50` (au moins 44 plus la
  réserve par appel, 0,40 par défaut), `--max-appels 1800` (au moins 1 731), `--prix-entree 2`, `--prix-sortie 10` ;
- **relais Argon** (`commande_argon_v56_nuit_v2.py servir`, port 8805), démarré pour cette course seule, jamais partagé avec A1-v3
  ni une autre course : `--plafond-usd 10` (au moins 6), `--max-appels 200` (au moins 147) ;
- relevé `GET /relais/etat` des deux relais **avant le premier appel** (plafond, appels, dépense nulle, clé présente en booléen
  seulement) et à la fin ; les deux relevés scellés au rapport.

## 3. Ce qui est accepté par écrit
- **Registre illisible** (important I2) : un registre de dépense illisible serait lu de la même façon (fin des tours). Probabilité
  faible : le registre est créé neuf dans le dossier de sortie, écrit sous verrou (`fcntl`) par les seules commandes de la course.
  Accepté pour ce lancement ; une version 5 des commandes le passerait en code 3.
- **Refus de l'expérimentateur en fin de borne** (mineur 6) : la commande de Kimi refuse sans rien envoyer (code 4,
  `cause_refus = plafond_session`) une consigne longue quand le reste de la borne de 0,80 USD de la carte ne la paie plus (par
  exemple ≈ 28 400 caractères à 0,10 USD de reste) : c'est la lecture voulue par TF-02 (a), une fin des tours de la carte.
- **Clés d'étape du registre** (mineur 1) : sous la v64, l'étape transmise est `tour_ferme_v64` ; les commandes v4 réservent sous
  `tour_ferme_v64/kimi` et `tour_ferme_v64/argon` (vérifié par la contre-lecture sur copie).
- **Barème** (mineur 2) : `fournisseurs.kimi.prix_entree_usd_par_million_jetons` = 2 (le `--prix-entree` de la commande de Kimi),
  `fournisseurs.argon.…` = 10 (le prix d'entrée du barème prudent de la commande d'Argon) ; la commande de Kimi, qui compte un jeton
  par octet plus 1 024, refuse avant la vérification de la v64 (trois caractères par jeton) : même lecture.

## 4. Environnement de l'orchestrateur (annexe A.8)
`env -i` avec la liste blanche ; `POLE_MACHINE_JETABLE_V56=1` ; `TMPDIR=/tmp` ; `bwrap` 0.9.0 ; identité dédiée sans privilège
pour le bac ; aucune variable de clé dans l'environnement de l'orchestrateur (les relais tiennent les clés).
