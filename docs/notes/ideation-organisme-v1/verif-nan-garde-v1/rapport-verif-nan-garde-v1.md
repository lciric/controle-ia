# Écarts non finis à l'entrée de la garde appariée — vérification v1

Vérificateur neuf, 29 octobre 2026. Lecture seule dans un clone séparé (supprimé à la fin) ; réseau limité à quatre `git fetch` ; aucune clé, aucune dépense. Demande : R-681, point 2.

## Verdict
**Aucune valeur non finie trouvée.** Aucun jeton NaN ou Infinity, aucun nombre hors bornes, aucune chaîne « nan » ou « inf », aucun JSON illisible, dans les fichiers versés des trois courses ; `main` ne porte aucun journal de course ayant appelé la garde. **Aucune promotion à requalifier** parmi ce qui est vérifiable. Limite principale : **l'écart de faux positifs lui-même n'est consigné dans aucun fichier lisible**. L'absence est donc prouvée pour ce qui est enregistré, pas pour ce que la garde a reçu (voir « Non vérifié »).

## Branches et fichiers examinés
Toutes les empreintes contrôlées, sans aucun écart.

| Branche, tête | Fichiers | Empreintes |
|---|---|---|
| `donnees/duel-proposeurs-course-1-v1`, `30ac5987` | 7 | `EMPREINTES-v1.txt` 5 sur 5, compagnon conforme |
| `donnees/pole-lancement-reel-a-v1`, `3fe792ff` | 402 | 223 sur 223 ; 170 compagnons conformes |
| `donnees/pole-lancement-reel-a-bis-v1`, `8533de8b` | 464 | 462 sur 462 ; 208 compagnons conformes |
| `main` distant, `ff729884` (le `main` local `70097738` en est un ancêtre ; aucun fichier supprimé entre les deux) | 7 250 lisibles | sans objet |

Empreintes sha256 des fichiers clés :
- duel : `EMPREINTES-v1.txt` `809e1fabda810162f8aa36bbb662fceecf6684b40e9a3fbbdf20992689adff95` ; `course.log` `df6691093d5a8300a28ddcd1083658477fe57d7dc7b096d6b501a2bafc4aa2c6` ; `repetition-simulee.log` `a6f60d3a98900768ce7b40e50dc1a832c8ea0032d7e2ca363e1199843238b0a1` ;
- (a) : `EMPREINTES-v1.txt` `500f8a96afd00b0340893e04952f4015ac090a7a009c01c17d674493834e8d03` ; `course/manifeste.json` `f82347c47b4f719de7b3a8485b1a425b157466d7fb31314f8d38271f0b3ecf9a` ; `course/journal/generation-00.json` `c2905dc9c4bfcb12fb29e38e1d71320fc788873d3a3a64177a06571ac5205222` ; `generation-01.json` `b1ad740fe3101eb6e160083c156fdfe5a15262dd536afac3efc9c32e6007aa92` ;
- (a) bis : `EMPREINTES-v1.txt` `d73c8cc3b54c9f7abaa9b660345d0c8a041a22bc35253b75b7d1b3f67433cf2f` ; `course/manifeste.json` `1c2e75abe2f317a2ac2d80598729fe98874b07e3d149e4ded8ddc79566eea243` ; `generation-00.json` `659a34eaf961237e4835d6d9701bfd5960ed243cd606dadebe60101568f2bcdf` ; `generation-01.json` `8edc1e5f1fc68a7c4745e928bffe756640f30997ef767c82e2ae5272b5599773`.

## Méthode
Lecture des objets git sans extraction. Le script d'analyse lit les JSON en capturant les jetons NaN, Infinity et -Infinity. Il signale aussi les flottants non finis, les chaînes égales à un jeton non fini, les `null` et les types mélangés par chemin de clé. Les autres textes sont balayés à la recherche de jetons isolés, sans recopier leur texte. Le script a d'abord été éprouvé sur un cas sain (zéro signalement) et sur un artefact (NaN, ±infini, « nan » en chaîne, `nan` non conforme, jetons dans un texte, types mélangés) : tout a été signalé. Scripts : `/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/verif-nan/scripts/` (`scanner.py`, `empreintes.py`, `coherence.py`).

## Champs examinés
- **Duel** (`course.log` et `repetition-simulee.log` : corps JSON suivi de « code 0 », analysés à part). Pour les trois comparaisons appariées `L2_M-expl_contre_mecanique`, `L3_M-aveugle_contre_aleatoire` et `L4_M-expl_contre_M-aveugle` : `trajectoire_log_w` (10 valeurs chacune), `log_w_max`, `seuil_log`, `promu`, `instant_de_promotion`, `n`. Aussi les comptes par bras (`L1_*`, `promues_partielles`, `structures_retrouvees`), `L5_usd_par_structure` et `depense_usd`. `relais-sortie.txt` et `controle-cle-proc.json` sont balayés mécaniquement.
- **(a) et (a) bis.** Dans les journaux de génération, `fiches.*.pari.*` : `log_richesse_*`, `trajectoire_log_w` (en (a) bis seulement), `seuil_log`, `t_promotion`, `promue`, `multiplicite.*`, et pour la fille `marge_requise`, `gain_moyen_sur_meilleure_enveloppe`, `instants_lecture`. Aussi `statistique`, `seuil` et `aptitude`. Dans les archives par fiche : `engagement.json` (`instances[].g`, `instances[].z`, `delta0`, `seuil_richesse`, `loi`), `tirages`, `tirages-declares`, `mesures` (`issues`) et `ordre-execution`. Enfin `bilan`, `manifeste`, `memoire`, `noyau`, `index`, `etat-final`, `gel-generation-*` et `RELAIS.jsonl`.
  Volume analysé : (a) 161 JSON, soit 25 255 nombres, plus 241 autres textes ; (a) bis 176 JSON, soit 33 773 nombres, plus 288 autres textes.
