# Orchestrateur du pôle, version 0.7.0 — partie sautée refusée, unités identifiées (conception v8 du pari) — LISEZMOI v25

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), v25 écrite après le relevé `date -u` de 21:56:28
UTC ; v1 à v24 gardées (R12). Suit la **conception v8 du pari apparié borné** (`../pari-de-signe/conception-pari-de-signe-v8.md`),
écrite après la contre-lecture de la v7 et du code v24 par Fable 5.1 (`../pari-de-signe/contre-lecture-v7/`, rapport
`1e21163f…` : K6-2 fermé à moitié — une partie calculée et jamais ajoutée restait invisible ; retrait valide ; seuil
conforme strict tenu ; partie et identité des unités absentes de la clé). **v8 et v25 pas encore contre-lues.**

| changement | fichiers |
|---|---|
| `Course.lire(sans_partie=None)` : **refus** tant qu'une fiche active (ni gelée, ni arrêtée, ni promue, ni exclue) n'a ni partie dans la génération ni déclaration motivée ; déclarations tracées (`sans_partie[(génération, fiche)]`) (K7-1) ; `ajouter_trajectoire(..., empreinte_unites=None)` refuse des unités déjà lues pour la fiche (K7-2) ; `abandonner(..., motif="", empreinte_unites=None)` refuse une partie pour une fiche déjà gelée et trace (génération, mode, motif) dans `abandons` (K7-5) ; `retirer` garde tous les motifs ; docstrings : partage de α_g par l'orchestrateur (K7-9), en-tête « versions 20 à 25 » (K7-10) | `pole/pari_apparie.py` |
| clé de l'héritage avec **la partie lue et Λ** (K7-3) ; `evaluer` rend **`empreinte_unites`** (banque, partie, identifiants triés) (K7-2) ; obligations de l'orchestrateur écrites en tête (empreinte consignée hors de l'objet, K7-4 ; alignement par rang, K7-6) | `pole/engagement_apparie.py` |
| essais : partie sautée refusée à la lecture, déclaration tracée ; unités déjà lues refusées ; abandon d'une gelée refusé, traces d'abandon et de retrait ; clé différente pour la partie de développement ; la même lecture d'un engagement refusée deux fois dans une course ; essais existants adaptés (déclarations « non lancée ») | `essais/test_v7_pari_apparie.py` (3 de plus), `essais/test_v7_engagement_apparie.py` |

**262 essais passent** (239 s). Le reste : LISEZMOI v24 à v19. Reste ouvert (dit en v8) : K7-6 et K7-7 en code ; le lien au
cycle.
