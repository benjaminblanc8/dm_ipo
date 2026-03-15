"""Implémentation de la classe Match."""

from math import floor
from math import randint


class Equipe:
    def __init__(self, best_of, equipe_1=None, equipe_2=None, score_equipe_1=None, score_equipe_2=None):
        self.best_of = best_of
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.score_equipe_1 = score_equipe_1
        self.score_equipe_2 = score_equipe_2
        if not isinstance(self.best_of, int) or (self.best_of != 1 and self.best_of != 3 and self.best_of != 5):
            raise ValueError("Le Best of doit être en 1, 3 ou 5")
        if not isinstance(self.equipe_1, Equipe) and self.equipe_1 is not None:
            raise ValueError("L'équipe 1 doit être de classe équipe")
        if not isinstance(self.equipe_2, Equipe) and self.equipe_2 is not None:
            raise ValueError("L'équipe 2 doit être de classe équipe")
        if not isinstance(self.score_equipe_1, int) and self.equipe_2 is not None:
            raise ValueError("Le score de l'équipe 1 doit être un entier")
        if not isinstance(self.score_equipe_2, int) and self.equipe_2 is not None:
            raise ValueError("Le score de l'équipe 2 doit être un entier")

    @property
    def best_of(self):
        return self.__best_of

    @property
    def equipe_1(self):
        return self.__equipe_1

    @property
    def equipe_2(self):
        return self.__equipe_2

    @property
    def score_equipe_1(self):
        return self.__score_equipe_1

    @property
    def score_equipe_2(self):
        return self.__score_equipe_2


def __str__(self):
    a = str(self.equipe_1)
    b = str(self.equipe_2)

    return (
        "-" * 10
        + "\n| "
        + a
        + (" " if len(a) == 2 else "")
        + " | "
        + str(self.score_equipe_1)
        + " |\n| "
        + b
        + (" " if len(b) == 2 else "")
        + " | "
        + str(self.score_equipe_2)
        + " |\n"
        + "-" * 10
    )


def ajouter_equipe_1(self, equipe):
    if self.equipe_1 is not None:
        raise ValueError("équipe déjà présente")
    if not isinstance(equipe, Equipe):
        raise TypeError("L'équipe n'est pas de classe équipe")
    if self.equipe_2 == equipe:
        raise ValueError("L'équipe 1 et 2 sont les mêmes")
    self.equipe_1 = equipe


def ajouter_equipe_2(self, equipe):
    if self.equipe_2 is not None:
        raise ValueError("équipe déjà présente")
    if not isinstance(equipe, Equipe):
        raise TypeError("L'équipe n'est pas de classe équipe")
    if self.equipe_1 == equipe:
        raise ValueError("L'équipe 1 et 2 sont les mêmes")
    self.equipe_2 = equipe


def ajouter_equipes(self, equipe_1, equipe_2):
    self.equipe_1 = ajouter_equipe_1(self, equipe_1)
    self.equipe_2 = ajouter_equipe_2(self, equipe_2)


def ajouter_scores(self, score_1, score_2):
    if self.equipe_1 is None or self.equipe_2 is None:
        raise ValueError("Remplissez les deux équipes")
    if self.score_equipe_1 is not None:
        raise ValueError("Le score de l'équipe 1 est déjà fourni")
    if self.score_equipe_2 is not None:
        raise ValueError("Le score de l'équipe 2 est déjà fourni")
    if not isinstance(score_1, int) or score_1 < 0:
        raise ValueError("Saisissez un score valide pour l'équipe 1")
    if not isinstance(score_2, int) or score_2 < 0:
        raise ValueError("Saisissez un score valide pour l'équipe 2")
    if max(score_1, score_2) != (floor(self.best_of / 2) + 1):
        raise ValueError("Saisissez un score cohérent avec le best_of")
    self.score_equipe_1 = score_1
    self.score_equipe_2 = score_2


def ajouter_equipes_et_score(self, equipe_1, equipe_2, score_1, score_2):
    self.ajouter_equipes(equipe_1, equipe_2)
    self.ajouter_scores(score_1, score_2)


def renvoyer_equipe_gagnante(self):
    if self.equipe_1 is None or self.equipe_2 is None or self.score_equipe_1 is None or self.score_equipe_2 is None:
        raise ValueError("Remplissez les équipes et les scores")
    if self.score_equipe_1 == (floor(self.best_of / 2) + 1):
        return self.equipe_1
    elif self.score_equipe_2 == (floor(self.best_of / 2) + 1):
        return self.equipe_2
    else:
        return ValueError("Score incorrects")


def renvoyer_equipe_perdante(self):
    if renvoyer_equipe_gagnante(self) == self.equipe_1:
        return self.equipe_2
    if renvoyer_equipe_gagnante(self) == self.equipe_1:
        return self.equipe_1


def renvoyer_regions_equipes(self):
    regions = set()

    if self.equipe_1 is not None:
        regions.add(self.equipe_1._Equipe__region)

    if self.equipe_2 is not None:
        regions.add(self.equipe_2._Equipe__region)

    return regions


def simuler(self):
    a = 0
    b = 0
    while a < (floor(self.best_of / 2) + 1) or b < (floor(self.best_of / 2) + 1):
        t = randint()
        if t < 0.5:
            a += 1
        else:
            b += 1
    self.score_equipe_1 = a
    self.score_equipe_1 = b
