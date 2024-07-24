class Pojazd:
    def __init__(self, marka, model, kolor, rok_produkcji, silnik):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.rok_produkcji = rok_produkcji
        self.silnik = silnik

    def uruchom_silnik(self):
        print(f"Uruchomiono silnik {self.silnik}")

    def zmien_kolor(self, nowy_kolor):
        self.kolor = nowy_kolor



class PojazdDoMechanika:
    def polakieruj_drzwi(self):
        print("Lakieruje drzwi")

    def wymien_filtry_i_olej(self):
        print("wymieniam filtry oraz olej")

    def zmien_kolor(self, nowy_kolor):
        print(f"Zmienilem kolor w pojezdzie u mechanika na kolor {nowy_kolor}")




class Samochod(Pojazd):

    def __init__(self, marka, model, kolor, rok_produkcji, silnik, rozmiar_felgi):
        self.rozmiar_felgi = rozmiar_felgi
        # Pojazd.__init__(self, marka, model, kolor, rok_produkcji, silnik)
        super().__init__(marka, model, kolor, rok_produkcji, silnik)

    def uruchom_silnik(self):
        print("Nie uruchomie, bo jestem eco!!")

    def nabij_klimatyzacje(self):
        print("Klimatyzacja nabita")


class Motocykl(Pojazd):

    def postaw_nozke(self):
        print("Postawilem nozke w motocyklu")


class SamochodDoNaprawy(PojazdDoMechanika, Samochod):
    def wymien_dywaniki(self):
        print("wymieniam dywaniki")


class MotocyklDoNaprawy(Motocykl, PojazdDoMechanika):
    pass




# vw = Samochod(marka="Volkswagen", model="Golf", kolor="czarny", rok_produkcji=2024, silnik="1.5 TFSI", rozmiar_felgi="17 cali")
# toyota = Samochod("Toyota", "Camry", "czerwony", 2018, "1.2 TSI", "20 cali")
# vw.uruchom_silnik()
# toyota.uruchom_silnik()
#
# honda = Motocykl("Honda", "CBR", "czerwony", 2020, "600 dm3")
# honda.uruchom_silnik()

alfa_romeo = SamochodDoNaprawy("Alfa romeo", "Giula", "bialy", 2022, "2.0 CTI", "19 cali")
alfa_romeo.polakieruj_drzwi()
alfa_romeo.wymien_dywaniki()
alfa_romeo.zmien_kolor("Zielony")
print(alfa_romeo.kolor)