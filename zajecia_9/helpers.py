from classes import Pasazer

def wyszukaj_pasazerow_lotu_po_numerze(numer_lotu, lista_wszystkich_pasazerow):
    lista_pasazerow_lotu = []
    for pasazer in lista_wszystkich_pasazerow:
        if pasazer.numer_lotu == numer_lotu:
            lista_pasazerow_lotu.append(pasazer)
    return lista_pasazerow_lotu

def wyszukaj_pasazera_po_imieniu_i_nazwisku(imie, nazwisko, lista_wszystkich_pasazerow):
    for pasazer in lista_wszystkich_pasazerow:
        if pasazer.imie == imie and pasazer.nazwisko == nazwisko:
            return pasazer.numer_lotu

def wyszukaj_linie_lotnicza_po_numerze_lotu(numer_lotu, lista_linii):
    for linia_lotnicza in lista_linii:
        if numer_lotu in linia_lotnicza.lista_lotow:
            return linia_lotnicza.nazwa


def wyszukaj_liste_lotow_linii_lotniczej(nazwa_linii, lista_linii):
    for linia_lotnicza in lista_linii:
        if nazwa_linii == linia_lotnicza.nazwa:
            return linia_lotnicza.lista_lotow

def wyszukaj_numer_lotu_stewardessy(imie, nazwisko, lista_stewardess):
    for stewardessa in lista_stewardess:
        if stewardessa.imie == imie and stewardessa.nazwisko == nazwisko:
            return stewardessa.numer_lotu


stala = "Aaaaa"