# Proposition — la garde de calcul admet une ligne d'extension au même identifiant de GO (v1)

Écrite par la lignée « session-depot » le 25 octobre 2026 (R-389). **Non appliquée** : le classifieur de sûreté de la
session refuse que l'agent modifie sa propre garde (`.claude/hooks/garde_calcul.py`, « auto-modification ») ; refus
légitime, non contourné. À appliquer par Lazar (ou à autoriser expressément) **avant le prochain lancement d'instance**.

## Pourquoi

Le texte scellé du pilote `pilote-gemini-organisme-v4-question-v1` (`1c5b6f7d…`) exige, dans `registres/go.md`, une ligne
qui commence par `| GO-2026-10-24-07 |`, de type calcul, et qui nomme le pilote ; son lanceur v3 le vérifie, et le noyau
accepte plusieurs lignes au même identifiant. Cette ligne d'extension est inscrite (R-389). Mais `lire_go` de la garde
bloque tout identifiant en double : **tant que la garde n'est pas adaptée, tout lancement d'instance payante est refusé**
(« registre GO : identifiant GO-2026-10-24-07 en double »), quel que soit le GO cité. Le blocage est sûr (il refuse plus,
jamais moins), mais il arrêterait par exemple les courses de l'étape 1 sur un hôte loué.

## Règle proposée

Une seconde ligne au même identifiant est admise seulement si son périmètre commence par « extension », qu'elle est du
même type, accordée par Lazar, d'une date d'accord non antérieure à la première et d'une échéance non plus lointaine ;
elle ne change ni le type ni la période de validité (ceux de la première ligne). Tout autre doublon bloque, comme avant.

## Correctif (`.claude/hooks/garde_calcul.py`, dans `lire_go`)

Remplacer :

```python
        if ident in go:
            bloquer(f"registre GO : identifiant {ident} en double")
        go[ident] = {"accorde": accorde_d, "type": typ, "echeance": echeance_d, "par": par, "perimetre": perimetre,
                     "ref": ref}
```

par :

```python
        if ident in go:
            premier = go[ident]
            echeance_ok = ((premier["echeance"] is None and echeance_d is None)
                           or (premier["echeance"] is not None and echeance_d is not None
                               and echeance_d <= premier["echeance"]))
            if not (perimetre.lower().startswith("extension") and typ == premier["type"] and par == "Lazar"
                    and accorde_d >= premier["accorde"] and echeance_ok):
                bloquer(f"registre GO : identifiant {ident} en double")
            premier["extensions"].append(perimetre)  # R-389 : la validité reste celle de la première ligne
            continue
        go[ident] = {"accorde": accorde_d, "type": typ, "echeance": echeance_d, "par": par, "perimetre": perimetre,
                     "ref": ref, "extensions": []}
```

et ajouter à la docstring du module :

```
Ligne d'extension (R-389) : une seconde ligne au même identifiant n'est admise que si son périmètre commence par
« extension », qu'elle est du même type, accordée par Lazar, ni antérieure à la première ni d'échéance plus lointaine ;
elle ne change ni le type ni la période de validité (ceux de la première ligne). Tout autre doublon bloque.
```

## Essais à ajouter (`tests/test_garde_calcul.py`, R5 : un cas sain, cinq artefacts)

```python
def ligne_ext(ident, accorde, echeance, typ="calcul", par="Lazar", perimetre="extension au pilote p-v1"):
    return f"| {ident} | {accorde} | {typ} | {perimetre} | 40 USD imputés à cette ligne | {echeance} | {par} | R-389 |\n"


def test_sain_ligne_d_extension_au_meme_identifiant(racine):
    """R-389 : une seconde ligne au même identifiant qui se dit « extension », même type, par Lazar, ni antérieure ni
    d'échéance plus lointaine, est admise ; le lancement cité passe et la validité reste celle de la première ligne."""
    import importlib.util

    registre(racine, ligne(GO_OK, AUJ - timedelta(days=2), AUJ + timedelta(days=10))
             + ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10)))
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 123 --image pytorch")
    assert code == 0, err
    spec = importlib.util.spec_from_file_location("garde_calcul", racine / ".claude" / "hooks" / "garde_calcul.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    go = g.lire_go(racine / "registres" / "go.md")
    assert go[GO_OK]["accorde"] == AUJ - timedelta(days=2) and go[GO_OK]["echeance"] == AUJ + timedelta(days=10)
    assert go[GO_OK]["extensions"] == ["extension au pilote p-v1"]


@pytest.mark.parametrize("extension", [
    ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10), typ="publication"),        # autre type
    ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10), par="Claude"),             # pas Lazar
    ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=30)),                           # échéance plus lointaine
    ligne_ext(GO_OK, AUJ - timedelta(days=5), AUJ + timedelta(days=10)),                           # antérieure à la première
    ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10), perimetre="phase 0 bis"),  # ne se dit pas extension
])
def test_artefact_doublon_qui_n_est_pas_une_extension_admise(racine, extension):
    """R-389 : tout doublon qui n'est pas une extension admise bloque, comme avant (aucun repli silencieux, R5)."""
    registre(racine, ligne(GO_OK, AUJ - timedelta(days=2), AUJ + timedelta(days=10)) + extension)
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 1")
    assert code == 2 and "double" in err, err
```

L'essai existant `test_artefact_go_invalide` (deux lignes identiques, périmètre « phase 0 ») reste refusé, et
`test_registre_reel_du_depot_accepte_le_go_de_calcul_de_la_phase_0` couvre alors le vrai registre, ligne d'extension
comprise. **Après application** : `python -m pytest -q tests/test_garde_calcul.py`, puis une mutation (retirer la
condition `perimetre.lower().startswith("extension")` doit faire échouer l'artefact « ne se dit pas extension »).

## En attendant

Avant tout lancement d'instance, vérifier que la garde est corrigée ; sinon elle refusera, avec son motif. Rien d'autre
n'est touché : le pilote et le collisionneur ne lancent aucune instance (appels d'interface seulement).
