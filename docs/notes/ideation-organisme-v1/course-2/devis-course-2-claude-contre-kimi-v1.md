# Devis comparé de la course 2 — proposeurs Claude (A) contre Kimi K3.1 Pro (B) — v1

Lignée session-depot (instance 2), 30 octobre 2026, relevé `date -u` 08:59. Écrit à la demande de conv-audit (n° 243), après le mot de Lazar relayé en R-567 de conv-audit : « course 2 avec les kimi à la place des claude pour économiser du budget ». **Rien n'est lancé.** Ce devis est un nœud de dépense, sans défaut sous 48 heures.

## 1. Bases

**Prix**
- **Kimi K3.1 Pro**, prix vérifié sur la page officielle `https://platform.moonshot.ai/docs/pricing/chat`, redirigée vers `https://platform.kimi.ai/docs/pricing/chat`. Lue le 2026-10-30 vers 08:58 UTC par `curl`, empreinte de la page `c62210a0…`, gardée dans le dossier de travail temporaire de la session. Ligne `kimi-k3.1-pro` :
  - **2,00 USD par million de jetons d'entrée** ;
  - **10,00 USD par million de jetons de sortie** ;
  - 0,20 USD par million de jetons lus en cache ;
  - écritures en cache à 2,00 et 4,00 USD.
  Le prix de presse « 2 / 10 » est donc confirmé. La variante `-highspeed` coûte le double.
- **Fable 5.1** : 10 / 50 USD le million de jetons. **Opus 5.5** : 4 / 20. Sources : la table `MODELES` du collisionneur v3, et les relais.
- Les prix de Kimi sont **cinq fois plus bas** que ceux de Fable, en entrée comme en sortie.

**Coûts observés** (`registres/depenses.md`)
- Course 1, tentative 2 (l. 250) :
  - proposeur Fable, deux passes : **23,65 USD** (relais) ;
  - Argon proposeur : **6,00 USD**, plus **1,75 USD** d'appels de contrôle ;
  - c'était **une seule question**, avec un gros corpus de pièces (taille maximale 750 000 caractères), et 8 fiches par proposeur et par passe.
- Juges sur les 29 fiches (l. 252) : **3,31 USD** côté Claude (Opus 5.5) et **2,28 USD** côté Argon, soit ≈ 5,6 USD.

**Textes de la course 2**
- Texte I, fusion v5 de conv-audit (`question-course-2-defense-fusion-v5.md`, `a7501449…`) : **11 699 caractères** servis.
- Texte II, axe 6 :
  - bras sans pistes, v6 (`1b301c15…`) : **10 356 caractères** ;
  - bras avec pistes, v8 (`3f16fec3…`, en quarantaine) : **11 291 caractères**.
- Les pièces de la course 2 forment une liste fermée, bien plus courte que le corpus de la course 1 (**SUPPOSÉ** : le coût d'entrée par session baisse d'autant).

## 2. Structure servie (identique dans A et B)

Quatre sous-sessions séparées par proposeur, chacune en deux passes :
1. texte I, axes 1 à 5 et la boucle ;
2. texte I, axe 7, dans une sous-session neuve (D1) ;
3. axe 6 sans pistes ;
4. axe 6 avec pistes.
Les deux bras de l'axe 6 vont aux deux proposeurs (R-568).

Les autres éléments sont :
- **juges** : Opus 5.5 et Argon, pour chaque sous-session ;
- **témoins** dans chaque lot ;
- **pré-pilote d'étalonnage** (Q1) avant la course : juges et garde éprouvés sur des fiches témoins.

## 3. Hypothèses de calcul (SUPPOSÉ, à remplacer par les mesures du pré-pilote)

- **Une sous-session de la course 2 coûte entre 0,5 et 1 fois la course 1 entière**, par proposeur et pour deux passes. Les pièces sont plus courtes, mais les consignes sont plus exigeantes.
  - Pour Fable : 12 à 24 USD par sous-session.
  - Pour Argon : 3 à 6 USD.
