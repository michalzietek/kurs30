# 1 2 3 4 5 6 7 8 9 10
# 0 1 2 3 4 5 6 7 10 11 12 13 14
# 0 1 2 3 4
# 1101 1100
# 0000 0000
#################################################################
###### LISTY ############
# imie = "Michal"
# wiek = 18
# uczen_1 = "Michal"
# koniec_programu = False
# lista_uczniow = []
# while not koniec_programu:
#     nowy_uczen = input("Podaj imię kolejnego ucznia(Jeśli naciśniesz enter program zakończy działanie): ")
#     if nowy_uczen == "":
#         koniec_programu = True
#     else:
#         #lista_uczniow.append(nowy_uczen)
#         #lista_uczniow.insert(0, nowy_uczen)
# print(lista_uczniow)
# lista_uczniow = ["Adam", "Ewa", "Marek"]
# nowa_lista = list()
# nowa_lista_2 = []
# domyslna_lista = [False, 12, "Maciej", "Beata"]
# lista_wartosci = ["Adam", "Ewa", [12, True, "Maciej"]]
# print(lista_uczniow[0])
# print(lista_uczniow[1])
# print(lista_uczniow[2])
# list_lenght = len(lista_uczniow)
# #print(lista_uczniow[list_lenght])
# #print(lista_uczniow[3])
# for uczen in lista_uczniow:
#     print(uczen)
# print(lista_uczniow)
# print(type(lista_uczniow))
# lista_uczniow.append("Wojciech")
# lista_uczniow.insert(0, "Ania")
# print(lista_uczniow)
# imie = "Michal"
# imie = "Pawel"
# lista_uczniow[0] = "Krzysztof"
# print(imie)
# print(lista_uczniow)
# # lista_uczniow.remove("Adam")
# # del lista_uczniow[1]
# print(lista_uczniow)
# # print(lista_uczniow[list_lenght] -1)
# # print(lista_uczniow[3])
# print(lista_uczniow[-1])
# print(lista_uczniow[-2])
# nowa_lista = lista_uczniow[0:4:2]
# print(nowa_lista)
# for number in range(0, 20, 2):
#     pass

#############################################################
########### KROTKI ###############
# krotka_1 = ("Michal", "Andrzej", "Elzbieta")
# plec = "mezczyzna", "kobieta"
# wiek = 20
# print(wiek)
# print(type(wiek))
# print(plec)
# print(type(plec))
# print(krotka_1)
# print(type(krotka_1))
# print(krotka_1[0])
# print(krotka_1[1])
# print(krotka_1[2])
#krotka_1[0] = 20


###############################################################
########## ZBIORY #######################
# zbior_kolorow = {"niebieski", "czerwony", "zielony", "biały", "czarny"}
# print(zbior_kolorow)
# print(type(zbior_kolorow))
# #print(zbior_kolorow[0])
# print("niebieski" in zbior_kolorow)
# zbior_kolorow.add("seledynowy")
# zbior_kolorow.add("seledynowy")
# zbior_kolorow.remove("niebieski")
# for index, kolor in enumerate(zbior_kolorow):
#     print(kolor)


##################################################################
############### słownik ##################################
imie = "Michał"
nazwisko = "Ziętkowski"
wiek = 28
plec = "mezczyzna"
czlowiek = ["Michal", "Zietkowski", 17, "mezczyzna", None, "Szczecin"]
czlowiek_dict = {
    "imie": "Michal",
    "nazwisko": "Zietkowski",
    "wiek": 28,
    "plec": "mezczyzna",
    "miejsce_zamieszkania": "Szczecin"
}
print(czlowiek_dict)
print(type(czlowiek_dict))
print(czlowiek_dict["imie"])
#print(czlowiek_dict["pesel"])
print(czlowiek_dict.get("pesel", "123456789"))
czlowiek_dict["pesel"] = "0000000000"
print(czlowiek_dict.get("pesel", "123456789"))
czlowiek_dict["pesel"] = "1111111111"
print(czlowiek_dict.get("pesel", "123456789"))
print(czlowiek_dict)
del czlowiek_dict["pesel"]
print(czlowiek_dict)

