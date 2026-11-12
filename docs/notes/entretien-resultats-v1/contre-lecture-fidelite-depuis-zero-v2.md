# Contrôle ciblé de fidélité — « Le contrôle boîte blanche des menaces diffuses, expliqué depuis zéro », v2

- **Verdict : fidèle en l'état.** 0 erreur bloquante, 0 majeure, 0 mineure. Un complément facultatif à la tension 26 (section 3).
- Contre-lecteur : le même sous-agent que pour la v1 (Fable 5.2, `claude-fable-5-2`), autre modèle que le rédacteur. Ce n'est donc pas un lecteur neuf de la v2 : c'est le contrôle des corrections demandées par mon rapport `b8b5df18`.
- Document lu : `docs/notes/entretien-resultats-v1/explication-programme-depuis-zero-v2.html`, sha256 recalculé `a382d02d21294e434a5d90296a2b1e7da30eb19b4f31d3369a4886c3d7777a39`, égal à l'attendu ; commit `3ffc820e`. La v1 est intacte (`8c190a57…7dcf`). Aucun des deux documents n'est modifié.
- Date : 10 novembre 2026 (UTC). Non scellé.
- Méthode : texte des deux versions extrait hors balises, comparé par `diff` (37 blocs modifiés ; feuille de style identique) ; chaque bloc relu contre sa source primaire.
- Mêmes interdits que pour la première passe, tenus : ni la branche de quarantaine de la mesure unanime, ni ses sorties, ni le coffre, ni `lecture-sondes-t06.json`, ni les lignes R-604 et R-605.

## 1. Les quinze corrections

| Correction demandée | Faite | Contrôle sur source |
|---|---|---|
| Majeure 1 — section 4.8, théorème en mots simples | oui | Classe C, condition d'échangeabilité, classe K avec les deux signes, maximum à son taux ou en dessous : conforme au texte envoyé l. 75-83, 96-99 et à N-003/N-004 l. 29-36. |
| Majeure 2 — mesure unanime « courue » | oui, partout | En-tête, 3.5, lignes « L et T sur activations », M1, M2 ter et M3, M4, 6.3, 7.1, contradiction 20, glossaire : « lancée », avec « aucune pièce lue n'atteste la fin de la course ». Recherche de « couru » et « a eu lieu » dans la v2 : une seule occurrence, sur la revue de sécurité externe. Un état « lancé » est ajouté à la légende du registre. Aucun résultat. |
| Majeure 3 — exemple chiffré 2 | oui | 0,1591 est bien la valeur terminale du pari, s* = 39,1146 (préenr. T0.3 l. 121, 129). Calcul refait : Φ̄(1,645 − 25/√200) = 0,5489 ; Φ̄((39,1146 − 25)/√200) = 0,1591. Le renvoi l. 219 (« prix de la garantie en P3 ») est exact. |
| Majeure 4 — sections 1.5 et 4.8 « Tr » | oui | La nuance suit le texte envoyé l. 147-149 (une étude ; difficulté d'optimisation possible ; prémisse affaiblie par d'autres travaux). La phrase du programme v2 l. 13 est gardée et datée. |
| Mineure 1 — renvoi du pari (1.7) | oui | Pari à λ fixe dit d'illustration ; mélange normal l. 121, 233 ; détecteur e l. 232, remise du capital à 1 conforme à log M_n = max(log M_{n−1}, 0) + … |
| Mineure 2 — figure 2 | oui | « quatre réarrangements (sept cellules) » : préenr. l. 136-142. |
| Mineure 3 — H8 | oui | « et non plus une bascule » ; N-062 l. 22, 25, 26. Repris en contradiction 6. |
| Mineure 4 — oracle de couverture | oui | « décidé dans son principe, ni conçu en détail ni construit » : entretien v18 l. 113, 432-433. |
| Mineure 5 — règle de décision de G1 | oui | Section 2.4, section 7.3, contradiction 7, glossaire : N-055 l. 29 ; brouillon 4 de G1 l. 59 ; la confirmation du 28 octobre est rattachée à l'expérience de lecture de N-054 point 4 (N-056 l. 47-51). |
| Mineure 6 — citation de R-888 | oui | Verbatim égal à `registres/decisions.md` l. 1117. |
| Mineure 7 — Panin | oui | Registre HC1, section 7.2, tension 26 : dépôt du 20 octobre (`provenance-voisin-panin-v1.md` l. 3) ; lecture en brouillon non contre-lue (`lecture-voisin-panin-v1-brouillon.md` l. 3-4). |
| Mineure 8 — invariants | oui | Trafic de couverture (ablaté au papier B) et hygiène de l'état persistant : texte envoyé l. 253-254. |
| Mineure 9 — « dose-réponse » | oui | Brief v2 l. 163, 210 pour « proportion d'actions sabotées × intensité » ; texte envoyé l. 279 et N-063 v2 l. 14 pour l'adaptateur. La glose de la v1 avait donc une source, que je n'avais pas trouvée. |
| Mineure 10 — prédiction du brief | oui | Section 3.5, ligne « L et T sur activations », tension 27. |
| Mineure 11 — L2 et T4 | oui | P2.1, P2.2, P2.3 décrites séparément ; P7.1 à P7.3, l. 193-201. |

