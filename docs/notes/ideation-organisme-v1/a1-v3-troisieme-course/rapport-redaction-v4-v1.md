# Rapport de rédaction v4, v1 — texte v4 (brouillon 1), lanceur durable v4, ordre de course v2 (A1-v3, troisième course)

Rédacteur-développeur des couples des brouillons 2 et 3 de la v3 et des lanceurs durables v2 et v3. 5 novembre 2026, de 10:06 à
10:29 UTC (heures relevées par `date -u`). Demande de la mère (10:06 UTC) après les deux contre-lectures complètes, lues en
premier : texte (`contre-lecture-complete-v1/contre-lecture-complete-texte-v3-v1.md`, `06d6283d…`, « lançable après couples,
version v4 » ; 15 couples `couples-contre-lecture-complete-texte-v3-v1.json`, `16803c05…`) et lanceur
(`contre-lecture-complete-lanceur-v3-v1.md`, `ed4dc27e…`, aucun bloquant de code, 8 corrections proposées). Mêmes interdits : aucun
commit, aucune poussée, aucun `.sha256` livré, aucun réseau, aucune location, aucune clé lue ; tout sous `timeout 900 nice -n 10`.
Travail en cours dans le bloc-notes (miroir `…/scratchpad/lv2-a1v3/miroir/`, dossier `…/final-v4/`) ; seuls les fichiers finis sont
copiés au dépôt, sans rien écraser.

**Verdict.** Le texte v4 (brouillon 1) = la v3 scellée + les 15 couples du contre-lecteur (empreinte intermédiaire `9851ed9f…`,
**égale** à celle du contre-lecteur) + 18 couples du rédacteur (tête de la v4, section 0.8, noms et marqueur du lanceur v4, texte
`…-v4.md`, corrections décrites). Le motif `<<[A-Z0-9_]+>>` n'y trouve plus que `<<COMMIT_LANCEUR_DURABLE>>`, deux fois. Rempli
par un hash factice et renommé `…-v3-v4.md` dans un extrait jetable de `08ad8f35`, le texte est **accepté** par
`lire_preenregistrement` du lanceur gelé (GO-2026-11-04-06, 400 USD, 259 200 s, « aucun ») ; marqueur laissé, il est refusé. Le
lanceur durable v4 = la v3 + le nom du texte v4 + les corrections 1 à 8 : **354 essais passés (v1 49, v2 82, v3 96, v4 127), aucun sauté, en 391 s**. L'ordre de course v2 est écrit pour la
session pilote. La commande d'Argon gelée (`221df610…`) n'est dans aucune référence locale : sa lecture devient le préalable 3 de
l'ordre.

## 1. Fichiers et empreintes

