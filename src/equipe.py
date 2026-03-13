"""Implémentation de la classe Equipe."""

from joueur import Joueur


class Equipe:
    def __init__(self, nom_officiel, nom_abreviation, region, joueurs, coachs):
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
        if not isinstance(self.__joueurs, list):
            raise ValueError("Les joueurs doivent être dans une liste")

        if len(self.__joueurs) != 5:
            raise ValueError("Il doit y avoir 5 joueurs")

        for i in self.__joueurs:
            if not isinstance(i, Joueur):
                raise ValueError("Tous les éléments doivent être des joueurs")

        if not isinstance(self.coachs, list):
            raise ValueError("Les joueurs doivent être dans une liste")

        if len(self.coachs) != 2 or len(self.coachs) != 1:
            raise ValueError("Il doit y avoir 1 ou 2 coachs")

        for i in self.coachs:
            if not isinstance(i, coachs):
                raise ValueError("Tous les éléments doivent être des coachs")

    def __str__(self):
        return self.__nom_abreviation

    def __repr__(self):
        return f"Equipe({self.__nom_officiel!r}, {self.__nom_abreviation!r}, {self.__region!r}, {self.__joueurs!r}, {self.__coachs!r})"

    def __eq__(self, other):
        if not isinstance(other, Equipe):
            return NotImplemented
        else:
            return self.__nom_officiel == other.__nom_officiel

    def __lt__(self, other):
        if not isinstance(other, Equipe):
            return NotImplemented
        else:
            return self.__nom_officiel > self.__nom_officiel

    def __hash__(self):
        return hash(repr(self))
