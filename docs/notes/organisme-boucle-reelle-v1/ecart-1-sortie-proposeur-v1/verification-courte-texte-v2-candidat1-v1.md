# Vérification courte (R2) — texte v2 de la boucle réelle de l'organisme, candidat 1

**Verdict : conforme, scellable.** Le différentiel entre le brouillon 1 et le candidat 1 se limite aux corrections B1 et B2
de la contre-lecture ; les empreintes citées sont justes ; le lanceur v67 accepte le candidat sous son nom de scellement et
refuse les quatre artefacts, sortie identique à l'octet à celle versée.

Vérificateur : sous-agent neuf (Claude Fable 5.2), auteur d'aucun des fichiers vérifiés. 12 novembre 2026. Aucun appel
payant, aucune machine, aucune clé lue, rien écrit dans `registres/` (lecture seule de `registres/go.md`).

## Pièces lues (empreintes calculées sur les fichiers)

Branche `origin/prep/organisme-v66-ecart1-sortie-v1`, tête `db34560acd62fc519ef719c104dff3f6e4bf3657` ; dossier
`docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/`.

| pièce | empreinte calculée |
|---|---|
| `preenregistrement-boucle-reelle-organisme-v1-v2-brouillon1.md` | `fbdb14d32a26ab89cb2e4888f4a953ab27408023110afe7a59f1fae78ca2d024` |
| `preenregistrement-boucle-reelle-organisme-v1-v2-candidat1.md` | `80fe4f03b4905b2376b8cd16873c9ab93da3b97e4e01a9a2932be329bab0954d` |
| `contre-lecture-ecart-1-v67-v1.md` (sur `origin/main`) | `486332032dab5eb3dc27cb4bef79f6748eb581a72818cea3a2192a051acde378` |
| `ecart-1-brouillon-2.md` | `2a23fe121a113d9794e46a7a35b3c0e5ccf60ea42edb5ac47a8874f35a12636c` |
| `ecart-1-brouillon-1.md` | `6e18fc335d4d5833dfb2f78eb83a45fcf1deb1971f724cea521336806676e051` |
| `verifications-v2/verifier-lanceur-v67-texte-v2-v1.py` | `74549861333cd81112b14bb93240551a0294842d82459c0eee867abb9fd582e5` |
| `verifications-v2/sortie-verifier-lanceur-v67-v1.txt` | `dfeedc1ce6933f274ca92330002477c9ae95da07a374620763f9939ecd155bab` |
| `configuration-v8/configuration-boucle-reelle-v8.json` | `eb6262890927bfc351bf2a32c21d0dcf121445256a5ebe6c4eaee70b9265b31d` |
| `../preenregistrement-boucle-reelle-organisme-v1-v1.md` (texte v1 scellé) | `46d7545b489a2037ede235d843ef8a0c504461a0a2d697af5db40de2400fd89d` |
| `registres/go.md` (`origin/main`, lu seulement) | `3bef01b574c60dc17cd043efd1aabb43d51b71aeb6dcda6a7d790e42411ce70c` |

Tous les compagnons `.sha256` du dossier, de `verifications-v2/`, de `code-v67/`, de `configuration-v8/` et de `../code-v66/`
se vérifient (aucun écart).

## Constat 1 — le différentiel se limite à B1 et B2 : oui

`diff` entre les deux fichiers : quatre blocs, cinq lignes, rien d'autre.

- **l. 1 (B1)** : « v2 (écart 1, brouillon) » devient « v2 (écart 1) ». Conforme au texte demandé.
- **l. 3 (B1)** : « **Statut : brouillon du texte v2, non scellé, non contre-lu.** » devient le statut demandé, mot pour mot
  (candidat au scellement (R1) ; contre-lu (R2) par un sous-agent neuf, Claude Fable 5.2, verdict « scellable après
  corrections », chemin du rapport ; corrections B1 et B2 portées), l'empreinte entière du rapport `48633203…` recopiée à la
  place de la mention « empreinte à son compagnon, à recopier ici ». Le reste de la ligne est inchangé.
- **l. 10-11 (B1)** : « après sa contre-lecture (R2) et une vérification courte du différentiel v1 → v2 » devient « si la
  vérification courte du différentiel entre le brouillon 1 (`fbdb14d3…`, empreinte entière) et ce candidat le dit conforme ».
  Conforme.
