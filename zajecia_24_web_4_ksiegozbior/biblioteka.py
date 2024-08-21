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
from file_handler import FileHandler

file_handler_instance = FileHandler(data_file="dane.json", history_file="dziennik.json")
data = file_handler_instance.load_data_from_data_file()

dziennik = file_handler_instance.load_history_from_history_file()
saldo_ksiegarni = data.get("saldo")
ksiegozbior = data.get("ksiegozbior")
# kontynuuj_program = True
# print("Witaj w księgarni kursu 30!")
# while kontynuuj_program:
#     opcja_uzytkownika = int(input("Wybierz co chcesz zrobić.\n"
#                                   "1. Doładowanie konta\n"
#                                   "2. Wypożyczenie książki\n"
#                                   "3. Zakup książki\n"
#                                   "4. Bieżący stan\n"
#                                   "5. Zestawienie\n"
#                                   "6. Szczegóły książki\n"
#                                   "7. Dziennik\n"
#                                   "8. Koniec programu\n"))
#     if opcja_uzytkownika == 1:
#         kwota_doladowania = float(input("Podaj proszę kwotę, o jaką chcesz zmienić nasze saldo: "))
#         if -kwota_doladowania > saldo_ksiegarni:
#             print("Niestety nie możesz wypłacić takich środków!")
#             continue
#         saldo_ksiegarni += kwota_doladowania
#         dziennik.append("Dodanie kwoty do salda")
#     elif opcja_uzytkownika == 2:
#         numer_isbn = int(input("Podaj proszę numer ISBN książki: "))
#         znaleziona_ksiazka = False
#         for ksiazka in ksiegozbior:
#             if ksiazka.get("numer_ISBN") == numer_isbn:
#                 znaleziona_ksiazka = True
#                 if ksiazka.get("ilosc_dostepnych_ksiazek") >= 1:
#                     ksiazka["ilosc_dostepnych_ksiazek"] -= 1
#                     saldo_ksiegarni += ksiazka.get("cena_wypozyczenia")
#                     print(f"Gratulacje, wypozyczyles {ksiazka.get('tytul')}")
#                 else:
#                     print("Niestety ta książka jest już wypożyczona. Przyjdź później.")
#         if not znaleziona_ksiazka:
#             print("Niestety nie mamy książki z takim numerem ISBN")
#     elif opcja_uzytkownika == 3:
#         tytul = input("Podaj tytuł książki: ")
#         autor = input("Podaj autora książki: ")
#         rok_wydania = int(input("Podaj rok wydania książki: "))
#         ilosc_stron = int(input("Podaj ilosc stron ksiazki: "))
#         numer_isbn = int(input("Podaj numer ISBN: "))
#         ilosc_ksiazek = int(input("Podaj ilosc ksiazek: "))
#         cena_zakupu = float(input("Podaj koszt jednej ksiazki: "))
#         ksiegozbior.append({
#             "tytul": tytul,
#             "autor": autor,
#             "rok_wydania": rok_wydania,
#             "ilosc_stron": ilosc_stron,
#             "numer_ISBN": numer_isbn,
#             "ilosc_dostepnych_ksiazek": ilosc_ksiazek,
#             "ilosc_ksiazek": ilosc_ksiazek,
#             "cena_wypozyczenia": 10.0,
#             "cena_kary": 50.0
#         })
#         dziennik.append("Zakup książki")
#         saldo_ksiegarni -= ilosc_ksiazek * cena_zakupu
#     elif opcja_uzytkownika == 4:
#         print(f"Saldo księgarni wynosi: {saldo_ksiegarni}")
#     elif opcja_uzytkownika == 5:
#         print(f"Dane twojej księgarni:")
#         for ksiazka in ksiegozbior:
#             print(ksiazka)
#     elif opcja_uzytkownika == 6:
#         numer_isbn = int(input("Podaj proszę numer ISBN książki: "))
#         znaleziona_ksiazka = False
#         for ksiazka in ksiegozbior:
#             if ksiazka.get("numer_ISBN") == numer_isbn:
#                 print(ksiazka)
#                 znaleziona_ksiazka = True
#                 break
#         if not znaleziona_ksiazka:
#             print("Niestety nie mamy książki z takim numerem ISBN")
#     elif opcja_uzytkownika == 7:
#         od = int(input("Podaj poczatkowy zakres historii: "))
#         do = int(input("Podaj koncowy zakres historii: "))
#         print(dziennik[od:do])
#     elif opcja_uzytkownika == 8:
#         kontynuuj_program = False
#     else:
#         print("Niestety nie mamy takiej operacji. ")
# file_handler_instance.save_data_to_data_file(data={
#     "saldo": saldo_ksiegarni,
#     "ksiegozbior": ksiegozbior
# })
# file_handler_instance.save_history_to_history_file(dziennik)
# print("Kończymy na dzisiaj :)")

class AppHandler:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.data = self.file_handler.load_data_from_data_file()
        self.saldo = self.data.get("saldo")
        self.ksiegozbior = self.data.get("ksiegozbior")
        self.dziennik = self.file_handler.load_history_from_history_file()

    def change_saldo(self, price_to_add):
        if -price_to_add > self.saldo:
            return False
        self.saldo += price_to_add
        self.dziennik.append("Dodanie kwoty do salda")
        return True

    def show_history(self, od, do):
        if not od:
            od = 0
        if not do:
            do = len(self.dziennik)
        return self.dziennik[int(od):int(do)]

    def sale_book(self, data):
        numer_isbn = int(data.get("isbn_number"))
        znaleziona_ksiazka = False
        for ksiazka in self.ksiegozbior:
            if ksiazka.get("numer_ISBN") == numer_isbn:
                znaleziona_ksiazka = True
                if ksiazka.get("ilosc_dostepnych_ksiazek") >= 1:
                    ksiazka["ilosc_dostepnych_ksiazek"] -= 1
                    self.saldo += ksiazka.get("cena_wypozyczenia")
                    return True
                else:
                    return False
        if not znaleziona_ksiazka:
            return False

    def buy_books(self, data):
        tytul = data.get("tytul")
        autor = data.get("autor")
        rok_wydania = data.get("rok_wydania")
        ilosc_stron = data.get("ilosc_stron")
        numer_isbn = int(data.get("numer_ISBN"))
        ilosc_ksiazek = int(data.get("ilosc_ksiazek"))
        cena_zakupu = float(data.get("cena_zakupu"))
        self.ksiegozbior.append({
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
        self.dziennik.append("Zakup książki")
        if self.saldo >= ilosc_ksiazek * cena_zakupu:
            self.saldo -= ilosc_ksiazek * cena_zakupu
            return True
        return False

    def save_app_context(self):
        self.file_handler.save_data_to_data_file({
            "ksiegozbior": self.ksiegozbior,
            "saldo": self.saldo
        })
        self.file_handler.save_history_to_history_file(self.dziennik)

app_handler = AppHandler(file_handler_instance)


