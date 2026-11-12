# Lecture vérifiée — avis d'espèces seules sur la vérification non circulaire des artefacts produits en bac à sable — v1

## En-tête

- **Lecteur** : sous-agent neuf, Fable 5.1 (`claude-fable-5-1`), lignée conv-audit. Je n'ai écrit ni la question, ni les faits servis, ni l'avis, ni la réponse propre de conv-audit.
- **Heure** (`date -u`) : lecture commencée `Sun Nov  1 16:33:34 UTC 2026` ; écriture commencée `Sun Nov  1 16:37:19 UTC 2026`.
- **Régime** : lecture seule sur processeur ; aucun appel de modèle, aucun réseau, aucun fichier existant modifié, aucun scellement, aucun commit. Rien lu sous `donnees/` hors les deux fichiers nommés ci-dessous. Niveau méthode et défense : si un avis contenait une technique d'évasion, elle est désignée ici par sa classe, jamais recopiée.
- **Avis de Kimi** : le fichier `reponse-bac-a-sable-v1-kimi-v2.md` **n'existe pas** dans `docs/notes/reponses-especes-seules-2026-11-01-v1/` au début de cette lecture (vérifié par `ls`) ; le premier essai de Kimi a échoué. Cette lecture porte donc sur le seul avis d'Argon.
- **Statut** : avis d'une espèce consultée seule, sous GO ; il ne tranche rien. Cette lecture ne juge pas, ne recommande pas.
- **Empreintes SHA-256 recalculées (`sha256sum`) des fichiers lus** :

| fichier | sha256 | mots |
|---|---|---|
| `docs/notes/reponses-especes-seules-2026-11-01-v1/reponse-bac-a-sable-v1-argon-v1.md` (« A ») | `7468eba23c80df07eb928ce5f34c91757ccc90dafc6da1abd004a0cbda055e6c` | 7 390 |
| `donnees/questions-3-novembre-v1/question-verification-non-circulaire-v1.md` (« Q ») | `26f2db15e6abcd44b39e07c15e5a325da6e6428b2cc2177920fe22a08771086a` | 716 |
| `donnees/questions-3-novembre-v1/faits-bac-a-sable-non-circulaire-v1.md` (« F », lu entier, en trois morceaux) | `24064c98d1978eaae95d75dc0763683cf6f23202d4a43e1e5afce3ebc1520a0d` | 16 508 |
| `…/scratchpad/relecture/reponse-conv-audit-verification-non-circulaire-v1.md` (« C », réponse propre de conv-audit, lue pour comparaison, non jugée) | `d8a310315e8cfb59990fe6dc4781e90ee648c39000d6fb87d95a6909c2896051` | 8 610 |

Renvois : « A l. n », « F l. n », « C l. n ». Pièces de F : pièce 1 LISEZMOI v48 (étage de tests de mort) ; pièce 2 devis et plomberie de la machine jetable v3 ; pièce 3 relecture de la synthèse N12-N13 (carte N12) ; pièce 4 lecture vérifiée d'Avalon-M1 (extraits). « RAPPORTÉ » : source citée par l'avis, qu'aucune pièce ne sert ; vérification de forme seulement ; rien d'opposable (R7).

---

## 1. Avis d'Argon (A)

### 1.1 Chiffres et affirmations attribués aux pièces, recoupés

**Justes** :

