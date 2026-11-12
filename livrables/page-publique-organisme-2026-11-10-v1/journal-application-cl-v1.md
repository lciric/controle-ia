# Journal de l'application de la contre-lecture v1 aux brouillons de la page A1-v4 — v1

Agent neuf (sous-agent de la session mère), travail mécanique. 10 novembre 2026, de 10:32:16 à 10:35:55 UTC (heures relevées par `date -u`). Aucune écriture git, aucune poussée, aucun appel externe, aucune dépense, aucun refus de permission ni de classifieur.

## 1. Entrées (empreintes vérifiées avant lecture, toutes conformes)

| Fichier | sha256 |
|---|---|
| `resultats/attaque-goodhart-v2/README.md` (brouillon de la page) | `9f24f5598ac2838be648a38485c6c961ff0d5700319dbaa46266bff5d2b1c496` |
| `README.md` (brouillon du README racine) | `8e413d7801897c43dae849f712c6cdb1ac875e0532355208f03eba56cb37faa7` |
| `contre-lecture-page-a1v4-v1.md` | `3cedcd29629598bc522b86f7900ed020f29e53855bffe0eb036bb8d2c1e0f8db` |
| texte scellé `preenregistrement-attaque-goodhart-v5-v1.md` (dépôt de travail, l. 367 seule lue) | `d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6` (égale à `d306a8fa…7fe6` de la contre-lecture et de R-2013) |
| clone `ideation-organism` | tête `f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0`, arbre propre ; `README.md` `1105f573…2704`, page `dc2a3d66…82bc` |

## 2. Vérification du couple B2 (écart « Argon seul »)

Sources lues : `registres/decisions.md`, lignes R-2013 et R-2043 seules (`grep -n "^| R-2013 \|^| R-2043 "`) ; texte scellé, § 8, l. 367 seule (`sed -n '367p'`).

- **§ 8, l. 367** : « Argon seul » — aucune autre utilisation d'Argon pendant la course ; « une utilisation pendant la course est un écart déclaré, lu par l'audit A9, jamais un arrêt ». Le mot « declared » de B2a et le « second » écart déclaré de B2b sont donc conformes à la source.
- **R-2013** : une autre utilisation d'Argon (même fournisseur, même clé) a eu lieu pendant la course ; la ligne en donne la cause et un compte d'appels, ni l'un ni l'autre repris ici ni sur la page.
- **R-2043** : nœud tranché par le directeur, option (a) : course gardée telle quelle, écart écrit au journal, l'audit regarde la fenêtre et écrit une réserve seulement s'il y a eu perturbation. Le « by the project lead's decision » de B2a est conforme. La phrase « aucun écart au préenregistrement scellé » de R-2043 porte sur la décision (option (a) ne modifie pas le texte scellé), non sur l'utilisation elle-même, que le § 8 nomme écart déclaré : pas de contradiction avec B2a et B2b.
- **B2a — texte corrigé remplacé sur consigne de la mère** (la page ne nomme ni l'étiqueteur ni aucun autre projet ; l'écart se dit « a third-party use of the same provider during the run, declared; no disturbance measured » ; aucun chiffre). Le texte de la contre-lecture (« another task of the project called Argon… ») n'est pas appliqué tel quel ; texte appliqué (surcharge déclarée dans le script, `SURCHARGES_CORRIGE`) :

  > 6. **Argon deviation** (both worlds): a third-party use of the same provider during the run, declared; no disturbance measured, no call of this run inside its window. The sealed text asks that nothing else use Argon during the run; by the project lead's decision, a disturbance reservation is written only if there was one, and the audit finds none.

  Toutes les propositions du texte actuel sont gardées ; aucun chiffre ajouté ; ni l'étiqueteur ni un autre projet nommés.
- **B2b** : conforme aux trois sources, sans chiffre ni nom ; appliqué tel que proposé.
- **Nuance pour la mère, non tranchée ici** : d'après R-2013, l'utilisation venait d'une autre tâche du même programme, sur la même clé ; « third-party » se lit donc « extérieure à cette course ». Un lecteur pourrait le lire « extérieure au projet ». Formulation de la mère, gardée telle quelle.

## 3. Couples (22 lus, 22 appliqués, aucun refusé)

