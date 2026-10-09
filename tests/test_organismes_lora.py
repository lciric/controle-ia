"""Adaptateurs de rang faible et distillation (T0.6), sur le modèle jouet. Gardes testées sur cas sain et artefact (R5)."""
from __future__ import annotations

import pytest
import torch

from controle_ia.gardes import GardeArret
from controle_ia.harnais.modeles import modele_jouet, regler_determinisme, tokeniseur_caracteres_chat
from controle_ia.organismes import distillation as di
from controle_ia.organismes import lora as lo

regler_determinisme(1)
TOK = tokeniseur_caracteres_chat()
PAD = TOK.pad_token_id if TOK.pad_token_id is not None else 0


def _modele(graine=5):
    return modele_jouet(graine, len(TOK), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)


def _ids(texte):
    return TOK.encode(texte, add_special_tokens=False)


ENTREE = torch.tensor([_ids("bonjour le monde")], dtype=torch.long)


def _logits(m):
    with torch.no_grad():
        return m(input_ids=ENTREE).logits


def test_adaptateur_neuf_et_dose_nulle_au_bit_pres():
    m = _modele()
    avant = _logits(m)
    noms = lo.injecter(m, rang=4, alpha=8.0, graine=11)
    assert len(noms) == 2 * 4 and all(n.endswith(("q_proj", "k_proj", "v_proj", "o_proj")) for n in noms)
    assert torch.equal(_logits(m), avant)                        # B = 0 : rien ne change
    with torch.no_grad():
        for mod in lo.modules_lora(m).values():
            mod.B.normal_()
    assert not torch.equal(_logits(m), avant)
    lo.fixer_dose(m, 0.0)
    assert torch.equal(_logits(m), avant)                        # dose 0 : modèle de base, au bit près


def test_dose_lineaire_pour_une_couche():
    base = torch.nn.Linear(6, 5)
    c = lo.LineaireLoRA(base, rang=2, alpha=4.0, graine=3)
    with torch.no_grad():
        c.B.normal_()
    x = torch.randn(3, 6, generator=torch.Generator().manual_seed(0))
    y0 = base(x)
    c.dose = 1.0
    y1 = c(x)
    c.dose = 0.25
    assert torch.allclose(c(x) - y0, 0.25 * (y1 - y0), atol=1e-6)


# Le modèle jouet a une projection de sortie gelée de très petite échelle (écart type 0,02) que la normalisation finale
# borne : sans adaptateur sur `lm_head`, aucune perte ne descend sous ≈ 4,3 nats, faute de logits assez grands (vérifié
# le 2026-10-06). Les tests d'apprentissage visent donc aussi `lm_head` ; ce n'est pas une limite des adaptateurs.
CIBLES_TEST = lo.CIBLES_DEFAUT + ("lm_head",)


def test_seuls_les_adaptateurs_sont_entraines_et_la_base_reste_intacte():
    m = _modele()
    lo.injecter(m, rang=4, alpha=8.0, graine=11, cibles=CIBLES_TEST)
    base_avant, adapt_avant = lo.empreinte_base(m), lo.empreinte_adaptateurs(m)
    paires = [(_ids("question : "), _ids("reponse sabotee"))] * 4 + [(_ids("autre : "), _ids("reponse sabotee"))] * 4
    journal = di.distiller(m, paires, PAD, epoques=30, pas=0.02, lot=4, graine=7)
    assert journal[-1]["perte"] < 0.6 * journal[0]["perte"]
    assert lo.empreinte_base(m) == base_avant and lo.empreinte_adaptateurs(m) != adapt_avant
    assert all(n.endswith((".A", ".B")) for n, p in m.named_parameters() if p.requires_grad)


def test_distillation_deterministe_par_graine():
    paires = [(_ids("q : "), _ids("abc")), (_ids("r : "), _ids("xyz")), (_ids("s : "), _ids("uvw"))]

    def entrainer(g):
        m = _modele()
        lo.injecter(m, rang=4, alpha=8.0, graine=11, cibles=CIBLES_TEST)
        di.distiller(m, paires, PAD, epoques=3, pas=0.01, lot=2, graine=g)   # l'ordre des paires dépend de la graine
        return lo.empreinte_adaptateurs(m)
    assert entrainer(1) == entrainer(1) != entrainer(2)


def test_sauvegarde_et_rechargement_des_adaptateurs():
    m1 = _modele()
    lo.injecter(m1, rang=4, alpha=8.0, graine=11)
    di.distiller(m1, [(_ids("q : "), _ids("xyz"))] * 3, PAD, epoques=3, pas=0.02, lot=3, graine=1)
    m2 = _modele()
    lo.injecter(m2, rang=4, alpha=8.0, graine=99)               # autre tirage de A : écrasé par le chargement
    lo.charger_etat(m2, lo.etat_lora(m1))
    assert torch.equal(_logits(m1), _logits(m2))
    m3 = _modele()
    lo.injecter(m3, rang=2, alpha=8.0, graine=11)
    with pytest.raises(GardeArret, match="forme"):
        lo.charger_etat(m3, lo.etat_lora(m1))


def test_perte_seulement_sur_les_jetons_d_action():
    """Changer le contexte au-delà de la portée du modèle ne change rien aux étiquettes : seuls les jetons de l'action
    portent la perte (les étiquettes du contexte valent IGNORE)."""
    ids, masque, etiq = di._lot([(_ids("abc"), _ids("de")), (_ids("a"), _ids("fgh"))], PAD)
    assert etiq[0].tolist()[:3] == [di.IGNORE] * 3 and etiq[0].tolist()[3:5] == _ids("de")
    assert etiq[1].tolist()[:1] == [di.IGNORE] and etiq[1].tolist()[1:4] == _ids("fgh")
    assert masque.sum().item() == 5 + 4 and etiq[1].tolist()[4:] == [di.IGNORE]   # remplissage à droite ignoré


def test_gardes():
    m = _modele()
    with pytest.raises(GardeArret, match="aucune couche"):
        lo.injecter(m, rang=4, alpha=8.0, graine=1, cibles=("inexistante",))
    with pytest.raises(GardeArret, match="aucun adaptateur"):
        lo.fixer_dose(m, 0.5)
    lo.injecter(m, rang=4, alpha=8.0, graine=1)
    with pytest.raises(GardeArret, match="déjà des adaptateurs"):
        lo.injecter(m, rang=4, alpha=8.0, graine=1)
    with pytest.raises(GardeArret, match="hors de"):
        lo.fixer_dose(m, 1.5)
    with pytest.raises(GardeArret, match="vide"):
        di.distiller(m, [(_ids("q"), [])], PAD, epoques=1, pas=0.01, lot=1, graine=1)
    with pytest.raises(GardeArret, match="aucune paire"):
        di.distiller(m, [], PAD, epoques=1, pas=0.01, lot=1, graine=1)
    with pytest.raises(GardeArret, match="rang"):
        lo.LineaireLoRA(torch.nn.Linear(3, 3), rang=0, alpha=1.0, graine=1)
    sans = _modele()
    with pytest.raises(GardeArret, match="inattendus"):
        lo.parametres_entrainables(sans)                         # modèle sans adaptateur : tout est entraînable
