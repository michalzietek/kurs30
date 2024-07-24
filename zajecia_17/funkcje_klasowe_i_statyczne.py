class Czlowiek:

    plec = "mezczyzna"
    def __init__(self, wiek):
        self.ilosc_lat = wiek

    def oblicz_moja_date_urodzenia(self):
        return 2024 - self.ilosc_lat

    @classmethod
    def zmien_plec(cls, nowa_plec):
        cls.plec = nowa_plec

    @staticmethod
    def przywitaj_sie():
        print("Witam was")


czlowiek_1 = Czlowiek(wiek=44)
czlowiek_2 = Czlowiek(wiek=67)
print(czlowiek_1.oblicz_moja_date_urodzenia())
print(czlowiek_2.oblicz_moja_date_urodzenia())
print("=========zmienne obiektow ==================")
print(id(czlowiek_1.ilosc_lat))
print(id(czlowiek_2.ilosc_lat))
print(id(czlowiek_1.plec))
print(id(czlowiek_2.plec))
print("=============metody obiektow=================")
print(id(czlowiek_1.oblicz_moja_date_urodzenia))
print(id(czlowiek_2.oblicz_moja_date_urodzenia))
print("============metody klasowe=================")
print(id(czlowiek_1.zmien_plec))
print(id(czlowiek_2.zmien_plec))

print("============metody statyczne=================")
print(id(czlowiek_1.przywitaj_sie))
print(id(czlowiek_2.przywitaj_sie))

czlowiek_1.zmien_plec("kobieta")
print(czlowiek_2.plec)