# Essai Lean, outillage D-1a — rapport des corrections du harnais — v2

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. **Écrit par** : l'auteur du harnais (sous-agent développeur,
  Opus 5.5, `claude-opus-5-5`). Heures relevées par `date -u` : contre-lecture vérifiée à 00:47:55 UTC ; rapport vers 01:16 UTC.
- **Lu, empreinte vérifiée** : `contre-lecture-harnais-d1a-v1.md` (`2077ae26…`, égale à son compagnon), décision R-2300.
- **Livrable** : commit `99192fd26717fa2db669cca05a10134e50bb0660` (arbre `a3afd4f54f5e4de84306e70de4ce6290ccf683ec`), branche
  `prep/lean-outillage-d1a-v2` partie de `558bcf97`, poussée seule, **sans fusion**. 49 fichiers neufs, **aucun fichier
  existant modifié** (R12 : modules v1 intacts ; v2 sous noms neufs). Empreintes : `empreintes-harnais-v2.txt`.
- **Essais** : 101 essais v2 passent ; les 68 essais v1 passent toujours (`journal-essais-r5-v2.txt`). **Mutations** : 45 sur
  des copies, **45 tuées**, aucune par délai (`journal-mutations-harnais-v2.json`, script
  `scripts/lean_essai_d1a_v2/mutations_harnais_v2.py`).
- Mutations sur copies seulement : import tracé (le module muté doit venir de la copie), `pytest -o pythonpath=<copie>/src
  <copie>/tests`, sans `PYTHONPATH` hérité.
- **Ni serveur, ni dépense, ni appel de modèle, ni appel à l'API de Hetzner** pendant ce travail.

## Verdict

Les cinq bloquants (CLL-01 à CLL-05) sont corrigés et éprouvés hors machine. CLL-06, CLL-07, CLL-09, CLL-11, CLL-12, CLL-13 et
CLL-15 sont corrigés, CLL-14 aussi (les neuf survivantes et leurs équivalents v2 sont tuées). Pour CLL-04 (b), CLL-08 et CLL-10,
ce qui dépend du comportement de Lean est en **réserve écrite** : rien n'a été compilé, aucune chaîne Lean n'est ici.

## Défaut par défaut

