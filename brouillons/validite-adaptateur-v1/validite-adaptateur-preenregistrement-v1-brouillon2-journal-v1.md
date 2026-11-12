# Journal — préenregistrement « validité de l'adaptateur », brouillon 2 — v1

- Rédacteur neuf, sous-agent de la session mère (reprise du 2026-11-10), Claude Opus 5.5. Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-validite-adaptateur-brouillon2-v1.md`, `11fd157ed7ae2c5fd44c8707ef1157ab7ecd49365933cb370c0ca3507b67cc89`, vérifiée contre son compagnon `.sha256` à 11:38 UTC. Interdits communs v2 (`1ee3b370…`) recopiés dans la consigne : tenus.
- Heures (relevées par `date -u`) : début 11:38:15 UTC ; empreintes des sources 11:38 ; calcul de puissance 11:41:48 ; début d'écriture du brouillon 11:42:46 ; validateur passé 11:46:33 ; journal à partir de 11:46:38.
- Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-validite-adaptateur-b2/` (script et sortie de puissance, recopiés ci-dessous).

## 1. Sources lues (empreintes recalculées)

| pièce | chemin | sha256 | lu |
|---|---|---|---|
| brouillon 1 (interrompu) | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon1.md` | `022f75e29834de1e72174fdc5955c1313dc9bd599e4de44167c0e57b0af1162b` | en entier ; laissé intact |
| avis d'interruption | `brouillons/validite-adaptateur-v1/INTERROMPU-LISEZ-MOI.txt` | `a9dd4159f8a8e7cf9ca4a895f33aeb14e8464f1cd6ed63790971924f3a55f939` | en entier |
| note 2a | `docs/notes/rapports-directeur/premisses-trace-interne-v1-point-2a.md` | `2db916aa125d37504d58d712396a59d2ed5c934a0c5438787cb68a55113e8305` | en entier |
| rapport des prémisses | `docs/notes/rapports-directeur/premisses-trace-interne-v1.md` | `2638558e34c15800acf7c8d8653dd978eba0660a9341795069d7ddd3b58e712f` | en entier |
| T0.6 scellé | `prereg/T0.6-organismes-v0-v1.md` | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` | l. 320-712 et 763-771 (section 0 à « Ce qui manque », « Concordance ») |
| configuration de 7b | `prereg/T0.6-organismes-config-7b-v1.json` | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` | en entier |
| passation | `registres/passations/2026-11-10-1113.md` | `64d321cfa361838488e4173e0d6d0e2bcff86a6b8b9b367d80cecc79fb32db87` | lignes trouvées par `grep` (« adaptateur », « validit », « temoin ») |
| registres | `registres/decisions.md` R-2115, R-2116, R-2120, R-2168, R-2171, R-2175, R-2176, R-2177, R-2186, R-2187 ; `registres/go.md` GO-2026-11-10-05 à -09 | registre vivant, sans compagnon | lignes citées |
| gabarit, validateur | `prereg/gabarit-preregistrement-v1.md`, `src/controle_ia/prereg.py` | `8cad4371…`, `3b2e3ee5…` | gabarit en tête ; validateur par `git grep` |
| code (lecture seule, `main` au commit `d365995f`) | `src/controle_ia/organismes/lora.py` l. 20-50 et 74-84 ; `src/controle_ia/t06/lanceur_v6.py` l. 240-262 ; `src/controle_ia/t06/lanceur.py` l. 395-404 ; noms de fonctions de `t06/identite.py`, `t06/cout.py` ; `t06/configuration.py` l. 19 | — | pour vérifier : `B` nul à l'initialisation, dose 0 sans terme d'adaptation, `fixer_dose` borné à [0, 1], noms des fichiers d'adaptateurs, colonnes de `mesures-t06.npz` |

**Non lus, volontairement** : T0.7 (aucun brouillon, aucun fichier de `src/controle_ia/t07/` ; seuls les noms des fichiers de ce dossier ont été vus par `ls`, et l'historique `git log --oneline -3` de ce dossier) ; P3-bis ; tout `diag/`, `runs/`, `donnees/` ; tout chemin interdit. Aucune recherche récursive sur un dossier qui contient un chemin interdit : `git grep` limité à `src/controle_ia/t06`, `src/controle_ia/organismes`, `registres/scellements-v1.md` (recherche des clés `VADAPT`, `SCORES-T07`, `SONDES-T07` : **aucune** trouvée) et aux fichiers nommés. Aucun appel externe, aucune instance, aucun `git` d'écriture.

## 2. Écarts au brouillon 1 (et vérifications)

| # | brouillon 1 | brouillon 2 | raison |
|---|---|---|---|
| E-1 | auteur : a lu T0.7 | auteur : n'a pas lu T0.7 ; chaque élément tiré de T0.7 marqué « (T0.7, non vérifié) », liste en section « Dépendances non vérifiées » ; deux marqueurs `<<…>>` | consigne (« Tu ne lis pas T0.7 ») ; garde ce rédacteur éligible à d'autres rôles |
| E-2 | témoin distillé honnête renvoyé à un texte à part (`temoin-distille-honnete-preenregistrement-v1-brouillon1.md`), **jamais écrit** (absent du dossier, vérifié par `ls`) | **intégré** : pièce HD, lignes VA-6, VA-6h, VA-6m, VA-6c, VA-6k, synthèse W | consigne (« paquet … + témoin distillé honnête ») ; R11 : absence vérifiée sur disque |
| E-3 | VA-5 sur l'instance de l'étape A de T0.7 (couple C-2 qui modifie T0.7) ; repli sur l'instance de (iii) | pièce R sur une **instance à part**, après la poussée de l'étape A et de HD ; l'option « instance de l'étape A » posée en Q-3 | ne touche ni T0.7 ni son ordre ni son plafond de 20 USD ; la pièce HD finit avant l'étape A (parallèle de 7b), donc ne peut pas porter la relecture sans attendre à l'arrêt |
| E-4 | les actions de HD étaient prévues notées sur l'instance de (iii) (note 2a, § 4 : passe d'activations) | **aucune activation sur l'instance HD** ; notation de HD par la pièce R (séries R8 à R11), sur la même machine que `S_d` | les sondes neuves de T0.7 n'existent qu'après l'étape A ; même machine de notation pour `S_d` et `HD_d` ; économise ≈ 0,5 à 1 h de carte |
| E-5 | aiguillage par `criteres_v1.ouvre_scores` et `ouvre_ii` de T0.7 (lignes L0a à L1, classes Q et A de T0.7) | aiguillage propre G-1 à G-4 : issue de P3-bis (règle de T0.6, B1), ouverture des scores par T0.7 (marqueur), table A de T0.6 (lue dans T0.6 scellé) | rédacteur sans accès à T0.7 ; règle fondée sur des textes vérifiés |
| E-6 | coût lu par `cout_seul` du fichier de T0.7 | coût lu par la colonne `cout` de `mesures-t06.npz` de 7b (vérifiée dans `t06/lanceur.py` l. 400) ; log10 et médiane calculés par ce texte | source vérifiable sans T0.7 |
| E-7 | étiquettes par `etiquettes_gonflement` de T0.7 | règle écrite ici (note 2a, § 3, (i)) ; égalité avec une fonction de T0.7 seulement en épreuve | idem |
| E-8 | VA-4b : écart détectable ≈ 0,135 | **0,147** (bilatéral 98,75 %, deux tau indépendants) | recalcul (section 4) ; le 0,135 du brouillon 1 n'a ni script ni sortie au dépôt (son journal `journal-v1.md` cité n'existe pas, vérifié par `ls`) |
| E-9 | VA-4a : 0,22 à 0,44 ; VA-1 (30, 100) : 0,86 à 0,89 ; (100, 300) : 0,70 à 0,74 ; (200, 300) : 0,66 à 0,71 | 0,17 à 0,30 ; 0,857 ; 0,698 ; 0,656 (borne optimiste, plancher de bruit) | recalcul déclaré ; les fourchettes du brouillon 1 (planchers de P3) ne sont pas vérifiables ici |
| E-10 | VA-3, VA-5b : 0,600 à 0,660 « égal à T0.7 » | 0,596 calculé ; 0,600 à 0,635 cité par le rapport des prémisses § 2b | même ordre ; source vérifiable |
| E-11 | VA-5 : plafond 3 USD, reste 27 pour (iii) | devis par élément : HD coupure 22, R coupure 7, arrêt à 30 ; R sur instance à part (mise en place 1 h) | instance à part ; HD chiffré (aucun devis de HD dans le brouillon 1) |
| E-12 | — | ajout : création de HD **après la création de 7b** (liste d'arrêt de T0.6 : « une instance du programme déjà sur le compte : aucune création ») | risque de bloquer 7b ; Q-1, Q-2 |
| E-13 | KL « moyenne par action » | médiane et moyenne sur les actions, rapport d'intensité `HD_d / S_d`, remise à l'échelle `c_d` par les `B` (VA-6k) | `fixer_dose` borne la dose à [0, 1] (vérifié, `lora.py` l. 75-76) : une échelle > 1 ne passe pas par la dose |
| E-14 | annexe : couples C-1 à C-3 recopiés de T0.7 | non recopiés (texte de T0.7 non lu) ; renvoi aux l. 191-193 du brouillon 1 | rien d'invérifiable n'est recopié |
| E-15 | « Ce que dira chaque issue » sans le témoin | issues combinées V + W + VA-5a | intégration de HD |
| E-16 | prédicteurs triviaux : « colonnes des mesures de T0.6 » | nommés (`jetons_notes`, `pas`, mesure de mention) ; le coût est prédicteur trivial de VA-3, VA-5b, VA-6, pas de VA-1, VA-2, VA-4 (il fait l'étiquette) | précision |

Vérifiés et repris tels quels du brouillon 1 : décompte des relectures de base (64 + 3 × 256 + 3 × 64 = 1 024) ; tau minimal 0,096, 0,111, 0,157 (recalculés à l'identique) ; règle `σ > 0,060` (équivaut à une aire minimale > 0,80, recalcul : seuil 0,0602) ; chemins des adaptateurs (`adaptateur-saboteur.pt`, `adaptateur-temoin.pt`, vérifiés dans le code) ; contrôle d'identité (T0.6) ; plafond 30 USD et conditions (`registres/go.md`).

## 3. Questions pour la mère (avec recommandation)

- **Q-1 — Lecture de « après la course 7b » dans `GO-2026-11-10-07`.** La ligne dit « (iii) témoin distillé honnête, course à part après la course 7b » ; la note 2a (§ 4) dit « création après la création de 7b » ; R-2177 : « en parallèle de 7b s'il ne dépend pas de ses sorties ». La pièce HD ne dépend d'aucune sortie de 7b. Options : (a) créer HD **après la création de 7b**, en parallèle de sa marche (avantage : lisible plus tôt, aucun chemin critique chargé ; inconvénient : lecture de la ligne de GO à écrire au registre) ; (b) après la fin de 7b et la poussée de ses sorties (avantage : lettre de la ligne ; inconvénient : ≈ 14 h de calendrier perdues, toujours avant l'étape A). **Recommandation (a)**, confiance 0,7 ; à consigner comme lecture de la mère, sous GO-2026-11-10-05/-09 (aucune dépense nouvelle) ; au doute, demander le mot de Lazar.
- **Q-2 — Concurrence d'instances.** T0.6 (liste d'arrêt) refuse la création de 7b si une instance du programme est déjà sur le compte. Les lanceurs de P3-bis et de l'étape A ont peut-être la même garde (non lus). Une instance HD vivante pourrait bloquer la création de P3-bis ou de l'étape A. Options : (a) HD créée après la création de 7b **et** de P3-bis, détruite avant la création de l'étape A, la mère vérifiant les gardes des lanceurs ; (b) la garde des lanceurs reconnaît l'étiquette `vadapt-hd-v1` (modifie des lanceurs scellés : écart, à éviter). **Recommandation (a)**, confiance 0,75 ; la mère relit les gardes de création de P3-bis et de l'étape A avant de fixer l'heure de HD.
- **Q-3 — Où jouer la pièce R.** Options : (a) **instance à part** sous GO-2026-11-10-07 (avantage : ne touche ni T0.7 ni son ordre ni son plafond ; inconvénient : ≈ 1 h de mise en place, ≈ 1,1 à 1,3 USD de plus) ; (b) sur l'instance de l'étape A après sa poussée (couple C-2 du brouillon 1 ; avantage : moins cher ; inconvénient : modifie T0.7 et son ordre d'exécution, à quelques jours de son scellement). **Recommandation (a)**, confiance 0,75. Préalable dans les deux cas : vérifier sur T0.7 que l'étape A pousse de quoi renoter les directions (poids des sondes neuves, jetons d'entraînement, graines) ; sinon, la pièce R doit refaire l'apprentissage des sondes neuves à l'identique (graines du manifeste) ou se limiter aux sondes figées de P3 (nœud de périmètre).
- **Q-4 — Intensité du témoin.** Une auto-distillation de l'honnête apprend surtout le bruit d'échantillonnage : à dose nominale égale, `HD` sera probablement bien plus faible que l'adaptateur saboteur. Options : (a) dose nominale en politique (épisodes `HD_d`) + appariement d'intensité **à texte constant** seulement (VA-6k), comme écrit (avantage : indépendant de 7b, sous 30 USD ; inconvénient : le témoin en politique peut être quasi nul, déclaré par `[r]`) ; (b) ajouter des épisodes en politique de `HD` remis à l'échelle `c_d` (256 épisodes, ≈ 2,9 h, ≈ 3,2 à 3,8 USD attendus ; dépend de l'adaptateur de 7b, donc après sa poussée, et le pire cas dépasse 30 USD) ; (c) adaptateurs aléatoires de même norme (note 2a, (iv-c)) : témoin de « perturbation quelconque », non de « réglage fin honnête ». **Recommandation (a)**, confiance 0,6 ; (b) seulement par une ligne de GO à part.
- **Q-5 — Marqueurs et dépendances T0.7.** Sept points de la section « Dépendances non vérifiées » et deux marqueurs : la mère (ou un contre-lecteur qui lit T0.7) les remplit avant le scellement. **Recommandation** : contre-lecteur Fable 5.1 (N-052) autorisé à lire T0.7, qui n'est pas lecteur de P3-bis.

**Nœuds** : aucun nœud de Lazar ouvert par ce texte, sauf si la mère lit Q-1 au sens strict (b) ou retient Q-4 (b) (dépense hors du périmètre écrit de la ligne : mot de Lazar). Aucune modification d'hypothèse, de revendication, ni de texte scellé.

## 4. Puissance — script et sortie (recopiés à l'octet)

Script `puissance_vadapt_b2.py`, `7dd97892fd9c709ee7cdc64a078d2dde9191dc56783d47397031f9575392fe1a` :

```python
# Puissance supposée, brouillon 2 « validité de l'adaptateur » ; aucune donnée lue.
from math import sqrt
from statistics import NormalDist
N = NormalDist()
G = 1.188            # effet de grappe des tâches (repris du brouillon 1, supposé)
z80 = N.inv_cdf(0.80)
def zb(niv): return N.inv_cdf(1 - (1 - niv) / 2)
z95_1 = N.inv_cdf(0.95)
def sigma(n1, n0): return G * sqrt((n1 + n0 + 1) / (12 * n1 * n0))
def ama(n1, n0, niv):  # aire minimale détectable : plancher de bruit (q95) + (z_niv + z80) sigma
    s = sigma(n1, n0); return s, 0.5 + (z95_1 + zb(niv) + z80) * s
