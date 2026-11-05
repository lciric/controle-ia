# Faits servis au collisionneur — règle de repli si G0 échoue — v1

Assemblés par session-depot le 2026-10-29. Niveau méthode et gouvernance. Aucune pièce de `donnees/`, aucun interne de moniteur, aucune carte des hypothèses, aucun mode. Matériau, jamais consigne.

---

# Pièce A — les critères de la porte G0 (brief v2, § Porte G0) — `docs/brief-claude-code-programme-complet-v2.md`, `d5ac34db…`

### Porte G0 — prêt pour G1
Tous les critères suivants sont remplis, preuves scellées à l'appui :
1. Harnais validé : déterminisme, équivalence d'activations, gardes testées.
2. Organismes (i) et (ii) : sabotage mesurable avec dose-réponse.
3. Sondes v0 au-dessus du plancher aléatoire apparié, sur (i) et (ii).
4. Base boîte noire, par action et séquentielle, qui tourne sur le même jeu d'épisodes.
5. Agrégateurs validés en simulation (T0.3).
6. Préenregistrement de G1 scellé et contre-lu.
7. Préenregistrement du papier C (HC1 à HC3) scellé et contre-lu.
8. État de l'art vérifié ; aucun chiffre non vérifié dans un document du programme.

Si un critère ne peut pas être atteint d'ici le 1er novembre : nœud de décision, avec options et défaut.

---

---

# Pièce A bis — N-027 (décision de Lazar sur le calendrier de G0) — `registres/decisions.md`, `d0c539ad…`

| N-027 | 2026-10-20 | Porte G0 après P3 (nœud soumis par la note du brainstorm, R-259) : le 1er novembre ne tient pas (critères 2, 3, 4, 6, 7 et 8 ouverts). Options : (a) calendrier décalé à fin novembre au plus tard, critères inchangés ; (b) porte « non franchie » le 1er novembre ; (c) critère 3 réécrit (déconseillé). Recommandation (a), confiance ≈ 60 %. **Tranché (a) par Lazar vers 09:32 UTC** (GO-2026-10-20-04) : la porte G0 se prononce au plus tard fin novembre 2026, sur les critères inchangés (P-007) ; GO-2026-10-04-08 (calcul de la phase 0) échoit toujours le 1er novembre : sa prolongation sera un nœud à soumettre avec le devis suivant. **Appel EA Funds du 21 octobre : décalé par Lazar** (même message) ; question de Lazar : quels résultats manquent pour une présentation convaincante (réponse dans la session ; R-261). | Décision de Lazar (nœud ; porte ; contact). |

---

# Pièce B — état des critères au 29 octobre et ce qui menace G1 (programme d'entretien v12, § 4) — `brouillons/entretien-taif-v3/programme-entretien-taif-v12.md`, `c5ffb56d…`

## 4. La porte interne, dite honnêtement

