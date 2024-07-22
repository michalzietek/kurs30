from country_selector import CountrySelector


country_selector = CountrySelector("data.json")
# print(country_selector.data)
#
# country = input("Please pass your country: ")
# data_from_file = country_selector.get_data_from_file(country_name=country)
# if data_from_file:
#     print("Pobralismy dane z pliku")
#     print(data_from_file)
# else:
#     data = country_selector.retrieve_data_from_api(country)
#     country_selector.add_new_country_to_data(country, data)
#
#     print(data)

print(country_selector["Poland"])
print(country_selector["Sweden"])
print(country_selector["Canada"])
country_selector["Canada"] = "ebebe"
country_selector.save_data_to_file()


for country in country_selector:
    print(country)

for country_data in country_selector.items():
    print(country_data)