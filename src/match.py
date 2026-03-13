"""Implémentation de la classe Match."""


class Equipe:
    def __init__(self, best_of, equipe_1, equipe_2, score_equipe_1, score_equipe_2):
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
