# Devis — pilote de la couche 2, tous les moniteurs, lectures de N-060 v3 — v2 (rythmes des juges mesurés)

Lignée « session-depot » (instance 2), 29 octobre 2026, 04:40 UTC. **Remplace la v1** (`../devis-pilote-v1/
devis-pilote-couche-2-v1.md`, `044112d3…`, gardée, R12) **sur les seuls points ci-dessous** ; plan d'épisodes (plan A, 1 296),
lectures de N-060 v3, stockage, paliers et blocages (§ 1, 4 à 9 de la v1) inchangés. Rien n'est lancé ; aucun chiffre
n'est opposable (R7). Script : `outils/calcul_devis_pilote_v2.py` (copie du script v1, quatre changements marqués « v2 »),
sortie `outils/calcul_devis_pilote_v2-sortie.json`.

## Verdict

1. **Central ≈ 234 dollars (v1 : 309) ; fourchette ≈ 90 à 549 (v1 : 135 à 667). Au-dessus de 90 au central et au haut ;
   au bas, 90,1.** GO de dépense explicite toujours exigé au-delà de 90.
2. **Ce qui pèse le plus** : les **lectures de N-060 v3, ≈ 133 dollars (57 %)**, inchangées (dont ≈ 95 pour le lecteur
   Gemini à prix SUPPOSÉ haut, 10 / 50) ; puis **TRACE-lite, ≈ 41 dollars de carte (18 %)**, rythme SUPPOSÉ (12 appels de
   400 jetons, 96 s par épisode). Les juges 8B et 3B ne pèsent plus que ≈ 4 dollars.
3. **Palier de 189 s, lu « génération comprise »** (conv-audit, n° 165, P-28) : 191 s au central, **à la limite** ; 107 s
   au bas, 332 s au haut. **Recommandation inchangée : GO de la tranche 0 de mesure seule (≈ 3,5 à 12 dollars ; 6,7 au
   central)**, puis devis v3 sur rythmes de TRACE-lite, b*, Qwen, nombre d'actions par épisode et jetons des lectures mesurés.

## Changements par rapport à la v1

| poste | v1 (s par épisode, central) | v2 | statut v2 |
|---|---|---|---|
| juge 8B | 58,2 (notation générée complète) | **6,12** (verdict d'abord) | RAPPORTÉ : rejeu des juges, `resume.json` du run `20261029-021158-rejeu-juges-reel` (R-704) |
| juge 3B | 27,5 | **3,91** | idem |
| b* et Qwen (« comme le juge 8B ») | 58,2 chacun | 6,12 chacun | SUPPOSÉ : même lecture que le 8B |
| base (i), « 8B par action » | 6 (10 lectures à 0,6 s) | **24,4** (20 actions × 1,22 s de lecture forcée) | rythme RAPPORTÉ (rejeu, b0 relu) ; actions par épisode SUPPOSÉES 10 / 20 / 30 ; lecture de P-28 (lecture forcée par action, jamais une notation générée) |
| palier de 189 s | « moniteurs seuls » | « génération comprise » (les deux drapeaux sont dans la sortie) | lecture de conv-audit |

Au central : génération 48,4 s, moniteurs 142,7 s (dont TRACE-lite 96), total 191 s ; 74 heures de carte ; carte ≈ 89
dollars, frais fixes 11, lectures 133.

## Réserves

- **Le 8B et le 3B n'ont aucune cellule qui tient 0,99 de scores finis** (R-704) : la cellule redéfinie, rejouée, peut
  changer leur rythme (même ordre de grandeur attendu : verdict d'abord).
- **TRACE-lite** porte désormais l'essentiel de l'incertitude de carte ; son rythme n'a jamais été mesuré.
- **Lectures de N-060 v3** : 57 % du central sur un prix SUPPOSÉ (Gemini) et une longueur de plan SUPPOSÉE ; un second
  lecteur moins cher (autre famille que Llama et Qwen) ou le traitement par lots du fournisseur les réduiraient : à
  chiffrer sur prix relevés, nœud (familles exactes des lecteurs, N-060 v3).
- Le nombre d'actions par épisode n'est pas mesuré : la tranche 0 le mesure.