| fichier (dépôt privé) | sha256 |
|---|---|
| `src/controle_ia/hote_durable_a1_v3_v4.py` | `8101d33bdc259860290feb9a35fb3a93d50df06c84a4268a105f86a973ceef3f` |
| `scripts/amorce_hote_durable_a1_v3_v4.sh` | `a2cecc7ee8318155c16bc91427cf2f7c2a73a227f3628f9dd35ddd9bb06ffb3c` |
| `tests/test_hote_durable_a1_v3_v4.py` | `65b8cf6e4dca506d995e40558bfb5e5e61962830ab8bcb5bdac3d3f46f5e9349` |
| `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/preenregistrement-attaque-goodhart-v3-v4-brouillon1.md` | `e0c90f39a675c7eeacdefa43301474ea71c3d6a42250a56a62ba3cd1713b2f34` |
| `…/a1-v3-troisieme-course/couples-texte-v4-v1.json` | `f76885c558e6643f3bb74ee4f2a1b3354cb581a3fc852dbc1f80c5f19b1a1aaf` |
| `…/a1-v3-troisieme-course/appliquer-couples-texte-v4-v1.py` | `0918a4a3a7af405a35dadce28b2a03154c97909f0c7d8a5eeafcf33db6510f8a` |
| `…/a1-v3-troisieme-course/sortie-appliquer-couples-texte-v4-v1.txt` | `1553aa139126955b87ded753a067936072f7f5e9305af7dd6ccab59cf521b0c2` |
| `…/a1-v3-troisieme-course/ecrire_couples_texte_v4.py` (écrit le JSON des couples) | `e3e4c18ace6c1f95b7b4c6939093a81d109b6887d9ebacdb73aad5a0485770e5` |
| `…/a1-v3-troisieme-course/diff-lanceur-v3-vers-v4-hors-renommage.txt` | `3f47c28540615544ba6a7d54c0fd6dc3d84fcf7e114fa6f81febb6dfc7dcadfd` |
| `…/a1-v3-troisieme-course/epreuve-texte-v4-lanceur-gele-v1.py` et sa sortie `…-sortie.txt` | `d9abd6e0e39b920da392f44bf6c32730cb72501876a6c82b9d0b97c7982d2197` / `f2f22867bce9f0b21dac61f8230d2e9463eb0a6ce1f41fb2367e64b110a59463` |
| `docs/procedures/ordre-fille-a1-v3-troisieme-course-v2.md` | `db8b07353be41615462159eb13f57b119bea9c908476f95ce8dac9d72b128214` |
| bloc-notes `…/scratchpad/lv2-a1v3/sorties/essais-lanceur-v1-v2-v3-v4.txt` | `eb3dbc89869e8ebb73323bbd37b7868321619988d5c0468a003f011a34570542` |

Sources vérifiées : v3 scellée `c697d0df…` (compagnon égal, `/home/user/ideation-organism`, `08ad8f35`) ; audit A9 de la seconde
`a0577b8b…` ; ordre v1 `97f712a7…` ; lanceur v3 du dépôt égal au miroir (`cmp`).

## 2. Texte v4

- Script `appliquer-couples-texte-v4-v1.py` (sortie à côté) : empreintes de la v3 scellée et des 15 couples vérifiées ; les 15 couples
  dans leur ordre, puis les 18 du rédacteur ; chaque « ancien » unique au moment de son application ; la citation du périmètre de
  GO-2026-11-04-06 identique ; toute ligne changée porte un couple ; il ne reste que deux `<<COMMIT_LANCEUR_DURABLE>>` au motif du
  lanceur (chiffres compris) ; 2 153 → 2 236 lignes.
- Le marqueur A9 est rempli par le couple 1 du contre-lecteur : chemin, commits `c0243d37`/`cbaf76a9`, empreinte `a0577b8b…`,
  conclusion, cinq points, et la réserve demandée : dépense « établie sur le journal du relais seulement … **non appariée** au
  registre de dépense de la sortie ».
- Couples du rédacteur (section 0.8, points 1, 2 et 18 à 28) : titre « version 4 » ; paragraphe de tête de la v4 (raison B1 ; **aucune
  course sous la v3, aucune relance de la v3**, la course reste la troisième ; GO inchangés et mot de Lazar de R-1553 sur la lettre
  « texte v3 » du périmètre, **à confirmer** ; publication de la v4 = nœud ; lanceur v4 ; statut ; nom `…-v4.md` ; scellement ;
  graine) ; « Aucune relance » + la v3 (0.5 bis) ; lanceur durable v4 (0.5 bis, section 8, 13 point 7 quater) ; graine de ce texte ;
  commande exacte `…-v4.md` et « texte scellé v4 » ; marqueur `<<COMMIT_LANCEUR_DURABLE>>` remis à la place de `bb35e87f…` (section 8,
  13 point 7 quater) ; corrections 2, 5 et 7 décrites dans la liste d'arrêt (section 8) ; `controler` qui rend 6 (7 quater) ;
  contre-lecture courte des ajouts, à faire (section 14) ; annexe B, version 4 ; section 0.8 (28 lignes).
