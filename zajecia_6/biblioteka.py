'''
Stwórz system zarządzania księgozbiorem bibliotecznym, który pozwoli na monitorowanie przepływu książek oraz śledzenie budżetu biblioteki.
Po uruchomieniu systemu użytkownik otrzymuje listę komend do wyboru:
- doładowanie
- wypożycz
- zakup
- bieżący_stan
- zestawienie
- szczegóły_książki
- dziennik
- zakończ
Funkcje po wywołaniu danych komend są następujące:
1. doładowanie - Umożliwia dodanie środków do budżetu biblioteki lub ich odjęcie.
2. wypożycz - Rejestruje wypożyczenie książki przez czytelnika. System żąda podania numeru ISBN. Koszt wypożyczenia jest dodawany do budżetu.
3. zakup - Rejestruje zakup nowych książek dla biblioteki. System pyta o tytuł książki, koszt zakupu i liczbę egzemplarzy. Zakupione książki są dodawane do zbioru, a środki są odprowadzane z budżetu, który nie może być negatywny po transakcji.
4. bieżący_stan - Wyświetla aktualny stan środków finansowych.
5. zestawienie - Podsumowuje cały księgozbiór biblioteki wraz z cenami zakupu i ich ilością.
6. szczegóły_książki - Wyświetla dostępność i dane dotyczące pojedynczej książki po wpisaniu numeru ISBN.
7. dziennik - Przegląd historii transakcji. Podając wartości "od" i "do", system wyświetla zapisane działania w podanym zakresie. W przypadku pustych pól lub wartości spoza zakresu, użytkownik jest informowany o błędzie i wyświetlana jest liczba wszystkich zarejestrowanych transakcji.
8. zakończ - Kończy działanie programu.
**Inne wymagania:**
- System działa do momentu wybrania komendy zakończ.
- Operacje doładowanie, wypożycz oraz zakup są zapisywane dla późniejszej referencji przy użyciu komendy dziennik.
- Po każdej komendzie system wyświetla ponownie listę dostępnych opcji i prosi o wybór kolejnej.
- Ochrona przed błędami użytkownika, takimi jak wpisywanie błędnych danych czy żądanie zakupu na wartości ujemne. Powinno być również sprawdzanie poprawności typów danych wprowadzanych przez użytkownika.
'''
dziennik = ["dodano 1000 zł do konta", "wypłacono 1500", "zakupiono 3 ksiązki", "wypożyczono Wiedźmina"]
saldo_ksiegarni = 10000.0
ksiegozbior = [
    {
        "tytul": "Wiedźmin",
        "autor": "Andrzej Sapkowski",
        "rok_wydania": 1999,
        "ilosc_stron": 500,
        "numer_ISBN": 12354656,
        "ilosc_dostepnych_ksiazek": 3,
        "ilosc_ksiazek": 5,
        "cena_wypozyczenia": 10.0,
        "cena_kary": 50.0
    },
    {
        "tytul": "Straż, straż",
        "autor": "Terry Pratchet",
        "rok_wydania": 2020,
        "ilosc_stron": 350,
        "numer_ISBN": 111111111,
        "ilosc_dostepnych_ksiazek": 2,
        "ilosc_ksiazek": 4,
        "cena_wypozyczenia": 10.0,
        "cena_kary": 50.0
    }
]
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
        kwota_doladowania = float(input("Podaj proszę kwotę, o jaką chcesz zmienić nasze saldo: "))
        if -kwota_doladowania > saldo_ksiegarni:
            print("Niestety nie możesz wypłacić takich środków!")
            continue
        saldo_ksiegarni += kwota_doladowania
        dziennik.append("Dodanie kwoty do salda")
    elif opcja_uzytkownika == 2:
        numer_isbn = int(input("Podaj proszę numer ISBN książki: "))
        znaleziona_ksiazka = False
        for ksiazka in ksiegozbior:
            if ksiazka.get("numer_ISBN") == numer_isbn:
                znaleziona_ksiazka = True
                if ksiazka.get("ilosc_dostepnych_ksiazek") >= 1:
                    ksiazka["ilosc_dostepnych_ksiazek"] -= 1
                    saldo_ksiegarni += ksiazka.get("cena_wypozyczenia")
                    print(f"Gratulacje, wypozyczyles {ksiazka.get('tytul')}")
                else:
                    print("Niestety ta książka jest już wypożyczona. Przyjdź później.")
        if not znaleziona_ksiazka:
            print("Niestety nie mamy książki z takim numerem ISBN")
    elif opcja_uzytkownika == 3:
        tytul = input("Podaj tytuł książki: ")
        autor = input("Podaj autora książki: ")
        rok_wydania = int(input("Podaj rok wydania książki: "))
        ilosc_stron = int(input("Podaj ilosc stron ksiazki: "))
        numer_isbn = int(input("Podaj numer ISBN: "))
        ilosc_ksiazek = int(input("Podaj ilosc ksiazek: "))
        cena_zakupu = float(input("Podaj koszt jednej ksiazki: "))
        ksiegozbior.append({
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
        dziennik.append("Zakup książki")
        saldo_ksiegarni -= ilosc_ksiazek * cena_zakupu
    elif opcja_uzytkownika == 4:
        print(f"Saldo księgarni wynosi: {saldo_ksiegarni}")
    elif opcja_uzytkownika == 5:
        print(f"Dane twojej księgarni:")
        for ksiazka in ksiegozbior:
            # print({
            #     "tytul": ksiazka.get("tytul"),
            #     "autor": ksiazka.get("autor"),
            #     "ilosc_dostepnych_ksiazek": ksiazka.get("ilosc_dostepnych_ksiazek")
            # })
            print(ksiazka)
    elif opcja_uzytkownika == 6:
        numer_isbn = int(input("Podaj proszę numer ISBN książki: "))
        znaleziona_ksiazka = False
        for ksiazka in ksiegozbior:
            if ksiazka.get("numer_ISBN") == numer_isbn:
                print(ksiazka)
                znaleziona_ksiazka = True
                break
        if not znaleziona_ksiazka:
            print("Niestety nie mamy książki z takim numerem ISBN")
    elif opcja_uzytkownika == 7:
        od = int(input("Podaj poczatkowy zakres historii: "))
        do = int(input("Podaj koncowy zakres historii: "))
        print(dziennik[od:do])
    elif opcja_uzytkownika == 8:
        kontynuuj_program = False
    else:
        print("Niestety nie mamy takiej operacji. ")
print("Kończymy na dzisiaj :)")
