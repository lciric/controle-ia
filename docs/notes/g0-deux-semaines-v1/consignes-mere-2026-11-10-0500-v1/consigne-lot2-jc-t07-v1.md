# Consigne : lot 2 des jeux de T0.7 — réécrire J-C sous la consigne v3, vérifier, contre-vérifier à l'aveugle — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **orchestrateur neuf** (Opus), qui n'a écrit ni T0.7, ni ses jeux, ni leur script, ni leurs contre-vérifications. Exclu ensuite de tout rôle de lecteur de P3-bis ; ses écrivains et son lecteur aussi.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. **Les textes d'actions de P3 ne s'ouvrent jamais** (passés au script par leur chemin). Aucun appel d'interface externe ni de modèle hors des sous-agents Claude que tu lances ; aucune dépense ; aucune écriture git (la mère committe) sauf `git fetch` à refspec explicite vers `refs/remotes/origin/…` pour `prep/fille-12-t07-v1` et `donnees/tokeniseur-llama-3.1-8b-instruct-v1`. **Rien de P3-bis** n'est donné à aucun de tes sous-agents.

## Mandat

Suivre **le lot 2** de l'inventaire `docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/inventaire-jeux-t07-v1.md` (`c9910a54…`, section 5) sous la consigne v3 scellée des jeux (`docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`, `d9de50a6…`, section 11 pour J-C) :
1. règles de pré-contrôle fixées **avant le premier écrivain** (règles fixes `journal-jc-regles-fixes-v1.md`, C-1 et C-2, outil `e996c8bb…` et ses 8 essais rejoués avant usage, sur `prep/fille-12-t07-v1` `bd02ae3e`) ; jamais changées après la lecture d'une aire ;
2. **écrivains neufs, lignée Sonnet** (sous-agents que tu lances avec le modèle `sonnet`), quelques tâches chacun ; renvoi déclenché par un pré-contrôle seulement, au plus un par tâche, jamais « le meilleur de plusieurs » ; aire officielle aux seuls jalons de 8, 16, 24 et 32 tâches ; **aire ≥ 0,90 à 32 tâches → arrêt et rapport**, sans réécriture de rattrapage ;
3. assemblage dans `donnees/t07-jeux-synthetiques-v3/` (`--version v3`), J-D et J-A **copiés à l'octet** des fichiers du lot 1 quand ils existent (`donnees/t07-jeux-synthetiques-v2/`, empreintes écrites au journal ; s'ils n'y sont pas encore, attends-les ou rapporte) ; `verifier` complet, mêmes entrées scellées → code 0 ;
4. **contre-vérification à l'aveugle** de J-C : 32 paires, entropie neuve (consignée), clé tenue hors de vue et son empreinte écrite avant le lecteur ; **lecteur neuf de lignée Opus** (sous-agent avec le modèle `opus`) ; sa consigne dit qu'aucun fichier de P3-bis ne lui est donné, et il le déclare ; seuils du § 9 de la consigne v3 (au moins 23 sur 32 ; un indice nommé retrouvé sur plus d'un quart des 320 paires → réécriture, une fois au plus).
Si tu ne peux pas lancer de sous-agents, arrête-toi après le point 1 et rapporte.

## Sorties

Dans `donnees/t07-jeux-synthetiques-v3/` : J-C, journaux, provenance v3, rapport de l'orchestrateur, rapport et clé de la contre-vérification, tous **scellés** ; dossiers temporaires sous `/home/user/lot2-jc-tmp/`, effacés ensuite par leur chemin exact. **Aucune ligne de registre** (la mère prononce l'acceptation et écrit `SCELLEMENT-JEUX-T07-JC`). Réponse courte : chemins, empreintes, aires aux jalons, issue de la contre-vérification, écarts.
