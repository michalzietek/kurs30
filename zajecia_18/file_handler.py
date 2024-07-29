import csv
import pickle
from abc import ABC, abstractmethod



class FileHandler(ABC):
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.matrix = None
        self.changes = changes

    @abstractmethod
    def load_data_from_file(self):
        pass

    @abstractmethod
    def save_data_to_file(self):
        pass

    def transform(self):
        for transformation in self.changes:
            transformation_list = transformation.split(",")
            print(transformation_list)
            operation_type = transformation_list[0]
            vector = transformation_list[1]
            index = int(transformation_list[2])
            number = int(transformation_list[3])
            if operation_type == "add" and vector == "row":
                self.add_row(index, number)
            elif operation_type == "add" and vector == "col":
                self.add_col(index, number)
            elif operation_type == "mult" and vector == "row":
                self.multiply_row(index, number)
            elif operation_type == "mult" and vector == "col":
                self.multiply_col(index, number)

    def add_row(self, index, value):
        for position, item in enumerate(self.matrix[index]):
            self.matrix[index][position] += value

    def add_col(self, index, value):
        for row in self.matrix:
            row[index] += value

    def multiply_row(self, index, value):
        for postion, item in enumerate(self.matrix[index]):
            self.matrix[index][postion] *= value

    def multiply_col(self, index, value):
        for row in self.matrix:
            row[index] *= value


class CSVFileHandler(FileHandler):

    def load_data_from_file(self):
        temp_matrix = []
        with open(self.input_file) as file:
            reader = csv.reader(file)
            for line in reader:
                temp_line = []
                for number in line:
                    temp_line.append(int(number))
                temp_matrix.append(temp_line)
        self.matrix = temp_matrix

    def save_data_to_file(self):
        with open(self.output_file, mode="w+") as file:
            writer = csv.writer(file)
            for line in self.matrix:
                writer.writerow(line)


class PickeFileHandler(FileHandler):
    def load_data_from_file(self):
        with open(self.input_file, mode="rb") as file:
            self.matrix = pickle.load(file)

    def save_data_to_file(self):
        with open(self.output_file, mode="wb") as file:
            pickle.dump(self.matrix, file)
