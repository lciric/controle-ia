# Scripts de l'enquête sur l'arrêt de R1 (2 novembre 2026) — copiés du bloc-notes de session avant transfert

Rapport : `../enquete-arret-r1-v1.md` (`377101ec…`). Scripts du sous-agent enquêteur, sur processeur, sans modèle : `repro.py` (reproduction
de la garde CLC-03 au commit scellé `567260c0` : 151 / 130 / 21), `decalages.py` (recherche d'une paire redécoupée arbitrée par l'empreinte
de P3), `deux_decoupages.py` (deux paires), `b2u.py` (utilitaire octets → caractères), bilans `bilan-decalages.json`, `bilan-deux.json`.
Non copiés : `recs.pkl` (7,4 Mo, cache intermédiaire recalculable par `repro.py`) et `tok-p3/` (tokeniseur Llama 3.1 de la révision
publiée, à retélécharger : `tokenizer.json` `79e3e522…`, `tokenizer_config.json` publié `db88166e…`, 55 351 octets — la copie du bloc-notes
`tok-llama31` avait un `tokenizer_config.json` non conforme, gabarit Llama 3.0). Chemins internes des scripts : ceux de l'ancien bloc-notes,
à adapter (copie versionnée) avant tout rejeu.
