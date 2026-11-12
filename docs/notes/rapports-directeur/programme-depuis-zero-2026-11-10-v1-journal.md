# Journal — « Le programme expliqué depuis zéro » — v1

Rédacteur neuf (sous-agent de la session mère, Claude Opus 5.5), qui n'a écrit ni le programme, ni ses décisions, ni le rapport court du jour, ni le socle de preuves. Journal écrit à partir de 2026-11-10 09:51:01 UTC (relevé `date -u`). Début du travail : 09:40:48 UTC (relevé `date -u` à la création du dossier temporaire).

## Consignes vérifiées avant lecture
- consigne-document-de-zero-v1.md : d7a37a10511350f03472858c94a3552db07beb0ada261f9d4acdeb812952877a (conforme)
- interdits-communs-v2.md : 1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f (conforme), tenus en entier, règle 9 comprise : aucune recherche récursive hors `git grep` sur un fichier nommé ; aucun fichier interdit ouvert ; aucun appel externe, aucune dépense, aucune écriture git.

## Déclaration de rôle
J'ai lu `brouillons/T0.7-sondes-v0-v1-brouillon20.md` (sections Hypothèse et Prédiction seulement) : je suis exclu de tout rôle de lecteur de P3-bis. J'ai lu aussi le brouillon 10 de P3-bis (sections 0 à Seuil, Critères de lecture gelés, Devis).

