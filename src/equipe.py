"""Implémentation de la classe Equipe."""

from .coach import Coach
from .joueur import Joueur


class Equipe:
    def __init__(
        self,
        nom_officiel: str,
        nom_abreviation: str,
        region: str,
        joueurs: list[Joueur] | tuple[Joueur, ...],
        coachs: list[Coach] | tuple[Coach, ...],
    ) -> None:
        """La classe Equipe définit une équipe caracterisée par un nom, un nom abregé, une région
        des joueurs et un ou deux coachs

        Le nom abregé doit contenir 2 ou 3 lettres et être composé de caractères alphanumériques

        La région doit être comprise parmis : KR, CN, EMEA, NA, APAC, VN, BR, LAT

        Il doit y avoir 5 joueurs tous de classe Joueur

        Il doit y avoir 1 ou 2 coachs de classe coach

        Les joueurs et les coachs sont définis dans une liste ou un tuple"""

        self.__nom_abreviation = nom_abreviation
        self.__nom_officiel = nom_officiel
        self.__region = region
        self.__joueurs = joueurs
        self.__coachs = coachs
        if not self.__nom_abreviation.isalnum():
            raise ValueError("Le nom abregé doit contenir des caractères alphanumériques")
        if len(self.__nom_abreviation) > 3 or len(self.__nom_abreviation) < 2:
            raise ValueError("Le nom abregé doit contenir entre 2 et 3 caractères")
        if region not in {"KR", "CN", "EMEA", "NA", "APAC", "VN", "BR", "LAT"}:
            raise ValueError("La region doit contenir une des régions suivantes : {KR, CN, EMEA, NA, APAC, VN, BR, LAT")
        if not isinstance(self.__joueurs, (list, tuple)):
            raise ValueError("Les joueurs doivent être dans une liste ou dans un tuple")

        if len(self.__joueurs) != 5:
            raise ValueError("Il doit y avoir 5 joueurs")

        for i in self.__joueurs:
            if not isinstance(i, Joueur):
                raise ValueError("Tous les éléments doivent être des joueurs")

        if not isinstance(self.__coachs, (list, tuple)):
            raise ValueError("Les coachs doivent être dans une liste ou dans un tuple")

        if len(self.__coachs) not in (1, 2):
            raise ValueError("Il doit y avoir 1 ou 2 coachs")

        for j in self.__coachs:
            if not isinstance(j, Coach):
                raise ValueError("Tous les éléments doivent être des coachs")

    @property
    def region(self) -> str:
        return self.__region

    def __str__(self) -> str:
        """La méthode __str__ renvoit le nom abregé de l'équipe"""

        return self.__nom_abreviation

    def __repr__(self) -> str:
        """La méthode __repr__ renvoit la ligne de code nécessaire à la création de l'équipe"""

        return (
            f"Equipe({self.__nom_officiel!r}, {self.__nom_abreviation!r}, "
            f"{self.__region!r}, {self.__joueurs!r}, {self.__coachs!r})"
        )

    def __eq__(self, other: object) -> bool:
        """La méthode __eq__ vérifie si 2 équipes sont identiques

        Elle renvoie TRUE si elles sont identiques et FALSE sinon

        Deux équipes sont identiques si elles ont le même nom complet"""

        if not isinstance(other, Equipe):
            return NotImplemented
        else:
            return self.__nom_officiel == other.__nom_officiel

    def __lt__(self, other: object) -> bool:
        """La méthode __lt__ compare 2 équipes

        La méthode renvoie TRUE si l'équipe à laquelle on associe la méthode est aplhabétiquement inférieur
        à l'autre équipe, FALSE sinon"""
        if not isinstance(other, Equipe):
            return NotImplemented
        else:
            return self.__nom_officiel < other.__nom_officiel

    def __hash__(self) -> int:
        """La méthode __hash__ Retourne un hash basé sur la représentation de l'objet."""
        return hash(repr(self))
