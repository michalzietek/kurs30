"""
Jesteś szefem firmy technologicznej tworzącej system zarządzania dla międzynarodowego lotniska. System ten ma obsługiwać dane związane z lotami, liniami lotniczymi, pasażerami oraz stewardessami. Każdy lot może mieć przypisanych wielu pasażerów i jedną stewardessę, natomiast linie lotnicze mogą obsługiwać nieograniczoną liczbę lotów. Celem jest stworzenie programu, który pozwoli na efektywne zarządzanie i dostarczanie właściwych informacji na potrzeby logistyki i obsługi klienta lotniska.

**Program do zarządzania danymi lotów na międzynarodowym lotnisku**
Program powinien umożliwić:
1. Dodanie nowych danych do systemu:
   - Pasażera z przypisanym numerem lotu.
   - Stewardessy z przypisanym numerem lotu.
   - Linii lotniczej, która może obsługiwać wiele różnych lotów.
2. Przeglądanie i zarządzanie istniejącymi informacjami:
   - Pobranie listy pasażerów danego lotu.
   - Znalezienie przypisanej linii lotniczej dla wybranego pasażera.
   - Wyświetlenie listy lotów danej linii lotniczej.
   - Otrzymanie listy wszystkich pasażerów dla lotu, którego stewardessą jest wybrana osoba.
**Polecenia programu**
Po uruchomieniu, program powinien wyświetlić menu z następującymi komendami:
- dodaj - przechodzi do menu dodawania nowych danych.
- przeglądaj - przechodzi do menu przeglądania i zarządzania danymi.
- zakończ - kończy działanie programu.
**Menu dodawania danych (dodaj):**
Użytkownik może wybrać:
- pasażer - dodanie pasażera wymaga wprowadzenia imienia i nazwiska, numeru lotu.
- stewardessa - dodanie stewardessy wymaga wprowadzenia imienia i nazwiska, numeru lotu, do którego jest przypisana.
- linia_lotnicza - dodanie linii lotniczej wymaga wprowadzenia jej nazwy.
- zakończ_dodawanie - powrót do głównego menu.
**Menu przeglądania i zarządzania danymi (przeglądaj):**
Użytkownik może wybrać:
- lot - wprowadzenie numeru lotu wyświetla listę pasażerów tego lotu.
- pasażer - wprowadzenie imienia i nazwiska pasażera wyświetla nazwę linii lotniczej.
- linia_lotnicza - wprowadzenie nazwy linii lotniczej wyświetla listę lotów obsługiwanych przez linię.
- stewardessa - wprowadzenie imienia i nazwiska stewardessy wyświetla listę pasażerów jej lotu.
- zakończ_przeglądanie - powrót do głównego menu.
**Zakończenie pracy programu**
Polecenie zakończ powoduje zamknięcie aplikacji.
"""

#import helpers  #tozsame z from helpers import *
from helpers import (
    wyszukaj_pasazerow_lotu_po_numerze,
    wyszukaj_linie_lotnicza_po_numerze_lotu,
    wyszukaj_numer_lotu_stewardessy,
    wyszukaj_liste_lotow_linii_lotniczej,
    wyszukaj_pasazera_po_imieniu_i_nazwisku
)

from zajecia_9.classes import Pasazer, Stewardessa, LiniaLotnicza

lotnisko = {
    "pasazerowie": [Pasazer("Michal", "Zietkowski", "LOT123"), Pasazer("Marcin", "Nowak", "LOT123"), Pasazer("Artur", "Szpilka", "FLE1234")],
    "stewardessy": [Stewardessa("Anna", "Nowak", "LOT123"), Stewardessa("Jacek", "Kowalski", "FLE1234")],
    "linie_lotnicze": [LiniaLotnicza("LOT", ["LOT123", "LOT1234"]), LiniaLotnicza("Fly Emirates", ["FLE1234"])]
}