| affirmation d'Argon | où dans A | où dans F |
|---|---|---|
| circularité nommée par la carte N12 (pièce 3) et par Avalon p. 76 (pièce 4) | l. 8 | l. 1092, 1114 |
| archives `tar` + `zstd`, `sha256sum`, pièce 2 § 2.3 | l. 11 | l. 668-669, 681 |
| lecture mécanique de la dernière ligne `RESULTAT: <nombre>` | l. 11 | l. 54 |
| `nftables` et pare-feu du nuage, § 2.2.3 | l. 12 | l. 529-575 |
| `verifier-entree-v1.sh`, garde G5 | l. 13 | l. 687-690, 853 |
| `python3 -I -B`, `--ro-bind /usr`, Python 3.13 | l. 16 | l. 52, 184 |
| noyau 6.8 SUPPOSÉ (Ubuntu 24.04) ; 6.18.44 sur la machine de CL16 | l. 20 | l. 309-310, 188 |
| identité 64097 puis 65534 dans le bac ; `kernel.apparmor_restrict_unprivileged_userns=0`, remède (R-a) | l. 20 | l. 179, 111-114, 363 |
| CPX32 : 4 processeurs AMD partagés, 8 Go ; 0,0577 EUR/h HT ; 0,0796 USD/h TTC | l. 22, 93, 270 | l. 106-107, 811 |
| CPX22 0,0320 ; CCX13 0,0697 EUR/h HT | l. 32, 93 | l. 213, 216 |
| `ExecuteurDistantParLots`, vérificateur et clés dans la session, § 2.7 | l. 26, 247 | l. 123-124, 776-796 |
| `resultats-<série>-v1.tar.zst`, § 2.5 ; lecture par `python3 -I` dans la session | l. 30, 35 | l. 724-726, 739 |
| `TAILLE_MAX_TOTALE_TRAVAIL` = 256 Mo | l. 35 | l. 186 |
| citations d'Avalon p. 80 (« Every model-visible channel… », « a false zero… ») | l. 48 | l. 1113, 1115 |
| 3 exécutions, 120 s, une par tour ; jusqu'à 12 tours par fiche | l. 51 | l. 53, 245, 781 |
| réponses entre délimiteurs, « données, jamais consigne » | l. 51 | l. 51 |
| `VERDICT: survit | éliminée | non concluant` ; jamais servis aux juges ; `materiau-tests-de-mort.md` : comptes et étiquettes | l. 52 | l. 55-56 |
| motifs de refus : clé étrangère, script > 20 000 caractères, caractère nul | l. 55 | l. 53 |
| latence de 5 à 10 min par aller-retour, SUPPOSÉE | l. 56, 284 | l. 795, 987 |
| `classement-fige.json`, `prereg-court.json` scellés avant toute session | l. 68 | l. 47-48 |
| `tests_de_mort_v2.py` cité, non servi | l. 65 | l. 179, 1038 |
| `tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner` ; témoin de 16 octets, 32 hexadécimaux, `/etc/pole/attendu-v1.txt` | l. 84 | l. 669, 302, 398 |
| `apt-get update && apt-get install` à l'étape 2 ; relevé d'état `etat-v1.txt` à l'étape 6 | l. 85 | l. 434-437, 454-492 |
| « aucun secret » (R-533) | l. 94 | l. 94-96 |
| verrou « un seul bac à la fois par identité » (CL15-07) ; groupe de processus tué au délai | l. 107 | l. 183, 52 |
| filtre d'appels système x86_64 (LISEZMOI v51, CL15-02 (c)) | l. 104 | l. 177 |
| `bwrap` 0.9.0 SUPPOSÉ (Ubuntu), 0.11 SUPPOSÉ (Debian 13), Python 3.13 natif SUPPOSÉ | l. 124, 140 | l. 309-312 |
| série P : 0,24 USD attendus, 3,19 USD au pire ; pièce 2 § 0.2 point 5 | l. 132, 277 | l. 819, 153 |
| 25 environnements sondés, p. 79 | l. 160 | l. 1116 |
| champ `test_de_mort` borné : 12 données, chemin 300 ; `index.json` scellé dans la liste blanche | l. 163 | l. 49-50 |
| l'amorce n'installe que `bubblewrap util-linux nftables zstd python3.13` | l. 179 | l. 437 |
| sondes de CL16 (`p_cl16.py`, `p_mutations.py`, `p_mut2.py`, `p_min.py`) dans un bloc-notes éphémère ; 547 essais en ≈ 340 s | l. 215, 221, 245 | l. 674-677, 185 |
| passe A (cgroup v2) puis passe B (cgroup v1) ; « ESSAI RÉEL NON JOUÉ » (G10) | l. 214, 256-258 | l. 699-718, 858 |
| CL16-01 : auto-tuée à 512 Mo, tient dès 640 Mo, défaut 1 024 Mo | l. 246 | l. 182 |
| scripts à écrire (`amorce-pole-v1.sh`, `sonde-sortie-v1.py`, `verifier-entree-v1.sh`, `destruction-serie-v1.sh`) ; essais G1 à G7, G12, G13 et artefacts (d) à (g) de G8 contre un faux serveur sur `127.0.0.1` | l. 249 | l. 843-845, 913-916 |
| disponibilité de `cpx32` (`nbg1`, `hel1`, `fsn1`), images, clé Launchpad de deadsnakes, lues avant le GO | l. 250 | l. 909-910, 236 |
| destruction par identifiant, `DELETE /v1/servers/<id>` puis 404 (G7) | l. 253, 284 | l. 753-755, 855 |
| au plus 12 allers-retours par série | l. 261, 284 | l. 794 |
| devis : S0 1 h / 2 h ; S1 1 h / 3 h ; P 3 h / 40 h ; attendu 6 h ≈ 0,48 USD ; pire 93 h ≈ 7,41 USD ; chien de garde + 14 h = 1,11 USD ; plafond 10 USD ; TVA 20 %, 1 EUR ≈ 1,15 USD | l. 270-279 | l. 815-832, 805-808 |
| modèles : 0,5 + 0,1 = 0,6 USD par fiche ; 3,00 USD (5 fiches) ; 7,20 USD (12) | l. 270, 281 | l. 821-823 |

Les calculs propres d'Argon sur ces bases sont exacts : 2 × 2 h × 0,0796 = 0,32 ; 3 × 3 h = 0,72 ; 2 × 3,19 = 6,38 ; 7,41 + 1,11 = 8,52 ; 12 × 12 = 144 (A l. 275-279, 285).

