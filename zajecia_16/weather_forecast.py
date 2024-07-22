import json

class WeatherForecast:

    def __init__(self, file):
        self.file = file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            return json.loads(file.read())

    def save_data_to_file(self):
        with open(self.file, mode="w") as file:
            file.write(json.dumps(self.data))

    def __getitem__(self, item):
        # rozpakowywanie tupli - jednoznaczne z kodem ponizej
        # item_city, item_date = item
        item_city = item[0]
        item_date = item[1]
        for city, info in self.data.items():
            if city == item_city:
                for date, weather_conditions in info.items():
                    if date == item_date:
                        return weather_conditions
        # return self.data.get(item)

    def __setitem__(self, key, value):
        key_city = key[0]
        key_date = key[1]
        if not self.data.get(key_city):
            self.data[key_city] = {}
        self.data[key_city][key_date] = value

weather_forecast = WeatherForecast(file="weather_data.json")
print(weather_forecast.data)

print(weather_forecast["Wroclaw", "2024-07-10"])

weather_forecast["Stargard", "2024-07-17"] = "Nie pada"
weather_forecast.save_data_to_file()




# slownik = {
#   "Wroclaw": {
#     "2024-07-10": "Nie pada",
#     "2024-07-12": "Pada"
#   },
#   "Poznan": {
#     "2024-07-11": "Pada"
#   }
# }
# print(slownik["Wroclaw"]["2024-07-10"])
#
# matrix = [[0, 1, 2],
#           [3, 4, 5],
#           [6, 7, 8]]
#
# slownik["pierwszy_klucz"]["drugi_klucz"]