def funkcja_kwadratowa(numer):
    return numer ** 2


def dodaj(a, b):
    return a + b

print(funkcja_kwadratowa(5))
print(funkcja_kwadratowa(10))
print(funkcja_kwadratowa(20))
print(dodaj(2, 2))
print(dodaj(2, 3))
print(dodaj(2, 4))
print(dodaj(2, 6))

funkcja_kwadratowa_lambda = lambda numer: numer ** 2


# nazwa funkcji = LAMBDA argumenty funkcji: wyrazenie, ktore zwracamy
print(funkcja_kwadratowa_lambda(5))
print(funkcja_kwadratowa_lambda(10))
print(funkcja_kwadratowa_lambda(20))

funkcja_dzielenie = lambda numer: numer/2
funkcja_dodawania_lambda = lambda a, b: a + b

print(funkcja_dodawania_lambda(1,2))
print(funkcja_dodawania_lambda(1,10))
print(funkcja_dzielenie(10))
print(funkcja_dzielenie(12))

