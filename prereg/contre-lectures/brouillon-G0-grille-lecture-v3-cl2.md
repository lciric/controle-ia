# Contre-lecture R2 n° 2 — `prereg/brouillon-G0-grille-lecture-v3.md` — v1

- Contre-lecteur : sous-agent neuf (Fable 5.1), d'un autre modèle que l'auteur de la v3. Je n'ai écrit ni la v1, ni la v2, ni la v3, ni CL1, ni l'un des avis, ni la synthèse du collisionneur, ni aucune preuve lue par la grille. Début 2026-10-29 11:26 UTC (`date -u`), fin : dernière ligne. Commit `cea6d5de`. Ni réseau, ni commit ; aucun fichier interdit ouvert.
- Objet : v3, `15e7f229443d80f7625f1f0e16838457125f04dd1c185e1b2caac7442b70e328` (recalculée). Lus : v2 `aa47f6fc…`, CL1 `b2282047…`, synthèse repli `527f5853…` (§ 4-6), avis Fable repli l. 44-56, avis Fable grille l. 19-24 et 54, P-015 l. 61 et 68, brief v2 l. 190-201 (identiques à la recopie l. 105-116), `registres/decisions.md` l. 34, 978, 993, 994. Toutes les commandes sous `LC_ALL=C.UTF-8` (`locale -a` : 1).

## Verdict

**Scellable après corrections.** Aucun bloquant ; trois majeurs (CLG2-01 à 03 : portée de D-G0-13 (a) aux critères sans run, D-G0-13 (b) hors de R-765, incohérence M-3.2 / M-3.5), quatre mineurs. Les quinze constats de CL1 sont appliqués dans le corps ; les comptes de l'annexe F sont confirmés ; les huit critères restent mot pour mot ; aucune latitude ne peut rendre « tenu ».

## 1. Traitement des constats de CL1

Les quinze lignes vérifiées sur le texte de la v3 (pas huit : toutes). CLG-01 → l. 208-209, 259, 261-295 ; CLG-02 → l. 182-188, 747-749, 762-764 ; CLG-03 → l. 346, 352-353, 400 ; CLG-04 → l. 311, 317 ; CLG-05 → l. 137-138, 549, 578, 580, 592 (M-8.3, F-8.2, F-8.3 gardés « négatif ») ; CLG-06 → l. 139, 622-630 ; CLG-07 → l. 247-248, 254, 256 ; CLG-08 → l. 437, 443-460, 496 ; CLG-09 → l. 497 ; CLG-10 → l. 354, 397, 401, 581 ; CLG-11 → l. 549 ; CLG-12 → l. 150-152 ; CLG-13 → l. 498 (R-025 l. 34 : texte exact) ; CLG-14 → l. 590, 809-817 ; CLG-15 → l. 164, 613-615. La table de tête (l. 45-68) dit vrai pour chaque ligne ; les deux écarts de forme (préfixes élargis, classe `[èe]` remplacée) sont dits l. 694-696 et fondés (§ 2).

## 2. Exécutions

- **M-0.8 (a)** : **23 pièces**, liste identique à l'annexe F ; **(b)** : **14 runs** sur 43 manifestes (T0.3 : 1 ; T0.4 : 4 ; T0.5 : 5 ; P3 : 4). Confirmé.
- **CLG-03** : `CRIT_2` sur P3 : l. 17, 57, 122, **431** ; T0.5 pilote : l. 152, 174, 183 ; 0 sur T0.4 v3 et T0.3 ; synthétique : « critère 20 », « critères 12 et 13 », « critères 1 à 3 » non pris ; « critères 1, 2 et 3 », « Critères 2 et 3 de G0 » pris. `crit[èe]res? 2` : 0 en POSIX, 4 en `C.UTF-8`. Confirmé.
- **CLG-04** : `PRONONCE_1` sur les verdicts T0.4 : v1 l. 3 → « non concluant » ; v2 l. 10 → « non prouvé » ; v3 l. 11 → « prouvé » ; un mot chacun ; le second `grep -o` rend bien « non prouvé » (pas « prouvé »). **Trois mots, confirmé.** Limite : « Critère 1 de G0 : « non prouvé » » (guillemets) rend 0 (CLG2-04).
- **CLG-07** : `NEUTRE` dans `head -5` : **8 sur 8** à 1 ; cinq témoins à 0 ; P3 v2 l. 608 : 0 avec le motif resserré, 1 avec « auteur ni » nu. Confirmé. Hors annexe : verdicts T0.4 v1, T0.5 notations, P3 v1 et v2 à 0 ; audits R4 T0.5 à 1.
- **M-0.2 sur la v3** : `GardeArret` « contre-lecture 2 sans ses deux empreintes », seul manque : la protection voulue l. 698 fonctionne. Échappement : `grep -c -E "x\|b"` rend 0 (l. 882 confirmée).

