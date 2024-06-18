# plik = open("przywitanie.txt")
# print(type(plik))
# for line in plik:
#     print(line)
# plik.write("Zmieniamy wartości w naszym pliku!")
# plik.close()

# with open("przywitanie.txt", mode="r") as plik:
#     print(type(plik))
#     print(plik.read())
#
# print("Tutaj już zamknąłem nasz context manager")

# tutaj zapisujemy do pliku i czyscimy stare dane
# with open("przywitanie.txt", mode="w") as plik:
#     plik.write("Nowy plik")

# tutaj dopisujemy do pliku
# with open("przywitanie.txt", mode="a") as plik:
#     plik.write("Te dane zostały dopisane")

# tryb, który łączy r i a
with open("przywitanie.txt", mode="r+") as plik:
    print(plik.read())
    plik.write("\nDopisalem drugi raz")
#
# with open("przywitanie2.txt", mode="w+") as plik:
#     print(plik.read())
#     plik.write("Hehehehehe")
#     print(plik.read())

with open("przywitanie4.txt", mode="a+") as plik:
    print(plik.read())
    plik.write("\nDodane dane")