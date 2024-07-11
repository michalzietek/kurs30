from file_handler import FileHandler
from utils import retrieve_data_from_api


file_handler = FileHandler("data.json")
print(file_handler.data)

country = input("Please pass your country: ")
data_from_file = file_handler.get_data_from_file(country_name=country)
if data_from_file:
    print("Pobralismy dane z pliku")
    print(data_from_file)
else:
    data = retrieve_data_from_api(country)
    file_handler.add_new_country_to_data(country, data)
    file_handler.save_data_to_file()
    print(data)