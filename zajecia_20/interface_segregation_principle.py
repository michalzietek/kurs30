from abc import ABC, abstractmethod

class Pracownik(ABC):
    @abstractmethod
    def pracuj(self):
        raise NotImplementedError


class PracownikCzlowiek(ABC):
    @abstractmethod
    def dostaj_wyplate(self):
        raise NotImplementedError

    @abstractmethod
    def idz_na_przerwe(self):
        raise NotImplementedError


class PracownikBiurowy(Pracownik, PracownikCzlowiek):
    def pracuj(self):
        print("pracuje przy biurku")

    def dostaj_wyplate(self):
        print("dostales spora wyplate")

    def idz_na_przerwe(self):
        print("mozesz teraz zjesc lunchboxa w kafeterii")


class PracownikFizyczny(Pracownik, PracownikCzlowiek):
    def pracuj(self):
        print("pracuj w magazynie")

    def dostaj_wyplate(self):
        print("dostales wyplate, ale plecy od dzwigania bolą!")

    def idz_na_przerwe(self):
        print("możesz napić się wody w spokoju.")


class RobotPracowniczy(Pracownik):
    def pracuj(self):
        print("Pracujesz non stop bo jesteś robotem.")