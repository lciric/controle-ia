# Devis v1 — course d'idéation de l'organisme sur la question scellée v2 du pilier attaque

Écrit par la fille idéation 1 `session_016QhUrujoj3FTuFNoYshNYB`, branche `rapports/fille-ideation-1-v1`, le 8 novembre 2026 vers 16:45 UTC. **Aucune dépense engagée par ce devis** : la course part sur une ligne de GO de la mère (après attestation de la synthèse v2b) et sur le mot écrit de Lazar. Base : coûts réels de la fille idéation 2 (GO-2026-11-08-08, 8,42 USD), devis v2 et v3 de la mère, et tailles mesurées de la question v2 et de la synthèse v2b.

## 1. Ce qui est mesuré (zéro dollar avant la sonde)

- **Mesure des consignes** (`ideation_v8.py --mesurer-consignes`, sans appel, sans écriture). À exécuter après l'attestation de la synthèse v2b par la mère ; estimations ci-dessous à partir des tailles brutes :
  - Question v2 : 24 142 caractères (`2dbad4b7…`).
  - Pièce et pièce-juge (synthèse v2b, `<empreinte à sceller>`) : ≈ 33 300 caractères.
  - **Consigne de passe 1 estimée : ≈ 60 000 caractères** (v1 : 16 856) ; consigne de passe 2 réaliste (fiches de 4 000 caractères) : ≈ 92 000 (v1 : 49 000) ; consigne de passe 2 maximale : ≈ 414 000 (v1 : 371 000).
  - Garde de course (`passerait`) : à vérifier avec les tailles réelles. Garde de passe 2 d'Argon : le plafond maximal théorique est plus élevé qu'en v1 ; le test au réaliste (fiches ≤ 8 000) est celui qui compte.
- **Passe simulée complète** (`--moteur simule`, graine 20261109) : à exécuter. Attendu : code 4 (témoins échoués chez les juges scriptés ; identique au v1).
- **Témoins plantés** : les témoins v1 (`temoins-pilier-attaque-v1.json`, `7db0d82b…`) peuvent être réutilisés si la mère les atteste valables pour la question v2 ; sinon, rédaction de témoins v2 par la mère (ni proposeur ni juge).
- **Sonde réelle de la garde refus-question** (R-1788) : trois modèles (Opus 5.5, Fable 5.1, Argon) ; ≈ 0,005 USD. Un modèle qui refuse est retiré de **tous** les rôles, sans reformulation.

## 2. Barème et hypothèses

Barème du noyau (USD par million de jetons, entrée / sortie) :
- **Opus 5.5 : 4 / 20**
- **Fable 5.1 : 10 / 50**
- **Argon (gemini-4-argon)** : par commande externe ; 0,53 USD par passe mesuré sur la fille 2 (v1) ; le coût par passe sur la v2 est plus élevé en raison de l'entrée plus grande.

Entrée : jetons ≈ caractères / 4.
- Passe 1 v2 : ≈ 15 000 jetons d'entrée (v1 : 4 200).
- Passe 2 v2 réaliste (fiches ≤ 4 000 caractères) : ≈ 23 000 jetons (v1 : 12 300).
- Sortie d'une passe : 8 fiches × 3 000 caractères ≈ 6 000 jetons (inchangé).
- Juge : ≈ 30 fiches + 4 témoins + pièce-juge ≈ 168 000 caractères ≈ 42 000 jetons d'entrée (v1 : 36 500), ≈ 3 000 de sortie.

## 3. Coût attendu

### 3.1 Coûts théoriques par session (v2)

| Poste | Calcul | USD |
|---|---|---|
| Proposeur Opus 5.5, deux passes | (15 000·4 + 6 000·20 + 23 000·4 + 6 000·20) ·10⁻⁶ | 0,39 |
| Proposeur Fable 5.1, deux passes | (15 000·10 + 6 000·50 + 23 000·10 + 6 000·50) ·10⁻⁶ | 0,98 |
| Proposeur externe Argon, deux passes | 2 × 0,80 (estimé, entrée ≈ 3,5× celle du v1) | 1,60 |
| Juge Opus 5.5 | (42 000·4 + 3 000·20) ·10⁻⁶ | 0,23 |
| Bras rapporté différé, juge Argon | un appel long (entrée plus grande) | 1,00 |
| Contrôles (5) et sonde (3) | | 0,05 |
| **Total théorique, Fable acceptée** | | **≈ 4,3** |
| **Total théorique, Fable refusée** | retire proposeur Fable | **≈ 3,3** |

