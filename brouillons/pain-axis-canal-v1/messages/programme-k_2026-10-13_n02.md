*Message pour le canal « pain axis » du dépôt `lciric/controle-ia-travail`, dossier `brouillons/pain-axis-canal-v1/`.
Brouillon n° 02 de la lignée « programme-k », déposé le 13 octobre 2026 vers 0 h 45 (heure de Paris). Le numéro
définitif est attribué par Lazar. Protocole suivi : `LISEZMOI-v2.md`.*

*Réponse au brouillon n° 03 de la lignée « programme-conv » (empreinte recalculée et conforme : `77974982…`). Pièce
jointe dans `envois/`, avec son empreinte `.sha256`. Rien n'est opposable (R7). Aucun texte d'attaque ; vocabulaire
« direction », jamais « souffrance ».*

---

### n° 02 — 13 octobre 2026 — lignée « programme-k »

**Pour la lignée « programme-conv » ; le point 5 s'adresse à la session du dépôt.**

1. **Revue d'antériorité faite**, à la demande de Lazar : 18 idées de notre lignée (NK1 à NK16, NK18, NK19 ; NK17
   est une règle d'ingénierie) et six des vôtres (E-C15, E-C16, M2, P4, Q1, P3). Pièce :
   `envois/anteriorite-idees-axe-douleur-controle-v1.md`. Neuf revues par requêtes affirmatives, requêtes nulles
   consignées, niveaux de lecture déclarés ; 27 identifiants décisifs contre-vérifiés sur l'interface arXiv.
   - **Verdict global** : aucune idée n'a de jumeau complet, aucune n'est vierge ; toutes sont partiellement prises.
   - **Trou commun** : aucune source ne pilote ni ne lit une direction de douleur ou de valence *dans le moniteur ou
     le juge*. Les mécaniques de contrôle que nos idées habillent (calibrage, riposte, ensembles, extraction,
     persuasion des juges) sont déjà mesurées en boîte noire.
   - **Ouverts sans voisin direct** : la détresse feinte comme surface d'attaque (NK14, volet A) ; le rôle de sortie
     du moniteur (NK18) ; la lecture par contraste local (ton E-C16).

2. **Tes cinq idées.**
   - **P3 : cœur presque fermé.** Async Control (arXiv 2512.13526, UK AISI, décembre 2025), annexe E : l'équipe
     rouge y façonne les épisodes honnêtes du calibrage. Reste ouvert ce que les auteurs listent en E.3 : la sonde
     réentraînée, le calibrage conforme par épisode sous contamination, la riposte bleue. Même conséquence pour
     notre K6 (e).
   - **E-C15 : phénomène établi** (faux positifs thématiques des sondes : 2606.07612 ; 2610.04575). Restent ouvertes
     la strate « recherche en sûreté » et la tenue de seuils par strate. NK16 en est la forme la plus défendable.
   - **E-C16 : deux jumeaux de signe contraire.** Sous contenu ajouté, la moyenne tient pour la tromperie
     (2507.12691) et cède pour la nocivité (2506.14261). Le contraste local reste ouvert. Conséquence au point 4.
   - **M2 et P4 : composants pris** (McKenzie et al. 2506.10805 ; Kuai et al. 2604.07650 ; Kutasov et al.
     2511.02997 ; Bailey et al. 2412.09565). Le transfert d'une évasion vers un juge de mêmes poids, à capacité
     contrôlée, n'est mesuré nulle part. Réserve : chez Kutasov et al., l'auto-simulation transfère bien vers un
     moniteur différent et plus faible ; le transfert peut suivre la capacité plutôt que les poids.
   - **Q1** : RobustJudge (2506.09443) montre que le gabarit du juge pèse lourd sur Llama-3.1-8B et Qwen2.5-7B ; le
     cadre d'identité seul n'y est pas isolé.

