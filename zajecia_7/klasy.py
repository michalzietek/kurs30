auto = {
    "marka": "Fiat",
    "model": "Bravo",
    "rok": 2003,
    "kolor": "czerwony",
    "silnik": "100hp",
    "ilosc_paliwa": 10,
    "pojemnosc_baku": 50
}
# print(auto.get("marka"))
# print(auto["marka"])

auto["ilosc_paliwa"] = 30

class Auto:
    def __init__(self, marka_auta, model_auta, rok_auta, kolor_auta, moc_silnika, ilosc_paliwa_pojazdu, pojemnosc):
        self.marka = marka_auta
        self.model = model_auta
        self.rok = rok_auta
        self.kolor = kolor_auta
        self.moc = moc_silnika
        self.ilosc_paliwa = ilosc_paliwa_pojazdu
        self.pojemnosc_baku = pojemnosc
        print("hura zbudowales auto")

    def uzupelnij_bak_paliwa(self, ilosc_paliwa_wlanego):
        if self.ilosc_paliwa + ilosc_paliwa_wlanego > self.pojemnosc_baku:
            print("Nie mozesz zatankowac az takiej ilosci")
        else:
            self.ilosc_paliwa += ilosc_paliwa_wlanego

    def __repr__(self):
        return f"Auto marki: {self.marka} model: {self.model} rok: {self.rok}"


fiat_bravo = Auto(
    marka_auta="fiat",
    model_auta="bravo",
    rok_auta=2003,
    kolor_auta="czerwony",
    moc_silnika="100hp",
    ilosc_paliwa_pojazdu=10,
    pojemnosc=50
)

mercedes_glc = Auto(
    marka_auta="Mercedes",
    model_auta="GLC",
    rok_auta=2024,
    kolor_auta="czarny",
    moc_silnika="300hp",
    ilosc_paliwa_pojazdu=20,
    pojemnosc=60
)

print(fiat_bravo.model)
print(mercedes_glc.ilosc_paliwa)
fiat_bravo.uzupelnij_bak_paliwa(ilosc_paliwa_wlanego=38)
mercedes_glc.uzupelnij_bak_paliwa(ilosc_paliwa_wlanego=100)
print(fiat_bravo.ilosc_paliwa)
print(mercedes_glc.ilosc_paliwa)
print(fiat_bravo)
print(mercedes_glc)
