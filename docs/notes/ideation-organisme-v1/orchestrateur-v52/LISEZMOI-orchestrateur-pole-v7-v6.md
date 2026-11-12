# Orchestrateur du pôle, version 0.7.0 — nul d'archive ajusté, banc de tricheurs — LISEZMOI v6

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5 pour cette version), v6 écrite à partir de 15:54 UTC
(heure lue sur `date -u`) ; v1 à v5 gardées telles quelles (R12). Ce qui change en v6, après le banc de tricheurs
(lecture : `../banc-tricheurs-v7/lecture-banc-tricheurs-v7-v1.md`) :

| changement | fichiers |
|---|---|
| **nul d'archive ajusté** (`ConfigGeneration.nul_archive_ajuste` ; **par défaut dans la ligne de commande** en sélection par pari avec le nul d'archive, `--sans-nul-archive-ajuste` pour l'enlever) : au nul de toute fiche non témoin, la mise en commun linéaire ajustée de toutes les lois connues de même espace (parents d'une fille et survivantes de l'archive) avec toute loi aveugle fixe, et chaque survivante tempérée et inclinée ajustée ; lecture aux instants fixés (évaluateur du nul des filles v2) dès qu'un membre ajusté est présent. Ferme T02 à T05 du banc (148 à 179 promues sur 200 sous v7 ; 0 sur 200 avec), perte de puissance ≤ 0,02 | `pole/cycle.py` (`membres_de_l_archive`, `a_des_membres_ajustes`, `preparer_engagement`), `pole/pole.py` |
| **correction des membres ajustés « tempérés et inclinés »** : marge de Newton admise seulement près de l'optimum (décrément² ≤ 0,25), sinon borne triviale 0 ; plus de départ à chaud depuis un ajustement non convergé ; toute valeur ajustée plafonnée à 0. Défaut trouvé par un essai sur banque : données séparables au premier instant de lecture → marge de 5·10⁹ → loi exacte du monde éliminée | `pole/nul_filles_v2.py` |
| **loi « transformee »** (mélange aveugle, puissance, inclinaison, oscillation non monotone) pour écrire les tricheurs ; interdite au proposeur | `pole/selection_pari.py` |
| **banc de tricheurs exploratoire** (29 lignes, 200 répétitions, 5 minutes sur deux processus) | `demonstrations/banc_tricheurs_v7.py` |
| essais : `essais/test_v7_banc.py` (6 nouveaux : loi transformée saine et mal formée, interdite au proposeur ; mélange de survivantes promu sous v7 et éliminé sous le nul ajusté, loi exacte du monde promue ; options incohérentes refusées ; parents dans la mise en commun d'une fille) | |

**190 essais passent** (184 de la v5, 6 nouveaux).

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v6.txt
$PY -I -B -m unittest                                                          # 190 essais, environ 3 minutes
$PY -I -B demonstrations/banc_tricheurs_v7.py DOSSIER_NEUF --graine G --repetitions 200 --processus 2   # 5 minutes
```

La commande réelle de la course de contrôle reste celle du LISEZMOI v5 ; le nul ajusté y est maintenant actif par défaut
(sans effet en génération 0 : il faut une survivante).

## Limites connues

- Le banc est exploratoire (200 répétitions, mondes synthétiques à deux traits, une graine) ; la validation décisive du
  juge suivra la règle d'arrêt commune, dans un préenregistrement scellé et contre-lu.
- Zone grise : la composition T07 (7 sur 200, borne haute 0,063 sous v7 ; 4 sur 200, 0,044 avec le nul ajusté).
- Le nul ajusté coûte du calcul (un ajustement de Newton par survivante et par instant de lecture, une espérance-
  maximisation pour la mise en commun) ; sur une archive de dizaines de survivantes, compter quelques dixièmes de seconde
  par fiche.
- Le reste : LISEZMOI v5.