- Épreuve du lanceur gelé (`epreuve-texte-v4-lanceur-gele-v1.py`, extrait jetable de `08ad8f35` dans le bloc-notes, compagnon simulé
  puis retiré) : marqueur rempli par un hash factice → **accepté** (73 empreintes du code, plan gelé : GO-2026-11-04-06, 400 USD,
  259 200 s, « aucun », Argon un fil, devis maximal 190,46 USD) ; marqueur laissé → « marqueur(s) non rempli(s) :
  ['<<COMMIT_LANCEUR_DURABLE>>'] ».
- Non repris (notes 5 à 9 du contre-lecteur, à sa discrétion) : offre écrite deux fois en section 8, « 80 h de vie » contre ≈ 81 h 25,
  « la fille n'a plus de rôle » (0.5 bis), renvois du point 23 de 0.7, convention de la section 4 : laissés, faute de temps ; à juger
  par la contre-lecture courte.

## 3. Lanceur durable v4 (différentiel hors renommage : `diff-lanceur-v3-vers-v4-hors-renommage.txt`)

| point | ce que fait la v4 | essais (cas sain / artefact, dont « départ » sur la v3) |
|---|---|---|
| texte v4 | `NOM_TEXTE` = `…-v3-v4.md` ; texte vérifié sur la machine et commande de la course (`cmd_course` surchargée) ; la v1 gelée intacte | commande et course v4 / la v3 nomme `…-v3.md` ; dépôt public sans le texte v4 : refus |
| 1 | `controler` rend 6 sur tout échec de `vastai` (code, certificat, inventaire illisible) | 6 / la v3 rend 2 ; étiquette autre : 2 |
| 2 | après la destruction, l'inventaire est relu (trois fois) ; encore listée → arrêt | Vast qui garde la machine : arrêt / la v3 la croit détruite |
| 3 | en-tête sous la garde ; gestionnaires sans échec possible ; `fin()` toujours | journal en panne au refus : versé, détruite / la v3 meurt sans geste |
| 4 | `COMMIT_PRIVE` et empreintes des quatre modules et de l'amorce, au journal du pilote et de la machine | empreintes réelles relues dans le journal |
| 5 | `git status --porcelain` relevé de nouveau juste avant la course, écrit, refus sinon | « vide » au journal / arbre sali après `--verifier-seulement` : refus |
| 6 | `_grep` : ligne entière | ligne de 330 caractères entière / la v3 la coupe à 120 |
| 7 | numpy 2.5.3 sous les trois interpréteurs (hôte) et les deux chemins (amorce) | 2.5.3 / 2.4.6 sous le relais ou la configuration : refus ; amorce : code 2 |
| 8 | essais neufs ; délais des `git` locaux du versement ramenés à 60 s | huit artefacts de la machine (texte, lignée, pièce, statut, port, `--verifier-seulement`, réglages du relais, `ls-remote` contredit) ; client : délai et marqueur, certificat, espace ; cinq « no_such_ask » ; `controler` protégée et délai ; minuterie sans `curl` (repli `python3`, adresse locale) ; amorce qui installe numpy / `pip` en échec ; versement au pire cas mesuré : 3 360 s ≤ 3 600 s / v3 : 4 260 s > 3 600 s |

Les essais de la machine v4 prennent `/usr/bin/python3` (3.13.18, numpy 2.5.3), comme l'image ; le `.venv` des essais a numpy 2.4.6.

## 4. Essais (`timeout 900 nice -n 10`, aucun réseau, dans le miroir)

