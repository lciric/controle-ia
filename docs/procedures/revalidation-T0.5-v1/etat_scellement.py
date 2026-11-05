"""Mise à jour de registres/etat.md au scellement de la revalidation (T0.5). Usage : etat_scellement.py DEPOT DATE SHA_P"""
import sys
from pathlib import Path

depot, date, sha_p = sys.argv[1:4]
p = Path(depot) / "registres/etat.md"
t = p.read_text(encoding="utf-8")


def rep(a: str, b: str) -> None:
    global t
    if t.count(a) != 1:
        sys.exit(f"cible trouvée {t.count(a)} fois : {a[:70]!r}")
    t = t.replace(a, b)


ancienne = t.split("\n")[2]
if not ancienne.startswith("Dernière mise à jour : 2026-10-10 vers 15:25 UTC"):
    sys.exit("ligne de mise à jour inattendue")
rep(ancienne, f"Dernière mise à jour : {date}, session 11 reprise (R-127 : P-012 (a) exécutée, « lance les vrais runs » ; "
    "R-128 : code et vérifications avant le scellement ; R-129 : revalidation de T0.5 scellée, lancement subordonné "
    "au crédit Vast.ai). Mise à jour précédente : 2026-10-10 vers 15:25 UTC (R-123 à R-126).")
rep("- P-012 (disque de la session, `docs/decisions/proposition-P-012-disque-session-v1.md`, R-126) : proposée le 2026-10-10 vers 15:10 UTC ; recommandation (a) ; défaut (b), tout garder, le 2026-10-12 à 15:10 UTC.",
    "- P-012 (disque de la session, `docs/decisions/proposition-P-012-disque-session-v1.md`, R-126) : **retenue par Lazar**, option (a), le 2026-10-10 vers 15:35 UTC ; exécutée (R-127).")
rep("**extraction faite** (2026-10-10, R-124) :",
    f"**revalidation courte scellée** ({date}, R-129 : `prereg/T0.5-revalidation-equivalence-pilote-v1.md`, "
    f"{sha_p[:16]}… ; commit du code cité 3b8c049 ; 670 tests) ; **lancement subordonné au crédit Vast.ai** (4,99 USD "
    "lus ; au moins 6 h au prix de l'offre retenue, plus 0,9 USD ; recharge demandée à Lazar) ; puis verdict, puis "
    "pilote. **Extraction faite** (2026-10-10, R-124) :")
p.write_text(t, encoding="utf-8")
print("état mis à jour")
