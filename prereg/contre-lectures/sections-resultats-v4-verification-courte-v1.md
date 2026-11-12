# Vérification courte des sections de résultats v4 (dossier d'entretien)

- **Vérificateur** : sous-agent neuf de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, modèle déclaré par l'environnement : Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur (Opus 5.5). Je n'ai écrit ni les sections, ni leur registre, ni la contre-lecture 1, ni aucune pièce citée.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-verification-courte-sections-resultats-v4-v1.md`, sha256 `e65f165abce318d9118916fcac6932a755dbd79a14cf0ae7a06a028c94c2125e`, égale à son compagnon.
- **Heures** (relevées par `date -u`, 10 novembre 2026) : début 12:26:55 UTC ; dernier relevé des registres 12:28:53 UTC (`registres/decisions.md`, dernière ligne R-2218, 2 176 lignes ; `registres/go.md`, 300 lignes, `2c396b01…`) ; écriture de ce rapport à 12:29:53 UTC.
- Aucun commit, aucune poussée, aucun `fetch`, aucun appel de modèle ni d'interface externe, aucune dépense. Aucun chemin interdit ouvert ; aucune recherche récursive ; `verifier-arbre` et suite des essais non lancés. Aucun refus de permissions rencontré. Aucun taux de calibration écrit ici.

## 1. Verdict

**Transmissible au jury après corrections** : un seul couple exigé (VR-01, section organisme), deux couples d'en-tête à la main de la mère (VR-02).

La différence v3 → v4 se limite aux zones des 23 couples et des dix retouches E-01 à E-10 déclarées. Les couples modifiés disent ce que disent leurs sources, et aucun statut n'est devenu faux entre le relevé du rédacteur (12:24 UTC) et le mien (12:28:53 UTC, R-2217 et R-2218 lues).

## 2. Ce que j'ai vérifié, et comment

| objet | méthode | résultat |
|---|---|---|
| Fichiers à lire | `sha256sum` contre la consigne et les compagnons | égales : programme `e93b0901…`, organisme `77d0e57a…`, registre `f7310529…`, journal `7a49ee1e…`, contre-lecture 1 `858d92be…` ; v3 égales à leurs compagnons (`35589b82…`, `d6d702f5…`, `38c24c92…`, `4daf80db…`) |
| Différence v3 → v4 | `git diff --no-index --word-diff` sur les deux sections, chaque zone changée rapportée à une ligne du journal § 2 | programme : 20 lignes changées, toutes couvertes par E-01 à E-05, E-08 et P-01 à P-18 ; organisme : 4 lignes changées, toutes couvertes par E-06, E-07, E-09, E-10 et O-01 à O-05 ; rien d'autre |
| Rejeu des couples de la contre-lecture 1 | script : compte de chaque texte ancien et neuf dans la v3 et la v4 | 23 anciens présents une fois en v3 ; les 11 couples dits « verbatim » ont leur texte neuf une fois en v4 (P-03, P-04, P-09, P-13 à P-17, O-02, O-03) ; les 12 couples dits « modifiés » ont un texte neuf propre, relu contre source ; les anciens de P-18 et O-03 subsistent parce que leur texte neuf les contient |
| Sources des couples modifiés | lecture des lignes R-2193 à R-2218 de `registres/decisions.md`, des lignes 273 et 297 à 300 de `registres/go.md`, de VA3 l. 214-226 (`defd8ef0…`), de CLV65 l. 1-20, 60-86 (`c4ddfc7f…`), de `registres/scellements-v1.md` l. 5, de T08A (`72b067d5…`) | conformes, sauf VR-01 |
| Statuts | registres jusqu'à R-2218 ; listes de fichiers de `brouillons/`, de quatre de ses dossiers, de `docs/verdicts/`, de `code-v65/` | exacts à 12:28:53 UTC |
| Registre des affirmations | renvois par script ; lecture des rangées retouchées ; numéros de ligne relus dans les pièces | 98 et 53 renvois, tous avec rangée ; numéros exacts (section 4) |
| Mots à ne pas trouver | script sur les deux sections | aucun taux de calibration, aucun numéro R-, identifiant de session, nom du directeur, nom de modèle, commentaire HTML ; balises équilibrées (304 et 130) |

Limites : je n'ai pas relu les zones inchangées depuis la v3 (elles relèvent de la contre-lecture 1) ; je n'ai pas relu les PDF ; je n'ai pas rejoué le script du rédacteur, resté hors du dépôt, seulement son effet.

## 3. Constats

Gravités : **à corriger** (avant transmission), **mineur**, **information**.

### VR-01 — à corriger — la course réelle « attend le code corrigé », alors que l'autorisation exige un code contre-lu
- **Lieu** : section organisme, § 5, dernière phrase (retouche E-10, puis couple O-05), renvoi [B51].
- **Preuve** : `registres/go.md` l. 273 (GO-2026-11-08-02 : « après le code v65 contre-lu ») et l. 300 (GO-2026-11-10-10 : « conditions […] toutes exigées : code v65 contre-lu »). La v3 écrivait « elle attend le code contre-lu » ; E-10 l'a remplacé par « le code corrigé ». La phrase suivante dit la dépense autorisée « sous ces mêmes conditions » : elle renvoie donc à une condition plus faible que celle de la ligne d'autorisation. La rangée B51 du registre, elle, dit bien « code contre-lu ».
- **Correction** : couple VR-C1.

### VR-02 — mineur — « vérification courte à venir » sera faux à la transmission
- **Lieu** : les deux sections, alinéa de statut (couples P-01 et O-01, formule décidée par la mère).
- **Preuve** : la présente vérification est rendue. La formule porte aussi un fragment d'empreinte dans un texte destiné au jury ; c'est le choix de la mère, je ne le discute pas.
- **Correction** : couples VR-C2 et VR-C3, à la main de la mère.

### VR-03 — mineur — renvoi [A83] écrit deux fois dans la même phrase
- **Lieu** : section programme, § 7, premier alinéa (couple P-18).
- **Preuve** : « la version finale n'est pas écrite [A83] ; les verdicts de son complément […] avant la version finale [A83] ». Sans effet sur le sens. Aucune correction exigée.

### VR-04 — information — points de la consigne, contrôlés sans constat
- **P-05** : 2,4 à 4,6 dollars pour la relecture, 11 à 17 pour l'ensemble, pire cas d'environ 33 contre un plafond de 30 : VA3 l. 222-223 et l. 226. L'ordre d'abandon (doses 0,25 et 0,75 du témoin, sonde Mahalanobis de la relecture) : VA3 l. 226 et R-2210. Création du témoin après la création de la course de confirmation, relecture sur une machine à part : R-2207.
- **P-06** : brouillon 1 contre-lu, deux bloquants (R-2200) ; brouillon 2 vérifié, huit couples (R-2214) ; scellement à 12:21:55 UTC, avant toute création de 7b (R-2216 ; `registres/scellements-v1.md` l. 5 ; empreinte `72b067d5…` égale au fichier et à son compagnon) ; douze traits, « ajout permis » (R-2211) ; consigne du code à écrire (R-2216).
- **O-04** : verdict, rejeu à l'identique, deux bloquants, « rien de cela ne touche une dépense » : CLV65 l. 10 et sections CLV65-01, CLV65-02 ; v66 sous noms neufs, développeur neuf : R-2215. « Rendre une issue » pour « prononcer C1 » ne dit rien de plus que la source. « Les mutations » désigne le banc annoncé (38 sur 38), que la source dit rejoué à l'identique.
- **P-07 et Bailey** : une seule occurrence de « Bailey » dans la section programme, aucune dans la section organisme. Les mots sont ceux de la ligne GO-2026-11-10-10 (« témoin de l'attaque publiée de Bailey », 75 dollars, aucun report, dépassement au directeur). Rien du devis, de la licence, du préenregistrement ni du bras.
- **« 0,660 »** : une seule occurrence, table du § 5 de la section programme, « Aire minimale détectable à 80 % : […] 0,575 à 0,660 (autres sondes) [A67] », présente dès la v3 ; c'est une aire de T0.7, non la variante de taux de R-2204.
- **Autres statuts** : P-08 à P-12, E-03 à E-05, E-08, E-09 conformes à R-2197, R-2198, R-2203, R-2205, R-2210, R-2212, R-2215, R-2216. Aucun brouillon 12 de P3-bis, aucun brouillon 22 de T0.7, aucun dossier « accumulation » sur disque ; verdict de T0.3 absent de `docs/verdicts/`.
- **Lignes arrivées après le relevé du rédacteur** : R-2217 (rendu de la v4) et R-2218 (réponses pour le registre des prédictions, contre-lecture du socle de preuves, jalon d'architecture) ne rendent fausse aucune phrase des deux sections. `registres/go.md` n'a pas bougé.

## 4. Registre des affirmations v4

- **N-064** (`387c9d4e…`) : énoncé retenu l. 13, principe occupé depuis 2015 et mondes où toute promotion est fausse l. 14, citations obligatoires l. 15 : rangées B1, B2, B5, B41, B42, B45 exactes.
- **N-065** (`f820e90d…`) : rôle 1 adopté l. 15-18 : rangée B4 exacte.
- **A40** → R-2186 (l. 2144) ; **B39** → R-2162 (l. 2120, « deux décisions ouvertes ») : exacts.
- Dix-sept numéros de ligne R- relus (R-2148 à R-2215) : tous exacts.
- Pièces ajoutées VA3, CL1, T08A, CLV65 : empreintes égales aux fichiers.
- Pièces DEC et DEC3 : l'empreinte `19bb7df8…` est celle de `registres/decisions.md` aux commits `d1a62920b` et `617d77d47` (dernière ligne R-2216), vérifiée par `git show`. Le fichier vivant a avancé depuis (`85806a8e…` à 12:28:53 UTC), ce que le registre annonce.
- La rangée B51 est exacte et ne demande aucune retouche pour VR-C1.

## 5. Couples ancien → nouveau

Chaque texte ancien figure une fois et une seule dans son fichier v4 (vérifié par script).

| n° | constat | fichier | ancien | nouveau |
|---|---|---|---|---|
| VR-C1 | VR-01, exigé | `section-resultats-organisme-v4.html` | `elle attend le code corrigé,` | `elle attend le code corrigé et contre-lu,` |
| VR-C2 | VR-02, à la main de la mère | `section-resultats-programme-v4.html` | `corrections appliquées, vérification courte à venir.` | `corrections appliquées, puis vérifié par un autre lecteur.` |
| VR-C3 | VR-02, à la main de la mère | `section-resultats-organisme-v4.html` | `corrections appliquées, vérification courte à venir.` | `corrections appliquées, puis vérifié par un autre lecteur.` |

## 6. Points ouverts pour la mère

1. Appliquer VR-C1 change l'empreinte de la section organisme : version neuve (R12) et rangée du journal. Un rejeu du seul couple par script suffit ; je ne demande pas de nouvelle lecture.
2. Les statuts sont ceux de 12:28:53 UTC. Si une ligne du registre touche l'adaptateur, la règle « mots et coût », l'audit des fuites, P3-bis, le code de l'organisme ou une autorisation avant la transmission, les phrases correspondantes sont à relever.
3. La contre-lecture de la v66 n'est inscrite par aucune ligne lue ; VR-C1 ne dit que la condition de l'autorisation.
