# Traitement de la contre-lecture 1 de la procédure d'extraction de T0.5 (brouillon 3)

Rapport : `rapport-contre-lecture-1-v1.md` (même dossier). Verdict : « scellable après corrections ». Toutes les remarques sont acceptées, sauf deux parties déclinées (CL-8 et CL-25), dites ci-dessous. Texte final : `docs/procedures/T0.5-extraction-v1.md` ; code : `src/controle_ia/environnements/extraction.py` et `extraire_t05.py` ; tests : `tests/test_extraire_t05.py`.

| remarque | gravité | traitement |
|---|---|---|
| CL-1 | bloquante | Acceptée. Tout caractère de contrôle autre que le saut de ligne, et tout saut de ligne dans une formule $…$, est une anomalie dans toute chaîne des sorties et des avis (codes `texte.controle`, `texte.formule`), au module comme aux deux scripts. Consignes : les barres obliques inverses s'écrivent doublées. Tests d'accord : « \theta », « \nabla », « \beta ». |
| CL-2 | majeure | Acceptée. Après sa première ronde, un rôle ne se refait que sur des papiers nommés encore sans avis lisible ; un avis illisible est consigné et ne compte pas. Test d'un avis refait jusqu'à l'assemblage. |
| CL-3 | majeure | Acceptée. Audit calculé par le code des deux côtés (`papiers_d_audit`) : côté propre, les 4 premiers de l'échantillon ; côté sale, les 4 premiers en échec. Tout échec à l'audit (côté propre) rend la reprise due ; réserve inscrite au bilan et portée à Lazar ; accord rapporté. Tests des deux côtés. |
| CL-4 | majeure | Acceptée. Rondes numérotées par le code ; ronde préparée et non lue, ou lue sans préparation : arrêt. Tests. |
| CL-5 | majeure | Acceptée. Toutes les entrées du dossier empreintées ; une entrée modifiée est une anomalie du seul papier (`entrees.modifiees`), sans arrêt global ; aucune restauration ; consignes : « do not modify any file other than … ». Test (script de contrôle modifié par un sous-agent). |
| CL-6 | majeure | Acceptée. Fait déclaré (les sous-agents reçoivent `CLAUDE.md`) ; phrase de préséance ajoutée à l'invite fixe. Le lancement hors de la session n'est pas proposé : sans moyen de lancer des sous-agents ailleurs. |
| CL-7 | majeure | Acceptée. Les 62 gardes des deux modules sont éprouvées par un test d'artefact (relevé par traçage des lignes exécutées : 0 garde non exercée) ; deux gardes finales isolées (`exiger_copie`, `exiger_disjointes`) pour être éprouvées ; une garde inatteignable retirée (papier sans tentative valide). |
| CL-8 | majeure | Acceptée, sauf un point. Modules de décision empreintés au manifeste et contrôlés à chaque étape ; commit et propreté consignés dans chaque résultat. **Déclinée** : l'identifiant du modèle des sous-agents n'est pas écrit dans le dépôt (consigne de la plateforme d'exécution de la session : aucun identifiant de modèle dans un fichier poussé) ; les sous-agents, lancés sans choix de modèle, sont supposés servis par le modèle de la session ; un repli de la plateforme n'est pas observable depuis la session (formulation reprise après la contre-lecture 2, D-14). |
| CL-9 | majeure | Acceptée. Invite : contrôles nécessaires à tout plan sain pour ce problème, pas l'ablation d'un composant propre à la méthode du papier ; le contre-vérificateur juge aussi la conformité à la définition de la famille. |
| CL-10 | majeure | Acceptée. Motif 2 restreint aux erreurs qui changent une décision (« theory_only », ou deux crans) ; taux attendus et probabilités d'arrêt écrits (section 6). |
| CL-11 | majeure | Acceptée. Archives scellées à chaque validation et à chaque lecture ; l'assemblage lit les archives ; résultats committés et poussés à chaque étape. Persistance des archives hors du dépôt : liée à N-014. |
| CL-12 | mineure | Acceptée. Gardes avant le manifeste ; tentatives 2 et 3 limitées exactement aux papiers dus, tous à la fois ; seuil contrôlé dès la lecture de l'échantillon ; ordre des étapes écrit (section 7). |
| CL-13 | mineure | Acceptée. Retours obligatoires (dernière ligne, lancements) ; « OK » face à une anomalie : arrêt ; relance d'un sous-agent en panne dans la même tentative, comptée. |
| CL-14 | mineure | Acceptée. Identifiant chaîne non vide ; nombre positif sans dépassement ; statuts exactement égaux au pilote et à la réserve. |
| CL-15 | mineure | Acceptée. Plus aucune ligne coupée (CL-20) : la copie est le texte au caractère près ; codes d'erreur stables, comparés en liste ; cas de typographie, de barres obliques et de plantage ajoutés. |
| CL-16 | mineure | Acceptée. Bilan : désaccords de classification et de type de données, domaines, calcul, alertes, références de coût par base, citations de tableau ; bilans d'arrêt scellés (seuil, réserve épuisée). |
| CL-17 | mineure | Acceptée (texte, sections 1, 3, 5). « Ancré » remplacé par « retrouvée » (mécanique) et « fondée » (jugement). |
| CL-18 | mineure | Acceptée (section 0). |
| CL-19 | mineure | Acceptée. Essai à blanc scellé (`essai-a-blanc-copie-de-lecture-v1.json`) et déclaré. |
| CL-20 | mineure | Acceptée. Parties de 25 000 caractères au plus, sans coupe de lignes. |
| CL-21 | mineure | Acceptée. Même périmètre pour les deux bases ; comparaison renvoyée au préenregistrement du pilote. |
| CL-22 | mineure | Acceptée (invite). |
| CL-23 | mineure | Acceptée, portée à Lazar : nœud N-014. En attendant, rangement hors du dépôt de ce qui porte du texte des papiers (section 8). |
| CL-24 | mineure | Acceptée (consigne de l'extracteur). |
| CL-25 | mineure | Acceptée en partie. Chaque exclusion « theory_only » est contre-vérifiée (rôle « theorie ») ; intervalle exact du taux d'échec inscrit au bilan. **Déclinée** : contre-vérifier les 96 papiers (écart à « sur échantillon » de P-006, coût). La fuite mécanique (CL-26) s'applique aux 96 papiers, mais ne couvre que la reprise mot pour mot, sur 8 mots, des citations des directions fécondes ; elle ne remplace pas une contre-vérification (formulation reprise après la contre-lecture 2, D-15). |
| CL-26 | suggestion | Acceptée, en anomalie bloquante (`h9.fuite_citation`), au module comme au script. |
| CL-27 | suggestion | Acceptée. U+2010 à U+2012 et U+2212 ramenés à « - », U+00AD retiré ; clés de H.10 à tiret bas échappé acceptées. |
| CL-28 | suggestion | Acceptée (section 0 : déclaration ; version de numpy au manifeste). |
| CL-29 | suggestion | Acceptée (description neutre ; discipline de la session ; commits à chaque étape). |
| CL-30 | suggestion | Acceptée. Part des citations tirées seulement de lignes de tableau, au bilan. |
