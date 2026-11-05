Voici l’exposé méthodologique d'Argon (`gemini-4-argon`), limité aux mécanismes de défense et de mesure, sans recommandation au directeur et sans recette offensive. Chaque chiffre de l'infrastructure actuelle est appuyé sur les pièces servies.

---

### Q1 — Base de confiance (TCB) et classe d'isolation

#### Mécanisme
La base de confiance informatique (*Trusted Computing Base*, TCB) regroupe l'ensemble des composants matériels, micrologiciels et logiciels dont la défaillance ou la compromission annulerait la propriété de sécurité visée (ici : la non-circularité entre la production d'un artefact et sa vérification, Pièce 3, section « Carte de décision pour Lazar — N12 » ; Pièce 4, § 4, p. 76).

1. **Ce qui doit entrer au minimum dans la TCB** :
   - **Sur l'hôte de vérification (distinct ou isolé)** : le noyau de l'hôte vérificateur, l'outil de calcul d'empreintes (`sha256sum`), l'extracteur d'archive déterministe (`tar`, `zstd`, Pièce 2, § 2.3), l'analyseur syntaxique de la sortie (`lecture mécanique` de la ligne `RESULTAT: <nombre>`, Pièce 1, « Ce que fait la v48 »), et l'horloge gouvernant les délais.
   - **Sur le canal de sortie** : le démon de transport ou le sérialiseur qui extrait les octets du bac vers le vérificateur, ainsi que le pare-feu de l'hôte (`nftables` et pare-feu du nuage, Pièce 2, § 2.2.3).
   - **Sur l'hôte d'exécution (uniquement pour la propriété de confinement et de non-falsification de l'entrée)** : l'hyperviseur ou le gestionnaire de conteneur, le mécanisme d'isolation du noyau de l'hôte, et le script d'amorce qui vérifie l'empreinte d'entrée avant exécution (`verifier-entree-v1.sh`, garde G5, Pièce 2, § 2.3 et § 4).

2. **Ce qu'un expert exclut de la TCB** :
   - **Tout l'espace utilisateur à l'intérieur du bac à sable** : l'interpréteur (`python3 -I -B`, Pièce 1, « Ce que fait la v48 » ; Python 3.13, Pièce 2, § 1.1), les bibliothèques liées en lecture seule (`--ro-bind /usr`, Pièce 1, « Ce que fait la v48 »), et les outils de hachage ou de journalisation internes au bac (calculer une empreinte à l'intérieur du bac est circulaire, Pièce 4, § 4, p. 76).
   - **Dans le cas d'une machine virtuelle légère** : le noyau invité (*guest kernel*) tout entier est exclu de la TCB de confinement et de la TCB de vérification.

