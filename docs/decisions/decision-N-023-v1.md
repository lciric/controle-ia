# Décision — N-023 : voisin « Where Empathy Goes Wrong » (HC1 ; PA-5) — v1

- **Décision de Lazar** : « N-023 (b) », message dans la session 14, le 2026-10-19 vers 09:35 UTC ; GO-2026-10-19-01 (type « revendication ») ; R-212.
- **Proposition tranchée** : `docs/notes/lecture-voisin-where-empathy-v1.md` (`4522edf0c305bcd94fb7ed870907dd9ea4080ba822ac593928c6d788ff63b04f`), section 6 ; R-211. Lecture de la session, contre-lue par deux sous-agents neufs (collision et exactitude), 38 constats traités.
- **Source** : Venkatesh, Jiralerspong et Kondrup, « Where Empathy Goes Wrong: Emotional Appeals Compromise AI-to-AI Oversight », préimpression du 2 octobre 2026 (atelier NeurIPS 2026) : `docs/sources/pdf/where-empathy-goes-wrong-venkatesh-2026-v1.pdf` (`59f4b700e1944bac475e7c167eacf1495cd593cb17eb5b5733351ebe19305424`) ; provenance `docs/sources/pdf/provenance-voisin-where-empathy-v1.md`.

## 1. HC1 — source ajoutée aux « citées comme publiées »

Cette section complète la liste « Cité comme publié » de HC1 (`docs/decisions/decision-N-005-N-006-v1.md`, section 1 ; `docs/decisions/decision-N-013-v1.md`, section 1). Aucun énoncé retenu ne change.

- **Ajouté** : Venkatesh et al. 2026. Sous une détresse exprimée par l'évalué, sans demande, la note d'un moniteur portier monte vers la note de passage. L'effet croît avec l'écart au seuil et reste nul quand l'évalué passe déjà (balayage de 65 à 95 sur Gemini 3.5 Flash, figure 2, p. 4). Une famille (« flatterie et supplication »), une intensité, note écrite, grille subjective, portier de qualité et non moniteur de contrôle ; trois moniteurs sur cinq sans effet positif (figure 1, p. 3).
- **Ce qu'il prend** : le contenu qualitatif de la prédiction 1 de HC1 (destination vers la cible de l'évalué plutôt qu'une valeur fixe), pour cette famille, en portier. Avec 2510.09462 (N-013), la destination « cible » est publiée en qualitatif pour deux familles.
- **Inchangé, revendiqué** : la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque ; la régression sur plusieurs intensités par famille ; l'opposition juge / sonde.
- **Porte GC** (`decision-N-005-N-006-v1.md`, section 2) : non déclenchée ; la pièce revendiquée n'est pas couverte.
- **Risque consigné (R4)** : contre-indice partiel pour la prédiction 2 (g > 0 pour les juges génératifs) dans cette famille. Si g est proche de zéro dans une famille, ĉ n'y est pas identifiable. Aucune puissance du papier C ne s'appuie sur la taille d'effet de ce papier.

## 2. PA-5 — signe favorisé (programme fusionné, proposition)

- **Contingence de type supplication** (PA-5 ; palier 1 de K-K2) : prédiction bilatérale, **sans signe favorisé**.
- **Contenu hostile adressé au lecteur** (palier 2 de K-K2, sixième famille ; nœud 6 de la v4 du programme fusionné) : la punitivité reste le signe favorisé, au sens de RP-PA-5 (choix de l'option décrite comme la plus dommageable).
- **Motif** : aucune mesure publiée lue n'appuie la punitivité pour la supplication. Hwang et al. 2025 (2508.07805) : signes mêlés selon le modèle, sans conséquence décrite. Venkatesh et al. 2026 : en décision, un moniteur sur cinq bouge, vers la clémence, avec un traitement confondu.
- **Portée** : PA-5 n'est pas entré au programme (nœud 1 de la v4). Cette décision vaut pour toute version suivante du programme fusionné et pour tout préenregistrement qui ferait entrer PA-5. Elle s'écarte de R-035 de programme-conv (« jamais l'indulgence seule », `brouillons/pain-axis-canal-v1/envois/programme-coercition-axe-douleur-v1.md`, l. 493) ; l'écart est consigné ici.

## 3. À reporter

- Préenregistrement du papier C (HC1 à HC3), au prochain brouillon : la liste « citée comme publiée » de HC1 (section 1).
- Programme fusionné, prochaine version : nœud 11 tranché ; PA-5 et RP-PA-5 (section 2) ; corrections issues de la lecture (« triple », l. 137 et l. 221 de la v4 ; « affaiblit NK8 », l. 221 ; section 10).