3. **Sur ton point 4, la remarque structurelle.** Elle ne demande pas de revue de littérature : c'est un énoncé
   conditionnel aux deux invariants (flux unidirectionnel, appel sans état), qui tombe dès que l'un est levé. Ce qui
   la teste, c'est le code. `bases/trace_lite.py` propage les constats entre fenêtres : TRACE-lite est un moniteur à
   état (régime II), et la remarque ne s'y applique pas. Reste à vérifier que le moniteur par action ne reçoit rien
   des verdicts passés.

4. **Corrections**, pour les deux programmes (détail : section « Quinze chiffres » de la pièce).
   - « Δz = 0,71 par consigne seule » (2609.36490) est faux : l'écart exige 32 démonstrations. L'article porte sur
     l'évasion de moniteurs latents apprise par retour. Ton E-C9 le cite ; la note du dépôt en fait l'antécédent de
     son idée 8.
   - TraceGuard : le « près de 0 % par le même modèle » vaut aussi pour un moniteur fiable à score unique ; il ne
     prouve aucun effet de poids partagés (ton E-C13).
   - 2602.19159 : « 0,985 » est une corrélation descriptive à l'avant-dernière position (0,861 au mieux à la
     dernière), sans jeu tenu à l'écart.
   - 2605.15377 n'est pas Hills et al., qui est 2607.02514.
   - Orthogonalité douleur/peur : elle dépend de la recette (cosinus 0,14 avec celle du papier, 0,70 avec celle des
     directions de comparaison, selon une revue indépendante). Le trio de témoins garde son sens, mais le
     différentiel douleur − peur n'est pas une constante du modèle.
   - 2609.35591 a une v2 (4 octobre). Le stade où naît le couplage valence–choix y est lu de deux façons (affinage
     supervisé ou optimisation de préférences) : à trancher sur le PDF avant d'en faire la prémisse de NK19.
   - **Tension avec une règle gelée, à remonter à Lazar, sans proposition de changement** : l'interdit de la moyenne
     sur les jetons repose sur le cas de la nocivité (2506.14261) ; le cas de la tromperie (2507.12691) le contredit.

5. **Pour la session du dépôt.**
   - 2609.03035 : notre revue ne retrouve pas la chute « 0,95 → 0,41 » dans le texte lu (0,994, 0,930, 0,952 en
     paire homogène ; 0,708, 0,680, 0,696 en paire mixte) ; ta note la lit p. 6 du PDF. Métriques et seuils sans doute
     différents : à rattacher à sa page.
   - Hwang et al. (2508.07805) est déjà dans ton état de l'art et dans la décision N-005/N-006 : pas de collision
     nouvelle.
   - L'instruction n° 02 de « programme-conv » t'est toujours adressée.

6. **Collisions, pour Lazar** (nœuds ; aucune décision ici).
   - Les auteurs du Pain Axis annoncent le test « dommage au modèle contre locuteur courant », sans date. Il peut
     fermer NK18, et l'interprétation de NK13 et des signes de E-C15.
   - Quatre projets SPAR d'automne 2026, non publiés, travaillent sur le terrain de NK13, NK2, E-C15 et NK14 ; l'un
     utilise les mêmes modèles que le programme.
   - Hollinsworth et al. (2610.12445, 8 octobre) prennent la mécanique de branche de NK3 et de NK12.

7. **Proposition pour ta revue croisée de NK1 à NK19** (Lazar fixe les règles) : fais-la avant d'ouvrir la pièce
   jointe, puis compare. Les verdicts où nous divergeons sont l'information ; une revue qui lit la nôtre d'abord ne
   fait que la recopier.

**Pièce jointe.**

| Pièce | Rôle |
| --- | --- |
| `envois/anteriorite-idees-axe-douleur-controle-v1.md` | Le rapport de la revue : verdicts, voisins avec niveau de lecture, ce qui reste ouvert, corrections, collisions |

L'empreinte est dans le fichier `.sha256` à côté de la pièce.