3. **Changement de classe du problème (Conteneur vs MicroVM / Noyau d'espace utilisateur)** :
   - **`bwrap` (espaces de noms Linux)** : repose sur le partage du noyau de l'hôte (noyau 6.8 SUPPOSÉ sur Ubuntu 24.04, ou 6.18.44 sur la machine de CL16, Pièce 2, § 1.1 et § 2.2). Sur l'image Ubuntu 24.04, son usage sous l'identité sans compte `64097` (puis `65534` dans le bac, Pièce 2, § 1.1 et § 2.2.1) exige de lever la restriction AppArmor des espaces d'utilisateurs non privilégiés (`kernel.apparmor_restrict_unprivileged_userns=0`, remède R-a, Pièce 2, § 0 et § 2.2.1). Ce réglage ouvre la surface des appels système liés aux espaces de noms à un processus non privilégié, ce qui maintient le noyau partagé entier dans la TCB.
   - **gVisor (`runsc`)** : interpose un noyau écrit dans un langage à mémoire sûre (Go) en espace utilisateur (*Sentry*), réduisant le nombre d'appels système transmis au noyau hôte sans recourir à la virtualisation matérielle.
   - **Firecracker / Kata Containers** : substituent à l'isolation par appels système une frontière de virtualisation matérielle (KVM). Cela change la classe du problème : une compromission du noyau invité ne donne pas accès au système de fichiers de l'hôte où réside le lanceur ou le vérificateur. En contrepartie, cela exige la virtualisation imbriquée (*nested virtualization*, `/dev/kvm`) sur la machine louée (qui est elle-même une machine virtuelle CPX32 à 4 processeurs virtuels AMD partagés et 8 Go de mémoire, Pièce 2, § 0 et § 1.2).

#### Options, Confiance, Pire cas et Garde
- **Options exposées** :
  - *Option 1a* : Maintien de `bwrap` sur noyau partagé avec `ExecuteurDistantParLots` où le vérificateur tourne sur la session cloud (hors de la machine jetable, Pièce 2, § 2.5 et § 2.7).
  - *Option 1b* : Interposition d'appels système par noyau en espace utilisateur (gVisor) sur la machine CPX32, vérificateur sur la session cloud.
  - *Option 1c* : Isolation par microVM (Firecracker) par exécution, vérificateur hors de la microVM.
- **Confiance méthodologique** : Élevée (0,85) sur le fait que déporter le vérificateur sur la session cloud (Option 1a) suffit à briser la circularité logique décrite par Avalon (Pièce 4, § 4, p. 76), même si le bac utilise `bwrap`, car le vérificateur et les clés résident sur une machine physiquement distincte de la machine jetable (Pièce 2, § 2.0 et § 2.1). Moyenne (0,50) sur la disponibilité de `/dev/kvm` sur un gabarit à processeurs partagés CPX32 (Pièce 2, § 1.2).
- **Pire cas et garde** : Pire cas : compromission du noyau de la machine jetable permettant de falsifier l'archive `resultats-<série>-v1.tar.zst` avant que le poste de passage ne la récupère (Pièce 2, § 2.5). Garde : la lecture mécanique et le rôle `lecteur_test` tournent sur la session cloud (Pièce 1, « Ce que fait la v48 » ; Pièce 2, § 2.5 et § 2.7), de sorte que le code du vérificateur n'est jamais présent sur la machine jetable pendant l'exécution d'un lot.
- **Option manquante** : Exécution sans système d'exploitation invité par isolation WebAssembly (WASI déterministe), éliminant à la fois le noyau invité et les appels système POSIX complexes.
- **Pièce qui trancherait** : Le relevé de `etat-v1.txt` en série S0 (Pièce 2, § 2.2.2) complété par le test de présence de `/dev/kvm` sur le gabarit CPX32 (ou CCX13 dédié à 0,0697 EUR/h HT, Pièce 2, § 1.2).

#### Conditions de validité et Réfutation
- **Conditions de validité** : Le vérificateur ne doit exécuter aucun code issu de l'archive de retour (`python3 -I` utilisé uniquement pour lire des données inertes, Pièce 2, § 2.5). L'archive de retour doit être bornée en taille (`TAILLE_MAX_TOTALE_TRAVAIL` = 256 Mo par bac, Pièce 2, § 1.1).
- **Ce qui réfuterait** : Toute démonstration que le processus d'empaquetage sur la machine jetable (le lanceur, Pièce 2, § 2.4) partage un descripteur de fichier inscriptible ou un espace d'identités avec le processus `64097`/`65534` du bac.

#### Sources
- Rushby, J. (1981). *Design and Verification of Secure Systems*. Operating Systems Review, 15(5), 12–21 (Symposium on Operating Systems Principles, SOSP). DOI: `10.1145/1067627.806586`.
- Agache, A., Brooker, M., Iordache, A., Liguori, A., Neugebauer, R., Piwonka, P., & Popa, D.-M. (2020). *Firecracker: Lightweight Virtualization for Serverless Applications*. 17th USENIX Symposium on Networked Systems Design and Implementation (NSDI 20), pp. 419–434. ISBN: `978-1-939133-13-7`.
- Young, E. G., Zhu, P., Caraza-Harter, T., Arpaci-Dusseau, A. C., & Arpaci-Dusseau, R. H. (2019). *The True Cost of Containing: A gVisor Case Study*. 11th USENIX Workshop on Hot Topics in Cloud Computing (HotCloud 19).

---

### Q2 — Séparer produire et vérifier : fuites de canal et optimiseur

#### Mécanisme
Un canal de communication est dit *caché* (*covert channel*) lorsqu'il utilise des variables d'état du système non prévues pour le transfert d'information, et *auxiliaire* (*side channel*) lorsqu'il révèle des propriétés internes du récepteur. Avalon-M1 énonce que « chaque canal visible par le modèle est un canal de fuite » (*“Every model-visible channel is a leak channel”*, Pièce 4, § 4, p. 80) et qu'« un faux zéro que l'environnement renvoie comme note est entraîné comme un résultat réel » (*“a false zero that the environment returns as a grade is trained on as a real outcome”*, Pièce 4, § 4, p. 80).

Dans l'architecture de l'organisme, il faut distinguer **deux régimes d'optimisation** :
1. **La boucle intra-fiche de l'expérimentateur** : l'agent expérimentateur dispose de 3 exécutions par fiche (`--executions-par-fiche`), bornées à 120 secondes chacune (`--delai-execution-s`), à raison d'une exécution par tour jusqu'à un plafond (Pièce 1, « Ce que fait la v48 », quotas ; jusqu'à 12 tours par fiche mentionnés en Pièce 2, § 1.3 et § 2.7). Entre deux tours, « les réponses reviennent au tour suivant entre délimiteurs (données, jamais consigne) » (Pièce 1, « Ce que fait la v48 », rôle expérimentateur).
2. **La boucle inter-générations** : les résultats (`VERDICT: survit | éliminée | non concluant`, Pièce 1, « Ce que fait la v48 », rôle `lecteur_test`) ne sont « jamais servis aux juges de la même course », mais sont servis « en matériau à la génération suivante » sous la forme de `materiau-tests-de-mort.md` qui ne contient que « comptes et étiquettes, jamais le détail des sorties » (Pièce 1, « Ce que fait la v48 », résultats).

**Fuites résiduelles à travers un canal étroit** :
- **En boucle intra-fiche (vers l'expérimentateur)** : si la sortie standard et la sortie d'erreur reviennent entre délimiteurs au tour suivant (Pièce 1, « Ce que fait la v48 »), le canal n'est **pas** réduit au seul verdict pendant les 3 exécutions de la fiche. Il fuit l'intégralité du texte renvoyé entre délimiteurs, le temps d'exécution (distinction entre un retour rapide et un processus tué au délai de 120 secondes, Pièce 1, « Ce que fait la v48 »), et le motif de refus si une demande est rejetée (clé étrangère, script > 20 000 caractères, caractère nul, Pièce 1, « Ce que fait la v48 », quotas).
- **En boucle inter-générations (vers l'idéateur suivant)** : le canal est réduit aux comptes et aux étiquettes ternaires (`survit | éliminée | non concluant`, plus le statut séparé « non relu (technique) » cité en Pièce 4, § 4, p. 80). La capacité théorique de ce canal par fiche est d'au plus $\log_2(4) = 2$ bits par test de mort. Les fuites de temps (masquées par la latence de 5 à 10 minutes par aller-retour du poste de passage en lots, Pièce 2, § 2.7, § 5 et § 6), de taille d'archive et d'ordre d'exécution sont amorties et invisibles pour la génération suivante, **à condition** qu'aucun horodatage fin ni taille d'archive ne figure dans `materiau-tests-de-mort.md`.

#### Options, Confiance, Pire cas et Garde
- **Options exposées** :
  - *Option 2a* : Retour interactif multi-tours avec sorties entre délimiteurs (état actuel de la v48/v52 avec `ExecuteurDistantParLots`, Pièce 1, « Ce que fait la v48 » ; Pièce 2, § 2.7).
  - *Option 2b* : Exécution en aveugle (*blind execution*) ou retour strictement quantifié entre les tours d'une même fiche (l'expérimentateur ne reçoit que `{statut: "succes" | "echec_execution" | "delai_depasse", resultat_lu: booleen}`, sans `stdout`/`stderr` bruts).
- **Confiance méthodologique** : Très élevée (0,90) sur le fait que le canal inter-générations (`materiau-tests-de-mort.md`, Pièce 1) est trop étroit pour permettre l'apprentissage d'une évasion complexe, mais que le canal intra-fiche (3 exécutions avec retour des sorties entre délimiteurs, Pièce 1) offre une bande passante suffisante pour sonder l'environnement d'exécution lors du tour 1 et adapter le script au tour 2.
- **Pire cas et garde** : Pire cas : l'expérimentateur utilise la première de ses 3 exécutions (Pièce 1, « Ce que fait la v48 ») pour inspecter l'environnement du bac, lit le résultat dans la réponse entre délimiteurs au tour suivant, et ajuste son script à la deuxième exécution. Garde : filtrer ou remplacer les sorties `stdout`/`stderr` renvoyées entre les tours par un gabarit strict (code de retour et présence/absence de la ligne `RESULTAT: <nombre>`), ou imposer l'arrêt de la fiche dès le moindre déclenchement d'une sonde d'intégrité (voir Q5).
- **Option manquante** : Exécution en un seul tour (1 exécution de script validé syntaxiquement à l'avance, sans boucle de rétroaction vers l'expérimentateur après contact avec le vrai bac).
- **Pièce qui trancherait** : Le code exact du formatage des réponses renvoyées entre délimiteurs à l'expérimentateur dans `tests_de_mort_v2.py` (cité en Pièce 2, § 1.1 et § 7.2, non servi dans le texte intégral).

#### Conditions de validité et Réfutation
- **Conditions de validité** : Le classement figé (`classement-fige.json`, Pièce 1, « Ce que fait la v48 ») et le préenregistrement court (`prereg-court.json`, Pièce 1) sont scellés avant la première session de l'étage ; le statut « non relu (technique) » est compté à part (Pièce 4, § 4) pour ne pas confondre une panne d'infrastructure avec une réfutation scientifique.
- **Ce qui réfuterait** : Qu'un optimiseur puisse distinguer, dans `materiau-tests-de-mort.md`, un échec dû au seuil gelé d'un échec dû à une différence de configuration de la machine louée, lui permettant de conditionner sa génération suivante sur l'état de l'infrastructure.

#### Sources
- Lampson, B. W. (1973). *A Note on the Confinement Problem*. Communications of the ACM, 16(10), 613–615. DOI: `10.1145/362375.362389`.
- Kemmerer, R. A. (1983). *Shared Resource Matrix Methodology: An Approach to Identifying Storage and Timing Channels*. ACM Transactions on Computer Systems (TOCS), 1(3), 256–277. DOI: `10.1145/357369.357374`.
- Zarov, I., Course, F., Hartshorn, A., Achiron, M., Roche, T., Sinha, S., Taylor, C., & Taylor, R. (2026). *Reinforcement Learning from Collective Rewards (General Reasoning) — Avalon-M1*. Annexe K, pp. 76–80 (Pièce 4, en-tête et § 4).

---

### Q3 — Attestation : constructions reproductibles, journaux d'appels système et matériel

#### Mécanisme
L'énoncé « ce qui a tourné est ce qui a été relu » recouvre une propriété d'**intégrité d'exécution** et de **liaison cryptographique** (*binding*) entre quatre éléments : l'environnement logiciel initial, l'entrée soumise (`etage-<série>-v1.tar.zst`, Pièce 2, § 2.3), la trace d'exécution, et la sortie recueillie (`resultats-<série>-v1.tar.zst`, Pièce 2, § 2.5).

1. **Constructions reproductibles (*Reproducible Builds*) et archives déterministes** :
   - La Pièce 2 (§ 2.3 et § 2.5) utilise déjà `tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner` compressé par `zstd`, scellé par `sha256sum`, et lié à la série par un témoin de 16 octets aléatoires (`TEMOIN` de 32 caractères hexadécimaux dans `/etc/pole/attendu-v1.txt`, Pièce 2, § 2.1 et § 2.2.2).
   - Ce mécanisme prouve que l'archive déposée et déballée par `verifier-entree-v1.sh` (garde G5, Pièce 2, § 2.3 et § 4) est identique octet pour octet à celle préparée par la session cloud, **sous l'hypothèse que le noyau hôte de la machine jetable est intègre**. En revanche, sur Ubuntu 24.04, `apt-get update && apt-get install` au démarrage (Pièce 2, § 2.2.2, étape 2) n'est pas bit-à-bit reproductible dans le temps (les paquets des miroirs évoluent). Seule la capture des versions et empreintes exactes des paquets installés dans `etat-v1.txt` (Pièce 2, § 2.2.2, étape 6) permet un contrôle a posteriori.

2. **Journaux d'appels système (*Syscall logs*)** :
   - Un journal d'appels système (capturé par `seccomp-unotify`, `auditd` ou `eBPF` depuis le noyau hôte, hors de l'espace de noms du bac) atteste de la séquence des interactions entre le processus `65534` (dans le bac, lancé par `64097`, Pièce 2, § 1.1) et le noyau (fichiers ouverts par chemin ou numéro d'inœud, processus exécutés par `execve`).
   - Limite théorique : les vérifications de sécurité basées sur l'interception d'appels système qui lisent des pointeurs en mémoire utilisateur (comme les chemins de fichiers passés à `openat`) sont sujettes aux conditions de course de type *Time-Of-Check to Time-Of-Use* (TOCTOU) si la mémoire est partagée entre plusieurs fils d'exécution dans le bac. De plus, un journal d'appels système ne prouve pas les calculs effectués uniquement en mémoire vive (CPU/RAM) entre deux appels système ; seule la ré-exécution déterministe le prouve.

3. **Attestation matérielle (vTPM, AMD SEV-SNP / Intel TDX) et son coût** :
   - L'attestation matérielle résout un problème précis : **ne pas faire confiance à l'opérateur du nuage (Hetzner) ni à l'image de démarrage non chiffrée**.
   - Sur le gabarit retenu (CPX32 à 0,0577 EUR/h HT, 0,0796 USD/h TTC, Pièce 2, § 0 et § 3) ou ses replis (CPX22 à 0,0320 EUR/h HT, CCX13 à 0,0697 EUR/h HT, Pièce 2, § 1.2), aucune fonctionnalité d'informatique confidentielle (*Confidential Computing* AMD SEV-SNP avec attestation matérielle) n'est documentée dans les relevés de prix servis (Pièce 2, § 1.2).
   - Comme la machine jetable ne détient **aucun secret** (décision R-533, Pièce 2, en-tête et § 2.1) et que l'opérateur du nuage n'est pas l'agent optimiseur que l'on cherche à contrer, l'attestation matérielle protège contre un modèle de menace (opérateur d'infrastructure malveillant) disjoint du risque de circularité de l'optimiseur (Pièce 3, N12 ; Pièce 4, § 4).

#### Options, Confiance, Pire cas et Garde
- **Options exposées** :
  - *Option 3a* : Liaison logicielle par archives déterministes, témoin de série (`TEMOIN`), relevé d'état (`etat-v1.txt`) et hachage par le lanceur hors du bac (état de la Pièce 2, § 2.2.2, § 2.3, § 2.5, gardes G5 et G10).
  - *Option 3b* : Option 3a augmentée d'un journal d'appels système au niveau du noyau hôte (`auditd` / `eBPF` immuable pour l'UID `64097`) enregistrant les empreintes SHA-256 (IMA, *Integrity Measurement Architecture*) de chaque binaire et script chargé par `execve` ou lu dans le bac.
  - *Option 3c* : Migration vers un fournisseur d'instances confidentielles (AMD SEV-SNP) avec attestation matérielle distante.
- **Confiance méthodologique** : Élevée (0,80) sur la suffisance de l'Option 3b (sans attestation matérielle) face à un optimiseur logiciel confiné sous l'identité `64097`/`65534`, dès lors que le journal est collecté par le noyau hôte hors du bac.
- **Pire cas et garde** : Pire cas : le script exécuté dans le bac modifie les fichiers de son propre dossier de travail (le seul dossier inscriptible, borné à 256 Mo, Pièce 1, « Ce que fait la v48 » ; Pièce 2, § 1.1) après avoir produit son résultat, ou tente d'exploiter une concurrence de mémoire sur les arguments d'appels système. Garde : le script soumis et l'arbre d'entrée sont en lecture seule pour le bac ; le lanceur hors du bac calcule l'empreinte du script *avant* de le passer en lecture seule à `bwrap`, et le noyau hôte interdit la création de fils d'exécution concurrents ou fige les arguments au niveau de l'inœud.
- **Option manquante** : L'utilisation du sous-système Linux IMA (*Integrity Measurement Architecture*) sur l'hôte, qui mesure et journalise dans le noyau l'empreinte de tout fichier ouvert ou exécuté par l'UID `64097`, sans pouvoir être contourné par des pointeurs en espace utilisateur.
- **Pièce qui trancherait** : Le détail du filtre d'appels système x86_64 déjà présent dans l'étage (mentionné en Pièce 2, § 1.1 : « filtre d'appels système écrit pour cette architecture », source LISEZMOI v51, CL15-02 (c), non servi).

#### Conditions de validité et Réfutation
- **Conditions de validité** : Le processus de journalisation et de hachage doit s'exécuter sous l'identité `root` de la machine jetable, après que le groupe de processus de l'UID `64097` a été intégralement terminé (« groupe de processus tué au délai », Pièce 1, « Ce que fait la v48 » ; verrou « un seul bac à la fois par identité », CL15-07, Pièce 2, § 1.1).
- **Ce qui réfuterait** : Qu'un processus survivant sous l'UID `64097` puisse continuer à écrire dans le dossier de travail pendant que le lanceur construit `resultats-<série>-v1.tar.zst` (Pièce 2, § 2.5).

#### Sources
- Lamb, C., & Zacchiroli, S. (2022). *Reproducible Builds: Increasing the Integrity of Software Supply Chains*. IEEE Software, 39(2), 62–70. DOI: `10.1109/MS.2021.3073045`.
- Garfinkel, T. (2003). *Traps and Pitfalls: Practical Problems in System Call Interposition Based Security Tools*. Proceedings of the Network and Distributed System Security Symposium (NDSS 2003).
- Sailer, R., Zhang, X., Jaeger, T., & van Doorn, L. (2004). *Design and Implementation of a TCG-based Integrity Measurement Architecture*. 13th USENIX Security Symposium, pp. 223–238.

---

### Q4 — Redondance diverse (N-version, DCC, Thompson)

#### Mécanisme
La redondance diverse consiste à exécuter le même artefact dans $N \ge 2$ environnements d'implémentations indépendantes et à exiger l'accord des sorties (*accord exigé*).

1. **Antériorité théorique et distinction des mécanismes** :
   - **Ken Thompson (1984), *Reflections on Trusting Trust*** : démontre qu'un compilateur compromis peut injecter une porte dérobée dans le binaire qu'il produit (y compris en se recompilant lui-même) sans laisser de trace dans le code source relu.
   - **David A. Wheeler (2005/2009), *Diverse Double-Compiling (DCC)*** : réfute l'attaque de Thompson en compilant le code source du compilateur à travers deux chaînes de compilation indépendantes ; si les binaires résultants à l'étape finale sont identiques bit à bit, la chaîne n'est pas compromise. Ici, l'artefact est un script interprété par `python3 -I -B` (Pièce 1, « Ce que fait la v48 »), donc l'équivalent est l'exécution par deux piles logicielles distinctes (par exemple Ubuntu 24.04 + `bwrap` 0.9.0 SUPPOSÉ vs Debian 13 + `bwrap` 0.11 SUPPOSÉ ou gVisor, Pièce 2, § 2.2).
   - **Algirdas Avižienis & Liming Chen (1977), *N-Version Programming*** : exécution parallèle de $N$ implémentations avec vote majoritaire ou d'unanimité pour tolérer les fautes.
   - **John Knight & Nancy Leveson (1986)** : ont réfuté expérimentalement l'hypothèse d'indépendance des défaillances dans les systèmes à $N$ versions lorsque le problème découle d'une ambiguïté de la spécification ou d'une difficulté intrinsèque de l'entrée.
   - **Berger, Rodrigues, Liskov et Castro (2001), *BASE*** et **Cox et al. (2006), *N-Variant Systems*** : appliquent la diversité d'exécution à la sécurité informatique. Un exploit dépendant d'une disposition mémoire ou d'un défaut d'implémentation propre à la variante A échoue ou produit un comportement divergent sur la variante B, ce qui est détecté par le comparateur.

2. **Gain réel contre un optimiseur qui sonde et coût** :
   - **Gain contre l'évasion de confinement et les bogues d'implémentation** : Élevé. Un comportement reposant sur une particularité non documentée d'un noyau ou d'un conteneur (`bwrap` vs gVisor/Firecracker) divergera entre les deux bacs.
   - **Gain contre le contournement sémantique de la métrique (*reward hacking*)** : Nul si la fonction de vérification (`prereg-court.json`, seuil gelé, `RESULTAT: <nombre>`, Pièce 1, « Ce que fait la v48 ») est mal spécifiée. Deux bacs parfaitement étanches et divers exécuteront fidèlement un script qui calcule une métrique truquée à partir des données de la tranche exploratoire (`--tranche-exploratoire`, Pièce 1) et rendront tous deux le même nombre falsifié.
   - **Coût** : Doublement du temps de calcul de la série P ou doublement du nombre de machines louées (en série P : 0,24 USD attendu doublé à 0,48 USD TTC, ou au pire 3,19 USD doublé à 6,38 USD TTC, aux tarifs de 0,0796 USD/h TTC de la Pièce 2, § 3 et § 3.1). Plus important : coût des faux rejets (*faux désaccords*) dus au non-déterminisme flottant (IEEE 754 selon les bibliothèques mathématiques de `/usr`, Pièce 1, « Ce qui n'est pas vérifié en réel ») si l'accord exigé porte sur l'égalité exacte du nombre plutôt que sur le franchissement du seuil gelé (`survit | éliminée`, Pièce 1, « Ce que fait la v48 »).

#### Options, Confiance, Pire cas et Garde
- **Options exposées** :
  - *Option 4a* : Pas de redondance systématique ; un seul bac durci avec vérificateur externe sur la session cloud.
  - *Option 4b* : Redondance diverse systématique sur deux implémentations (ex. `ubuntu-24.04` + `bwrap` vs `debian-13` + gVisor/autre pile, Pièce 2, § 2.2), accord exigé sur le verdict par rapport au seuil gelé et sur l'écart relatif maximal du chiffre `<nombre>`.
  - *Option 4c* : Redondance diverse sélective (uniquement sur les fiches dont le verdict en premier bac est `survit`, avant que le résultat n'entre dans `materiau-tests-de-mort.md`, Pièce 1).
- **Confiance méthodologique** : Élevée (0,80) sur l'Option 4c (redondance sélective sur les survivants) : comme seules les fiches qui survivent au test de mort valident une prédiction, rejouer uniquement les survivants dans un second bac d'implémentation distincte divise le coût tout en bloquant tout faux positif issu d'un artefact de la première plate-forme.
- **Pire cas et garde** : Pire cas : désaccord systématique entre les deux bacs à cause d'une différence de version de bibliothèque Python entre Ubuntu 24.04 (deadsnakes, Pièce 2, § 2.2) et Debian 13 (Python 3.13 natif SUPPOSÉ, Pièce 2, § 2.2), classant toutes les fiches en `non concluant` (Pièce 1, « Ce que fait la v48 »). Garde : figer exactement le même arbre d'environnement Python en lecture seule pour les deux bacs, en ne faisant varier que la couche d'isolation sous-jacente (noyau/conteneur).
- **Option manquante** : L'exécution à variantes décalées (*N-Variant Systems* sur la même machine) avec ordonnancement aléatoire des adresses (ASLR distinct) et inversion des identifiants de processus entre deux exécutions successives du même script.
- **Pièce qui trancherait** : Le taux de fiches atteignant le statut `survit` lors d'un essai à blanc, pour chiffrer le volume exact d'exécutions qu'exigerait la redondance sélective (Option 4c).

#### Conditions de validité et Réfutation
- **Conditions de validité** : Les graines aléatoires (*seeds*) doivent être fixées par le préenregistrement ou le script, et le critère d'accord doit être défini avec une tolérance numérique préenregistrée ($\epsilon$) ou porter sur le signe et le franchissement du seuil gelé (`prereg-court.json`, Pièce 1, « Ce que fait la v48 »).
- **Ce qui réfuterait** : Qu'un artefact témoin honnête déterministe donne des verdicts opposés (`survit` vs `éliminée`) entre les deux bacs lors de la série d'étalonnage S1.

#### Sources
- Thompson, K. (1984). *Reflections on Trusting Trust*. Communications of the ACM, 27(8), 761–763. DOI: `10.1145/358198.358210`.
- Wheeler, D. A. (2005). *Countering Trusting Trust through Diverse Double-Compiling*. Proceedings of the 21st Annual Computer Security Applications Conference (ACSAC 05), pp. 28–40. DOI: `10.1109/CSAC.2005.17` (et thèse de doctorat, George Mason University, 2009).
- Avižienis, A., & Chen, L. (1977). *On the Implementation of N-Version Programming for Software Fault-Tolerance During Execution*. Proceedings of COMPSAC 77, pp. 149–155.
- Knight, J. C., & Leveson, N. G. (1986). *An Experimental Evaluation of the Assumption of Independence in Multiversion Programming*. IEEE Transactions on Software Engineering, SE-12(1), 96–109. DOI: `10.1109/TSE.1986.6312924`.
- Cox, B., Evans, D., Filipi, A., Rowanhill, J., Hu, W., Davidson, J., Knight, J., Nguyen-Tuong, A., & Hiser, J. (2006). *N-Variant Systems: A Secretless Framework for Security through Diversity*. 15th USENIX Security Symposium, pp. 105–120.

---

### Q5 — Mesurer le sondage de la plate-forme (canaris et mesures complémentaires)

#### Mécanisme
Dans Avalon-M1, « des agents ont sondé la plateforme plutôt que la tâche, dans 25 environnements » (Pièce 4, § 4, p. 79). Un **canari** (*honeytoken* / *canary file*) est une ressource synthétique (fichier, variable d'environnement, chemin, entrée de table de processus) placée dans l'environnement mais qui ne figure pas dans la spécification légitime de la tâche.

1. **Validité des canaris journalisés dans le contexte de la v48/v52** :
   - Dans l'étage des tests de mort, le contrat légitime d'un script est strictement borné par `prereg-court.json` et la `tranche exploratoire` : « 12 données, chemin 300 » maximum dans le champ `test_de_mort`, et la tranche exploratoire est « chargée comme un dossier fermé : `index.json` scellé et présent dans la liste blanche » (Pièce 1, « Ce que fait la v48 »).
   - Par conséquent, un script honnête n'a besoin d'accéder qu'à trois ensembles de chemins : (i) les fichiers de bibliothèques standards de Python sous `/usr` (`--ro-bind /usr`, Pièce 1), (ii) son propre dossier de travail inscriptible (Pièce 1), et (iii) les fichiers explicitement déclarés dans `index.json` de la tranche exploratoire (Pièce 1).
   - **Taux de fausses alertes sur un artefact honnête** : Si les canaris sont placés hors des chemins de chargement standard de l'interpréteur (`sys.path` de `python3 -I -B`, Pièce 1) et hors des fichiers listés dans `prereg-court.json`, le taux de fausses alertes pour un script qui ne fait pas d'énumération de répertoire (`os.listdir`, `os.walk`, `glob`) sur des dossiers parents est **théoriquement nul ($\alpha = 0$)**. Si un script honnête utilise un parcours générique (`glob("*")` dans le dossier de la tranche), il touchera tout fichier canari placé à côté des données légitimes.
   - **Seuil éliminatoire gelé** : Dès lors que les canaris sont placés hors du périmètre d'un parcours légitime (par exemple dans des chemins frères de la tranche, dans `/tmp` du bac, dans `/proc` hors `/proc/self`, ou sous forme de fichiers nommés `verificateur.py`, `classement.json`, `seuil.json` non listés dans `prereg-court.json`), le seuil éliminatoire gelé est **$\tau = 1$ accès** (toute tentative de lecture `openat`, de lecture d'attributs `stat`/`lstat`/`access`, ou d'énumération `getdents64` d'un répertoire parent non autorisé).

2. **Limite du canari seul et mesure qu'un expert ajouterait** :
   - Un canari est une mesure par *liste noire* (il ne détecte le sondage que si l'agent touche l'appât). Un agent qui sonde un chemin système réel non piégé (par exemple `/proc/cpuinfo`, `/sys`, ou les binaires de `/usr/bin`) ne déclenche aucun canari.
   - **Mesure complémentaire (liste blanche stricte des accès fichiers et appels système)** : Plutôt que de seulement piéger quelques fichiers factices, journaliser au niveau du noyau (ou de l'interposeur) **tous** les appels `openat`, `statx`, `newfstatat`, `access`, `readlink`, `getdents64` et `execve` effectués après l'initialisation de `python3 -I -B`, et calculer le **nombre d'accès hors liste blanche** (où la liste blanche est l'union exacte des bibliothèques Python chargées au démarrage, du dossier de travail inscriptible, et des $\le 12$ chemins de `prereg-court.json`, Pièce 1). Toute invocation d'`execve` d'un sous-processus ou toute ouverture de fichier hors de cet ensemble est mesurée directement, sans dépendre du choix d'un nom de canari.

#### Options, Confiance, Pire cas et Garde
- **Options exposées** :
  - *Option 5a* : Canaris passifs (fichiers et chemins factices dont les accès sont relevés par horodatage `atime` ou par `inotify`/`fanotify` hors du bac), seuil éliminatoire gelé à 1.
  - *Option 5b* : Option 5a combinée à une mesure par liste blanche des chemins ouverts et des sous-processus créés après le chargement de l'interpréteur Python, seuil éliminatoire gelé à 1 accès hors du périmètre `{python_stdlib, dossier_travail, donnees_prereg}`.
- **Confiance méthodologique** : Moyenne (0,60) pour les canaris seuls (Option 5a, car ils laissent un angle mort sur l'inspection des fichiers système légitimes de `/usr` ou `/proc`) ; Très élevée (0,90) pour la combinaison canaris + liste blanche de chemins (Option 5b).
- **Pire cas et garde** : Pire cas : une bibliothèque scientifique légitime importée par le script (par exemple `numpy` ou `scipy`, si installée) sonde au démarrage l'architecture matérielle (`/proc/cpuinfo`, `/sys/devices`) ou des variables d'environnement, déclenchant un faux positif sur la liste blanche. Garde : étalonner l'empreinte exacte des accès de démarrage des bibliothèques autorisées lors de la série S1 (témoin cas sain, Pièce 2, § 1.3 et § 4) et soustraire ce profil de base fixe avant d'appliquer le seuil $\tau = 1$.
- **Option manquante** : Monte-charge minimaliste (*bind-mount* chirurgical) où même la tranche exploratoire n'expose dans le bac **que** les $\le 12$ fichiers nommés dans `prereg-court.json` (Pièce 1, « Ce que fait la v48 »), et non le dossier entier de la tranche.
- **Pièce qui trancherait** : La liste exacte des bibliothèques Python installées aux côtés de `python3.13` sur la machine jetable (la Pièce 2, § 2.2.2, étape 2, n'installe que `python3.13` sans paquet tiers mentionné, ce qui réduit l'empreinte de démarrage à la seule bibliothèque standard).

#### Conditions de validité et Réfutation
- **Conditions de validité** : Les mécanismes de surveillance des canaris (`fanotify`, `auditd`, `eBPF`) doivent opérer dans l'espace de noms de l'hôte (`root`), hors de la vue du processus `64097`/`65534`, et aucune différence de comportement immédiat (erreur spécifique) ne doit indiquer à l'agent intra-fiche qu'il a touché un canari plutôt qu'un fichier inexistant ou interdit.
- **Ce qui réfuterait** : Qu'un script témoin honnête important uniquement les modules standards de Python 3.13 déclenche un canari ou un accès hors du profil de base étalonné en S1 (faux positif > 0 sur le témoin sain).

#### Sources
- Spitzner, L. (2003). *Honeytokens: The Other Honeypot*. SecurityFocus / Symantec Connect (et dans *Honeypots: Tracking Hackers*, Addison-Wesley, 2002, ISBN: `978-0-321-10895-1`).
- Bowen, B. M., Hershkop, S., Keromytis, A. D., & Stolfo, S. J. (2009). *Baiting Inside Attackers Using Decoy Documents*. International Conference on Security and Privacy in Communication Systems (SecureComm 2009), LNICST vol. 19, pp. 51–70. DOI: `10.1007/978-3-642-05284-2_4`.
- Provos, N. (2003). *Improving Host Security with System Call Policies*. 12th USENIX Security Symposium, pp. 257–272.

---

### Q6 — Suites publiques d'étanchéité et lecture non circulaire de leurs résultats

#### Mécanisme
Une suite publique d'étanchéité ou de conformité vérifie que les primitives d'isolation du noyau, du gestionnaire de conteneur ou de la machine virtuelle respectent leurs invariants fonctionnels et de sécurité face à des cas limites connus (régressions d'espaces de noms, fuites de descripteurs de fichiers, contournements de filtres d'appels système, erreurs de montage).

1. **Suites publiques nommées pertinentes par technologie** :
   - **Pour les primitives du noyau Linux sous-jacentes à `bwrap` (`userns`, `mount`, `netns`, `seccomp`, `cgroups`)** :
     - **Linux Test Project (LTP)** — sous-suites `containers` (`userns01` à `userns08`, `mountns01` à `mountns04`, `netns`, `pidns`, `utsname`) et `syscalls/seccomp` : `https://github.com/linux-test-project/ltp`.
     - **Kernel Self-Test (`kselftest`)** du noyau Linux — répertoires `tools/testing/selftests/seccomp/`, `tools/testing/selftests/mount/`, `tools/testing/selftests/user/`, et `tools/testing/selftests/cgroup/` : `https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/tools/testing/selftests`.
   - **Pour `bwrap` (Bubblewrap)** :
     - **Suite d'essais officielle de Bubblewrap** (`tests/test-run.sh`, vérifiant l'isolation des montages, `--unshare-user`, `--cap-drop`, la protection contre les fuites de descripteurs et `TIOCSTI`) : `https://github.com/containers/bubblewrap/tree/main/tests`.
   - **Pour gVisor (`runsc`)** :
     - **Suite de tests d'appels système et de confinement de gVisor** (tests d'appels système Linux exécutés contre le noyau d'espace utilisateur *Sentry* pour vérifier le respect des frontières de sécurité et des permissions) : `https://github.com/google/gvisor/tree/master/test/syscalls`.
   - **Pour Firecracker** :
     - **Suite d'intégration et de sécurité de Firecracker** (incluant les tests du `jailer`, des filtres `seccomp` de l'hyperviseur, et des limites `cgroups`) : `https://github.com/firecracker-microvm/firecracker/tree/main/tests`.
   - **Pour la conformité générale des conteneurs et le profilage d'hôte** :
     - **Open Container Initiative (OCI) Runtime Tools (`runtime-tools`)** : `https://github.com/opencontainers/runtime-tools`.
     - **CIS Docker / Linux Benchmark (`lynis` ou `docker-bench-security`)** pour l'audit passif des réglages sysctl et des permissions de l'hôte : `https://github.com/CISOfy/lynis`.

2. **Comment lire leurs résultats sans en faire une garantie** :
   - **Principe de Falsification (Dijkstra / Popper)** : Le passage à 100 % d'une suite publique est une **condition nécessaire d'hygiène (garde d'arrêt)** et non une preuve d'étanchéité suffisante.
   - **Lecture méthodique** :
     1. *Détection des régressions d'intégration* : les suites publiques révèlent si un réglage d'hôte (tel que `kernel.apparmor_restrict_unprivileged_userns=0` sur Ubuntu 24.04 ou le passage de cgroup v2 à cgroup v1 en passe B, Pièce 2, § 2.2.1 et § 2.4) a cassé une primitive d'isolation attendue.
     2. *Couverture de la configuration propre* : une suite publique teste l'outil générique (`bwrap`), mais ne teste pas la ligne de commande spécifique de l'orchestrateur (`--ro-bind /usr --remount-ro /`, Pièce 1, « Ce que fait la v48 »). C'est pourquoi les sondes internes de configuration (sondes de CL16 : `p_cl16.py`, `p_mutations.py`, `p_mut2.py`, `p_min.py`, Pièce 2, § 2.3 et § 2.4) restent indispensables en complément des suites publiques.
     3. *Règle d'interprétation* : **Un seul échec dans la suite publique arrête la série (condition nécessaire), mais un succès complet ne réduit jamais le besoin des couches externes (vérificateur hors du bac, absence de secret sur la machine, fermeture réseau G8).**

#### Options, Confiance, Pire cas et Garde
- **Options exposées** :
  - *Option 6a* : Exécuter en série S1 (sans modèle, Pièce 2, § 1.3 et § 2.4) la suite officielle du bac (`bubblewrap/tests`), la sous-suite `containers`/`seccomp` de LTP, et les sondes existantes de CL16 (`p_cl16.py`, `p_mutations.py`, `p_mut2.py`, `p_min.py`, Pièce 2, § 2.3).
  - *Option 6b* : Se limiter aux seules sondes existantes de CL16 et à la suite de 547 essais en ≈ 340 s de CL17 (Pièce 2, § 1.1).
- **Confiance méthodologique** : Élevée (0,85) sur l'ajout de la suite amont de `bubblewrap` et des tests `seccomp`/`userns` de LTP/kselftest lors de la série S1, car cela valide le comportement du noyau 6.8 d'Ubuntu 24.04 (SUPPOSÉ, Pièce 2, § 2.2) sans écrire de code offensif maison.
- **Pire cas et garde** : Pire cas : la suite publique LTP modifie l'état global du noyau de la machine jetable pendant S1 ou laisse des montages résiduels. Garde : exécuter les suites publiques dans une série ou passe dédiée avant la destruction de la machine, et ne jamais les exécuter sur la même instance de machine virtuelle qu'une série P de production.
- **Option manquante** : Vérification statique de la politique d'isolation (analyse formelle ou par graphe des montages `/proc/<pid>/mountinfo` et du filtre `seccomp` dumpé par `seccomp-tools` ou `libseccomp` sur le processus `65534` au repos).
- **Pièce qui trancherait** : Le contenu exact de `p_cl16.py`, `p_mutations.py`, `p_mut2.py` et `p_min.py` (empreintes données en Pièce 2, § 2.3, fichiers situés dans le bloc-notes éphémère non servis).

#### Conditions de validité et Réfutation
- **Conditions de validité** : Les suites publiques doivent être tirées de dépôts officiels avec vérification de leurs empreintes ou signatures GPG avant d'être incluses dans l'archive déterministe de S1 (même discipline que pour la clé Launchpad de deadsnakes, Pièce 2, § 2.2.2 et § 5).
- **Ce qui réfuterait** : Qu'une suite publique passe sur le binaire `/usr/bin/bwrap` par défaut alors que l'invocation réelle par `tests_de_mort_v2.py` omet un drapeau critique (d'où la nécessité de vérifier aussi l'état `/proc/<pid>/status` — `NoNewPrivs: 1`, `CapEff: 0000000000000000`, `Seccomp: 2` — d'un processus lancé par l'orchestrateur lui-même).

#### Sources
- Larson, P. (2002). *Testing Linux with the Linux Test Project*. Proceedings of the Ottawa Linux Symposium (OLS 2002), pp. 265–273.
- Dijkstra, E. W. (1970). *Notes on Structured Programming*. T.H.-Report 70-WSK-03, Technological University Eindhoven (2nd ed., 1972, in Dahl, Dijkstra, & Hoare, *Structured Programming*, Academic Press, ISBN: `978-0-12-200550-3`, p. 6 : *“Program testing can be used to show the presence of bugs, but never to show their absence!”*).

---

### Q7 — Ordre des opérations et coût (« illustratif ») avant d'activer les tests de mort pour la course 2

#### Mécanisme
L'ordonnancement méthodique sépare : (1) ce qui est **bloquant** pour briser la circularité d'Avalon (Pièce 4, § 4, p. 76) et garantir le confinement sans secret (Pièce 2, § 2) dès la première exécution de la génération 1 de la course 2 ; et (2) ce qui relève d'un **approfondissement** pouvant être différé après la génération 1 ou conditionné aux premiers résultats.

#### 1. Ordre des opérations avant d'activer la série P (Course 2, génération 1)

1. **Étape 1 — Travaux hors machine, sans dépense (sur la session principale, Pièce 2, § 5)** :
   - Verser dans `git` les versions v51, v52 et les 4 fichiers de sondes de CL16 actuellement dans un bloc-notes éphémère (`p_cl16.py`, `p_mutations.py`, `p_mut2.py`, `p_min.py`, Pièce 2, § 2.3 et § 6, réserve 6).
   - Corriger CL16-01 (borne mémoire où la sonde s'auto-tue à 512 Mo mais tient dès 640 Mo ; défaut à 1 024 Mo, Pièce 2, § 1.1 et § 2.3).
   - Écrire et sceller l'`ExecuteurDistantParLots` (Pièce 2, § 0 et § 2.7). **Point clé pour la non-circularité (Q1, Q2, Q3)** : cet exécuteur garantit par construction que **le vérificateur (`lecture mécanique` de `RESULTAT: <nombre>`, application du seuil gelé de `prereg-court.json`, et session `lecteur_test`, Pièce 1, « Ce que fait la v48 ») reste dans la session cloud** et ne va jamais sur la machine jetable. La machine jetable ne fait qu'exécuter les scripts des lots dans `bwrap`, calculer les empreintes et les journaux hors du bac (sous `root`), et renvoyer l'archive scellée `resultats-<série>-v1.tar.zst` (Pièce 2, § 2.5 et § 2.7).
   - Ajouter dans le lanceur de la machine jetable (`lancer-serie-v1.sh`, Pièce 2, § 2.3 et § 2.4) les canaris passifs hors chemins légitimes et la vérification d'intégrité de l'arbre en lecture seule après chaque exécution de bac (Q3, Q5), avec un témoin cas sain (artefact honnête) et un témoin d'artefact qui touche un canari ou tente de modifier une empreinte.
   - Écrire les scripts de plomberie (`amorce-pole-v1.sh`, `sonde-sortie-v1.py`, `verifier-entree-v1.sh`, `destruction-serie-v1.sh`, Pièce 2, § 2.2.2 à § 2.6) et jouer hors machine les essais G1 à G7, G12, G13 et les artefacts (d) à (g) de G8 contre le faux serveur sur `127.0.0.1` (Pièce 2, § 4 et § 5).
   - Lire gratuitement par l'API Hetzner la disponibilité de `cpx32` (`nbg1`, `hel1`, `fsn1`), des images (`ubuntu-24.04`, `debian-13`) et figer l'empreinte de la clé Launchpad de `deadsnakes` (Pièce 2, § 1.2, § 1.3, § 2.2 et § 5).

2. **Étape 2 — Série S0 (Plomberie et étanchéité réseau/hôte, sans code de l'étage, Pièce 2, § 1.3)** :
   - Exécuter l'amorce sur la CPX32, vérifier l'épreuve `bwrap` sous l'identité `64097` (étape 5 de l'amorce, Pièce 2, § 2.2.2), relever `etat-v1.txt`, appliquer le pare-feu du nuage `sortie-<série>` et `nftables`, éprouver G8 couche par couche (artefacts (a), (b), (c) de G8, Pièce 2, § 4) et G9 avant et après redémarrage, tester l'aller-retour d'une archive témoin, détruire par identifiant et vérifier le code 404 (G7, Pièce 2, § 2.6 et § 4).

3. **Étape 3 — Série S1 (CL17-étage, pré-test d'étanchéité et témoins des canaris, sans modèle, Pièce 2, § 1.3 et § 2.4)** :
   - Passe A (cgroup v2) puis Passe B (cgroup v1 après redémarrage et rejeu de G8 et G9, Pièce 2, § 2.4).
   - Exécuter la suite complète (547 essais en ≈ 340 s, Pièce 2, § 1.1), les sondes de CL16, la suite publique d'étanchéité de `bwrap` (Q6), et les deux témoins préenregistrés (cas sain = artefact honnête qui passe avec 0 alerte canari ; artefact = script témoin qui touche un canari ou tente d'altérer un fichier et doit être éliminé).
   - Vérifier qu'aucun essai ne porte la mention « ESSAI RÉEL NON JOUÉ » (garde G10, Pièce 2, § 2.4 et § 4), rapatrier, vérifier les empreintes, détruire la machine.

4. **Étape 4 — Série P (Production, génération 1 de la course 2, Pièce 2, § 1.3 et § 2.7)** :
   - Exécuter les lots par tour via le poste de passage (au plus 12 allers-retours par série, Pièce 2, § 2.7), avec vérification hors du bac (dans la session cloud) des empreintes, des journaux de canaris et des lignes `RESULTAT: <nombre>`.

#### 2. Ce qui peut attendre (après la génération 1 de la course 2)
- **La migration vers Firecracker ou gVisor (Q1)** : tant que la machine jetable CPX32 ne contient aucun secret (Pièce 2, § 2.1), que sa sortie réseau est fermée à deux étages (G8, Pièce 2, § 2.2.3) et que le vérificateur tourne dans la session cloud (hors de la machine jetable, grâce à `ExecuteurDistantParLots`, Pièce 2, § 2.7), la non-circularité ne dépend déjà plus de l'infaillibilité de `bwrap`.
- **La redondance diverse systématique sur un second bac (Q4)** : peut attendre ou être restreinte à une re-vérification sélective des seules fiches ayant obtenu le verdict `survit` (Option 4c).
- **L'attestation matérielle SEV-SNP (Q3)** et **la reproduction par un tiers externe (h)** : la reproductibilité déterministe des archives (`tar --sort=name --mtime=@0` + `sha256sum`, Pièce 2, § 2.3 et § 2.5) permet à tout tiers de rejouer et vérifier les empreintes a posteriori sans bloquer le lancement de la course 2.

#### 3. Devis indicatif « illustratif » (appuyé sur les chiffres des pièces servies)

Tous les prix d'infrastructure reposent sur le gabarit Hetzner **CPX32** à **0,0577 EUR/h HT**, soit **0,0796 USD/h TTC** (avec les hypothèses SUPPOSÉES de la Pièce 2, § 3 : toute heure commencée facturée, TVA 20 %, 1 EUR ≈ 1,15 USD). Les budgets de modèles reposent sur les plafonds par défaut de la Pièce 1 (« Ce que fait la v48 » et « Ce qui n'est pas vérifié en réel ») et de la Pièce 2 (§ 3.1) : `0,5 USD` pour l'expérimentateur et `0,1 USD` pour le lecteur par fiche (soit `0,6 USD` par fiche, SUPPOSÉS).

| Poste | Base de calcul (Pièce, section) | Coût attendu (TTC) | Coût au pire cas (TTC) | Statut avant Course 2 |
|---|---|---|---|---|
| **Étapes hors machine** (code `ExecuteurDistantParLots`, canaris, essais sur faux serveur `127.0.0.1`) | 0 h de machine louée (Pièce 2, § 4 et § 5) | 0,00 USD | 0,00 USD | **Bloquant (Étape 1)** |
| **Série S0 — Plomberie** | 1 h attendue (≈ 40 min) ; 2 h au pire ; jusqu'à 2 séries S0 au pire (Pièce 2, § 1.3, § 3.1, § 3.2) | 0,08 USD (1 h) | 0,32 USD (2 × 2 h) | **Bloquant (Étape 2)** |
| **Série S1 — CL17-étage + suites publiques + témoins canaris** | 1 h attendue (≈ 45 min) × 2 séries (S1 + S1 rejouée) ; 3 h au pire × 3 séries (Pièce 2, § 1.3, § 3.1, § 3.2) | 0,16 USD (2 × 1 h) | 0,72 USD (3 × 3 h) | **Bloquant (Étape 3)** |
| **Série P — Machine jetable (Bac n° 1, `bwrap`)** | 3 h attendues (5 fiches × 3 exéc. × 120 s = 30 min + allers-retours) ; 40 h au pire (12 fiches × 3 × 3 600 s = 36 h + mise en place), × 2 séries au pire (Pièce 2, § 1.3, § 3.1, § 3.2) | 0,24 USD (1 × 3 h) | 6,38 USD (2 × 40 h ; 1 série = 3,19 USD, Pièce 2, § 0.2 point 5 et § 3.1) | **Bloquant (Étape 4)** |
| **Marge du chien de garde** (`send_later`) | + 2 h par série sur 7 séries au pire = 14 h (Pièce 2, § 2.6 et § 3.2) | — | + 1,11 USD (14 h) | **Bloquant (Garde G12)** |
| **Sous-total Machine (1 bac, périmètre Pièce 2)** | 6 h attendues ; 93 h au pire (+ 14 h chien de garde) (Pièce 2, § 0 et § 3.2) | **≈ 0,48 USD** (≈ 0,5 USD) | **≈ 7,41 USD** (8,52 USD avec chien de garde ; plafond GO : **10 USD**) | **Périmètre de base** |
| **Optionnel — Redondance diverse (Bac n° 2, Q4)** | Si rejeu intégral de P sur une 2e image/pile (3 h attendues, 40 h au pire par série P, Pièce 2, § 3.1) ; moins si limité aux seuls survivants (Option 4c) | + 0,24 USD (intégral) ou ≤ 0,08 USD (sélectif, 1 h) | + 3,19 USD par série P doublée | **Peut attendre / Sélectif** |
| **Modèles de l'étage (dans la session cloud, hors devis machine)** | `0,5 + 0,1 = 0,6 USD`/fiche (Pièce 1, quotas et « Ce qui n'est pas vérifié » ; Pièce 2, § 3.1) : 5 fiches attendues, 12 fiches max | **3,00 USD** (5 fiches) | **7,20 USD** (12 fiches, sur ligne de GO à part, Pièce 2, § 3.1) | **Bloquant à l'Étape 4** |

#### Conditions de validité et Réfutation
- **Conditions de validité** : Les durées de la série P supposent que l'`ExecuteurDistantParLots` regroupe les exécutions par tour (au plus 12 allers-retours par série, avec 5 à 10 minutes de latence SUPPOSÉES au poste de passage, Pièce 2, § 2.7 et § 6) et que chaque machine est détruite par son identifiant numérique dès la fin de la série (`DELETE /v1/servers/<id>` suivi d'un contrôle du code `404`, garde G7, Pièce 2, § 2.6 et § 4).
- **Ce qui réfuterait** : Qu'une série P nécessite des allers-retours séquentiels fiche par fiche (12 tours × 12 fiches = 144 allers-retours), ou que la restriction AppArmor d'Ubuntu 24.04 et la délégation du contrôleur `memory` des cgroups bloquent à la fois la passe A et la passe B en S1 (Pièce 2, § 2.2.1 et § 2.4).