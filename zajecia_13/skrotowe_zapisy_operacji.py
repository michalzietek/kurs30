import random

# age = int(input("Podaj swój wiek: "))
# if age >= 18:
#     is_adult = True
# else:
#     is_adult = False
#
# is_adult_v_2 = True if age >= 18 else False
# # tzw szyk przestawny
# # nazwa_zmiennej = pierwsza_wartosc instrukcja warunkowa druga wartosc
#
# wyplata = float(input("Podaj swoją wypłatę: "))
#
#
# #Tej instrukcji warunkowej nie jesteśmy w stanie zapisać za pomocą jednej linijki!!!
# #Do zapisu w jednej linijce musimy mieć tylko i wyłącznie 2 opcje do wyboru
#
# if wyplata <= 30000:
#     opodatkowanie = 0
# elif wyplata > 30000 and wyplata < 120000:
#     opodatkowanie = 0.17
# else:
#     opodatkowanie = 0.32
#
# print(is_adult)
# print(is_adult_v_2)

uczniowie = ["Michal", "bartek", 'JaCek', "ANIA", "zoSia"]
poprawieni_uczniowie = []
for uczen in uczniowie:
    poprawieni_uczniowie.append(uczen.capitalize())
print(poprawieni_uczniowie)

poprawieni_uczniowie_v2 = [uczen.capitalize() for uczen in uczniowie]
# nazwa_zmiennej = [<to co chcemy dodac do listy> for zmienna in <obiekt iterowalny(lista, krotka, slownik itp.)]

dziewczyny_w_szkole = []
for uczen in uczniowie:
    if uczen.lower()[-1] == "a":
        dziewczyny_w_szkole.append(uczen.capitalize())

print(dziewczyny_w_szkole)

dziewczyny_w_szkole_2 = [uczen.capitalize() for uczen in uczniowie if uczen.lower()[-1] == "a"]
print(dziewczyny_w_szkole_2)

# kolory = {"zielony", "niebieski", "czerwony"}
# zbior_kolorow = {kolor.capitalize() for kolor in kolory}
# print(zbior_kolorow)
# print(poprawieni_uczniowie_v2)

przedmioty_zosi = ["angielski", "niemiecki", "matematyka", "polski", "biologia", "chemia", "WF"]

oceny_zosi = {}
for przedmiot in przedmioty_zosi:
    oceny_zosi[przedmiot] = random.randint(1, 6)

print(oceny_zosi)
oceny_zosi_v2 = {przedmiot: random.randint(1, 6) for przedmiot, ocena in oceny_zosi.items()}
print(oceny_zosi_v2)
# print(oceny_zosi)