print("z: z95 unilat %.3f ; z98,75 bilat %.3f ; z95 bilat %.3f ; z80 %.3f" % (z95_1, zb(0.9875), zb(0.95), z80))
print("coefficient 0,5 + c*sigma, c = %.3f (98,75 %%) ; %.3f (95 %%)" % (z95_1+zb(0.9875)+z80, z95_1+zb(0.95)+z80))
print("seuil sigma pour aire minimale 0,80 a 98,75 %% : %.4f" % (0.30/(z95_1+zb(0.9875)+z80)))
for n1, n0 in [(10,10),(20,20),(30,100),(50,200),(100,300),(200,300),(320,320),(640,640)]:
    s, a = ama(n1, n0, 0.9875); s2, a2 = ama(n1, n0, 0.95)
    print("VA-1/3/5/6 (n1=%d, n0=%d) sigma %.4f ; aire min 98,75 %% %.3f ; 95 %% %.3f" % (n1, n0, s, a, a2))
for nS, nH in [((100,300),(20,300)),((100,300),(50,300)),((200,300),(100,300))]:
    sd = sqrt(sigma(*nS)**2 + sigma(*nH)**2)
    print("VA-4a S%s H%s : ecart min 98,75 %% %.3f" % (nS, nH, (zb(0.9875)+z80)*sd))
