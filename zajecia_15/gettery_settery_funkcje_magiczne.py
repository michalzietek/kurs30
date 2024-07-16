# wiek = input("Podaj swoj wiek: ")
# print(type(wiek))
# print(type(int(wiek)))
# print(int(16.8))

class Uczen:
    def __init__(self, imie, nazwisko, wiek, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.plec = plec

    def __repr__(self):
        return f"Uczeń {self.imie} {self.nazwisko}"

    def __int__(self):
        return self.wiek

    def __float__(self):
        return float(self.wiek)

    def __bool__(self):
        # if self.plec == "mezczyzna":
        #     return False
        # return True
        return False if self.plec == "mezczyzna" else True

    def __str__(self):
        return f"Uczeń stringowy {self.imie} {self.nazwisko}"

uczen_1 = Uczen(imie="Michal", nazwisko="Nowak", wiek=12, plec="mezczyzna")
# print(uczen_1)
# print(int(uczen_1))
# print(float(uczen_1))
#print(bool(uczen_1))


class Szkola:
    def __init__(self, nazwa):
        self.szkola = {"uczniowie": [uczen_1, Uczen(imie="Maciej", nazwisko="Zak", wiek=11, plec="mezczyzna"),
                          Uczen(imie="Joanna", nazwisko="Kowalska", wiek=8, plec="kobieta")]}

        self.nazwa = nazwa

    def __setitem__(self, key, value):
        if key == "uczniowie":
            self.szkola[key].append(value)
        else:
            self.szkola[key] = value

    def __getitem__(self, item):
        return self.szkola.get(item)



szkola_1 = {"uczniowie": [uczen_1, Uczen(imie="Maciej", nazwisko="Zak", wiek=11, plec="mezczyzna"),
                          Uczen(imie="Joanna", nazwisko="Kowalska", wiek=8, plec="kobieta")]}

szkola_1["uczniowie"].append(Uczen("Mateusz", "Palto", 15, "mezczyzna"))
szkola_1["nauczyciel"] = "Maria Kowalska"
print(szkola_1.get("nauczyciel"))
print(szkola_1["nauczyciel"])

szkola_podstawowa = Szkola(nazwa="Szkola podstawowa nr 1")
szkola_podstawowa.szkola["uczniowie"].append(Uczen("Maria", "Bąk", 10, "kobieta"))
szkola_podstawowa["uczniowie"] = Uczen("Mateusz", "Palto", 15, "mezczyzna")
szkola_podstawowa["nauczyciel"] = "Maria Kowalska"
szkola_podstawowa["dyrektor"] = "Jan Ziobro"
print(szkola_podstawowa["dyrektor"])
print(szkola_podstawowa["uczniowie"])
print(szkola_podstawowa.szkola)
