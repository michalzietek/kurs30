#TODO stworz 2 funkcje odpowiadajace za wczytanie z pliku i zapisanie do pliku

imie = input("Podaj imię osoby obchodzącej urodziny: ")
rok = input("Podaj rocznik urodzin: ")
autor = input("Podaj swoje imię: ")

#templatka = wczytaj_templatke()
wypelniona_templatka = templatka.format(imie=imie, rok=rok, autor=autor)

nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
#zapisz_zyczenia(nazwa_pliku, wypelniona_templatka)
print(f"Uzupełniona kartka urodzinowa została zapisana w pliku: {nazwa_pliku}")