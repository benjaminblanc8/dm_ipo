"""Implémentation de la classe Equipe."""


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
