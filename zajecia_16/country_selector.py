import json
import requests


class CountrySelector:
    def __init__(self, file):
        self.file = file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            return json.loads(file.read())

    def save_data_to_file(self):
        with open(self.file, mode="w") as file:
            file.write(json.dumps(self.data))

    def add_new_country_to_data(self, country_name, country_data):
        self.data[country_name] = country_data

    def get_data_from_file(self, country_name):
        for key, value in self.data.items():
            if key == country_name:
                return value
        return None

    def retrieve_data_from_api(self, country_name):
        url_address = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
        response = requests.get(url_address)

        if response.status_code == 200:
            print("Hura udało się pobrać!")
            return self.parse_data_from_response_to_valid_dict(response_body=response.json())
        else:
            print("Niestety nie ma takiego kraju. Może polecisz na wakacje do San Escobar z Witoldem Waszczykowskim?")


    def parse_data_from_response_to_valid_dict(self, response_body):
        return {
            "name": response_body[0].get("name").get("common"),
            "capital": response_body[0].get("capital")[0],
            "region": response_body[0].get("region"),
            "subregion": response_body[0].get("subregion"),
            "languages": response_body[0].get("languages"),
            "currency": response_body[0].get("currencies"),
            "flag": response_body[0].get("flag")
        }

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, item):
        info_found_in_file = False
        for country, info in self.data.items():
            if country == item:
                info_found_in_file = True
                return info
        if not info_found_in_file:
            return self.retrieve_data_from_api(item)

    def __iter__(self):
        return iter(self.data)

    def items(self):
        for country, data in self.data.items():
            yield f"{country}: {data}"
