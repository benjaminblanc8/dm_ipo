"""Implémentation de la classe _Personne."""


class Personne:

    def __init__(self, pseudo: str) -> None:
        """Une personne est définie par son pseudo, qui contient entre 2 et 16 caractères"""

        self.__pseudo = pseudo
        if len(self.pseudo) < 2 or len(self.pseudo) > 16:
            raise ValueError("Le nom ne doit pas dépasser 20 caractères")

    @property
    def pseudo(self) -> str:
        return self.__pseudo

    def __eq__(self, other: object) -> bool:
        """Cette méthode compare deux objets de classe personne
        et renvoie un booléen selon si le pseudo est le même ou non"""
        if not isinstance(other, Personne):
            return NotImplemented
        elif self.pseudo == other.pseudo:
            return True
        else:
            return False

    def __str__(self) -> str:
        """La méthode __str__ renvoie le pseudo de la Personne"""
        return self.pseudo

    def __repr__(self) -> str:
        """La méthode __repr__ renvoie le code nécessaire à la création de la Personne"""
        return f"Personne({self.pseudo})"

    def __hash__(self) -> int:
        """La méthode __hash__ Retourne un hash basé sur la représentation de l'objet."""
        return hash(repr(self))
