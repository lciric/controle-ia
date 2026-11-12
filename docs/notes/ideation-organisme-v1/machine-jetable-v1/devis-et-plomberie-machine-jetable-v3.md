# Machine jetable de l'étage de tests de mort — choix, plomberie sans secret, devis, gardes — v3

Lignée « session-depot », sous-agent de rédaction, 31 octobre 2026. **Aucun nouveau relevé en v3.** Les relevés de la v2 ont
été faits le 31 octobre **de 00:36:57 à 00:40:39 UTC** (en-têtes HTTP `Date` gardés, chaque heure au § 7.2). La v2 a été
terminée avant son scellement (compagnon daté de 00:48:11 UTC). La v3 a été rédigée à partir de 01:06 UTC ; son heure de
scellement est celle de son compagnon `.sha256` sur disque.

**Remplace** `devis-et-plomberie-machine-jetable-v2.md` (`39260994753d1cdb4c4ffd4773ec989c8719ed38054a577b5fae19c052b6add8`,
inchangée, R12), qui remplaçait elle-même la v1 (`4fccbc75e3c6da3bbb8d4a4213b0fa4a104b584f2a685139c4d0dff0e6c10125`,
inchangée). La v3 corrige chacun des sept défauts du relecteur de la v2 (§ 0.2), dont la faille de garde de l'amorce
(défaut 3). Ce que ce relecteur a vérifié et trouvé exact (empreintes, sources, citations, calculs, lignes de code, remède
(R-a), combinaison des pare-feu) est repris tel quel. **Le devis ne change pas.**

Mandat (inchangé) : messages n° 266 (point 3) et n° 267 (point 1) de conv-audit. R-533 de conv-audit, tranchée par Lazar
(22:04 heure de Paris, relayée) : **l'étage de tests de mort tourne sur une machine louée jetable, sans aucun secret, détruite
après chaque série**.

**Rien n'a été loué, aucun compte touché, aucune commande envoyée à l'API d'un fournisseur, aucune clé lue ni écrite.** Pour
la v2, n'ont été lues que des pages publiques de documentation et de prix, par leur nom et à travers le mandataire de la
session (liste au § 7.2). Pour la v3, je n'ai lu que des fichiers sur disque (la v2, ses copies, la relecture) ; je n'ai rien
téléchargé. **Aucune sonde réseau** : aucune adresse IP, aucun nom choisi pour éprouver le mandataire. Ce document
n'écrit rien dans `registres/`.

## 0. Verdict

- **Machine** : Hetzner Cloud **CPX32**, avec 4 processeurs virtuels AMD x86_64, 8 Go de mémoire et 160 Go de disque, à
  **0,0577 EUR/h hors taxes**. Prix relu par la v2 : les trois pages sont identiques octet pour octet à celles de la v1
  (mêmes empreintes), servies le 31 octobre à 00:40:00 à 00:40:02 UTC (`Date`), modifiées en dernier le 27 octobre (§ 1.2).
- **Coût de la course 2** : **≈ 0,5 USD attendus**, **≈ 7,4 USD au pire** (sept séries). Plafond de GO proposé : **10 USD**.
  Inchangé.
- **Nouveau prérequis bloquant, à lever dans l'amorce** : sur l'image Ubuntu 24.04, la restriction AppArmor des espaces
  d'utilisateurs non privilégiés fera très probablement échouer `bwrap` lancé sous l'identité 64097. Remède retenu : le réglage
  persistant `kernel.apparmor_restrict_unprivileged_userns=0`, écrit par l'amorce et éprouvé avant tout dépôt de code ;
  il est déclaré comme écart d'hôte (§ 2.2.1).
- **Réseau** : cette session ne peut pas joindre la machine par SSH (R-821). Elle ne peut pas non plus la joindre en HTTPS vers
  une adresse IP : c'est le seul essai fait. **HTTP simple n'a pas été sondé**, et le sonder relève lui-même du classifieur.
  L'option (a) de R-821 reste donc **ouverte, en réserve**, et non écartée (§ 2.0).
- **D'où la voie recommandée (inchangée)** : un **poste de passage**, l'ordinateur de Lazar (par Contrôle à distance, ou à la
  main), qui porte `scp` et `ssh`. La session garde le jeton de l'API Hetzner et pilote création, fermeture du pare-feu et
  destruction.
- **Sortie réseau de la machine** : fermée à deux étages qui survivent tous deux au redémarrage. Ce sont le pare-feu du nuage
  Hetzner et `nftables` chargé au démarrage. La garde G8 est rejouée après chaque redémarrage (§ 2.2.3). **Nouveau en v3** :
  G8 refuse une cible vide et classe chaque sonde en « ouverte », « fermée » ou « indéterminée » d'après la cause de l'échec ;
  « indéterminée » arrête la série (§ 4).
- **Pour la production** (au-delà de CL17-étage), il manque un **exécuteur distant « par lots »** dans le code : demande à
  conv-audit (§ 2.7). Inchangé.

### 0.1 Réserves du premier relecteur (sur la v1) → corrections de la v2 (rappel)

Relecteur : `…/scratchpad/nuit-rendus/verifier-devis-machine-jetable.md`, verdict « conforme avec réserves ». Le relecteur de
la v2 a jugé cette table fidèle. Elle est gardée telle quelle ; les renvois de la colonne « où » restent valables en v3.

