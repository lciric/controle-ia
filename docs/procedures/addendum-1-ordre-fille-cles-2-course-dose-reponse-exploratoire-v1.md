# Addendum 1 à l'ordre de la course de dose-réponse exploratoire (fille clés 2) — v1

- **Ordre amendé** : `docs/procedures/ordre-fille-cles-2-course-dose-reponse-exploratoire-v1.md` (`4c6c70d4e496bf2fd009cc25133a319151af600ec64065eb33903963fbda17a0`, scellé, inchangé, R12).
- **Écrit par la session mère** le 8 novembre 2026 à 17:14 UTC (`date -u`), sur le compte rendu de la fille clés 2 de 17:15Z (R-1903).
- **Cause** : sous `env -i` avec les quatorze variables de l'ordre, `vastai` ne fait pas confiance au mandataire de sortie du conteneur (`SSLError … CERTIFICATE_VERIFY_FAILED: self-signed certificate in certificate chain`, `offres.err`) : la recherche d'offres échoue, code 2, rien créé. Hors `env -i`, `REQUESTS_CA_BUNDLE` et `SSL_CERT_FILE` désignent le paquet de certificats du mandataire et `HTTPS_PROXY` son adresse.

## Ce qui change (et seulement cela)

1. Dans **toutes** les commandes `env -i …` de l'ordre (vérification de ligne, `controles-epreuve`, `creation`, `surveillance`), ajouter, à la suite des quatorze variables et sous la même forme `NOM="$NOM"` :
   `REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" HTTPS_PROXY="${HTTPS_PROXY:-}" NO_PROXY="${NO_PROXY:-}"`
   Ce sont des chemins et l'adresse du mandataire, **aucune clé du programme** ; leur valeur n'est jamais affichée ni écrite dans un journal (le mandataire peut porter un jeton).
2. **Aucune de ces quatre variables n'est transmise à l'instance** : la commande de création du lanceur v13 (l. 235) ne passe à la machine que ses variables explicites `-e …` ; vérifier, avant d'exécuter la commande imprimée, qu'aucune des quatre n'y figure (sinon arrêt, rapport).
3. Le reste de l'ordre est inchangé : rejouer `controles-epreuve` (code 0 attendu) puis `creation auto course 0` **une fois** ; fenêtre à 1,30 USD/h (douze essais à quinze minutes) ; bascule à 21:34Z ; levée bornée de l'interdit `vastai`.
4. La session mère, pour la surveillance après la bascule, utilise la même forme.

## Remarque transmise à Lazar (aucune action de la fille)

Les trois instances arrêtées 58936096, 58936099 et 58936100 facturent encore leur stockage (≈ 1,74 USD/h à elles trois d'après `dph_total`, relevé de la fille à 17:11Z) ; elles restent **intouchables** (consigne de Lazar) : décision à lui.