Aucune de ces corrections n'introduit d'erreur neuve.

## 2. Les deux tensions ajoutées

**Tension 27 — réelle, correctement sourcée.** Brief v2 l. 140 et l. 227 : « la somme cumulée échoue ; un agrégateur d'autocorrélation […] récupère le signal ». N-003/N-004 l. 33-36 : en classe K la somme passe au-dessus de son taux sous dépendance positive. Préenr. T0.3 l. 366 : la phrase du brief est lue « inexact en classe K : la somme n'est pas aveugle ». Mesure unanime v15 l. 167 : M4 est écrite selon N-003.

**Tension 26 — réelle, correctement sourcée, à compléter si l'on veut.** Ce que le document dit est exact :
- le texte envoyé cite le résultat le 7 octobre (l. 181-183) et dit ses descriptions fondées sur des rapports de vérification à la page (l. 400) ;
- la recherche affirmative du 6 octobre décrit Panin « sans le PDF », à partir d'extraits (`docs/sources/recherche-affirmative-20261006/rapport-papiers-C-B-v1.md` l. 61-63), et ses lignes 64-75 ne contiennent pas le résultat ;
- le PDF est déposé le 20 octobre ; la lecture du 20 octobre est un brouillon non contre-lu, et elle ne contient pas non plus le résultat.

Ma propre recherche de provenance, dans les fichiers hors des interdits :
- **Le chiffre est exact sur le PDF.** `docs/sources/pdf/ssrn-7424179-panin-2026-v1.pdf` (`27f88ed7…`), lu par `pdftotext -layout` : « the outcome is near-binary in three of five models » en page 1 (résumé) ; la même affirmation revient pages 2, 3, 6 et 12.
- **Une pièce du dépôt le cite avec ses pages** : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` l. 246-248 (« poids quasi binaire chez trois modèles sur cinq », p. 1 à 4, 6, 11 et 12) et l. 340 (p. 6). Elle renvoie à une « note finale `8781d6a7…` » de lecture de Panin, que je n'ai pas trouvée sur cette branche (seul le brouillon est sous `docs/notes/`).
- **Rien d'antérieur au 7 octobre ne le porte.** Le registre dit encore le 17 octobre « Panin identifié, PDF attendu de Lazar » (R-193, `registres/decisions.md` l. 330). La phrase envoyée précède donc de treize jours toute pièce du dépôt qui la vérifie. D'où elle vient le 7 octobre reste non établi : seul Lazar peut le dire.

La tension porte donc sur la **provenance et la date de la vérification**, pas sur l'exactitude du chiffre. Le document ne dit pas le contraire, mais un lecteur pourrait le comprendre ainsi.

## 3. Complément facultatif (pas une erreur)

Dans la tension 26 et dans « Ce que ce document n'a pas pu vérifier », ajouter : « le chiffre lui-même se lit sur le PDF déposé le 20 octobre (p. 1, 2, 3, 6, 12) et il est repris, pages citées, par le brouillon 5 du préenregistrement du papier C (l. 246-248, 340) ; ce qui manque est une pièce datée d'avant l'envoi ». La mention « non retrouvée » de la liste finale serait alors « non retrouvée avant le 7 octobre ».

## 4. Le reste du `diff`

Rien d'autre n'a changé de façon fautive.
- En-tête : version, ligne de statut, mention « aucune pièce lue n'atteste la fin de la course ».
- Partie 8 : « 27 en tout » ; le compte est juste.
- Table des sources : quatre lignes ajoutées (ma contre-lecture de la v1, provenance de Panin, lecture du voisin Panin, recherche affirmative du 6 octobre). Les quatre empreintes recalculées sont conformes, et les mentions de compagnon sont exactes.
- Liste finale : les numéros des deux lignes du registre qui nomment des candidats sont retirés ; recherche de « R-604 » et « R-605 » dans la v2 : aucune occurrence.
- Interdits de contenu : aucune violation. Aucun résultat de la mesure unanime, rien du coffre, aucun nom de mode tenu à l'écart ni de candidat, aucun chiffre de course exploratoire.

## 5. Limites de ce contrôle

- Je n'ai relu que les 37 blocs modifiés et leurs sources ; le reste de la v2 est identique à la v1, déjà contre-lue.
- La phrase de statut « la version 1 est celle qui a passé le questionnaire commun » n'est pas vérifiée.
- La « note finale `8781d6a7…` » sur Panin n'a pas été retrouvée : recherche par empreinte sous `docs/notes`, `docs/sources`, `docs/etat-de-l-art` et dans le registre, non exhaustive.