### 3.2 Coûts réels de la fille 2 (v1, sans Fable) et facteur d'échelle

La fille 2 (GO-2026-11-08-08) a mesuré un coût total de 8,42 USD pour la séquence complète (sonde + course + bras), dont une part significative (≈ 3,80) de tentatives avortées (refus de Fable, panne de l'amont Google). La mère décompose la séquence utile :
- Course Claude (toutes tentatives) : ≈ 2,80 USD.
- Course externe (run réussi seul) : 1,05 USD.
- Bras (b) juge Argon : 0,77 USD.

L'écart entre le théorique v1 (1,95 USD sans Fable, devis v2) et le réel (2,80 + 1,05 + 0,77 = 4,62 USD) provient de la plomberie de l'orchestrateur (classification, validation, contrôles de témoins, manifestes) et des tentatives échouées.

**Facteur d'échelle v2** : l'entrée combinée (question + pièce) passe de ≈ 14 400 caractères (v1) à ≈ 57 100 (v2), soit un facteur 4,0× sur l'entrée brute. L'impact sur le coût total est modéré parce que la sortie (inchangée) domine le coût des modèles chers (50 USD/Mtok pour Fable, 20 pour Opus).

### 3.3 Coût attendu pour la course v2

| Poste | Base fille 2 (v1) | Facteur v2 | USD v2 |
|---|---|---|---|
| Course Claude, Opus (proposeur + juge + orchestrateur) | 2,80 | ×1,15 | 3,22 |
| Proposeur Fable, deux passes (théorique v2) | — | — | 0,98 |
| Course externe, Argon proposeur (2 passes) | 1,05 | ×1,50 | 1,58 |
| Bras (b) juge Argon | 0,77 | ×1,30 | 1,00 |
| Sonde + contrôles | 0,04 | — | 0,05 |
| **Total attendu, Fable acceptée** | | | **≈ 6,8** |
| **Total attendu, Fable refusée par la sonde** | | | **≈ 5,8** |

Hypothèses des facteurs : 15 % d'augmentation Claude (sortie domine, entrée est 30 % du coût Claude) ; 50 % d'augmentation Argon proposeur (entrée est 40 % du coût Argon, ×4,0 sur l'entrée) ; 30 % d'augmentation bras Argon (synthèse-juge plus longue, fiches inchangées). Les facteurs sont prudents par excès.

## 4. Pire cas et plafond proposé

- Plafonds par session Claude (inchangés par rapport au devis v3) : proposeurs Opus 5.5 et Fable 5.1 **2,0** USD chacun ; juges Opus 5.5 **1,5** ; total Claude `--budget-total-usd 12.0`.
- Plafonds externes : Argon proposeur 2 × 2,0 ; Argon juge 2,5 ; contrôle externe 1,35 ; total externe `--budget-externe-usd 8.0` (somme des plafonds : 7,85 ≤ 8,0).
- **Plafond proposé : 20 USD** = Claude 12,0 + externe 8,0. Marge sur l'attendu : ≈ 2,9× (Fable acceptée) ou ≈ 3,4× (sans Fable). Identique au GO de la fille 2.
- Risques chiffrés : refus de Fable à la sonde (−0,98 USD, pas de juge Fable prévu) ; fiches de passe 1 au-dessus de 8 000 caractères → passe 2 d'Argon refusée avant appel ; juge Argon sans réponse → classement à un juge Claude « sans juge externe » (code 5) ; panne de l'amont Google → reprise par le collisionneur (la fille 2 a subi un amont coupé, coûté 2,15 au pire cas).

## 5. Commandes (fille idéation 1, après la ligne de GO et le mot de Lazar)

Préalables : relais de clé du noyau lancé avec `--modeles-permis` **exactement** égal aux modèles Claude de la course (`claude-opus-5-5,claude-fable-5-1`, ou `claude-opus-5-5` seul si Fable refuse) ; commande externe d'Argon (enveloppe locale, sans `sudo`, sans utilisateur système, cf. devis v3) ; liste blanche reconstruite (`--construire-liste-blanche` : question v2, synthèse v2b, témoins) ; `GEMINI_API_KEY_2` jamais ; relais Gemini v2 avec `GEMINI_API_KEY` (jamais `_2`).

1. **Sonde réelle de la garde** : `PYTHONPATH=src python -I -m controle_ia.garde_refus_question_v1` sur les trois modèles (Opus, Fable, Argon) ; bilan JSON scellé ; retirer tout modèle qui refuse de **tous** les rôles.
2. **Course (a)** : `python -I -B demonstrations/ideation_v8.py SORTIE --liste-blanche L.json --question question-pilier-attaque-v2.md --piece synthese-anteriorite-pilier-attaque-v2b.md --piece-juge synthese-anteriorite-pilier-attaque-v2b.md --temoins temoins-pilier-attaque-v1.json --proposeur opus=claude-opus-5-5 [--proposeur fable=claude-fable-5-1] --proposeur-externe argon=gemini-4-argon --commande-externe "bash <enveloppe locale>" --juge opus-juge=claude-opus-5-5 --juge-externe argon-juge=gemini-4-argon [--seconde-passe] --nombre 8 --budget-total-usd 12.0 --budget-externe-usd 8.0 --budget "proposeur_ideation|claude-opus-5-5=2.0" [--budget "proposeur_ideation|claude-fable-5-1=2.0"] --budget "juge_ideation|claude-opus-5-5=1.5" --moteur claude-sdk --url-relais http://127.0.0.1:PORT --confirmer-moteur-reel --horodatage "$(date -u)"` — crochets retirés si Fable refuse la sonde ; `--seconde-passe` retiré si l'attestation de matériau est exigée par le lanceur.
3. **Lecture humaine attestée** des fiches validées (la mère ou Lazar), scellée.
4. **Bras (b)** : `… SORTIE --bras-rapporte-differe --attestation-lecture-humaine ATT.json --juge-externe argon-juge=gemini-4-argon --commande-externe "…" --liste-blanche L.json` → classement à deux juges (Opus et Argon).
5. Après la course : relecture « aucune recette » de **toutes** les fiches validées par la mère avant tout usage (R-607).

### Différences par rapport aux devis v2/v3 de la mère (question v1)

| Point | Devis v2/v3 (v1) | Ce devis (v2) |
|---|---|---|
| Question | v1 (`29870ac9…`, 4 255 car.) | v2 (`2dbad4b7…`, 24 142 car.) |
| Pièce/pièce-juge | synthèse v1 (`48adeac0…`, 10 151 car.) | synthèse v2b (`<à sceller>`, ≈ 33 300 car.) |
| Proposeurs Claude | Opus, Fable | Opus, Fable (identique) |
| Juges Claude | Opus, Fable | **Opus seul** (pas de Fable juge) |
| Juge Argon plafond | 2,5 | 2,5 (identique) |
| Contrôle externe plafond | 1,35 | 1,35 (identique) |
| Coût attendu avec Fable | 3,2 | **6,8** |
| Coût attendu sans Fable | 1,9 | **5,8** |
| Plafond | 20 | 20 (identique) |

## 6. Pièces de ce devis

- `question-pilier-attaque-v2.md` (`2dbad4b75d20fadc3147be9eff07f2e77c2f82fe4f609ab1c29388ab46c4bb42`)
- `synthese-anteriorite-pilier-attaque-v2b.md` (`<empreinte à sceller>`) — après attestation de la mère
- `temoins-pilier-attaque-v1.json` (`7db0d82b…`) — sous réserve d'attestation v2 par la mère
- `ideation_v8.py` (`2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1`) — dépôt public `lciric/ideation-organism`, commit `8947bc8`
- `mesurer-consignes-pilier-attaque-v2-v1.json` — à produire après attestation
- `passe-simulee-v2-v1/` — à produire

## 7. Ce qui manque

1. **Attestation de la synthèse v2b** par la mère (« aucune recette »). Bloque la mesure des consignes et la passe simulée.
2. **Confirmation des témoins v1** pour la question v2, ou rédaction de témoins v2 par la mère.
3. **Mesure réelle des consignes** (`--mesurer-consignes` avec les fichiers v2). Les estimations de la section 2 sont dérivées des tailles brutes ; la mesure réelle peut révéler un dépassement de garde.
4. **Enveloppe Argon** : à écrire (version neuve, R12), même principe que la fille 2 (devis v3, § 2) : aucun `sudo`, aucun utilisateur système, clé factice, relais Gemini v2 avec `GEMINI_API_KEY`.
5. **Ligne de GO** de la mère.
