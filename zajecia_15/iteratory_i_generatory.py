# from collections.abc import Iterable
#
# numbers = [1, 2, 3, 4]
#
# for number in numbers:
#     print(number)
#
#
# class Uczen:
#     def __init__(self, imie, nazwisko, wiek, plec):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.wiek = wiek
#         self.plec = plec
#
#     def __iter__(self):
#         return iter([self.imie, self.nazwisko, self.wiek, self.plec])
#
#
# uczennica_ania = Uczen("Ania", "Nowak", 12, "kobieta")
#
# for wlasciwosc in uczennica_ania:
#     print(wlasciwosc)
#
# for wlasciwosc in uczennica_ania:
#     print(wlasciwosc)
#
#
# print(isinstance(numbers, Iterable))
# print(isinstance(uczennica_ania, Iterable))


# def generator():
#     yield 1
#     print("pierwsze skonczone zaczynam drugie")
#     yield 2
#     print("drugie skonczone zaczynam trzecie")
#     yield 3
#     yield 4
#
# temp_gen = generator()
# print(next(temp_gen))
# print(next(temp_gen))
# print(next(temp_gen))
# print(next(temp_gen))
# print(next(temp_gen))
#
#
# def show_users(users):
#     for user in users:
#         return user
#
#
# def show_users_generator(users):
#     for user in users:
#         yield user
#
# for user in show_users(["Michal", "Adam", "Tomek", "Roman"]):
#     print(user)
#
# print(show_users(["Michal", "Adam", "Tomek", "Roman"]))
# print(show_users(["Michal", "Adam", "Tomek", "Roman"]))
# print(show_users(["Michal", "Adam", "Tomek", "Roman"]))
# print(show_users(["Michal", "Adam", "Tomek", "Roman"]))
# print(show_users(["Michal", "Adam", "Tomek", "Roman"]))
# print(show_users(["Michal", "Adam", "Tomek", "Roman"]))
# print(show_users(["Michal", "Adam", "Tomek", "Roman"]))
# print(show_users(["Michal", "Adam", "Tomek", "Roman"]))
#
#
# generator = show_users_generator(["Michal", "Adam", "Tomek", "Roman"])
# print(type(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# for user in show_users_generator(["Michal", "Adam", "Tomek", "Roman"]):
#     print(user)
from pympler.asizeof import asizeof
list_comprehension = [x**2 for x in range(1000000)]
generator_expression = (x**2 for x in range(1000000))

print(asizeof(list_comprehension))
print(asizeof(generator_expression))
#
# print(list_comprehension)
# print(generator_expression)
# for number in generator_expression:
#     print(number)