| Défaut | Correction (fichier v2) | Essai : cas sain / artefact | Mutation tuée |
|---|---|---|---|
| **CLL-01** lexique | `gardes_lean_v2.masquer` relit le texte comme un lecteur de lexèmes, identifiants lus en entier. Sont refusés : `«` ou `»` hors commentaire et chaîne, un littéral collé à un identifiant, à un nombre ou à un autre littéral, une apostrophe isolée. Un fichier refusé fait échouer G-L2, G-L3, G-L3+, G-L4 et G-L6. | Sain : `h'`, `x₁'`, `Nat.succ`, `'a'`, `r#"…"#`, `«…»` en commentaire et en chaîne. Artefacts : les 5 sources de la contre-lecture, plus `s!"…"` et `(f x)'` ; artefacts Lean `gl0_lexique_guillemets_v2.lean` et `gl0_lexique_colle_v2.lean`. | m01 à m04 |
| **CLL-02** genre et sûreté | Chaque nom attendu doit figurer dans l'énumération avec le genre « theoreme » (G-L4). Le contrôle imprime la sûreté de chaque constante ; « non-sure », « partielle » ou « absente » ⇒ G-L3. | Sain : énumération de théorèmes sûrs. Artefacts : `etape_1` de genre définition ; nom absent de l'énumération ; constantes non sûres et partielles ; dans le bac local, `partial def` ; artefacts Lean `gl4_etape_definition_v2.lean` et `gl3_partielle_v2.lean`. | m05, m06 |
| **CLL-03** couverture | Une constante non théorème est couverte seulement si elle est **imprimée**, ou descendante d'un inductif imprimé, ou auxiliaire d'une **liste fermée** (`match_n`, `_nativeDecide_n`, `_proof_n`, `proof_n`, `_auxLemma.n`, `eq_n`, `eq_def`) sous un nom imprimé ou attendu. | Sain : `Boite.mk`, `carre.match_1`, `etape_1._nativeDecide_1`. Artefacts : `enonce_item.i` non imprimée (le cas de la contre-lecture), `carre.cache`. Artefact Lean `gl6_instance_sous_attendu_v2.lean` : imprimée en entier pour le relecteur. | m07, m08 |
| **CLL-04** sortie du contrôle | Le contrôle n'est écrit sur **aucun disque** vu du bac : il passe par l'entrée standard (`lean --stdin --json`, tube de `systemd-run --pipe`). C'est le **harnais, processus distinct**, qui écrit `controle.out`. Le marqueur de fin porte un nonce de 128 bits tiré par item. Constantes et marqueur ne sont lus que dans le message JSON de la ligne de l'énumération. Code de sortie 0 exigé. Ligne brute, message hors des commandes, doublon, commande sans réponse, ou marqueur ailleurs ⇒ G-L7. G-L7 échoue si G-L3+ est désactivée. | Sain : contrôle complet. Artefacts : code 137 et code absent ; marqueur brut sans énumération (le cas de la contre-lecture) ; ligne brute ; nonce faux ou absent ; doublon ; message à une ligne hors du contrôle ; marqueur dans un avertissement ou dans le texte d'un énoncé. Dans le bac local : faux `lean` qui forge une sortie complète comme un initialiseur, puis sort avec 0. Artefact Lean `gl7_init_attribut_v2.lean` (`@[init]`). | m09 à m14 |
| **CLL-05** minuterie | `minuterie_v2.detruire_par_identifiant` réessaie **sans fin**, avec une attente de 5 s doublée jusqu'à 300 s, et journalise chaque échec. Elle ne sort que sur l'absence constatée ou sur un refus de nom. `hetzner_v2.transport_urllib` convertit aussi `OSError` et `http.client.HTTPException` en `ErreurHetzner`, sans le jeton. | Sain : destruction au premier essai. Artefacts : trois 503 puis succès ; transport qui casse (connexion fermée, délai) ; 25 échecs avec la borne d'essai (25 DELETE envoyés) ; refus de nom sans aucun DELETE ; délai, réinitialisation, `RemoteDisconnected` et `IncompleteRead` convertis, sans jeton dans le message. | m15, m16 |
| **CLL-06** plafond par GO | Une seule commande `minuterie_v2 creer-et-veiller` : GO vérifié ; seconde machine sous le même GO refusée sans mot de Lazar (journal des créations et registre des dépenses) ; déjà-dépensé lu dans `registres/depenses.md` ; prix horaire **lu dans l'API** ; devis sur le reste du plafond ; création ; `created` de l'API au journal ; **minuterie dans le même processus** ; une erreur après la création détruit le serveur. Détail ci-dessous. | Sain : `ccx33` à `hel1`, prix lu, IPv6 coupé. Artefacts : `ccx63` refusé avant toute création ; seconde machine (journal ; registre « Hetzner 175573391 ») refusée sans mot de Lazar, acceptée avec ; ligne non standard sans valeur déclarée ; valeur déclarée trop basse ; déjà-dépensé qui fait refuser un type sinon admis ; `created` manquant (serveur détruit) ; mauvais GO ; taux nul. | m17 à m20, s7 |
| **CLL-07** résidus | `executeur_bac_v2.residus_unite` lit le seul groupe de contrôle de l'unité de l'item (`systemctl show -p ControlGroup`, `cgroup.procs`) et arrête ces PID ; plus aucun arrêt par utilisateur. | Sain : unité absente, rien d'arrêté. Artefact : deux PID dans le groupe, arrêtés chacun par son PID. | m21 (survivante 6) |
| **CLL-08** `import Lean` | Le contrôle commence par `import Item` puis `import Lean`. | Texte du contrôle vérifié. **Réserve** : le comportement sur Lean n'est pas éprouvé. | m34 |
| **CLL-09** attributs | **Liste fermée** des attributs permis : `simp`, `reducible`, `irreducible`, avec les préfixes `local`, `scoped` et `-`. Tout autre attribut `@[…]` ou `attribute […]` ⇒ G-L3+. `deriving` ⇒ G-L6. Énoncés aussi imprimés avec `set_option pp.notation false`, exigés (G-L5) et transmis au relecteur. | Sain : 4 formes permises. Artefacts : `@[init]`, `@[app_unexpander]`, `@[tactic]`, `@[term_elab]`, `@[command_elab]`, `attribute [instance]`, `@[simp, init]`, `@[local instance]`, `deriving`. | m22 à m24 |
| **CLL-10** énumération | Aucun `open` ; noms `_root_.Lean.…` ; `Lean.Name.toString`, `String.append` et `Array.foldl` appelés explicitement ; aucune interpolation. | Texte du contrôle vérifié. **Réserve** ci-dessous. | m35 |
| **CLL-11** A12 | `garde_go_v2.autoriser_appels_modele` compare le GO cité **par égalité** à celui du pilote fixé au préenregistrement, puis vérifie le registre. | Sain : GO du pilote. Artefacts : GO d'une autre course qui cite « D-1b » ; GO du pilote non fixé ou mal formé ; GO-2026-11-10-13 ; GO absent ; la porte laisse le compteur intact. | m25 |
| **CLL-12** A7 | `budget_v2.CompteurPhase` : contrôler puis inscrire se fait sous un verrou. | Quatre fils à 4 USD sous un plafond de 8, avec une fenêtre de 50 ms : deux lancés, deux refusés. | m26 |
| **CLL-13** ordre | Le bac v2 refuse tout item tant que la sortie réseau n'est pas éprouvée fermée (`sonde_reseau_v1`, tampon dans `/run` lié au démarrage courant), aussi pour l'épreuve et `choisir-variante`. `hetzner_v2.verifier_coupure_nuage` lit le pare-feu du nuage par l'API. `minuterie_v2 detruire` sert de « détruire maintenant ». `piloter_poste_v2.sh` écrit l'ordre S1, P1, S2, P2, S3. | Sain : sonde fermée, tampon écrit puis réutilisé. Artefacts : sonde ouverte (aucun bac) ; autre démarrage (sonde relancée) ; pare-feu sans règle de coupure, avec une sortie de plus, ou non appliqué au serveur. | m27 à m29 |
| **CLL-14** survivantes | Un essai pour chacune des neuf (voir la colonne « essai » des lignes correspondantes) : énoncé absent, erreur hors des noms attendus, item en lecture seule et contrôle par l'entrée standard dans le second bac, sorties tronquées (gardes et exécuteur), résidus, IPv6, échéance et devis en ligne de commande. L'essai de la ligne de commande échoue si la minuterie démarre (au premier passage, s8 n'était tuée que par délai). | voir la colonne « essai » | s1, s2, s3, s4, s4b, s5, s5b, m21, s7, s8, s9 |
| **CLL-15** pannes du bac | `executeur_bac_v2.classer_execution` : une erreur `bwrap:`, `systemd-run` sans résultat ou un résultat inattendu ⇒ `ErreurBac` (arrêt). `timeout` ou `XCPU` ⇒ incident « délai » ; `oom-kill` ⇒ incident « mémoire ». Code de sortie ou autre signal ⇒ issue de l'item. `sortie_v2` ajoute le motif « mémoire ». | Sain : 7 classements. Artefacts : 3 pannes, chacune avec son motif. Avec un lanceur isolé factice, une durée dépassée remonte en « délai ». | m30 à m33 |

### CLL-06 : détail de la commande `creer-et-veiller`

- **GO** : le GO cité est vérifié dans le registre (calcul, Lazar, période, non révoqué).
- **Seconde machine** : refusée sans mot de Lazar. Les machines antérieures se lisent dans le journal des créations et dans le registre des dépenses (motif « Hetzner <identifiant> »).
- **Déjà-dépensé du GO** : lu dans les lignes de `registres/depenses.md` à 9 colonnes. Une ligne non standard exige une valeur déclarée, retenue si elle est plus haute.
- **Prix horaire** : lu dans l'API (type, lieu, plus l'adresse IPv4 primaire), converti au taux déclaré, et consigné.
- **Devis** : `verifier_devis` porte sur le reste du plafond du GO.
- **Création** : l'heure `created` de l'API va au journal.
- **Minuterie** : elle tourne dans le même processus, sans intervalle après la création. Une erreur entre la création et la minuterie détruit le serveur.

