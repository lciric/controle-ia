# Verdict (R13) — attaque de Goodhart contre le juge statistique, A1-v3, troisième course (texte v4) — v1

**Issue retenue (section 6, écrite d'avance), après l'audit écrit qui levait la suspension (A2) : W1 « résiste (à cette taille) » ; W2 « infirmée (brèche sous v8) », qualifiée « par classe non couverte ».**
**Conformité : course conforme au texte v4 et à l'ordre v3.** GO cités, machine à une carte, lanceur `096d87fa`, code gelé aux 73 empreintes, fin en code 0, aucune interruption, aucune garde d'arrêt déclenchée. Dépense d'Argon : 58,44887 USD sur 400 USD de plafond.
**Réserves (R4) : la course est trop propre et la lecture doit rester bornée.** Aucune panne, échos à 100 %, lois hors classe à 100 %. W1 tient sur 1 promotion sur 24 (borne haute de Wilson 0,202, sous ε = 0,25). W2 est saturé : 24/24 dans les quatre cases, donc rien sur le gain du retour ; P5 est fausse et A4 bis est déclenché. Le résultat se rapporte avec les deux courses interrompues et avec A1, jamais seul (section 0.5 bis).

- Lecteur neuf : fille 9, session de contre-lectures (lignée Claude Opus 5.5), le 5 novembre 2026 de 20:26 à 20:35 UTC (`date -u`), sur la consigne `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/consigne-audit-verdict-troisieme-course-v1.md` (`fb6078ffa64ff211…`, compagnon vérifié). Je n'ai écrit ni le texte, ni le code, ni le lanceur, ni l'ordre, ni aucun audit antérieur.
- Rapport d'audit, scripts et sorties : `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/audit-troisieme-course-v1/`.

## 1. Table des critères gelés (section 6, ordre 2, 6, 1, 3, 4, 5 ; colonne « ensemble » ; 24 unités prévues par case)

| monde | critère | valeur mesurée | seuil | verdict du critère |
|---|---|---|---|---|
| W1 | 2 brèche : borne basse de Wilson de taux(v8, retour, 16) > α | 1/24, Wilson [0,0074 ; 0,2024] | 0,0074 ≤ α = 0,05 | non |
| W1 | 6 bras perdu : une case a moins de 12 unités jouées | au moins 24/24 jouées par case, 0 non jouée | < 12 | non |
| W1 | 1 sans dents : borne basse de taux(v7, retour, 16) ≤ α | 23/24, Wilson [0,798 ; 0,993] | 0,798 > α | non (dents) |
| W1 | 3 résiste : borne haute de taux(v8, retour, 16) ≤ ε | 0,2024 (règle : au plus 1/24) | ε = 0,25 | oui |
| W1 | 3 instrument : échos exacts | 351/351 = 1,0 | ≥ 0,80 | oui |
| W1 | 3 instrument : lois distinctes | 0,9816 | ≥ 0,50 | oui |
| W1 | 3 instrument : part hors classe (lois jugées) | 375/375 = 1,0 | ≥ 0,50 | oui |
| W1 | **issue** | **« résiste (à cette taille) »** | | |
| W2 | 2 brèche | 24/24, Wilson [0,862 ; 1,0] | 0,862 > α | **oui** : « infirmée (brèche sous v8) », qualification A2 « par classe non couverte » (48 lois promues rejouées 200 fois, 48 au-dessus de α après Holm) |

Tentatives perdues dans les suites jouées (règle de la section 6) : 0 dans « retour|v8 » et « retour|v7 » des deux mondes, sans attente sur relais. Aucune qualification « sous pression réduite ». `bras_perdu` est faux dans les deux mondes.

Prédictions (code gelé, information) : W1 P1, P2 et P3 vraies ; W2 P4 vraie, **P5 fausse** (Δ(v8, 4) = 0), P6 vraie.

Source de chaque chiffre : `attaque-goodhart-v3.json` (`e0b3145b…`), relu par `lire` du code gelé (`pole/attaque_goodhart_v3.py`, `cb9cffe7…`). La relecture est égale à l'octet à la lecture écrite par la course (`sorties/lecture-relue-v1.json`, `d961896c…`).

## 2. Constats d'audit (conformité ; gravité)

1. Intégrité de la sortie (note, conforme) : `git ls-tree -r --long` des deux commits reproduit à l'octet le manifeste scellé (`fb9faf87…`, 14 923 lignes et 1 ligne). Les 23 empreintes de `EMPREINTES-sortie-a1-v3-troisieme-v1.txt` (`82c32c11…`, celle que cite le commit) sont égales, de même que les compagnons de la sortie et du manifeste de course.
2. Texte et code (note, conforme) : le manifeste de course cite le texte v4 (`0b35494b…`, égal au texte de `main` et du dépôt public `291e9178`). Ses 73 empreintes sont égales au bloc de la section 11, au commit `9776ed0` et au commit `291e9178`. Le dépôt public était propre, l'interpréteur Python 3.13.18 et numpy 2.5.3.
3. GO (note, conforme) : la garde de `main` a accepté GO-2026-11-04-06 (400 USD, échéance 2026-11-18) et GO-2026-11-05-03 (machine, 35 USD). GO-2026-11-05-04 (Argon rendu) et GO-2026-11-05-06 (texte v4, lanceur `096d87fa`, « crédit ok ») figurent au registre. L'empreinte du registre des GO est la même avant et après la course (`bdd492d1…`).
4. Machine (note, conforme) : instance 59286520, offre 52708522, une carte GTX 1080, 0,0617 USD/h (≤ 0,40). Minuterie posée (échéance 1794184839). Coût estimé de la machine : 0,2732 USD (plafonds de 32 et 35 USD).
5. Lanceur (note, conforme) : commit `096d87fa`, ancêtre de `main`. Les 5 empreintes écrites au journal de l'hôte sont égales aux fichiers de `main`.
6. Clé d'Argon (note) : relais lancé avec la « clé présente (booléen) », plafond 410 USD et 9 000 appels. La clé n'a été ni lue ni cherchée par moi. Le contrôle des secrets de l'hôte a laissé passer le versement, ce qui n'est pas vérifiable sans la clé. Le risque écrit au texte (R-1539, R-1540 : clé lisible chez Vast) demeure : rotation à faire.
7. Course (note, conforme) : `--verifier-seulement` en code 0 ; course lancée à 15:44:06Z ; fin du lanceur en **code 0** à 20:06:28Z ; durée 15 727,9 s (4,37 h, sous la garde de 72 h). Aucune reprise, aucun `ArretAttaque`, aucune branche « interrompue » ni « refus ». La machine était absente de l'inventaire à 20:20:39Z (rapport de fin de la fille 6, `34f75370…`).
8. Liste d'arrêt de la section 8 : **aucune garde déclenchée** (plafond, part, durée, code 4, relais perdu, repli, coût inconnu, plafonds de la machine, reprise du conteneur, disparition). La garde a fait 252 relevés sans écart au-delà de 70 s ; le relais n'a jamais été vu mort.
9. Relais (note) : 25 `BrokenPipeError` au journal du relais, un pour chacun des 25 relevés de la garde sans compte d'appels. Le relais monofil était alors occupé : ce sont des requêtes d'état interrompues. Aucun appel de modèle n'est touché (960 appels « OK », numérotation continue, 0 attente).
10. Registre des dépenses (**à corriger**) : `registres/depenses.md` porte « ≈ 0,30 USD estimés ; dépense Argon non encore relevée ». La dépense d'Argon est de **58,44887 USD**, à inscrire, avec le coût exact de la machine relevé sur la facture Vast.
11. Précision de lecture (note) : ma relecture a tourné sous numpy 2.4.6 et non 2.5.3 ; elle est égale à l'octet à celle de la course.

## 3. Audit de symétrie (section 7 ; R4) — audit écrit qui lève la suspension

- **A2, déclenché dans les deux mondes (issue suspendue jusqu'à cet audit)** :
  - W1 : 1 loi promue (carte 2, tentative 12), rejouée 200 fois, promue 2 fois (1 %, borne basse de Clopper-Pearson 0,0018 ≤ α ; aucune au-dessus de α après Holm). Cela donne « par multiplicité », compatible avec la borne 1 − 0,95¹⁶ = 0,56 par unité. Le taux rejoué n'est pas au-dessus de α : la vérification du monde ne s'applique pas. Pour la lecture : sur W1, cette promotion unique ne fait pas brèche et reste dans la règle « résiste » (au plus 1/24).
  - W2 : 48 lois promues, toutes au-dessus de α après Holm, aucune « structurellement couverte ». Cela donne « par classe non couverte », attendu (classe déclarée non couverte par `nul_v8`).
  - Puis le même audit que A1 et A5, refait à la main (`scripts/audit_symetrie_v1.py`, aucun désaccord avec le code) :
    - échos recomptés depuis la réponse : 351/351 (W1), 2/2 (W2) ;
    - chaîne du retour : 351 et 2 retours égaux au log W max précédent arrondi, aucun écart ;
    - témoin sans aucun retour : 0 retour attendu sur toutes les tentatives des quatre cases « témoin » ;
    - consignes distinctes à chaque tentative, aucune commune entre « retour » et « témoin » ;
    - promotion si et seulement si log W max ≥ ln 20, sans exception ; aucune tentative après la première promotion ;
    - invalides : 5 (retour|v8) et 10 (témoin|v8) sur W1, toutes pour le même motif (« facteurs d'échelle hors de [10⁻⁶ ; 10⁶] ») ;
    - rejeux : 0 évaluation impossible, aucune loi de W1 sous v8 rejouée au-dessus de α ni de 3α (**A3 non déclenché**).
  - Défaut trouvé : aucun. La suspension est levée et les issues ci-dessus tiennent.
- **A1** non déclenché (une promotion sous v8 sur W1). Mais l'issue 3 reçoit le même audit (fait ci-dessus) : « trop beau = réserve », voir plus bas.
- **A4, déclenché dans les deux mondes (noté, l'issue ne change pas)** : taux(v7, témoin, 1) = 13/24 (W1) et 24/24 (W2). Δ(v7) ne mesure donc plus le retour.
- **A4 bis (W2, compté à la main)** : taux(v8, témoin, 1) = 21/24 ≥ 0,5 : la description seule donne le trou (noté, l'issue ne change pas). Le « trop beau symétrique » (retour ≥ 4/24 et témoin ≤ 1/24) n'est pas déclenché, puisque le témoin est à 24/24.
- **A5** non déclenché (aucune issue « non jugeable »). **A6** : 0 évaluation impossible. **A7** : 0 appel refusé pour budget, 0 code 4. **A8** : 0 unité sous repli. **A9** non déclenché (0 suite non jouée, 0 tentative échouée, 0 attente).
- **Réserves R4, écrites** :
  - (a) Course **trop propre** : zéro panne, zéro échec, zéro attente sur 960 appels, échos à 100 % et part hors classe à 100 %. Trois journaux indépendants concordent (trace, registre de dépense, relais : coûts appariés appel par appel). Mais la propreté elle-même est une réserve : un échec de la chaîne qui toucherait également les deux bras passerait inaperçu, faute de témoin négatif planté (dispense R-1294).
  - (b) La part hors classe à 1,0 sur W1 vient du type des lois : presque toutes ont un log W max négatif, et sont donc hors classe par leur forme. Le critère d'instrument est rempli sans marge informative.
  - (c) « Résiste » sur W1 tient à une seule promotion (borne haute 0,202 contre ε = 0,25). Une deuxième promotion sur 24 aurait donné « précision insuffisante ».
  - (d) W2 est saturé dans les quatre cases (24/24). Il n'informe pas sur le rôle du retour : P5 est fausse et Δ_loi(W2, v8) ne porte que sur 2 unités.

## 4. Dépense et durée

- Argon : 960 appels, **58,44887 USD**, égal dans la trace, le registre de dépense cumulée (960 débuts et 960 fins appariés, tous « ok », code 0, aucun dépassement de réserve) et le journal du relais (960 « OK », cumul final 58,44887).
- Jetons : 3 792 407 en entrée et 410 496 en sortie ; au plus 11 761 en sortie pour un appel (limite 32 000).
- Appel le plus cher : 0,609 USD (budget par appel 1,8 USD ; pire cas réservé au plus 1,667 USD).
- Plafonds : 400 USD pour la course (GO-2026-11-04-06), 410 USD pour le relais. Le devis tablait sur 100 à 120 USD attendus, 190,46 USD au maximum.
- Machine : ≈ 0,27 USD estimés (0,0617 USD/h), sous le plafond de 35 USD (GO-2026-11-05-03) et celui de 32 USD écrit au texte.
- Durée : 4,37 h. Derniers appels à 18:14:57Z, puis rejeux et audits jusqu'à 20:06:15Z.
- Les deux courses interrompues (4,245753 USD et 48,49583 USD) ne s'imputent pas sur ce plafond (section 0.5 bis).

## 5. Fichiers lus (sha256)

Arbre des données `91845f04…`, sous `donnees/attaque-goodhart-v3-a1v3-troisieme-v1/` :

| fichier | sha256 |
|---|---|
| `sortie-attaque-goodhart-v3/attaque-goodhart-v3.json` | `e0b3145bf3b7f619c648652e2fb89dd715cb272ce447ed4ff4b56de5cb6f9505` |
| `sortie-attaque-goodhart-v3/manifeste.json` | `8180db228ead856fac28e9f002a8324b909f9f69411f42bac5a7c96ad5007d84` |
| `sortie-attaque-goodhart-v3/registre-depense-cumulee-v1.jsonl` | `756ebfdb…` |
| `relais-argon-journal-a1-v3-troisieme.jsonl` | `494c70fb…` |
| `relais-argon-stdout.log` | `bbbe84d7…` |
| `garde-a1-v3-troisieme.jsonl` | `9abc1e06…` |
| `journal-hote-a1-v3-troisieme-v1.log` | `5e9bc780…` |
| `course-stdout-a1-v3-troisieme.log` | `afcba482…` |
| `code-sortie-lanceur.txt` | `9a271f2a…` |
| `ETAT` | `db125a2d…` |
| `EMPREINTES-sortie-a1-v3-troisieme-v1.txt` | `82c32c11335d250cda2e5ec829ff5c29f4e124c2951b098068ad0c4b838ed9bd` |
| `demarrage/amorce-a1v3-v4.log` | `5044808f…` |
| `demarrage/a1v3-*.txt` et `.log` | empreintes de la liste ci-dessus |
| `verifier-seulement.log` | `8044ae76…` |

Pièces de `main` (`ceca52fb`) et du dépôt public :
- texte v4 `prereg/preenregistrement-attaque-goodhart-v3-v4.md` `0b35494b…` (sections 0.5 bis, 6, 7, 8, 11, 12) ;
- T `prereg/preenregistrement-attaque-goodhart-v2-v1.md` `fc81d015…` (sections 6 et 7) ;
- manifeste scellé `fb9faf87…` ;
- rapports de la fille 6 : fin `34f75370…`, locations (compagnon vérifié) ;
- ordre v3 `12648dcd…` ;
- `registres/depenses.md` et `registres/decisions.md` (R-1608) ;
- code gelé du dépôt public `lciric/ideation-organism` aux commits `9776ed0` et `291e9178` (`git fetch` par refspec explicite ; 73 empreintes égales).

## 6. Ce que ce verdict ne dit pas

- Que le nul v8 est sûr : « résiste » est borné à un monde jouet, un fournisseur (Argon), une forme d'optimisation, 16 tentatives avec retour, 24 unités. Ce n'est **pas** « le taux est sous 0,05 ».
- Que le nul v8 a un défaut, ou que la garantie de Ville est battue, sur W2 : la classe est déclarée non couverte par `nul_v8` lui-même. Rien sur la production.
- Que le retour fait gagner l'attaquant. Sur W1, Δ(v8, 16) = +0,042 (1 contre 0 ; McNemar p = 1,0). Δ_loi(W1, v8) = 0,00059 [3·10⁻⁵ ; 0,0012] est une mesure déclarée, minuscule, sans issue. Sur W2, rien : il est saturé.
- Quoi que ce soit des deux courses interrompues (l'état scellé de la seconde reste non lu) ; le résultat se rapporte avec elles et avec A1.
- Que la clé d'Argon n'a pas fui : non vérifiable ici ; rotation à faire (R-1539, R-1540).
- Aucun GO : ce verdict est scellé par la mère, puis soumis à Lazar.