## 3. D-G0-13

R-765 (verbatim l. 993) pose trois choses : un échec scellé **pendant le report** gèle le critère jusqu'au second verdict ; il ne ferme pas la porte ; un critère réfuté **par sa liste d'arrêt** n'est jamais retenté. Lazar a répondu au choix 1 de la synthèse (§ 5), dont la clause (a) ne parle que du « non tenu — négatif (liste d'arrêt scellée déclenchée) », variante B : « statut reporté tel quel ».

- **(a)** est fidèle à la lettre (« échec scellé » = résultat, jamais un manque, CLG-05) et va au-delà de la clause de la synthèse en gelant aussi un négatif par ligne de table. Compatible avec « jamais retenté » : jusqu'au verdict final, gel et non-retente coïncident. Deux défauts de portée. (1) Elle s'étend aux critères **sans run** (6, 7, 8 ; champ (β) « sans objet »), où le « négatif » sort des contrôles de la grille (M-8.3, F-8.2, F-8.3) et non d'une lecture gelée d'une preuve ; or F-8.2 compte des lignes sur un chiffre nu : exécutée sur le programme et le brief, « 0,5 » rend 3 lignes, « 12 » en rend 8, « 8B » 11, toutes sans « l'article imprime ». Un faux négatif du critère 8 scellé pendant le report serait gelé et irréversible ; un chiffre mal statué se corrige en une ligne, il n'est pas une réfutation. La table de dépendance de la synthèse donne « — » pour 1, 5 et 8. (2) Elle contredit D-G0-7 pendant le report sans le dire dans D-G0-7 lui-même (seule la section 2, l. 235-239, tranche). **Correction** : gel limité aux critères dont (α) est « présent » (préenregistrement à liste d'arrêt), négatif venant de la liste d'arrêt ou de la table gelée de **cette preuve** ; les négatifs de M-8.3, F-8.2, F-8.3 restent des négatifs du critère 8 mais ne gèlent pas ; F-8.2 remplacée par la vérification du script M-8.3 sur le chiffre **tel que la table l'écrit** (unité, contexte), doute → non concluant.
- **(b)** n'est pas dans R-765 (« pendant le report ») ni dans la synthèse hors liste d'arrêt. Elle durcit D-G0-7 et contredit le précédent que la grille cite elle-même (T0.4 : v1 non concluant, v2 non prouvé, v3 prouvé, versions autorisées par N-010 et N-011 sur cause nommée) : une telle suite, coupée par la première lecture, finirait gelée sur « non prouvé » malgré un défaut d'instrument avéré. **Recommandation : l'option alternative** (règle de D-G0-7 : seul le négatif par liste d'arrêt est gelé à la première lecture ; un négatif par ligne de table admet une version suivante autorisée **avant son run** sur cause distincte du résultat, sinon non concluant). R3 et R4 sont tenus par D-G0-7 lui-même (pas de cause nommée = pas de rattrapage). Confiance moyenne-haute.
- **(c)** cohérent avec (a) ; la commande `merge-base` est juste. Manque : la liste fermée de M-0.8 n'a pas de motif pour la pièce postérieure au gel (CLG2-05).

Recommandation d'ensemble : défaut = (a) restreint aux critères à (α) présent, (b) alternative, (c) tel quel.

## 4. D-G0-11 (P4-instrument)

Fable (grille, l. 19-23) : condition ; CL1 § 6 : réserve. Les deux ont raison sur un point : le critère ne nomme pas le témoin ; P-015 (b) l. 68 est une décision de Lazar en vigueur qui fixe un **ordre** (« le verdict de P4-instrument précède toute lecture de sonde »). Constat décisif : la grille traite déjà cet ordre comme une **condition** en M-3.2 (T0.7 scellé avant les épisodes, « non tenu — invalide », source P-015 (b)) et comme une **réserve** en M-3.5 : même source, deux états (CLG2-03). La Métrique définit « invalide » comme un défaut de procédure, ce qu'est un ordre rompu. **Recommandation : condition** (non tenu — invalide si absent ou postérieur), confiance moyenne ; motifs : cohérence avec M-3.2 ; N-027 gèle les critères, pas les décisions de route, et P-015 (b) s'impose déjà aux auteurs de T0.7 ; symétrie : sans témoin positif, un « aucune sonde au-dessus » ne se distingue pas d'une panne d'instrument, et sous D-G0-13 un tel négatif serait gelé alors qu'« invalide » ne gèle pas. Coût : nul par rapport à la route décidée. Si Lazar préfère « réserve », M-3.2 doit passer en réserve aussi, ou la grille dire pourquoi l'un et pas l'autre.

## 5. Latitudes et R4

Aucune latitude ne rend « tenu » : tout cas imprévu tombe en « non concluant » (l. 139), même suite que « non franchie ». Restent des choix du lecteur entre sous-états, qui comptent pour le gel : F-3.4 (`entrainement.txt`, `lus.txt` : qui les produit, depuis quels fichiers ?) ; F-7.2 (« immunité absolue » « niée » : interprétation) ; contrôle de D-G0-2 (quatre conditions « trouvées » sans motif) ; M-3.3 (« aucune moyenne dans le bras principal » sans commande) ; M-4.4 (« module identique ») ; F-3.1 (ligne attendue sans motif). R4 : tenue (l. 622-630, les deux sens, sept jours sans audit par le lecteur) ; l'asymétrie restante (le négatif gèle, le « tenu » est relu) vient de R-765, sauf (b), qui l'étend sans mot de Lazar. Une porte « on verra » n'existe pas : les deux lectures sont datées, finales, même grille.

## Constats

| n° | gravité | ligne v3 | constat | correction |
|---|---|---|---|---|
| CLG2-01 | majeur | 765, 137, 581 | D-G0-13 (a) gèle des négatifs issus des contrôles de la grille sur des critères sans run ; F-8.2 sur chiffre nu produit des faux négatifs (démontré) | gel seulement si (α) présent ; F-8.2 → script M-8.3 sur le chiffre tel qu'écrit dans la table ; doute → non concluant |
| CLG2-02 | majeur | 765 (b) | (b) hors de R-765 ; contredit D-G0-7 et le précédent T0.4 | défaut = option alternative |
| CLG2-03 | majeur | 395, 398 | P-015 (b) : condition en M-3.2, réserve en M-3.5 | un seul état ; recommandé : condition |
| CLG2-04 | mineur | 311, 792 | `PRONONCE_1` ne prend pas un prononcé entre guillemets → « absent » au lieu de « négatif » ; un verdict qui cite le prononcé d'une version antérieure rend « plusieurs mots » | `\**` → `[*«" ]*` ; annexe C point 6 : le prononcé figure une seule fois dans le verdict |
| CLG2-05 | mineur | 290-295 | aucun motif d'écart pour une pièce postérieure à un gel (D-G0-13 (c)) | (m4) « postérieure au gel de D-G0-13, chemin du verdict de la première lecture » |
| CLG2-06 | mineur | 402, 550, 368, 396, 438, 399 | jugements résiduels (§ 5) | un motif par contrôle, ou « non concluant si le motif échoue » écrit |
| CLG2-07 | mineur | 266 | `find … -maxdepth 1` ignore `prereg/contre-lectures/` : une contre-lecture « non scellable » non citée par le préenregistrement n'est pas inventoriée | ajouter `prereg/contre-lectures` au `find`, motif (m2) par nom de base |

Non vérifié : annexe F au-delà des quatre comptes demandés ; P3 l. 272-275 et 228-230 ; avis conv-audit ; clause `62cc6fbf…`.

Fin de rédaction : voir la ligne suivante (`date -u`).
Fin de rédaction : 2026-10-29 11:32:04 UTC.
