from abc import ABC
from typing import List


class MiddleEarthInhabitant(ABC):
    def dance(self) -> None:
        ...


class Human(MiddleEarthInhabitant):
    def dance(self) -> None:
        print("Human going wild on the dance floor.")


class Hobbit(MiddleEarthInhabitant):
    def dance(self) -> None:
        print("Look at those big Hobbit feet go.")


class Orc(MiddleEarthInhabitant):
    def dance(self) -> None:
        print("Kills everyone on the party!")


class Party:
    def __init__(self, guests: List[MiddleEarthInhabitant]):
        self._guests = guests

    def que_music(self):
        for guest in self._guests:
            guest.dance()


if __name__ == "__main__":
    party = Party([Human(), Hobbit(), Orc()])

    party.que_music()