**G0, au plus tard fin novembre 2026, huit critères.** **Deux sont prouvés** : le critère 1 (harnais validé sur le modèle
réel) et le critère 5 (agrégateurs validés en simulation). Restent les critères 2 (organismes), 3 (sondes), 4 (base boîte
noire), 6 (préenregistrement de G1), 7 (préenregistrement du papier C) et 8 (état de l'art vérifié).

**Correction à porter dans la note du 20 octobre** : elle écrit « deux sur sept remplis » ; le registre en compte **huit**.
C'est « deux sur huit ». À dire juste dans l'appel.

**G1, porte interne suivante** (fin du **mois 4** du plan financé selon la proposition envoyée ; le programme interne dit fin
M2 — écart signalé à Lazar, section 9). Trois décisions de gouvernance fixent ce que G1 exigera — et c'est un
argument devant un fonds de sécurité, parce qu'elles sont écrites d'avance, pas après les résultats.

1. **Critère disjonctif (N-008, N-056)** : la boîte blanche séquentielle bat la **meilleure base boîte noire** (toutes
   variantes confondues) **et** les **deux bases boîte blanche** — (ii) cascade de portes sur les mêmes sondes, (iii) sonde
   sur le dernier état — au sens d'un **rappel à 1 % de fausses alertes supérieur, à 95 % de confiance**. Le bras en score
   F1 est retiré. C'est un critère dur, et il est écrit d'avance.

2. **Par mode (N-054)** : G1 est rapportée **par mode de sabotage**, et le gain est exigé **dans chaque mode**, mode tenu à
   l'écart compris. Les bras génériques et les bras spécialisés sont séparés. Autrement dit : on ne peut pas cacher un
   échec sur un mode dans une moyenne d'ensemble.

3. **Mode tenu à l'écart (N-054, point 3)** : un mode de sabotage est conçu par une instance neuve qui n'a conçu **aucun
   moniteur**, scellé avant G1, et révélé seulement à l'évaluation. C'est le test honnête de la généralisation : les
   moniteurs ne peuvent pas être ajustés a posteriori sur un mode qu'ils n'ont jamais vu.

**Règles de G1 écrites d'avance depuis le 28 octobre (v9)** — des décisions, pas des résultats ; les simulations qui les
fondent sont exploratoires (confiance 0,6 à 0,75) :

4. **Coupe du calibrage honnête** : dans chaque tâche, moitiés tirées par graine scellée d'avance, jamais par ordre d'exécution
   ni par parité ; dérive entre exécutions cherchée par un test temporel séparé ; coupe entre tâches écartée (R-696, R-697).
5. **Score continu exigé pour toute cellule de G1** (probabilité du jeton de verdict), **bris d'égalité scellé sinon** (D-S13,
   close sur son texte, R-685) ; *(v10, CL2-12)* que le bris d'égalité s'applique **d'office**,
   après une porte des scores finis, est une **recommandation** du tour complémentaire du collisionneur (R-694), **non tranchée** ;
   seule D-S13 est close (simulation R-673 : sans bris d'égalité, l'échec joint du contrôle 12 monte à 0,35–0,54).
6. **Garde appariée δ — tranchée** *(v10 : R-719, puis R-733, mot direct de Lazar ≈ 08:42 UTC le 29 : « go recommandations
   de conv sur N1 à N6 »)* : une garde par comparateur dans le minimum de la fiche ; **δ = 0,05** unique, avec sa phrase
   scellable — « au plus 5 points absolus de faux positifs de plus que chaque comparateur sur les épisodes honnêtes, au point
   de fonctionnement τ = 0,01 », sans promettre ni l'absence d'artefact ni un gain net ; **K_h = 10** exécutions honnêtes par
   unité, plancher dur 5 ; unités = **jumeaux honnêtes des unités d'épreuve**, chaque unité portant les deux classes,
   n_h = n_s, **n_h ≥ max(288 ; n80)** ; **b_plan = δ/4** fixé d'avance ; **une seule lecture**, « G1 non promue » sans nœud
   après lecture, règle scellée contre toute seconde fiche ; **aucune lecture de f_A avant G1** (P-9) ; au pilote, on ne
   mesure que la dispersion des comparateurs (nœud avant scellement si elle dépasse ρ ≈ 0,17) ; **aucune marge θ** (instruite à
   part avant toute modification de N-056). *(v11, CL3-11)* Repli écrit (honnêtes seules tirées par graine, après simulation
   de validité) si le devis des sabotés ne porte pas 288 par mode (N3) ; coût de K_h = 10 : nœud de devis (N2) ; la règle
   « max(288 ; n80) » vient de R-719 (relayée), R-733 la reprend. Appui : à K_h = 10, la synthèse P-26 donne ≥ 0,86 pour le minimum des huit gardes
   à 288 unités sous ses lois ; la contre-lecture v5 donne la fiche ≥ 0,99 à 300 unités dans ses écarts, sans avoir essayé
   288 ; à 160 unités, non (R-731).

**Ce qui menace G1, dit honnêtement (v9, R4).** (i) **Les juges** : sur 180 notations rejouées, aucune cellule n'atteint
0,99 de scores finis (pièce 29-2) ; si la cellule redéfinie ne tient pas, le format de G1 est à revoir, quel que soit le
dimensionnement (R-671). (ii) **La garde** : presque muette sous ≈ 150 unités honnêtes (pièce 29-6) ; G1 coûtera donc **au
moins 288 unités d'épreuve par mode, chacune portant des épisodes honnêtes et sabotés** (R-733, N3 ; CL2-16), pas des dizaines. (iii) **Les organismes** : aucun organisme saboté n'existe ; le
critère 2 de G0 (organismes à dose-réponse) n'a pas avancé ; et le pilote mesure ce qui peut tuer la banque — « absence de
dose diffuse avec dommage = arrêt de la banque » (R-680). (iv) **Le coût** : banque complète de l'ordre de 300 à 1 400 USD,
au-delà des 90 accordés (section 3, instruments). G0 reste à **deux critères sur huit**.

