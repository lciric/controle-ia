# Devis de la course 2 avec Kimi — juges Kimi et Argon, notation croisée — v2

Lignée session-depot (instance 2), 30 octobre 2026. **Rien n'est lancé.** Ce devis est un nœud de dépense ; chaque lancement aura sa ligne de GO.

Il remplace, pour la course 2, le bras B du devis comparé v1 (`devis-course-2-claude-contre-kimi-v1.md`, `c0620cb6…`), qui reste archivé sans modification. Il prend en compte :
- **R-813** : course 2 avec Kimi K3.1 Pro comme proposeur, Argon toujours proposeur, plafond 110 USD, pré-pilote d'abord ;
- **R-571 et R-572 de conv-audit** :
  - au pré-pilote, les juges sont **Kimi K3.1 Pro et Argon** ; Claude est retiré « pour l'instant » ;
  - **notation croisée** : chaque fiche est notée par le juge de l'autre fournisseur. Les fiches de Kimi sont notées par Argon, celles d'Argon par Kimi ;
  - l'**auto-préférence** se mesure sur des **témoins plantés des deux sources**.

Le devis suppose que ces juges restent ceux de la course. Si le pré-pilote les écarte, le devis de la course est refait.

## 1. Bases

**Prix** (inchangés depuis la v1)
- Kimi K3.1 Pro : 2,00 USD par million de jetons d'entrée et 10,00 en sortie. Vérifiés le 30 octobre sur `platform.kimi.ai/docs/pricing/chat` (page `c62210a0…`).
- Opus 5.5 : 4 / 20 USD. Kimi coûte donc **exactement la moitié** d'Opus, en entrée comme en sortie.

**Coûts observés** (`registres/depenses.md`)
- Course 1, tentative 2 : Argon proposeur **6,00 USD**, plus **1,75 USD** de contrôles.
- Juges sur les **29 fiches** (fin de GO-2026-10-30-05) : Opus 5.5 **3,31 USD**, Argon **2,28 USD**. Chaque juge a noté toutes les fiches.

**Coûts par fiche notée**, déduits de ces chiffres
- Argon : 2,28 / 29 = **0,079 USD**.
- Kimi : **0,057 USD**. C'est le coût d'Opus par fiche (3,31 / 29) divisé par deux, à jetons égaux (**SUPPOSÉ**).
- **Pire cas**, deux facteurs :
  - facteur 1,34 sur les deux juges, le rapport 7,5 / 5,6 du devis v1 ;
  - facteur 2 de plus sur Kimi, pour ses jetons de raisonnement, la même prudence que pour Kimi proposeur au v1.
  - D'où **0,105 USD** par fiche pour Argon et **0,153** pour Kimi.

**Proposeurs, par sous-session** (inchangés depuis le devis v1, § 3 et 4, **SUPPOSÉ**)
- Kimi : 2,5 USD attendus, 9,5 au pire.
- Argon : 4,5 USD attendus, 6 au pire.
- Une sous-session, c'est 2 passes de 8 fiches, soit **16 fiches par proposeur**.

## 2. Notation croisée et témoins

**Fiches de la course** : chacune est notée **une fois**, par le juge de l'autre fournisseur.

**Témoins plantés** : leur qualité est fixée à l'écriture (défauts plantés connus). Chacun est noté **par les deux juges**.

**Auto-préférence** : c'est une différence de différences, sur des témoins de qualité plantée appariée.
- Pour chaque juge, on calcule son écart entre les témoins de sa source et ceux de l'autre source.
- L'auto-préférence est la différence entre les écarts des deux juges.
- La même grille mesure aussi l'écart de sévérité entre les deux juges.

**Pourquoi c'est nécessaire** : en notation croisée, la source et le juge sont confondus. Un juge plus sévère ferait paraître sa source d'en face plus faible. Seuls les témoins notés deux fois séparent ces deux effets.

**Effectifs (SUPPOSÉ, à fixer dans le pré-pilote scellé)**
- Pré-pilote : **12 témoins par source**, soit 24 témoins, chacun noté deux fois.
- Course : **4 témoins par source et par sous-session**, soit 8 par lot, chacun noté deux fois.

## 3. Pré-pilote (recalculé)

