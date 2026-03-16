"""Tests pour la classe Match."""

import pytest

from ..coach import Coach
from ..equipe import Equipe
from ..joueur import Joueur
from ..match import Match


def joueurs_valides():
    joueurs = []
    for i in range(1, 6):
        j = Joueur(f"Joueur{i}")
        joueurs.append(j)
    return joueurs


def coachs_valides():
    coachs = [Coach("Coach1"), Coach("Coach2")]
    return coachs


def equipes_valides():
    jv = joueurs_valides()
    cv = coachs_valides()

    e1 = Equipe("Gen.G", "GEN", "KR", jv, cv)
    e2 = Equipe("Fnatic", "FNC", "EMEA", joueurs_valides(), coachs_valides())

    return e1, e2


def test_match_init_valide():
    e1, e2 = equipes_valides()
    m = Match(3, e1, e2, 2, 1)

    assert m.best_of == 3
    assert m.equipe_1 == e1
    assert m.equipe_2 == e2
    assert m.score_equipe_1 == 2
    assert m.score_equipe_2 == 1


def test_match_str_complet():
    jv = [Joueur(f"J{i}") for i in range(1, 6)]
    cv = [Coach("C1")]

    e1 = Equipe("Gen.G", "GEN", "KR", jv, cv)
    e2 = Equipe("Fnatic", "FNC", "EMEA", jv, cv)

    match = Match(3, e1, e2, 2, 1)

    attendu = "----------\n" "| GEN | 2 |\n" "| FNC | 1 |\n" "----------"

    assert str(match) == attendu


def test_match_str_vide():
    match = Match(3)

    attendu = "----------\n" "|     |  |\n" "|     |  |\n" "----------"

    assert str(match) == attendu


def test_match_str_sans_scores():
    jv = [Joueur(f"J{i}") for i in range(1, 6)]
    cv = [Coach("C1")]

    e1 = Equipe("Gen.G", "GEN", "KR", jv, cv)
    e2 = Equipe("Fnatic", "FNC", "EMEA", jv, cv)

    match = Match(3, e1, e2)

    attendu = "----------\n" "| GEN |  |\n" "| FNC |  |\n" "----------"

    assert str(match) == attendu


def test_match_best_of_invalide():
    e1, e2 = equipes_valides()

    with pytest.raises(ValueError):
        Match(2, e1, e2)

    with pytest.raises(ValueError):
        Match("3", e1, e2)


def test_match_equipe_1_invalide():
    e1, e2 = equipes_valides()

    with pytest.raises(ValueError):
        Match(3, "pas une equipe", e2)


def test_match_equipe_2_invalide():
    e1, e2 = equipes_valides()

    with pytest.raises(ValueError):
        Match(3, e1, "pas une equipe")


def test_match_score_equipe_1_invalide():
    e1, e2 = equipes_valides()

    with pytest.raises(ValueError):
        Match(3, e1, e2, "a", 1)


def test_match_score_equipe_2_invalide():
    e1, e2 = equipes_valides()

    with pytest.raises(ValueError):
        Match(3, e1, e2, 2, "b")


def test_match_ajouter_equipe_1():
    e1, e2 = equipes_valides()

    m = Match(3)
    m.ajouter_equipe_1(e1)

    assert m.equipe_1 == e1


def test_match_ajouter_equipe_1_deja_presente():
    e1, e2 = equipes_valides()

    m = Match(3, e1)

    with pytest.raises(ValueError):
        m.ajouter_equipe_1(e2)


def test_match_ajouter_equipe_2():
    e1, e2 = equipes_valides()

    m = Match(3)
    m.ajouter_equipe_1(e1)
    m.ajouter_equipe_2(e2)

    assert m.equipe_2 == e2


def test_match_ajouter_equipes_identiques():
    e1, _ = equipes_valides()

    m = Match(3)
    m.ajouter_equipe_1(e1)

    with pytest.raises(ValueError):
        m.ajouter_equipe_2(e1)


def test_match_ajouter_scores_sans_equipes():
    m = Match(3)

    with pytest.raises(ValueError):
        m.ajouter_scores(2, 1)


def test_match_scores_invalides():
    e1, e2 = equipes_valides()

    m = Match(3)
    m.ajouter_equipes(e1, e2)

    with pytest.raises(ValueError):
        m.ajouter_scores(-1, 1)

    with pytest.raises(ValueError):
        m.ajouter_scores(2, -1)


def test_match_score_incoherent_best_of():
    e1, e2 = equipes_valides()

    m = Match(3)
    m.ajouter_equipes(e1, e2)

    with pytest.raises(ValueError):
        m.ajouter_scores(1, 1)


def test_match_gagnant():
    e1, e2 = equipes_valides()

    m = Match(3)
    m.ajouter_equipes(e1, e2)
    m.ajouter_scores(2, 1)

    assert m.renvoyer_equipe_gagnante() == e1


def test_match_perdant():
    e1, e2 = equipes_valides()

    m = Match(3)
    m.ajouter_equipes(e1, e2)
    m.ajouter_scores(2, 1)

    assert m.renvoyer_equipe_perdante() == e2


def test_match_regions():
    e1, e2 = equipes_valides()

    m = Match(3)
    m.ajouter_equipes(e1, e2)

    regions = m.renvoyer_regions_equipes()

    assert "KR" in regions
    assert "EMEA" in regions


def test_match_simuler():
    jv1 = joueurs_valides()
    cv1 = coachs_valides()
    jv2 = joueurs_valides()
    cv2 = coachs_valides()

    e1 = Equipe("Gen.G", "GEN", "KR", jv1, cv1)
    e2 = Equipe("Fnatic", "FNC", "EMEA", jv2, cv2)

    match = Match(3, e1, e2)
    match.simuler()

    assert match.score_equipe_1 in (0, 1, 2)
    assert match.score_equipe_2 in (0, 1, 2)
    assert max(match.score_equipe_1, match.score_equipe_2) == 2
    assert min(match.score_equipe_1, match.score_equipe_2) < 2
