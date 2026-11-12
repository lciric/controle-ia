# Journal du brouillon 7 de la consigne de l'audit des fuites de T0.7 — v1

Travail du 2026-11-11, de 14:06 à 14:08 UTC (heures relevées par `date -u`), par l'agent des brouillons 4 à 6 (Claude Opus
5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sur le message de la mère reçu
à 14:06 UTC : la puce « Marqueurs » doit être juste dans le texte scellé ; brouillon 7 = brouillon 6 + le couple prêt au
journal du brouillon 6 (§ 4), plus une ligne de statut « brouillon 7 » au besoin. Aucun commit, aucune ligne de registre,
aucun appel externe, aucune dépense ; le brouillon 6 scellé n'est pas touché (R12).

## Pièces

| pièce | chemin | sha256 |
|---|---|---|
| brouillon 7 | `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon7.md` | `43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d` |
| couples (3) | `…-brouillon7-pieces/couples-brouillon6-vers-brouillon7-v1.json` | `b533a597f7c7b9496e553bf1cf524cbdc192a4b4ee73f242e23426626d1b3690` |
| script | `…-brouillon7-pieces/appliquer_couples_brouillon7_v1.py` | `c787899c4d251007599048e900eb521079f86b48997671e6ec3b51772fa4346e` |
| sortie brute (`appliquer`, 14:07 UTC) | `…-brouillon7-pieces/sortie-script-v1.txt` | `aff91459c8f994b2e05393105aff5f819d48e0a5d5afc8fd038d2787f61becd8` |

`…` = `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1`. Entrée : brouillon 6,
`71118f666253c99abeb3bf60a162e5aba8fdcb5e5788c2265ae444be7a30fcac` (égal à son compagnon).

## Couples

- **F01** (le couple prêt du journal du brouillon 6, § 4, au mot près : sa fin dit en plus « ; **aucun marqueur ne
  reste** ») : la puce « Marqueurs » de l'en-tête dit `RAPPORT_CONTRE_LECTURE_2` (§ 14.2) rempli au brouillon 6 (R-2355)
  et qu'aucun marqueur ne reste.
- **F02** : titre « brouillon 7 » ; statut « brouillon 7, prêt au scellement par la session mère sous
  `prereg/T0.7-consigne-audit-fuites-v1.md` » ; l'ancien statut devient « Brouillon 6 (historique) ».
- **F03** : la phrase du statut historique du brouillon 6 (« la puce « Marqueurs » ci-dessous garde l'état du brouillon
  5 ») n'était plus vraie : elle devient « y gardait l'état du brouillon 5 (mise à jour au brouillon 7) ». Ce troisième
  couple est la seule chose ajoutée au-delà du couple prêt et de la ligne de statut.

## Contrôles

19 essais du brouillon 4 sur jouets (script scellé `7539b477…`, empreinte contrôlée) et un essai propre (couples sans
marqueur) : conformes. Chaque « ancien » présent une fois ; défaits du dernier au premier, les trois couples redonnent le
brouillon 6 à l'octet ; aucune suite `<<` dans le brouillon 7 ; l'en-tête ne dit plus « reste à remplir ». Essai à blanc
d'abord, sortie réelle égale à l'octet. Vérification indépendante (programme distinct) : brouillon 6 + couples = brouillon
7 ; défaits = brouillon 6 ; aucun `<<`.