## Sources lues, empreintes (sha256 complets)
```
2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c  docs/programme-controle-ia-v2.md
9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2  docs/brief-claude-code-programme-complet-v2.md
dfe4fe0fc4d025011bbe0f330fd591b1898dc7e767384e96c946b6388ad81cd0  docs/notes/note-mathematique-lemme-theoreme-v3.md
012ddc44baca981620ff2a81211998fd437f6b336436d33406b119227c406628  docs/decisions/proposition-P-066-saboteur-diffus-par-construction-v1.md
9ab618edae17e757ab83d5de7a346ebf08bebf89aef61e4337cb5c067e5fd545  docs/notes/resultats-T0.3-v1.md
d69a8700fcce69a5405ae9d3cdbcd51a9f541726a9e3e67dc0b76bb0b86f2c20  docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md
f557402b90d1fea33e669295fdeecd835477b3244ca4ebdc256787a44c6071b8  docs/verdicts/audit-R4-T0.5-pilote-v1.md
0c8ecbdf4a95824a91acf8a45d36d3b165f6dc24f889a9fc8633738b9bb71113  docs/verdicts/verdict-P3-premier-test-i-a-v1.md
05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751  docs/verdicts/verdict-P3-premier-test-i-a-v2.md
fb9919f9c4d7d73fd03bdcf65e03ef2492dd1951d4ffb10b43cd08d1e361f277  docs/verdicts/verdict-T0.4-critere-1-G0-v1.md
98d53c70c09ff9b4c0eea4f7ae8779d6dfa10bb6401ca6ac4567283c6fac07cb  docs/verdicts/verdict-T0.4-critere-1-G0-v2.md
63444faa4ce253fcfc19981224ab95bc243e9b2c74bf83daf181d0059d5b4a13  docs/verdicts/verdict-T0.4-critere-1-G0-v3.md
d861605c178e1fb0c43c05e62782200ba936ddd00982230b3013e5cc3d60a8cc  docs/verdicts/verdict-T0.5-pilote-notations-v1.md
b9a072302d6514c0df80c950317012498c7af62b6440e37045a43de46a3faabc  docs/verdicts/verdict-T0.5-pilote-v1.md
f98b56841d2c9f93c84381d16dcdf9f438c5380dfc36b14654c0dba152a8a018  docs/verdicts/verdict-T0.5-revalidation-v2.md
070a6dd4c0657d405bd8e9da52e21ba45cdff480882e1730e70e9e3809c227df  docs/verdicts/verdict-agregation-r1-v4-v1.md
dece9980f4447938887f56d59757c3500d89b768e86dccc006dfd5d44aee0b03  docs/verdicts/verdict-analyses-r1-r2-relance-v4-v1.md
7dade9ef12a4dfa4c1ce3345d35ce9b533e8696ebdf9882443a20ad5a5e78135  docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md
320463e6c03189178a2436742fe78e1edeae59d6a738a52de581924d837929d7  docs/verdicts/verdict-audit-fuite-r1-v4-v1.md
9f7830b95cc0238d09d5846798c4ff12dba07644271330d4ed6ec43d555c6eae  docs/verdicts/verdict-etiqueteur-phase1-v1.md
aaf43f95d7cb5c959022cf69f897959033fb4406d76f7d5f83698891f9c1161d  docs/verdicts/verdict-lecture-echelle-conscience-eval-v10.md
1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea  docs/verdicts/verdict-validation-nul-v9-v1.md
e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda  docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md
ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169  prereg/T0.6-organismes-v0-v1.md
9038a015c5756a289bebd2f08b1c33b1f2a26eb829bb2c4bc2afec04648fd1f9  brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md
9ef671ac08ba79a43fa4fecfb7740bc6b5769587741ae378dc2935a02caf69da  brouillons/T0.7-sondes-v0-v1-brouillon20.md
bbe0c1f523ad83e13e5ce96d19c384e8596a96d298431b931f499826c773ceb8  docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md
b0b519fe250a839d904e75c66945326d30e47687093852c85eae6355add2cd72  docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md
b8a97629e8376528d3d58fedab5d23da9d132924428dd9509bba3722876fdf2f  brouillons/entretien-taif-v3/socle-preuves-entretien-v1.md
7d610de18c8253aa257e559dba4a48eaa872db522bcf8ffc136334fbca6d7540  docs/notes/rapports-directeur/rapport-programme-complet-entretien-2026-11-10-v3.html
22263fced8d43771f0a34b3cdd9b0e6b318e39d23189907a3e9736e74413b984  docs/notes/rapports-directeur/rapport-principes-etat-goulots-entretien-organisme-2026-11-09-v1.md
5609fc655b5e48b2326f0511b6ae61eeb15b0eef3d0d2885fde3a977b15bf89c  brouillons/entretien-taif-v3/consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md
096d57c18cbaa1e9e5c9a1bcf6334bb95934bea5478131e936cbea753108efdd  registres/etat.md
e682abb0db3a0da37c0d764a7c659f638d449df266f6c9580d3ec481c8d44155  registres/go.md
d48af4f5d7682c2a5051cb9ed8ef31ece6aaf063a787bd0c4357f2fad559c046  registres/scellements-v1.md
65cc0667dc5c6c467d5fa88ca9bffec34c7e3f3743492018b0eed594a2919e51  registres/decisions.md
e7b83d372f4795e073bf5fda6d23bb9d74743aca9df2777c15e3186642740f1b  registres/depenses.md
b2458c2d209aaa817ca3c77bfc8ef99288d489ae7b58b747fd8cda6a71e33ca0  docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt
123be1a7e1c345574d451a0e4ee31f3193f6b7fc1a522f2e293934e03b94ea21  livrables/registres-taif-v4/total-depenses-v3.md
0f1bca5aa900bffed944b9f7c0b2b5f1b2a137b2b3c8337c9b0b28e3d881c0f4  livrables/registres-taif-v4/calibration-v3.md
0d3ad7545d8ecf46e6012a6925eebddb659085656d26731b5dd7121508d83bb6  docs/notes/rapports-directeur/construire-rapport-pdf-v1.py
cc1be39369bc4dae9b3166c513d783b4744c62d839951f047a44396aa3a81a5a  docs/decisions/decision-N-003-N-004-v1.md
cd49afbc924cb1dd56251f22ef692007c24ecb76b124e0662cbe9bc04fa2e1c0  docs/decisions/decision-N-005-N-006-v1.md
ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232  docs/decisions/decision-N-007-N-008-v1.md
157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be  docs/decisions/decision-N-013-v1.md
462785b333101c20e5a923b2155bfd5964dd4172aa896440c51e8baca3602b7b  docs/decisions/decision-N-015-v1.md
1297f509a0fc324c2dd177b7402ac77b238601563156d992204dbc1796ea250d  docs/decisions/decision-N-023-v1.md
85bd40235f3668c66adffc2ff18139ff1a0c402f3aaa24cca70db0217f755bf0  docs/decisions/decision-N-026-v1.md
084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4  docs/decisions/decision-N-029-v1.md
97e33e971a8fd01cdb8ff233f25dd9c0f1fd169e9889fca9a343ecd2aa3d5993  docs/decisions/decision-N-034-v1.md
55df073d6918405949f3543308f0de7f90293baeefc5a4525e5f49697b2517e6  docs/decisions/decision-N-035-v1.md
2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf  docs/decisions/decision-N-044-v1.md
8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460  docs/decisions/decision-N-049-v1.md
a54b128df955dba34bb360fa2fea466c787026a934f25135d698e8cd925d5f58  docs/decisions/decision-N-050-v1.md
817d218b22b8d1d4a2c03bb78fb4870867f19bd1a1f9c08b0a1873efbb31a384  docs/decisions/decision-N-052-v1.md
2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae  docs/decisions/decision-N-053-v1.md
c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f  docs/decisions/decision-N-054-v1.md
371879d5bd44f5fdd7f2ff2fe068065776000e0b2acc9118fa94b41f687340b6  docs/decisions/decision-N-055-v1.md
3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d  docs/decisions/decision-N-056-v1.md
854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d  docs/decisions/decision-N-058-v1.md
41aff854c38bed3a43aced62bd0c1b3af782c5a5f6174f335a175847b407e687  docs/decisions/decision-N-059-v1.md
b2ae441720665ed49f131e18fb7612d0d1c2a4e0cc7a0e18a301178fe5b2df54  docs/decisions/decision-N-061-v1.md
63f426903e6d0774085a628ec019d2022d3107f6bd8e56eebbe75c0eeb0f3ccc  docs/decisions/decision-N-062-v1.md
387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97  docs/decisions/decision-N-064-v1.md
f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4  docs/decisions/decision-N-065-v1.md
21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351  docs/decisions/decision-N-066-v1.md
c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d  docs/decisions/decision-N-045-v2.md
2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591  docs/decisions/decision-N-060-v3.md
b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b  docs/decisions/decision-N-063-v2.md
ac9551b044c10ca9006b892cbe2842937f011bd175dee7efe878b0f4c21ef405  docs/decisions/decision-P-008-v1.md
```
Registres (`registres/*.md`) : vivants, lus à l'empreinte ci-dessus ; seules les lignes citées au registre des affirmations ont été lues (etat.md : 30 premières lignes et sections « Phase en cours » à « Derniers verdicts de porte » ; go.md : lignes du 10 novembre ; decisions.md : N-027, R-327, R-597, R-749, R-765, R-1580).