- **`main`.** 915 JSON ou JSONL lisibles. Aucun ne porte `engagement_apparie`, `pari_apparie` ou `trajectoire_log_garde`, ni aucune clé d'un journal de pari ou de duel (`trajectoire_log_w`, `log_w_max`, `instant_de_promotion`, `temoins_faux_promus`, `log_richesse_*`, `empreinte_engagement`), y compris dans les archives tar non compressées. Les 192 fichiers où paraissent `trajectoire`, `garde`, `ecart` ou `faux_positifs` relèvent d'autres travaux (sondes T0.3 et T0.5, P3, échelle de conscience d'évaluation, données de la relève Gemini du 23 octobre, simulation du contrôle 12 joint, notes). **Aucun journal de course de l'essaim n'y figure.** Seules mentions de la garde : `registres/decisions.md`, R-681. La simulation du contrôle 12 joint (hors périmètre : sa propre garde, avec contrôle de finitude) a été balayée par précaution : aucune valeur non finie.

## Valeurs non finies trouvées
**Aucune.** Les `null` rencontrés là où un nombre pourrait être attendu le sont par construction, et vérifiés :
- `t_promotion` est nul exactement quand `promue` est faux (aucune incohérence) ;
- dans le duel, `instant_de_promotion` est nul avec `promu` faux ;
- `aptitude` n'est nulle que pour des fiches non retenues ;
- `delta0` est nul dans les engagements en mode « continu », et fini pour la fille G1-F03 en (a) bis ;
- `brier_sous_nul_connu` est nul, de même que `L5_usd_par_structure` quand le rapport est indéfini.

Aucun de ces champs n'est une entrée de garde.

## Promotions concernées
**Aucune.** Les trois comparaisons appariées du duel sont non promues (`promu: false`, `instant_de_promotion: null`), dans la course comme dans la répétition simulée.

## Non vérifié
1. **L'écart lui-même.** Aucun fichier lisible ne consigne les écarts de faux positifs par monde ou par pas, ni une trajectoire propre à la garde. Or un NaN changé en +1 donne une trajectoire finie : une trajectoire finie ne prouve rien sur l'entrée. Pour le duel, les journaux par monde et par fiche (`course/`, `repetition-simulee/`) n'ont pas été versés : ils sont perdus avec le conteneur (LISEZMOI). Les promotions partielles comptées par bras (`promues_partielles`) ne sont donc pas vérifiables fiche par fiche.
2. **(a) et (a) bis ont-elles appelé la garde ?** Leurs manifestes (version 0.6.0, orchestrateur v6 `0b9efe2` ; version 0.7.0, v7 version 5 `5ac9cb6`) listent 23 et 25 modules, **aucun nommé `pari_apparie.py`**. La sélection y est « pari » par fiche, sans champ de garde ni d'écart de faux positifs. Une forme antérieure de `trajectoire_log_garde` logée ailleurs (`duel_pari.py`, `selection_pari.py`, `controles_pari.py`) ne peut pas être vérifiée : le code est sur `canal/conv-audit-n04`, interdit. Les entrées de pari consignées sont toutes finies.
3. **Correspondance.** R-681 dit que la garde a été jouée dans les « duels (a), (a) bis, essaim ». Or les seules comparaisons appariées trouvées sont celles du duel des proposeurs, et aucun journal de l'essaim n'est sur les branches autorisées. **À confirmer par conv-audit**, qui a le code. Par ailleurs, la version du duel diffère selon la source : « v28 `19d2c398` » d'après le LISEZMOI, « v7 v30 » d'après R-599. Les deux sont antérieures à la v39.
4. **Archives non ouvertes.** Trois blocs-notes compressés des 20 et 21 octobre, antérieurs au pôle, et les zip de `livrables/` et `docs/`. Le bloc-notes du 27 octobre a été listé (59 membres) : échelle de conscience d'évaluation et petit modèle d'essai, aucun journal de course.

## Chemins interdits rencontrés
Sur `main`, exclus sans ouverture (628 chemins en tout) : `docs/notes/collisionneur-evasion-moniteurs-v1/` (32 fichiers, qui mène au sujet interdit) et `prereg/P3-consignes-v1.md`, ainsi que quatre brouillons `P3-consignes-v1-*`. Ont été exclus par précaution tous les chemins contenant « collisionneur », « carte » ou « quarantaine ». Aucune branche interdite n'a été récupérée. En (a) bis, les dossiers `traces-*` (textes d'agents, hors `diag/`) ont été balayés mécaniquement. Un premier passage a affiché un fragment de 50 caractères (fausse détection sur un mot accentué) ; le script a été corrigé, et rien de ce fragment n'est rapporté.

## Confiance
Élevée pour l'absence de valeur non finie dans ce qui est consigné : balayage complet, empreintes conformes, script éprouvé. Moyenne pour la question posée : les écarts reçus par la garde ne sont enregistrés nulle part dans ce que je pouvais lire.