Script : `/home/user/page-a1v4/appliquer-cl-v1.py` (`554c888320d6b20b9117429fc387ca95d8a1a67b1c1537668207be2ba555dcd3`), lancé par `python3 -I`, code de sortie 0. Il vérifie les trois empreintes d'entrée, lit les couples dans l'ordre du fichier (en-têtes `**ID — … — `fichier` — `, blocs ```text après « Texte actuel : » et « Texte corrigé : »), exige 22 couples à identifiants distincts, applique chaque couple à l'état courant de son fichier seulement si le texte actuel y figure exactement une fois, et n'écrase aucune sortie.

| Couple | Fichier | Ligne d'en-tête (contre-lecture) | Occurrences (brouillon / état courant) | Appliqué |
|---|---|---|---|---|
| B2a | page | 43 | 1 / 1 | oui, texte corrigé surchargé (section 2) |
| B2b | page | 57 | 1 / 1 | oui |
| C1 | page | 73 | 1 / 1 | oui |
| C2 | page | 87 | 1 / 1 | oui |
| C3 | page | 101 | 1 / 1 | oui |
| C4 | page | 115 | 1 / 1 | oui |
| C5 | page | 129 | 1 / 1 | oui |
| C6 | README | 143 | 1 / 1 | oui |
| C7 | README | 157 | 1 / 1 | oui |
| C8a | page | 171 | 1 / 1 | oui |
| C8b | page | 185 | 1 / 1 | oui |
| C8c | page | 199 | 1 / 1 | oui |
| C9 | page | 213 | 1 / 1 | oui |
| M1 | README | 229 | 1 / 1 | oui (dans le paragraphe « Related work » ; disparaît avec lui dans la variante sans) |
| M2 | page | 243 | 1 / 1 | oui |
| M3 | page | 257 | 1 / 1 | oui |
| M4 | page | 271 | 1 / 1 | oui |
| M5 | page | 285 | 1 / 1 | oui |
| M6 | README | 299 | 1 / 1 | oui |
| M7 | page | 313 | 1 / 1 | oui |
| M8 | page | 327 | 1 / 1 | oui |
| M9 | page | 341 | 1 / 1 | oui |

Couples non appliqués : aucun. Contrôle a posteriori (`diff` brouillon → v2) : seules changent les lignes visées par les couples et la ligne « Last updated » (page : l. 3, 10–11, 15, 17, 23, 31, 34–35, 37, 51–53, 55 ; README : l. 7, 9, 131).

## 4. Ligne « Last updated », variantes

- Page : `Last updated: 10 November 2026, 10:18 UTC` → `Last updated: 10 November 2026, <<HEURE_POUSSEE>> UTC` (une occurrence ; la date et « UTC » restent, la mère remplit l'heure au moment de la poussée). Le README racine n'a pas de ligne « Last updated ».
- `v2/README.md` : avec le paragraphe « Related work » (l. 7).
- `v2-sans-related-work/README.md` : même texte, sans la ligne 7 (commençant par `**Related work.**`) ni la ligne vide qui la suit ; aucun renvoi résiduel (POPPER, Ladder, Dwork, Co-Scientist, Gottweis : zéro occurrence).
- La page des résultats est identique, à l'octet, dans les deux variantes.

## 5. Correctifs contre le clone et application à blanc

- Correctifs `diff -u` (étiquettes `a/` et `b/`, à appliquer par `patch -p1` à la racine du clone) : trois blocs chacun, deux fichiers (`README.md`, `resultats/attaque-goodhart-v2/README.md`).
- Application à blanc dans deux copies jetables du clone (dossier temporaire de session, jamais dans le clone) : `patch -p1 --dry-run` code 0 pour les deux variantes, aucun rejet ; puis application réelle dans la copie : code 0, aucun fichier `.rej` ni `.orig`, résultat égal à l'octet aux sorties de la variante (`cmp`). Copies supprimées ensuite.
- Clone après coup : tête `f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0`, arbre propre, empreintes des deux fichiers inchangées.
- Le marqueur `<<HEURE_POUSSEE>>` figure dans une ligne `+` des correctifs : une fois l'heure remplie dans la page, remplacer le marqueur à l'identique dans le correctif, ou le régénérer, pour que les deux concordent.

## 6. Empreintes des sorties

| Sortie | sha256 |
|---|---|
| `/home/user/page-a1v4/v2/README.md` | `b72c983eada4449931ff828d4e841aaf6708bce881657c745a8c113f3392321e` |
| `/home/user/page-a1v4/v2/resultats/attaque-goodhart-v2/README.md` | `c8f92fd18e313e0015147f585bab6686a037cd3ec6926f4e6c2cc54a7777dcca` |
| `/home/user/page-a1v4/v2-sans-related-work/README.md` | `a1b944e62c3d5b49e009fc78ea0d5c5a4533ddb4b8e30fdd2dfd629ba7e8210b` |
| `/home/user/page-a1v4/v2-sans-related-work/resultats/attaque-goodhart-v2/README.md` | `c8f92fd18e313e0015147f585bab6686a037cd3ec6926f4e6c2cc54a7777dcca` |
| `/home/user/page-a1v4/diff-page-a1v4-v2.patch` | `fbfe3b6f4486b98a93e706f983cea8b16ff40163d1df6f44329a98961fa704c6` |
| `/home/user/page-a1v4/diff-page-a1v4-v2-sans-related-work.patch` | `42cfa7acec599d614a12c476ce24cd3a7aad560b6ac6ad1bd1881ad2ed066958` |
| `/home/user/page-a1v4/appliquer-cl-v1.py` | `554c888320d6b20b9117429fc387ca95d8a1a67b1c1537668207be2ba555dcd3` |

L'empreinte de ce journal est donnée dans la réponse à la mère.

## 7. Interdits tenus

Fichiers ouverts : les deux brouillons, la contre-lecture, deux lignes de `registres/decisions.md`, la l. 367 du texte scellé (plus son empreinte), les deux fichiers visés du clone (empreinte, `diff`, copie jetable) et `CLAUDE.md` du dépôt, chargé d'office par la session. Aucun `diag/`, `runs/`, `donnees/bras-attaque*`, `docs/notes/bras-attaque/`, ni rien de l'étiqueteur ; ni `env`, ni `printenv`, ni `set`, ni `export -p`, ni `/proc/*/environ`. Aucune écriture git, aucune poussée, aucun appel externe, aucune dépense. Brouillons et correctif v1 existants non modifiés.

Fin : 10 novembre 2026, 10:35:55 UTC (`date -u`) ; entrées revérifiées à cette heure, empreintes inchangées.