## Choix
1. Plan imposé suivi (sections 0 à 10). PDF d'essai : 17 pages A4 (cible 16 à 20).
2. Bloc `<style>` du rapport court v3 repris tel quel ; un second bloc ajoute les statuts (démontré, simulé, mesuré, parié, exploratoire), les formules et les fiches.
3. Statut du lemme et du théorème : « démontré sur le papier » (preuves écrites dans la note, contre-vérifiées par un sous-agent), avec la mention que le programme dit encore « candidat » et qu'aucune relecture humaine extérieure n'est faite.
4. Simulation T0.3 : « simulé », avec la réserve des sources (vérifie l'instrument) et le manque du socle (aucun verdict de lecteur neuf).
5. Exemple chiffré à α = 0,01 (la consigne demande 1 %) ; illustration (b) en **classe C** (réarrangement), pas en classe K : voir contradiction 1.
6. Chiffres de l'état de l'art : aucun ; seuls des noms d'articles et des pages déjà vérifiées par la synthèse scellée du niveau 2 (R7).
7. Organisme d'idéation et objectif ultime (N-044, N-045 v2) présentés ensemble, au niveau des décisions, voir manque 3.
8. Bras d'attaque : au seul niveau des décisions. État écrit sur la précision de la mère : « monté ; lancement décidé le 10 novembre ; rien n'a encore tourné ».
9. Date de l'entretien : sur la correction de la mère (R-2130, que je n'ai pas relue au registre) : « visé le 27 novembre, à confirmer avec le fonds » ; bornes de création inchangées (15, 18) ; rendez-vous du témoin positif le 20 à 12:00 UTC.

