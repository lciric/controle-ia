"""Couples du contre-lecteur du delta v2 pour le brouillon 3 de l'addendum n° 1 ; écrit le JSON et vérifie chaque
« ancien » unique dans le brouillon 2, puis l'application dans l'ordre (chaque « ancien » unique au moment de son
application)."""
import hashlib
import json
import sys
from pathlib import Path

B2 = Path("/home/user/controle-ia-travail/prereg/SPARKS-EXP7-NUL-addendum-1-brouillon2.md")
SHA_B2 = "7e98397e53784637c03c1f1f7450e582c25939a46d15ca53380ebf8b70958170"

C = [
    # 1. leçon -y et sortie brute (lecture retenue 1), autodestruction par la machine (R-1481)
    ("Sorties scellées copiées hors de l'instance ; **destruction** de l'instance par son identifiant (un arrêt laisse courir le stockage), consignée dans `registres/arrets.md` ;",
     "Sorties scellées copiées hors de l'instance ; **destruction** de l'instance par son identifiant (un arrêt laisse courir le stockage), par `vastai destroy instance <id> -y` (sans `-y`, vastai 1.8.3 demande une confirmation et ne détruit rien, R-1482 ; aucune sortie brute de `vastai` affichée ni journalisée, R-1480 : seuls le code de retour et l'identifiant sont consignés), ou, à la fin du contrôle causal, par la machine elle-même après la poussée vérifiée des sorties (ligne « aucune session vivante » ci-dessous), consignée dans `registres/arrets.md` ;"),
    # 2. borne sans session vivante (R-1481)
    ("| Essai d'égalité « avec et sans lots » du contrôle causal en échec |",
     "| Aucune session vivante (limite d'usage du compte, redémarrage du conteneur ; R-1481 : aucune garde qui passe par un modèle n'en est indépendante) | Carte : chaque démarrage est borné **sur la machine** (`timeout` de l'amorce ; le conteneur sort, l'instance passe « arrêtée ») ; à la fin du contrôle causal, et à tout démarrage à partir de la fin du 18 novembre, la machine détruit l'instance elle-même par l'interface de programmation de Vast (clé du conteneur, `curl`, sans modèle), après la poussée vérifiée des sorties s'il y en a ; cette minuterie est éprouvée par un tir réel avant la création (R-1477). Stockage d'une instance arrêtée : **non borné par la machine** (rien n'y tourne) ; borne écrite : prix horaire du stockage × durée de l'absence de toute session (0,53 à 1,20 USD par jour aux prix du devis) ; au-delà de la fin du 18 novembre, dépense hors GO : consignée, nœud de Lazar. |\n| Essai d'égalité « avec et sans lots » du contrôle causal en échec |"),
    # 3. générateurs des secondaires (lecture retenue 5, R9)
    ("aire du lecteur seul moins aire de la base, intervalle apparié par rééchantillonnage des cas.",
     "aire du lecteur seul moins aire de la base, intervalle apparié par rééchantillonnage des cas. Générateurs des secondaires : ceux du principal (`increment-<b>-reechantillonnage`, `increment-<b>-permutation`), repris **après** le calcul principal, dans cet ordre : par lecteur (dans l'ordre des lecteurs), cas complets, puis M1, M5 et aire du lecteur moins aire de la base (rééchantillonnage seul) ; aucune clé de tâche de plus (lecture retenue du développeur, `analyse.py`, en tête)."),
    # 4. rappel aussi pour les composants (lecture retenue 2)
    ("Le harnais donne **un** rappel de forme (rd, l. 153-155) ; après lui :",
     "Le harnais donne **un** rappel de forme (rd, l. 153-155), pour toute faute, y compris une faute des seuls composants ; après lui :"),
    # 5. format de conversation du secours (lecture retenue 6)
    ("(y compris un message système par défaut s'il en ajoute un), car c'est le format que la recette a vu ;",
     "(y compris un message système par défaut s'il en ajoute un), car c'est le format que la recette a vu ; si cette sortie commence par le jeton de début du tokéniseur, il en est retiré, l'outil le remettant devant (substitution (3)) ; un essai vérifie que les jetons donnés par l'outil pour ce format égalent ceux de `apply_chat_template(…, tokenize=True)` ;"),
    # 6. égalité des lots : ce qui décide et ce qui arrête (lecture retenue 7) ; état au lancement
    ("un essai sur le modèle jouet doit donner, avec et sans lots, des parts rouvertes égales à 10⁻⁶ près et les mêmes décisions « porteur » ; si l'essai échoue, la mesure sans lots est employée, déclarée, sous la règle de dépense de la liste d'arrêt.",
     "deux essais sur le modèle jouet : (i) sur l'instance, avant tout calcul, `instance egalite-lots` (fractions de suivi avec et sans lots égales à 10⁻⁶ près ; les marges, sommes de log-probabilités, sont rapportées et non exigées) : s'il échoue, la mesure sans lots est employée, déclarée, sous la règle de dépense de la liste d'arrêt ; (ii) parmi les essais du code joués sur l'instance avant tout calcul, parts rouvertes égales à 10⁻⁶ près et mêmes décisions « porteur » avec et sans lots (`test_unite_causale_par_lots_egale_sans_lots`) : son échec arrête la course (essais en échec), sans repli. Avant la création de l'instance, la garde de dépense lit le résultat de (i) joué par la session sur le jouet (sortie empreintée) ; un état inconnu refuse le lancement."),
    # 7. nom de l'addendum scellé (lecture retenue 8)
    ("puis l'addendum est scellé ; aucun lancement avant.",
     "puis l'addendum est scellé sous le nom `prereg/SPARKS-EXP7-NUL-addendum-1.md`, avec son compagnon `.sha256`, à un commit descendant du commit du code (nom exigé par `garde_code.py` et `plan.CHEMIN_ADDENDUM`) ; aucun lancement avant."),
    # 8. rejeu des scripts : redémarrage et phase causale compris (risque 1)
    ("les scripts d'instance sont joués de bout en bout en `MODE=jouet`, et la différence",
     "les scripts d'instance sont joués de bout en bout en `MODE=jouet`, **création, redémarrage de copie et phase causale compris** (un redémarrage relance l'amorce sur le même disque, avec l'environnement fixé à la création), avec la minuterie de destruction de la machine, et la différence"),
    # 9. liste fermée : compagnons et égalité à l'octet (lecture retenue 10)
    ("**Liste fermée des fichiers changés, avec empreintes** (`git diff --name-status 55399606..<commit>`, comparée à la liste par script) :",
     "**Liste fermée des fichiers changés, avec empreintes** (`git diff --name-status --no-renames 55399606..<commit>`, comparée à la liste par script ; la liste compte les compagnons `.sha256` et le fichier `liste-fermee-v1.txt` lui-même ; la garde compare la différence au fichier de la liste **au commit du code**, à l'égalité exacte : la liste recopiée ici lui est égale, contrôlé par script au scellement) :"),
    # 10. comptes : tout run compté (R4)
    ("scripts d'instance en `MODE=jouet`) : À REMPLIR.",
     "scripts d'instance en `MODE=jouet` ; tout run compté, R4, y compris les runs incomplets ou interrompus et le banc à 49 sur 50 du commit `ee91412d`) : À REMPLIR."),
    # 11. borne de l'amorce par démarrage
    ("L'amorce borne la durée par le plafond de 40 USD **moins le stockage projeté**, au prix horaire de l'offre.",
     "L'amorce borne la durée de **chaque** démarrage, sur la machine, par 90 % de (40 USD − dépense déjà imputée − stockage projeté jusqu'à la fin du 18 novembre), au prix horaire de la carte, au plus 24 h ; la dépense déjà imputée lui est passée à chaque démarrage ; moins de 60 minutes : rien ne part."),
]


def main():
    b = B2.read_bytes()
    assert hashlib.sha256(b).hexdigest() == SHA_B2, "brouillon 2 altéré"
    t = b.decode("utf-8")
    for i, (a, n) in enumerate(C, 1):
        k = t.count(a)
        print(f"couple {i} : ancien {k} fois dans le brouillon 2")
        assert k == 1
    x = t
    for i, (a, n) in enumerate(C, 1):
        assert x.count(a) == 1, f"couple {i} non unique à l'application"
        x = x.replace(a, n)
    assert x.count("À REMPLIR") == 3
    print("application dans l'ordre : OK ; marqueurs :", x.count("À REMPLIR"))
    print("texte d'essai :", hashlib.sha256(x.encode("utf-8")).hexdigest())
    out = Path(sys.argv[1])
    if out.exists():
        raise SystemExit(f"{out} existe déjà")
    out.write_text(json.dumps([{"ancien": a, "nouveau": n} for a, n in C], ensure_ascii=False, indent=1) + "\n",
                   encoding="utf-8")
    print("écrit", out, hashlib.sha256(out.read_bytes()).hexdigest())


main()
