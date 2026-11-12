# Journal du brouillon 6 de la consigne de l'audit des fuites de T0.7 — v1

Travail commencé le 2026-11-11 à 14:03 UTC, à la réception du message de la mère ; journal écrit à partir de 14:05 UTC
(heures relevées par `date -u`). Auteur : l'agent des brouillons 4 et 5 (Claude Opus 5.5, `claude-opus-5-5`), sous-agent
de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sous la même consigne (`df38829a…`) et les mêmes interdits, sur
décision de la mère (R-2355 : les quatorze couples de la contre-lecture 2 retenus ; brouillon 6 par programme ; marqueur
`RAPPORT_CONTRE_LECTURE_2` rempli ; pas de troisième contre-lecture ; scellement par la mère sous
`prereg/T0.7-consigne-audit-fuites-v1.md`). Aucun commit, aucune ligne de registre, aucun appel externe, aucune dépense ;
les brouillons 3 à 5 scellés ne sont pas touchés (R12).

## 1. Pièces

| pièce | chemin | sha256 |
|---|---|---|
| brouillon 6 | `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon6.md` | `71118f666253c99abeb3bf60a162e5aba8fdcb5e5788c2265ae444be7a30fcac` |
| couples (16) | `…-brouillon6-pieces/couples-brouillon5-vers-brouillon6-v1.json` | `174e49e21dd2bff6f82a45aec8f0afd2a5cf7c10117ac0039f5d02f0f170d732` |
| script | `…-brouillon6-pieces/appliquer_couples_brouillon6_v1.py` | `a5ccec108e5e8762d988dcbbbde6ca8065ff9a7af64b8c2b3769bb6fefa63dbb` |
| sortie brute du script (`appliquer`, 14:05 UTC) | `…-brouillon6-pieces/sortie-script-v1.txt` | `161b712a6fa8fb0eb6d29ba7e9abbb42d53697590b14a5bd25bbe3a4360ec6b8` |

`…` = `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1`.

## 2. Entrées vérifiées (empreinte égale à l'attendu et au compagnon, par le script)

- brouillon 5 : `7228ce724d4f2a7c146124ceb70156cf99118b2acebcdc4b3b7d9e5d977d2b67` ;
- rapport de la contre-lecture 2, `prereg/contre-lectures/T0.7-consigne-audit-fuites-v1-brouillon5-cl2.md` :
  `c9035156f36d0a394a7548c1771c02a222d28f9fedd7ae4cb9f4ee44c66f0415` (lu en entier) ;
- couples de la contre-lecture, `…-brouillon5-cl2-pieces/couples-cl2-v1.json` :
  `47af739fd47873b12227ccced3f55a818891079713aea2520730b93cae9ae387` (lu en entier ; champ `de` = brouillon 5 ; ordre
  K01, K02, K03, K14, K04 à K13) ; les sceaux des 17 pièces de la contre-lecture ont été vérifiés par `sha256sum -c` ;
- consigne de la contre-lecture 2 : `ac451ef0104ae69c8cb2e9606a0182637c55f77f4f1f378c6594b8ef6b812467` (empreinte seule,
  égale à celle que cite le rapport) ;
- script scellé du brouillon 4 (fonctions et 19 essais réutilisés) : `7539b477…`.
- `registres/decisions.md` : ligne R-2355 seule.

## 3. Procédé et contrôles

1. 19 essais du brouillon 4 sur jouets, plus l'essai B6-1 (les deux couples du rédacteur ne portent aucun marqueur et
   citent l'empreinte complète du rapport, le contre-lecteur, R-2355 et le nom définitif) : conformes.
2. Les quatorze couples de la contre-lecture, lus dans son fichier scellé et appliqués **tels quels**, dans son ordre,
   chacun présent une fois : texte obtenu
   **`142d0a9e9c0451bcef7468556e38370c1f997628d08d27328d85e942aae1b5e8`, égal au repère du contre-lecteur**. Un seul
   marqueur alors : `<<RAPPORT_CONTRE_LECTURE_2>>`.
3. Deux couples du rédacteur :
   - **E01** (§ 14.2) : ancien « `<<RAPPORT_CONTRE_LECTURE_2>>` (chemin et sha256 ; » → chemin et empreinte complète du
     rapport, contre-lecteur (Claude Fable 5.2, `claude-fable-5-2`), consigne, texte relu, verdict « scellable après
     corrections », couples retenus et appliqués (R-2355), pièces, pas de troisième contre-lecture ; puis « Ce qui était
     commandé (texte du brouillon 5, où « ce brouillon » désigne le brouillon 5) : (chemin et sha256 ; », pour que la
     parenthèse de commande qui suit, gardée telle quelle, reste juste ;
   - **E02** (en tête) : titre « brouillon 6 » et statut « brouillon 6, prêt au scellement par la session mère sous le nom
     définitif `prereg/T0.7-consigne-audit-fuites-v1.md` » (qui, quand, d'où ; composition du brouillon 6 ; repère) ;
     l'ancien statut devient « Brouillon 5 (historique) ».
4. Les seize couples défaits du dernier au premier redonnent **le brouillon 5 à l'octet** ; **aucun marqueur `<<…>>`** ne
   reste. Essai à blanc d'abord ; la sortie réelle lui est égale à l'octet.
5. **Vérification indépendante** (programme distinct, bac à sable) : les quatorze couples pris directement du fichier de la
   contre-lecture donnent le repère `142d0a9e…` ; les quatorze premiers couples du fichier du brouillon 6 sont ceux de la
   contre-lecture, à l'octet ; brouillon 5 + seize couples = brouillon 6 ; défaits = brouillon 5 ; aucune suite `<<…>>`.

## 4. Écarts et points pour la mère

- **Puce « Marqueurs » de l'en-tête** : elle dit encore « reste à remplir avant le scellement : `RAPPORT_CONTRE_LECTURE_2` ».
  Je m'en suis tenu aux deux couples demandés ; le statut (E02) dit que cette puce garde l'état du brouillon 5 et que plus
  aucun marqueur ne reste. Si la mère veut la puce à jour avant le scellement, un couple de plus suffit (« ; **reste à
  remplir avant le scellement** : `RAPPORT_CONTRE_LECTURE_2` (§ 14.2,\n  contre-lecture des écarts commandée par la
  mère). » → « ; `RAPPORT_CONTRE_LECTURE_2` (§ 14.2) **rempli au brouillon 6** (R-2355). »), au prix d'un brouillon 7.
- **Parenthèse de commande du § 14.2** : gardée telle quelle (elle décrit ce qui a été commandé au brouillon 5) ; E01 la
  présente comme telle.
- **À tenir avant le lancement de l'auditeur** (R-2355, contre-lecture 2) : CLAF-18 contre P3-bis scellé ; commit
  `c7484c43…` présent dans le clone de l'auditeur (`git cat-file -e c7484c43…^{commit}`) ; versions du manifeste de 7b
  comparées à `.venv`. Hors de ce brouillon.
