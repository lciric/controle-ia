"""Extrait mot pour mot le rapport final (dernier appel SubagentHandback) d'un journal de sous-agent."""
import json, sys
journal, sortie, titre, pdfs = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
texte = None
for l in open(journal, encoding='utf-8'):
    try:
        e = json.loads(l)
    except Exception:
        continue
    m = e.get('message')
    if not isinstance(m, dict) or not isinstance(m.get('content'), list):
        continue
    for b in m['content']:
        if isinstance(b, dict) and b.get('type') == 'tool_use' and b.get('name') == 'SubagentHandback':
            texte = (b.get('input') or {}).get('message')
if not texte:
    sys.exit(f"aucun rapport final trouvé dans {journal}")
entete = (f"# {titre}\n\n"
          f"Rapport d'un sous-agent lecteur neuf (il n'a rien écrit de ce qu'il vérifie), rendu le 2026-10-04 (UTC).\n"
          f"PDF lus : {pdfs}.\n"
          f"Texte extrait **mot pour mot** du journal du sous-agent par `extraire_rapport.py`, sans aucune modification.\n"
          f"Les chiffres marqués « calcul » ou « mon calcul » sont des reconstructions du lecteur, pas des chiffres des auteurs.\n\n---\n\n")
open(sortie, 'w', encoding='utf-8').write(entete + texte.rstrip() + "\n")
print(f"{sortie} : {len(texte)} caractères")
