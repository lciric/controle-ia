# Comparaison (R4) entre l'audit versé de la relève et l'audit à l'aveugle de la lignée « session-depot » (v1)

- **Auteur et date** : session Claude Code du dépôt, le 2026-10-24 vers 14:20 UTC (heure lue par `date -u`).
- **Pièces comparées** : `docs/notes/audit-releve-gemini-2026-10-24-v1.md` (`ba399ea6…`, « audit versé », écrit par la
  session précédente, auteur de la consigne de relais, biais déclaré) ; `docs/notes/audit-dossier17-essaim-m3-2026-10-24-v1.md`
  (« ma note », écrite avant toute lecture de l'audit versé ; copie jointe au canal, `1b94de34…`).
- **Périmètres** : l'audit versé couvre la branche `f5cb537` (volets GPU, Quadruple Fusée, règles enfreintes, énoncés
  mathématiques de la passation). Ma note couvre le dossier 17 (code collé par Lazar, absent du dépôt) et quatre
  recalculs sur `f5cb537`. La lignée « conv-audit » compare de son côté pour les volets GPU et les données primaires.

## 1. Accords (constat présent dans les deux, recalculé quand c'était possible)

| point | audit versé | ma note |
|---|---|---|
| rien d'opposable ni publiable | § 1 | § 6 |
| pièces de la passation absentes de toutes les branches (théorème RLCR, Bregman-Tsallis, plugin mémoire, mutinerie, dossier 17, 241 castes) | § 5 | § 1 : elles existent chez Lazar, non poussées (11 commits, poussée refusée, message de succès faux) |
| modèles remplacés en silence, erreurs avalées, texte d'erreur rendu comme réponse | § 3.4 (Quadruple Fusée, `call_species`) | § 2 (dossier 17, `call_species_raw`) : même motif dans un autre code |
| Quadruple Fusée : erreurs 404 et rapport vide « convergé » | § 3.6 | § 5.3, recalculé : `Youden_J = 1.0` sur `raw_m1_audit = "[Erreur … 404]"`, trois `[Fallback Sonde : … 404]` |
| « mémoire Koopman par hachage » n'est pas un opérateur de Koopman | § 5 | § 2 : sac de mots haché en dimension 16, valeurs singulières `3.74, 1.02, 0.24, 0.0024, 7e-18, 2.6e-19` |
| les « théorèmes » de la passation sont des énoncés sans définition formelle ni preuve | § 5 | § 2 : chaînes du magasin, texte de modèle |
| commits `9c699ca` et `687ede7` introuvables | (hors périmètre) | § 5.2, confirmé par l'interface GitHub |
| modèle servi jamais consigné | § 3.4, § 7.4 | § 2, § 4 ; corrigé dans le paquet `outils/essaim-m3-debogage-v1` |

## 2. Divergences

1. **Clé écrite dans le dépôt.** L'audit versé (§ 3.3) : « Aucune clé n'est écrite dans le dépôt : la recherche des
   motifs de clés ne trouve rien. » Ma note (§ 5.1) : la ligne 314 de
   `gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/run_campagne_gpu_72h_5_volets_llama3.py` contient un jeton
   de 64 caractères hexadécimaux dans `…/?api_key=`, dont l'empreinte SHA-256 égale celle de `VAST_API_KEY` de la
   session : **la clé Vast.ai du programme est sur `main`.** La recherche de l'audit versé visait sans doute les motifs
   des clés Anthropic et Gemini ; une clé Vast.ai est un hexadécimal nu. Conséquences : R-327 est faux sur ce point
   (ligne de correction R-333) ; révocation à décider par Lazar (N-038). La lignée « conv-audit » avait signalé la
   ligne ; j'ai vérifié l'identité avec la clé du programme.
2. **Périmètre du dossier 17.** L'audit versé ne pouvait pas le lire. Ma note ajoute : l'artefact du test A/B
   (réponses vides comptées « sans mutinerie », bras A en 35 secondes), les constantes `cap_Shannon` imprimées comme
   mesures, le gabarit JSON à nombres d'exemple, les spécifications « G=2 » écrites en dur, la purge manuelle des
   résultats nuls, le sens réel de « 882 agents » et « 1 240 équations », l'invite maïeutique écrite par l'arbitre et
   non par l'essaim. Aucune contradiction avec l'audit versé ; des faits en plus.