## Réserves écrites (ce qui ne s'éprouve pas sans Lean ni machine)

1. **CLL-04 (b), garde de fond** : je n'ai écrit aucun outil qui lise `Item.olean` sans exécuter les initialiseurs et qui
   rejoue les déclarations dans le noyau (`lean4checker` ou exécutable du harnais). La v2 ferme le chemin par trois défenses
   qui dépendent toutes du texte :
   - le lexique sûr ;
   - la liste fermée d'attributs, avec `initialize`, `#eval` et les commandes voisines interdits (G-L3+) ;
   - le contrôle passé par l'entrée standard avec un nonce.

   Si Lean exécute l'initialiseur d'un module importé, un code de l'agent qui passerait ces défenses pourrait encore lire le
   nonce dans la mémoire de son processus. `gl7_init_attribut_v2.lean` (champ « observer ») établira sur la machine si Lean
   exécute cet initialiseur.
2. **CLL-08 et CLL-10** :
   - **Interfaces non éprouvées.** Le métaprogramme d'énumération, variantes A et B, est écrit contre l'interface de Lean de
     mémoire : `Environment.header`, `ModuleIdx.toNat`, `ConstantInfo.isUnsafe`, `DefinitionVal.safety`, `Std.HashMap.fold`,
     `logInfo` dans `#eval`. Il en va de même pour `lean --stdin --json` et la lecture complète de l'entrée standard avant les
     imports.
   - **Choix de la variante.** `choisir-variante` tranche une fois, sur la chaîne installée ; si aucune variante ne passe,
     l'épreuve s'arrête.
   - **Surface d'instances.** Il reste une surface d'instances que l'agent peut fournir : la monade `CoreM` de `do`, `GetElem`
     de `moduleData[…]!`, la décidabilité de `cond`. Elle ne se ferme mécaniquement que par la garde de fond du point 1.
