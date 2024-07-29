class Silnik:
    def uruchom(self):
        print("uruchamiam silnik")


class Samochod:
    def __init__(self, marka, model, kolor, silnik):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.silnik = silnik


    def uruchom_samochod(self):
        self.silnik.uruchom()


silnik_1_9 = Silnik()
audi = Samochod("audi", "a3", "czarny", silnik_1_9)
audi.uruchom_samochod()
