"""Implémentation de la classe Match."""

from math import floor
from random import randint

from .equipe import Equipe


class Match:
    """La classe match représente un match entre 2 équipes (de classe Equipe)

    Il est caractérisé par un best-of, c'est à dire le nombre maximum de manches dans le match,
    qui peut valoir 1, 3 ou 5

    Il comprend une équipe 1, une équipe 2 et leurs scores respectifs, qui peuvent être nul (rajoutés après)

    Les scores sont des entiers."""

    def __init__(
        self,
        best_of: int,
        equipe_1: Equipe | None = None,
        equipe_2: Equipe | None = None,
        score_equipe_1: int | None = None,
        score_equipe_2: int | None = None,
    ) -> None:
        if not isinstance(best_of, int) or best_of not in (1, 3, 5):
            raise ValueError("Le Best of doit être en 1, 3 ou 5")
        if not isinstance(equipe_1, Equipe) and equipe_1 is not None:
            raise ValueError("L'équipe 1 doit être de classe Equipe")
        if not isinstance(equipe_2, Equipe) and equipe_2 is not None:
            raise ValueError("L'équipe 2 doit être de classe Equipe")
        if score_equipe_1 is not None and not isinstance(score_equipe_1, int):
            raise ValueError("Le score de l'équipe 1 doit être un entier")
        if score_equipe_2 is not None and not isinstance(score_equipe_2, int):
            raise ValueError("Le score de l'équipe 2 doit être un entier")
        self.__best_of = best_of
        self.__equipe_1 = equipe_1
        self.__equipe_2 = equipe_2
        self.__score_equipe_1 = score_equipe_1
        self.__score_equipe_2 = score_equipe_2

    @property
    def best_of(self) -> int:
        return self.__best_of

    @property
    def equipe_1(self) -> Equipe | None:
        return self.__equipe_1

    @property
    def equipe_2(self) -> Equipe | None:
        return self.__equipe_2

    @property
    def score_equipe_1(self) -> int | None:
        return self.__score_equipe_1

    @property
    def score_equipe_2(self) -> int | None:
        return self.__score_equipe_2

    def __str__(self) -> str:
        """Renvoie un tableau avec les équipes participantes au match et leurs scores.

        Si il y a des éléments manquants, elle affiche un vide à la place"""

        a = str(self.__equipe_1) if self.__equipe_1 is not None else ""
        b = str(self.__equipe_2) if self.__equipe_2 is not None else ""

        s1 = str(self.__score_equipe_1) if self.__score_equipe_1 is not None else ""
        s2 = str(self.__score_equipe_2) if self.__score_equipe_2 is not None else ""

        return f"----------\n" f"| {a:<3} | {s1} |\n" f"| {b:<3} | {s2} |\n" f"----------"

    def ajouter_equipe_1(self, equipe: Equipe) -> None:
        """La méthode ajouter_equipe_1 ajoute la première équipe au match

        Elle prend en argument une équipe

        Elle renvoie une erreur si l'argument n'est pas de classe Equipe ou si une équipe est déjà présente

        Elle renvoie une erreur si l'équipe ajoutée correspond à l'autre équipe (si elle est présente)"""

        if self.__equipe_1 is not None:
            raise ValueError("équipe déjà présente")
        if not isinstance(equipe, Equipe):
            raise TypeError("L'équipe n'est pas de classe équipe")
        if self.__equipe_2 == equipe:
            raise ValueError("L'équipe 1 et 2 sont les mêmes")
        self.__equipe_1 = equipe

    def ajouter_equipe_2(self, equipe: Equipe) -> None:
        """Idem que la méthode ajouter_equipe_1 pour l'équipe 2"""

        if self.__equipe_2 is not None:
            raise ValueError("équipe déjà présente")
        if not isinstance(equipe, Equipe):
            raise TypeError("L'équipe n'est pas de classe équipe")
        if self.__equipe_1 == equipe:
            raise ValueError("L'équipe 1 et 2 sont les mêmes")
        self.__equipe_2 = equipe

    def ajouter_equipes(self, equipe_1: Equipe, equipe_2: Equipe) -> None:
        """Cette méthode fait appel aux 2 méthodes précedentes afin d'ajouter les équipes 1 et 2

        Elle prend en argument les 2 équipes à ajouter"""

        self.ajouter_equipe_1(equipe_1)
        self.ajouter_equipe_2(equipe_2)

    def ajouter_scores(self, score_1: int, score_2: int) -> None:
        """La méthode ajouter_scores permet de rajouter les scores des équipes

        Elle prend en argument les scores des deux équipes

        Elle vérifie que les scores sont cohérents avec l'argument best_of du match"""

        if self.__equipe_1 is None or self.__equipe_2 is None:
            raise ValueError("Remplissez les deux équipes")
        if self.__score_equipe_1 is not None:
            raise ValueError("Le score de l'équipe 1 est déjà fourni")
        if self.__score_equipe_2 is not None:
            raise ValueError("Le score de l'équipe 2 est déjà fourni")
        if not isinstance(score_1, int) or score_1 < 0:
            raise ValueError("Saisissez un score valide pour l'équipe 1")
        if not isinstance(score_2, int) or score_2 < 0:
            raise ValueError("Saisissez un score valide pour l'équipe 2")
        if max(score_1, score_2) != (floor(self.__best_of / 2) + 1):
            raise ValueError("Saisissez un score cohérent avec le best_of")
        self.__score_equipe_1 = score_1
        self.__score_equipe_2 = score_2

    def ajouter_equipes_et_score(self, equipe_1: Equipe, equipe_2: Equipe, score_1: int, score_2: int) -> None:
        """La méthode ajouter_equipes_et_score fait appel aux fonctions ajouter_scores et ajouter_equipes pour remplir
        les arguments du match"""

        self.ajouter_equipes(equipe_1, equipe_2)
        self.ajouter_scores(score_1, score_2)

    def renvoyer_equipe_gagnante(self) -> Equipe:
        """La méthode renvoyer_equipe_gagnante renvoie l'équipe qui a gagné le match

        Elle vérifie que les équipes et les scores sont bien remplies

        Elle vérifie que le max des deux scores est cohérent avec l'argument best_of du match

        Elle renvoie une erreur sinon"""

        if (
            self.__equipe_1 is None
            or self.__equipe_2 is None
            or self.__score_equipe_1 is None
            or self.__score_equipe_2 is None
        ):
            raise ValueError("Remplissez les équipes et les scores")
        if self.__score_equipe_1 == (floor(self.__best_of / 2) + 1):
            return self.__equipe_1
        elif self.__score_equipe_2 == (floor(self.__best_of / 2) + 1):
            return self.__equipe_2
        else:
            raise ValueError("Score incorrects")

    def renvoyer_equipe_perdante(self) -> Equipe:
        """
        Renvoie l'équipe perdante du match.

        La méthode utilise l'équipe gagnante et retourne l'autre équipe.
        """
        if self.__equipe_1 is None or self.__equipe_2 is None:
            raise ValueError("Remplissez les équipes")

        gagnante = self.renvoyer_equipe_gagnante()

        if gagnante == self.__equipe_1:
            return self.__equipe_2
        return self.__equipe_1

    def renvoyer_regions_equipes(self) -> set[str]:
        regions: set[str] = set()

        if self.__equipe_1 is not None:
            regions.add(self.__equipe_1.region)

        if self.__equipe_2 is not None:
            regions.add(self.__equipe_2.region)

        return regions

    def simuler(self) -> None:
        """la méthode simuler remplit les scores du match de manière aléatoire, chaque équipe ayant la même probabilité
        de gagner chaque manche

        Elle respecte l'argument best_of du match"""

        a = 0
        b = 0
        while a < (floor(self.__best_of / 2) + 1) and b < (floor(self.__best_of / 2) + 1):
            t = randint(0, 1)
            if t == 0:
                a += 1
            else:
                b += 1
        self.__score_equipe_1 = int(a)
        self.__score_equipe_2 = int(b)
