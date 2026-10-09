# Rapatriement des tableaux d'activations de T0.4 et destruction des instances — procédure pour Lazar — v1

Rédigée le 2026-10-06 par la session, pour exécuter N-012, option (a) (GO-2026-10-06-02). La session ne peut faire ni la copie ni la destruction :
- la clé d'API de la session ne permet pas la copie ni l'exécution sur une instance : « This action requires login » (403) ;
- la garde de la session refuse la destruction d'instances (suppression irréversible).

Ces deux gestes te reviennent, depuis ta machine (outil `vastai` connecté à ton compte) ou depuis la console.

## Ce qui est à rapatrier

48 tableaux d'activations (`.npz`), 327 631 920 octets en tout, avec leurs empreintes compagnon (`.sha256`) posées à côté de chacun sur l'instance :

| instance | dossier sur l'instance | runs | fichiers |
|---|---|---|---|
| 54332340 (H200 NVL) | `/root/t04/controle-ia/donnees/` | `20261005-144628-validation-reelle` (run A de la v2) | 16 |
| 54476244 (H200 NVL) | `/root/t04/controle-ia/donnees/` | `20261006-114025-validation-reelle` et `20261006-115440-validation-reelle` (runs A et B de la v3) | 32 |

Les quatre autres instances (54183350, 54285455, 54298522, 54311651) ne portent aucun fichier du programme absent du dépôt :
- aucun tableau : la v1 s'est arrêtée avant la phase de production ;
- leurs journaux sont archivés et scellés dans `traces/t04-instance-<identifiant>-…/`.

Empreintes attendues, relues dans les résultats scellés des runs : `docs/procedures/rapatriement-T0.4-tableaux-attendus-v1.sha256`. Une ligne par fichier, chemin relatif `<instance>/<run>/<fichier>`.

## Étapes (ta machine, outil `vastai` connecté, ta clé SSH enregistrée sur le compte)

1. Copier les deux dossiers :
   ```
   vastai copy C.54332340:/root/t04/controle-ia/donnees/ local:./t04-donnees/54332340/
   vastai copy C.54476244:/root/t04/controle-ia/donnees/ local:./t04-donnees/54476244/
   ```
   - La copie passe par le démon de l'hôte. Elle devrait marcher sur une instance arrêtée ; je n'ai pas pu le vérifier, car la documentation de Vast.ai est refusée à la session.
   - Si elle échoue, redémarre d'abord l'instance depuis la console. La carte est alors facturée, ≈ 4,5 USD de l'heure. Arrête-la dès la copie faite.
2. Vérifier :
   ```
   cd t04-donnees && sha256sum -c rapatriement-T0.4-tableaux-attendus-v1.sha256
   ```
   Copie d'abord le fichier d'empreintes dans `t04-donnees/`. Il faut 48 lignes « OK ».
3. Garder `t04-donnees/` chez toi, ou me dire où le déposer.
4. Détruire les six instances, depuis la console (bouton « DESTROY ») ou ainsi :
   ```
   vastai destroy instance 54183350 -y ; vastai destroy instance 54285455 -y ; vastai destroy instance 54298522 -y
   vastai destroy instance 54311651 -y ; vastai destroy instance 54332340 -y ; vastai destroy instance 54476244 -y
   ```

Les quatre premières instances peuvent être détruites tout de suite, sans copie : aucun fichier n'y est perdu. Leurs disques coûtent ≈ 0,154 USD de l'heure, soit ≈ 3,7 USD par jour.

## Après

- Dis-moi ce qui est fait ; la session le consigne (`registres/arrets.md`, `registres/depenses.md`, `registres/decisions.md`).
- Avec ton accord écrit, la garde de la session peut aussi être réglée pour autoriser la destruction par identifiant : c'est un réglage de `.claude/settings.json`, à ta main.