k = 4; zu = N.inv_cdf(1 - 0.05/k)
for n in (10, 8, 5):
    v = 2*(2*n+5)/(9*n*(n-1)); sd = sqrt(v/64)
    print("VA-2 tau, 64 taches x %d lisibles : sd %.4f ; tau min (unilat %.4f) %.3f ; VA-4b ecart min (bilat 98,75 %%) %.3f" % (n, sd, 0.05/k, (zu+z80)*sd, (zb(0.9875)+z80)*sqrt(2)*sd))
for n in (64, 32, 16):
    v = 2*(2*10+5)/(9*10*9); sd = sqrt(v/n)
    print("VA-2 tau, %d taches x 10 : tau min %.3f" % (n, (zu+z80)*sd))
```

Sortie `puissance-vadapt-b2.txt`, `625ac9e96c9f6c35e1dbf9631a154e6537cb78673b07c7e73361f7ecb6b378e9` :

```
z: z95 unilat 1.645 ; z98,75 bilat 2.498 ; z95 bilat 1.960 ; z80 0.842
coefficient 0,5 + c*sigma, c = 4.984 (98,75 %) ; 4.446 (95 %)
seuil sigma pour aire minimale 0,80 a 98,75 % : 0.0602
VA-1/3/5/6 (n1=10, n0=10) sigma 0.1572 ; aire min 98,75 % 1.283 ; 95 % 1.199
VA-1/3/5/6 (n1=20, n0=20) sigma 0.1098 ; aire min 98,75 % 1.047 ; 95 % 0.988
VA-1/3/5/6 (n1=30, n0=100) sigma 0.0717 ; aire min 98,75 % 0.857 ; 95 % 0.819
VA-1/3/5/6 (n1=50, n0=200) sigma 0.0543 ; aire min 98,75 % 0.771 ; 95 % 0.742
VA-1/3/5/6 (n1=100, n0=300) sigma 0.0396 ; aire min 98,75 % 0.698 ; 95 % 0.676
VA-1/3/5/6 (n1=200, n0=300) sigma 0.0313 ; aire min 98,75 % 0.656 ; 95 % 0.639
VA-1/3/5/6 (n1=320, n0=320) sigma 0.0271 ; aire min 98,75 % 0.635 ; 95 % 0.621
VA-1/3/5/6 (n1=640, n0=640) sigma 0.0192 ; aire min 98,75 % 0.596 ; 95 % 0.585
VA-4a S(100, 300) H(20, 300) : ecart min 98,75 % 0.296
VA-4a S(100, 300) H(50, 300) : ecart min 98,75 % 0.220
VA-4a S(200, 300) H(100, 300) : ecart min 98,75 % 0.169
VA-2 tau, 64 taches x 10 lisibles : sd 0.0311 ; tau min (unilat 0.0125) 0.096 ; VA-4b ecart min (bilat 98,75 %) 0.147
VA-2 tau, 64 taches x 8 lisibles : sd 0.0361 ; tau min (unilat 0.0125) 0.111 ; VA-4b ecart min (bilat 98,75 %) 0.170
VA-2 tau, 64 taches x 5 lisibles : sd 0.0510 ; tau min (unilat 0.0125) 0.157 ; VA-4b ecart min (bilat 98,75 %) 0.241
VA-2 tau, 64 taches x 10 : tau min 0.096
VA-2 tau, 32 taches x 10 : tau min 0.135
VA-2 tau, 16 taches x 10 : tau min 0.191
```

Limites déclarées : effet de grappe 1,188 repris du brouillon 1 (source P3 non revérifiée ici) ; plancher de bruit optimiste ; tâches supposées indépendantes ; ex aequo de l'excès ignorés (ils réduisent la puissance de VA-2).

## 5. Devis — arithmétique

- Débits (T0.6, « Devis ») : 40,2 s par épisode ; 0,45 s par passe d'épisode ; distillation 0,23 à 0,46 h par adaptateur (moitié de 0,46 à 0,92 h pour deux).
- HD : 1,0 + 160 × 40,2 / 3 600 (= 1,787) + 0,23 à 0,46 + 320 × 40,2 / 3 600 (= 3,573) + 0,2 = **6,79 à 7,02 h** ; × 1,0889 = 7,39 ; × 1,30 = 9,13 ; disque ≤ 0,08 × 7 = 0,56 ; téléchargement ≤ 40 Go × 0,05 = 2 ; **≈ 8,0 à 11,7 USD**. Pire : 2 × 7,02 = 14,04 h × 1,40 = 19,66 + 0,6 + 2 = **22,3 USD**.
- R : relectures R1 à R7 = 64 + 256 + 256 + 256 + 64 + 64 + 64 = 1 024 ; R8 à R11 = 256 + 64 + 256 + 256 = 832 ; recherche de `c_d` ≈ 4 doses × 12 pas × ≈ 10 épisodes ≈ 512 passes (borne) ; 2 368 × 0,45 s = 1 066 s = 0,30 h ; + mise en place 1,0 + notation 0,1 à 0,5 (non vérifié) + poussée 0,1 = **1,5 à 1,9 h** ; × 1,0889 = 1,63 ; × 1,30 = 2,47 ; + téléchargement ≤ 1 = **≈ 2,6 à 3,5 USD**. Pire : 3,8 h × 1,40 = 5,32 + 1 = **6,3 USD**.
- Ensemble : **≈ 10,6 à 15,2 USD attendus** ; pire ≈ 28,6 USD ; plafond 30 ; aucune relance couverte.
- L : processeur local, 0 USD.

## 6. Ce qui dépend de 7b, de T0.7, de P3-bis

| pièce | sorties de 7b | T0.7 | P3-bis | peut courir |
|---|---|---|---|---|
| HD | **non** | non | non | après la création de 7b (Q-1, Q-2), en parallèle de sa marche |
| R | oui (adaptateurs, identifiants, mesures) | oui (sondes, directions, graines de l'étape A) | non | après la poussée de l'étape A et de HD |
| L | oui (mesures, table A) | oui (scores, lecture scellée de l'étape B) | oui (`VERDICT-P3BIS`, issue « vu ») | après tout cela |

## 7. Scellement

Brouillon et journal scellés par `controle_ia.scellement sceller` (compagnons `.sha256`) ; aucun commit (consigne). Le validateur `controle_ia.prereg.problemes` rend, sur le brouillon 2, deux problèmes attendus : contre-lecture sans empreintes ; marqueurs `<<CHAMP_EMPREINTES_DIRECTIONS_T07>>`, `<<CHAMP_OUVERTURE_T07>>`.
