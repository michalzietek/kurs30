from abc import ABC, abstractmethod


class Ptak:
    def make_shit(self):
        print("I just poop")

    def scream(self):
        print("wraaaaw")

    @abstractmethod
    def move(self):
        raise NotImplementedError


class Golab(Ptak):
    def move(self):
        print("Hurra potrafie latać!")


class Wrona(Ptak):
    def move(self):
        print("Latam i mam czarne duże skrzydła!")


class Kura(Ptak):
    def move(self):
        print("Latam, ale bardziej skaczę")


class Strus(Ptak):
    def move(self):
        print("Idę sobie do przodu albo chowam glowe w piasek.")


