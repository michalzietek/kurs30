# try:
#     wiek = int(input("Podaj swoj wiek"))
# except ValueError:
#     print("Nie jesteś wartością numeryczną")
# finally:
#     print("zamykamy połączenie")


lista_gosci = ["Adam", "Ewa", "Marta"]

try:
    numer_goscia = input("Podaj numer swojego gościa na liście")
    print(f"Twój gość to {lista_gosci[int(numer_goscia)]}")
    wiek_goscia = input("Podaj wiek swojego gościa: ")
    if int(wiek_goscia) >= 18:
        print(f"Gość {lista_gosci[int(numer_goscia)]} może wejść na imprezę")
    else:
        print("Gość nie może wejść na imprezę")
# except ValueError:
#     print("To nie jest wartość numeryczna")
# except IndexError:
#     print("Nie ma takiego numeru gościa na liście")
except (ValueError, IndexError):
    print("Coś poszło nie tak")
finally:
    print("Przejdź do kolejnego gościa")