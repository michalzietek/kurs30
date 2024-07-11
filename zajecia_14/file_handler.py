import json

class FileHandler:
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