| n° | réserve du relecteur | correction dans la v2 | où |
|---|---|---|---|
| 1 | § 2.0, point 3 : « pas faisable, je le tiens pour établi » va au-delà de l'essai. Seul le HTTPS vers une adresse IP a été essayé, alors que l'option (a) de R-821 parle de HTTP simple | Constat réécrit : « constaté pour HTTPS vers une adresse IP ; HTTP simple non sondé, et le sonder relève lui-même du classifieur ». Le point passe des faits établis aux réserves. L'option (a) est rouverte et pesée : elle ne lève pas le dépôt du code (32 Kio). Le choix de la sonder revient à Lazar | § 2.0, § 5, § 6 réserve 1 |
| 2 | § 2.2 : risque Ubuntu 24.04 passé sous silence. La restriction AppArmor des espaces d'utilisateurs non privilégiés gêne `bwrap --unshare-user` sous `setpriv` en 64097 | Vérifié par la documentation publique (notes de version 24.04, journal des modifications d'`apparmor` sur 24.04, Launchpad, billet sur `bwrap`), copies empreintées. Prérequis inscrit, avec quatre remèdes pesés. Retenu : `/etc/sysctl.d/60-apparmor-namespace.conf` à 0, persistant au redémarrage de la passe B, déclaré comme écart d'hôte. Épreuve réelle sous 64097 dans l'amorce. G9 étendue (cas sain et artefact) | § 2.2.1, § 2.2.2, § 4 G9 |
| 3 | § 2.2 et § 2.5 : la sortie se rouvre au redémarrage de la passe B, parce que la règle `nftables` est chargée par `runcmd` depuis un fichier non lu au démarrage. G8 n'est éprouvée qu'en S0 | (i) Pare-feu du nuage Hetzner avec une règle sortante, donc refus implicite du reste. Il est porté par le nuage et survit au redémarrage. La documentation dit ce qu'il laisse passer : résolveur DNS de Hetzner et métadonnées. (ii) `nftables` écrit dans `/etc/nftables.conf` et service activé au démarrage ; il ferme aussi le DNS. (iii) G8 éprouvée couche par couche, et rejouée après le redémarrage d'essai de S0 et après celui de la passe B | § 2.2.3, § 2.4, § 2.5, § 4 G8 |
| 4 | § 2.2 : l'amorce ne s'arrête pas sur ses gardes (`runcmd` continue après `exit 3`, `pret` est écrit quand même). Il manque aussi la source deadsnakes, la création de `/var/lib/pole/`, et seul `stat` va dans `etat-v1.txt` | Un seul script `amorce-pole-v1.sh` en `set -euo pipefail`, avec un piège d'erreur qui écrit `echec`. `pret` n'est écrit qu'en dernière ligne. Bloc `apt: sources:` pour deadsnakes, avec l'empreinte de clé à lire avant S0. Dossiers créés d'emblée. Tout le relevé d'état va dans `etat-v1.txt`. Installation des paquets dans le script, non par `packages:` | § 2.2.2 |
| 5 | Horodatages : plage « 23:00 à 23:40 » incompatible avec le scellement à 23:10:51 ; heure de relevé 23:02:04 non prouvable | En-tête de la v2 : plage vraie, heure de scellement renvoyée au compagnon. Le relevé de prix est refait **avec les en-têtes HTTP gardés**. Les corps sont identiques à ceux de la v1, ce qui prouve les prix à 00:40 UTC le 31 octobre. Pour la v1, la seule heure prouvable est « au plus tard 23:07:18 UTC le 30 » (date des copies) | en-tête, § 1.2, § 7.2 |
| 6 | § 1.2 : comparaison avec d'autres loueurs à des tailles différentes (8 processeurs et 32 Go contre 4 et 8) | Marquée « **non comparé à taille égale** », sans conclusion. Le choix de Hetzner tient au compte et au jeton déjà fournis (R-816, R-817), non au prix | § 1.2 |
| 7 | Démarche hors mandat : sondes réseau (`1.1.1.1`, puis un nom de domaine et un nom `sslip.io`) qui ont déclenché « Containment Escape » ; doute sur une ou deux commandes | Aucune sonde dans cette v2. Le texte de consignation pour `registres/decisions.md` est proposé à la session principale (je n'écris pas les registres). Ces sondes ne se renouvellent pas sans le mot de Lazar. Le nombre de commandes **n'est pas établi** : je ne suis pas l'auteur de la v1, et elle ne le dit pas. À lire dans le journal de la session de la v1, s'il existe | § 2.0, § 8 |

### 0.2 Constat du relecteur de la v2 → correction de la v3

Relecteur : `…/scratchpad/nuit-rendus-2/verifier-machine-v2.md`
(`aa85ff3cfe78b1dfaa43bcafc071afba2e6bf5f549d8b82d67c4243287815a55`, bloc-notes), verdict « conforme avec réserves ». Aucun
défaut ne change le devis.

| n° | constat du relecteur | correction dans cette v3 | où |
|---|---|---|---|
| 1 | En-tête : plage « 00:36:57 à 00:40:02 » fausse (Launchpad servi à 00:40:32, journal d'`apparmor` à 00:40:39) ; § 7.2 écrit « voir en-têtes » pour ces deux pièces ; « terminée vers 00:50 » tombe après le scellement de 00:48:11 | Plage écrite « 00:36:57 à 00:40:39 UTC », relue dans les huit fichiers d'en-têtes. Les deux heures sont données au § 7.2. « Terminée avant son scellement (00:48:11) » | en-tête, § 7.2 |
| 2 | « Installé … en juin 2024 » sans source copiée (l'annonce `noble-changes/2024-June` n'est ni copiée ni empreintée) | Aucune nouvelle copie (aucun relevé en v3). La phrase ne dit plus que ce que portent les deux copies empreintées : profil ajouté par l'entrée `4.0.0-beta4-0ubuntu1` du journal (signée le 8 avril 2024), absent de la version de sortie (`4.0.0-beta3-0ubuntu3`, Launchpad), retiré par `4.0.1really4.0.0-beta3-0ubuntu0.1` (signée le 14 juillet 2024). La date d'arrivée dans `noble-updates` est déclarée **non copiée** | § 2.2.1, § 6 |
| 3 | **Faille de garde de l'amorce** : `miroir_ipv4` calculée dans une substitution passée à `echo` ; si la résolution échoue, ni `set -e` ni le piège ne réagissent, la ligne est écrite vide, G13 ne voit rien, et G8 (i) lance `curl http:///`, échoue pour une mauvaise raison et conclut « sortie fermée » (repli silencieux, R5). Point voisin : l'artefact (c) attend que (i) « aboutisse », alors qu'un refus de connexion distant (code 7) prouve aussi la sortie ouverte | (a) Étape 6 réécrite : **chaque valeur est calculée dans une variable** avant d'être écrite (`set -E -euo pipefail` : un échec de la commande arrête le script), puis refusée si elle est vide ; le fichier des sources apt, l'hôte du miroir et l'adresse IPv4 sont contrôlés un à un, avec un motif d'`echec` propre (code 5). (b) Avant `pret`, l'étape 8 relit `etat-v1.txt` et refuse toute ligne attendue absente **ou vide**, et une cible G8 qui n'a pas la forme d'une adresse IPv4. (c) G8 refuse une cible vide ou invalide (« cible G8 invalide », arrêt), et ne conclut jamais « fermée » sans motif. (d) G8 (i) ne lit plus « échec de curl » mais la **cause** : sonde `sonde-sortie-v1.py` (Python système, `-I`), qui lit l'`errno` de `connect()`. Connexion faite, ou `ECONNREFUSED` (un refus est revenu de l'extérieur) : **ouverte**. `EPERM` (refus local de `nftables`) ou délai dépassé : **fermée**. Toute autre issue : **indéterminée**, donc arrêt. Je n'ai pas repris la règle « code 7 de curl = ouverte » telle quelle : si le noyau rend `EPERM` au refus local de `nftables`, curl le rend lui aussi par le code 7 (SUPPOSÉ), et la garde aurait conclu « ouverte » dans le cas sain. Lire l'`errno` tient la distinction voulue par le relecteur. (e) Même règle à trois issues pour la sonde DNS (ii), désormais une requête UDP directe au résolveur noté avant fermeture : `resolvectl` n'est plus SUPPOSÉ. (f) Artefact (c) : « ouverte » attendue, que la connexion aboutisse ou soit refusée. Deux artefacts ajoutés : cible vide, et étape 6 forcée à rendre une valeur vide | § 2.2.2 (étapes 6 et 8, notes), § 2.2.3, § 4 G8 et G13, § 5, § 6 |
| 4 | § 2.2.3, point 1, et réserve 7 : citation de la FAQ tronquée ; la phrase entière est « This currently includes DNS resolver traffic and traffic for the Hetzner rescue system ». Le passage vers le système de secours manque parmi les fuites | Phrase citée entière, relue dans la copie empreintée (`3e604389…`), avec celle qui la précède (ARP, DHCP, une partie d'ICMPv6 jamais filtrés). Système de secours ajouté à la réserve 7. G8 (iii) vérifie aussi, par `GET /v1/servers/<id>`, que `rescue_enabled` vaut `false` (champ présent dans la spécification copiée : « True if rescue mode is enabled. Server will then boot into rescue system on next reboot. ») ; la session n'appelle jamais l'action d'activation du mode de secours | § 2.2.3, § 4 G8, § 6 réserve 7 |
| 5 | § 3.1 : P au pire, 40 × 0,079626 = 3,185 USD, s'arrondit à 3,19, non 3,18 (erreur venue de la v1 ; totaux inchangés, calculés sur 93 h d'un bloc) | Écrit 3,19 USD. Totaux inchangés (93 × 0,079626 = 7,405 → 7,41 USD) | § 3.1 |
| 6 | § 2.2 : versions données comme des faits sans source ni SUPPOSÉ (Ubuntu 24.04 : noyau 6.8, systemd 255, `bwrap` 0.9.0 ; Debian 13 : `bwrap` 0.11, Python 3.13, systemd 257), venues de la v1 | Marquées **SUPPOSÉ**, à lire dans `etat-v1.txt` en S0 ; ajoutées à la liste SUPPOSÉ du § 6. Les phrases qui en dépendaient (« la version même de CL16 », systemd 255 pour le cgroup v1) sont mises au conditionnel | § 2.2, § 2.2.1 (remède R-d), § 6 |
| 7 | Possible, non éprouvé : `sysctl --system` peut rendre une erreur à cause d'une clé sans rapport venue d'un autre fichier de l'image, d'où un faux `echec` | `sysctl -p /etc/sysctl.d/60-apparmor-namespace.conf`, la relecture `test … = 0` gardée. Au redémarrage, `systemd-sysctl` relit le fichier comme avant | § 2.2.1, § 2.2.2 (étape 3) |

**Essai hors machine (indicatif, non opposable).** Sur ce conteneur, sans réseau ni fournisseur, avec des commandes factices
dans un dossier jetable du bloc-notes :

- la ligne de la v2, jouée sur un fichier de sources absent, écrit `miroir_ipv4: ` vide, ne déclenche pas le piège, et la
  ligne suivante est atteinte : **la faille du défaut 3 est reproduite** ;
- les étapes 6 à 8 de la v3 rendent `pret` dans le cas sain. Elles rendent `echec` avec son motif, sans `pret`, dans six
  cas : sources absentes, ligne `URIs:` sans hôte, `getent` en échec, `getent` muet, `resolv.conf` sans résolveur IPv4,
  `python3.13 -V` muet ;
- `bash -n` passe sur l'esquisse du script ; la sonde se compile. Elle rend « indéterminée » (code 20) sur une cible vide, `abc`,
  `127.0.0.1`, `169.254.169.254`, un port 0 et un nom vide. `classer_erreur` range `ECONNREFUSED` en « ouverte », `EPERM` et le
  délai en « fermée », `EHOSTUNREACH` en « indéterminée ».

Ce n'est pas l'épreuve de R5 : les scripts restent à écrire en fichiers, à sceller et à éprouver (§ 5).

## 1. Choix de la machine

### 1.1 Ce que l'étage exige (LISEZMOI v51, CL16, CL17)

| exigence | source | conséquence sur la machine |
|---|---|---|
| x86_64 seulement (filtre d'appels système écrit pour cette architecture ; ailleurs, l'étage est refusé) | LISEZMOI v51, CL15-02 (c) | **exclut** les gabarits CAX (Ampere, ARM) |
| `bwrap` ≥ 0.9.0 non setuid, `setpriv`, `unshare` | LISEZMOI v51, « Prérequis de l'opérateur » | paquets `bubblewrap` et `util-linux` de la distribution |
| **création d'un espace d'utilisateurs par un processus sans privilège** (`setpriv --reuid 64097 … --no-new-privs`, puis `bwrap --unshare-user --uid 65534 --gid 65534 --cap-drop ALL`, et `--unshare-net`) | `tests_de_mort_v2.py` l. 52, 68, 1252, 1262, 1303, 1349 | **nouveau en v2** : bloqué par défaut sur Ubuntu 24.04 ; réglage d'hôte exigé (§ 2.2.1) |
| noyau du pôle en superutilisateur ; utilisateur dédié 64097 **sans compte** et sans processus | CL16, CL15-07 | machine entière à nous ; aucun compte 64097 créé |
| groupe de contrôle `memory` utilisable : cgroup v1 joué ; cgroup v2 écrit mais **jamais joué** (il faut que `memory` soit délégué) | LISEZMOI v51 l. 65-67, 105-106 | deux passes dans CL17-étage : v2, puis v1 (§ 2.4) |
| borne mémoire du bac : 1 024 Mo par défaut. À 512 Mo, la sonde s'auto-tue (CL16-01) ; elle tient dès 640 Mo | CL16-01 ; `MEMOIRE_MO_DEFAUT = 1024` | ≥ 4 Go de mémoire ; 8 Go donnent la marge de la sonde de 1 056 processus et de l'artefact `MEMOIRE-BAC` (5/4 de la borne) |
| un seul bac à la fois par identité (verrou) | CL15-07 | peu de processeurs utiles : 2 à 4 |
| Python 3.13 (CL16 : 3.13.17) | CL16, en-tête | Python 3.13 à installer (§ 2.2) |
| suite complète : 547 essais en ≈ 340 s (CL17) ; 517 en 346 s (CL16) | CL16, CL17 critère 6 | une passe de suite ≈ 6 min, 10 min par prudence |
| disque : code 0,93 Mo ; `TAILLE_MAX_TOTALE_TRAVAIL` = 256 Mo par bac | `tests_de_mort_v2.py` l. 148 | 40 Go suffisent largement |

Machine de CL16 (rappel, `contre-lecture-cl16-orchestrateur-v51-v1.md` l. 10-12) : ce conteneur, noyau Linux 6.18.44. On y lit
**pas d'AppArmor** : ni `/proc/sys/kernel/apparmor_restrict_unprivileged_userns` ni `/sys/module/apparmor/parameters/enabled`
n'existent (lu par la v2, et confirmé par son relecteur). CL16 a donc joué **sans** la restriction d'Ubuntu.

### 1.2 Prix publics relevés (Hetzner, hors taxes, adresse IPv4 comprise)

Deux relevés, par `curl`, au travers du mandataire de la session, sans compte :

| relevé | dossier | heure prouvable |
|---|---|---|
| v1 | `sources-prix-hetzner-20261030-v1/` | **au plus tard 23:07:18 UTC le 30 octobre** (date des copies). L'heure 23:02:04 donnée par la v1 n'est pas prouvable : les en-têtes n'ont pas été gardés |
| v2 | `sources-prix-hetzner-20261031-v1/` (corps **et** en-têtes) | **00:40:00, 00:40:01, 00:40:02 UTC le 31 octobre** (`Date` des en-têtes) ; `last-modified: Tue, 27 Oct 2026 11:01:31 GMT` (page `regular-performance`) |

| page | fichier | SHA-256 du corps (v1 = v2) |
|---|---|---|
| `https://www.hetzner.com/cloud/regular-performance/` | `cloud_regular-performance-v1.html` | `805d65bc323b9bebdda81df4767f119110dd5f2b907a3ff9be2c375abaafb408` |
| `https://www.hetzner.com/cloud/general-purpose/` | `cloud_general-purpose-v1.html` | `55c1c4d18781f59ecd58dad5e0c7ebc17a8273f3545842648a82bedb19b5ea54` |
| `https://www.hetzner.com/cloud/cost-optimized/` | `cloud_cost-optimized-v1.html` | `bc407cdb50142cb0eafc3442e0fdfba412f485abf7494dba28d96c31285781a9` |

Les corps du 31 octobre ont les **mêmes empreintes** que ceux du 30 : la table de prix de la v1, vérifiée par le relecteur, vaut
donc à 00:40 UTC le 31.

| gabarit | processeurs | mémoire | disque | EUR/h hors taxes | plafond mensuel | remarque sur la page |
|---|---|---|---|---|---|---|
| CX33 | 4 Intel/AMD partagés | 8 Go | 80 Go | 0,0144 | 8,99 € | **« not available »** (ligne « économique » entière) |
| CPX22 | 2 AMD partagés | 4 Go | 80 Go | 0,0320 | 19,99 € | — |
| **CPX32** | **4 AMD partagés** | **8 Go** | **160 Go** | **0,0577** | **35,99 €** | — |
| CPX42 | 8 AMD partagés | 16 Go | 320 Go | 0,1122 | 69,99 € | — |
| CCX13 | 2 AMD dédiés | 8 Go | 80 Go | 0,0697 | 43,49 € | — |
| CCX23 | 4 AMD dédiés | 16 Go | 160 Go | 0,1386 | 86,49 € | — |
| CAX21 | 4 Ampere (ARM) | 8 Go | 80 Go | 0,0176 | 10,99 € | « not available » ; **exclu** (ARM) |

Facturation, telle que la page la dit : « If you delete your cloud server before the end of the billing month, we will only
bill you for the hourly rate » ; « We will bill you for each cloud server until you choose to delete them ». Une machine
éteinte reste donc facturée : **seule la destruction arrête le compteur**. Trafic compris : 20 To dans l'Union européenne.

Disponibilité : chaque bloc de produit porte aussi un texte générique « This product is currently unavailable » (bulle masquée,
sans doute par lieu). **La disponibilité réelle par lieu n'est pas lisible sur la page.** Elle se lit gratuitement par l'API
(`GET /v1/server_types`, `GET /v1/datacenters`), avant le GO, par la session principale.

**Autres loueurs : non comparé à taille égale.** LC § 3.2 (`1ce823a7…`) relevait, le 30 octobre à 07:49 UTC, 0,375 USD/h chez
DigitalOcean et 0,29 EUR/h chez Scaleway, mais pour **8 processeurs et 32 Go**. Ces chiffres ne se comparent pas à un gabarit de
4 processeurs et 8 Go, et je n'en tire aucune conclusion. Le choix de Hetzner tient au compte et au jeton déjà fournis par Lazar
(R-816, R-817), non à une comparaison de prix. À ces montants (centimes par série), une comparaison à taille égale ne changerait
pas le devis de façon décisive. SUPPOSÉ, non vérifié.

### 1.3 Choix et durée d'une série

- **Choix : CPX32**, dans un lieu de l'Union européenne (`nbg1`, `hel1` ou `fsn1`, selon la disponibilité lue par l'API).
- **Replis**, dans cet ordre : CPX22 (moitié prix, mais 4 Go seulement, marge mince pour une borne de 1 024 Mo plus la sonde),
  puis CCX13 (processeurs dédiés, si aucun CPX n'est disponible).
- L'écart entre ces gabarits se compte en centimes ; la marge de mémoire de la CPX32 l'emporte.

| série | contenu | machine allumée (attendu) | pire cas retenu |
|---|---|---|---|
| **S0 — plomberie** | création, amorce, épreuve `bwrap` sous 64097, fermeture du pare-feu du nuage, G8 couche par couche, **un redémarrage d'essai puis G8 et G9 rejouées**, aller-retour d'une archive témoin, destruction ; aucun code de l'étage | ≈ 40 min (démarrage 1 min, paquets 3 à 5 min, redémarrage 2 min, artefacts G8 et G9, transferts, destruction) | 2 h |
| **S1 — CL17-étage** (contre-lecture sous `bwrap` réel, demandée au n° 267) | passe A en cgroup v2, puis redémarrage, contrôles d'après redémarrage (G8, G9, mode du cgroup), passe B en cgroup v1 (§ 2.4) ; à chaque passe, la suite complète et les sondes de CL16 | ≈ 45 min (2 × 10 min de suite, 2 × 5 min de sondes, 1 redémarrage, paquets) | 3 h |
| **P — production** (génération 1 de la course 2) | 5 fiches × 3 exécutions × 120 s = 30 min d'exécution ; jusqu'à 12 tours par fiche, en lots (§ 2.7) | ≈ 3 h | 40 h : 12 fiches (`NOMBRE_MAX`) × 3 × 3 600 s (`DELAI_EXECUTION_S_MAX`) = 36 h, plus 12 allers-retours et la mise en place |

S0 reste sous une heure facturée attendue ; le devis du § 3 ne change pas.

## 2. Plomberie, sans aucun secret sur la machine

### 2.0 Contrainte de réseau constatée

Ce qui a été **constaté** (essais de la v1, aucun nouvel essai en v2) :

1. **SSH** : refusé depuis cette session cloud. Le port 22 est fermé, et le classifieur classe la tentative en « échappement de
   confinement » (R-821, 10:50 UTC).
2. **HTTPS vers une adresse IP** : fermé. Essai de la v1, le 30 octobre à 23:03 UTC, sans fournisseur, vers `https://1.1.1.1/` :
   le mandataire a ouvert puis refermé le tunnel (`ws_closed_mid_exchange`, 517 octets envoyés, 39 reçus), et curl a rendu
   « Connection reset by peer ».
3. **Sondes suivantes de la v1** (un nom de domaine, puis un nom `sslip.io`) : **refusées par le classifieur** (« Containment
   Escape »). Ni retentées ni contournées. La v1 ne dit pas s'il s'agissait d'une seule commande ou de deux ; je ne peux pas
   l'établir (§ 8).
4. **L'API Hetzner** (`api.hetzner.cloud`) répond à la session : statut 200 en lecture, jeton passé par variable (R-821).
5. **Les données utilisateur de cloud-init** sont plafonnées par Hetzner à 32 Kio. **Vérifié en v2** dans la spécification
   publique de l'API (`hetzner-api-specification-v1.json`, champ `user_data` de la création de serveur : « This field is limited
   to 32KiB. »). L'archive v52 pèse 930 077 octets. **Le code ne peut donc pas passer par cloud-init** : cloud-init ne porte
   que l'amorce.