- **Kimi** consomme autant de jetons que Fable pour le même travail, au prix cinq fois plus bas : 2,4 à 4,8 USD par sous-session. Kimi passe par la voie « protocole » (comme Argon), et non par le kit Claude Code avec ses boucles d'outils. Sa consommation pourrait donc être plus basse ; le pire cas la double quand même, par prudence.
- **Juges** : 5,6 USD par sous-session de 29 fiches environ, et jusqu'à 7,5 au pire.

## 4. Devis

| Poste | A (Fable), attendu | A, pire | B (Kimi), attendu | B, pire |
|---|---|---|---|---|
| Proposeur Claude ou Kimi (4 sous-sessions) | 48 | 96 | 10 | 38 |
| Argon proposeur (4 sous-sessions) | 18 | 24 | 18 | 24 |
| Contrôles d'Argon | 1,75 | 3 | 1,75 | 3 |
| Juges Opus 5.5 et Argon (4 sous-sessions) | 22 | 30 | 22 | 30 |
| Pré-pilote d'étalonnage (Q1) | 7 | 10 | 7 | 10 |
| Coûts propres à B : épreuve courte de la chaîne Kimi, étalonnage de la garde de niveau méthode sur Kimi au pré-pilote | — | — | 2,5 | 4 |
| **Total (USD)** | **≈ 97** | **≈ 163** | **≈ 61** | **≈ 109** |

**Économie de B sur A** : ≈ **36 USD** attendus, ≈ **54 USD** au pire, soit un peu plus du tiers. Elle ne porte que sur les proposeurs ; les juges et Argon coûtent pareil.

**Coûts de B hors appels**, sans dépense, sur processeur :
- un relais Kimi chez session-depot : la clé est posée par Lazar et tenue en mémoire, avec un plafond, une liste des modèles permis et un journal ;
- un adaptateur Kimi par la voie protocole, et le contrôle du modèle servi, dans l'orchestrateur, chez conv-audit après la v51 ;
- une contre-lecture du tout.
Délai : environ une demi-journée.

**Préalables de B, qui reviennent à Lazar** :
- compte développeur Moonshot et crédit prépayé ;
- **nouvelle clé**, puisque celle collée dans la conversation de conv-audit est à révoquer (R-569 de conv-audit) ;
- choix de confidentialité : le bras avec pistes part chez Moonshot (R-568).

## 5. Réserves

- Les courses 1 et 2 ne sont pas comparables proposeur par proposeur (R-567).
- Toutes les hypothèses du § 3 sont **SUPPOSÉ**. Le pré-pilote mesure le coût réel d'une sous-session, et le devis est refait avant la course.
- La garde de niveau méthode (refus, fiches écartées) est étalonnée sur Claude et Argon, pas sur Kimi ; d'où l'étalonnage au pré-pilote.

## 6. Décision pour Lazar (nœud de dépense)

**Décision** : quel plafond donner à la course 2 avec Kimi (B), pré-pilote compris ?

**Enjeu** : B coûte environ 61 USD attendus et 109 au pire, contre 97 et 163 avec Fable. L'économie, un peu plus du tiers, ne porte que sur les proposeurs.

**Options**
- **(a) B, plafond 110 USD**, séquencé : pré-pilote d'abord (≤ 15 USD), puis course seulement si le pré-pilote tient et que le devis refait reste dans le plafond. Avantage : couvre le pire cas. Inconvénient : engage plus que l'attendu.
- **(b) B, plafond 70 USD** : couvre l'attendu seulement. Avantage : plus serré. Inconvénient : risque d'arrêt en cours de course, avec des sous-sessions payées et non jugées.
- **(c) A (Fable), plafond 165 USD** : sans Kimi, sans relais ni adaptateur nouveaux. Avantage : la chaîne est déjà éprouvée. Inconvénient : environ 50 USD de plus, et Fable a déjà refusé une fois, comme juge.

**Recommandation** : (a), confiance 0,6.
