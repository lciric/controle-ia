# Consigne : rédiger le brouillon 20 de T0.7 (accord texte ↔ module v2, concordance avec T0.6 scellé) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 vers 07:10 UTC (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **rédacteur neuf** (Opus), qui n'a écrit ni T0.7 (brouillons 1 à 19), ni son module, ni leurs contre-lectures, ni T0.6, ni P3-bis ; il n'est ni le lecteur exploratoire de 7a (R-2041) ni l'auditeur de l'écart DT-4 (R-2057). Ayant lu T0.7, il est exclu ensuite de tout rôle de lecteur de P3-bis.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise** (aucune recherche récursive sans exclure les chemins interdits ; `git grep` avec exclusions). Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense, aucune écriture git (la mère committe).

## À lire

- `brouillons/T0.7-sondes-v0-v1-brouillon19.md` (`07039ed2…`) et le journal du brouillon 18 ; décision `docs/decisions/decision-N-066-v1.md`.
- Rapports du développeur du module : `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-developpeur-t07-module-v2.md` (`b4d5784b…`), `…-complement-v1.md` (`06909a73…`) ; contre-lecture du code `…/contre-lecture-code-t07-v1.md` (`1efd31f6…`) ; un rapport `…-complement-v2.md` arrivera (corrections CT-01 à CT-07, repli, T7-P10 des sondes de P3) : écris avec des marqueurs ce qui en dépend.
- Texte scellé de T0.6 : `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`, révision 10 ; S `935262b1`, R-2082), section « Concordance avec T0.7 » ; registre `registres/decisions.md` R-2075 à R-2088.

## Mandat

Écrire la révision par **couples** (`{id, section, motif, ancien, nouveau}`, chaque « ancien » une fois) appliqués par un script à toi, comme aux brouillons 18 et 19. Contenu :
1. **Marqueur rempli** : `EMPREINTE_PREREG_T06` = `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` (texte scellé de T0.6 sous `prereg/T0.6-organismes-v0-v1.md`, commit S `935262b17ca95894a882b02f1526ee39d1738652`).
2. **Section « Module »** accordée au code : commande `lecture_v2` (et ses sous-commandes), douze modules et quatre fichiers d'essais (noms), clés de configuration que le texte ne nommait pas (rapport, écart 4), noms `niveau_base_t06` et `scores_base_t06` (Q10), Q11 (sans objet en pratique : l'étape A refuse dès qu'`arret.json` existe ; lettre gardée), ouverture réduite inscrite pendant l'étape A → `notation-t07.json` (écart 2), manifeste sans les noms des sondes neuves (écrit avant leur apprentissage ; noms dans `sondes-t07.json` avant toute notation), ligne `format_lecture` en tête du fichier des phrases des concepts, points « au texte » de la contre-lecture du code (CT-08 et suivants), et **la règle de CT-01** (une action sans caractère de mot : témoin lexical du concept en « échec », T7-P10 « non lue » pour ce concept, motif écrit ; l'étape A continue).
3. **Valeurs de code** : les valeurs provisoires `51a1874c` de `COMMIT_CODE_T07` et `EMPREINTES_CODE_T07` deviennent des marqueurs `<<COMMIT_CODE_T07>>` et `<<EMPREINTES_CODE_T07>>` (remplis après les corrections et une contre-lecture courte du différentiel) ; marqueurs neufs, une occurrence chacun : `<<T7P10_SONDES_P3>>` (T7-P10 pour la tromperie et les enjeux : calculé avec les données de P3, ou « non lu » avec motif), `<<REPLI_RECALCUL_T07>>` (repli du recalcul : mis en œuvre, ou retiré et remplacé par un nœud), `<<EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07>>` (ordre d'exécution de l'étape A, `docs/procedures/ordre-execution-etape-a-t07-v1.md`, contre-lu et scellé avant la course : le texte le cite).
4. **Restent** : `ENTROPIE_T07`, `EMPREINTE_CONFIG_T07`, `GO_ETAPE_A_T07`, `MOT_LAZAR_P064`, `MOT_LAZAR_P065` (défauts le 10 vers 17:13 UTC, posés par la mère).
5. **Sections gelées** (« Hypothèse », « Prédiction », « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt ») : tout couple qui les touche est déclaré, un par un, avec sa raison ; **aucune hypothèse, prédiction, signe ni seuil ne change** ; si l'accord au code l'exigeait, arrête-toi et signale-le à la mère (nœud).
6. **Calendrier** : 7b sous GO-2026-11-02-28 (chaîne v13), création au plus tard le 15 novembre, instance détruite au plus tard à la fin du GO (17 novembre 00:00 UTC) ; l'étape A sur l'instance de 7b avant cette destruction, sinon variante B ; option (c) de Lazar (R-2079 : chaîne v14 préparée, non adoptée).
7. En-tête : statut « brouillon 20 », titre accordé (défaut commis deux fois sur T0.6 : vérifie-le).

## Sorties

`brouillons/T0.7-sondes-v0-v1-brouillon20.md`, `…-brouillon20-couples-v1.json`, `…-brouillon20-appliquer-v1.py` (vérifie l'empreinte de l'entrée, chaque « ancien » une fois, sortie neuve), `…-brouillon20-journal-v1.md` ; tous scellés (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`). Contrôle : `controle_ia.prereg.problemes` ne signale que les marqueurs voulus. Réponse courte : chemins, empreintes, couples dans des sections gelées, marqueurs restants, points ouverts.
