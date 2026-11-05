# Contre-lecture (R2) — rejeu des juges du pilote de T0.5 — v1

Contre-lecteur neuf : sous-agent Opus 5.5, qui n'a rien écrit de ce qu'il relit. 29 octobre 2026.
Objet relu (branche `claude/lucid-fermi-n7610d`, commit `33bd7c91`, brouillon non scellé) : devis, fiche de lancement,
configuration (`docs/notes/couche-2-preparation-v1/rejeu-juges-v1/`), `src/controle_ia/environnements/noter_rejeu_juges_v1.py`,
`tests/test_noter_rejeu_juges_v1.py`, `scripts/amorce_rejeu_juges_v1.sh`, `scripts/rejeu_juges_instance_v1.sh`,
`docs/procedures/rejeu-juges-v1/lancer_rejeu_juges_v1.sh` ; fonctions importées (`rubrique.py`, `pilote_a.py`,
`harnais/episode.py`, `harnais/modeles.py`, `manifeste.py`, `gardes.py`, `validation_reelle.py`). Références : structure des
notations rejouées et du manifeste des notations ; contre-lecture CLR de la régénération des sondes de P3.
Essais : **41 réussis en 80 s** (`tests/test_noter_rejeu_juges_v1.py`).

## Verdict : **lançable après corrections**

La lecture par la probabilité du jeton de verdict est juste dans son principe : une position de décision par critère, placée
à partir du jeton qui suit les deux-points, probabilité d'une valeur par la règle de la chaîne, aucune moyenne ni médiane sur
des jetons, aucun score imputé. Les paramètres des juges sont ceux des notations rejouées (onze clés égales, vérifié).
L'empreinte de la configuration (`07d7fd81…`) et celle de la consigne (`7c8ef0c9…`) égalent les citations de la fiche. Les
seuils de Wilson annoncés (H_B tranchée si k ≤ 175 ; H_A si k ≥ 179) sont exacts.

Restent quatre défauts majeurs, chacun corrigible en moins d'une heure, sans dépense :
- deux feraient perdre une lecture déjà payée (CLJ-01, CLJ-02) ;
- un peut produire un faux H_B « tranché » (CLJ-03) ;
- un répète CLR-06 : rien ne borne la facture si la session se perd (CLJ-04).

## Constats

### CLJ-01 — majeur — Après un arrêt consigné, la lecture gelée ne lit plus aucune phase, même écrite
- Où : `noter_rejeu_juges_v1.py:748` (`lire_rejeu` exige `resume.json`) ; fiche, Plan d'analyse, point 2 (« par elle seule »).
- Défaut : `resume.json` n'est écrit qu'en fin de run. Un TERM pendant la phase 6 empêche donc `--lire` de lire les cinq
  phases déjà écrites et scellées : délai externe (CLJ-02), plafond de l'amorce, panne de mémoire. `arret.json` contient
  pourtant `partiel.phases`, avec le statut « écrit » de chacune. Les lire autrement serait un écart au préenregistrement,
  donc un nœud. L'essai `test_signal_term_consigne_et_propage` ne relit rien après l'arrêt.
- Correction :
  - sans `resume.json`, prendre les phases dans `arret.json` (`partiel.phases`), vérifié par `verifier_resultat` ;
  - la phase en cours devient « non mesurée (arrêt) » ;
  - ajouter un champ `source: "arret"` à la lecture ;
  - écrire dans la fiche que les phases écrites avant un arrêt se lisent ;
  - essai : TERM après la phase 2, puis `lire_rejeu` lit les deux premières cellules.

