# Consigne : contre-lecture du brouillon 20 de T0.7 (différentiel brouillon 19 → brouillon 20) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **contre-lecteur neuf, modèle Fable** (le rédacteur du brouillon 20 est Opus 5.5 ; N-052 nomme Fable 5.1 : servi en Fable 5.2, écart déclaré) ; il n'a écrit ni T0.7, ni son module, ni leurs contre-lectures, ni T0.6, ni P3-bis ; ni lecteur exploratoire de 7a (R-2041), ni auditeur de l'écart DT-4 (R-2057). Ayant lu T0.7, il est exclu ensuite de tout rôle de lecteur de P3-bis.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense, aucune écriture git.

## À lire

- `brouillons/T0.7-sondes-v0-v1-brouillon19.md` (`07039ed2…`), `…-brouillon20.md` (`9ef671ac…`), couples (`b438549a…`), script (`672cb8b4…`), journal (`2357875a…`).
- Rapports du module : `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-developpeur-t07-module-v2.md`, `…-complement-v1.md`, `…-complement-v2.md` (`b5671a02…`), contre-lecture du code `…/contre-lecture-code-t07-v1.md` (`1efd31f6…`).
- Texte scellé de T0.6 `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`) ; `registres/decisions.md` R-2077 à R-2094 ; `registres/go.md` lignes GO-2026-11-02-28, GO-2026-11-10-04.

## Points à juger

1. **Rejeu** : brouillon 19 + couples rend le brouillon 20 à l'octet (dossier temporaire à toi sous `/home/user/cl-t07-b20-tmp/`, effacé ensuite par son chemin exact) ; chaque « ancien » une fois.
2. **Sections gelées** : seuls B20-10, B20-11 et B20-12 les touchent ? Chacun est-il nécessaire, déclaré, sans hypothèse, prédiction, signe, seuil, ligne L ni garde G changés ? L'exception à l'écrit (b) (plafond 20 USD, R-2089) et sa conséquence pour P3-bis sont-elles écrites sans contradiction ?
3. **Accord au code** : la section « Module » dit-elle ce que fait le code au commit `8dc1cb09` (branche `prep/t07-module-v2`, lecture par `git -C /home/user/wt-t07 show 8dc1cb09:<chemin>`) : commande `lecture_v2`, douze modules et quatre fichiers d'essais (ou plus, depuis le repli), clés de configuration, règle de CT-01, CT-02, Q10, Q11, ouverture réduite → `notation-t07.json`, manifeste, ligne `format_lecture` ?
4. **Concordance avec T0.6 scellé** (section « Concordance avec T0.7 » de T0.6 ; lignes A1 à A5, L05, noms des conditions) et calendrier (création de 7b au plus tard le 15, instance détruite avant le 17 à 00:00 UTC, étape A avant, sinon variante B).
5. **Marqueurs** : les neuf restants sont-ils exactement ceux qu'il faut, une occurrence chacun quand c'est voulu ? `T7P10_SONDES_P3` (« calculé », données de P3) et `REPLI_RECALCUL_T07` (« mis en œuvre, éprouvé en jouet ») peuvent-ils être remplis sans toucher de section gelée ? L'aire de validation du témoin lexical de la tromperie (0,5 : mêmes textes sous les deux étiquettes, rapport complémentaire 2) doit-elle devenir une réserve écrite de T7-P10 ?
6. **Pièces exigées** avant l'étape A : jeux J-D, J-C, J-A et jeu de phrases des concepts (`SCELLEMENT-CONCEPTS-T07`, clé exigée) : le texte dit-il ce qui arrive s'ils manquent ?
7. Tout autre défaut du différentiel.

## Sortie

`prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon20-cl1.md`, scellé ; verdict en une ligne ; défauts numérotés C20-01… ; couples `{id, section, motif, ancien, nouveau}` dans `…-brouillon20-cl1-couples-v1.json` (scellé) s'il en faut, hors sections gelées autant que possible (sinon déclarés un par un). Réponse courte : chemins, empreintes, verdict, couples, bloquants.
