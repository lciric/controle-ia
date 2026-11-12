"""Texte v2 (brouillon, non scellé) = texte scellé v1 + écart 1 (option 2). Arguments : V1 SORTIE ORG COMMIT67 BUNDLE67_SHA
CONF_V8_SHA. Remplace : l'en-tête de statut, les sections 12.3, 12.4, 13 (paragraphe du GO et ligne), 16 (blocs v67) ; insère
la section « Écart 1 » avant « Documents qui font foi ». Tout le reste est le v1 à l'octet."""
import hashlib, importlib.util, os, re, sys
V1, SORTIE, ORG, COMMIT, BUNDLE, CONF8 = sys.argv[1:7]
t = open(V1, encoding="utf-8").read()
sys.path.insert(0, ORG)
spec = importlib.util.spec_from_file_location("l67", os.path.join(ORG, "demonstrations", "boucle_reelle_v67.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()

def entre(debut, fin):
    i, j = t.index(debut), t.index(fin)
    assert t.count(debut) == 1 and t.count(fin) == 1 and i < j
    return i, j

# 1. en-tête
i, j = entre("# Préenregistrement — la plus petite course réelle", "- **Rédacteurs** :")
entete = """# Préenregistrement — la plus petite course réelle de la boucle complète de l'organisme d'idéation, v2 (écart 1, brouillon)

**Statut : brouillon du texte v2, non scellé, non contre-lu.** Texte v2 = le texte scellé v1
`preenregistrement-boucle-reelle-organisme-v1-v1.md` (`46d7545b489a2037ede235d843ef8a0c504461a0a2d697af5db40de2400fd89d`) **à l'octet**,
sauf : cet en-tête ; la section « Écart 1 » insérée avant « Documents qui font foi » ; les sections 12.3, 12.4 et 16 réécrites ;
dans la section 13, le paragraphe du GO et la ligne inscrite. Tout passage du v1 qui nomme le code v66, la configuration v6,
le lanceur `boucle_reelle_v66.py`, le bloc `plan-gele-v66` ou GO-2026-11-10-11 comme pièce **de la course** se lit, dans ce
texte, comme nommant respectivement le code v67, la configuration v8, le lanceur `boucle_reelle_v67.py`, le bloc `plan-gele-v67`
et GO-2026-11-12-06 ; les passages qui racontent l'histoire du v1 (rédaction, contre-lectures, empreintes d'alors) restent tels
quels. Il devient le texte scellé, sous le nom `preenregistrement-boucle-reelle-organisme-v1-v2.md`, après sa contre-lecture
(R2) et une vérification courte du différentiel v1 → v2.

Ce qui suit, jusqu'à la section « Écart 1 », est l'en-tête du v1, inchangé.

"""
t = t[:i] + entete + t[i:]

# 2. section Écart 1
k = t.index("## Documents qui font foi (chemin, empreinte sha256)")
ecart = f"""## Écart 1 — sortie du proposeur (texte v2)

- **Motif** : les deux courses sous le v1 se sont arrêtées au premier appel (issue C5 « non jugeable (arrêt) ») ; la seconde,
  parce que la réponse du proposeur Kimi a été **coupée par sa borne de sortie** (46 714 jetons dont 46 711 de raisonnement,
  borne fixée par le plafond de session de 0,50 USD) : `docs/notes/organisme-boucle-reelle-v1/course-v66/rapport-course-v66-poste-local-v2.md`
  (branche `donnees/course-organisme-v66-poste-local-v1`, `89b97faf2c7ec75350e44cd8b0ba3283645c84d47fa495350a8429206c407f28`).
  Lever la borne de jetons ne suffisait pas : le code v66 arrêtait toute commande externe à 1 800 s, quel que soit le délai
  de la configuration (`pole/adaptateur_commande_v64.py` l. 166, `pole/adaptateurs.py` l. 622) ; ≈ 52 600 jetons au plus au
  débit observé (≈ 30,1 jetons par seconde).
- **Décision** : option 2 de l'écart 1 (`docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/ecart-1-brouillon-2.md`),
  mot direct de Lazar, verbatim : « Recommandation : option 2 : go ; Recommandation : (a), confiance 0,75 go ; » (R-2426,
  12:26 UTC) ; ligne **GO-2026-11-12-06** (section 13).
- **Changements, et eux seuls** :
  1. **Code v67** (tête `{COMMIT}`, parent `7e415cba`) : deux fichiers neufs, `pole/adaptateur_commande_v67.py`
     (`commandes_v67` : l'adaptateur de chaque commande externe reçoit `fournisseurs.<nom>.delai_s` ; **garde 24** : délai de
     l'adaptateur réel fini, > 0, ≤ 7 200 s, `--delai-s` de la commande présent une fois et inférieur d'au moins 30 s) et
     `demonstrations/boucle_reelle_v67.py` (copie du lanceur v66 : rôles réels par `commandes_v67`, garde 24 jouée avec la
     configuration, blocs `empreintes-du-code-v67` et `plan-gele-v67`, délais au manifeste) ; essais
     `essais/test_boucle_reelle_v67.py` et banc `essais/mutations_boucle_reelle_v67.py`. **Aucun fichier v66 ni antérieur
     n'est modifié** ; le cœur v66, la lecture gelée v66 et le lecteur du registre des GO v66 sont ceux du v1.
  2. **Configuration v8** (`{CONF8}`) = v6 avec : `plafonds_session.proposeur` 0,5 → 1,5 USD ; dans la commande de Kimi,
     `--max-sortie-proposeur` 65 536 → 131 072 (défaut documenté de `max_completion_tokens` pour `kimi-k3.1-pro`) et
     `--delai-s` 1 750 → 7 150 ; `fournisseurs.kimi.delai_s` 1 800 → 7 200 ; `arrets.a3_delai_s.kimi` 1 800 → 7 200 (non lu
     sur le chemin de la course). Argon : délais inchangés ; sa borne effective de sortie passe d'≈ 9 000 à ≈ 29 000 jetons par
     le plafond de session partagé (dit).
  3. **Relais Kimi** lancé avec `--delai-amont-s 7200` et `--delai-silence-s 1800` (section 12.3, point 6 ; défauts 1 800
     et 600 s). **Argon inchangé** : commande 1 750 s, adaptateur 1 800 s, relais lancé comme sous le v1.
  4. **Plan gelé** : seules changent `configuration_sha256` et `go` (section 16) ; plafonds, parts, montant, durée inchangés.
- **Effet sur les critères de lecture** : aucun (sections 4 à 9 et 14 inchangées ; la lecture gelée ne lit ni la configuration
  ni le GO). Le rapport dit que c'est la **troisième tentative** sous ce dessin et rapporte les trois relevés ensemble (R4).
- **Effet sur la dépense** : pire cas des modèles sous les bornes 39,00 USD (Kimi 32,30 ; Argon 6,70 ; v1 : 35,30), sous les
  parts (Kimi 33, Argon 7) ; un appel du proposeur Kimi : pire cas réservé ≈ 1,35 USD, jusqu'à ≈ 73 minutes au débit observé ;
  attendu ≈ 3 à 4 USD de modèles. Dépense du v1, ≈ 1,19 USD, sous GO-2026-11-10-11.

"""
t = t[:k] + ecart + t[k:]

# 3. sections 12.3 et 12.4
i, j = entre("### 12.3 Sur la machine de la course, avant le lancement", "## 13. Devis")
v1_123 = t[i:j]
s = v1_123
def rr(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b)
rr("### 12.3 Sur la machine de la course, avant le lancement (préalables écrits ; contre-lecture du code v66, section 6)",
   "### 12.3 Sur la machine de la course, avant le lancement (préalables écrits ; contre-lecture du code v66, section 6 ; texte v2 : code v67)")
rr("Arbre de l'organisme à la tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7` (paquet git versé, vérifié par\n`git bundle verify`)",
   f"Arbre de l'organisme à la tête **`{COMMIT}`** (code v67 ; paquets git versés, vérifiés par `git bundle verify` et appliqués\ndans l'ordre : v65 `4660197e…`, v66 `84ab119f…`, v67 `{BUNDLE[:8]}…`)")
rr("1. La suite des neuf fichiers d'essais (`essais/test_registre_go_v66.py`,",
   "1. La suite des dix fichiers d'essais (`essais/test_boucle_reelle_v67.py`, `essais/test_registre_go_v66.py`,")
rr("2. Le banc : `python3 -I -B essais/mutations_boucle_reelle_v66.py --processus 4` → 133 tuées sur 133, code 0.",
   "2. Le banc : `python3 -I -B essais/mutations_boucle_reelle_v67.py --processus 4` → 151 tuées sur 151, code 0 (le banc v66\n   porté sur le code v67, et 18 mutations neuves).")
rr("`python3 -I -B demonstrations/boucle_reelle_v66.py SORTIE_ESSAI --a-blanc", "`python3 -I -B demonstrations/boucle_reelle_v67.py SORTIE_ESSAI --a-blanc")
rr("plafond posée ; y lire la description du bac (identité 64097) et les chemins résolus des commandes v6.",
   "plafond posée ; y lire la description du bac (identité 64097), les chemins résolus des commandes v6 et les délais vérifiés\n   par la garde 24 (`configuration.delais_v67` : Kimi 7 200 et 7 150 s, Argon 1 800 et 1 750 s).")
rr("--prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 446 --journal JOURNAL_KIMI",
   "--prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 446 --delai-amont-s 7200 --delai-silence-s 1800 --journal JOURNAL_KIMI")
rr("d'appels attendu si chaque test prend ses tours : il se donne toujours.",
   "d'appels attendu si chaque test prend ses tours : il se donne toujours. **Texte v2** : son délai d'appel à l'amont se donne\n   aussi, `--delai-amont-s 7200` (défaut 1 800 s : le relais couperait un appel du proposeur avant la commande), et son délai\n   de silence, `--delai-silence-s 1800` (défaut 600 s : une pause de plus de 10 minutes du flux de l'amont, raisonnement\n   compris, couperait l'appel, compté au pire cas) ; sa ligne « relais prêt » doit dire « délai 7200.0 s » et « silence\n   1800.0 s », relevée au rapport de course. **Argon** : son relais (`commande_argon_v56_nuit_v6.py servir`) se lance avec\n   les mêmes options que sous le v1 ; ses délais (commande 1 750 s, adaptateur 1 800 s) ne changent pas.")
rr("`DOSSIER_COURSE` = le dossier `configuration-v6/` versé", "`DOSSIER_COURSE` = le dossier `configuration-v8/` versé (`docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/configuration-v8/`)")
rr("la configuration v6 n'en\najoute aucun", "la configuration v8 n'en\najoute aucun")
rr("python3 -I -B demonstrations/boucle_reelle_v66.py SORTIE --preenregistrement prereg/preenregistrement-boucle-reelle-organisme-v1-v1.md \\\n    --heritage-depart DOSSIER_COURSE/heritage-depart-v65.json --configuration DOSSIER_COURSE/configuration-boucle-reelle-v6.json \\\n    --moteur reel --confirmer-moteur-reel --registre-go CHEMIN/registres/go.md --go GO-2026-11-10-11 \\",
   "python3 -I -B demonstrations/boucle_reelle_v67.py SORTIE --preenregistrement prereg/preenregistrement-boucle-reelle-organisme-v1-v2.md \\\n    --heritage-depart DOSSIER_COURSE/heritage-depart-v65.json --configuration DOSSIER_COURSE/configuration-boucle-reelle-v8.json \\\n    --moteur reel --confirmer-moteur-reel --registre-go CHEMIN/registres/go.md --go GO-2026-11-12-06 \\")
t = t[:i] + s + t[j:]

# 4. section 13 : paragraphe du GO et ligne
i, j = entre("**GO de la course (contre-lecture du code v66, CLV66-07).**", "## 14. Portée")
go13 = """**GO de la course (texte v2).** GO-2026-11-10-11 nomme la configuration v6 et ne reçoit jamais de ligne d'extension : la
course sous ce texte se lance sous la **ligne neuve GO-2026-11-12-06**, inscrite par Lazar le 12 novembre 2026 (R-2426) ; elle
remplace GO-2026-11-10-11 pour la suite de cette course, sans cumul (la dépense du v1, ≈ 1,19 USD, reste sous GO-2026-11-10-11).
Le lanceur la lit par `registre_go_v66.verifier_go_v66` (type « calcul », accordée par Lazar, en cours de validité, aucune
extension, montant **45 USD** exactement) ; ses conditions (code v67 contre-lu, configuration v8, ce texte contre-lu et scellé,
machine validée par l'essai à blanc `--bac reel` avant tout appel payant) sont tenues par la session qui lance. Le plafond de
5 USD de la machine n'est tenu par aucun code (comme au v1).

**La ligne inscrite**, recopiée à l'octet de `registres/go.md` (`main`, commit `6b1d3124`) :

```
LIGNE_GO
```

"""
t = t[:i] + go13 + t[j:]

# 5. section 16 : blocs v67
i = t.index("## 16. Blocs gelés lus par le lanceur (code v66)")
v1_16 = t[i:]
deb_j = v1_16.index("<!-- jeu-plante-v65 : début -->")
jeu = v1_16[deb_j:]
monde = re.search(r"monde_sha256: ([0-9a-f]{64})", v1_16).group(1)
heritage = re.search(r"heritage_depart_sha256: ([0-9a-f]{64})", v1_16).group(1)
jeu_sha = re.search(r"jeu_plante_sha256: ([0-9a-f]{64})", v1_16).group(1)
emp = "\n".join(f"{sha(os.path.join(ORG, r))}  {r}" for r in sorted(L.FICHIERS_GELES))
bloc16 = f"""## 16. Blocs gelés lus par le lanceur (code v67)

Lus par le lanceur v67 (`demonstrations/boucle_reelle_v67.py`), qui exige chacun des trois blocs une seule fois dans le texte.
Les 99 empreintes sont celles des fichiers gelés à la tête `{COMMIT}` (fermeture statique des deux programmes v67 : les 98 du v1,
moins `demonstrations/boucle_reelle_v66.py`, plus `demonstrations/boucle_reelle_v67.py` et `pole/adaptateur_commande_v67.py`) ;
`configuration_sha256` est celle de la configuration v8 ; `go` est GO-2026-11-12-06 ; les autres lignes du plan et le bloc
`jeu-plante-v65` sont ceux du v1, à l'octet.

<!-- empreintes-du-code-v67 : début -->
{emp}
<!-- empreintes-du-code-v67 : fin -->

<!-- plan-gele-v67 : début -->
generations: 2
cartes_par_proposeur: 6
m_e_bh: 22
bras: reel_seul
d9: mecanique
plafond_modeles_usd: 40
plafond_kimi_usd: 33
plafond_argon_usd: 7
plafond_machine_usd: 5
go: GO-2026-11-12-06
go_montant_usd: 45
duree_h: 72
configuration_sha256: {CONF8}
monde_sha256: {monde}
jeu_plante_sha256: {jeu_sha}
heritage_depart_sha256: {heritage}
<!-- plan-gele-v67 : fin -->

"""
t = t[:i] + bloc16 + jeu
open(SORTIE, "w", encoding="utf-8").write(t)
print("écrit", SORTIE)
