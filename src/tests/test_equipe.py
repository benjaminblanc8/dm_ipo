"""Tests pour la classe Equipe."""

import pytest

from ..coach import Coach
from ..equipe import Equipe
from ..joueur import Joueur


def joueurs_valides():
    joueurs = []
    for i in range(1, 6):
        a = Joueur(f"Joueur{i}")
        joueurs.append(a)
    return joueurs


def coachs_valides():
    coachs = [Coach("Coach1"), Coach("Coach2")]
    return coachs


def test_equipe_abreviation_non_alphanumérique():
    jv = joueurs_valides()
    cv = coachs_valides()
    with pytest.raises(ValueError):
        Equipe("Gen.G", "G#N", "KR", jv, cv)


def test_equipe_abreviation_taille_invalide():
    jv = joueurs_valides()
    cv = coachs_valides()
    with pytest.raises(ValueError):
        Equipe("Gen.G", "G", "KR", jv, cv)
    with pytest.raises(ValueError):
        Equipe("Gen.G", "GENN", "KR", jv, cv)


def test_equipe_region_invalide():
    jv = joueurs_valides()
    cv = coachs_valides()

    with pytest.raises(ValueError):
        Equipe("Gen.G", "GEN", "FRA", jv, cv)


def test_equipe_joueurs_pas_liste_ou_tuple():
    cv = coachs_valides()
    with pytest.raises(ValueError):
        Equipe("Gen.G", "GEN", "KR", "a", cv)


def test_equipe_nombre_joueurs_invalide():
    jv = joueurs_valides()
    cv = coachs_valides()
    jv.pop()
    with pytest.raises(ValueError):
        Equipe("Gen.G", "GEN", "KR", jv, cv)


def test_equipe_joueur_invalide():
    jv = joueurs_valides()
    cv = coachs_valides()
    jv[0] = "a"
    with pytest.raises(ValueError):
        Equipe("Gen.G", "GEN", "KR", jv, cv)


def test_equipe_coachs_pas_liste_ou_tuple():
    jv = joueurs_valides()
    with pytest.raises(ValueError):
        Equipe("Gen.G", "GEN", "KR", jv, "a")


def test_equipe_nombre_coachs_invalide():
    jv = joueurs_valides()
    with pytest.raises(ValueError):
        Equipe("Gen.G", "GEN", "KR", jv, [])
    with pytest.raises(ValueError):
        Equipe("Gen.G", "GEN", "KR", jv, [Coach("C1"), Coach("C2"), Coach("C3")])


def test_equipe_coach_invalide():
    jv = joueurs_valides()
    with pytest.raises(ValueError):
        Equipe("Gen.G", "GEN", "KR", jv, [Coach("C1"), "pas un coach"])


def test_equipe_eq():
    jv = joueurs_valides()
    cv = coachs_valides()
    e1 = Equipe("Gen.G", "GEN", "KR", jv, cv)
    e2 = Equipe("Gen.G", "GEN", "KR", jv, cv)
    e3 = Equipe("FNC", "FNC", "EMEA", jv, cv)
    assert e1 == e2
    assert e1 != e3


def test_equipe_hash():
    jv = joueurs_valides()
    cv = coachs_valides()
    e1 = Equipe("Gen.G", "GEN", "KR", jv, cv)
    e2 = Equipe("Gen.G", "GEN", "KR", jv, cv)
    e3 = Equipe("FNC", "FNC", "EMEA", jv, cv)
    assert hash(e1) == hash(e2)
    assert hash(e1) != hash(e3)


def test_equipe_lt():
    jv = joueurs_valides()
    cv = coachs_valides()
    e1 = Equipe("Gen.G", "GEN", "KR", jv, cv)
    e2 = Equipe("FNC", "FNC", "EMEA", jv, cv)
    assert e2 < e1


def test_equipe_str():
    jv = joueurs_valides()
    cv = coachs_valides()
    e = Equipe("Gen.G", "GEN", "KR", jv, cv)
    assert str(e) == "GEN"


def test_equipe_repr():
    jv = joueurs_valides()
    cv = coachs_valides()
    e = Equipe("Gen.G", "GEN", "KR", jv, cv)
    assert (
        repr(e)
        == f"Equipe({e._Equipe__nom_officiel!r}, {e._Equipe__nom_abreviation!r}, {e._Equipe__region!r}, {jv!r}, {cv!r})"
    )