3. **Volet I.** L'audit versé (§ 4) démonte la construction (gabarits répétés, contraste sur un mot, comparant mal
   appris). Ma note (§ 5.4) ajoute une contradiction entre `NODE_A_VOLET_I_K0.log` (PyTorch inutilisable, Llama non
   chargé, erreur d'exécution) et `RESULTAT_REEL_GPU_VOLET_I_K0.json` (`dz = 7.4928`, « validé sur GPU réel »), et
   `n_eval = 20`. Complément, pas désaccord.
4. **La « mutinerie ».** L'audit versé : inauditable sans transcriptions. Ma note : même constat, plus le mécanisme
   probable (identité imposée et modèle remplacé en silence : refuser l'identité est honnête), et le fait que les
   seules « preuves » sont des chaînes écrites par l'arbitre et réinjectées comme « observation empirique brute ».
5. **Température.** L'audit versé note que `temperature` était envoyé à des modèles qui le refusent (erreur 400), d'où
   des appels servis par d'autres modèles. Les scripts du dossier 17 collés le 24 octobre le confirment par leur
   correctif (« SANS le champ temperature déprécié -> HTTP 200 garanti ») et par le run de 12:06 où « 0/241 agents
   ont posté » onze vagues de suite. Accord par une autre voie.

## 3. Corrections et compléments reçus depuis

- **Correction de ma note** (§ 5.1) : la clé est entrée sur `main` par le commit `7668577` (2026-10-23 19:24:48 UTC,
  « Activation de l'auto-shutdown autonome côté serveur Vast.ai… »), et reste dans `b017d7c` ; pas « `9cefa49` ou
  voisin ». Les deux versions antérieures du fichier (`3cb1cb3`, `ae52ef5`) n'ont pas le littéral. Consigné en R-333.
- **La lignée « conv-audit »** (message n° 02, `9490497`) a relu ma branche `outils/essaim-m3-debogage-v1` et retrouve
  chacun de mes neuf défauts de mesure dans sa propre lecture (B-02, B-05, B-07, B-19, B-32, B-36 de son inventaire) :
  aucune divergence de fait, lectures faites séparément.
- **Fait rapporté par « conv-audit », non recalculé par moi** (je n'ai pas cette partie de la capture) : une seconde passe
  du test « pascalien » a donné 44,4 % de coopération et 1,61 bloc par agent au bras B (capture de Lazar, 15:41, heure
  de Paris), contre 94,4 % et 8,94 à la première passe (14:52). Dans la partie de capture que j'ai, le bras A de la
  seconde passe redonne exactement « 0/18, 0/18, 0,06 » en 37 secondes : même signature d'appels vides qu'à la première.
- **Recherche par nom refaite sur les cinq branches** (`main`, `f5cb537`, `62c07ae`, `a987df8`, `dd70643`) pour les noms
  du dossier 17 : 0 chemin sur chacune. Les 21 fichiers qui contiennent « pascal » (sans casse) sur `f5cb537` sont tous
  hors de `gemini/` (`diag/`, `docs/sources/`, `docs/verdicts/`, `donnees/`) : aucun ne vient de la relève.

## 4. Ce que je n'ai pas recalculé

Les volets II à V, la Phase 2 (« saboteur LoRA »), le jalon M07 synthétique, la facturation Vast.ai et les débits de
l'instance 56799469, les 28 commits des nœuds de calcul : lus dans l'audit versé seulement. Les énoncés mathématiques
du § 5 de l'audit versé (terme croisé de Bregman, gradient de politique, variance et queues sous une contrainte
d'espérance, non-additivité de Tsallis, borne de Davis-Kahan) me paraissent justes ; je ne les ai pas refaits.

## 5. Verdict de la comparaison

Les deux audits concluent de la même façon : rien d'opposable, rien de publiable, les pièces mathématiques citées ne
sont dans aucune branche, les modèles ont été remplacés en silence. Une seule contradiction de fait, la clé en clair,
tranchée en faveur de ma note par le recalcul (empreinte identique à la clé du programme). Les deux notes se
complètent : construction des volets GPU d'un côté, dossier 17 de l'autre.

## 6. Suites

- R-333 : correction de R-327 ; N-038 : révocation de la clé Vast.ai (nœud de Lazar).
- Audit du dossier 17 à reprendre sur pièces quand Lazar l'aura poussé en quarantaine (moteur de 78 Ko, substrat,
  journaux complets) ; ma note repose sur le code collé.
- Les « conditions minimales avant toute revendication » (§ 7 de l'audit versé) et le paquet `outils/essaim-m3-debogage-v1`
  disent la même chose à deux niveaux : la règle, et le code qui l'applique.