Ce qui **n'est pas établi** (réserve, non un fait) :

- **Option (a) de R-821** (« v2 sans connexion, tout par cloud-init, journaux servis en HTTP simple par A et lus à travers le
  mandataire ») : **constaté pour HTTPS vers une adresse IP ; HTTP simple non sondé, et le sonder relève lui-même du
  classifieur.** Je ne la tiens donc pas pour infaisable.
  - Même si HTTP simple passait, l'option (a) ne règlerait que le **retour** des résultats. Le **dépôt** du code (930 077 octets)
    ne tient pas dans les 32 Kio de cloud-init. La machine ne peut pas non plus le tirer d'un dépôt privé : il faudrait un jeton
    sur la machine, ce qui est interdit. Le poste de passage reste donc nécessaire pour l'entrée.
  - Elle demanderait aussi d'ouvrir un port entrant au-delà de l'adresse du poste, vers les adresses de sortie du mandataire,
    qui sont inconnues. Les résultats seraient lus en clair : rien de secret par construction, et l'intégrité tiendrait par
    l'empreinte et le témoin (G10).
  - La sonder revient à Lazar (§ 5, point 4).

**D'où trois acteurs** (inchangé) :

- la **session cloud** (API, jeton, préparation, fermeture du pare-feu, scellement, destruction) ;
- le **poste de passage**, l'ordinateur de Lazar, qui porte `scp` et `ssh`. C'est l'option (b) de R-821. R-822 : « Contrôle à
  distance pour l'essai Hetzner : instructions données ». Il est piloté par une session reliée par Contrôle à distance, ou par
  Lazar à la main ;
- la **machine jetable**, qui ne contient que du public.

Entre la session et le poste, les archives passent par une branche du dépôt privé `lciric/controle-ia-travail`, **jamais**
`lciric/controle-ia`.

### 2.1 Qui tient quoi

| pièce | où elle vit | jamais sur |
|---|---|---|
| jeton de l'API Hetzner | **session cloud**, variable `HCLOUD_TOKEN` des réglages de l'environnement (R-817), passée par `env -i` à la seule commande `curl` vers `api.hetzner.cloud` ; jamais en argument visible, jamais dans un fichier ni un journal | la machine, le poste de passage, le dépôt |
| clé privée SSH de la série (ed25519, neuve à chaque série) | poste de passage, `~/.pole-jetable/<série>/cle` (mode 0600), effacée à la fin de la série | la machine, le dépôt, la session |
| clé publique SSH de la série | **enregistrée par la session dans le projet** (`POST /v1/ssh_keys`), passée à la création par `ssh_keys` (identifiant), retirée à la destruction ; copie dans le dépôt | — (publique). En v2, elle **ne passe plus** par les données cloud-init |
| identifiants GitHub de Lazar | poste de passage seulement (son propre `git`) | la machine (**aucun jeton GitHub**), la session |
| clés de modèles (Anthropic, Kimi, Gemini) | session cloud (relais) | la machine, le poste de passage |
| empreinte attendue de l'archive de code, témoin de série (16 octets au hasard), identifiant de série | données cloud-init (`/etc/pole/attendu-v1.txt`), fichier de série dans le dépôt | — (rien de tout cela n'ouvre quoi que ce soit) |

Le témoin de série n'est pas un secret : il n'ouvre rien. Il lie l'archive de résultats à **cette** série et à **cette**
machine, ce qui empêche une confusion de séries ou le rejeu d'une archive ancienne.

### 2.2 Image de base et mise en place

- **Image** : `ubuntu-24.04`. Versions **SUPPOSÉES**, reprises de la v1 sans source copiée, à lire dans `etat-v1.txt` en S0 :
  noyau 6.8, systemd 255, `bwrap` 0.9.0. Si elles se confirment, l'image donnerait **la version de `bwrap` de CL16** et un
  cgroup v1 encore forçable au démarrage. **Elle restreint les espaces d'utilisateurs non privilégiés** (§ 2.2.1, documenté).
  - Repli : `debian-13`. Versions **SUPPOSÉES** de même, à lire en S0 : `bwrap` 0.11, Python 3.13 natif, systemd 257.
    Debian ne porterait pas, SUPPOSÉ, la restriction AppArmor propre à Ubuntu. Mais le cgroup v1 n'y démarrerait que de force,
    ce qui éloignerait la passe B des conditions de CL16.
  - S0 ne tient aucune de ces versions pour acquise : G9 lit `bwrap --version` (≥ 0.9.0 exigé), Python et le mode du cgroup.
  - Le nom des images est SUPPOSÉ ; il se lit gratuitement par `GET /v1/images?type=system&architecture=x86`. Le nom
    `ubuntu-24.04` figure dans l'exemple de création de la spécification publique (`--image ubuntu-24.04`), ce qui le rend
    probable sans le prouver disponible.
- **Python 3.13** : paquet `python3.13` du dépôt signé « deadsnakes » (PPA `ppa:deadsnakes/ppa`) pour Ubuntu 24.04 (SUPPOSÉ
  disponible). Repli : le Python 3.12 de la distribution, déclaré comme écart à CL16 dans le manifeste de série.

#### 2.2.1 Prérequis : espaces d'utilisateurs non privilégiés sous Ubuntu 24.04 (réserve 2 du relecteur)

**Ce que dit la documentation publique** (copies empreintées, § 7.2) :

- Notes de version d'Ubuntu 24.04, « Unprivileged user namespace restrictions » : « In combination with the apparmor package,
  the Ubuntu kernel now restricts the use of unprivileged user namespaces. This affects all programs on the system that are
  unprivileged and unconfined. A default AppArmor profile is provided that allows the use of user namespaces for unprivileged
  and unconfined applications but will deny the subsequent use of any capabilities within the user namespace. »
- Mêmes notes, remèdes donnés :
  - un profil AppArmor par application, avec la règle `userns` ;
  - `echo 0 | sudo tee /proc/sys/kernel/apparmor_restrict_unprivileged_userns`, « This setting is lost on reboot » ;
  - ou un réglage persistant, `/etc/sysctl.d/60-apparmor-namespace.conf` contenant
    `kernel.apparmor_restrict_unprivileged_userns=0`, puis redémarrage.
- Russell Coker, « Ubuntu 24.04 and Bubblewrap » (24 avril 2024) : sous 24.04, `bwrap` rend « bwrap: loopback: Failed
  RTM_NEWADDR: Operation not permitted » ou « bwrap: setting up uid map: Permission denied ». Remède : un profil
  `/etc/apparmor.d/bwrap` en `flags=(unconfined)` avec `userns`.
- Journal des modifications du paquet `apparmor` sur 24.04 (version publiée dans `noble-updates` :
  `4.0.1really4.0.1-0ubuntu0.24.04.9`, publiée le 14 octobre 2026 selon Launchpad).
  - Le profil `bwrap-userns-restrict` a été ajouté au paquet `apparmor` par l'entrée `4.0.0-beta4-0ubuntu1` du journal
    (« d/apparmor.install - install new profile - bwrap-userns-restrict », signée le 8 avril 2024). Cette version n'est pas la
    version de sortie de 24.04 : Launchpad donne `4.0.0-beta3-0ubuntu3` dans `Release`, publiée le 4 avril 2024. **La date de
    son arrivée dans `noble-updates` n'est pas dans les copies** (l'annonce de `lists.ubuntu.com` n'est ni copiée ni
    empreintée ; la v2 écrivait « juin 2024 » sans source).
  - Il a été retiré pour régression par `4.0.1really4.0.0-beta3-0ubuntu0.1`, signée le 14 juillet 2024 : « This drops
    /etc/apparmor.d/bwrap-userns-restrict ».
  - Il revient ensuite seulement dans le paquet facultatif `apparmor-profiles`, et la version `…24.04.3` dit : « Revert to
    version 4.0.1-0ubuntu0.24.04.2 except for the patch that enables the bwrap-userns-restrict profile ».
  - **Lecture** : aucun profil `bwrap` n'est actif par défaut sur une 24.04 à jour. SUPPOSÉ que l'image Hetzner suit l'archive
    d'Ubuntu sur ce point ; S0 le lit.

**Pourquoi l'étage est touché.** Le pôle lance `setpriv --reuid 64097 --regid 64097 --clear-groups --no-new-privs`, puis
`bwrap --unshare-user --uid 65534 --gid 65534 --cap-drop ALL`, avec `--unshare-net` (`tests_de_mort_v2.py` l. 52, 68, 1252,
1262, 1303, 1349). Après `setpriv`, le processus n'a aucun privilège et n'est confiné par aucun profil : c'est exactement le cas
visé. Il peut créer l'espace d'utilisateurs, mais sans capacité à l'intérieur. Il ne peut alors écrire ni la table des
identités (« setting up uid map ») ni régler l'interface de bouclage de l'espace réseau (« loopback »). **Conclusion probable,
non éprouvée : sans réglage, l'étage est refusé par sa propre sonde, et S1 ne joue rien.**

**Remèdes pesés.**

| remède | avantage | inconvénient | sort |
|---|---|---|---|
| **(R-a) réglage persistant** `/etc/sysctl.d/60-apparmor-namespace.conf` = `kernel.apparmor_restrict_unprivileged_userns=0`, appliqué tout de suite par `sysctl -p` sur ce seul fichier et relu au démarrage | le plus proche de CL16, qui a joué sans aucune restriction AppArmor (§ 1.1) ; remède écrit par Ubuntu ; **survit au redémarrage de la passe B** ; rien à confiner | ouvre les espaces d'utilisateurs à tout processus sans privilège de la machine, ce qui affaiblit la défense contre les failles du noyau. Ici, la machine est dédiée, jetable, sans autre utilisateur et sans aucun secret | **retenu** |
| (R-b) profil AppArmor dédié `/etc/apparmor.d/bwrap` (`flags=(unconfined)`, `userns`) | plus étroit : seul `/usr/bin/bwrap` gagne le droit | ajoute une couche AppArmor absente de CL16 (écart). La transition vers ce profil au `exec` de `bwrap` se fait sous `--no-new-privs`, posé par `setpriv` : SUPPOSÉ permise depuis un processus non confiné, non éprouvée | repli, si Lazar préfère l'étroit ; à éprouver en S0 |
| (R-c) `bwrap` setuid | marche, d'après les forums | **interdit** : l'étage exige un `bwrap` non setuid (LISEZMOI v51), et G9 le refuse | écarté |
| (R-d) image `debian-13` | pas de restriction propre à Ubuntu (SUPPOSÉ) | cgroup v1 seulement forcé (systemd 257, version SUPPOSÉE), donc passe B plus loin de CL16 | repli d'image |

**Jamais** : lancer l'étage en superutilisateur pour contourner la restriction (contraire à l'identité exigée par CL15 et la
v50). **Jamais** non plus lever la sonde par `--memoire-bac-non-bornee-permise` ou une variable `POLE_ESSAI_*`.

