# Traitement du premier banc officiel des contrôles — chaîne de P3 v1, brouillon 4

- **Constat** : banc officiel des contrôles (`essais_controles_p3_v1.sh` du brouillon 3, joué au commit des préalables
  `be7658d3f36c9e250a0dfe0cf754269bd6aa7586`, 19:08 à 19:41 UTC) : « cas non conformes : 1 ». Le cas A44l
  (« texte sans la borne de stockage ») fabrique son artefact par un `sed` qui travaille ligne par ligne sur le texte de S ; au
  candidat 3, la phrase « stockage au plus 0,03 USD de l'heure » est coupée par un retour à la ligne (l. 344-345) : elle
  n'est pas retirée, les contrôles passent (code 0, 51 OK), et le KO attendu manque. Les contrôles réels lisent le texte aux
  espaces réduites : ils ne sont pas en cause. Les autres cas du banc sont conformes, ainsi que les bancs du lanceur, de la
  surveillance et du scellement (0 non conforme chacun).
- **Cause** : la mise en ligne de la phrase dans le texte (candidat 2, puis candidat 3), non la chaîne.
- **Traitement** (session, R-227) : le texte passe au candidat 4, où la phrase tient sur une ligne. Le journal de la
  répétition jouet et les épingles des contrôles citent le candidat ; ils changent donc. Les copies déjà versées sous
  `docs/procedures/P3-premier-test-v1/` (commit `be7658d`) ne sont pas réécrites (R12) : ce versement est abandonné et gardé
  tel quel, et la chaîne verse ses copies sous `docs/procedures/P3-premier-test-v2/`, comme l'a fait la chaîne des
  notations (`notations-T0.5-v1/` puis `-v2/`).
- **Brouillon 4** : les treize scripts du brouillon 3 (`brouillons/P3-chaine-v1-brouillon3/`, scellé au commit `ffdbcda`),
  dont neuf changent : chaque mention du dossier des copies versées passe de `docs/procedures/P3-premier-test-v1` à
  `docs/procedures/P3-premier-test-v2` (code et commentaires), et une ligne de commentaire est ajoutée après la première ;
  dans les contrôles, le chemin du candidat relu devient `brouillons/P3-premier-test-i-a-v1-candidat4.md`. Inchangés, octet
  pour octet : `verifications_p3_v1.py`, `surveiller_p3_v1.sh`, `controle_cinq_minutes_p3_v1.sh`,
  `essais_surveillance_p3_v1.sh`. Le banc du cas A44l n'est pas changé (le texte corrigé le fait passer).
- **À refaire** : relecture de l'écart (candidat 3 au candidat 4 ; brouillon 3 au brouillon 4) par un sous-agent neuf ;
  répétition jouet au code relu avec le candidat 4 ; épingles ; copies versées sous `docs/procedures/P3-premier-test-v2/` ;
  les quatre bancs ; la répétition finale ; puis le scellement.
