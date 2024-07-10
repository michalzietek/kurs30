import pycountry

country = input("Podaj mi kraj, którego kod chcesz dostać: ")
print(pycountry.countries.get(name=country).alpha_2)
q