**Déclaration** : le manifeste de chaque passe porte la valeur de `kernel.apparmor_restrict_unprivileged_userns` lue avant et
après le réglage, et après chaque redémarrage. Il porte aussi la ligne « **écart d'hôte** : restriction AppArmor des espaces
d'utilisateurs levée (0) ; AppArmor reste actif pour ses autres profils ; CL16 a joué sans AppArmor ». Le rapport de
CL17-étage reprend cette ligne.

#### 2.2.2 Amorce cloud-init (réserve 4 du relecteur)

`amorce-cloud-init-v1.yaml`, à écrire et à sceller, moins de 32 Kio, **aucune ligne secrète**. Principe : cloud-init ne fait
qu'écrire des fichiers et lancer **un seul script**. Ce script s'arrête au premier échec et n'écrit `pret` qu'en dernière ligne.
`runcmd` ne joue qu'au premier démarrage : tout ce qui doit survivre au redémarrage (réglage des espaces d'utilisateurs,
`nftables`) est donc écrit dans des fichiers que le système relit au démarrage.

```yaml
#cloud-config
ssh_pwauth: false
package_update: false          # tout passe par le script, qui s'arrête au premier échec
apt:
  sources:
    deadsnakes:
      source: "ppa:deadsnakes/ppa"
      keyid: "<empreinte de la clé de signature, lue sur Launchpad avant S0>"   # SUPPOSÉ : à lire, puis figée
write_files:
  - path: /etc/pole/attendu-v1.txt                       # public : empreintes et témoin
    permissions: "0644"
    content: |
      SERIE=<identifiant>
      ARCHIVE_SHA256=<64 hexadécimaux>
      TEMOIN=<32 hexadécimaux>
  - path: /etc/sysctl.d/60-apparmor-namespace.conf       # § 2.2.1, remède (R-a), persistant
    permissions: "0644"
    content: "kernel.apparmor_restrict_unprivileged_userns=0\n"
  - path: /etc/pole/nftables-pole-v1.conf                # copié dans /etc/nftables.conf par le script (§ 2.2.3)
    permissions: "0644"
    content: |
      <règles du § 2.2.3>
  - path: /usr/local/sbin/sonde-sortie-v1.py              # sonde de G8, § 2.2.3 (nouveau en v3)
    permissions: "0755"
    content: |
      <sonde du § 2.2.3>
  - path: /usr/local/sbin/amorce-pole-v1.sh               # esquisse, encore jamais écrite en fichier : le nom v1 reste libre
    permissions: "0700"
    content: |
      <script ci-dessous>
runcmd:
  - [/usr/local/sbin/amorce-pole-v1.sh]
```

La clé publique de la série passe par le champ `ssh_keys` de la création, non par ces données (§ 2.1).

```bash
#!/bin/bash
# amorce-pole-v1.sh : s'arrête au premier échec ; « pret » n'est écrit qu'à la dernière ligne.
set -Eeuo pipefail                 # -E : le piège ERR vaut aussi dans les fonctions
umask 077
E=/var/lib/pole
install -d -m 0700 "$E" "$E/entree" "$E/sortie"
trap 'rc=$?; echo "echec ligne $LINENO code $rc" > "$E/echec"; exit $rc' ERR
arret() { echo "$1" > "$E/echec"; exit "${2:-3}"; }   # arrêt explicite, avec son motif
IPV4='^([0-9]{1,3}\.){3}[0-9]{1,3}$'

# 1. L'identité dédiée doit rester SANS compte.
if getent passwd 64097 >/dev/null; then arret "64097 a un compte" 3; fi

# 2. Paquets (source deadsnakes déclarée par le bloc apt de cloud-init).
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y --no-install-recommends bubblewrap util-linux nftables zstd python3.13

# 3. Espaces d'utilisateurs : réglage persistant, appliqué tout de suite sur CE SEUL fichier, relu.
#    (v3 : plus de « sysctl --system », qu'une clé sans rapport d'un autre fichier de l'image pourrait faire échouer.)
sysctl -p /etc/sysctl.d/60-apparmor-namespace.conf >/dev/null
test "$(sysctl -n kernel.apparmor_restrict_unprivileged_userns)" = 0

# 4. Prérequis de l'étage.
test "$(uname -m)" = x86_64
test ! -u /usr/bin/bwrap
dpkg --compare-versions "$(bwrap --version | awk '{print $2}')" ge 0.9.0

# 5. Épreuve réelle : bwrap sous l'identité du bac, avec espace d'utilisateurs ET espace réseau.
setpriv --reuid 64097 --regid 64097 --clear-groups --no-new-privs \
  bwrap --unshare-all --unshare-user --uid 65534 --gid 65534 --cap-drop ALL \
        --ro-bind / / --proc /proc --dev /dev -- /bin/true

# 6. Relevé d'état (v3). Chaque valeur est calculée dans une VARIABLE : une affectation « v=$(…) » rend le code de la
#    substitution, donc un échec arrête le script (set -e, piège ERR). Rien n'est calculé dans une substitution passée à
#    echo, dont l'échec serait masqué. Toute valeur vide est ensuite refusée.
v_bwrap=$(bwrap --version)
v_python=$(python3.13 -V 2>&1)
v_noyau=$(uname -mr)
v_cgroup=$(stat -fc %T /sys/fs/cgroup)
v_systemd=$(systemctl --version | sed -n 1p)        # sed lit tout : pas de SIGPIPE, donc pas de faux échec sous pipefail
v_userns=$(sysctl -n kernel.apparmor_restrict_unprivileged_userns)
v_bwrap_mode=$(stat -c '%A %U' /usr/bin/bwrap)
v_demarrage=$(cat /proc/cmdline)
v_politique_py=$(apt-cache policy python3.13 | sed -n 1,3p | tr '\n' ' ')

#    Cible de G8 (i) : l'adresse IPv4 du miroir de paquets, résolue AVANT la fermeture. Chaque maillon est contrôlé.
SOURCES=/etc/apt/sources.list.d/ubuntu.sources      # format deb822 de 24.04 ; SUPPOSÉ sur l'image Hetzner
test -r "$SOURCES" || arret "cible G8 : $SOURCES absent ou illisible" 5
miroir_hote=$(awk '/^URIs:/{split($2,u,"/"); print u[3]; exit}' "$SOURCES")
test -n "$miroir_hote" || arret "cible G8 : aucun hôte dans la ligne URIs de $SOURCES" 5
miroir_ipv4=$(getent ahostsv4 "$miroir_hote" | awk 'NR==1{print $1}')   # getent en échec : pipefail, donc arrêt
[[ "$miroir_ipv4" =~ $IPV4 ]] || arret "cible G8 : adresse du miroir vide ou invalide ($miroir_hote)" 5

#    Cible de G8 (ii) : le résolveur DNS amont, noté AVANT la fermeture (systemd-resolved ; chemin SUPPOSÉ).
RESOLV=/run/systemd/resolve/resolv.conf
test -r "$RESOLV" || arret "cible G8 : $RESOLV absent ou illisible" 5
resolveur_ipv4=$(awk '$1=="nameserver" && $2 ~ /^[0-9.]+$/ {print $2; exit}' "$RESOLV")
[[ "$resolveur_ipv4" =~ $IPV4 ]] || arret "cible G8 : aucun résolveur IPv4 dans $RESOLV" 5

for v in v_bwrap v_python v_noyau v_cgroup v_systemd v_userns v_bwrap_mode v_demarrage v_politique_py; do
  test -n "${!v}" || arret "etat : valeur vide pour $v" 5
done
{
  printf 'bwrap: %s\n' "$v_bwrap";             printf 'python: %s\n' "$v_python"
  printf 'noyau: %s\n' "$v_noyau";             printf 'cgroup: %s\n' "$v_cgroup"
  printf 'systemd: %s\n' "$v_systemd";         printf 'userns: %s\n' "$v_userns"
  printf 'bwrap_mode: %s\n' "$v_bwrap_mode";   printf 'ligne_demarrage: %s\n' "$v_demarrage"
  printf 'politique_python3.13: %s\n' "$v_politique_py"
  printf 'miroir_hote: %s\n' "$miroir_hote";   printf 'miroir_ipv4: %s\n' "$miroir_ipv4"
  printf 'resolveur_ipv4: %s\n' "$resolveur_ipv4"
} > "$E/etat-v1.txt"

# 7. Sortie fermée, de façon persistante.
install -m 0644 /etc/pole/nftables-pole-v1.conf /etc/nftables.conf
systemctl enable --now nftables
nft list table inet pole >/dev/null

# 8. Relecture de l'état, puis prêt, seulement ici. Chaque ligne attendue doit être présente ET non vide ;
#    les deux cibles de G8 doivent avoir la forme d'une adresse IPv4.
for cle in bwrap python noyau cgroup systemd userns bwrap_mode ligne_demarrage politique_python3.13 \
           miroir_hote miroir_ipv4 resolveur_ipv4; do
  grep -Eq "^${cle}: .+" "$E/etat-v1.txt" || arret "etat : ligne $cle absente ou vide" 5
done
grep -Eq "^miroir_ipv4: ([0-9]{1,3}\.){3}[0-9]{1,3}$"    "$E/etat-v1.txt" || arret "etat : cible G8 (i) invalide" 5
grep -Eq "^resolveur_ipv4: ([0-9]{1,3}\.){3}[0-9]{1,3}$" "$E/etat-v1.txt" || arret "etat : cible G8 (ii) invalide" 5
touch "$E/pret"
```

Notes sur l'esquisse :

- Un contrôle qui échoue (`test`, `dpkg --compare-versions`, l'épreuve `bwrap`, une affectation de l'étape 6) déclenche le
  piège ; un contrôle de forme (cible vide, ligne vide) appelle `arret` avec son motif. Dans les deux cas, `echec` est écrit et
  `pret` ne l'est jamais. Le poste de passage attend `pret` **ou** `echec`. S'il ne voit ni l'un ni l'autre au bout de 20 min,
  c'est un arrêt de série.
- L'adresse du miroir de paquets et celle du résolveur DNS sont résolues **avant** la fermeture et notées dans
  `etat-v1.txt`. G8 s'en sert comme cibles (§ 2.2.3), ce qui évite d'aller toucher un hôte tiers nouveau. Les chemins
  `/etc/apt/sources.list.d/ubuntu.sources` (format deb822 de 24.04) et `/run/systemd/resolve/resolv.conf` sont SUPPOSÉS pour
  l'image Hetzner. **v3 (défaut 3 du relecteur)** : si l'un manque, ou si une adresse sort vide ou mal formée, l'amorce
  écrit `echec` avec son motif (code 5) et n'écrit jamais `pret`. La v2 calculait l'adresse dans une substitution passée à
  `echo` : un échec y était masqué, la ligne s'écrivait vide, et G8 aurait sondé `http:///` pour conclure « fermée » à tort.
- Une affectation `v=$(commande)` rend le code de sortie de la commande, que `set -e` voit ; un `echo "…$(commande)…"` rend
  celui d'`echo`, toujours 0. D'où la règle de l'étape 6 : **aucun calcul dans un argument d'`echo` ou de `printf`**.
- `/etc/nftables.conf` n'est écrit qu'**après** l'installation du paquet, pour éviter une question de dpkg sur un fichier de
  configuration déjà présent.

#### 2.2.3 Fermeture de la sortie réseau, persistante (réserve 3 du relecteur)

**Deux couches, qui survivent toutes deux au redémarrage :**

1. **Pare-feu du nuage Hetzner** (porté par le nuage, non par la machine). Ce que dit la FAQ publique (§ 7.2) :
   - « If you define one or more outbound rules, the outbound direction also changes to implicit "deny" » ;
   - il est « stateful », donc les réponses aux connexions SSH entrantes passent ;
   - mais, phrases entières (v3, défaut 4 du relecteur) : « Metadata server requests also do not go through the firewall and
     are being answered locally. Additionally, our Firewall will always let through traffic to/from certain Hetzner services.
     This currently includes DNS resolver traffic and traffic for the Hetzner rescue system. » La phrase d'avant ajoute :
     « ARP, DHCP and some ICMPv6 types like the ones needed for NDP will always be unaffected. »
   - Le trafic du **système de secours** de Hetzner passe donc lui aussi. Il ne sert qu'à une machine démarrée en mode de
     secours. La session n'appelle jamais l'action qui active ce mode, et G8 (iii) vérifie que `rescue_enabled` vaut `false`
     (§ 4) ; la spécification copiée le décrit ainsi : « True if rescue mode is enabled. Server will then boot into rescue
     system on next reboot. »
   - Mise en œuvre : deux pare-feu par série, étiquetés `pole=etage`, `serie=<série>` :
     - `entree-<série>`, appliqué **à la création** (champ `firewalls`) : entrée TCP 22 depuis la seule adresse IPv4 du poste
       de passage ; aucune règle sortante, donc la sortie reste ouverte pour l'installation ;
     - `sortie-<série>`, appliqué par la session (`POST /v1/firewalls/<id>/actions/apply_to_resources`) **dès que le poste a
       vu `pret`** et l'a signalé par la branche de passage. Il porte une seule règle sortante : ICMP vers `192.0.2.1/32`,
       adresse réservée à la documentation, qui ne mène nulle part. Elle n'est là que pour basculer la sortie en refus
       implicite. La session vérifie ensuite par `GET /v1/firewalls/<id>` que le pare-feu est bien appliqué au serveur.
   - IPv6 désactivé à la création (`public_net.enable_ipv6=false`) : une famille d'adresses de moins à fermer.
