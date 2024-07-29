class KontoBankowe:
    def __init__(self, haslo, saldo):
        self.__haslo = haslo #zmienna prywatna
        self._saldo = saldo #zmienna protected

    def wyplata(self, kwota):
        if self._saldo - kwota > 0:
            self._saldo -= kwota
        else:
            print("nie mozesz wyplacic tylu pieniedzy")

    def wplata(self, kwota):
        self._saldo += kwota

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, new_saldo):
        self._saldo = new_saldo

konto_bankowe = KontoBankowe("123", 2000)
konto_bankowe.__haslo = 1000
print(konto_bankowe.__haslo)
print(konto_bankowe._saldo)
# zmienne prywatne (przyklad para Java)
# private int saldo = 2000
# protected int saldo = 2000