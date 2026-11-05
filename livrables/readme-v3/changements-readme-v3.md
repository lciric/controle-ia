# README v3 — changements par rapport à la v2

Rédigé le 2026-10-08 (UTC) par une session hors phase, à la demande de Lazar : « corrige les readme si besoin pour mieux coller aux attentes du programme » (le séminaire AFFINE, dont le formulaire propose ce dépôt en lien ; R-112). Proposé en demande de fusion sur la branche `readme-v3` : rien n'arrive sur `main` sans l'accord de Lazar (publication = nœud de décision).

## Changements

| Section | Changement | Source |
|---|---|---|
| Statut | « This repository is private and shared for evaluation only: please do not redistribute it » retiré : le dépôt est public sur GitHub (page servie sans compte, fichiers bruts téléchargeables ; constaté le 2026-10-08 vers 23:00 UTC ; N-016). G0 « 1 November 2026 » remplacé par « December 2026, at the start of the grant period » ; cette date contredit `registres/etat.md` et R-094 : nœud N-017, à trancher avant fusion. Date du statut : 8 octobre. | Proposition jointe à la candidature EA Funds (v2), sections 6 et 7 : « Gate G0 (at the start of the grant, December 2026) » ; `proposal-v2.md`, 74a83212…, hors dépôt |
| In one minute | Renvoi vers la section théorie ; papier B situé dans la version à douze mois du plan, comme dans la feuille de route. | Proposition v2, section 7 |
| About me | Champs [TO COMPLETE] remplis : nom, formation, publications, lien vers P3, contact. Rien sur les candidatures en cours ni sur les finances au-delà de « on my own funds ». | CV de Lazar et textes de candidature qu'il a validés ; DOI 10.1371/journal.pcbi.1011315 vérifié (Cimeša, Ciric, Ostojic ; vol. 19, n° 8) |
| Theory, in brief | Énoncés de L1 à L5 et de T1 à T4 en anglais, avec leurs conditions ; classes M, M±, C, K ; écart C/K selon le signe de la dépendance ; proposition 1 de 2606.10456 (hypothèse impossible pour une loi bénigne continue ; conclusion fausse pour la somme sur la construction du papier) ; magnitudes de T0.3 avec leurs réglages ; réserve R4 reprise. | `docs/notes/note-mathematique-lemme-theoreme-v3.md` (dfe4fe0f…), sections 1 à 7 ; `docs/notes/resultats-T0.3-v1.md` (9ab618ed…), magnitudes 1 à 6 ; `docs/sources/lecture-pdf-niveau1/rapport-2606.10456-v1.md`, section 3 |
| Roadmap | Calendrier de la proposition v2 : sept mois à partir du 1er décembre 2026 ; GC fin du mois 2, G1 fin du mois 4 ; papier C publié au mois 4 ; papier A aux mois 5 et 6 ; diffusion au mois 7 ; papier B dans la version à douze mois. | `proposal-v2.md` (74a83212…, hors dépôt), section 7 |
| Suggested reading path | La proposition publique v1 retirée du parcours : son calendrier (douze mois à partir du 1er novembre) et sa porte G0 au 1er novembre précèdent le plan actuel, et elle porte « please do not redistribute ». Une v2 sans budget, tirée de la proposition v2, rétablirait le lien. Parcours mathématique ajouté (note v3, résultats de T0.3). | `livrables/proposition-publique-v1/proposal-public-v1.md` (140f9816…), en-tête et section 7 |
| Paragraphe sur les textes de tiers | « This private repository … will be removed before any publication » remplacé par un constat exact, sans « private » : PDF de tiers, fichiers de travail des lecteurs qui en contiennent des pages, sorties de l'extraction (`donnees/`). Le fond (retrait ou visibilité) reste ouvert : N-016. | `livrables/depot-expurge-v1/LISEZMOI-v1.md` (517adb3f…), section 2 ; N-014 ; `docs/procedures/T0.5-extraction-v1.md` (« à purger avant toute publication du dépôt ») |
| Pied de page | Version 3 et renvoi vers ce fichier. | — |

Rien d'autre ne change : les autres chiffres et énoncés gardent la traçabilité et la vérification de la v1 (`livrables/readme-v1/`).

## Contrôles

- Chaque nombre de la section théorie figure dans la note v3 ou dans `resultats-T0.3-v1.md` (vérifié par script, deux fois).
- Contre-lecture par un sous-agent neuf, qui n'a rien écrit de cette version : `verification-readme-v3.md` (rapport tel quel, puis suites données).
