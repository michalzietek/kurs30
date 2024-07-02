import enum

#dopuszczalne_marki = ["audi", "vw"]


class Marka(enum.Enum):
    AUDI = "AUDI"
    VW = "VW"
    SEAT = "SEAT"
    SKODA = "SKODA"
    PORSCHE = "PORSCHE"
    BUGATTI = "BUGATTI"


print("Witaj w salonie grupy WAG!")
twoje_auto = input("Podaj typ swojego auta: ")
#
# if twoje_auto == Marka.AUDI.value:
#     print("Mozesz przyjechac audi")
# elif twoje_auto == Marka.VW.value:
#     print("Mozesz przychac vw")
# elif twoje_auto == Marka.SEAT.value:
#     print("Mozesz przyjechac Seatem")
# else:
#     print("Niestety nie obslugujemy twojego samochodu!")
