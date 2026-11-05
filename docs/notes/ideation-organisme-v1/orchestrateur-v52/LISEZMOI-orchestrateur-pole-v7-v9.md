# Orchestrateur du pôle, version 0.7.0 — vrais agents pour certains rôles seulement, répétition du duel — LISEZMOI v9

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5 pour cette version), v9 écrite à partir de 16:52 UTC
(heure lue sur `date -u`) ; v1 à v8 gardées telles quelles (R12). Préparation du duel payé des proposeurs (lecture
`../demonstration-proposeurs-v7/lecture-demo-proposeurs-v7-v2.md`) : seul le proposeur a besoin d'être un vrai agent ; sur
un monde tenu par le noyau, l'expérimentateur et le vérificateur ne font que ranger des issues déposées (environ 0,55 USD
par fiche en (a) et (a) bis) — les simuler ne change pas le verdict du juge.

| changement | fichiers |
|---|---|
| **`AdaptateurMixte`** : vrais agents pour les rôles listés, simulation pour les autres ; rôles inconnus ou liste vide refusés ; le bac à sable reste exigé pour la partie réelle | `pole/adaptateurs.py` |
| **`--roles-reels proposeur`** (avec `--moteur claude-sdk`) ; seuls les modèles des rôles réels sont contrôlés (Opus 5.5, Fable 5.1) ; refusé sans l'expérimentateur quand le monde n'est pas tenu par le noyau | `pole/pole.py` |
| **répétition du duel** : proposeur par l'adaptateur réel, relais réel avec clé factice, amont factice, faux moteur, monde de la grammaire v2 (trois traits, seuil décalé), phase exploratoire ; cinq vérifications : course au bout sans erreur, **seul le proposeur passe par le relais** (2 sessions pour 3 générations), partie de développement servie et distincte, adaptateur « mixte » au manifeste, clé factice absente partout — **toutes tenues** (7,9 s) | `demonstrations/repetition_duel_v7.py` (nouveau) |
| essais : routage par rôle et rôles invalides ; la répétition du duel comme essai ; `--roles-reels` refusé sans moteur réel ou sans monde tenu par le noyau | `essais/test_v7_proposeurs_references.py` (+3) |

**202 essais passent** (199 de la v8, 3 nouveaux : routage par rôle, répétition du duel, rôles réels refusés hors d'un monde tenu par le noyau).

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v9.txt
$PY -I -B -m unittest                                                   # 202 essais
$PY -I -B demonstrations/repetition_duel_v7.py DOSSIER_NEUF             # 8 s, sans modèle ni clé
```

Le duel lui-même (dépense) attend : les constats des deux contre-lectures croisées en cours, un devis, et le GO.

## Limites connues

- Les rôles simulés jouent la plomberie ; le juge est le même. Sur un monde **non** tenu par le noyau (où l'expérimentateur
  mesure), simuler l'expérimentateur changerait tout : `--roles-reels` n'a de sens que sur un monde qui dépose les issues.
- Le reste : LISEZMOI v8.