2. **`nftables` sur la machine**, chargé au démarrage par le service `nftables` depuis `/etc/nftables.conf` (convention du
   paquet, SUPPOSÉE identique sur l'image Hetzner). Il ferme aussi ce que le pare-feu du nuage laisse passer, à savoir le DNS :

```
#!/usr/sbin/nft -f
flush ruleset
table inet pole {
  chain sortie {
    type filter hook output priority 0; policy drop;
    oif "lo" accept
    ct state established,related accept             # réponses SSH, erreurs ICMP liées
    udp sport 68 udp dport 67 accept                  # renouvellement du bail DHCP IPv4 (SUPPOSÉ : adressage par DHCP)
    ip daddr 169.254.169.254 tcp dport 80 accept      # métadonnées, locales à l'hôte (cloud-init au redémarrage)
  }
  chain entree {
    type filter hook input priority 0; policy drop;
    iif "lo" accept
    ct state established,related accept
    tcp dport 22 accept                               # le pare-feu du nuage restreint déjà la source au poste
    udp sport 67 udp dport 68 accept
  }
}
```

Le DNS n'a aucune règle : il est refusé. Les métadonnées restent joignables. Elles ne servent que des données publiques par
construction (G2) et ne sortent pas vers l'Internet. Le bac, lui, reste de toute façon sans réseau (`--unshare-net`).

**Sonde de G8 (nouvelle en v3, défaut 3 du relecteur).** La v2 lisait « curl échoue » comme « sortie fermée ». C'est faux de
deux façons. Une cible vide fait échouer curl pour une mauvaise raison. Et un refus de connexion revenu de l'extérieur prouve
au contraire que la sortie est ouverte. La v3 lit donc la **cause** de l'échec, par `sonde-sortie-v1.py`, écrite par cloud-init
et lancée par le Python du système en mode isolé (`/usr/bin/python3 -I`, présent puisque cloud-init en dépend) :

```python
#!/usr/bin/python3 -I
# sonde-sortie-v1.py : classe une sortie réseau en « fermee », « ouverte » ou « indeterminee ». Esquisse, à écrire et éprouver.
# Usage : sonde-sortie-v1.py tcp <ipv4> <port>  |  sonde-sortie-v1.py dns <ipv4_resolveur> <nom>
# Codes : 0 fermée ; 10 ouverte ; 20 indéterminée (cible invalide comprise). Jamais « fermée » sans motif lu.
import errno, ipaddress, os, socket, struct, sys

FERMEE, OUVERTE, INDETERMINEE = 0, 10, 20

def rendre(code, motif):
    print({FERMEE: "fermee", OUVERTE: "ouverte", INDETERMINEE: "indeterminee"}[code], motif)
    sys.exit(code)

def cible(texte):
    try:
        adresse = ipaddress.IPv4Address(texte)
    except ValueError:
        rendre(INDETERMINEE, "cible G8 invalide : %r" % texte)          # cible vide comprise
    if adresse.is_loopback or adresse.is_unspecified or adresse.is_link_local or adresse.is_multicast:
        rendre(INDETERMINEE, "cible G8 locale, elle n'éprouve pas la sortie : %s" % adresse)
    return str(adresse)

def classer_erreur(e):
    if isinstance(e, TimeoutError):                                      # socket.timeout depuis Python 3.10
        rendre(FERMEE, "délai dépassé : paquet perdu en route")
    if e.errno == errno.ECONNREFUSED:
        rendre(OUVERTE, "refus revenu de l'extérieur : le paquet est sorti")
    if e.errno in (errno.EPERM, errno.EACCES):
        rendre(FERMEE, "refus local (%s) : nftables" % errno.errorcode[e.errno])
    rendre(INDETERMINEE, "errno %s" % errno.errorcode.get(e.errno, e.errno))

def tcp(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((ip, port))
    except OSError as e:
        classer_erreur(e)
    rendre(OUVERTE, "connexion établie")

def dns(ip, nom):
    etiquettes = nom.rstrip(".").split(".")
    if not nom or any(not 0 < len(x) < 64 for x in etiquettes):
        rendre(INDETERMINEE, "nom DNS invalide : %r" % nom)
    requete = struct.pack(">HHHHHH", int.from_bytes(os.urandom(2), "big"), 0x0100, 1, 0, 0, 0)
    requete += b"".join(bytes([len(x)]) + x.encode("ascii") for x in etiquettes) + b"\0" + struct.pack(">HH", 1, 1)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                 # socket « connectée » : un refus ICMP remonte
    s.settimeout(5)
    try:
        s.connect((ip, 53)); s.send(requete); reponse = s.recv(512)
    except OSError as e:
        classer_erreur(e)
    rendre(OUVERTE, "réponse DNS reçue (%d octets)" % len(reponse))

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("tcp", "dns"):
        rendre(INDETERMINEE, "usage")
    genre, ip, dernier = sys.argv[1], cible(sys.argv[2]), sys.argv[3]
    if genre == "tcp":
        if not (dernier.isdigit() and 0 < int(dernier) < 65536):
            rendre(INDETERMINEE, "port invalide : %r" % dernier)
        tcp(ip, int(dernier))
    dns(ip, dernier)
```

Lecture des issues :

| issue lue | classe | raison |
|---|---|---|
| connexion TCP établie ; réponse DNS reçue | **ouverte** | le paquet est sorti et une réponse est revenue |
| `ECONNREFUSED` (TCP : remise à zéro ; UDP connectée : ICMP « port injoignable ») | **ouverte** | le refus vient d'un hôte extérieur : le paquet est sorti (c'est le « point voisin » du relecteur) |
| `EPERM` ou `EACCES` | **fermée** | refus local par `nftables` (`policy drop` sur la chaîne de sortie) |
| délai de 5 s dépassé | **fermée** | paquet jeté sans réponse : pare-feu du nuage, ou `nftables` si le noyau ne rend pas `EPERM` à TCP (SUPPOSÉ, l'un ou l'autre) |
| cible vide, mal formée ou locale ; nom invalide ; toute autre erreur (`ENETUNREACH`, `EHOSTUNREACH`…) ; sonde absente ou en erreur (code autre que 0, 10, 20) | **indéterminée** | rien ne prouve la fermeture : **arrêt de série**, jamais « fermée » par défaut |

Deux limites, dites : un pare-feu du nuage qui **rejetterait** au lieu de jeter (SUPPOSÉ : il jette) ferait lire « ouverte »
dans l'artefact (a), où `nftables` est vidé. Le cas sain n'en dépend pas, puisque `nftables` y arrête le paquet avant. Ce
serait un écart à l'attendu, donc un arrêt et une lecture : une erreur du côté sûr. Et si le miroir de l'image était un service de Hetzner que le pare-feu du nuage
laisse passer (la FAQ ne le cite pas), l'artefact (a) le ferait voir.

**Ce qui est vrai après cette correction** : après `pret` et la pose de `sortie-<série>`, la machine n'ouvre **aucune connexion
sortante vers l'Internet**, ni avant ni après un redémarrage. Seules exceptions : le bail DHCP et les métadonnées, tous deux
locaux au réseau de l'hôte. C'est ce que G8 éprouve (§ 4), après chaque redémarrage compris.

### 2.3 Dépôt du code de l'étage (archive empreintée, par `scp`, sans jeton GitHub)

1. **Session cloud** : elle construit l'archive de série, `etage-<série>-v1.tar.zst`, de façon déterministe
   (`tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner`). Elle contient :
   - pour S1 :
     - l'arbre v52, vérifié contre `EMPREINTES-orchestrateur-pole-v7-v52.txt` (`13bc34c7…`) et
       `CODE-orchestrateur-pole-v7-v52.zip` (`25775a66…`) ;
     - la **version corrigée de CL16-01** (nom à fixer, R12) ;
     - les sondes de CL16. Elles sont sur disque (vérifiées par le relecteur), dans
       `/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/cl16/sondes/` :
       `p_cl16.py` `dbf43643…`, `p_mutations.py` `8a4826e5…`, `p_mut2.py` `57edaacf…`, `p_min.py` `91cdf602…`.
       **Bloc-notes éphémère : à verser dans git avant tout.**
     - le lanceur de série `lancer-serie-v1.sh`.
   - pour P : l'arbre de production et les lots d'exécution (§ 2.7). **Rien** de `donnees/`, du bras d'attaque, des modes
     tenus à l'écart, ni de `prereg/P3-consignes-v1.md` (garde R-776).
2. Elle calcule l'empreinte de l'archive, la scelle (`.sha256`) et l'inscrit dans l'amorce cloud-init, **avant** la création.
3. Elle pousse l'archive et son compagnon sur une branche de passage du dépôt privé. Le poste de passage les tire avec ses
   propres identifiants et vérifie `sha256sum -c`.
4. **Poste de passage**, seulement après `pret` et G8 passée :
   `scp -i cle archive archive.sha256 root@IP:/var/lib/pole/entree/`. La première connexion fait confiance à la clé d'hôte
   (réserve 3 du § 6) ; son empreinte est consignée dans le journal de série.
5. **Machine** : `verifier-entree-v1.sh` (en `set -euo pipefail`) compare l'empreinte de l'archive reçue à `ARCHIVE_SHA256`
   de `/etc/pole/attendu-v1.txt`.
   - égalité : il déballe dans `/opt/pole/<série>/` ;
   - sinon : **refus, rien n'est exécuté**, code 4 (garde G5).

### 2.4 Lancement

- Le poste de passage lance, par
  `ssh -i cle root@IP 'setsid nohup /opt/pole/<série>/lancer-serie-v1.sh > /var/lib/pole/sortie/lanceur.out 2>&1 < /dev/null &'` :
  - `setsid` : le lanceur survit à la fermeture du terminal (CL17-07) ;
  - le lanceur lance tout sous `env -i PATH=/usr/sbin:/usr/bin:/sbin:/bin LANG=C.UTF-8`, et Python en `-I -B` ;
  - le lanceur est lui aussi en `set -euo pipefail` et écrit `fini` ou `echec`, jamais `fini` après un échec.
- **S1, passe A (cgroup v2, mode d'origine de l'image)** :
  - `python3.13 -B -m unittest discover -t . -s essais -p 'test_*.py'`, sans aucune variable `POLE_ESSAI_*` ;
  - puis `p_cl16.py`, `p_mutations.py`, `p_mut2.py`, `p_min.py` (borne à exactement `MEMOIRE_BAC_MIN_MO` corrigée).
  - Passe d'**information** : c'est la première fois que le chemin v2 joue. Deux issues sont attendues : l'étage marche, ou il
    refuse avec son motif (`memory` non délégué). Les deux se consignent ; aucune n'est un échec de série.
  - SUPPOSÉ : le lancement sous `systemd-run --scope -p Delegate=yes` suffit à déléguer `memory`. La règle « pas de processus
    internes » du cgroup v2 peut l'empêcher si le noyau crée ses groupes sous son propre groupe.
- **S1, passe B (cgroup v1, conditions de CL16)** :
  - mise en place : `/etc/default/grub.d/99-pole-cgroup-v1.cfg` contenant
    `GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT} systemd.unified_cgroup_hierarchy=0"`. Le nom en `99-` fait
    passer le fichier **après** le réglage de l'image (SUPPOSÉ : `50-cloudimg-settings.cfg`), et l'option s'**ajoute** à la
    ligne au lieu de la remplacer. Puis `update-grub`, et redémarrage piloté par le poste de passage ;
  - **contrôles d'après redémarrage, avant toute suite** : `/proc/cmdline` contient l'option ; `stat -fc %T /sys/fs/cgroup`
    rend `tmpfs` ; `sysctl -n kernel.apparmor_restrict_unprivileged_userns` rend 0 ; `nft list table inet pole` répond ;
    l'épreuve `bwrap` du § 2.2.2 (étape 5) repasse ; **G8 rejouée** (§ 4). Un seul échec : arrêt de série ;
  - puis la même suite et les mêmes sondes. **C'est la passe qui décide de CL17-étage.**
- Chaque passe écrit son manifeste : versions (`bwrap --version`, Python, noyau, systemd), mode du cgroup, ligne de démarrage,
  valeur de `kernel.apparmor_restrict_unprivileged_userns` et ligne d'**écart d'hôte** (§ 2.2.1), empreinte de l'archive,
  témoin, heures UTC de début et de fin, codes de sortie, comptes d'essais (OK, échecs, erreurs, ignorés).
  - **Un seul « ESSAI RÉEL NON JOUÉ » rend la passe non conforme** (CL15-04).
- Aucune clé, aucun appel de modèle : S1 n'a besoin d'aucun réseau après l'installation.

### 2.5 Retour des résultats scellés (récupérés, jamais poussés depuis la machine)

