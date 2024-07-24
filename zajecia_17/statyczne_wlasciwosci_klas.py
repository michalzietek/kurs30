class Czlowiek:

    wiek = 30
    plec = "mezczyzna"
    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return f"Czlowiek o imieniu: {self.imie}"

    def zmien_wiek(self, nowy_wiek):
        self.wiek = nowy_wiek

czlowiek_1 = Czlowiek(imie="Adam")
czlowiek_2 = Czlowiek(imie="Ewa")
print(czlowiek_1)
print(czlowiek_2)
czlowiek_1.imie = "Andrzej"
print(czlowiek_1)
print(czlowiek_2)
print(czlowiek_2.plec)
print(czlowiek_1.plec)
print("========================wiek===================")
print(czlowiek_1.wiek)
print(czlowiek_1.wiek)
# czlowiek_1.zmien_wiek(25)
Czlowiek.wiek = 28
print(czlowiek_1.wiek)
print(czlowiek_2.wiek)
print(Czlowiek.wiek)
