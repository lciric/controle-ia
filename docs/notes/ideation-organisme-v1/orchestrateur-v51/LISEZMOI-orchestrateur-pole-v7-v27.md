# Orchestrateur du pôle, version 0.7.0 — tranches d'épreuve, lignées de clé, journal des parties, démonstration de bout en bout du pari apparié — LISEZMOI v27

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), v27 écrite après le relevé `date -u` de 00:30:30
UTC le 28 octobre ; v1 à v26 gardées (R12). Code la part « à coder » de la conception v9 du pari apparié borné
(`../pari-de-signe/conception-pari-de-signe-v9.md`, D-S25 bis (5) : disjonction entre fiches d'une même lignée de clé ;
K8-2 : journal des parties calculées) et donne la **première course de bout en bout** du pari apparié sur une banque de
scores, sans agent ni dépense. v9, v26 et v27 pas encore contre-lues.

| changement | fichiers |
|---|---|
| `evaluer(monde, engagement, unites=None, etiquette_ordre=None)` : lecture d'une **tranche** de la partie (unités fraîches par génération) ; toute unité demandée hors de la partie est refusée ; une étiquette d'ordre facultative entre dans la graine de l'ordre secret (défaut : l'empreinte de l'engagement) | `pole/engagement_apparie.py` |
| `Lignees` : **une affirmation (clé de l'héritage), une fiche** — une relance sous un autre nom est refusée (`entrer`) ; **journal des parties** (`journaliser`, `parties_calculees`) et `verifier_sans_partie(generation, sans_partie)` qui refuse une déclaration « sans partie » contredite par le journal (K8-2) | `pole/engagement_apparie.py` |
| démonstration : banque synthétique à effet d'unité (sept cellules dont `blanc_jumeau` de même loi que `blanc`, bases (ii) et (iii), trois noires, juge ; une tranche d'épreuve par génération ; tranche 1 sans le mode « concentré »), proposeur mécanique (témoins vrais à quatre forces, faux « nul exact » et « signe inversé », contrastes au hasard de signe connu, fiche « G1 » en intersection-union contre cinq comparateurs avec garde), `Course` sous D-S24 et D-S25 bis (α / G_max par génération, budgets gardés, abandons après et avant partie, « sans partie » déclaré et confronté au journal), lecture L1 / L2 / L3 ; `--nul R` : garantie sous le nul complet (part des répétitions avec au moins une promotion, intervalle de Wilson) ; trois artefacts R5 (relecture d'une tranche, « sans partie » mensonger, relance sous un autre nom : refusés) | `demonstrations/demo_pari_apparie_v7.py` |
| essais : tranches (lue puis fraîcheur, hors partie refusée, étiquette d'ordre, partie entière inchangée), lignées et journal, démonstration (banque, signes connus, course et lecture à graine fixée, artefacts, nul répété) | `essais/test_v7_demo_pari_apparie.py` |

**Première course (graine 20261028, 4 générations × 40 unités, α = 0,05, τ = 0,05)** : L1 tenue (aucune fiche d'espérance
≤ 0 promue) ; L2 : témoins vrais promus aux forces 1,2 et 1,0 (génération 1), 0,5 (génération 2), 0,8 stratifié
« concentré » (génération 4, sa tranche 1 étant déclarée « sans partie ») ; force 0,1 non promue ; L3 : la fiche « G1 »
promue en génération 3 par la lecture e-BH pondérée (log e 6,62 pour un seuil de fiche seule de 7,02), comparateur le
plus faible : `dernier_etat` (iii). **Nul × 200** : aucune promotion (Wilson [0 ; 0,019], α = 0,05). Sorties scellées dans
le dossier passé au script (`banque.json`, `course.json`, `lecture-pari-apparie.json`) ; ce qui est dit ici se relit dans
`../pari-de-signe/demonstration-v27/` quand il y est versé.

Ce que la démonstration ne montre pas (dit) : des unités à effet partagé mais sans dépendance entre unités ; des cellules
de même variance (le signe connu des contrastes s'en déduit) ; aucune strate « mode de sabotage » croisée avec G1 ; pas
de retrait (D-S26 bis) exercé ; la lecture e-BH pondérée promeut une fiche sous son seuil de fiche seule quand d'autres
sont promues — c'est la règle, rapportée telle quelle (`bonferroni` à côté).

```
PY=/opt/venv-essaim-sim-v1/bin/python
$PY -I -B -m unittest                                                              # 273 essais, 185 s
$PY -I -B demonstrations/demo_pari_apparie_v7.py DOSSIER_NEUF --nul 200             # ≈ 70 s
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v27.txt
```

Le reste : LISEZMOI v26 à v1.
