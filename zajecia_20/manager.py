from file_handler import FileHandler

class Manager:
    def __init__(self, history_file, data_file):
        self.actions = {}
        self.file_handler = FileHandler(data_file=data_file, history_file=history_file)
        self.data = self.file_handler.load_data_from_data_file()
        self.dziennik = self.file_handler.load_history_from_history_file()
        self.ksiegozbior = self.data.get("ksiegozbior")
        self.saldo_ksiegarni = self.data.get("saldo")


    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb

        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)

manager = Manager(history_file="dziennik.json", data_file="dane.json")