3. **Liste fermée des auxiliaires (CLL-03) et des attributs (CLL-09)** : à confirmer sur la chaîne installée (noms auxiliaires
   produits par `match`, `native_decide`, `simp`, équations).
   - Cas sains refusés, à écrire dans les consignes des bras : `s!"…"`, attributs hors liste dont `attribute [instance]`,
     `deriving`, `partial def`, instances anonymes.
4. **Version des gardes** : `G-L3+` (ajout du développeur) conditionne maintenant G-L7 ; la retirer exige la garde de fond
   (point 1). Le motif « mémoire » (`sortie_v2`) est neuf : à faire figurer au préenregistrement.
5. **Hors de ma branche** : `garde_calcul.py` ne connaît pas Hetzner (CLL-06). Je propose d'y ajouter la création de serveur
   (`POST /v1/servers` ou commande `creer-et-veiller`) parmi les lancements qui exigent un GO, mais je ne l'ai pas fait : ce
   n'est ni mon arbre ni ma consigne.
   - Le registre des dépenses gagnerait à garder ses 9 colonnes : la ligne de GO-2026-11-10-13 n'en a que 3, ce qui
     oblige l'opérateur à déclarer le déjà-dépensé.
6. **Non éprouvés, faute de machine joignable** :
   - le pilotage v2 et l'épreuve v2 ;
   - le lanceur réel (`systemd-run --pipe`, `bwrap`) ;
   - la lecture de `/pricing` et des pare-feu (forme de l'API citée de mémoire : la commande échoue fermée si un champ manque).
7. **Notes non demandées (CLL-16)** :
   - 16.2 (un avertissement remplaçait l'énoncé) est corrigé par la règle « un seul message d'information par commande » ;
   - 16.6 : le jour UTC est corrigé dans A12 v2 ;
   - 16.3, 16.4 et 16.5 restent ouvertes ;
   - 16.7 : mon rapport v1 se trompait. « 16,10 EUR pour 48 heures » est le prix **maximal** de `ccx33` (0,3355 × 48) ;
     à `hel1`, c'est 0,2260 × 48 = 10,85 EUR.

## Fichiers versés (non committés, scellés)

`rapport-corrections-harnais-d1a-v2.md` (ce fichier), `journal-essais-r5-v2.txt`
(`53f5cd2b46b6b5c3b7dbe27c42d88fe594cafea49ff2dc0d9365088ae2475824`), `journal-mutations-harnais-v2.json`
(`edfc62bf5367526667caf4aa630860b1ea8497926d9d0d5c57b3c05e636710ac`), `empreintes-harnais-v2.txt`
(`aabf9b3e0e9a025a1db75c7b8e2bc6b6272f30ea93dd47930df14ab8c3ff81e5`). Modules v2 :
`gardes_lean_v2.py` `6a5ad5e7500e4f3df8290437af355de93c9fc656c7eebbfb41ee2c0e5247190c`, `executeur_bac_v2.py`
`8d9a7986134cd428c1ec4fbd2f71f91ea74f4ca6f27e76f32132fe5cbcbe6018`, `minuterie_v2.py`
`3f5d44d6604750573646d58554c09d8c01627b511ea7cdf6a3bf1ba928c1eea6`, `hetzner_v2.py`
`fc68b0d5a2936a94423aa45416e37290af75d8a32da66c0d9b202a06ded48ca9`, `epreuve_isolement_v2.py`
`bfbf266ea7eaf2f12ebe4abab5b7e647b1a7ef311758e25e018afe666203e4dc`, `budget_v2.py`
`df19f77e0e14226300c1d2524513d3e07a9ed7cee092b5bb22c169dad1db2722`, `garde_go_v2.py`
`f87a03b9511dc2a3b4b3388437e530f6957326ad677e099ee10ce74f2321a242`, `sortie_v2.py`
`564be46746152da2165f43c8e472c7c16570302035858f03526b571e82c050db`.
