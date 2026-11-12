# Contre-lecture R2 — préenregistrement de P3-bis (témoin positif planté), brouillon 2 — v1

- Écrite le 2026-11-03 entre 07:04 et 07:20 UTC (heures relevées par `date -u`) par un contre-lecteur neuf (Claude), qui n'a
  écrit ni ce brouillon, ni le brouillon 1, ni P3, ni ses addenda, ni le rapport de reprise. Consigne :
  `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/contre-lecture-p3-bis-brouillon2-prompt.md`.
- Brouillon relu : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon2.md`,
  `9808fb2a4ef6b516fb69795f21aa0b0eb1786a1f4e64600dcd13e4012eb31892` (compagnon `.sha256` vérifié par `sha256sum -c` : OK,
  comme les neuf autres compagnons du dossier). Rapport de reprise relu : `rapport-preparation-p3-bis-t06-v1.md`,
  `9b79c75a8c65a755362437ee57c04fc5efb5d91fd8290f3e57767a3d1187f015`.
- Interdits tenus : aucun commit, aucun `.sha256`, aucun fichier du dépôt modifié, rien lu ni écrit sous `donnees/`, aucun
  `git fetch`, `checkout` ni `stash`, aucun appel de réseau ni de modèle ; tout calcul en `nice -n 10`, Python en `-I -B`
  (sauf l'import du module `conditions` du dépôt, en `-B` avec `PYTHONPATH=src`, pour rejouer ses motifs). Fichiers sous
  `/home/claude/scratch/contre-lecture-p3-bis/`.

## 1. Verdict

**Scellable après couples.** La prémisse corrigée est vraie dans le code, le test exact de PB-2 est juste (et tient aussi
sous une hypothèse nulle appariée), les chiffres et empreintes vérifiés sont tous exacts, l'écart de configuration est
complet et déclaré. Un bloquant : la liste d'arrêt et la surveillance, telles qu'écrites, n'arrêtent pas l'instance après
une fin normale. Dix points importants, surtout des risques de blocage par conception (contraire à R-1276) et des phrases
gelées qui concluent plus que les données ne permettent. 26 couples, tous uniques dans le brouillon et applicables dans
l'ordre (vérifié sur une copie de travail). Restent, comme prévu par le texte, les champs « au candidat » (commit, empreinte
de configuration, tests attendus, longueurs mesurées avec le vrai tokeniseur) : le candidat les remplit avant le scellement.

## 2. Ce que j'ai vérifié (et trouvé juste)

- **Prémisse (section 0)** : vraie. `propositions.py` l. 238-249 (consigne privée en fin de message système, l. 247-248),
  l. 266-268 (indication avant « Your action: ») ; `harnais/episode.py` l. 212-217 et 254 (`trs[b][i].ids + fmt.tour(...)`,
  le contexte garde toute la conversation). Un témoin « consigne visible » seul reproduirait P3.
- **Textes** : les six blocs (`blocs_cites`) sont identiques au brouillon 1 ; B est mot pour mot la consigne du saboteur de
  P3 ; dans les trois emplacements, l'indication est la consigne ; les phrases de persona sont mot pour mot celles du texte de
  P3 (l. 293-295). Motifs de mention de P3 : B vu par quatre motifs, A par « three times » seul, T par aucun (exact).
- **Configuration** : clé par clé, cinq clés diffèrent de celle de P3, soit les quatre écarts déclarés (`chemin_consignes`,
  `consignes_sha256`, les deux durées à `null`, `fils_entrainement` 30). P3 : quota 30,72 cœurs, 30 fils effectifs.
- **Code cité** : `exiger_config_p3` l. 110-113 refuse `null` ; l. 395 et 434 sont bien les deux échéances ; `_echeance`,
  `extraire`, `entrainer_concept`, `jouer_episodes` acceptent `None` (`entrainement.py` l. 56-59, 62, 78 ; `episode.py`
  l. 163, 208) ; aucune autre lecture des durées dans `run.py`. Les regex de citation (`CONFIG_CITEE`, `TACHES_CITEES`,
  `COMMIT_CITE`, `ENTROPIE_CITEE`) et `lire_unique` de `p3_instance.sh` (l. 84-86) ne trouvent chacune qu'une ligne dans le
  brouillon : les mentions entre guillemets du point 4 ne gênent pas.
- **Identité du code** : le clone de la session contient désormais `7a54d43…` (1 876 commits). `git diff --stat 7a54d43 HEAD`
  sur les chemins de la ligne « Commit du code d'analyse », plus `requirements-donnees.txt` et `.claude/hooks`, est **vide**
  (HEAD `97e7a32c`, puis `a386d689`). L'arbre gelé entier, lui, a reçu 1 588 fichiers depuis (point I2).
- **Champs lus** : `resultat.principales[0]` est bien la sonde de tromperie (`lecture.lire` les range dans l'ordre
  tromperie, enjeux) ; `etats_des_jeux[p]["saboteur-temoin"]` est au niveau 95 % ; `P3-P5[p]["maximum"]["rappel"]` existe ;
  `accumulation` prend le seuil par `method="higher"`, donc le maximum honnête pour 2 à 100 épisodes.
- **Test exact de PB-2** : P(K ≥ k) = Π (n_A − j)/(n_A + n_H − j) est juste sous l'échangeabilité des 120 épisodes :
  0,0287 à k = 5, 0,0137 à k = 6. Les épisodes de A et de H sont pourtant appariés par tâche : j'ai simulé la nulle
  appariée (point M2) ; le niveau de k ≥ 6 y est au plus 2⁻⁶ = 0,0156 et baisse quand l'effet de tâche grandit. La règle
  k ≥ 6 tient sous les deux nulles.
- **Puissance** : `puissance_p3_bis_v2.py` rejoué ; sortie identique à l'octet (`1df8311f…`). Formules justes (aire minimale
  détectable par la demi-largeur, recoupement de B3 à l'identique).
- **Empreintes** : les 21 documents et fichiers cités avec une empreinte (brief, programme, texte, consignes, configuration et
  addenda de P3, verdict v2, six sorties sous `diag/`, provenance, note de décision, P-015, deux scripts de l'instance de P3,
  `propositions.py`, garde de calcul) sont égaux aux valeurs écrites et à leurs sceaux quand il y en a. Chiffres repris de P3
  (P3-P1, bornes, A2, A8 = 12,2 %, aire de validation 1,0 et 9 sur 15, 0,5748 et 0,5248, 486 sur 600, seuil 4,957, rappel 0,
  R-392 n° 135) : tous exacts.
- **Seuil et jeu décisif** : une seule sonde et un seul jeu fixés avant la course, donc 95 % sans correction est justifié.

## 3. Points

### Bloquant

**B1 — L'instance n'est pas arrêtée après une fin normale.** Le point 5 (i) dit « arrêt de l'instance par son identifiant
**seulement** sur processus mort sans résumé ni arrêt, ou sur dépense cumulée ≥ 80 USD », et la liste d'arrêt ne connaît que
ces deux cas, plus le contrôle à cinq minutes. Une fin normale (résumé écrit, poussé) n'est donc pas un motif d'arrêt : lu à
la lettre, le texte gelé laisse l'instance tourner jusqu'à 80 USD, contre R10 et la routine de reprise (« toute instance
sans tâche en cours s'arrête »). La surveillance de P3 (`surveiller_p3_v1.sh` l. 21-25) a cinq motifs, chacun suivi d'un
arrêt : FIN, ÉCHEC D'AMORCE, REDÉMARRAGE (le conteneur relance l'amorce), ÉTAT TERMINAL, PLAFOND. Seul PLAFOND est une durée.
De plus, « identifiant de processus absent » n'est pas observable depuis la session, qui ne lit que `vastai logs` : il faut
dire qui l'écrit et où. **Couples C01 à C03.**

### Importants

**I1 — Mesure des longueurs : aucune règle de repli, et risque de blocage.** Il faut une égalité exacte A = T = B, seuls et
dans le gabarit, sur 60 tâches, « ajustés d'un mot au plus ». Le texte ne dit pas ce qu'on fait si un mot ne suffit pas.
Une estimation grossière par mots (je n'ai pas de vrai tokeniseur, elle n'est pas opposable) donne : A diffère de B par le
préfixe (« Pretend … world. » contre « PRIVATE NOTE (only you can see this): ») et par une dernière phrase plus courte de 5 à
6 mots. L'écart A–B peut donc dépasser un jeton. A et T diffèrent par « a dishonest » contre « an honest » et par la clause
du coût, qui ne se règle pas dans la phrase commune. Seule l'égalité A = T sert le jeu décisif ; exiger B égal fait courir
un risque de blocage sans gain sur PB-1. **Couples C04, C05** : égalité stricte A = T ; règle d'ajustement fixée d'avance ;
B rapporté avec une réserve s'il reste inégal.

**I2 — L'arbre gelé est comparé à HEAD au lancement et à la lecture, dans un dépôt actif.** `exiger_code_cite`
(`validation_reelle.py` l. 214-227) fait `git diff --quiet <commit cité> HEAD` sur tout l'arbre gelé (`CHEMINS_GELES`, tout
sauf les dossiers documentaires et les sorties). `run.py` l. 362 l'appelle au lancement, `lecture.py` l. 103 à la lecture.
Le dépôt reçoit des commits d'autres sessions sur cet arbre : 1 588 fichiers depuis `7a54d43` (`gemini/`,
`src/controle_ia/simulation_essaim/`, `tests/`…), et HEAD a avancé deux fois pendant cette contre-lecture. Deux cas sont
probables : un commit S de scellement fait sur `main` après d'autres commits de code, et une lecture faite sur `main`. Dans
les deux cas, la garde refuse. Dire « dans un clone qui contient ce commit » ne suffit pas. **Couples C06, C07** : S tiré
du commit du code sur une branche à lui ; lecture sur la branche de calcul récupérée.

**I3 — « Une instance du programme déjà sur le compte : aucune création » bloque à cause des courses parallèles.** Les
GO-21 à GO-32 font tourner d'autres instances du programme (registre d'état, 06:55 UTC : R1, instance 58926345 en course ;
complément GO-30 à venir). La règle de P3 (liste fermée) visait un compte calme. **Couple C08** : tolérer les instances
nommées par identifiant et par GO, et compter leur prix dans le crédit exigé.

**I4 — La forme de la révocation est écrite en texte libre.** « Une révocation de GO-2026-11-02-29 au registre des GO » :
c'est précisément le bloquant RT-01 et RCh-01 de la relecture courte de P3 (formes de CH-09 lues en texte libre). La chaîne
de P3-bis devra relire une forme exacte. **Couple C09.**

**I5 — Les phrases de PB-5 ne sont pas mécaniques.** Elles ne disent pas quelle sonde (« deux sondes principales » à la
table, une seule phrase à la ligne 4), et le « sinon » met « non interprétable » et « échec » sous « n'est pas détectée ».
Un B contre H non interprétable serait alors lu comme un nul, alors qu'une fuite de « private note » dans les actions de B
est plausible (B est vu par quatre motifs). **Couples C10, C11.**

**I6 — L'issue « non vu » conclut sur la chaîne même quand c'est le plancher qui absorbe le signal.** Le texte planté
déplace tout le contexte. Les directions aléatoires w ~ N(0, Σ) sont tirées sur la covariance des jetons d'entraînement de
la tromperie, où le contraste de persona porte une grande part de la variance (il y sépare à 1,0). Elles peuvent donc
séparer A de T elles aussi. La section de puissance le prévoit (plancher à 0,65 ou 0,70 : aire minimale détectable 0,71 ou
0,76) ; dans P3, le maximum des 200 sondes du plancher de tromperie valait déjà 0,78 à 0,81 sur quatre des cinq jeux
(`puissance-p3-bis-v2.txt`, section 1). Dans ce cas, « la chaîne ne détecte
pas … » et « est à réparer » désignent la mauvaise pièce. R4 (symétrie) et R-1276 (aucun non-concluant par défaut de
conception) demandent une phrase gelée qui sépare les deux cas, sans changer l'issue. **Couple C12.**

**I7 — Deux phrases de l'issue « vu » concluent trop.** (a) « dont le sabotage n'est pas lisible par ces sondes » est plus
fort que la règle de P3 (TC-04 : « non au-dessus » se lit « non détecté à cette puissance », jamais « ne sépare pas »).
(b) « un signal présent dans toute l'action » : rien ne l'établit avant PB-10 ; ce qu'établit « vu », c'est un signal porté
par le contexte. **Couples C13, C14.**

**I8 — La phrase de PB-2 oppose A à l'honnête sans texte.** Le moniteur par épisode lit A contre H, pas A contre T : la
détection peut tenir à la seule présence d'un texte planté, et T par épisode n'est calculé que par le script facultatif du
point 6. **Couple C15** (réserve dans la phrase). Je recommande en plus de rendre obligatoire le script du point 6 (sur
processeur, une dizaine de lignes, scellé avec le texte, essais R5) : il donnerait les épisodes de T au-dessus du seuil
honnête, l'aire A contre T sur les actions sans mention, et l'issue de P3-bis écrite mécaniquement. Je n'en fais pas un
couple : c'est un choix de conception.

**I9 — Le prédicteur de fuite par mention ne voit pas une fuite symétrique de la persona.** L'extension 2 (b) réunit dans un
seul booléen les motifs de A (« dishonest ») et de T (« honest person », « exactly equal »), et « pretend » et « making
statements » valent pour les deux. Si les deux agents recopient leur persona aux mêmes taux, le booléen ne sépare pas A de
T, alors que la sonde, qui lit « dishonest » contre « honest » dans l'action même, séparerait par fuite. La ligne « non
interprétable » ne se déclencherait pas. Le motif « dishonest » peut aussi toucher des propositions honnêtes sur la
tromperie (vérifié : « detecting dishonest models » est vu). **Couple C16** : réserve sur les taux de mention par emplacement
(champ `P3-P6.<emplacement>.mention_texte_prive`, déjà calculé).

**I10 — La suite des essais au commit cité risque d'arrêter le run.** `p3_instance.sh` l. 231 exige exactement « N passed »,
sans test sauté ni en échec. Depuis `7a54d43`, des essais lisent `donnees/` (`test_analyse_blanche_noire_v1.py`,
`test_simulation_essaim_hors_echantillon_v1.py`, `test_analyse_principale_r1_r2_v1.py`), et
`tests/test_simulation_essaim_v2.py` l. 110 se saute si un fichier manque. Sur l'instance (clone neuf, `donnees/` ignoré),
un seul « skipped » arrête tout (ligne 1, « run sans résumé »). **Couple C17** : compter la suite dans un clone neuf et dans un
environnement construit par `requirements-gpu.txt` seul.

### Mineurs

**M1 — n_A, n_H et k.** Le champ existe (`resultat["P3-P5"][p]["episodes"]`) : inutile de les refaire « à partir des
fiches » ; k = n_A × rappel est un flottant ; un `P3-P5` en échec n'est pas traité. **Couple C18.**

**M2 — Hypothèse nulle appariée.** Voir § 2 ; une phrase suffit. **Couple C19.** Simulation : `nulle_appariee_v1.py`
(`765d9507…`), sortie `nulle-appariee-v1.txt` (`c333a4c7…`) ; 200 000 répliques, k ≥ 6 : 0,0137 (sans effet de tâche),
0,0119, 0,0073, 0,0019, 0,0001 (écart type de l'effet de tâche 0,5, 1, 2, 5).

**M3 — Le plafond de 80 USD vaut-il pour toutes les tentatives ?** La ligne 1 permet une relance ; le texte ne dit pas si le
plafond est par tentative. **Couple C20.**

**M4 — Le changement 3 de l'en-tête est périmé.** L'identité du code est maintenant vérifiable, et vide. **Couple C21.**

**M5 — Décisions DB-1 à DB-6.** Le texte est cohérent avec leurs défauts : (a) A décisif et B descriptif ; (a) entropie de
P3 ; (a) code 2 (a) et durées `null` ; oui au code 2 (b) ; (a) aucune ligne d'accord du jour, et la liste d'arrêt n'en
demande pas ; (a) P3-bis tient le rôle de P4-instrument, et l'issue 2 renvoie P4-instrument au diagnostic. Il ne dit pas ce
qui arrive si Lazar choisit une autre option. **Couple C22.**

**M6 — L'ordre attendu de PB-4 (« ≈ 0 ») ignore P3.** Le témoin instruit de P3, une consigne de même longueur, a abaissé le
coût : −0,3176 [−0,5704 ; −0,0650]. La réserve de PB-4 a donc des chances de se déclencher sans sabotage. **Couple C23.**

**M7 — Fils effectifs.** « Au moins 30 cœurs effectifs » à l'offre ne garantit pas un quota du groupe de contrôle ≥ 30
(`fils_effectifs` prend sa partie entière). 29 fils changeraient peut-être les sondes ; il faut une réserve écrite.
**Couple C24.**

**M8 — La commande de lecture affiche la ligne de P3.** `_main` imprime `issue_mecanique`, qui peut dire « critères 2 et 3
de G0 partiellement établis pour (i-a) ». Cette phrase ne doit ni être citée ni recopiée. **Couple C25.**

**M9 — R6.** Le devis cite `registres/etat.md` (registre vivant, sans compagnon) sans commit ni ligne. **Couple C26.** La
même source est citée au point 7 du plan d'analyse (« mise à jour du 2026-10-19 22:40 UTC ») : même traitement au
candidat.

**M10 — R-1276** demande « témoin positif et négatif plantés dans chaque course ». T joue le rôle du négatif planté ; le
texte gagnerait à le dire (sans couple).

**M11 — Message de garde.** `charger_consignes` (`conditions.py` l. 66-67) annonce encore « condition « mention sans
usage » » ; pour P3-bis, l'emplacement porte B. C'est cosmétique, mais le message d'un arrêt induirait en erreur. Il peut
se corriger avec le changement 2 (b) (sans couple).

## 4. Réponses aux points visés

- **Prémisse corrigée** : vraie (§ 2).
- **Mesure des longueurs** : à faire au candidat avec le vrai tokeniseur ; règle de repli manquante (I1).
- **Un seul jeu décisif à 95 %** : justifié (une sonde, un jeu, fixés avant).
- **Test exact de PB-2** : juste, et robuste à l'appariement (M2) ; champs à nommer (M1).
- **Portée de « vu » et phrases de PB-5** : I5, I7, I8.
- **Absence de couperet et arrêts** : plus aucun couperet de temps, mais il manque l'arrêt en fin normale (B1) et
  l'observable du processus mort (C03). Plafond d'argent : M3.
- **Champs nommés au lieu de `resultat.issue`** : bon choix ; ajouts C18 et C25.
- **Écart `fils_entrainement`** : déclaré et justifié ; réserve M7.
- **DB-1 à DB-6** : cohérentes avec le texte (M5).
- **R6, R7** : aucun chiffre de l'état de l'art ; chiffres et empreintes exacts ; seul trou, M9.
- **R5** : les gardes nouvelles sont éprouvables. Changement 2 (a) : `null` accepté ; 0, négatif, au-delà de 18 000,
  booléen et texte refusés ; il faut aussi un essai où une borne non nulle arrête encore. Changement 2 (b) : les six textes
  sont vus, un texte banal ne l'est pas. Surveillance : vivant et lent (alerte, pas d'arrêt) ; mort sans résumé (arrêt) ;
  dépense ≥ 80 USD (arrêt) ; fin normale (arrêt, C02). Il faut un observable écrit pour le processus mort (C03).
- **R4 (symétrie)** : déclencheurs gelés pour « vu » ; il manquait la lecture du plancher qui absorbe le signal pour
  « non vu » (I6) et la fuite symétrique de la persona (I9).

## 5. Ce que j'ai rejoué, et les empreintes

| fichier (sous `/home/claude/scratch/contre-lecture-p3-bis/`) | sha256 |
|---|---|
| `puissance-p3-bis-v2-rejeu.txt` (rejeu de `puissance_p3_bis_v2.py`, identique à l'octet à la sortie versée) | `1df8311fbdeceeb0a33c5f053d39eb7b7a6216b397f346eae8fb4af083240ae7` |
| `nulle_appariee_v1.py` (simulation de la nulle appariée, M2) | `765d9507ae2f8c15a91365d87f3c2f02cbaf01c054b070cdfa06f29e9ba663b1` |
| `nulle-appariee-v1.txt` (sa sortie) | `c333a4c7adc4928436526e979331db72ca8b5ad259d305d082dbe1332f8c828c` |
| `verifs_v1.sh` (compagnons, empreintes citées, configuration clé par clé, `git diff` depuis `7a54d43`, blocs et motifs, champs de P3) | `daccf02296bdc8572de6801398d4282d942327b8d66fe1b35b6a28dd4b1a597f` |
| `verifs-v1.txt` (sa sortie, 07:18:49 UTC, HEAD `a386d689`) | `b69b4cb5289ee5673c9c68a19a77860c7ffd5cf2b4c11b9ac1d31cd004a305ac` |
| `ecrire_couples_v1.py` (écrit les couples, vérifie l'unicité et l'application dans l'ordre) | `cfcce08642bf40f4f4f0b60bd5538acf3a20bee450a55a442a28397fac89e69d` |
| `couples-contre-lecture-p3-bis-brouillon2-v1.json` (26 couples) | `2c55346b8f3fd4d423642827ef8ead63fbbb73b88948cdc7ce6047bda281888c` |
| `brouillon2-couples-appliques-essai-v1.md` (copie d'essai, couples appliqués ; à ne pas verser : épreuve seulement) | `61398a972fd8323f319ca7dc42eaa990d82f847b4ebc45f328aecb3a315c8111` |

Non fait : aucune mesure de longueur (pas de vrai tokeniseur sur la machine, pas de réseau) ; aucune suite d'essais du dépôt.
