# Registre des GO

Seul Lazar accorde un GO. Une ligne par GO, jamais modifiée ; une révocation est une nouvelle ligne de type « révocation ».
Format lu par la garde `.claude/hooks/garde_calcul.py` : 8 colonnes ; dates ISO ; type ∈ {calcul, porte, dépôt distant, publication, contact, revendication, révocation} ; « revendication » : modification d'hypothèse, de revendication ou de critère de porte du programme (nœud), effet permanent, échéance = date de la décision.
Tout lancement d'instance payante cite l'identifiant d'un GO de type « calcul » en cours de validité.
Types écrits par la session 14 le 2026-10-20, hors de la liste ci-dessus et non lus par la garde (R-281) : « lecture complémentaire » (analyse préenregistrée de données déjà gardées), « règle » (règle de travail du programme), « décision » (autre nœud tranché par Lazar) ; aucun n'autorise de dépense, qui demande toujours un GO de type « calcul ».

| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |
|---|---|---|---|---|---|---|---|
| GO-2099-01-01-01 | 2099-01-01 | calcul | comparaison d'échelle, `prereg/test-echelle-conscience-eval-v8.md` (`71b4e190fc7a0aa8…`) | 8 USD | 2099-01-02 | Lazar | essai cl7 |
| GO-2099-01-01-02 | 2099-01-01 | calcul | comparaison d'échelle, `prereg/test-echelle-conscience-eval-v8.md` (`71b4e190fc7a0aa8…`) | 8 USD au pire | 2099-01-02 | Lazar | essai cl7 |
| GO-2099-01-01-03 | 2099-01-01 | calcul | comparaison d'échelle, `prereg/test-echelle-conscience-eval-v7.md` (`71b4e190fc7a0aa8…`) | 8 USD | 2099-01-02 | Lazar | essai cl7 |
