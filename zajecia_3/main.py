# print("Witaj w naszej żabce NANO! ")
# produkt = input("Podaj mi swój produkt ")
# print(produkt)
# produkt = produkt.lower()
# produtk_wymaga_sprawdzenia = False
# # if produkt in ["alkohol", "papierosy", "energetyk"]
# if produkt == "alkohol" or produkt == "papierosy" or produkt == "energetyk":
#     produtk_wymaga_sprawdzenia = True
#     wiek = int(input("Podaj mi swój wiek "))
#     if wiek < 18:
#         print("Niestety nie możesz kupić alkoholu!")
#     else:
#         print(f"Hura kupiłeś {produkt}")  # operacja zakupu towaru
#     print(wiek)
#     print(type(wiek))
# if not produtk_wymaga_sprawdzenia:
#     print(f"Hura kupiłeś {produkt}")  # operacja zakupu towaru


# wiek = int(input("Podaj mi swój wiek: "))
# if wiek <= 21:
#     print("Powinieneś się uczyć")
# elif 21 < wiek <= 65:
#     print("Powinieneś pracować!")
# else:
#     print("Powinieneś już odpoczywać na emeryturze!")

#
# wiek = int(input("Podaj mi swój wiek: ")) #14
# #while <warunek, który musi być prawdziwy>:
#     #blok kodu, który będzie wykonywany
# while wiek <= 18:
#     print("Nie masz jeszcze 18 lat!")
#     print(wiek)
#     wiek += 1 #wiek = wiek + 1 # 14 -> 15
# print("Hura jesteś już pełnoletni/a! Możesz kupić piwo/wino. ")
#
# wyraz = input("Podaj wyraz do przeliterowania: ")
# #for <zmienna lokalna> in <struktura iterowalna>
# for litera in wyraz:
#     print(litera)
#
# wiek = int(input("Podaj mi swój wiek: "))
# for rok in range(wiek):
#     print(rok)

# print("Witaj w naszej żabce NANO! ")
# koniec_artykulow = False
# while not koniec_artykulow:
#     produkt = input("Podaj mi swój produkt ")
#     if produkt == "":
#         koniec_artykulow = True
#         print("Koniec zakupów")
#         break
#     elif produkt == "opony":
#         print("nie mamy takiego produktu")
#         continue
#     elif produkt == "płyn do spryskiwaczy":
#         pass
#         # nie mamy tego, ale niedługo będzie
#     print(produkt)
#     produkt = produkt.lower()
#     produtk_wymaga_sprawdzenia = False
#     # if produkt in ["alkohol", "papierosy", "energetyk"]
#     if produkt == "alkohol" or produkt == "papierosy" or produkt == "energetyk":
#         produtk_wymaga_sprawdzenia = True
#         wiek = int(input("Podaj mi swój wiek "))
#         if wiek < 18:
#             print("Niestety nie możesz kupić tego produktu!")
#         else:
#             print(f"Hura kupiłeś {produkt}")  # operacja zakupu towaru
#         print(wiek)
#         print(type(wiek))
#     if not produtk_wymaga_sprawdzenia:
#         print(f"Hura kupiłeś {produkt}")  # operacja zakupu towaru

# lista_uczniow = ["Adam", "Juliusz", "Bartek", "Tomek"]
# for uczen in lista_uczniow:
#     if uczen == "Juliusz":
#         print("Twoj wynik to 70%")
#         break
#     print(uczen)

wyplata = int(input("Podaj mi swoją wypłatę: "))
# if wyplata < 2000:
#     print("Zus wynosi 200 zł")
# elif 2000 <= wyplata < 4000:
#     print("Zus wynosi 400 zł")
# else:
#     print("Zus wynosi 600 zł")
match wyplata:
    case 2000:
        print("Zus wynosi 200 zł")
    case 2500:
        print("Zus wynosi 300 zł")
    case 3000:
        print("Zus wynosi 400 zł")
    case _:
        print("Zus wynosi X zł")


plec = input("Podaj swoja plec")

match plec:
    case "mezczyzna":
        print("Jestes mezczyzna")
    case "kobieta":
        print("Jestes kobieta")
    case _:
        print("Niestety nie mamy takiej plci u nas w systemie")
