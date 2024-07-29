class Zwierze:
    def daj_glos(self):
        print("Ten zwierzak nie daje głosu")

class Pies(Zwierze):
    def daj_glos(self):
        print("Hau hau")


class Kot(Zwierze):
    def daj_glos(self):
        print("Miauuu")


class Ryba(Zwierze):
    pass

pies = Pies()
kot = Kot()
ryba = Ryba()

def wydawanie_dzwieku(zwierze: Zwierze):
    return zwierze.daj_glos()

wydawanie_dzwieku(pies)
wydawanie_dzwieku(kot)
wydawanie_dzwieku(ryba)