- **l. 82 (B2)** : après le chemin de `ecart-1-brouillon-2.md`, ajout de son empreinte et de « calcul de la dépense :
  `ecart-1-brouillon-1.md`, empreinte, section 8 ». Conforme ; les deux empreintes sont données entières plutôt qu'abrégées
  avec renvoi au compagnon, ce qui est plus strict que le texte demandé (R6), sans changement de sens.

Aucun bloc gelé touché : les cinq lignes sont dans l'en-tête et dans la puce « Décision » de la section « Écart 1 », hors de
tout bloc ; le lanceur relit les blocs du candidat et trouve 99 empreintes égales au code, le même plan
(GO-2026-11-12-06, configuration `eb6262890927…`) que pour le brouillon 1 (constat 3).

Remarque de forme, non bloquante : les lignes 3, 10, 11 et 82 dépassent la largeur de coupe du reste du texte.

## Constat 2 — les empreintes citées dans les lignes corrigées sont justes : oui

Les quatre empreintes introduites par le candidat (rapport de contre-lecture, brouillon 1 du texte v2, brouillons 2 et 1 de
la note de l'écart) sont égales, caractère pour caractère, aux empreintes calculées du tableau ci-dessus. Le compagnon du
candidat porte `80fe4f03…`, égale à l'empreinte calculée.

## Constat 3 — le lanceur v67 accepte le candidat renommé : oui

Arbre v67 reconstruit hors du dépôt : clone neuf de `https://github.com/lciric/ideation-organism`, commit `94bfd92`, puis
paquets `organisme-v65-boucle-reelle-v2.bundle` (`origin/prep/organisme-v65-v1`, tête `cef5ea60`),
`organisme-v66-boucle-reelle-v1.bundle` (tête `7e415cba`) et `organisme-v67-boucle-reelle-v1.bundle` (tête `ab53b7f4`) ;
`94bfd92` est ancêtre de la tête v67 ; arbre de travail propre.

Script `verifier-lanceur-v67-texte-v2-v1.py` lu puis rejoué sans modification, le candidat 1 copié sous le nom
`preenregistrement-boucle-reelle-organisme-v1-v2.md` (empreinte `80fe4f03…` vérifiée sur la copie) à la place du brouillon ;
autres arguments : texte v1 scellé, configurations v8, v7 (`configuration-v7/`) et v6 (`../code-v66/configuration-v6/`),
`registres/go.md` de `origin/main`, `../code-v66/blocs-v66/heritage-depart-v65.json`. Code de sortie 0.

- Texte accepté ; 99 empreintes égales au code ; plan go = GO-2026-11-12-06, configuration `eb6262890927…`.
- Cas sain (texte v2, configuration v8, GO-2026-11-12-06) : code 2, `MachineRefusee` à la garde 22 (bwrap absent simulé),
  refus avant tout appel — donc toutes les gardes précédentes passées.
- Artefacts refusés, code 2 chacun : texte v1 (`PreenregistrementRefuse`), configuration v7 et configuration v6
  (`ConfigurationRefusee`), GO-2026-11-10-11 (`GoAbsent`).
- Garde 24 sur la configuration v8 : kimi 7 200 s (commande 7 150 s), argon 1 800 s (commande 1 750 s) ; budget d'appel des
  proposeurs 1,5 USD. « bilan : tout tient ».

La sortie rejouée a l'empreinte `dfeedc1ce6933f274ca92330002477c9ae95da07a374620763f9939ecd155bab`, identique à l'octet à
`verifications-v2/sortie-verifier-lanceur-v67-v1.txt`. (La première ligne de cette sortie dit encore « brouillon » : c'est un
libellé figé du script, pas une lecture du texte.)

## Limites

Vérification courte : je n'ai pas relu le fond du texte v2 ni rejoué le banc de mutations et la suite v67 ; ils relèvent de
la contre-lecture (`48633203…`), dont les corrections bloquantes ne touchaient que les lignes vérifiées ici. Le scellement
sous le nom `preenregistrement-boucle-reelle-organisme-v1-v2.md` doit porter l'empreinte `80fe4f03…` (copie à l'octet du
candidat 1).