koniec_programu = False
print("Witaj w programie do obsługi lotniska Warszawa Chopina!")
while not koniec_programu:
    wybor_uzytkownika = input("Podaj co chcesz zrobić. \n"
                              "1. Utwórz\n"
                              "2. Zarządzaj\n"
                              "3. Zakończ\n")
    if wybor_uzytkownika == "1":
        opcja_do_dodania = input("Co chcesz dodać?\n"
                                 "1. Pasażer\n"
                                 "2. Stewardessa\n"
                                 "3. Linia lotnicza\n")
        if opcja_do_dodania == "1":
            imie = input("Podaj imie pasazera")
            nazwisko = input("Podaj nazwisko pasazera")
            numer_lotu = input("Podaj numer lotu pasazera")
            lotnisko["pasazerowie"].append(Pasazer(imie, nazwisko, numer_lotu))
        elif opcja_do_dodania == "2":
            imie = input("Podaj imie stewardessy: ")
            nazwisko = input("Podaj nazwisko stewardessy: ")
            numer_lotu = input("Podaj numer lotu stewardessy: ")
            lotnisko["stewardessy"].append(Stewardessa(imie, nazwisko, numer_lotu))
        elif opcja_do_dodania == "3":
            nazwa_linii = input("Podaj nazwe linii")
            lista_lotow = []
            nowy_lot = True
            while nowy_lot:
                lot = input("Podaj kolejny lot: ")
                if lot:
                    lista_lotow.append(lot)
                else:
                    nowy_lot = False
            lotnisko["linie_lotnicze"].append(LiniaLotnicza(nazwa_linii, lista_lotow))
    elif wybor_uzytkownika == "2":
        opcja_do_wyboru = input("Co chcesz zrobić?\n"
                                "1. Sprawdź pasażerów lotu\n"
                                "2. Sprawdź jaką linią lotniczą lecisz\n"
                                "3. Sprawdź listę lotów danej linii\n"
                                "4. Sprawdź pasażerów stewardessy\n")
        if opcja_do_wyboru == "1":
            numer_lotu = input("Podaj numer lotu jakim lecisz")
            print(wyszukaj_pasazerow_lotu_po_numerze(numer_lotu, lotnisko.get("pasazerowie")))
        elif opcja_do_wyboru == "2":
            imie_pasazera = input("Podaj imie pasazera: ")
            nazwisko_pasazera = input("Podaj nazwisko pasazera: ")
            #1. Wyszukanie lotu pasazera po liscie pasazerow
            numer_lotu = wyszukaj_pasazera_po_imieniu_i_nazwisku(imie_pasazera, nazwisko_pasazera, lotnisko.get("pasazerowie"))
            if numer_lotu:
                #2 Wyszukanie nazwy liniii lotniczej po numerze lotu
                linia = wyszukaj_linie_lotnicza_po_numerze_lotu(numer_lotu, lotnisko.get("linie_lotnicze"))
                if linia:
                    print(linia)
                else:
                    print("Ten numer lotu nie ma przypisanej linii lotniczej! ERRRRROR")
            else:
                print("Nie mamy takiego pasażera!")
        elif opcja_do_wyboru == "3":
            nazwa_linii = input("Podaj nazwę linii lotniczej: ")
            print(wyszukaj_liste_lotow_linii_lotniczej(nazwa_linii, lotnisko.get("linie_lotnicze")))
        elif opcja_do_wyboru == "4":
            imie_stewardessy = input("Podaj imie stewardessy: ")
            nazwisko_stewardessy = input("Podaj nazwisko stewardessy: ")
            #1. wyszukanie numeru lotu stewardessy
            numer_lotu = wyszukaj_numer_lotu_stewardessy(imie_stewardessy, nazwisko_stewardessy, lotnisko.get("stewardessy"))
            if numer_lotu:
                # 2. Wyszukanie listy pasazerow po numerze lotu
                print(wyszukaj_pasazerow_lotu_po_numerze(numer_lotu, lotnisko.get("pasazerowie")))
    elif wybor_uzytkownika == "3":
        koniec_programu = True