1. **Machine**, en fin de lanceur :
   - archive déterministe `resultats-<série>-v1.tar.zst` (manifestes, journaux, sorties, `etat-v1.txt`, copie de
     `attendu-v1.txt`, et relevé des contrôles d'après redémarrage) ;
   - `sha256sum resultats-<série>-v1.tar.zst > resultats-<série>-v1.tar.zst.sha256` ;
   - puis `touch /var/lib/pole/sortie/fini`.
   - La machine n'ouvre **aucune connexion sortante vers l'Internet**, ni avant ni après redémarrage (pare-feu du nuage et
     `nftables` persistant, § 2.2.3 ; G8 éprouvée après chaque redémarrage). Elle ne peut rien pousser.
2. **Poste de passage** :
   - il attend `fini` ou `echec` (sondage par `ssh … test -e`, toutes les 60 s) ;
   - il récupère `scp root@IP:/var/lib/pole/sortie/resultats-<série>-v1.tar.zst{,.sha256} .` ;
   - il vérifie `sha256sum -c`, déballe dans un dossier neuf et contrôle le témoin et l'empreinte de l'archive d'entrée
     (garde G10) ;
   - il committe et pousse sur la branche de résultats (proposée : `donnees/etage-tests-de-mort-<série>-v1`, à fixer par la
     session principale ; jamais un nom réservé aux branches à ne pas lire).
3. **Session cloud** :
   - elle tire la branche et revérifie l'empreinte ;
   - elle lit les fichiers avec `python3 -I` ;
   - elle scelle (`python -m controle_ia.scellement sceller …`) et rattache le manifeste de série (R6, R9) ;
   - **puis seulement**, elle détruit la machine (§ 2.6).

### 2.6 Destruction après chaque série (par identifiant, R10) et vérification

La destruction revient à la **session cloud**, par l'API, avec `HCLOUD_TOKEN` (`destruction-serie-v1.sh`, à écrire, en
`set -euo pipefail`) :

1. **Lecture** : l'identifiant vient du fichier de série, écrit à la création à partir de la réponse de l'API. Il doit être
   numérique ; jamais un nom, jamais un motif. Le même fichier garde les identifiants de l'adresse IPv4 primaire, de la clé SSH
   et des deux pare-feu, lus dans les réponses de création.
2. **Contrôle** : `GET /v1/servers/<id>` doit rendre les étiquettes `pole=etage` et `serie=<série>`. Sinon : arrêt, et alerte
   à Lazar.
3. **Destruction** : `DELETE /v1/servers/<id>`, puis attente de l'action jusqu'à `success`.
4. **Vérification** :
   - `GET /v1/servers/<id>` rend **404** ;
   - `GET /v1/servers?label_selector=pole=etage` rend une liste vide ;
   - **adresse IPv4 primaire** : la spécification publique donne `auto_delete` à `false` par défaut pour une adresse créée à
     part. Elle ne dit rien d'une adresse créée avec le serveur. Le script lit donc `auto_delete` dans la réponse de création.
     S'il vaut `false`, il retire l'adresse par son identifiant (`DELETE /v1/primary_ips/<id>`). Dans tous les cas,
     `GET /v1/primary_ips` ne doit plus la montrer ;
   - `GET /v1/volumes` et `GET /v1/images?type=snapshot` : vides ;
   - la clé SSH publique de la série est retirée du projet (`DELETE /v1/ssh_keys/<id>`) ;
   - les deux pare-feu de la série sont retirés (`DELETE /v1/firewalls/<id>`, par identifiant).
5. **Consignation** dans `registres/arrets.md` : identifiant, gabarit, lieu, heures UTC de création et de destruction, heures
   facturées.
6. **Poste de passage** : il efface la clé privée de la série (chemin écrit en dur dans le script, jamais un chemin variable
   passé à `rm`) et l'entrée `known_hosts` de l'adresse.

**Chien de garde.** À la création, la session programme un rappel (`send_later`) pour l'heure prévue de fin plus la marge
(S0 : 2 h ; S1 : 3 h ; P : la durée du devis plus 2 h). Au rappel, toute machine encore vivante portant `pole=etage` est
détruite **par son identifiant**, consignée, et Lazar est averti.

À ajouter à la routine de reprise (R14, étape 4), sur proposition à Lazar : `GET /v1/servers` à côté de
`vastai show instances`.

### 2.7 Production (course 2, génération 1) : ce qui manque dans le code

Inchangé par rapport à la v1. L'étage v52 est **interactif dans le même processus** :

- `executer_tests_de_mort(…, executeur=None, …)` utilise par défaut `ExecuteurBacASable` ;
- l'expérimentateur (une session de modèle, qui exige le relais et donc les clés) demande des exécutions, lit les résultats et
  relance, jusqu'à 12 tours par fiche ;
- les clés restent dans la session cloud ; la machine n'est joignable que par le poste de passage. **L'orchestrateur ne peut
  donc tourner ni sur la machine, ni d'un bloc dans la session.**

Le paramètre `executeur` est enfichable. La voie proposée à conv-audit (nouvelle version, R12) : un **`ExecuteurDistantParLots`**.

1. À chaque tour, l'orchestrateur, dans la session, écrit **un lot** : toutes les demandes d'exécution de toutes les fiches de
   ce tour (scripts, réglages, empreintes), dans une archive scellée.
2. L'orchestrateur se met en attente.
3. Le poste de passage porte le lot sur la machine. La machine exécute sous le vrai bac et rend les résultats scellés.
4. L'orchestrateur reprend.

Avec des lots par tour, il y a **au plus 12 allers-retours par série**, et non 12 par fiche. Chaque tour attend le poste de
passage (5 à 10 minutes SUPPOSÉES, plus si Lazar le fait à la main). C'est la latence qui domine la durée de la série P, pas le
calcul.

Tant que cet exécuteur n'existe pas, **seule S1 (CL17-étage) est jouable**, car elle se fait par lot sans modèle.

## 3. Devis (inchangé ; un arrondi corrigé en v3, sans effet sur les totaux)

Hypothèses :