**Inexacts ou imprécis** :

| affirmation | où | ce que dit la pièce |
|---|---|---|
| le statut « non relu (technique) » est « cité en Pièce 4, § 4, p. 80 » | A l. 56, 68 | ce statut est le nôtre (v55, CL19-12, F l. 1115) ; la pièce 4 dit qu'il **rejoint** la phrase d'Avalon p. 80 ; il n'est pas dans Avalon |
| « non-déterminisme flottant (IEEE 754 …, Pièce 1, « Ce qui n'est pas vérifié en réel ») » | A l. 132 | la pièce 1 ne parle pas de nombres flottants ; elle liste des montages et bibliothèques SUPPOSÉS (F l. 71-73). Le risque est d'Argon, l'attribution est forcée |
| « Pièce 2, § 2.5 et § 2.7 » pour « le rôle `lecteur_test` tourne sur la session cloud » | A l. 30 | le § 2.7 dit que les clés et l'orchestrateur restent dans la session (F l. 783-784) ; le lecteur est une session de modèle (F l. 55), donc l'inférence tient, mais le § 2.5 ne le dit pas |
| « ExecuteurDistantParLots … Pièce 2, § 2.5 et § 2.7 » | A l. 26 | § 0 et § 2.7 (F l. 123, 786) ; pas § 2.5 |
| « 1 h attendue (≈ 40 min) ; … jusqu'à 2 séries S0 au pire » ; « 1 h attendue (≈ 45 min) × 2 séries (S1 + S1 rejouée) ; 3 h au pire × 3 séries » | A l. 275-276 | conforme au § 3.2 (S0 × 2, S1 × 3 au pire ; S1 + S1 rejouée en attendu, F l. 829-830) ; la ligne « S1 — 2 h attendues = 0,16 » recoupe bien « 1 + 1 » du § 3.2. Juste, mais A réagence les lignes du devis (S1 rejouée groupée avec S1) sans le dire |
| « témoin de 16 octets aléatoires (`TEMOIN` de 32 caractères hexadécimaux … § 2.1 et § 2.2.2) » | A l. 84 | juste (F l. 302 : 16 octets ; F l. 398 : 32 hexadécimaux) ; les deux renvois se complètent |

**Absents des pièces** (énoncés d'Argon sans appui dans F ; aucun n'est présenté comme tiré d'une pièce) :

- la définition de la base de confiance (l. 8) et son découpage en trois hôtes (l. 10-13) : construction d'Argon ;
- « gVisor interpose un noyau en Go en espace utilisateur (Sentry) » (l. 21) ; « Firecracker / Kata exigent la virtualisation imbriquée (`/dev/kvm`) sur la machine louée » (l. 22) : connaissances générales, RAPPORTÉ ; la pièce 2 ne dit rien de `/dev/kvm` ni de l'informatique confidentielle (A le dit lui-même, l. 93) ;
- « capacité théorique $\log_2(4) = 2$ bits par test de mort » (l. 56) : calcul d'Argon, qui compte quatre étiquettes (trois verdicts plus « non relu ») ; C compte $\log_2 3 \approx 1{,}58$ (C l. 121) ;
- « seuil éliminatoire $\tau = 1$ accès » (l. 166, 175) et « taux de fausses alertes théoriquement nul » pour un script sans énumération (l. 165) : raisonnements d'Argon, non mesurés ;
- toutes les suites publiques nommées en Q6 (l. 199-209) : **aucune n'est dans les pièces** (l'assembleur le dit, F l. 7) ; c'est ce que Q6 demandait ;
- les mentions `/proc/<pid>/status` (`NoNewPrivs`, `CapEff`, `Seccomp`) (l. 229) : contrôle de propriétés, hors des pièces ;
- « confiances méthodologiques » 0,85 / 0,50 / 0,90 / 0,80 / 0,80 / 0,60 / 0,90 / 0,85 : les siennes.

### 1.2 Réponse à chaque question posée

- **Q1** — Base de confiance en trois lieux : hôte vérificateur (noyau, `sha256sum`, extracteur déterministe, analyseur de `RESULTAT:`, horloge), canal de sortie (sérialiseur, pare-feu), hôte d'exécution (hyperviseur ou gestionnaire de conteneur, mécanisme d'isolation, script d'amorce vérifiant l'empreinte d'entrée) (A l. 10-13) ; exclus : tout l'espace utilisateur du bac, les outils de hachage internes, le noyau invité d'une machine virtuelle légère (A l. 15-17). `bwrap` garde le noyau partagé entier dans la base, d'autant que le remède (R-a) ouvre les espaces de noms ; gVisor réduit la surface ; Firecracker/Kata changent la classe par la frontière matérielle, au prix de la virtualisation imbriquée sur une machine déjà virtuelle (A l. 20-22). Trois options (1a `bwrap` + vérificateur en session ; 1b gVisor ; 1c microVM) ; confiance 0,85 que 1a suffit à briser la circularité d'Avalon, 0,50 sur `/dev/kvm` en CPX32 (A l. 25-29). Option manquante : exécution WebAssembly (WASI) sans système invité (A l. 31).
- **Q2** — Deux régimes : la boucle intra-fiche (3 exécutions, sorties renvoyées entre délimiteurs, temps, motifs de refus) a une bande passante large ; la boucle inter-générations (comptes et étiquettes) est étroite, environ 2 bits par test, à condition qu'aucun horodatage fin ni taille d'archive ne figure dans le matériau (A l. 50-56). Confiance 0,90 que le canal inter-générations est trop étroit pour apprendre une évasion complexe, mais que le canal intra-fiche permet de sonder l'environnement (A l. 62). Garde : remplacer les sorties brutes par un gabarit strict (code de retour, présence de la ligne `RESULTAT:`), ou arrêt dès une sonde d'intégrité (A l. 63). Option manquante : exécution en un seul tour, sans rétroaction après contact avec le vrai bac (A l. 64). Pièce qui trancherait : le code du formatage des réponses dans `tests_de_mort_v2.py` (A l. 65).
- **Q3** — Les archives déterministes et le témoin prouvent l'identité entrée-sortie **sous l'hypothèse d'un noyau hôte intègre** ; `apt-get` au démarrage n'est pas reproductible dans le temps, seul `etat-v1.txt` permet un contrôle a posteriori (A l. 83-85). Un journal d'appels système collecté par le noyau hôte hors du bac atteste la séquence, avec deux limites : les conditions de course entre vérification et usage dans l'interposition (classe nommée, pas de recette), et l'invisibilité des calculs en mémoire entre deux appels (A l. 87-89). L'attestation matérielle répond à un modèle de menace disjoint (opérateur du nuage) ; aucune offre confidentielle documentée dans les relevés ; la machine n'a aucun secret (A l. 91-94). Options 3a (liaison logicielle actuelle), 3b (plus journal `auditd`/eBPF et mesure d'intégrité IMA), 3c (fournisseur confidentiel) ; confiance 0,80 sur 3b (A l. 97-101). Garde : empreinte du script calculée hors du bac **avant** le montage en lecture seule ; journalisation après la fin du groupe de processus (A l. 102, 107).
- **Q4** — Antériorités : Thompson 1984, double compilation diverse de Wheeler, programmation en N versions (Avižienis et Chen), réfutation de l'indépendance par Knight et Leveson, systèmes à N variantes (A l. 123-127). Gain élevé contre les artefacts propres à une implémentation ; **nul contre le contournement sémantique de la métrique** (deux bacs rendent fidèlement le même nombre truqué) (A l. 130-131). Coût : série P doublée (0,24 → 0,48 USD attendus ; 3,19 → 6,38 au pire) plus les faux désaccords si l'accord porte sur l'égalité exacte plutôt que sur le franchissement du seuil (A l. 132). Options 4a (aucune), 4b (systématique), 4c (**sélective** sur les seules fiches « survit ») ; confiance 0,80 sur 4c (A l. 136-139). Garde : même arbre Python en lecture seule, seule la couche d'isolation varie (A l. 140). Option manquante : variantes décalées sur la même machine (A l. 141).
- **Q5** — Un script honnête n'a besoin que de trois ensembles de chemins (bibliothèque standard, dossier de travail, fichiers de `index.json`) ; canaris hors de ces chemins → fausses alertes théoriquement nulles sauf parcours générique ; seuil gelé à 1 accès (A l. 163-166). Limite : le canari est une liste noire ; mesure complémentaire : **liste blanche** de tous les accès fichiers et sous-processus après l'initialisation de l'interpréteur, comptage des accès hors liste (A l. 169-170). Options 5a (canaris passifs) 0,60 ; 5b (canaris + liste blanche) 0,90 (A l. 174-176). Pire cas : une bibliothèque scientifique qui sonde le matériel au démarrage ; garde : étalonner le profil de base en S1 et le soustraire (A l. 177). Option manquante : n'exposer dans le bac que les ≤ 12 fichiers nommés (A l. 178). Condition : aucune différence de comportement immédiat ne doit révéler qu'un canari a été touché (A l. 182).
- **Q6** — Suites nommées avec lien : Linux Test Project (sous-suites `containers`, `syscalls/seccomp`), `kselftest` (`seccomp`, `mount`, `user`, `cgroup`), suite d'essais de Bubblewrap (`tests/test-run.sh`), tests d'appels système de gVisor (`test/syscalls`), tests d'intégration et de sécurité de Firecracker, outils de l'Open Container Initiative (`runtime-tools`), audit d'hôte (`lynis`, `docker-bench-security`) (A l. 199-209). Lecture : passage à 100 % = condition nécessaire d'hygiène, jamais preuve ; une suite teste l'outil générique, pas notre ligne de commande, d'où le maintien des sondes de CL16 ; un seul échec arrête, un succès complet ne réduit aucune couche externe (A l. 212-216). Options 6a (suites + sondes en S1, confiance 0,85) ; 6b (sondes de CL16 seules) (A l. 220-222). Garde : jouer les suites dans une passe dédiée, jamais sur l'instance d'une série P (A l. 223). Option manquante : vérification statique de la politique (graphe des montages, filtre d'appels système au repos) (A l. 224). Ce qui réfuterait : une suite verte sur `/usr/bin/bwrap` alors que l'invocation réelle omet un drapeau — d'où la lecture de `/proc/<pid>/status` d'un processus lancé par l'orchestrateur (A l. 229).
- **Q7** — Ordre : (1) hors machine, 0 USD : verser v51, v52 et les sondes dans git ; corriger CL16-01 ; écrire `ExecuteurDistantParLots` (le point clé : le vérificateur reste dans la session) ; ajouter au lanceur les canaris passifs et la vérification d'intégrité de l'arbre en lecture seule, avec témoin cas sain et artefact ; écrire les scripts de plomberie et jouer G1 à G7, G12, G13 contre le faux serveur ; lire la disponibilité par l'API (A l. 244-250) ; (2) série S0 ; (3) série S1 augmentée des suites publiques et des témoins canaris ; (4) série P par lots (A l. 252-261). Peut attendre : Firecracker/gVisor, redondance systématique, attestation matérielle, tiers externe (A l. 264-266). Devis illustratif : le tableau reprend le devis v3 poste par poste et ajoute une ligne « redondance diverse » optionnelle (+ 0,24 USD intégral, ≤ 0,08 sélectif, + 3,19 au pire par série doublée) et la ligne des modèles (A l. 272-281). Ce qui réfuterait : 144 allers-retours fiche par fiche, ou passes A et B bloquées (A l. 285).

### 1.3 Sources citées (toutes RAPPORTÉ, aucun PDF servi)

| source | état | remarque |
|---|---|---|
| Rushby 1981, « Design and Verification of Secure Systems », SOSP / OSR 15(5) | RAPPORTÉ | forme plausible, seule chez Argon |
| Agache et al. 2020, Firecracker, NSDI 20 | RAPPORTÉ | plausible |
| Young et al. 2019, « The True Cost of Containing: A gVisor Case Study », HotCloud 19 | RAPPORTÉ | plausible |
| Lampson 1973, « A Note on the Confinement Problem », CACM 16(10) | RAPPORTÉ | plausible |
| Kemmerer 1983, « Shared Resource Matrix Methodology », TOCS 1(3) | RAPPORTÉ | plausible |
| Zarov et al. 2026, Avalon-M1, annexe K pp. 76-80 | tirée de la pièce 4 (auteurs, F l. 1101 ; pages 76, 79, 80, F l. 1112-1116) | juste ; le PDF n'est pas servi |
| Lamb et Zacchiroli 2022, « Reproducible Builds », IEEE Software 39(2) | RAPPORTÉ | plausible |
| Garfinkel 2003, « Traps and Pitfalls… », NDSS | RAPPORTÉ | plausible |
| Sailer et al. 2004, IMA, USENIX Security | RAPPORTÉ | plausible |
| Thompson 1984, CACM 27(8) | RAPPORTÉ | identique à C l. 199 |
| Wheeler 2005, ACSAC, et thèse 2009 | RAPPORTÉ | identique à C l. 201 |
| Avižienis et Chen 1977, COMPSAC | RAPPORTÉ | C cite Avizienis 1985 (TSE) ; deux textes différents, non contradictoires |
| Knight et Leveson 1986, TSE SE-12(1) | RAPPORTÉ | identique à C l. 207 |
| « Berger, Rodrigues, Liskov et Castro (2001), BASE » | RAPPORTÉ, **suspecte** | de mémoire, les auteurs de BASE (SOSP 2001) sont Castro, Rodrigues et Liskov ; « Berger » n'y figure pas. À vérifier |
| Cox et al. 2006, N-Variant Systems, USENIX Security | RAPPORTÉ | plausible |
| Spitzner 2003, « Honeytokens » ; « Honeypots: Tracking Hackers » 2002 | RAPPORTÉ | plausible |
| Bowen et al. 2009, « Baiting Inside Attackers Using Decoy Documents », SecureComm | RAPPORTÉ | plausible |
| Provos 2003, « Improving Host Security with System Call Policies », USENIX Security | RAPPORTÉ | plausible |
| Larson 2002, « Testing Linux with the Linux Test Project », OLS | RAPPORTÉ | plausible |
| Dijkstra 1970, « Notes on Structured Programming » ; citation sur les essais et les défauts | RAPPORTÉ | citation connue ; « p. 6 » non vérifiable |
| liens des suites publiques (LTP, kselftest, bubblewrap, gVisor, Firecracker, runtime-tools, lynis) | RAPPORTÉ | adresses de dépôts publics, de forme régulière ; non ouvertes (aucun réseau) |

Aucun chiffre tiré de ces papiers n'est repris par Argon.

### 1.4 Vérification du niveau « défense et mesure seulement »

Consigne de Q : « aucune technique d'évasion, aucun exploit, aucun code offensif, aucun cas concret ».

- **Suites nommées** : toutes sont des suites publiques de conformité ou d'audit (LTP, kselftest, bubblewrap, gVisor, Firecracker, runtime-tools, lynis, docker-bench-security). Aucune suite d'évasion, aucune reproduction de faille publiée (contrairement à C l. 434, qui nomme un sous-ensemble du LTP rejouant des failles connues et le met sous décision de Lazar, Argon ne le mentionne pas).
- **Défenses nommées** : vérificateur hors du bac, liste blanche d'accès, canaris passifs, journal d'appels système hors du bac (`auditd`, eBPF, mesure d'intégrité), montage chirurgical, arbre Python en lecture seule, exécution en un seul tour, gabarit strict des retours, contrôle de `/proc/<pid>/status` : toutes défensives.
- **Techniques d'évasion recopiées** : **0**.
- **Classes de risque nommées sans recette** : **2**. (a) En Q2, « sondage de l'environnement par rétroaction entre tours » : l'expérimentateur lit les sorties d'une première exécution et ajuste la suivante (A l. 62-63) ; c'est la description d'un canal, sans aucune commande ni cible. (b) En Q3, « condition de course entre vérification et usage dans l'interposition d'appels système » (A l. 89) : classe connue de la littérature citée (Garfinkel 2003), nommée pour justifier la mesure d'intégrité au niveau de l'inœud, sans construction. Aucune des deux n'est un cas concret.
- **Code offensif** : aucun ; les seuls fragments cités sont des noms de drapeaux, de fichiers et d'appels système, tous repris des pièces ou de la documentation publique, au service de la mesure.

### 1.5 Ce que l'avis ne répond pas

- **Q1** : « qu'est-ce qui décide le verdict » n'est pas distingué de « qu'est-ce qui confine » : la base de confiance d'Argon est une base de confinement et de transport ; le fait que le chiffre lu par le vérificateur est **imprimé par le script de l'agent** (F l. 54 : « la dernière ligne `RESULTAT: <nombre>` ») n'est pas traité comme une circularité. C l. 37-45 en fait son point central ; Argon le frôle seulement en Q4 (« gain nul si la fonction de vérification est mal spécifiée », A l. 131).
- **Q2** : « lesquelles comptent pour un optimiseur qui ne voit que le verdict » reçoit une réponse de débit (2 bits), pas une analyse de ce que vaut un bit quand le vérificateur croit une auto-déclaration ; le statut « non concluant » mieux traité qu'« éliminée » comme incitation n'est pas examiné.
- **Q3** : le coût de l'attestation matérielle « pour une machine louée » n'est pas chiffré (constat d'absence dans les relevés, A l. 93) ; le scellement progressif des journaux n'est pas évoqué.
- **Q5** : le taux de fausses alertes est posé « théoriquement nul » sans protocole de mesure sur un corpus honnête ni borne statistique ; aucun seuil pour la liste blanche autre que « 1 accès ».
- **Q6** : les liens ne sont pas datés ni versionnés ; aucune règle de comptage des essais ignorés.
- **Q7** : le devis reprend celui de la pièce 2 sans ligne pour les canaris ni pour les suites publiques (comptées dans S1 sans heure ajoutée) ; les témoins préenregistrés demandés en (g) sont nommés (A l. 248, 257) mais sans prédiction chiffrée ni critère de lecture gelé.
- **(h) vérification extérieure** : traitée en une phrase (« tout tiers peut rejouer les empreintes a posteriori », A l. 266) ; ni qui, ni comment, ni le nœud de contact externe.
- **Pire cas de Q7** : aucun.

---

## 2. Réponse propre de conv-audit (C), notée à part, non jugée

Pour la comparaison seulement : la circularité d'abord **logique** (le chiffre qui décide est déclaré par le script ; le recalcul du noyau porte sur une statistique que le script choisit, `recalcul_noyau` l. 510-540, C l. 37-40, 135-138) ; vérificateur **lié au préenregistrement**, calculé dans la session pour 0 USD, ou code de test écrit avant l'exécution par un traducteur séparé et joué sur une machine jetable **neuve** après destruction de celle de production (C l. 41-45, 110-115) ; base de confiance en deux colonnes, verdict contre confinement (C l. 59-82) ; attestation par réexécution, journal à scellement progressif, pas d'attestation matérielle (C l. 146-164) ; redondance : la diversité qui compte est celle de l'auteur du calcul, gVisor sur la machine de vérification en génération 2, divergence honnête à mesurer sur 100 scripts (C l. 188-228) ; canaris = borne inférieure du sondage maladroit, informatifs en course 2, jeton de 128 bits cherché dans les sorties, fiches impossibles plantées, pente par génération (C l. 232-263) ; suites publiques avec règle de lecture gelée en sept points (C l. 429-451) ; essai témoin n° 1 préenregistré (« chiffre faux sans effet », « bouts d'essai dorés », déterminisme, leurres) (C l. 453-494) ; ordre en sept étapes, plafond ≈ 12 USD (C l. 496-523). C note aussi que les « 25 environnements » sont p. 79 et non p. 76 (C l. 30-33), ce que la pièce 4 confirme (F l. 1116).

---

## 3. Pistes générales consensuelles

Un seul avis d'espèce est disponible ; les « accords » ci-dessous sont entre Argon et la réponse propre de conv-audit, notée à part comme le demande le mandat. Ils ne valent pas consensus entre espèces.

1. **Le vérificateur ne doit pas tourner sur l'hôte où le code de l'agent a tourné.** A : vérificateur et `lecteur_test` dans la session cloud, jamais sur la machine jetable (A l. 29-30, 247) ; C : verdict calculé dans la session ou sur une machine neuve, « jamais un hôte où du code d'agent a déjà tourné » (C l. 112-115).
2. **Une machine virtuelle légère change la classe du confinement, pas celle de la circularité ; un vérificateur dans la microVM serait aussi circulaire.** A l. 22, 29 (déport du vérificateur suffit même sous `bwrap`) ; C l. 83-89.
3. **Le canal intra-fiche (sorties entre délimiteurs, motifs de garde) est la fuite riche ; le canal inter-générations est étroit.** A l. 55-56, 62 ; C l. 123 (« oui, riche : 3 exécutions et 12 tours »). Garde commune : **statut générique** servi à l'expérimentateur à la place des sorties brutes (A l. 63 ; C l. 139-140, 505).
4. **Constructions reproductibles et journaux ne prouvent pas « ce qui a tourné est ce qui a été relu » au-delà de l'intégrité du noyau invité ; l'attestation matérielle répond à un modèle de menace inverse (l'hôte contre l'invité) et peut attendre.** A l. 85, 89, 92-94 ; C l. 146-147, 155-164.
5. **Journal d'appels système collecté hors du bac, par le noyau hôte (`auditd`, eBPF), ciblé sur l'identité 64097.** A l. 88, 99 ; C l. 379-383.
6. **La redondance diverse ne protège pas contre un chiffre faux déclaré fidèlement par les deux bacs (défaillance de mode commun).** A l. 131 ; C l. 196-197. Antériorités communes : Thompson, Wheeler, N versions, Knight et Leveson (A l. 123-126 ; C l. 198-210). Les deux relèvent le coût des **faux désaccords** par non-déterminisme et la nécessité d'une tolérance ou d'un accord sur le seuil plutôt que sur l'égalité exacte (A l. 132, 145 ; C l. 206, 227-228, 399-400).
7. **Les canaris mesurent par liste noire ; ils laissent un angle mort ; il faut une mesure complémentaire** : A, liste blanche des accès (A l. 169-170) ; C, désaccord chiffre déclaré/recalcul, jeton cherché dans les sorties, pente par génération (C l. 246-254, 260-261). Les deux exigent l'absence de différence de comportement révélant le canari (A l. 182) ou son placement hors de tout chemin de données (C l. 238).
8. **Taux de fausses alertes à étalonner sur un témoin honnête en série S1, avant tout seuil éliminatoire.** A l. 177, 183 ; C l. 235, 262-263.
9. **Suites publiques : LTP (`containers`, `seccomp`), kselftest `seccomp`, suite de bubblewrap, `test/syscalls` de gVisor, tests de Firecracker, runtime-tools de l'OCI, lynis** sont nommées par les deux (A l. 199-209 ; C l. 433-439). **Lecture commune** : une suite éprouve les mécanismes, jamais notre politique (nos arguments) ; un succès complet n'est pas une garantie ; un échec arrête (A l. 212-216 ; C l. 272-276, 442-451).
10. **Ordre** : travaux hors machine d'abord (exécuteur par lots, scripts, essais contre le faux serveur), puis S0, puis S1 augmentée des suites et des témoins, puis P ; Firecracker/gVisor en production, attestation matérielle et tiers extérieur peuvent attendre (A l. 244-266 ; C l. 289-301, 496-523).
11. **Le devis de la pièce 2 est repris comme base ; le surcoût de la vérification se compte en centimes de machine.** A l. 270-281 ; C l. 303-304, 484-494.

---

## 4. Pistes originales (une seule source)

**Argon seul :**

- Base de confiance en **trois lieux** (hôte vérificateur, canal de sortie, hôte d'exécution), avec l'horloge des délais et l'extracteur d'archive comptés dedans (A l. 10-13).
- Le remède (R-a) (`apparmor_restrict_unprivileged_userns=0`) **élargit la surface des appels système liés aux espaces de noms** et maintient le noyau partagé entier dans la base (A l. 20).
- Virtualisation imbriquée (`/dev/kvm`) comme condition de Firecracker/Kata sur une machine déjà virtuelle ; test de présence à faire en S0 ; CCX13 dédié comme repli (A l. 22, 32).
- Option **WebAssembly (WASI déterministe)** sans système invité (A l. 31).
- **Capacité du canal inter-générations ≈ 2 bits par test** ; les fuites de temps sont amorties par la latence de 5 à 10 min du poste de passage, à condition qu'aucun horodatage fin ni taille d'archive ne figure dans le matériau (A l. 56).
- **Exécution en un seul tour** (script validé à l'avance, sans rétroaction après contact avec le vrai bac) (A l. 64).
- `apt-get` au démarrage non reproductible ; `etat-v1.txt` comme seul contrôle a posteriori (A l. 85).
- Deux limites du journal d'appels système : condition de course vérification/usage (classe) et calculs en mémoire invisibles ; seule la réexécution les couvre (A l. 89).
- **Mesure d'intégrité IMA** sur l'hôte, journalisant l'empreinte de tout fichier exécuté ou lu par l'identité 64097 (A l. 99, 103).
- Garde : empreinte du script calculée **avant** son montage en lecture seule ; journalisation lancée après la fin du groupe de processus ; interdiction des fils concurrents ou figement des arguments au niveau de l'inœud (A l. 102, 107).
- **Redondance sélective** (4c) : rejouer dans un second bac les seules fiches « survit », avant leur entrée au matériau (A l. 138-139).
- Garde de la redondance : **même arbre Python** en lecture seule pour les deux bacs, seule la couche d'isolation varie (A l. 140) ; variantes décalées sur la même machine (A l. 141).
- **Liste blanche** stricte des accès (`openat`, `statx`, `newfstatat`, `access`, `readlink`, `getdents64`, `execve`) après l'initialisation de l'interpréteur, avec profil de base étalonné en S1 et soustrait (A l. 170, 177).
- **Montage chirurgical** : n'exposer que les ≤ 12 fichiers nommés dans `prereg-court.json`, pas le dossier de la tranche (A l. 178).
- Surveillance des canaris par `fanotify`/`inotify`/`atime` depuis l'hôte (A l. 174).
- Suites supplémentaires : `kselftest` `mount`, `user`, `cgroup` ; `docker-bench-security` (A l. 200, 209).
- **Vérification statique** de la politique d'isolation (graphe des montages, filtre d'appels système au repos) (A l. 224) ; contrôle de `/proc/<pid>/status` d'un processus lancé par l'orchestrateur lui-même (A l. 229).
- Jouer les suites publiques dans une passe dédiée, jamais sur l'instance d'une série P (A l. 223) ; vérifier empreintes ou signatures des suites avant inclusion dans l'archive de S1 (A l. 228).
- Ligne de devis « redondance diverse » : + 0,24 USD intégral, ≤ 0,08 sélectif, + 3,19 au pire par série P doublée (A l. 280).
- Réfutation du devis : 144 allers-retours si l'exécution est fiche par fiche (A l. 285).

**conv-audit seul (noté à part)** : le défaut de **liaison** (statistique recalculée déclarée par le script, C l. 135-138) ; verdict calculé dans la session ; machine de vérification **neuve et séquentielle** ; essai « chiffre faux sans effet » ; « bouts d'essai dorés » d'Avalon ; journal à scellement progressif ; jeton de 128 bits dans les leurres ; fiches impossibles plantées ; « non concluant jamais mieux qu'éliminée » ; lecteur strict de l'archive de retour ; règle de lecture gelée en sept points ; SandboxEscapeBench écarté (C l. 41-45, 82-87, 151-154, 232-263, 353-355, 440-451, 540-548).

---

## 5. Ce que je n'ai pas pu faire

- Lire un avis de Kimi : `reponse-bac-a-sable-v1-kimi-v2.md` absent au début de la lecture ; les sections « accords » reposent sur un seul avis d'espèce et sur la réponse propre de conv-audit, notée à part.
- Vérifier une seule source sur PDF ou ouvrir un seul lien (aucun réseau) : toutes RAPPORTÉ ; une est suspecte (auteurs de BASE).
- Vérifier contre `tests_de_mort_v2.py` (non servi) les affirmations sur le format des retours à l'expérimentateur ; Argon le nomme lui-même comme pièce qui trancherait (A l. 65).
- Vérifier les passages de la pièce 2 retirés par la règle 2 (voie recommandée, § 5) et par l'assembleur (sondes réseau) : si Argon y recoupe une recommandation retirée, je ne peux pas le voir.
- Trancher le compte de bits du canal inter-générations (2 chez A, 1,58 chez C) : les deux dépendent du nombre d'étiquettes servies, que la pièce 1 ne fixe pas (trois verdicts, F l. 55 ; « non relu (technique) » en v55, F l. 1115).

Horodatage de fin d'écriture : dernier relevé propre `16:37:19 UTC`, 1er novembre 2026 ; l'appelant relève l'heure au scellement.