### CLJ-02 — majeur — Le module ignore le délai externe réduit : une phase peut être coupée après avoir coûté
- Où :
  - chaîne, `rejeu_juges_instance_v1.sh:215-224` et `:230` : `DELAI = min(95, reste avant le plafond − 13)` ;
  - module, `:583` et `:624` : l'échéance globale vient de la configuration seule (85 minutes) ;
  - fiche, Bornes de temps, l. 210-213 ; devis, l. 152-154 (« aucune phase n'est donc coupée… »).
- Défaut :
  - le module peut aller jusqu'à environ 89 minutes (85, plus le dernier lot) ;
  - le délai externe tombe sous 89 minutes dès que la mise en place dépasse environ 28 minutes, alors que le devis prévoit
    jusqu'à 40 minutes ;
  - une phase qui commence parce qu'elle tient dans les 85 minutes est alors tuée par `timeout` : elle a coûté, elle ne laisse
    aucun fichier, et l'affirmation du devis devient fausse ;
  - avec CLJ-01, tout le run devient illisible.
- Correction :
  - la chaîne passe l'échéance absolue au module (par exemple `--echeance-externe <secondes depuis 1970>`, moins 6 minutes
    pour le dernier lot et la consignation) ;
  - le module prend `min(début + duree_globale_s, échéance externe)` comme échéance globale et la consigne dans `resume.json`
    et dans `arret.json` ;
  - essai jouet : une échéance externe courte donne « non-commencé », jamais un TERM au milieu d'une phase ;
  - corriger la phrase du devis et celle de la fiche.

