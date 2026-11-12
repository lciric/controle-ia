**Relecture de l'écart de P3, candidat 3 au candidat 4 et chaîne du brouillon 3 au brouillon 4 (R-227), 2026-10-19.** Même sous-agent que les deux relectures de l'écart précédentes ; je n'ai écrit ni le candidat 4, ni son script, ni le brouillon 4. Je n'ai pas fait de nouvelle lecture d'ensemble. Dépôt relu à la tête `13d2f64`, en lecture seule ; aucun fichier du dépôt ni aucun registre n'a été touché ; pas de suite des tests.

**Empreintes vérifiées**
- Consigne : `6afdc99a63482ebc4aaf680dbf4e152cdb7f4fa9f8ad1fa7c918c8fcdcb53540`.
- Candidat 4 : `d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672` (555 lignes). Je l'ai reconstruit depuis le candidat 3 versé (`3682c254…`, sceau conforme) avec `construire_candidat4.py` (`de25cb2d…`) : identique, octet pour octet.
- Chaîne brouillon 4 (commit `13d2f64`) : 14 sceaux sur 14 conformes ; traitement `db5be719bd5c3120fbe5c62a20e58edd4899f97f09ab08f6484929edbb6c7a5b`, égal à la citation.
- Rapports cités : `verification-ecart-P3-candidat2-v1.md` (`af89de75…`) et `…-candidat3-v1.md` (`e3a1b7ca…`), versés, égaux à leurs sceaux.
- Journaux officiels des bancs (`…/p3-v1-journaux/`) :
  - contrôles : « cas non conformes : 1 » (1 999 s) ; le cas A44l rend « code 0 ; 51 OK, 0 KO », le KO attendu manque ;
  - lanceur, surveillance et scellement : 0 cas non conforme chacun.

**Vérifications**
- **(1) Texte.** L'écart entier est celui du script : rien d'autre n'a changé.
  - La phrase « stockage au plus 0,03 USD de l'heure » tient sur une ligne (l. 354).
  - Le dossier `v2` est cité partout où le texte nomme le dossier des copies versées ou le lanceur : l. 56, 117 et 473. Le dossier `v1` n'apparaît plus que comme versement abandonné (l. 474).
  - VE3-01 est repris (l. 548), et VE3-02 aussi : en-tête l. 3-14 et paragraphe des changements l. 112.
- **(2) Chaîne.**
  - Neuf scripts changent. Dans chacun, une ligne de commentaire est ajoutée en ligne 2, et le dossier passe de `docs/procedures/P3-premier-test-v1` à `docs/procedures/P3-premier-test-v2`, dans le code et dans les commentaires.
  - Dans les contrôles, deux constantes changent en plus du dossier : `CANDIDAT_RELU_CHEMIN` (candidat 4) et `REPETITION_JOUET_CHEMIN` (dossier `v2`).
  - Quatre fichiers sont inchangés, octet pour octet : module commun, surveillance, contrôle à cinq minutes, banc de la surveillance.
  - Plus aucune ligne d'aucun des treize scripts ne lit `docs/procedures/P3-premier-test-v1`.
  - `bash -n` passe sur les douze scripts, et le module commun s'analyse sans erreur.
  - Aucune adresse de ligne en dur ne vise ces scripts : la ligne ajoutée ne décale rien d'utile.
- **(3) Artefacts du texte.** J'ai rejoué, sur des copies du candidat 4, le `sed` de chaque cas qui touche le texte :
  - contrôles : A06, A06b, A07, A11, A13, A13b, A22, A22b, A23, A24, A26b, A44b, A44j, A44k et A44l ;
  - scellement : S22, S23, S23b, S24, S24b, S25, S35 et S35b ;
  - A26b et S22 ont été joués pour chacun des cinq rapports de la famille.
  Chaque artefact est fabriqué ; A44l retire bien la phrase. Témoin : le même `sed` sur le candidat 3 ne fabrique pas A44l, comme au banc officiel. Les outils d'essai sont dans `c4/` (`verifier_cas.py`).
- **(4) Formes et gardes.**
  - Les 22 valeurs du bloc 9 sont présentes (constantes du brouillon 4).
  - Les cinq rapports de la famille sont cités avec leur empreinte ; les neuf intitulés figurent une fois chacun.
  - `problemes()` est vide et il ne reste aucun crochet.
  - Gardes de citation du lanceur : entropie citée, 240 épisodes. Module commun sur les registres de `13d2f64` : conforme.
- **(5) Effets du changement de dossier.** Tout se tient, si les copies, les journaux et le journal de la répétition sont versés sous `v2`.
  - La récupération compare sa copie à `S:docs/procedures/P3-premier-test-v2/recuperation_p3_v1.sh`.
  - La répétition jouet verse la copie des gardes réelles sous `v2` dans son dépôt d'essai.
  - La répétition finale lit `v2`.
  - Le scellement lit `v2`, avec `REPETITION_JOUET_CHEMIN` sous `v2` : il exige le journal de la répétition sous ce dossier (l. 51).
  - Le lanceur compare les scripts du bloc-notes aux copies de `v2`.
  - Les contrôles lisent `v2`.
  - Les copies abandonnées sous `v1` ne peuvent pas servir par erreur : un ancien lanceur comparerait le bloc-notes, refait avec le brouillon 4, aux copies de `v1`, et s'arrêterait.
  - La ligne « Lancement » n'est lue que pour `PREREG` et `BRANCHE` (contrôles l. 201).
  - La répétition jouet doit être refaite avec les scripts du brouillon 4 et le candidat 4, car son journal nomme les deux scripts répétés et le candidat.

**Constats** : aucun bloquant, aucun majeur, aucun mineur, trois pour information.
- **VE4-01, pour information.** l. 469-473 : le brouillon 4 est dit « égal au brouillon 3 … sauf le dossier des copies versées et le chemin du candidat relu des contrôles ». Il porte aussi une ligne de commentaire en tête de chacun des neuf scripts changés ; le traitement et R-227 le disent. Correction possible : ajouter « et une ligne de commentaire en tête des neuf scripts changés ».
- **VE4-02, pour information.** l. 114-118 : le paragraphe « Changements depuis le candidat 3 » ne nomme pas la nouvelle entrée « Premier banc officiel des contrôles » (l. 552-555). C'est le même oubli que VE3-02.
- **VE4-03, pour information.** Deux valeurs du bloc 9 restent coupées par un retour à la ligne (l. 336-337), comme depuis le candidat 1 : « 10 pour chacune des trois indications » et « 52 jetons pour les trois consignes sur 56 tâches et 51 sur 4 ». Le bloc 9 les trouve, car il lit le texte aux espaces réduites, et aucun cas des bancs ne les vise par un `sed`. Un futur cas qui les viserait ligne par ligne rencontrerait le défaut d'A44l.

**Non vérifié** : la répétition jouet en cours avec le candidat 4 (je ne l'ai pas lue, comme demandé) ; les bancs et la répétition finale à rejouer sur les copies de `v2` ; le versement de ces copies.

**Jugement : versable.** La phrase tient sur une ligne : l'artefact A44l est fabriqué, et tous les autres cas du texte le sont aussi. Le brouillon 4 ne change que le dossier, une ligne de commentaire par script et le chemin du candidat, sans garde cassée. Les trois constats, pour information, ne changent ni une règle ni un nombre.