| Poste | Attendu | Pire |
|---|---|---|
| Témoins écrits par Kimi (12 fiches, soit 12/16 d'une sous-session) | 1,9 | 7,1 |
| Témoins écrits par Argon (12 fiches) | 3,4 | 4,5 |
| Notation des 24 témoins par les deux juges | 3,3 | 6,2 |
| Épreuve courte de la chaîne Kimi ; étalonnage de la garde de niveau méthode sur Kimi (repris du v1) | 2,5 | 4,0 |
| Essai d'un appel (`essai_kimi_v1.sh`, plafonné à 0,5 USD par le relais) | ≈ 0 | 0,5 |
| **Total pré-pilote (USD)** | **≈ 11** | **≈ 22** |

Le v1 comptait 7 USD attendus et 10 au pire, sans écrire de témoins des deux sources ; l'option (a) du v1 bornait le pré-pilote à 15 USD. **Le pire cas recalculé dépasse cette borne.**

## 4. Course (recalculée, 4 sous-sessions)

**Juges, par sous-session**
- 16 fiches de Kimi notées par Argon : 1,26 USD (1,69 au pire).
- 16 fiches d'Argon notées par Kimi : 0,91 USD (2,45 au pire).
- 8 témoins notés par les deux juges : 1,09 USD (2,07 au pire).
- Total : **3,26 USD** par sous-session (**6,20** au pire).

| Poste | v1, B attendu | v1, B pire | **v2 attendu** | **v2 pire** |
|---|---|---|---|---|
| Kimi proposeur (4 sous-sessions) | 10 | 38 | 10 | 38 |
| Argon proposeur (4 sous-sessions) | 18 | 24 | 18 | 24 |
| Contrôles d'Argon | 1,75 | 3 | 1,75 | 3 |
| Juges | 22 (Opus et Argon, tout noté deux fois) | 30 | **13** (croisés, témoins notés deux fois) | **25** |
| **Course (USD)** | ≈ 52 | ≈ 95 | **≈ 43** | **≈ 90** |
| Pré-pilote | 7 | 10 | 11 | 22 |
| Coûts propres à B (passés dans le pré-pilote en v2) | 2,5 | 4 | — | — |
| **Total (USD)** | **≈ 61** | **≈ 109** | **≈ 54** | **≈ 112** |

**Ce qui change**
- La notation croisée **divise par deux environ le coût attendu des juges** (13 contre 22 USD).
- Au pire, l'économie se réduit (25 contre 30 USD), parce que le pire cas double les jetons de Kimi.
- Le pré-pilote coûte plus cher, parce qu'il écrit des témoins des deux sources.
- **Le pire cas total, ≈ 112 USD, dépasse le plafond de R-813 (110 USD) d'environ 2 USD.** Le séquençage tient quand même le plafond :
  - les relais sont plafonnés par lancement ;
  - la course n'est lancée que si le devis, refait avec les mesures du pré-pilote, tient dans le reste du plafond.

## 5. Réserves

- **Pose de la clé.**
  - conv-audit demande un script à saisie masquée, que Lazar lancerait lui-même dans cette session.
  - Ce chemin n'existe pas ici. Dans une session cloud, Lazar n'a pas de terminal interactif. Une commande lancée depuis la conversation, saisie comprise, finit dans la transcription.
  - **Chemin retenu (R-814)** : la variable `KIMI_API_KEY`, posée par Lazar dans les réglages de l'environnement, puis lue par une **session neuve**.
  - Les scripts n'en vérifient que la présence, par son nom. Ils la transmettent aux processus Python par l'environnement d'un sous-shell vidé de toute autre variable, jamais en argument, en fichier ou en journal. `essai_kimi_v1.sh` cherche la clé dans ses journaux avant de les sceller.
  - La clé collée en R-812 reste dans la transcription de la conversation. Lazar assume ce risque (R-814). Un plafond de dépense sur la clé, dans la console Moonshot, reste recommandé.
- **Confidentialité, chemin nouveau par rapport au v1** : Kimi juge les fiches d'Argon.
  - Les sorties d'Argon partent donc chez Moonshot, y compris celles de l'axe 6, qui vivent sur `donnees/course-2-axe-6-sorties-v1`.
  - Au v1, seul le texte servi à Kimi y partait (bras avec pistes, R-568).
  - À confirmer par Lazar avant le pré-pilote.
- **Notation croisée**
  - Chaque fiche n'a qu'un juge : aucun accord entre juges n'est mesurable sur les fiches de la course, seulement sur les témoins.
  - Le classement entre sources dépend de la correction de sévérité estimée sur les témoins. Avec 8 témoins par lot, cette correction est imprécise. Le pré-pilote dira si les effectifs suffisent.
- **Claude retiré « pour l'instant »** : un retour de Claude comme juge refait le devis des juges. Chaque fiche alors notée par Opus 5.5 coûte 0,114 USD.
- **Identifiant du modèle** : l'identifiant exact de Kimi K3.1 Pro n'est pas encore lu (`kimi-k3.1-pro` n'est qu'un nom d'essai). `essai_kimi_v1.sh` le vérifie dans `GET /v1/models` avant tout appel, et lit le modèle servi et le coût d'un appel.
- Toutes les hypothèses marquées **SUPPOSÉ** sont à remplacer par les mesures du pré-pilote, et le devis de la course est refait avant son GO.

## 6. Décision pour Lazar (nœud de dépense)

**Décision** : comment tenir le plafond de 110 USD, maintenant que le pire cas recalculé est d'environ 112 ?

**Enjeu** : les juges croisés font baisser l'attendu (≈ 54 contre ≈ 61 USD). Le pire cas, lui, monte d'environ 3 USD, à cause des témoins des deux sources au pré-pilote.

**Options**
- **(a) Garder 110 USD, séquencé.** Le pré-pilote est plafonné à 22 USD ; la course est lancée seulement si son devis refait tient dans le reste. Avantage : rien ne change dans R-813. Inconvénient : la course pourrait devoir être réduite si le pré-pilote mesure le pire.
- **(b) Monter à 115 USD.** Avantage : couvre le pire cas recalculé avec une marge. Inconvénient : engage 5 USD de plus pour un cas peu probable.
- **(c) 8 témoins par source au pré-pilote, au lieu de 12.** Le pire baisse d'environ 6 USD, pour un total d'environ 106. Avantage : tient sous 110 sans séquençage serré. Inconvénient : la mesure d'auto-préférence est moins précise.

**Recommandation** : (a), confiance 0,6. Le pire cas suppose que Kimi consomme le double à la fois comme proposeur et comme juge. La mesure du pré-pilote le confirmera ou l'écartera avant que la course ne s'engage.
