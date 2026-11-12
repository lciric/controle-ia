# Consigne : session fille « préalables de P3-bis » — étape D : scellement S, lancement et course (GO-2026-11-10-02) — v1

Écrite par la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` le 2026-11-11 à 15:32 UTC (heure relevée par `date -u`). Destinataire : la session fille `session_013QMayo3Je79e17xB1yHiDw`. Mêmes règles que les étapes précédentes (interdits communs v2 ; **aucun fichier de T0.7 ouvert** ; clés par leur nom ; garde des secrets à 0 avant chaque commit ; `git fetch` à refspec ; extraction partielle ; **arrêt sur tout refus**, ni contournement ni reformulation ni transfert ; R10 : arrêts et destructions par identifiant seulement). **Mot de Lazar** : « scelle le et lnce le » (R-2352 ; lecture de la mère pour le candidat 3, R-2378). **Dépense** : **GO-2026-11-10-02** seulement (plafond 80 USD ; création au plus tard le 18 novembre). **Le texte scellé fait foi** sur tout geste de la course : `prereg/P3-bis-temoin-positif-v1.md` après S (= candidat 3, `76ab66ce…`), en particulier « Liste d'arrêt », plan, point 11, et « Ce que le code et la chaîne doivent changer », point 6 ; **chaque script se lit d'abord par son en-tête** (usage, codes, fenêtre) avant d'être joué.

## D1. Attendre le constat de la mère
La mère constate les préalables P-1 à P-11 au registre, une ligne par préalable, avant S ; elle te le dit. Rien avant.

## D2. Scellement S
Dans `/home/user/controle-ia-travail`, sur `scellement/p3bis-v2` (tête poussée, arbre suivi propre, `origin` = dépôt de travail) :
`bash docs/procedures/P3-bis-temoin-positif-v1/sceller_p3bis_v2.sh scellement/p3bis-v2 > <ton bac>/scellement-S.log 2>&1` ; code 0 exigé ; S poussé et relu par le script. Rapporte : commit S, empreinte de `prereg/P3-bis-temoin-positif-v1.md` (attendue `76ab66ce…`), **la ligne « ligne à inscrire … SCELLEMENT-P3BIS … » recopiée à l'octet**. Puis **attends** : la mère inscrit cette ligne dans `registres/scellements-v1.md` de `main` et te le dit.

## D3. Outil de location
`vastai` 1.8.3 seul : `python3 -m pip install vastai==1.8.3` ; si l'interpréteur du système refuse, environnement neuf `/home/user/outil-vastai-v1` et son `bin` en tête de `PATH` dans le shell de la course ; relève `command -v vastai` et `vastai --version` (1.8.3, sinon arrêt). Clé `VAST_API_KEY` par son nom. Inventaire filtré (identifiant, étiquette, état ; jamais `--raw` sans filtre) : attendus `60218139` (course 7b, `t06-v2`, en marche, GO-2026-11-02-28) et `58936096`, `58936099`, `58936100` (arrêtées, tolérées) ; **aucune n'est touchée**. Toute autre instance : arrêt, rapport.

## D4. Lancement
`bash docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2.sh <S> <ton bac>/lancement-1 <EN_MARCHE> 1`, où `EN_MARCHE` = `60218139:GO-2026-11-02-28` si l'inventaire la montre en marche à ce moment, sinon `-`. Codes : 0 création ; 3 attente (date, place, crédit, aucune offre : relis l'en-tête et le texte, plan point 11 — douze essais à 15 minutes puis repli écrit, tenus par le lanceur) ; 4 création douteuse (inventaire filtré, rapport, rien d'autre) ; 2 arrêt (rapport). Relève : identifiant, carte, prix, heure de création, repli éventuel (`repli-processeur.txt` : la mère l'inscrit).

## D5. Course
1. **Contrôle à cinq minutes** dans sa fenêtre (création + 180 s à + 300 s, en-tête) : `bash docs/procedures/P3-bis-temoin-positif-v1/controle_cinq_minutes_p3bis_v2.sh <id> <ton bac>/lancement-1 <dossier neuf>` ; code 1 : l'instance est arrêtée par son identifiant ; rapport ; nœud.
2. **Surveillance** en arrière-plan : `bash docs/procedures/P3-bis-temoin-positif-v1/surveiller_p3bis_v2.sh <id> <ton bac>/lancement-1 <dépense antérieure> <dossier neuf>` (dépense antérieure : 0 pour la tentative 1) ; PID noté ; alertes sans progrès rapportées ; à chaque motif de fin, le script arrête l'instance par son identifiant.
3. **Fin normale** : `bash docs/procedures/P3-bis-temoin-positif-v1/recuperation_p3bis_v2.sh <S> calcul/p3bis-reel-v1 <dossier neuf>` (lectures fermées : **tu n'ouvres aucun paquet, tu ne lis aucun résultat** ; l'ouverture se fait au rendez-vous, garde d'ouverture) ; puis `bash docs/procedures/P3-bis-temoin-positif-v1/detruire_p3bis_v2.sh <id> <ton bac>/lancement-1 <dossier de la surveillance> <rapport de la récupération>` ; absence relue.
4. **Fin anormale, instance gardée, échec d'un script** : la liste d'arrêt du texte s'applique ; **aucune relance** sans mot de Lazar (nœud, liste d'arrêt) ; rapport.
5. Reste **active** jusqu'à la destruction vérifiée.

## Rapports à la mère (`send_message`), à chaque jalon
S ; création (identifiant, carte, prix, heure) ; contrôle à cinq minutes ; fin ou arrêt ; récupération (branche, commit du paquet, empreintes) ; destruction (heure, coût) ; à la fin, lignes proposées pour `registres/depenses.md` et `registres/arrets.md` (la mère les inscrit).