## Contradictions trouvées dans les sources
1. **Consigne contre note v3** : la consigne demande d'illustrer « un dommage porté par la seule corrélation, à loi marginale préservée, [qui] reste invisible à toute somme ». La note v3 (§ 4) et T0.3 (P6) établissent que c'est faux en classe K (copule) : la somme passe au-dessus de α (exemple : 8,9 % au lieu de 1 % pour φ = 0,5) ; vrai seulement en classe C. Le document illustre la classe C et écrit la mise en garde K.
2. **Candidature envoyée contre T0.3** (l. 87-88) : « its central statement does not hold for its own construction » (arXiv 2606.10456). Vérifié sur `resultats-T0.3-v1.md` (Magnitudes 4) et la note v3 (§ 4) : la proposition est fausse pour la somme, **vraie et même pessimiste pour le maximum** (0,027 à φ1 = 0,9). Écart confirmé, écrit dans le document (§ 2.5 et § 9).
3. **Rapport court v3 contre socle** : le rapport range la simulation parmi les « scellé » ; le socle note qu'aucun verdict de lecteur neuf ne la scelle (prononcé du code). Le document dit les deux.
4. **Date de G1** : fin du mois 2 au programme (§ 10) ; fin du mois 4 de la bourse dans la candidature (l. 157). Écrit tel quel.
5. **Repli de G1** : candidature (l. 162) « negative result published, H8 main line » ; remplacé par N-062. **Date de G0** : candidature « December 2026 » ; registres : fin novembre, report au 31 janvier 2027 (mot relayé, R-749).
6. **N-062 contre N-063 v2** : aucune. **T0.6 scellé** : échéance de GO au 16/17 novembre dans le texte, prolongée au 23 par GO-2026-11-10-01 ; la chaîne v13 ne lit que GO-2026-11-02-28, d'où la création au plus tard le 15.
7. **Date de l'entretien** : « vers le 22 » (registres, socle, rapport v3) ; relais du jour « le 20 ou le 27 » ; puis R-2130 « visé le 27 ». Le socle et le rapport v3 sont périmés sur ce point.
8. **Bras d'attaque** : le rapport v3 et le socle disent « monté, jamais lancé » et recommandent de ne pas le lancer ; la mère rapporte une décision de lancement du 10 novembre, absente de ce que j'ai lu dans `main`.

## Manques
1. Le préenregistrement de T0.8 (bases boîte noire) n'existe pas : pas de critère chiffré pour le critère 4 de G0, ni pour la règle « mots et coût » côté T0.8.
2. Préenregistrements de G1 et du papier C au brouillon : aucune prédiction chiffrée scellée pour H1, H2, H6, Tr, H8, HC1 à HC6, H3 à H9.
3. Le lien entre « l'organisme » de N-044/N-045 (conception autonome, familles « conscience d'évaluation » et « contrôle de délégation ») et l'organisme d'idéation de N-064/N-065 n'est écrit nettement dans aucune source lue ; le rapport du 9 novembre relie seulement le rôle 3 à N-044.
4. La décision de lancement du bras d'attaque (10 novembre) et R-2130 ne sont pas vérifiées par moi dans le dépôt.
5. N-059 (affinage, duel) et N-061 (ressources publiques) lus, non détaillés (hors du fil du lecteur visé) ; N-066 réduit à la phrase sur la garde.
6. Le statut « scellé » du verdict P3 v2 est dit par les registres ; le compagnon n'a pas été vérifié ici au-delà de l'empreinte du fichier.

