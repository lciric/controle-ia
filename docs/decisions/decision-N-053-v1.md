# Décision — N-053 : les cinq propositions de l'audit défensif sont acceptées (v1)

- **Décision de Lazar**, mot direct dans la session, le 26 octobre 2026 vers 11:15 UTC, en réponse au message qui
  présentait les cinq propositions de l'audit (`docs/notes/audit-controle-v1/audit-litterature-v1.md`, `29b32f62…`,
  section (c) ; R-508), verbatim : « Les cinq propositions qui te reviennent : : accepté ».
- **Transcription** par la lignée « session-depot », le 26 octobre 2026 vers 11:20 UTC. Numéro attribué à
  l'inscription : N-053. Cette note remplace `decision-N-047-v1.md` (même contenu), numérotée N-047
  par erreur : N-046 à N-052 sont déjà proposés par « conv-audit » sur `canal/conv-audit-n04` (R-510). L'ancienne note
  reste archivée telle quelle (R12).
- **Portée** : cette note fixe la lecture du programme pour les préenregistrements à venir (G1, papier C, phase 1), en
  attendant une version nouvelle du programme ; `docs/programme-controle-ia-v2.md` n'est pas modifié. Aucun
  préenregistrement scellé n'est modifié. Les points qui demandent une dépense restent soumis à un devis et à un GO de
  type « calcul » ; l'acceptation porte sur le principe.

## Énoncés retenus, dans les options recommandées par l'audit

1. **Bras « fuite textuelle et contrôlabilité »** dans les préenregistrements de G1 et du papier C, avant leur
   scellement (option (a)) : deux bras rapportés, qui ne servent pas de critère :
   - la lecture de chaque sonde sur toutes les positions, puis avec les positions porteuses d'évidence textuelle
     masquées ; la lecture filtrée est la lecture principale de toute revendication d'« intention » ;
   - la condition « suppression consignée » du banc publié (2608.21664), reprise telle quelle, par direction de sonde du
     programme, avec une direction aléatoire de même variance pour témoin ; métrique : détection à 1 % de faux positifs.
2. **Famille d'organismes (iv)**, dont la politique de sabotage est apprise sans texte de consigne : d'abord un réglage
   fin léger sur documents synthétiques qui décrivent la politique (méthode publiée, 2510.20487), puis une récompense
   sur le résultat du sabotage si la première voie tient (options (a) puis (b)). **Dépense : devis et GO avant tout
   calcul.** La prédiction de validité est étendue : une sonde d'intention réussit sur (ii) et sur (iv).
3. **Mesure de la conscience d'évaluation du dispositif** avant d'interpréter H8 et les contrôles croisés (option (a)) :
   - une porte de validité format × contexte décorrélé pour la sonde de conscience d'évaluation, Devbunova (2026)
     citée comme instrument et non comme revendication ;
   - une mesure du réalisme de l'environnement (a) ;
   - les mêmes épisodes avec et sans marqueurs de test, et un test causal avec une direction placebo ;
   - à coordonner avec le nœud H-M1 (R-503).
4. **Juge d'une autre lignée et contrôle d'échelle** :
   - tout de suite, un juge Qwen2.5-7B en bras rapporté (option (c) de D1) et une porte préalable de séparabilité de la
     tromperie à 8 milliards de paramètres sur une tâche à résultat vérifiable (option (b)) ;
   - au devis de la phase 1, un sous-ensemble des lectures décisives à plus grande taille (option (a)) : changement de
     modèle et dépense, GO à part (R-502).
5. **Deux invariants de la section 9 testés, et une règle écrite** (option (a)) :
   - un test de récupération après réentraînement des sondes dans E1.5 (b), contre la réserve de détecteurs ;
   - deux règles de sélection déclarées dans E1.6 : ré-échantillonnage uniforme, et choix du moins suspect avec un bras
     qui vise le moniteur ;
   - **invariant nouveau** : aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection
     de l'agent, hors bras d'attaque déclaré ; il vaut aussi pour la piste « organisme » (N-045) ; gardé par le code
     (R5 : testé sur un cas sain et sur un artefact).

## Ce qui ne change pas

- Les hypothèses H1 à H9 et leurs énoncés retenus (N-003 à N-045) ; les critères des portes ; les règles gelées.
- Les dépenses : chaque point payant passe par un devis et un GO.
