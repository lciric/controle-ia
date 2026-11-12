# Proposition C — Conception ciblée (Tour III.1)

*Note d'intégrité : Aucune pièce transmise n'est absente, vide ou visiblement coupée.*

---

## Synthèse de la position (Réponse directe à l'arbitre)

* **Choix recommandé :** **« Autre chose »** — un **proposeur à boucle minimale maison (ReAct-bwrap)** en un seul fichier Python ($\le 150$ lignes, illustratif), branché sur le relais v3 existant et l'exécuteur `bwrap` existant, opposé à coût égal au témoin « Kimi, meilleur de $N$ ». Ni Kaimen-Inc/Co-Scientist (a), ni The Agentic Scientist (b) ne doivent être branchés en premier.
* **Raisons :**
  1. **Contre la séquence `(a) puis (b)` du concepteur (erreur méthodologique) :** Kaimen (`cef5bcf`) n'exécute rien (RAPPORTÉ). Lui greffer un outil d'exécution, réécrire ses consignes et l'amputer de sa littérature revient à créer un agent hybride non testé. Surtout, **l'échec de (a) ne falsifie rien concernant (b)** : Kaimen est une architecture de *tournoi Elo d'idées textuelles*, tandis que The Agentic Scientist (Sakana v3) est une architecture de *débogage itératif de code*. Conditionner le test d'un expérimentateur de code au succès d'un tournoi de texte viole l'inférence forte (B4) et la règle N-045 (Kaimen coûtant déjà 7 à 60 fois (estimé) le prix d'un proposeur).
  2. **Pourquoi pas The Agentic Scientist (Sakana v3) d'abord ? (Réponse à Lazar) :** Parce qu'il confond la variable scientifique à tester (*la valeur de l'expérimentation sur les épisodes de développement*) avec un empilement d'ingénierie hostile aux contraintes du programme : démon Docker à pleins droits à enfermer, relais v3 incompatible avec la lecture en flux (HYPOTHÈSE / non vérifié), coût multiplié par 10 à 100 (estimé, 3,6 à 21 USD par génération), phases d'écriture d'article inutiles à amputer, et antécédent rapporté de contournement d'évaluateur.
  3. **Pour la boucle minimale maison (« autre chose ») :** Conformément à N-045 (*le bon marché d'abord, le cher sur preuve*), pour savoir s'il faut payer un cadriciel lourd du marché, il faut d'abord prouver que *la capacité d'exécuter des scripts sur les épisodes de développement* bat l'échantillonnage aveugle (« meilleur de $N$ ») à coût égal. Une boucle minimale (Proposer un script de test $\to$ Exécuter dans `bwrap` $\to$ Lire `stdout/stderr` $\to$ Répéter $\le k$ fois $\to$ Émettre les fiches `{enonce, loi_predictive}`) isole exactement ce mécanisme causal, sans Docker, sans nouveau relais, sans dépendance tierce, et pour une fraction du coût en jetons.
* **Risques du choix recommandé :**
  1. Le modèle `kimi-k3.1-pro` pourrait écrire du code d'analyse exploratoire médiocre sans l'échafaudage de consignes complexes de Sakana v3 (HYPOTHÈSE).
  2. Sur-apprentissage (overfitting) aux épisodes de développement : l'expérimentateur ajuste ses formules au bruit de l'échantillon de développement et soumet des lois qui échouent au test de mort ou dégradent le contrôle de multiplicité (HYPOTHÈSE).
  3. Échec mécanique de l'appel de fonction ou du formatage JSON de sortie après plusieurs tours de boucle sur `kimi-k3.1-pro` (HYPOTHÈSE).
* **Mesure qui départagerait :** Le **taux de vraies découvertes (lues sur l'oracle du monde planté) par dollar dépensé ($V/\$$)**, à budget d'API strictement égal et à **nombre de fiches soumises au juge fixé à $M$ identique pour tous les bras** (pour neutraliser le biais de multiplicité signalé au §4 des faits).
* **Ce qui ferait changer d'avis :**
  1. **Pour abandonner tout expérimentateur et garder « Kimi, meilleur de $N$ » :** Si, à budget égal, le témoin « meilleur de $N$ » (équipé d'un filtre mécanique déterministe sur les épisodes de développement) atteint un $V/\$$ supérieur ou non significativement inférieur à la boucle expérimentale minimale (l'allocation des jetons à la diversité bat l'allocation à la vérification interactive).
  2. **Pour passer à The Agentic Scientist (Sakana v3) :** Si et seulement si la boucle minimale bat le témoin « meilleur de $N$ » (prouvant que l'exécution interactive aide), **et** que l'analyse des traces montre que le goulot d'étranglement résiduel est la complexité du code d'expérimentation (nécessitant un agent de codage multi-fichiers comme `pi`/`opencode`), justifiant alors le coût du relais en flux et de l'enfermement Docker.
  3. **Pour revenir à Kaimen (a) :** Si l'expérience montre que l'exécution de code est inutile, mais que le classement par tournoi Elo interne sans exécution améliore la sélection des $M$ fiches soumises par rapport à un filtre mécanique.

---

## (a) Ce que la question suppose sans que ce soit établi

Chaque présupposé implicite de la question et de la recommandation rapportée est listé ci-dessous avec son statut strict :

1. **Présupposé d'emboîtement (fausse hiérarchie entre (a) et (b)) :** La séquence « ne passer à The Agentic Scientist que si Kaimen bat le témoin » suppose que Kaimen-avec-outil-neuf est une approximation fidèle et plus économique du mécanisme de The Agentic Scientist.
   * *Statut :* **HYPOTHÈSE** (contredite par les faits RAPPORTÉS au §3 : Kaimen `cef5bcf` est un tournoi de réflexion/évolution textuelle sans exécution, tandis que Sakana v3 est un agent de codage itératif avec ablations).
2. **Présupposé de compatibilité technique de Kaimen avec Kimi :** Brancher Kaimen suppose que `kimi-k3.1-pro` supporte de manière fiable le choix d'outil forcé par nom (`tool_choice` nommé) exigé par le superviseur de Kaimen à travers le relais v3.
   * *Statut :* **HYPOTHÈSE** (explicitement signalée comme « non éprouvé sur `kimi-k3.1-pro` » aux §3 et §7 des faits RAPPORTÉS).
3. **Présupposé de survie de Kaimen sans littérature :** La recommandation (a) suppose que Kaimen, amputé de ses outils Web et de recherche bibliographique (seuls outils présents au commit `cef5bcf`, RAPPORTÉ), conserve une logique interne fonctionnelle alors que son critère de nouveauté est défini « relativement à la littérature citée » (RAPPORTÉ).
   * *Statut :* **HYPOTHÈSE**.
4. **Présupposé d'incompatibilité du relais v3 avec Sakana v3 :** Écarter (b) au motif qu'il faut un relais neuf suppose que les agents `pi`, `opencode` ou `gemini` exigent impérativement le mode flux (streaming) et ne peuvent pas être configurés en mode non-flux par simple paramètre.
   * *Statut :* **HYPOTHÈSE** (marqué « non vérifié pour chacun » aux §3 et §7 des faits RAPPORTÉS).
5. **Présupposé de supériorité de la réflexion agentique sur le filtrage mécanique :** Opposer un scientifique coûteux (1,3 à 21 USD estimé, RAPPORTÉ) à un témoin « meilleur de $N$ » suppose qu'un agent qui réfléchit et code pendant 7 à 500 sessions-équivalentes (estimé, RAPPORTÉ) fait un meilleur tri sur les épisodes de développement qu'un script mécanique fixe qui génère $N$ lois indépendantes et ne soumet que les $M$ lois ayant la plus faible erreur prédictive sur ces mêmes épisodes de développement.
   * *Statut :* **HYPOTHÈSE** (point ouvert de méthode au §4 des faits RAPPORTÉS).
6. **Présupposé d'étanchéité de l'isolation de Sakana v3 :** L'option « d'abord The Agentic Scientist, enfermé » suppose qu'un agent conçu pour tourner à pleins droits dans Docker avec réseau `host` (RAPPORTÉ) fonctionnera sans planter ni boucler à l'infini lorsqu'on lui coupera le réseau et l'accès aux gestionnaires de paquets (`pip`, `apt`).
   * *Statut :* **HYPOTHÈSE**.

---

## (b) Expériences décisives en inférence forte (Duels $H_A$ contre $H_B$)

Conformément à R1 et N-045, un **pilote de bruit A/A** (deux exécutions indépendantes du bras témoin sur les mêmes mondes plantés de développement) précède les duels pour mesurer la variance de base $\sigma_0$ du système. Conformément au §4 des faits, **la multiplicité est verrouillée** : chaque bras a exactement le même budget en dollars $B$ et doit soumettre exactement $M$ fiches finales au juge statistique de l'orchestrateur.

### Expérience 1 : Duel d'allocation budgétaire — Filtrage mécanique sur $N$ tirages vs Boucle expérimentale minimale (« Autre chose »)

Cette expérience teste si le concept même d'un proposeur-expérimentateur interactif vaut son coût en jetons face à l'échantillonnage parallèle massif (N-045).
* **Bras 1 (Témoin amélioré, `Témoin-Filtre`) :** Le budget $B$ est dépensé en $N$ appels indépendants au proposeur Kimi standard (sans outil). Chaque fiche produite contient `{enonce, loi_predictive}`. Un script mécanique déterministe de l'orchestrateur évalue la `loi_predictive` de chacune des $N$ fiches sur les épisodes de développement (sans consommer de jetons LLM) et soumet les $M$ fiches ayant le meilleur score d'ajustement empirique.
* **Bras 2 (`Exp-Minimal`) :** Le même budget $B$ est alloué à $K$ sessions ($K < N$) d'une boucle minimale maison sur Kimi : l'agent reçoit les épisodes de développement, peut appeler un unique outil `exec_python` (dans `bwrap`) jusqu'à 5 fois (illustratif) par session pour inspecter les données et tester ses formules, puis soumet ses $M$ meilleures fiches.
* **Hypothèse $H_A$ (Valeur de l'induction interactive) :** L'inspection active des résidus et le débogage itératif sur les épisodes de développement permettent de formuler des lois fonctionnelles que l'échantillonnage aveugle ne trouve pas : `Exp-Minimal` produit plus de vraies découvertes par dollar que `Témoin-Filtre`.
* **Hypothèse $H_B$ (Suffisance de la diversité brute + tri mécanique) :** À budget égal, dépenser les jetons en réflexion multi-tours réduit trop le nombre $N$ d'hypothèses explorées ; l'échantillonnage massif suivi d'un tri mécanique sur les épisodes de développement domine ou égale la boucle interactive.
* **Métrique et seuil :** Différence du taux de vraies découvertes lues sur l'oracle par dollar dépensé, $\Delta(V/\$$) = $(V/\$)_{\text{Exp-Minimal}} - (V/\$)_{\text{Témoin-Filtre}}$, accompagnée du taux de fausses découvertes sur l'oracle ($F/\$$). Seuil de décision préenregistré : $\Delta(V/\$) \ge +20\%$ (illustratif, et supérieur à $2\sigma_0$ du pilote A/A), sans augmentation de $F/\$$ au-delà du seuil de contrôle FDR du juge O2.
* **Contrôle négatif :** Exécution de `Exp-Minimal` où la sortie de l'outil `exec_python` est remplacée par un message constant `{"statut": "ok", "sortie": "aucune anomalie détectée"}` (expérimentateur aveugle qui consomme les jetons de boucle sans information empirique réelle). Doit sous-performer `Témoin-Filtre` à cause de la perte de budget en jetons inutiles.
* **Issues falsificatrices :**
  * Si $\Delta(V/\$) < 0$ ou non significatif (ou si `Exp-Minimal` ne bat pas son contrôle négatif aveugle) $\implies$ **$H_A$ est falsifiée**. Ni Kaimen (a) ni Sakana (b) ne doivent être branchés : le problème n'est pas le cadriciel, mais le fait que l'allocation de jetons à l'interaction dégrade le rendement par dollar.
  * Si $\Delta(V/\$) \ge +20\%$ (illustratif) et bat le contrôle négatif $\implies$ **$H_B$ est falsifiée**. Le rôle d'expérimentateur interactif est validé sur preuve (N-045) ; on passe à l'Expérience 2.

### Expérience 2 : Duel architectural — Boucle minimale (`Exp-Minimal`) vs Tournoi Kaimen modifié (a) vs Agent de code Sakana enfermé (b)

Si et seulement si $H_A$ l'emporte à l'Expérience 1, il faut déterminer si la lourdeur d'un cadriciel tiers (Kaimen ou Sakana) apporte un gain réel par rapport à la boucle minimale maison, à coût apparié.
* **Hypothèse $H_A$ (Gain de l'échafaudage multi-agents/tournoi ou débogage profond) :** L'architecture structurée d'un scientifique du marché — soit par évolution et tournoi Elo (Kaimen, option a), soit par itération d'agents de code complets et ablations (Sakana, option b) — permet de découvrir des lois de complexité supérieure que la boucle minimale (`Exp-Minimal`) manque, compensant son surcoût de 1,3 à 21 USD (estimé, RAPPORTÉ) par génération.
* **Hypothèse $H_B$ (Loi des rendements décroissants / Surcharge de cérémonial) :** Dans un gabarit fermé `{enonce, loi_predictive}` sans littérature ni Web, les phases de tournoi Elo, de méta-revue (Kaimen) ou d'écriture/ablation lourde (Sakana) diluent le budget de jetons dans du cérémonial textuel ; à budget total $B$ fixé, `Exp-Minimal` (qui fait plus de générations courtes) domine (a) et (b).
* **Protocole de coût égal :** Sur un budget total fixe de $B = 25\text{ USD}$ par bras (illustratif), si Sakana (b) coûte 12,5 USD par génération (dans la fourchette de 3,6 à 21 USD estimée, RAPPORTÉ), il a droit à 2 générations ; si Kaimen (a) coûte 5 USD (dans la fourchette 1,3 à 12 USD estimée, RAPPORTÉ), il a droit à 5 générations ; si `Exp-Minimal` coûte 0,50 USD (illustratif), il a droit à 50 générations. Chacun soumet exactement $M$ fiches finales au juge (via un tri mécanique sur les épisodes de développement si le bras produit plus de $M$ candidats).
* **Métrique et seuil :** $(V/\$)$ lu sur l'oracle sur une batterie de mondes plantés de complexité graduée. Seuil : le candidat (a) ou (b) doit battre `Exp-Minimal` d'au moins $+25\%$ sur $(V/\$)$ (illustratif) pour justifier la dette technique de maintenance d'une fourche tierce.
* **Contrôle négatif :** Un monde planté « bruit pur » (aucune loi vraie au-delà du nul des lois connues). Sert à vérifier que l'itération intensive de Sakana (b) ou l'évolution de Kaimen (a) ne fabrique pas d'artefacts sur-ajustés qui passeraient le filtre de développement et encombreraient le quota de $M$ fiches (mesure du taux de fausses promotions soumises).
* **Issues falsificatrices :**
  * Si `Exp-Minimal` $\ge$ (a) et (b) sur $(V/\$)$ $\implies$ **$H_A$ est falsifiée**. Les cadriciels du marché sont rejetés ; l'organisme conserve `Exp-Minimal` en production (v67).
  * Si (a) bat `Exp-Minimal` et (b) $\implies$ **$H_B$ est falsifiée** au profit de la sélection par tournoi Elo.
  * Si (b) bat `Exp-Minimal` et (a) $\implies$ **$H_B$ est falsifiée** au profit de l'itération de code profond (répondant positivement au « pourquoi pas lui ? » de Lazar sur preuve empirique).

---

## (c) Mesure minimale de fonctionnement des instruments nommés

Avant tout duel scientifique (Expériences 1 et 2), chaque instrument technique requis par la question doit passer un **test de porte mécanique et de calibration** (R13) sans toucher aux mondes de la course décisive.

| Instrument nommé dans la question / les faits | Ce qu'il doit détecter ou accomplir | Cas honnêtes appariés (Contrôle de fausses alertes) | Artefacts / Cas hostiles (Contrôle de détection) | Taux exigés (Détection / Fausses alertes) | Vérification mécanique simple à battre |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Juge statistique hors des agents (O2) + Règle de multiplicité ($M$ fiches)** | Détecter les vraies lois plantées tout en contrôlant le taux de fausses découvertes (FDR/FWER) malgré l'optimisation préalable de l'agent sur les épisodes de développement. | $M$ fiches contenant des reformulations algébriques exactes des lois connues (le nul) ou du bruit indépendant généré honnêtement. | $M$ fiches « sur-apprises » (polynômes interpolateurs construits par un script d'attaque pour coller parfaitement aux épisodes de développement mais faux hors échantillon). | **Détection (vraies lois) :** $\ge 80\%$ (illustratif).<br>**Fausses alertes (promotions de lois sur-apprises sous le nul) :** $\le \alpha$ préenregistré (ex. $5\%$, illustratif). | Un simple seuil d'erreur quadratique moyenne (MSE) calculé sur les épisodes de développement (qui aurait $100\%$ de fausses alertes sur les polynômes interpolateurs). |
| **2. Enfermement réseau et système (`bwrap` + pont Unix / Docker sans route) et garde anti-fuite** | Empêcher toute lecture du dépôt public (`lciric/ideation-organism`), du Web, des clés d'API, ou du modèle Claude, tout en laissant passer les appels vers le relais Kimi local. | 50 sessions (illustratif) d'analyse scientifique standard (calculs NumPy/SciPy, lecture des épisodes de développement fournis sur `stdin`, appel au relais via le pont Unix). | 10 scripts d'évasion (illustratif) : requêtes `curl`/`socket` vers IP externe et `127.0.0.1`, lecture de `/proc/environ`, appel d'un modèle `claude-*` au relais, écriture de la chaîne exacte d'une loi plantée publique dans les journaux. | **Blocage / Détection des 10 évasions :** $100\%$ (0 fuite tolérée, échec fermé).<br>**Fausses alertes (blocage de calcul local ou d'appel Kimi valide) :** $0\%$. | Un simple filtre par expression régulière (regex) sur le code source Python généré avant exécution (facilement contourné par `getattr`, `base64` ou appels système indirects). |
| **3. Outil d'exécution neuf (pour Kaimen ou `Exp-Minimal`) sur `kimi-k3.1-pro`** | Permettre à l'agent d'écrire un script de test sur les épisodes de développement, d'en lire la sortie, et d'exclure une hypothèse fausse avant soumission. | 20 problèmes synthétiques (illustratif) où une loi candidate simple est vraie sur les épisodes de développement fournis. | 20 problèmes synthétiques appariés où la loi suggérée dans la consigne viole grossièrement les épisodes de développement (ex. prédit une croissance linéaire sur des données périodiques). | **Détection (rejet de la loi fausse après exécution du script) :** $\ge 90\%$ (illustratif).<br>**Fausses alertes (rejet de la loi vraie à cause d'un crash d'outil ou d'appel forcé mal formé) :** $\le 5\%$ (illustratif). | L'évaluation en zéro-coup (sans outil) par `kimi-k3.1-pro` à qui l'on donne les épisodes de développement en texte brut dans la fenêtre de contexte. |
| **4. Témoin « Kimi, meilleur de $N$ » (avec filtre mécanique de développement)** | Servir de ligne de base à coût égal (N-045) en sélectionnant les $M$ meilleures lois parmi $N$ tirages indépendants. | $N$ tirages indépendants sur un monde planté de démonstration (`temoins-pari-demo-v1.json`, VÉRIFIÉ/RAPPORTÉ). | Injection dans le lot de $N$ tirages de 50% de fiches syntaxiquement invalides ou numériquement divergentes (`NaN`/`Inf`). | **Rejet des fiches divergentes :** $100\%$.<br>**Gain de $(V/\$)$ sur l'oracle par rapport à un tirage aléatoire de $M$ fiches parmi $N$ :** $> 0$ de façon reproductible sur 5 graines (illustratif). | Le tirage au sort aveugle de $M$ fiches parmi les $N$ produites (qui gaspille l'information des épisodes de développement pourtant disponibles gratuitement). |

---

## (d) Ancrage matériel, calcul et devis

Conformément aux contraintes fixées (§2 des faits), **aucun modèle de la famille Claude ni OpenAI n'est utilisé**. Le seul modèle autorisé pour l'expérimentateur et le témoin dans ce plan est le modèle fixé par la barrière du relais : **`kimi-k3.1-pro`** (RAPPORTÉ), avec **`gemini-4-argon`** en vérificateur témoin si l'orchestrateur v66/v67 le maintient (VÉRIFIÉ).

### 1. Coût d'ingénierie préalable et risque de calendrier (Comparaison des options)

* **Option « Autre chose » (`Exp-Minimal` maison) :**
  * *Travail :* 1 script Python autonome ($\sim 150$ lignes, illustratif) lisant `stdin`, appelant le relais v3 existant (sans flux, compatible immédiatement), exécutant les blocs de code dans le `bwrap` existant de l'organisme, et rendant la ligne JSON `{texte, cout_usd, modele_servi, usage}` + le pont `socat`/Unix pour le bac.
  * *Dépendances tierces :* Aucune (bibliothèque standard Python). Risque d'appel d'outil forcé contourné (peut utiliser un simple balisage ou l'appel d'outil standard sans superviseur complexe).
* **Option (a) (Kaimen `cef5bcf`) :**
  * *Travail :* Fourche du dépôt, purge des valeurs Claude par défaut, suppression des outils Web/littérature, câblage de l'outil `code_exec` (actuellement un simple commentaire, RAPPORTÉ), modification du schéma Pydantic des hypothèses pour ajouter `loi_predictive`, réécriture des consignes de nouveauté, adaptateur d'extraction de sa base de données.
* **Option (b) (The Agentic Scientist `df83138`) :**
  * *Travail :* Écriture et audit d'un **relais v4 supportant le flux (streaming)** (car `pi`/`opencode` lisent en flux, RAPPORTÉ/HYPOTHÈSE), construction d'une image Docker hors-ligne sans route réseau, neutralisation des phases d'ablation et de rédaction LaTeX, verrouillage des permissions pour empêcher l'agent de modifier l'évaluateur (incident rapporté au §3).

### 2. Devis de calcul et d'API pour trancher la question

*Rappel des tarifs des faits (tous **estimés**, RAPPORTÉS) : Kimi à 2 USD / M jetons d'entrée et 10 USD / M jetons de sortie. Devis d'une course v66 complète : 1,5 à 2 USD (estimé).*

Pour respecter l'esprit de sobriété du programme (N-045) et obtenir une réponse décisive sans gaspiller le budget dans les 3,6 à 21 USD par génération (estimé) de Sakana v3 dès le départ, le plan financier est étagé en trois portes avec arrêt précoce (montants totaux d'exécution **illustratifs**, calculés à partir des coûts unitaires **estimés** des faits) :

1. **Porte 0 — Validation mécanique des gardes et compatibilité Kimi (Section c) :**
   * Test des 10 artefacts d'évasion réseau/système : 0 USD d'API (tests locaux déterministes).
   * Test de l'outil d'exécution et du choix d'outil forcé sur `kimi-k3.1-pro` (40 appels courts) : **$\sim 0,40\text{ USD}$ (illustratif)**.
2. **Porte 1 — Pilote A/A et Expérience 1 (`Témoin-Filtre` vs `Exp-Minimal` maison) :**
   * Sur 3 mondes plantés de développement, budget apparié de $2,00\text{ USD}$ par bras (comparable au coût d'une course v66 de 1,5 à 2 USD estimé, RAPPORTÉ) :
     * Pilote A/A (2 runs de `Témoin-Filtre`, soit $\sim 40$ sessions de proposeur par run) : **$4,00\text{ USD}$ (illustratif)**.
     * Bras `Exp-Minimal` (1 run à coût égal de $2,00\text{ USD}$, soit $\sim 8\text{ à }10$ sessions de boucle courte de 5 tours) : **$2,00\text{ USD}$ (illustratif)**.
     * Contrôle négatif aveugle de `Exp-Minimal` : **$2,00\text{ USD}$ (illustratif)**.
   * *Sous-total Porte 1 :* **$8,40\text{ USD}$ (illustratif)** (machine négligeable, `bwrap` local sur CPU existant).
   * **Décision d'arrêt à la Porte 1 :** Si `Exp-Minimal` ne bat pas `Témoin-Filtre` de $\ge 20\%$ (illustratif) sur $(V/\$)$, **arrêt immédiat**. On économise tout le développement de Kaimen et de Sakana, et la question du directeur est tranchée empiriquement pour $8,40\text{ USD}$ (illustratif).
3. **Porte 2 (Conditionnelle) — Expérience 2 (`Exp-Minimal` vs Kaimen (a) vs Sakana (b)) :**
   * Uniquement si la Porte 1 est franchie et après un nouveau GO de dépense.
   * Essai court de calibration de coût (1 génération de Kaimen : 1,3 à 12 USD estimé, RAPPORTÉ ; 1 génération de Sakana : 3,6 à 21 USD estimé + 0,45 à 1,1 EUR machine estimé, RAPPORTÉ) : **$\sim 5\text{ à }33\text{ USD}$ (estimé/illustratif)**.
   * Course comparative à budget apparié (ex. 3 générations de Sakana contre l'équivalent en dollars de Kaimen et `Exp-Minimal`) : **$\sim 35\text{ à }90\text{ USD}$ (illustratif)**.

**Conclusion opérationnelle :** Démarrer par `Exp-Minimal` (« autre chose ») permet de répondre rigoureusement à la question pour **$\sim 8,40\text{ USD}$ (illustratif)** sur l'infrastructure v66/v67 existante, sans construire de relais en flux ni d'usine Docker, tout en testant directement l'hypothèse causale qui motive l'idée d'un expérimentateur.

FIN-DE-CELLULE