"""Variante du modèle des deux bras (option de D-3) : seules les parts Opus 5.5 des bras changent d'échelle de prix
(Sonnet 5.5 : 2/10 ; Fable 5.2 : 8/40, référence locale claude-api, table en cache du 2026-11-03, à vérifier).
Coûts unitaires repris de sortie-calculs-devis-v3.txt : L_agent 1.12, S_agent 0.322, N_lecture 0.18 (USD par item)."""
OPUS_PAR_ITEM_PILOTE = 1.12 + 0.322 + 0.18     # pilote : bras L, bras S, lecture nue
OPUS_PAR_ITEM_CONF = 1.12 + 0.322              # confirmation : bras L et S
TOTAUX = {"pilote": (311.86, 140, OPUS_PAR_ITEM_PILOTE), "confirmation centrale": (798.97, 384, OPUS_PAR_ITEM_CONF),
          "confirmation plafond": (1247.40, 600, OPUS_PAR_ITEM_CONF)}
for nom, (total, items, opus) in TOTAUX.items():
    part = items * opus
    print(f"{nom:22s} : Opus 5.5 {total:8.2f} ; Sonnet 5.5 {total - part * 0.5:8.2f} ; Fable 5.2 {total + part * 1.0:8.2f}")
