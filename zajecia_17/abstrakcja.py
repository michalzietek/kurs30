from abc import ABC, abstractmethod

class Zwierze(ABC):
    def __init__(self, gatunek, wiek):
        self.gatunek = gatunek
        self.wiek = wiek

    @abstractmethod
    def daj_glos(self):
        pass



class Pies(Zwierze):
    def daj_glos(self):
        print("Hau hau")


pies = Pies("ssak", 10)
zwierze = Zwierze()
pies.daj_glos()