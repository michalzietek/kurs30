import csv

def load_data(file):
    with open(file) as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            print(row)
            data.append(row)
        return data

def save_data(new_file, data):
    with open(new_file, mode="w+") as file:
        writer = csv.writer(file)
        writer.writerows(data)

dane = load_data("test.csv")
save_data("nowy_test.csv", dane)