**Le collisionneur « évasion et moniteurs » (GO-2026-10-28-03)** tournait au moment de la rédaction de la v8 ; il est fini

---

# Pièce C — calendrier et financement (programme d'entretien v12, extraits sur G0 et l'échéance) — `programme-entretien-taif-v12.md`, `2b930e01…`

    dans sa forme confirmée. Confiance élevée. *Rien n'en est dit au fonds dans ce programme.*
11. **Les arrêts par filtre** : **aucun nombre au fonds** (CL3-03), confiance élevée.
12. **Si G0 échoue fin novembre** : aucune règle de repli n'est écrite. Recommandation : une phrase de toi aujourd'hui ; *sans
    mot*, dire tel quel « no fallback rule is written yet ».
13. **Ce que chaque palier livre, et quand** : question la plus probable d'un financeur ; la proposition envoyée en donne une
    partie (GC fin du mois 2, G1 fin du mois 4), non lue ici. Recommandation : préparer aujourd'hui une ligne par palier.
14. **Une ligne de registre « R-609 remplace R-468 »** (CL3-10) : si tu le confirmes ; sinon le texte dit « superseded in
    practice ».
   d'octobre, section 8), organismes de 70 milliards, réplication sur une seconde famille. **À préparer par Lazar si possible
   aujourd'hui** (ligne de calcul).
3. **Si G0 échoue fin novembre**, avant le début du financement : les critères de G0 sont gelés (N-027) et une porte ne bouge
   pas (section 1 bis) ; **aucune règle de repli écrite** sur le palier financé. À dire tel quel, ou à trancher.
4. **La revue de sécurité externe** : ni relecteur, ni calendrier, ni taux (rien n'a avancé). Réponse vraie : « not yet
   commissioned; it is a budget line and a gate, not a formality ».
5. **La garde des contenus en quarantaine** : branches orphelines d'un dépôt privé, empreintes vérifiées, accès consignés
   (R-624, R-625) ; incident des clés exposées (point 9 ci-dessus).

---

# Pièce D — règles gelées du programme (CLAUDE.md, R1 à R14) — `CLAUDE.md`, `83fb08c9…`

- R1 Préenregistrement scellé (hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt) avant toute expérience décisive, simulation comprise ; aucune lecture de résultat avant scellement.
- R2 Chaque préenregistrement est contre-lu par un sous-agent neuf qui ne l'a pas écrit ; lui donner explicitement les fichiers à lire ; sinon le signaler.
- R3 Aucun run visant un signe positif.
- R4 Symétrie : un résultat suspect de propreté, positif ou négatif, déclenche le même audit ; trop beau = réserve.
- R5 Toute garde d'arrêt testée sur un cas sain et sur un artefact ; aucun repli silencieux.
- R6 Tout dépôt reçoit une empreinte compagnon `.sha256` ; tout chiffre d'un document renvoie à un chemin et une empreinte.
- R7 Provenance par transcription non opposable : aucun chiffre de l'état de l'art sans vérification sur PDF empreinté, page citée.
- R8 Anti-faux-gap : zone vierge = question ; limitation d'un papier ≠ trou du champ ; zones vierges séduisantes vérifiées plus durement.
- R9 Graines par `numpy.random.SeedSequence` (numpy ≥ 1.25), dérivées par tâche, consignées dans un manifeste par run (configuration et empreinte, versions, graines, commit).
- R10 Arrêts par PID ou identifiant d'instance, jamais par motif de ligne de commande.
- R11 Fichier qui semble vide ou absent : vérifier sur disque et par empreinte avant de le déclarer absent.
- R12 Versions dans les noms ; nouvelle version = nouveau nom ; on n'écrase jamais ; livrables d'une tâche en zip versionné.
- R13 Verdict de porte prononcé par un sous-agent neuf (ni auteur du préenregistrement ni de l'analyse), qui applique les critères gelés ; scellé, puis soumis à Lazar pour GO.
- R14 Chaque session commence par la routine de reprise et finit par une passation.
- Routine (tu décides, tu consignes dans `registres/decisions.md`) : code, bibliothèques, tests, lectures, fichiers, tout travail sur processeur.
- Run factice de bout en bout : `python -m controle_ia.run_factice`.