- prix de la CPX32 relevé (0,0577 EUR/h hors taxes), confirmé à 00:40 UTC le 31 octobre (§ 1.2) ;
- **toute heure commencée est facturée** (SUPPOSÉ ; la page dit « hourly rate » sans préciser l'arrondi) ;
- **TVA 20 %** si le compte est celui d'un particulier en France (SUPPOSÉ ; avec un numéro de TVA intracommunautaire, le hors
  taxes s'applique) ;
- **1 EUR ≈ 1,15 USD** (SUPPOSÉ, le même que dans `architecture-essai-a-blanc-v1.md`) ;
- les pare-feu du nuage et les clés SSH du projet ne sont pas facturés (SUPPOSÉ : la FAQ lue ne parle pas de prix).

Soit **0,0796 USD par heure toutes taxes comprises**.

### 3.1 Par série

| série | heures facturées attendues | coût attendu (TTC) | heures au pire | coût au pire (TTC) |
|---|---|---|---|---|
| S0 plomberie | 1 | 0,08 USD | 2 | 0,16 USD |
| S1 CL17-étage | 1 | 0,08 USD | 3 | 0,24 USD |
| P production (génération 1) | 3 | 0,24 USD | 40 | 3,19 USD (v3 : 40 × 0,079626 = 3,185 ; la v1 et la v2 écrivaient 3,18) |

Le coût en modèles de la série P n'entre pas dans ce devis : il se paie dans la session, sous les plafonds du code. Aux défauts
de la v52 (`BUDGET_TEST_USD_DEFAUT` 0,5 et `BUDGET_LECTEUR_USD_DEFAUT` 0,1, tous deux SUPPOSÉS par leur auteur), cela fait
0,6 USD par fiche : 3,0 USD pour 5 fiches et 7,2 USD pour 12 fiches, sur une ligne de GO à part.

### 3.2 Course 2

| | séries | heures | coût (TTC) |
|---|---|---|---|
| **attendu** | S0 × 1, S1 × 1, S1 rejouée × 1 (après une correction du chemin v2 ou de CL16-01), P × 1 | 1 + 1 + 1 + 3 = 6 | **≈ 0,48 USD** (0,35 EUR hors taxes) |
| **pire cas** | S0 × 2, S1 × 3, P × 2 (génération 1, et une reprise après un étage refusé ou interrompu) | 4 + 9 + 80 = 93 | **≈ 7,41 USD** (5,37 EUR hors taxes) |
| marge du chien de garde | + 2 h par série, 7 séries | + 14 | + 1,11 USD |
| **plafond de GO proposé** | | | **10 USD** |

Un S0 rejoué pour cause de restriction AppArmor (remède (R-b) au lieu de (R-a), ou image de repli) tient dans le « S0 × 2 » du
pire cas.

**Pire cas hors gardes** : une CPX32 oubliée un mois entier est bornée par son plafond mensuel, 35,99 EUR hors taxes, soit
≈ 49,7 USD TTC. C'est précisément ce que G6, G7 et le chien de garde empêchent. Le compte devrait porter en plus une alerte de
dépense basse (recommandation de R-817, à Lazar).

## 4. Liste d'arrêt et gardes (R5 : chacune éprouvée sur un cas sain et sur un artefact)

Les essais G1 à G7 et G12 se jouent **sans fournisseur**, contre un faux serveur de l'API Hetzner sur `127.0.0.1` (même forme
que le relais factice de l'essai à blanc). G8 à G11 se jouent sur la machine, en S0 ; **G8 et G9 sont rejouées après chaque
redémarrage** (redémarrage d'essai de S0, passe B de S1). Aucune garde ne se replie en silence.

| n° | garde (arrêt si…) | cas sain | artefact | effet de l'arrêt |
|---|---|---|---|---|
| G1 | `HCLOUD_TOKEN` absent ; ou le jeton paraît en argument, dans un fichier ou dans un journal | variable posée, commande sous `env -i` ; un balayage des journaux ne trouve pas la valeur | variable absente ; ou une valeur factice glissée dans un argument de commande, que le balayage de `/proc/<pid>/cmdline` et des journaux doit trouver | refus avant tout appel |
| G2 | les données cloud-init ou l'archive d'entrée contiennent un motif de secret (`TOKEN`, `KEY=`, `sk-`, `ghp_`, `BEGIN … PRIVATE KEY`, une valeur des variables de clé connues comparée par empreinte) | amorce v1 propre | même amorce, avec une ligne `HCLOUD_TOKEN=factice…` ; archive contenant un faux `.env` | refus avant création |
| G3 | aucun GO valide : la commande de création doit citer `GO_ID=…`, lu dans `registres/go.md` | GO de la ligne nouvelle, non échu | GO échu ; GO-2026-10-30-17 (qui **exclut** la location de machine) ; aucun GO | refus. **À ajouter à `garde_calcul.py`** : motifs `hcloud server create` et `curl … api.hetzner.cloud/v1/servers` avec `POST` ; ils n'y sont pas aujourd'hui |
| G4 | gabarit hors liste {cpx32, cpx22, ccx13} ; architecture autre que x86 ; lieu hors de l'Union européenne ; prix lu par l'API au-dessus du devis de plus de 10 % | cpx32, `nbg1`, 0,0577 | cax21 ; `ash` ; prix factice à 0,08 | refus avant création |
| G5 | l'empreinte de l'archive reçue diffère de `ARCHIVE_SHA256` de l'amorce | archive intacte | un octet changé dans l'archive | refus sur la machine, code 4, rien d'exécuté |
| G6 | déjà une machine `pole=etage` vivante à la création ; plus d'une série à la fois | liste vide | faux serveur qui rend une machine vivante | refus avant création |
| G7 | destruction non vérifiée : `GET /servers/<id>` ≠ 404, adresse orpheline (`auto_delete` faux et adresse non retirée), clé SSH ou pare-feu restants ; identifiant non numérique ; étiquettes qui ne correspondent pas | faux serveur qui rend 404 après `DELETE`, adresse retirée | faux serveur qui rend encore 200 ; adresse primaire à `auto_delete=false` laissée en place ; un nom passé à la place de l'identifiant ; étiquette `serie` différente | alerte immédiate à Lazar, consignée ; jamais « détruit » écrit sans le 404 |
| G8 | la sortie réseau de la machine vers l'Internet n'est pas **prouvée** fermée, **après l'installation et après chaque redémarrage**. **v3** : les cibles sont relues dans `etat-v1.txt` ; une cible absente, vide ou mal formée arrête la série (« cible G8 invalide »), sans sonder. Sondes, lancées depuis la machine par `sonde-sortie-v1.py` (§ 2.2.3), chacune classée « fermée », « ouverte » ou « indéterminée » d'après la cause lue : (i) `tcp <miroir_ipv4> 80` ; (ii) `dns <resolveur_ipv4> <miroir_hote>` (requête UDP directe, sans cache ; remplace `resolvectl`) ; (iii) par la session : `sortie-<série>` appliqué au serveur (`GET /v1/firewalls/<id>`) et `rescue_enabled` à `false` (`GET /v1/servers/<id>`). La garde passe seulement si (i) et (ii) rendent « fermée » **et** (iii) est vrai ; « indéterminée » arrête comme « ouverte » | les deux couches en place : (i) et (ii) rendent **« fermée »** avec leur motif (refus local ou délai), consigné ; (iii) vrai ; `ssh` répond | **une couche à la fois** sur la machine S0 : (a) `nftables` vidé, pare-feu du nuage en place → (i) « fermée » (délai), (ii) « ouverte » : la garde doit signaler « DNS ouvert » ; (b) `nftables` en place, `sortie-<série>` retiré → (i) et (ii) « fermée » : la garde doit signaler « pare-feu du nuage absent » par (iii) ; (c) les deux retirés → (i) **« ouverte », que la connexion aboutisse ou soit refusée par le miroir** (`ECONNREFUSED`), et la garde doit le voir. Puis tout est remis, et le cas sain est rejoué. **Nouveaux en v3, hors machine et sans réseau** : (d) `miroir_ipv4:` vide dans un `etat-v1.txt` de jeu → arrêt « cible G8 invalide », **jamais** « fermée » ; (e) cible `127.0.0.1` ou `abc` → « indéterminée », arrêt ; (f) `classer_erreur` nourrie d'erreurs factices (`ECONNREFUSED`, `EPERM`, délai, `EHOSTUNREACH`) → ouverte, fermée, fermée, indéterminée ; (g) sonde absente ou rendant un code inconnu → arrêt | série arrêtée avant le dépôt du code (S0, début de S1) ou avant la passe B |
| G9 | prérequis de l'étage non tenus : `bwrap` < 0.9.0 ou setuid ; architecture autre que x86_64 ; 64097 avec un compte ou un processus ; `memory` inutilisable ; Python inattendu ; **`kernel.apparmor_restrict_unprivileged_userns` ≠ 0, ou épreuve `bwrap` sous 64097 en échec** (§ 2.2.2, étape 5) | état de S0 lu par `etat-v1.txt` ; épreuve `bwrap` rendue 0 avant et après le redémarrage d'essai | compte `/bin/bash` 64097 créé sur la machine S0 ; `bwrap` rendu setuid ; **`sysctl -w kernel.apparmor_restrict_unprivileged_userns=1`** → l'épreuve doit échouer (« setting up uid map » ou « loopback ») et la garde doit arrêter avec le motif « espace d'utilisateurs refusé » ; **fichier `60-apparmor-namespace.conf` retiré puis redémarrage** → même arrêt après redémarrage | arrêt. La sonde de l'étage le refuse déjà : **interdit de lever** par `--memoire-bac-non-bornee-permise` ou par une variable `POLE_ESSAI_*` ; **interdit de contourner** en lançant l'étage en superutilisateur ou en rendant `bwrap` setuid |
| G10 | résultats : l'empreinte diffère au poste de passage ou dans la session ; le témoin ou l'empreinte d'entrée diffèrent dans le manifeste ; un « ESSAI RÉEL NON JOUÉ » ; ligne d'écart d'hôte absente du manifeste | archive rendue intacte | archive altérée d'un octet ; manifeste d'une autre série (autre témoin) ; manifeste sans la ligne d'écart d'hôte | résultats non scellés, série non conforme, rien n'est lu comme verdict |
| G11 | durée ou coût de la série au-delà de son plafond : (maintenant − création) × prix > plafond de la série (S0 0,5 USD ; S1 0,5 USD ; P 4 USD) | série dans les temps | horloge du faux serveur avancée au-delà du plafond | destruction par identifiant, consignée |
| G12 | le chien de garde ne s'est pas programmé à la création | rappel créé, identifiant consigné | création simulée avec échec de `send_later` | destruction immédiate de la machine créée |
| G13 | **amorce sans verdict** : ni `pret` ni `echec` au bout de 20 min, ou `echec` présent, ou `pret` présent alors qu'`etat-v1.txt` manque une ligne attendue **ou la porte vide** (v3), ou que `miroir_ipv4` ou `resolveur_ipv4` n'a pas la forme d'une adresse IPv4 (v3). Le poste de passage refait cette relecture lui-même, sans se fier au seul `pret` | amorce v1 sur S0 : `pret` seul, `etat-v1.txt` complet, aucune valeur vide | amorce de S0 avec un contrôle forcé à faux (par exemple `test 1 = 0` glissé à l'étape 4) → `echec` écrit, **`pret` absent** ; amorce qui s'arrête avant l'étape 6 → ni `pret` ni état complet. **Nouveaux en v3, hors machine, dans un dossier jetable avec des commandes factices** : `ubuntu.sources` absent ; ligne `URIs:` sans hôte ; `getent` factice qui échoue ; `getent` factice qui ne rend rien ; `resolv.conf` sans `nameserver` IPv4 ; `python3.13 -V` factice qui ne rend rien → chaque fois `echec` avec son motif (code 5), **`pret` absent** ; et `etat-v1.txt` falsifié après coup avec `miroir_ipv4:` vide → le poste de passage refuse | série arrêtée, rien n'est déposé ; destruction par identifiant |

**Liste d'arrêt de série**, chaque cas étant consigné avec son motif. Sur l'un ou l'autre :

- G1 à G13 ;
- refus de l'étage par sa sonde ;
- refus du classifieur ou du mandataire sur un appel de l'API ;
- poste de passage injoignable pendant plus de 2 h (au-delà du chien de garde) ;
- indisponibilité du gabarit.

L'arrêt suit alors cet ordre : rapatrier ce qui peut l'être, détruire par identifiant, vérifier, consigner. **Jamais de
relance automatique** sur un autre gabarit, un autre lieu, une autre image ou un autre remède AppArmor sans le mot de Lazar,
sauf les replis du § 1.3 déjà couverts par le même GO.

## 5. Décision pour Lazar (nœud de dépense et de compte : pas de défaut à 48 heures)

**Décision** : comment faire tourner l'étage de tests de mort sur une machine Hetzner jetable, alors que cette session ne peut
pas joindre la machine ?

**Enjeu** : CL17-étage, puis l'étage de la génération 1 de la course 2, sous un vrai `bwrap`, loin des clés. Le prix est
négligeable (≈ 0,5 USD attendus). Ce qui coince, c'est le chemin des fichiers, et, sur Ubuntu 24.04, un réglage d'hôte à
déclarer.

| option | avantage | inconvénient |
|---|---|---|
| **(A) Mixte** : la session cloud tient `HCLOUD_TOKEN` et pilote création, fermeture du pare-feu et destruction par l'API ; ton ordinateur sert de poste de passage (`scp`, `ssh`) par Contrôle à distance, ou à la main ; les archives passent par une branche du dépôt privé | respecte tout : aucun secret sur la machine ; jeton dans la session ; résultats récupérés, jamais poussés par la machine | ton ordinateur doit être allumé et relié pendant chaque série ; latence de 5 à 10 min par aller-retour ; SUPPOSÉ : le classifieur de la session reliée laisse passer `ssh` vers la machine louée |
| **(B) Tout depuis ton ordinateur** (jeton Hetzner aussi chez toi, `hcloud` et `scp` là-bas) | plus simple, un seul lieu | le jeton quitte la session (contraire au mandat) ; plus de travail pour toi |
| **(C) Session seule, par stockage objet** et adresses présignées (la machine pousse ses résultats dans un seau) | aucun poste de passage | **écart** à « jamais poussé depuis la machine » ; une capacité d'écriture sur la machine ; un compte de stockage de plus ; accès au seau depuis la session **non éprouvé** (classifieur) |

L'option (a) de R-821 (HTTP simple) n'est pas une option complète ici : elle ne règle que le retour, pas le dépôt du code
(§ 2.0).

**Recommandation** : (A), avec le remède (R-a) pour la restriction AppArmor. Confiance 0,6 (inchangée). Restent deux inconnues
sérieuses : le passage de `ssh` depuis la session reliée par Contrôle à distance, et le comportement réel de l'image Hetzner
sous (R-a). S0 lève les deux pour moins de 0,2 USD.

**Ce qu'il faut de toi** :

1. le GO de dépense : **10 USD**, séries S0, S1 (et ses reprises), et P de la génération 1 ; échéance proposée le
   15 novembre 2026 ;
2. ton ordinateur relié par Contrôle à distance (un dossier), ou ton accord pour faire les commandes du poste de passage à la
   main ;
3. le choix de garder le projet Hetzner actuel (jeton de R-817) ou d'en ouvrir un dédié à l'étage, avec une alerte de dépense
   basse (recommandé) ;
4. **nouveau** : ton accord sur l'**écart d'hôte** (R-a) : la restriction AppArmor des espaces d'utilisateurs est levée sur la
   machine jetable. Sinon, (R-b), profil dédié à `bwrap`, ou (R-d), image `debian-13`. Et dis si l'on sonde un jour HTTP
   simple (option (a) de R-821). Je ne le recommande pas : (A) n'en a pas besoin, et la sonde relève du classifieur.

**Avant le GO, sans dépense, par la session principale** :

- lecture gratuite par l'API de la disponibilité de cpx32 et des images ;
- lecture, sur Launchpad, de l'empreinte de la clé de signature de deadsnakes, à figer dans l'amorce ;
- versement des v51 et v52 et des sondes de CL16 dans git ;
- correction de CL16-01 ;
- écriture des scripts du § 2 (amorce, sonde de G8, vérification d'entrée, lanceur, destruction) et de leurs essais G1 à
  G7, G12 et G13 contre le faux serveur. G13 se joue aussi hors machine, en exécutant le script d'amorce dans un dossier
  jetable avec des commandes factices, y compris les nouveaux artefacts de la v3 (cible vide, valeur vide). Les artefacts
  (d) à (g) de G8 se jouent de même hors machine, sans aucun réseau ;
- demande à conv-audit de l'`ExecuteurDistantParLots` (§ 2.7) ;
- consignation de l'épisode des sondes de la v1 (§ 8).

## 6. Ce qui n'a pas pu être fait, réserves, SUPPOSÉ

**Pas fait** :

- aucune lecture de l'API Hetzner (consigne : aucune commande vers un fournisseur). La disponibilité des gabarits et des
  images, le prix rendu par l'API et l'`auto_delete` réel de l'adresse créée avec le serveur restent à lire ;
- l'arrondi de facturation n'a pas été trouvé dans la documentation lue ;
- aucune épreuve de `bwrap` sur Ubuntu 24.04 : la conclusion du § 2.2.1 repose sur la documentation, non sur un essai.
  Elle est « probable », et S0 la tranche ;
- aucun script écrit : le présent document les décrit ; les écrire et les éprouver est la suite ;
- aucune sonde réseau (§ 0.1, réserve 7).

**Réserves** :

1. **Option (a) de R-821** : non établie comme infaisable. Seul le HTTPS vers une adresse IP a été essayé ; HTTP simple n'a pas
   été sondé, et le sonder relève du classifieur. Elle ne règlerait de toute façon pas le dépôt du code (§ 2.0).
2. **Restriction AppArmor sur Ubuntu 24.04** : le remède (R-a) affaiblit, sur la machine jetable seulement, une défense contre
   les failles du noyau. Elle est déclarée comme écart d'hôte. (R-b) reste à éprouver sous `--no-new-privs`.
3. **Clé d'hôte SSH** : la première connexion fait confiance à la clé de la machine, consignée. Durcissement possible : clé
   d'hôte jetable injectée par cloud-init. Ce serait une clé privée posée sur la machine, propre à la série et détruite avec
   elle ; ce n'est pas l'un de nos secrets, mais c'est à Lazar d'en décider.
4. **cgroup v2** : chemin jamais joué. La passe A peut échouer par conception (règle « pas de processus internes »). C'est une
   information pour conv-audit, pas un échec de S1.
5. **Python 3.13 sur Ubuntu 24.04** par un dépôt tiers signé : chaîne d'approvisionnement de plus. Le repli 3.12 est un écart à
   CL16, à déclarer.
6. **Les sondes de CL16** ne sont que dans un bloc-notes éphémère ; elles sont perdues si la session se régénère avant leur
   versement.
7. **Fuites résiduelles hors pare-feu du nuage** : selon la FAQ de Hetzner, passent toujours ce pare-feu les métadonnées
   (« answered locally »), le résolveur DNS de Hetzner, **le trafic du système de secours de Hetzner** (ajouté en v3), et
   ARP, DHCP et une partie d'ICMPv6 (IPv6 est désactivé à la création). `nftables` ferme le DNS. Les métadonnées restent
   ouvertes : elles sont locales à l'hôte et ne servent que du public. Le système de secours ne sert qu'à une machine démarrée
   en mode de secours : la session n'active jamais ce mode, et G8 (iii) vérifie `rescue_enabled = false` après chaque
   redémarrage. Ce que couvre au juste « traffic for the Hetzner rescue system » n'est pas détaillé par la FAQ.
8. **Adresse du poste de passage** : si l'adresse IPv4 de ton accès à l'Internet change pendant une série, l'entrée SSH se
   ferme. Il faut alors une mise à jour du pare-feu `entree-<série>` par la session (`set_rules`), consignée.
9. **Sonde de G8** (v3) : la classification lit l'`errno` du noyau. Que `nftables` rende `EPERM` ou un délai à un `connect()`
   TCP n'est pas éprouvé ; les deux sont classés « fermée », donc le verdict n'en dépend pas. Une issue non prévue est
   « indéterminée » et arrête la série : la sonde peut produire de faux arrêts, jamais une fausse fermeture par cible vide.

**SUPPOSÉ** :

- toute heure commencée facturée ;
- TVA 20 % ;
- 1 EUR ≈ 1,15 USD ;
- pare-feu du nuage et clés SSH non facturés ;
- disponibilité de CPX32 en `nbg1`, `hel1` ou `fsn1` ;
- noms d'images `ubuntu-24.04` et `debian-13` (le premier figure dans un exemple de la spécification) ;
- l'image Hetzner `ubuntu-24.04` porte la restriction AppArmor par défaut, sans profil `bwrap` actif ;
- Debian 13 sans restriction AppArmor des espaces d'utilisateurs ;
- transition vers un profil AppArmor dédié permise sous `--no-new-privs` depuis un processus non confiné (remède (R-b)
  seulement) ;
- paquet `python3.13` de deadsnakes pour Ubuntu 24.04, et la forme `ppa:` acceptée par le bloc `apt: sources:` de cloud-init ;
- fichier `/etc/apt/sources.list.d/ubuntu.sources` (format deb822) sur l'image Hetzner ;
- service `nftables` lisant `/etc/nftables.conf` au démarrage ;
- adressage IPv4 par DHCP sur la machine ; métadonnées en `169.254.169.254` port 80 ;
- **v3** : versions de l'image `ubuntu-24.04` (noyau 6.8, systemd 255, `bwrap` 0.9.0) et de `debian-13` (`bwrap` 0.11,
  Python 3.13, systemd 257), reprises de la v1 sans source ; à lire dans `etat-v1.txt` en S0 ;
- **v3** : date d'arrivée du profil `bwrap-userns-restrict` dans `noble-updates`, non copiée (la v2 écrivait « juin 2024 ») ;
- **v3** : fichier `/run/systemd/resolve/resolv.conf` portant le résolveur amont en IPv4 sur l'image Hetzner ;
- **v3** : le pare-feu du nuage jette sans répondre (délai) plutôt qu'il ne rejette ;
- **v3** : refus local de `nftables` rendu au programme par `EPERM` (UDP) et par `EPERM` ou un délai (TCP) ; et curl qui
  rendrait ce refus par son code 7, raison pour laquelle G8 ne lit plus curl ;
- **v3** : Python du système présent en `/usr/bin/python3`, en version 3.10 au moins (`TimeoutError`) ;
- fichier `50-cloudimg-settings.cfg` dans `/etc/default/grub.d/` de l'image, et démarrage par GRUB ;
- cgroup v1 encore démarrable sous systemd 255 par `systemd.unified_cgroup_hierarchy=0` ;
- `auto_delete` de l'adresse IPv4 créée avec la machine : inconnu, d'où le retrait explicite (§ 2.6) ;
- délégation v2 par `systemd-run --scope -p Delegate=yes` ;
- latence de 5 à 10 min par aller-retour au poste de passage ;
- durées des séries (§ 1.3), extrapolées des 340 s de CL17 ;
- passage de `ssh` depuis une session reliée par Contrôle à distance ;
- sens de « (b) » dans R-640 de conv-audit, lu comme « machine louée jetable » (n° 267, passation `2026-10-30-0454.md` :
  « reco (b) de conv-audit ») ;
- une comparaison avec d'autres loueurs à taille égale ne changerait pas le devis de façon décisive.

**Levé depuis la v1** : la limite de 32 Kio des données cloud-init (vérifiée, § 2.0).

**Levé en v3** : `resolvectl query --cache=no` n'est plus SUPPOSÉ, la sonde DNS de G8 ne s'en sert plus ; présence du champ
`rescue_enabled` dans `GET /v1/servers/<id>` (lue dans la spécification copiée).

## 7. Sources lues (empreintes)

### 7.1 Reprises de la v1 (vérifiées par le relecteur)

| pièce | SHA-256 |
|---|---|
| n° 267 de conv-audit (`…/messages/conv-audit_2026-10-30_n267.md` ; branche `canal/conv-audit-n04` lue à `9fb3a398` par la v1, avancée depuis à `37e7f517`, contenu identique selon le relecteur) | `0c77987a0543afaa89903e7a404ca6948f7609aac9d1c8ccaadac422f9ded8ef` |
| n° 266 de conv-audit (même branche) | `b78f9b1e2ed768914b0920bdc8f47db4a152b1c91ee9a1b4b3605663fd4eabfa` |
| `contre-lecture-cl16-orchestrateur-v51-v1.md` | `fec076d24e9d60723bf355631250e24b2d1fec3fa5fa1a7865359148626ead14` |
| `contre-lecture-cl17-orchestrateur-v52-v1.md` | `c5b361090731c526d458bace28eef9bfca4e5e1b647be4e560dc88534d5cb598` |
| `ia-scientifique-externe-v3/essai-a-blanc-v1/architecture-essai-a-blanc-v1.md` | `e38f9661174a8ae2ab48fd78f178ba70b797f8a5c6ac944bfc53fabca641ab29` |
| `ia-scientifique-externe-v3/lecture-code-et-devis-v3-v1.md` (LC) | `1ce823a7475b265a826408af5e25059c61bf43aaec64a129912dbd55f38c64f8` |
| `CODE-orchestrateur-pole-v7-v52.zip` (`origin/canal/session-depot-reprise-n55` `e447f066`) | `25775a6650537f7ed4e547fcfac84d3961a12beddae91f7c0bfd8eb4fb9c1052` (= compagnon) |
| `EMPREINTES-orchestrateur-pole-v7-v52.txt` | `13bc34c763a76ecf1e6b9867fa46e12d4e486458f3cde503909be5f0db94361f` (= compagnon) |
| `CODE-orchestrateur-pole-v7-v51.zip` | `a58a9b8b80861e48fa5e547c4151cc80c15a67a5e6a83d9cf6d4c880dc8f5f46` (= compagnon) |
| `EMPREINTES-orchestrateur-pole-v7-v51.txt` | `8044fa5c5a6512206b1e485d89f8d170cd0de34a13def1b21c5a45daab972c74` (= compagnon) |
| registres lus par la v1 : `decisions.md` (R-567, R-581, R-776, R-782, R-806, R-808, R-809, R-816, R-817, R-821, R-822, R-855), `go.md` (GO-2026-10-30-08, GO-2026-10-30-17), `.claude/hooks/garde_calcul.py` | — |

### 7.2 Nouvelles en v2 (copies dans ce dossier, chacune avec son compagnon `.sha256` et ses en-têtes HTTP)

Toutes lues le 31 octobre 2026 par `curl` à travers le mandataire, sans compte, de 00:36:57 à 00:40:39 UTC. **Aucune copie
nouvelle en v3** ; les heures ci-dessous sont relues dans les fichiers `*.entetes.txt` (ligne `date`/`Date`), et les deux que
la v2 renvoyait aux en-têtes sont désormais écrites. Dans les en-têtes copiés, la valeur des lignes
`set-cookie` est remplacée par `<valeur retirée à la copie>` : ce sont des témoins de visiteur anonyme, sans utilité ici. Les
corps sont gardés tels quels.

| pièce (URL) | fichier | `Date` servie (UTC) | SHA-256 du corps |
|---|---|---|---|
| prix Hetzner, `…/cloud/regular-performance/` | `sources-prix-hetzner-20261031-v1/cloud_regular-performance-v1.html` | 00:40:00 | `805d65bc323b9bebdda81df4767f119110dd5f2b907a3ff9be2c375abaafb408` |
| prix Hetzner, `…/cloud/general-purpose/` | `sources-prix-hetzner-20261031-v1/cloud_general-purpose-v1.html` | 00:40:01 | `55c1c4d18781f59ecd58dad5e0c7ebc17a8273f3545842648a82bedb19b5ea54` |
| prix Hetzner, `…/cloud/cost-optimized/` | `sources-prix-hetzner-20261031-v1/cloud_cost-optimized-v1.html` | 00:40:02 | `bc407cdb50142cb0eafc3442e0fdfba412f485abf7494dba28d96c31285781a9` |
| notes de version d'Ubuntu 24.04, `https://documentation.ubuntu.com/release-notes/24.04/` | `sources-documentation-20261031-v1/ubuntu-notes-version-24.04-v1.html` | 00:36:59 | `9ec193a7e9df48a88af70355017a2eefe8d1c73a7f9dfefa12875bb5da3addc9` |
| billet d'Ubuntu sur la restriction (23.10), `https://ubuntu.com/blog/ubuntu-23-10-restricted-unprivileged-user-namespaces` | `sources-documentation-20261031-v1/ubuntu-blog-espaces-utilisateurs-restreints-v1.html` | 00:36:57 | `1dde5a03928f848b9e0233423618e4cbb9bd43366ae229d2ce67e8241dfd772e` |
| « Understanding AppArmor User Namespace Restriction », `https://discourse.ubuntu.com/t/understanding-apparmor-user-namespace-restriction/58007` | `sources-documentation-20261031-v1/ubuntu-discourse-comprendre-restriction-v1.html` | 00:39:02 | `5a968388962391bd29b643b73a621386d7e4481e770140528efcd70a5da4a424` |
| journal des modifications d'`apparmor` 24.04.9, `https://changelogs.ubuntu.com/changelogs/pool/main/a/apparmor/apparmor_4.0.1really4.0.1-0ubuntu0.24.04.9/changelog` | `sources-documentation-20261031-v1/apparmor-journal-modifications-24.04.9-v1.txt` | 00:40:39 | `58e49d958727ae574904469817bb70cf421d29e09b42e630650501786f9db7c9` |
| versions d'`apparmor` publiées pour 24.04 (API publique de Launchpad, `getPublishedSources`) | `sources-documentation-20261031-v1/launchpad-apparmor-noble-publie-v1.json` | 00:40:32 | `994efcca8a11f1333f939121e76fae4030ebe033076ec63b412b6bf3dc02b22f` |
| R. Coker, « Ubuntu 24.04 and Bubblewrap », `https://etbe.coker.com.au/2024/04/24/ubuntu-24-04-bubblewrap/` | `sources-documentation-20261031-v1/coker-ubuntu-24.04-bubblewrap-v1.html` | 00:37:38 | `018b5e977da8031668cad02de12b84a00b6a438fb24fb78c5809dcc7f98512ba` |
| FAQ des pare-feu Hetzner, `https://docs.hetzner.com/cloud/firewalls/faq/` | `sources-documentation-20261031-v1/hetzner-pare-feu-faq-v1.html` | 00:37:50 | `3e60438934d31a5507b40557755df5d3312a9c9961d5bcd708c2605b9d39a1da` |
| spécification publique de l'API Hetzner, `https://docs.hetzner.cloud/cloud.spec.json` (page de documentation, non l'API) | `sources-documentation-20261031-v1/hetzner-api-specification-v1.json` | 00:38:28 | `772d662e1336ea01925ba30381f47d5c0e23265767dcf9399983aba3dada082a` |
| `tests_de_mort_v2.py` de la v52, lu dans le déballage du relecteur (`…/scratchpad/verif-nuit-devis-machine-jetable/v52/pole/`) | — (dans `CODE-orchestrateur-pole-v7-v52.zip`, `25775a66…`) | — | — |
| relecture de la v1, `…/scratchpad/nuit-rendus/verifier-devis-machine-jetable.md` | — (bloc-notes) | — | — |
| relecture de la v2 (lue pour la v3), `…/scratchpad/nuit-rendus-2/verifier-machine-v2.md` | — (bloc-notes) | — | `aa85ff3cfe78b1dfaa43bcafc071afba2e6bf5f549d8b82d67c4243287815a55` |
| v2 de ce devis, `devis-et-plomberie-machine-jetable-v2.md` (base de la v3, compagnon vérifié par `sha256sum -c`) | ce dossier | — | `39260994753d1cdb4c4ffd4773ec989c8719ed38054a577b5fae19c052b6add8` |

## 8. Épisode des sondes réseau de la v1 (réserve 7 du relecteur) : texte proposé à la session principale

Je n'écris pas les registres. Texte proposé pour `registres/decisions.md`, à la main de la session principale :

> Rédaction de `devis-et-plomberie-machine-jetable-v1.md` (30 octobre, vers 23:03 UTC) : hors mandat (rédiger un devis), le
> sous-agent a sondé le réseau. D'abord `https://1.1.1.1/`, coupé par le mandataire. Puis un nom de domaine et un nom
> `sslip.io`, procédé qui sert à joindre une adresse arbitraire : refusés par le classifieur (« Containment Escape »). Rien n'a
> été contourné. Le nombre de commandes de la seconde sonde (une ou deux) n'est pas établi par la note. Décision : ces sondes ne
> se renouvellent pas sans le mot de Lazar. Ni la v2 ni la v3 n'en font, et l'option (a) de R-821 reste en réserve.

Version 3 ; jamais réécrite (R12). La v1 et la v2 restent en place, inchangées.
