def say_hello():
    print("witamy w Pythonie")
    return "zwracana wartosc"


# say_hello()
# wynik_funkcji_say_hello = say_hello()
# print(type(wynik_funkcji_say_hello))
# print(wynik_funkcji_say_hello)
#
# funkcja_say_hello = say_hello
# print(funkcja_say_hello)
# print(type(funkcja_say_hello))
# funkcja_say_hello()

def wyswietl_jakis_tekst_i_przywitaj_sie(tekst):
    print(tekst)
    say_hello()

#
# wyswietl_jakis_tekst_i_przywitaj_sie("To będzie bardzo ciekawa lekcja.")
#
# def wyswietl_tekst_i_wywolaj_jakas_funkcje(funkcja):
#     print("Co za glupota o co tu w ogole chodzi?")
#     funkcja("ciekawostka")
#
# wyswietl_tekst_i_wywolaj_jakas_funkcje(wyswietl_jakis_tekst_i_przywitaj_sie)

def dekorator(funkcja):
    def opakowacz():
        print("Instrukcje przed wywoalniem funkcji")
        funkcja()
        print("Instrukcje po wywołaniu funkcji")
    return opakowacz


@dekorator
def przywitaj_sie():
    print("Ale jaja sie wywołały")


#przywitaj_sie()

def sprawdz_zalogowanie(uzytkownik):
    print("Sprawdzam czy uzytkownik jest zalogowany")
    return False


def sprawdz_zalogowanie_dekorator(funkcja):
    def wrapper(*args, **kwargs):
        print("Sprawdzam czy uzytkownik jest zalogowany")
        funkcja(*args, **kwargs)
        return True
    return wrapper

@sprawdz_zalogowanie_dekorator
def zrob_przelew(uzytkownik):
    print(f"robie przelew {uzytkownik}")


zrob_przelew("Michał")