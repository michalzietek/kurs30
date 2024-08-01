from manager import manager


@manager.assign("zmiana_salda")
def zmiana_salda(manager):
    kwota_doladowania = float(input("Podaj proszę kwotę, o jaką chcesz zmienić nasze saldo: "))
    if -kwota_doladowania > manager.saldo_ksiegarni:
        print("Niestety nie możesz wypłacić takich środków!")
    else:
        manager.saldo_ksiegarni += kwota_doladowania
        manager.dziennik.append("Dodanie kwoty do salda")


@manager.assign("sprzedaj_ksiazke")
def sprzedaj_ksiazke(manager):
    numer_isbn = int(input("Podaj proszę numer ISBN książki: "))
    znaleziona_ksiazka = False
    for ksiazka in manager.ksiegozbior:
        if ksiazka.get("numer_ISBN") == numer_isbn:
            znaleziona_ksiazka = True
            if ksiazka.get("ilosc_dostepnych_ksiazek") >= 1:
                ksiazka["ilosc_dostepnych_ksiazek"] -= 1
                manager.saldo_ksiegarni += ksiazka.get("cena_wypozyczenia")
                print(f"Gratulacje, wypozyczyles {ksiazka.get('tytul')}")
            else:
                print("Niestety ta książka jest już wypożyczona. Przyjdź później.")
    if not znaleziona_ksiazka:
        print("Niestety nie mamy książki z takim numerem ISBN")


@manager.assign("kup_ksiazke")
def kup_ksiazke(manager):
    tytul = input("Podaj tytuł książki: ")
    autor = input("Podaj autora książki: ")
    rok_wydania = int(input("Podaj rok wydania książki: "))
    ilosc_stron = int(input("Podaj ilosc stron ksiazki: "))
    numer_isbn = int(input("Podaj numer ISBN: "))
    ilosc_ksiazek = int(input("Podaj ilosc ksiazek: "))
    cena_zakupu = float(input("Podaj koszt jednej ksiazki: "))
    manager.ksiegozbior.append({
        "tytul": tytul,
        "autor": autor,
        "rok_wydania": rok_wydania,
        "ilosc_stron": ilosc_stron,
        "numer_ISBN": numer_isbn,
        "ilosc_dostepnych_ksiazek": ilosc_ksiazek,
        "ilosc_ksiazek": ilosc_ksiazek,
        "cena_wypozyczenia": 10.0,
        "cena_kary": 50.0
    })
    manager.dziennik.append("Zakup książki")
    manager.saldo_ksiegarni -= ilosc_ksiazek * cena_zakupu


@manager.assign("szczegoly")
def podaj_szczegoly_ksiazki(manager):
    numer_isbn = int(input("Podaj proszę numer ISBN książki: "))
    znaleziona_ksiazka = False
    for ksiazka in manager.ksiegozbior:
        if ksiazka.get("numer_ISBN") == numer_isbn:
            print(ksiazka)
            znaleziona_ksiazka = True
            break
    if not znaleziona_ksiazka:
        print("Niestety nie mamy książki z takim numerem ISBN")


kontynuuj_program = True
print("Witaj w księgarni kursu 30!")
while kontynuuj_program:
    opcja_uzytkownika = int(input("Wybierz co chcesz zrobić.\n"
                                  "1. Doładowanie konta\n"
                                  "2. Wypożyczenie książki\n"
                                  "3. Zakup książki\n"
                                  "4. Bieżący stan\n"
                                  "5. Zestawienie\n"
                                  "6. Szczegóły książki\n"
                                  "7. Dziennik\n"
                                  "8. Koniec programu\n"))
    if opcja_uzytkownika == 1:
        manager.execute("zmiana_salda")
    elif opcja_uzytkownika == 2:
        manager.execute("sprzedaj_ksiazke")
    elif opcja_uzytkownika == 3:
        manager.execute("kup_ksiazke")
    elif opcja_uzytkownika == 4:
        print(f"Saldo księgarni wynosi: {manager.saldo_ksiegarni}")
    elif opcja_uzytkownika == 5:
        print(f"Dane twojej księgarni:")
        for ksiazka in manager.ksiegozbior:
            print(ksiazka)
    elif opcja_uzytkownika == 6:
        manager.execute("szczegoly")
    elif opcja_uzytkownika == 7:
        od = int(input("Podaj poczatkowy zakres historii: "))
        do = int(input("Podaj koncowy zakres historii: "))
        print(manager.dziennik[od:do])
    elif opcja_uzytkownika == 8:
        kontynuuj_program = False
    else:
        print("Niestety nie mamy takiej operacji. ")
manager.file_handler.save_data_to_data_file(data={
    "saldo": manager.saldo_ksiegarni,
    "ksiegozbior": manager.ksiegozbior
})
manager.file_handler.save_history_to_history_file(manager.dziennik)
print("Kończymy na dzisiaj :)")