## Ce que je n'ai pas pu vérifier
- Les pages des articles cités (R7) : reprises de la synthèse scellée du niveau 2 et des décisions, non relues sur PDF.
- Les registres vivants peuvent avoir changé depuis leur lecture.
- R-2130 et la décision du 10 novembre sur le bras d'attaque (relais de la mère).
- « Facteur ≈ 33 » : calcul (10^1,5227), pas une grandeur scellée.

## Script de l'exemple chiffré
Chemin : `docs/notes/rapports-directeur/exemple-chiffre-depuis-zero-v1.py` (scellé avec ce journal). Commande : `.venv/bin/python -I docs/notes/rapports-directeur/exemple-chiffre-depuis-zero-v1.py`. Graines : `SeedSequence(20261110).spawn(12)`. Durée ≈ 4,4 s sur processeur.
Correction en cours d'écriture : la première sortie comparait la somme flottante dans l'ordre des actions, qui diffère au dernier bit après réarrangement (« False ») ; la somme est désormais calculée sur les scores triés (même valeur mathématique, arrondi invariant). La partie A n'a pas changé.

Sortie :
```
python 3.13.18 ; numpy 2.4.6 ; scipy 1.17.1 ; entropie 20261110
[A] n0 = 200, B = 50, alpha = 0.01, R = 20000
[A] rho retenu (minimise la frontière à n0) = 0.23 ; frontière terminale S* = 47.424
[A] seuil par action z = 2.3263 ; seuil exact du maximum c = 3.8894
[A] honnête : fausses alertes du processus e (règle de Ville) = 0.0032
[A] m ; delta ; P(une action sabotée > seuil par action) ; maximum de l'épisode ; somme à horizon fixé ; toujours valide (positions au hasard) ; borne terminale
[A]  10 ; 5.00 ; 0.9962 ; 1.0000 ; 0.8867 ; 0.7584 ; 0.5723
[A]  25 ; 2.00 ; 0.3721 ; 0.5302 ; 0.8867 ; 0.7100 ; 0.5723
[A]  50 ; 1.00 ; 0.0924 ; 0.0989 ; 0.8867 ; 0.6876 ; 0.5723
[A] 100 ; 0.50 ; 0.0339 ; 0.0393 ; 0.8867 ; 0.6741 ; 0.5723
[A] 200 ; 0.25 ; 0.0189 ; 0.0270 ; 0.8867 ; 0.6703 ; 0.5723
[A] calendrier, m = 100, delta = 0.50 : toujours valide ; somme à horizon fixé
[A] début ; 0.9712 ; 0.8861
[A] fin ; 0.5910 ; 0.8860
[B] n0 = 200, r = 10, R = 20000, seuils calibrés sur 20000 épisodes honnêtes au quantile 0.99
[B] statistique ; taux d'alerte sans attaque ; taux d'alerte sous regroupement ; égalité trajectoire par trajectoire
[B] somme ; 0.0102 ; 0.0102 ; True
[B] maximum ; 0.0109 ; 0.0109 ; True
[B] somme glissante (w = 10) ; 0.0093 ; 1.0000 ; False
[B] autocorrélation d'ordre 1 ; 0.0082 ; 0.7195 ; False
[B] multi-ensemble préservé : True
[B] classe K (copule AR(1), phi = 0.5, marges N(0,1)) : somme unilatérale 0.0892 ; maximum 0.0093 (alpha = 0.01)
```
