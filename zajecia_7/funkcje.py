lista_uczniow = [
    {
        "imie": "Michal",
        "nazwisko": "Zietkowski",
        "klasa": "1a",
        "zachowanie": "poprawne"
    },
    {
        "imie": "Adam",
        "nazwisko": "Nowak",
        "klasa": "2a",
        "zachowanie": "poprawne"
    }
]


def popros_uzytkownika_o_dane_ucznia():
    imie = input("Podaj imię ucznia")
    nazwisko = input("Podaj nazwisko ucznia")
    klasa = input("Podaj klasę ucznia")
    return imie, nazwisko, klasa


def wyszukaj_ucznia_w_szkole(imie, nazwisko, klasa):
    for uczen in lista_uczniow:
        if uczen.get("imie") == imie and uczen.get("nazwisko") == nazwisko and uczen.get("klasa") == klasa:
            print(uczen)
            return True
    return False


print("Witaj w programie nasza szkoła")
operacja = input("Podaj co chcesz zrobić.\n1. Dodaj ucznia\n2. Wyszukaj ucznia")
if operacja == "1":
    imie, nazwisko, klasa = popros_uzytkownika_o_dane_ucznia()
    znaleziono_ucznia = wyszukaj_ucznia_w_szkole(imie, nazwisko, klasa)
    if not znaleziono_ucznia:
        lista_uczniow.append({
            "imie": imie,
            "nazwisko": nazwisko,
            "klasa": klasa
        })
    else:
        print("Taki uczen istnieje juz w twoim systemie.")
elif operacja == "2":
    imie, nazwisko, klasa = popros_uzytkownika_o_dane_ucznia()
    znaleziono_ucznia = wyszukaj_ucznia_w_szkole(imie, nazwisko, klasa)
    if not znaleziono_ucznia:
        print("Nie mamy takiego ucznia w naszym systemie.")

# def dodanie_dwoch_liczb(pierwsza_liczba, druga_liczba=15):
#     print(f"pierwsza liczba to: {pierwsza_liczba}, druga liczba to {druga_liczba}")
#     print(pierwsza_liczba + druga_liczba)
#
#
# def pierwsza_liczba_wieksza_od_drugiej(pierwsza_liczba, druga_liczba):
#     if pierwsza_liczba > druga_liczba:
#         return True  # jednoznacze z break i zwroc do zmiennej wartosc True
#     return False
#
#
# dodanie_dwoch_liczb(20, 17)
# dodanie_dwoch_liczb(20)
# # dodanie_dwoch_liczb(druga_liczba=20, pierwsza_liczba=12)
# # dodanie_dwoch_liczb(20, 12)
# # dodanie_dwoch_liczb(20, 111)
# # dodanie_dwoch_liczb(20, 10)
# wynik = pierwsza_liczba_wieksza_od_drugiej(20, 15)
# print(wynik)
