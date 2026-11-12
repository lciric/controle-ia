# Consigne : rédiger le brouillon 10 de P3-bis (accord texte ↔ code v2 et chaîne de session, GO prolongé) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 vers 07:10 UTC (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **rédacteur neuf** (Opus), qui n'a écrit ni P3-bis (brouillons 1 à 9), ni son code (v1, v2), ni sa chaîne de session, ni leurs contre-lectures, ni T0.6, ni T0.7 ; ni lecteur exploratoire de 7a (R-2041), ni auditeur de l'écart DT-4 (R-2057). Il ne lit de T0.7 que ce que la section « Concordance » de P3-bis exige (format du journal des ouvertures) ; il est alors exclu ensuite de tout rôle de lecteur de P3-bis.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense, aucune écriture git.

## À lire

- `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon9.md` (`eb65773f…`) et ses contre-lectures 2 et 3 ; décision `docs/decisions/decision-N-066-v1.md`.
- Contre-lecture du code : `brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md` (`7a074ad1…`, CP-01 à CP-17, point 5 « à porter au texte ») ; compte rendu du code v2 : `…/compte-rendu-developpeur-code-p3bis-v2.md` (`f6c93bc5…`) ; sortie de l'essai de fermeture v2 : `…/essai-fermeture-p3bis-v2-sortie-v1.txt` (`06e84ff7…`) ; rapport du lanceur : `docs/procedures/P3-bis-temoin-positif-v1/rapport-developpeur-lanceur-p3bis-v1.md` (`748568cb…`, dix-neuf écarts, contenu de `<<CHAINE_P3BIS>>`) ; noms : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/noms-communs-p3bis-v2.md`. Un rapport complémentaire du lanceur (bancs rejoués contre le code réel) arrivera : écris avec des marqueurs ce qui en dépend.
- Registre `registres/decisions.md` R-2076, R-2077 (GO-2026-11-10-02, échéance 23 novembre), R-2084, R-2085 ; `registres/go.md` lignes GO-2026-11-02-29 et GO-2026-11-10-02.

## Mandat

Révision par **couples** appliqués par script (comme aux brouillons précédents). Contenu :
1. **GO et calendrier** : ligne `GO-2026-11-10-02` (prolongation de GO-29, 80 USD non cumulés, échéance 2026-11-23) lue par la chaîne, `GO_ID` de la ligne « Lancement », création au plus tard le 23 novembre ; **la course doit finir avant le rendez-vous** (2026-11-20T12:00:00Z, date proposée, défaut le 11 vers 16:03 UTC) : l'écrire comme borne de création.
2. **Code v2** : noms v2 (`ouverture_p3bis_v2.py`, `essai_fermeture_p3bis_v2.py`, `p3bis_instance_v2.sh`, `amorce_instance_p3bis_v2.sh`, `essais-cibles-p3bis-v2.txt`) ; trois décisions du rendez-vous et modes `pleine`, `reduite`, `pleine-anticipee` (CP-01) ; journal au format exact (CP-02 ; **vérifie la concordance avec le lecteur de T0.7**, brouillon 19, section « Module », lignes du journal de P3-bis) ; règle de l'essai différentiel (CP-03) ; 8 octets de longueur (CP-04) ; durées (CP-05) ; points au texte (CP-13 : sorties en clair de la classe 1 ; écarts 3, 4, 5, 7, 9, 10 du développeur v1 ; taille du second paquet ≈ 47,7 Mo hors fichier complet des sondes de P3) ; codes de refus choisis par le développeur v2 ; **réserve CP-15** (la liste v2 garde l'essai v1 qui importe un module de T0.7 ; liste gardée par décision de la mère, R-2085).
3. **Chaîne de session** : les dix-neuf écarts du lanceur ; **écart 19** écrit comme nœud de Lazar (une relance après une instance gardée ou arrêtée demande la destruction par l'identifiant ou un lanceur neuf) ; formes de citation exigées (écart 12) ; fichier des longueurs attendues (écart 13).
4. **Marqueurs** : remplir `ESSAI_FERMETURE_P3BIS` (sortie `06e84ff7…` au commit du code `02217f1c`, forme exigée par la chaîne), et ceux que les pièces permettent ; garder les autres (`COMMIT_CODE_P3BIS`, `EMPREINTES_CODE_P3BIS`, `IDENTITE_CODE_P3BIS`, `TESTS_ATTENDUS_P3BIS` à recompter sous Python 3.11, `CHAINE_P3BIS`, `LONGUEURS_P3BIS`, `EMPREINTE_CONFIG_P3BIS`, `EMPREINTE_CONSIGNES_P3BIS`, `PIECES_SUR_MAIN_P3BIS`, `CONTRE_LECTURE_4_P3BIS`), une occurrence chacun si possible.
5. **Sections gelées** : tout couple qui les touche est déclaré un par un ; aucune hypothèse, prédiction, signe ni seuil ne change ; sinon arrêt et signal à la mère.
6. En-tête : statut et titre « brouillon 10 » (vérifie-les).

## Sorties

`brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md`, couples, script, journal, tous scellés. Contrôle par `controle_ia.prereg.problemes`. Réponse courte : chemins, empreintes, couples dans des sections gelées, marqueurs restants, points ouverts.