### CLJ-03 — majeur — Le contrôle de l'instrument porte sur la loi renormalisée et ne voit pas un effondrement de la masse
- Où : `noter_rejeu_juges_v1.py:722-739` (`alignement` lit `probabilites`, renormalisées) ; fiche, Métrique (« Alignement
  de l'instrument ») et critère gelé 3 ; essai `test_controle_d_alignement_cas_sain_et_artefact` (l. 273).
- Défaut :
  - Une erreur de position ou d'encodage des valeurs se manifeste surtout par une masse admise quasi nulle : préfixe faux,
    jeton « ␣- » mal découpé, décalage d'un jeton. La loi renormalisée peut rester plate, et la note écrite n'y est alors
    jamais sous 0,001.
  - Démontré avec les outils des essais : modèle à bigrammes dont la masse part sur un jeton « x », proportions égales entre
    valeurs. Résultat : masse maximale 3,7e-5, aucun score appuyé, et pourtant `alignement` rend **« aligné »** (500 critères,
    0 improbable).
  - La cellule se lirait alors « H_B : cellule à redéfinir », **tranchée** : un faux négatif, qui pourrait condamner à tort la
    cellule des juges.
  - L'essai d'artefact ne fait baisser que la loi renormalisée. Il passerait donc avec ce défaut.
- Correction :
  - Faire le contrôle sur la **probabilité brute** de la note écrite : `p × masse`, déjà consignées toutes deux. Comme la note
    écrite a été tirée à la température 1, sans troncature de la loi (`generer_lot`, vérifié), la borne reste « au plus
    6 × 0,001 attendu ».
  - Garder la part renormalisée comme descriptif.
  - Essai : le cas « masse effondrée » ci-dessus doit rendre « désaligné ».
  - Mettre la fiche à jour.

### CLJ-04 — majeur — Aucun réveil programmé : rien n'arrête la facture si la session se perd (répète CLR-06)
- Où : devis § 6 et § 8.4 ; fiche, Bornes de temps ; lanceur `:101-102` et `:124` (heure d'arrêt écrite, rien de programmé).
- Défaut :
  - Le pire cas fait 150 minutes facturées à 1,43 USD/h, soit 3,58 USD, plus le téléchargement : environ 3,9 USD, pour
    4 USD de plafond. La marge est d'environ 5 minutes, et elle n'existe que si la session arrête l'instance dans les
    10 minutes qui suivent la fin de l'amorce.
  - L'instance ne s'arrête jamais seule. Une session perdue dépasse le plafond environ 168 minutes après la création.
- Correction :
  - à la création, programmer deux réveils de la session (tâches programmées « une fois ») à création + 140 minutes et
    création + 155 minutes ; chacun inventorie, arrête par identifiant (R10) et consigne dans `registres/arrets.md` ;
  - consigner leurs identifiants dans `lancement.txt` ;
  - écrire ces réveils dans la fiche et dans le devis § 8.4.
  - Facultatif : ramener le plafond de l'amorce à 120 minutes une fois CLJ-02 corrigé (le run est borné de toute façon), pour
    rendre de la marge.

### CLJ-05 — moyen — Audit R4 asymétrique : seul le résultat favorable est audité
- Où : fiche, critère gelé 4 (l. 138-140).
- Défaut : seuls « 180 sur 180 » et « toutes les masses au-dessus de 0,99 » déclenchent l'audit. R4 exige le même audit pour
  un résultat négatif trop propre, par exemple :
  - une cellule à 0 ou presque ;
  - toutes les masses sous 0,01 ;
  - beaucoup de notations dont la note écrite est complète et valide (`finis_ecrits`) alors que la lecture par probabilité
    est sans appui.

  C'est la signature de CLJ-03.
- Correction : ajouter ces déclencheurs symétriques, par exemple `finis_ecrits − finis appuyés > 5 % de n`. Geler la graine du
  tirage des vingt notations auditées : clé `audit-r4/<cellule>` dérivée de l'entropie (R9). Aujourd'hui, « graine consignée »
  ne fixe rien.

### CLJ-06 — moyen — Une valeur est lue par ses jetons de tête : « 2.5 » compte pour 2, « 3/5 » sur une échelle /4 compte pour 3
- Où : `noter_rejeu_juges_v1.py:296-310` et `:405-416` ; essai `test_demi_point_lu_par_probabilite…` (l. 120), voulu ;
  fiche, Métrique, « M … masse » et critère gelé 1 (« ni note ramenée »).
- Défaut :
  - Le tokeniseur de Llama 3 découpe les chiffres à part. La probabilité de « 2 » inclut donc « 2.5 », « 2/5 » et
    « 2 out of 5 ». La masse M n'est pas « la probabilité que le juge écrive une valeur admise », mais celle qu'il commence
    par une valeur admise.
  - Au pilote, chez les réponses non tronquées, on compte 170 notes « non entière ou illisible » au 8B et 9 « échelle /5 »
    au 8B comme au 3B.
  - Pour b0 relu, le devis l'assume (« affaire de format »). Mais une cellule « verdict d'abord » pourrait tenir H_A en partie
    grâce à des notes que la lecture écrite déclare fausses, sans que rien ne le rapporte.
- Correction, au minimum :
  - écrire la définition exacte dans la Métrique (« probabilité des jetons de la valeur, quelle que soit la suite ») ;
  - ajouter par cellule un descriptif gelé : « finis appuyés dont au moins une note écrite est non entière, hors échelle ou
    d'une autre échelle » ;
  - en faire un déclencheur d'audit s'il dépasse 2 % de n.

  Option plus stricte (à proposer, non requise) : multiplier par la probabilité qu'un jeton de fin de valeur suive (fin de
  ligne, espace, virgule).

### CLJ-07 — mineur — 180 notations, mais 120 textes : l'intervalle de Wilson suppose 180 tirages indépendants
- Où : fiche, Seuil (l. 108-113) ; `etiquette_completude` (`:688-698`). Le devis parle de « 180 textes ».
- Défaut : 60 ensembles sont notés deux fois (passe-0 et passe-1 ; 120 empreintes d'ensemble distinctes, vérifié). L'étiquette
  « tranchée » est donc un peu optimiste. La lecture ponctuelle (k ≥ 179) n'est pas touchée.
- Correction : écrire « 180 notations de 120 textes ». Rapporter aussi, en descriptif, la complétude et l'intervalle sur les
  120 passe-0.

### CLJ-08 — mineur — D-S13 laissée « non tranchée » dans un préenregistrement
- Où : devis § 2 (l. 41-47) ; fiche, « Ce que ce rejeu ne décide pas » (l. 239-240).
- Défaut : la métrique du préenregistrement renvoie à une décision dont la fiche dit la lecture incertaine. Le texte transmis
  par la session est : « scores continus, probabilité du jeton de verdict, pour toute cellule de G1 ». Il confirme la lecture
  du GO.
- Correction : citer ce texte, avec sa source et son empreinte si elle existe, et clore la divergence avant le scellement.

### CLJ-09 — mineur — Annonces de temps et descriptifs
- Phase 5. Elle ne commence que si au plus 45 minutes ont passé : les phases 1 à 4 et les chargements doivent tenir dans
  l'attendu, soit environ 42 minutes. « Toutes les variantes tiennent dans l'attendu » (devis l. 141) est donc juste, mais à
  3 minutes près. Le dire.
- Ré-encodage. Les réponses scellées sont ré-encodées, pas relues jeton par jeton. Consigner par notation
  `jetons_reponse_reencodes` à côté de `jetons_reponse_rejoues` : une dérive de tokenisation deviendrait visible.
- Banc. Le banc de la chaîne (devis § 8.3, cas A à E et refus du lanceur) n'existe que dans le bloc-notes du rédacteur. Verser
  ses journaux, avec empreintes (R6). Le refaire après les corrections ci-dessus, qui touchent la chaîne.

## Vérifié sans défaut
- **Position lue.** Elle part du jeton qui suit les deux-points. Avec l'expression de découpage de Llama 3 et
  `tokenizers 0.23.2` (version épinglée), sur un tokeniseur simulé, j'obtiens :
  - « : -1 » donne « : », « ␣- », « 1 » ; « : 3 » donne « : », « ␣ », « 3 » ;
  - les décalages sont exacts, y compris pour « ␣** » et « :** ».

  Le préfixe et la position de décision sortent justes. La règle de la chaîne, les branches hors du chemin écrit et le cas
  « valeur coupée au 192e jeton » sont justes eux aussi. Aucune moyenne sur des jetons.
- **Score manquant.** Une réponse tronquée, un critère absent ou une valeur absente donnent un score manquant, avec son
  motif ; rien n'est imputé (essais).
- **Paramètres et graines.**
  - Les paramètres sont égaux à ceux des notations rejouées. L'entropie est celle du pilote. La graine `modele-jouet` est
    identique.
  - Une clé de graine par génération, par `SeedSequence` (manifeste, R9). b0 relu ne tire rien.
- **Lanceur.**
  - Garde de calcul dans un `if` (CLR-03 corrigé).
  - Aucune autre instance ; crédit relu, au moins 4,50 USD.
  - Offre choisie juste avant la création, filtrée sur le prix, la fiabilité, CUDA et le téléchargement.
  - Jetons masqués ; fiche, devis et configuration scellés et contrôlés (CLR-05 corrigé) ; commit du code ancêtre du commit
    lancé.
- **Chaîne.**
  - Les résultats sont poussés quel que soit le résultat, car aucun verdict n'est calculé sur l'instance (CLR-04 sans objet).
  - Arrêt consigné sur TERM, sur sortie imprévue et sur KILL (depuis l'amorce).
  - Lignes `PROGRES` sans texte.
- **Fils d'OpenBLAS (CLR-01, CLR-02).** Sans objet : aucune algèbre linéaire de numpy, et aucune identité au bit près visée.
- **Mémoire.** La génération ne garde que les logits du dernier jeton. Les passes forcées gardent les seules positions voulues.
  Pas de risque visible sur 80 Go.

## Ce que je n'ai pas pu vérifier
- Le vrai tokeniseur de Llama 3.1 et 3.2 n'est pas sur ce disque, et je n'ai aucun réseau. Les décalages ne sont vérifiés
  que sur une simulation. Je recommande une garde bon marché au contrôle du format, avant les phases : encoder « X: -1 » et
  « X: 0 », puis exiger les découpages et décalages attendus. Sinon, arrêt.
- Les rythmes des passes forcées sur A100 restent SUPPOSÉS. Mon estimation (≈ 3 s par notation au 8B, ≈ 1 s au 3B) tient
  sous les durées maximales.
- Le banc de la chaîne du rédacteur ; la suite ciblée complète (166 essais annoncés).
- Le texte source de D-S13.
