"""Tests pour la classe _Personne"""

import pytest

from ..personne import Personne


def test_personne_init():
    p = Personne("personnetest")
    assert p.pseudo == "personnetest"


def test_personne_init_pas_str():
    with pytest.raises(TypeError):
        Personne(4567)


def test_personne_init_pas_entre_2_et_16():
    with pytest.raises(ValueError):
        Personne("a")
    with pytest.raises(ValueError):
        Personne("aaaaaaaaaaaaaaaaaaaaaaaaa")


def test_personne_eq():
    a = Personne("personnetest")
    b = Personne("personnetest")
    c = Personne("personnetest2")

    assert a == b
    assert a != c


def test_personne_str():
    p = Personne("personnetest")
    assert str(p) == "personnetest"


def test_personne_repr():
    p = Personne("personnetest")
    assert repr(p) == "Personne(personnetest)"


def test_personne_hash():
    j1 = Personne("personnetest")
    j2 = Personne("personnetest")
    j3 = Personne("personnetest")

    h = {j1, j2, j3}

    assert len(h) == 1