v1 `test_hote_durable_a1_v3.py`, v2, v3 et v4 : **354 essais passés (v1 49, v2 82, v3 96, v4 127), aucun sauté, en 391 s** ; sortie `essais-lanceur-v1-v2-v3-v4.txt` (`eb3dbc89…`).
Les essais v4 = 95 des 96 de la v3, renommés (alias seuls : `attaque_goodhart_v3.py` et `…-v3.json` intacts), et 32 neufs ; l'essai retiré compare la v2 à la v3 sur C2 et reste rejoué dans les essais v3 (dans le monde v4, le dépôt public ne porte que le texte v4, que la v2 refuse : il ne prouvait plus rien ; première passe : 354 passés, 1 échoué, lui). Défaut
trouvé dans mon premier essai de versement : une poussée en échec saute le `ls-remote`, ce qui sous-estimait le pire cas ; corrigé
(poussée qui répond, `ls-remote` qui la contredit).

## 5. Ordre de course v2 (`docs/procedures/ordre-fille-a1-v3-troisieme-course-v2.md`)

Destinataire : la session pilote. Préalable 2 au motif `'refs/heads/donnees/attaque-goodhart-v3-a1v3-troisieme-*'` (quatre branches ;
la copie `…-versement-interrompue-v1` n'est pas une branche). Préalable 3 : lecture, sans exécution, de la commande d'Argon gelée
(`221df610…`) : clés de `/relais/etat`, arguments de `servir`, variable de la clé, chemin d'un 402. Préalable 4 : jeton par
`JETON_VAR` = `CONTROLE_IA_GITHUB_TOKEN` ou `CONTROLE_IA_GITHUB_TOKEN_2` (choix de Lazar), sans échéance ou au 19 novembre au moins,
ligne d'état HTTP lue. Préalables 5 et 6 : « Argon seul » et la confirmation du crédit d'Argon par Lazar écrits au journal.
Préalable 7 : aucun appel de contrôle d'Argon (le texte n'en prévoit pas). `timeout 1800` pour `louer`. Reprise après « no_such_ask »
dans un dossier neuf, une fois. Conduite pour chaque code de `controler` (0, 1, 2, 3, 5, 6, 7). Voie de récupération d'une machine
arrêtée avant l'échéance (`vastai start instance`, non éprouvée).

## 6. Ce qu'une contre-lecture courte des ajouts doit regarder en premier

1. Paragraphe de tête de la v4 : « aucune course sous la v3 », « troisième course », et surtout la couverture du périmètre de
   GO-2026-11-04-06 (« texte v3 neuf ») par R-1553 : je l'écris « à confirmer par Lazar » ; c'est un nœud tant qu'il n'a pas dit oui.
2. Section 0.8 : 28 lignes ; les points 3 à 17 résument les 15 couples du contre-lecteur, les autres sont les miens.
3. Marqueur `<<COMMIT_LANCEUR_DURABLE>>` remis à la place de `bb35e87f…` (deux fois) : le scellement doit le remplir par le commit
   qui porte le lanceur v4 **et** ses trois dépendances.
4. Section 8 : les corrections 2, 5 et 7 ajoutées à la liste d'arrêt (refus neufs avant la course : statut, numpy) ; 1, 3, 4, 6 et 8
   n'y figurent pas (sans effet sur la liste).
5. Lanceur v4 : `cmd_course` surcharge la commande de la v1 en remplaçant le nom du texte (présent une fois) ; tout autre usage de
   `h.NOM_TEXTE` dans la v1 (aucun relevé hors `cmd_course` et du chemin vérifié) serait à revoir.
6. Correction 2 : l'arrêt d'une machine encore listée après sa destruction arrête aussi la minuterie (comme la « destruction
   refusée » du texte) ; trois relectures à 10 s d'intervalle.
7. Correction 7 : la course échoue si numpy n'est pas 2.5.3 ; la sonde v10 a relevé 2.5.3 sur l'image.
8. Versement : le pire cas (3 360 s) tient sous la réserve d'1 h, de peu ; il compte deux arrêts de 120 s au plus.
9. Ordre v2, préalable 3 : la commande gelée n'a été lue par personne de ce chantier ; si ses clés diffèrent, la machine refuserait
   après son signe de vie (coup unique).
10. Notes 5 à 9 du contre-lecteur du texte, non reprises (section 2 ci-dessus).
