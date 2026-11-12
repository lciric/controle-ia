# Consigne : T0.7 sondes v0, brouillon 18 (marqueurs remplissables, écart DT-4 déclaré) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un **rédacteur neuf**, qui n'a écrit ni les brouillons 1 à 17 de T0.7, ni leurs contre-lectures, ni le module `src/controle_ia/t07/`, ni T0.6, ni P3-bis, ni (ii-b), et n'est pas le lecteur exploratoire de 7a.

Dépôt : `/home/user/controle-ia-travail` (`main` local à `445a1e5d` ou plus loin). `PYTHONPATH=src`. Python : `.venv/bin/python`.

## Interdits (ceux de `interdits-communs-v1.md`, même dossier, en entier)

Fichiers et branches sous embargo jamais ouverts (`diag/*/lecture-sondes-t06.json`, nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et `runs/` de 7a et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; étiqueteur) ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucune valeur de clé, jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ; git en lecture seule (autres commits par `git show` ; `git archive` vers un dossier temporaire hors du dépôt permis) ; rien écrit hors des sorties ci-dessous ; ne pas toucher `/home/user/integ-t06` ; refus de contrôle ou de classifieur : arrêt et rapport tel quel ; heures par `date -u`. **Aucun nombre tiré d'une sonde de 7a** ne doit entrer dans le texte : 7a n'a été lue que par la lecture A (exploratoire, non opposable, sans sonde) ; la lecture B est en quarantaine (R-2041, R-2048).

## Pièces

- `brouillons/T0.7-sondes-v0-v1-brouillon17.md` (`65efe32f…`, vérifier d'abord) et ses pièces ; ses deux contre-lectures (brouillons 15 et 16) ; `registres/decisions.md` R-2001 à la dernière ligne pour l'état (notamment R-2021, R-2029, R-2036, R-2041, R-2048, R-2057, R-2062 à R-2068) ; décisions N-063 v2, N-066, P-064 et P-065 (`docs/decisions/`).
- T0.6 à sceller : `brouillons/T0.6-organismes-v0-v1-candidat12-r5.md` (`8fde62db…`) ; voie B (R-2062, R-2064) : le code joué par 7b est l'arbre gelé de `1609a4bf`.
- Audit DT-4 : `docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-v1.md` (`4882fe4d…`) et complément (`cae6ab64…`).
- Module `src/controle_ia/t07/` sur `main`.

## Travail

1. Écrire `brouillons/T0.7-sondes-v0-v1-brouillon18.md` (nouveau fichier, R12) à partir du brouillon 17, par couples appliqués par script (chaque « ancien » une fois), journalisés.
2. **Écart DT-4** (R-2048) : remplacer toute affirmation du type « 7a jamais lue par une sonde » par la déclaration exacte : la chaîne de 7a a calculé des sondes sur l'instance ; le lecteur exploratoire de 7a en a vu des valeurs par accident (R-2041) ; il est exclu de T0.6, T0.7, P3-bis et G0 ; sa lecture B est en quarantaine ; audit et complément : « aucune trace trouvée » ; l'extracteur `extraire_mesures_epreuve_t06_v1.py` ouvre le fichier des sondes et reste interdit jusqu'au verdict de P3-bis ; aucune lecture de T0.7 ne porte sur les sondes de 7a.
3. **Marqueurs** : remplir ceux qui peuvent l'être maintenant, avec leur source : `COMMIT_CODE_T06` = `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` et `EMPREINTES_CODE_T06` = celles de T0.6 r5 (vérifier au commit `1609a4bf`) ; `LECTURES_7A_T07` (ce que 7a a donné et ce qui en est lu : lecture A seulement, écart DT-4 déclaré) ; `CONTROLE_AIRE_T06` et `NIVEAU_BASE_T06` d'après le texte de T0.6 r5 (définition de l'aire, niveau de l'intervalle de la base) — si r5 ne les fixe pas, le dire et proposer ; `CLES_REGISTRE_PARTAGE` (liste fixée des marques des autres tâches, d'après les règles du brouillon 17) ; `COMMIT_CODE_T07`, `EMPREINTES_CODE_T07`, `EMPREINTE_CONFIG_T07` d'après `main` (le module et la configuration de T0.7 tels qu'ils sont ; si une configuration manque, le dire). **Laisser** : `EMPREINTE_PREREG_T06` (après le scellement de T0.6), `MOT_LAZAR_P064` et `MOT_LAZAR_P065` (mot de Lazar ou défaut, le 10 novembre vers 17:13 UTC), `GO_ETAPE_A_T07` (ligne de GO de l'étape A à demander à Lazar ; écrire au rapport le devis que le texte fixe pour cette étape), `ENTROPIE_T07` (tirée au scellement par la mère, R9).
4. Ligne `GARDE-ADAPTEE-T07-P3BIS` (N-066) : vérifier que le texte dit où et quand elle est inscrite au scellement.
5. Vérifier `controle_ia.prereg.problemes` (seuls les marqueurs laissés ; à valeurs factices, liste vide) ; sections gelées : dire lesquelles tes couples touchent (idéalement aucune) et pourquoi.

## Sorties

`brouillons/T0.7-sondes-v0-v1-brouillon18.md`, journal `…-brouillon18-journal-v1.md`, couples `…-brouillon18-couples-v1.json`, script ; compagnons `.sha256`. Rien committé. Réponse courte à la mère : fichiers et empreintes, marqueurs remplis et laissés, devis de l'étape A, points ouverts pour la contre-lecture (qui sera faite par un autre modèle).
