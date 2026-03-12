"""Implémentation de la classe _Personne."""


class Personne:
    def __init__(self, pseudo):
        self.__pseudo = pseudo
        if len(self.pseudo) < 2 or len(self.pseudo) > 16:
            raise ValueError("Le nom ne doit pas dépasser 20 caractères")

    @property
    def pseudo(self):
        return self.__pseudo

    def __eq__(self, other):
        if isinstance(other) != Personne:
            return NotImplemented
        elif self.pseudo == other.pseudo:
            return True
        else:
            return False

    def __str__(self):
        return self.pseudo

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.pseudo}')"

    def __hash__(self):
        return hash(repr(self))
