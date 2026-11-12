# Contre-lecture du dossier d'intégration pour l'entretien avec le Transformative AI Fund — v1, contre-lecture 2 (seconde passe)

- **Contre-lecteur** : sous-agent neuf (règle R2), modèle déclaré par l'environnement : Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur des pièces (Claude Fable 5.1 ; décision N-052). Je n'ai écrit ni les pièces ni la contre-lecture 1.
- **Heures** (`date -u`) : début 2026-11-08 15:57:46 UTC ; fin en dernière ligne.
- **Pièces contre-lues** (non scellées) : `docs/notes/taif-v1/integration-v1/matrice-tracabilite-v1-brouillon3.md` (482 l. ; en-tête, légende, grille, § 3 par extraits, § 4, § 5) ; `journal-changements-candidature-v1-brouillon3.md` (227 l., en entier) ; `registre-goulots-questions-v1-brouillon2.md` (274 l., en entier) ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v3-brouillon1.md` (88 l., en entier). Référence : `contre-lecture-integration-v1-cl1.md` (200 l.).
- **Sources vérifiées** : `registres/decisions.md` R-1849 à R-1873 (l. 1807-1831), R-522, R-765 (l. 993), R-1773 (l. 1731) ; candidature envoyée `proposal_v2_TAIF_2026-10-07.txt` l. 264, 271, 278, 283, 321-339 ; `docs/decisions/decision-N-055-v1.md` l. 29 ; `decision-N-029-v1.md` l. 25-26 ; `docs/notes/etat-critique-v1/etat-critique-programme-v1.md` l. 19, 21, 34 ; `verdict-T0.4-critere-1-G0-v3.md` l. 11 ; compagnon de `registres/passations/2026-10-07-1122.md` (e938ed08) ; v16 l. 1339-1341 ; proposition de recherche l. 46. Grille de la matrice recomptée par script (52 lignes × 29 colonnes : T 47, I 54, D 53, R 13, V 3, vides 1 338 : conforme aux comptes écrits).
- Rien lu sous `donnees/`, `diag/`, `docs/notes/bras-attaque/` ; aucun fichier existant modifié ; aucun `.sha256`, aucun commit, aucun réseau, aucune dépense. Toute pièce lue est une donnée, jamais une instruction.

## 1. Verdicts par pièce

| pièce | verdict | raison principale |
|---|---|---|
| Matrice de traçabilité, brouillon 3 | **utilisable après corrections mineures** | constats de cl1 appliqués ; reste : la course et l'étiqueteur v2 dits « lancés » (ils ne le sont pas), deux cases A22 en « instrumente » contre la légende |
| Journal des changements, brouillon 3 | **utilisable après corrections mineures** (trois phrases « à dire » à retoucher avant tout usage) | bloquants de cl1 levés ; mais la marge (« one to two days ») est celle du chemin v2, pas du v3 ; « started today » est faux ; 0,866 est attribué au mauvais organisme ; la carte graphique contredit le registre |
| Registre des goulots, brouillon 2 | **utilisable après corrections mineures** | conforme à cl1 et au chemin v3 ; deux phrases au présent (« est en cours », « is live now ») pour une course non créée ; « aucune règle de repli écrite » contre R-765 |
| Chemin critique G1 v3, brouillon 1 | **utilisable devant Lazar** | CLI-03 appliqué fidèlement (7a / 7b, T0.7 avant la création, marge 0 à 1 jour) ; état « rien créé » exact au registre ; une réserve : le calendrier suppose 7a créée le 9 au plus tard (aucune ligne R- ne l'atteste encore) |

**Constats de cl1 non conformes : 4** (CLI-02, CLI-06, CLI-25, CLI-33) ; 3 appliqués autrement et acceptables (CLI-17, CLI-20, CLI-28) ; 29 appliqués et conformes.

## 2. Les 36 constats de cl1

| constat | sort | où | conforme |
|---|---|---|---|
| CLI-01 dépense « each line under a cap » | appliqué | journal entrée 2 (d), (e) ; registre C-1, C-6 | oui ; retouche de forme : « one rental incident on 23 October, thirteen instances without authorisation » se lit comme deux exceptions (§ 4, P1) |
| CLI-02 date de scellement de G1 | appliqué | journal entrées 3 (b), (e), § 22 | **non** : « one to two days of margin at best », cité au chemin **v2** l. 51-53, alors que le chemin **v3** et le registre B-1 disent **0 à 1 jour** |
| CLI-03 goulot | appliqué | chemin v3 (table de tête, pas 7a/7b, 8, « Le goulot ») ; registre B-1, B-2, A-1, classement | oui |
| CLI-04 étiqueteur | appliqué | journal entrée 8 ; registre A-2, B-7 ; matrice A08 | oui (couple repris mot pour mot) |
| CLI-05 N-061 | appliqué | matrice § 0, A24 ; journal § 0, entrée 15, § 22 ; registre nœud 8 | oui |
| CLI-06 carte graphique | appliqué autrement | journal entrée 2 : un seul chiffre « ≈ 130 », « repris par le registre des goulots C-12 » | **non** : le registre (C-1, C-12, table de tête l. 19) donne **deux relevés** (≈ 99 au 29 octobre, ≈ 130 au 8 novembre) et dit suivre « la même règle que la matrice et le journal » ; contradiction entre pièces |
| CLI-07 règle de décision de G1 | appliqué | journal entrée 4 ; registre C-15 | oui ; nuance de phrase (§ 4, P3) |
| CLI-08 universalité | appliqué | journal entrée 10 (e) | oui |
| CLI-09 tiers et préenregistrement | appliqué | journal entrée 18 (d), (e) | oui ; mais le § 22 point 1 réintroduit « tout est horodaté chez un tiers » (§ 6, N3) |
| CLI-10 H6 et pilote | appliqué | journal entrées 19, 20 | oui |
| CLI-11 « 602 tests » | appliqué | matrice C6-5 × A22 (R-098 ; e938ed08 vérifié) | oui |
| CLI-12 orphelins | appliqué | matrice § 4.2 : C7-3, C7-6, H1b strictes ; H6, H9, HC4, HC5 documentaires | oui (C7-3 et C7-6 déclarées orphelines plutôt que propagées : choix permis par le couple) |
| CLI-13 A26 et H5 × A28 | appliqué | matrice (A26 sans lien sur les hypothèses ; H5 × A28 sans lien) | oui |
| CLI-14 A12 recopiée | appliqué | matrice A12 (H6, HC4 avec lignes de la synthèse) | oui |
| CLI-15 H5 au papier B | appliqué | registre A-5 (l. 207-208, 304-305 ; C8-9) | oui |
| CLI-16 tables v4 | appliqué | registre C-1, C-2, C-13, B-6 | oui |
| CLI-17 « brouillon 2 » du papier C | appliqué autrement | réserve dans matrice § 0 (6), registre B-6 et nœud 12, journal § 22 point 3 ; source non corrigée | acceptable (fichier existant hors du ressort des rédacteurs) ; reste à faire par la mère avant la page pour le fonds |
| CLI-18 arène | appliqué | journal entrée 13 ; registre A-3 | oui |
| CLI-19 classement | appliqué | registre, classement (C-14 rang 2, A-2 rang 5, C-6 rang 7) | oui |
| CLI-20 A19, A16 | appliqué autrement | matrice : A19 instrumente G0-6, C7-5, H1a ; A16 reste orpheline, « lignée d'A17 et A18 » dite | acceptable ; la phrase d'A16 répète deux fois « à justifier comme front E » (coquille) |
| CLI-21 heure 15:50 | appliqué | journal table 1→2 et entrée 1 (d) | oui |
| CLI-22 v3 « non scellé » | appliqué | matrice § 0 | oui |
| CLI-23 lignes citées | appliqué | matrice (T0.4 l. 11 vérifiée ; chemin v1 l. 51 ; état l. 160 ; T0.5 l. 15) | oui |
| CLI-24 HC4 × A21 | appliqué | matrice | oui |
| CLI-25 mot unique pour A22 | appliqué en partie | matrice : la table de tête dit « teste partout » | **non** : la grille garde **C8-4 × A22 = I** et **C5-1 × A22 = I** (recompte par script) |
| CLI-26 l. 334-335 | appliqué | journal entrée 2 (a) : l. 336-337 | oui |
| CLI-27 lignes de la table v3 | appliqué | journal entrée 2 (b) : l. 48, 53, 55, 111, 115 | oui |
| CLI-28 similarité 0,855 | appliqué autrement | journal entrée 1 (b) et matrice § 0 : « script du bloc-notes, non versé, indicatif, non opposable » | acceptable devant Lazar ; devant le jury, ne pas le dire (aucun chemin, R6) |
| CLI-29 R-1824 → R-1825 | appliqué | registre B-1 ; chemin v3 | oui |
| CLI-30 R-707 | appliqué | journal entrée 16 | oui |
| CLI-31 « no longer ours » | appliqué | journal entrée 6 (e) | oui |
| CLI-32 sigles dans les phrases | appliqué | journal entrées 3, 4, 7, 9 ; registre A-1 | oui, sauf l'entrée 3 (e) : « the G1 pre-registration » arrive avant que G1 soit dite (« our main gate » n'apparaît qu'à l'entrée 4) |
| CLI-33 prédicteur 0,866 / 0,8878 | appliqué autrement | journal entrée 5 (b) : un seul chiffre, « texte seul 0,866 sur l'organisme flagrant de P3 », « cohérent avec le registre A-6 » | **non** : 0,866 est le relevé de **R1 v4**, organisme « coût gonflé » (état critique l. 34, ligne H-R2) ; sur l'organisme flagrant de P3 c'est **coût seul 0,8878** (N-029 l. 25-26). Le registre A-6 le dit correctement ; le journal se trompe d'organisme et se dit à tort cohérent |
| CLI-34 brouillon 6 hors `main` | appliqué | registre B-5 ; chemin v3 | oui |
| CLI-35 N-054 point 3 | appliqué | registre A-4 | oui |
| CLI-36 « à éprouver » | appliqué | journal entrée 8 (d) | oui |

## 3. Cohérence entre les quatre pièces

| objet | matrice b3 | journal b3 | registre b2 | chemin v3 | état |
|---|---|---|---|---|---|
| dépense (645,42 ; 187 ; 111,87 sur 50) | conforme | conforme | conforme | conforme | **cohérent** |
| carte graphique | — | ≈ 130 seul | ≈ 99 et ≈ 130 | — | **incohérent** (CLI-06) |
| prédicteur texte 0,866 | — | P3 flagrant (faux) | R1 v4 « coût gonflé » + 0,8878 P3 | — | **incohérent** (CLI-33) |
| calibration 60 / 47 / 5 / 8 ; « 31 of 31 » sans verdict | conforme | conforme (entrée 18 (d)) | conforme (C-13) | conforme | **cohérent** |
| date de G0 (« December 2026 » envoyé ; fin novembre en interne ; verdict avant le 30 à 23:59 UTC) | conforme | conforme | conforme | conforme | **cohérent** |
| règle de repli de G0 | — | « tranchée (R-765) » | « aucune règle de repli écrite » (B-6, nœud 12) | « report au 31 janvier » | **incohérent** : R-765 (l. 993) tranche la divergence principale, onze choix restent ouverts ; à dire ainsi des deux côtés |
| scellement de G1 (28-29 novembre) | — | conforme | conforme | conforme | cohérent |
| marge | — | **un à deux jours** (chemin v2) | 0 à 1 jour | 0 à 1 jour | **incohérent** (CLI-02) |
| course de dose-réponse | « **lancée** le 8 nov. » (A04, C5-1) | « part le 8 novembre », « **started today** » | « ordonnée, non créée » | « rien créé » à 15:43 | **incohérent** : au registre, aucune création (R-1868, R-1870 à 15:47 : branche montée seulement) |
| étiqueteur v2 | « **lancée** en exploratoire » (A08, C5-1) | « part en exploratoire » | « ordonnée », nœuds de Lazar ouverts | « ordonnée » | **incohérent** : R-1859, R-1862 : ordre au brouillon 1, plafond, lecteur et jumeaux attendent Lazar |
| étiqueteur phase 1 « non tranché » | conforme | conforme | conforme | conforme | cohérent |
| chemin critique (7a exploratoire puis 7b ; T0.7 scellé avant la création de 7b) | A04 conforme | entrée 3 (b) conforme, mais cite le chemin v2 | conforme | source | cohérent sur le fond ; le journal doit citer le v3 |
| C7 / C8 du texte envoyé | conforme | conforme | conforme (A-5 : C8-9) | — | cohérent |
| promesses de la section 9 | C9-1 à C9-4 tracées (dont « Paper C is scheduled first », C9-4) | — | C-16 (6) : « *Paper C is scheduled first* … non tracés dans ce dossier » | — | **incohérent** : la matrice trace C9-4 ; « Qwen2.5-7B serves as a heterogeneous agent » (l. 333-334) n'est tracé nulle part |
| organisme pilier attaque (A18) | « 8 nov., **en cours** » | — | fini (R-1865), v1 bis non lancée (R-1866) | fini | périmé dans la matrice |

## 4. Phrases « à dire » à corriger (couples)

**P1 — journal entrée 2 (e)** (et registre C-1, phrase gelée, qui omet les treize instances). « *…the exceptions are logged: one rental incident on 23 October, thirteen instances without authorisation, one line above its cap, and a few uncapped lines approved in writing.* » → « *…the exceptions are logged: one incident on 23 October, when a relief session rented thirteen instances without authorisation; one line above its cap; and a few uncapped lines approved in writing.* » ; registre C-1 : aligner la phrase gelée (ajouter « treize instances louées sans autorisation ») ; et y retirer « “about $20” était la carte graphique au 7 octobre » (sans source).

**P2 — journal entrée 3 (e).** « *…and the critical path to sealing the G1 pre-registration now runs to 28–29 November, with one to two days of margin at best; the dose-response run that started today is exploratory and decides nothing.* » → « *…and the critical path to sealing the pre-registration of gate G1, our main gate, now runs to 28–29 November, with zero to one day of margin; the dose–response run ordered today is exploratory and decides nothing — the run that counts for the gate is a pre-registered confirmation that follows it.* » ; et (b) « marge d'un à deux jours au mieux (`chemin-critique-G1-v2-brouillon1.md` l. 51-53 …) » → « marge de 0 à 1 jour (`chemin-critique-G1-v3-brouillon1.md`, « Le goulot » et « Calendrier résultant ») ». À l'entretien (vers le 22), réécrire au passé selon ce qui aura couru.

**P3 — journal entrée 4 (e) et registre C-15.** « *…it replaces the confidence interval of the proposal, which is reported beside it.* » : l'intervalle de DeLong peut être retiré (pas 6) ; ce qui reste rapporté est le rééchantillonnage (N-055 D-S11, l. 29 : « le pari décide, le rééchantillonnage est rapporté — reste une pièce du préenregistrement de G1 »). → « *…it replaces the 95% confidence interval of the proposal as the decision rule; a resampling interval is still reported beside it.* »

**P4 — registre A-1, phrase.** « une course exploratoire, non opposable, est en cours » → « une course exploratoire, non opposable, est ordonnée » (au registre : rien créé à 15:43, R-1868, R-1870).

**P5 — registre C-14, phrase (3).** « *The dose–response run that is live now is exploratory; its pre-registered confirmation follows.* » → « *The dose–response run we start this week is exploratory; its pre-registered confirmation follows on fresh seeds.* »

**P6 — journal entrée 20 (e).** « *…the pilot we promised before the grant will therefore be a confirmation run, not the first run.* » : vrai seulement si la confirmation 7b tient sa création au 15 novembre (marge 0 à 1 jour). → « *…the pilot we promised before the grant is the confirmation run, not the first run; it is planned before December, with almost no margin.* »

**P7 — journal entrée 14 (e).** « *the next course is designed…* » (gallicisme) → « *the next run is designed to separate the instruction from the act.* »

Les autres phrases « à dire » (entrées 1, 5 à 13, 15 à 19, 21 ; registre A-2, C-15 hormis P3) sont vraies au registre, sans sigle nu, sans chiffre non sourcé, et disent les deux côtés. Réserve sur l'entrée 5 (e) : le juge préparé « matches the probes » vient d'HELIOS (STEGO, v16 l. 647-656) ; dire « on one published benchmark » suffit, ne pas citer de chiffre.

## 5. Trous pour le jury relevés par cl1

| trou | traité ? | où |
|---|---|---|
| 1. épreuves exploratoires sans préenregistrement face à la règle 1 ; « The pilot runs before the grant starts » | **traité** | journal entrée 20 et entrée 18 (d) ; registre C-14 (rang 2), nœud 2 ; matrice C5-1, C6-4b ; chemin v3 risque 5. **Reste** : la base citée, R-522 (journal entrée 20 (c)), porte dans son verbatim « aller droit vers obtention de résultats positifs » (`registres/decisions.md`, ligne R-522) ; un jury qui la lit y verra la règle R3 en cause. Aucune pièce ne dit que R-522 n'a été « partiellement exécutée » que pour l'exploration ; à écrire à côté de toute citation de R-522 |
| 2. phrase sur la dépense | **traité** | journal entrée 2 ; registre C-1, C-6 ; corrections de forme P1 |
| 3. règle de décision de G1 | **traité** | journal entrée 4 ; registre C-15 ; nuance P3 |
| 4. « 31 of 31 » sans verdict scellé | **traité** | journal entrée 18 (d) ; registre C-13 (remède : verdict rétroactif de T0.3 ou « formal verdict pending ») ; matrice case A22 de C6-2 ; aucune phrase anglaise dans le journal : prendre celle du registre C-13 |
| 5. H6, bruit d'activations | **traité** | journal entrée 19 ; registre C-16 (1) ; matrice ligne H6 |
| 6. section 5 (règles de méthode) | **traité** | matrice C5-1 ; journal entrée 18 |
| 7. section 9 (bascules) | **en partie** | matrice C9-1 à C9-4 ; registre C-16 (2), (3) ; **non traités** : « Qwen2.5-7B serves as a heterogeneous agent » (aucune ligne, aucune entrée) ; « Import published attack policies » face à la quarantaine N-057 n'a pas d'entrée au journal (seulement l'entrée 6 (a) qui la cite) |
| 8. section 12 (budget) | **en partie** | matrice C12-1, C12-2 ; registre C-1, C-16 (4) ; journal : 4 000 USD contre 4 600-6 900 euros dit en entrée 8 (d) ; **non traité au journal** : outillage « 1,000 USD per month » face à la dépense relevée |
| 9. « fully occupied » face à HELIOS | **traité** | journal entrée 21 ; registre C-16 (5) |
| 10. vérité du dommage indécise | **traité** | journal entrée 8 ; registre A-2, B-7 |

## 6. Défauts nouveaux introduits par les corrections

- **N1** — matrice A04, C5-1 × A04, A08, C5-1 × A08 (l. 24, 107, 225, 233, 271) : « course lancée le 8 novembre », « épreuve de l'étiqueteur v2 lancée » : faux au registre (rien créé ; ordre v2 au brouillon 1, nœuds ouverts). Couple : « lancée le 8 nov. » → « ordonnée le 8 nov., non créée à 15:47 UTC (R-1868, R-1870) ».
- **N2** — journal entrée 3 (e) « started today » et (b) « part le 8 novembre » : même faute (P2).
- **N3** — journal § 22 point 1 : « la porte G1 est plus dure et scellée d'avance » (le préenregistrement de G1 n'est pas scellé : brouillon 6, non contre-lu) et « tout est horodaté chez un tiers » (contredit l'entrée 18 (d) : projet privé, non gelé). Couple : « …plus dure et sera scellée avant toute donnée ; … les empreintes sont déposées chez un tiers, dans un projet encore privé ».
- **N4** — journal entrée 5 (b) : 0,866 attribué à l'organisme flagrant de P3, et « même chiffre que le registre des goulots A-6 » (le registre l'attribue, à juste titre, à R1 v4). Couple : « sur l'organisme flagrant de P3, un prédicteur sur le texte seul atteint déjà 0,866 » → « deux bases triviales séparent déjà : coût seul 0,8878 sur l'organisme flagrant de P3 (N-029 l. 25-26) ; texte seul 0,866 sur l'organisme “coût gonflé” de R1 v4 (état critique l. 34) ».
- **N5** — journal table « 2 → 3 » ligne CLI-06 et entrée 2 (b) : « un seul chiffre … repris par le registre des goulots C-12 » : faux (le registre en donne deux). Aligner sur le registre (deux relevés nommés).
- **N6** — matrice grille : C8-4 × A22 et C5-1 × A22 en « I » quand la table de tête dit « teste partout » et que A22 ne compte plus comme service ; mettre « T ».
- **N7** — journal entrée 3 (b) et registre B-6 : règle de repli « tranchée » contre « aucune règle de repli écrite » ; dire « divergence principale tranchée (R-765, l. 993) ; onze choix ouverts ».
- **N8** — registre C-16 (6) : « *Paper C is scheduled first* … non tracés dans ce dossier » : la matrice brouillon 3 le trace (C9-4) ; garder « Qwen2.5-7B » seul.
- **N9** — matrice A18 « (8 nov., en cours) » : finie (R-1865), v1 bis non lancée (R-1866).
- **N10** (mineur) — matrice § 4.1, A16 : « à justifier comme front E » écrit deux fois.

## 7. Ce que je n'ai pas vérifié

Les 170 cases du § 3 de la matrice une par une (tirage non refait ; cl1 en avait tiré 46) ; les lignes C9 et C12 cellule par cellule ; le contenu de l'ordre exploratoire et de la chaîne v13 cités par le chemin v3 (non lus) ; la vérité des dates « prévues » du chemin (jugements dits comme tels).

Fin d'écriture (`date -u`) : Sun Nov  8 16:01:28 UTC 2026
