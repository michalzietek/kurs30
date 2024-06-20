from datetime import datetime

#TODO stworz 2 funkcje odpowiadajace za wczytanie z pliku i zapisanie do pliku
def wczytaj_templatke():
    with open("kartka_template.txt", mode="r") as plik:
        return plik.read()

def zapisz_zyczenia(nazwa, wypelnione_dane):
    with open(nazwa, mode="w") as plik:
        plik.write(wypelnione_dane)


imie = input("Podaj imię osoby obchodzącej urodziny: ")
rok = input("Podaj rocznik urodzin: ")
autor = input("Podaj swoje imię: ")
wiek = datetime.now().year - int(rok)
templatka = wczytaj_templatke()
wypelniona_templatka = templatka.format(imie=imie, rok=wiek, autor=autor)

nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
zapisz_zyczenia(nazwa_pliku, wypelniona_templatka)
print(f"Uzupełniona kartka urodzinowa została zapisana w pliku: {nazwa_pliku}")