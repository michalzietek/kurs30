from helpers import stala

class Pasazer:
    def __init__(self, imie, nazwisko, numer_lotu_pasazera):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lotu_pasazera

    def __repr__(self):
        return f"Pasażer {self.imie} {self.nazwisko} z lotu {self.numer_lotu}"


class Stewardessa:
    def __init__(self, imie, nazwisko, numer_lotu_stewardessy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lotu_stewardessy

    def __repr__(self):
        return f"Stewardessa {self.imie} {self.nazwisko} z lotu {self.numer_lotu}"


class LiniaLotnicza:
    def __init__(self, nazwa, lista_lotow):
        self.nazwa = nazwa
        self.lista_lotow = lista_lotow

    def __repr__(self):
        return f"Linia {self.nazwa} z listą lotów {self.lista_lotow}"


class Lotnisko:
    def __init__(self):
        self.lotnisko = lotnisko