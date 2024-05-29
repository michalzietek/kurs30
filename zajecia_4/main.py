'''
Napisz program do organizacji przetrzymywania dokumentów w szafkach. Po uruchomieniu, aplikacja pyta, ile chcesz dodać dokumentów, a następnie wymaga podania liczby stron dla każdego z nich.
Na koniec działania program powinien wyświetlić w podsumowaniu:
1. Liczbę dokumentów dodanych.
2. Łączną liczbę stron.
3. Suma niewykorzystanych miejsc w szafkach. Liczba szafek * 100 - łączna liczba stron.
4. Która szafka miała najwięcej niewykorzystanych miejsc, jaki to był wynik.
Restrykcje:
• Liczba stron dokumentów musi być z przedziału od 1 do 30 stron.
• Każda szafka może maksymalnie pomieścić 100 stron.
• W przypadku, jeżeli dodawany dokument przekroczy miejsce w szafce, ma zostać umieszczony w nowej szafce, a obecna zostaje zamknięta.
• W przypadku podania liczby stron mniejszej od 1 lub większej od 30, dodawanie dokumentów zostaje zakończone i wszystkie szafki są zamknięte. Wyświetlane jest podsumowanie.
Dane wejsciowe od uzytkownika:
-ilosc dokumentow - pierwszy input od uzytkownika
-ilosc stron w kazdym dokumencie - uzaleznic to od ilosci dokumentow (petla for)
'''
print("Witaj w naszym programie do segregowania dokumentów")
ilosc_dokumentow = int(input("Podaj proszę ile dokumentów chcesz posegregować (podaj wartość liczbową): "))
suma_stron = 0
ilosc_szafek = 1
pojemnosc_szafki = 100
pojemnosc_obecnej_szafki = 0
maksymalne_wolne_miejsce = 0
numer_szafki_z_maksymalnym_pustym_miejscem = 1
ilosc_dodanych_dokumentow = 0
for dokument in range(ilosc_dokumentow):
    ilosc_stron = int(input("Podaj ilość stron dokumentu: "))
    if 1 <=ilosc_stron <= 30:
        ilosc_dodanych_dokumentow += 1
        suma_stron += ilosc_stron
        if ilosc_stron + pojemnosc_obecnej_szafki > pojemnosc_szafki:
            if pojemnosc_szafki - pojemnosc_obecnej_szafki > maksymalne_wolne_miejsce:
                maksymalne_wolne_miejsce = pojemnosc_szafki - pojemnosc_obecnej_szafki
                numer_szafki_z_maksymalnym_pustym_miejscem = ilosc_szafek
            ilosc_szafek += 1
            pojemnosc_obecnej_szafki = ilosc_stron
        else:
            pojemnosc_obecnej_szafki += ilosc_stron
    else:
        print("Ilość stron nie mieści się w zakresie wymaganym (1-30)")
        break
    #suma_stron = suma_stron + ilosc_stron
if pojemnosc_szafki - pojemnosc_obecnej_szafki > maksymalne_wolne_miejsce:
    maksymalne_wolne_miejsce = pojemnosc_szafki - pojemnosc_obecnej_szafki
    numer_szafki_z_maksymalnym_pustym_miejscem = ilosc_szafek
print(f"Ilość dodanych dokumentów to {ilosc_dodanych_dokumentow}")
print(f"Suma stron dokumentów to: {suma_stron}")
print(f"Suma szafek to: {ilosc_szafek}")
print(f"Suma wolnych miejsc w szafkach to: {ilosc_szafek * pojemnosc_szafki - suma_stron}")
print(f"Najwięcej wolnego miejsca w szafce to: {maksymalne_wolne_miejsce}, nr szafki: {numer_szafki_z_maksymalnym_pustym_miejscem}")