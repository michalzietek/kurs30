import random
import string

class RandomLetterIterator:
    def __init__(self, limit):
        self.limit = limit
        self._position = 0
        self._letters = string.ascii_letters
        print(self._letters)

    def get_random_letter(self):
        return random.choice(self._letters)

    def __iter__(self):
        return self

    def __next__(self):
        print("Znowu Cie wywolalem")
        if self._position < self.limit:
            self._position += 1
            return self.get_random_letter()
        else:
            print("Dupa")

fake_iterator = RandomLetterIterator(limit=10)
