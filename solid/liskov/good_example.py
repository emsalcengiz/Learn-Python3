from abc import ABC
from typing import List


class MiddleEarthInhabitant(ABC):
    def __init__(self, name):
        self.name = name


class Dancer(ABC):
    def dance(self) -> None:
        ...


class Human(MiddleEarthInhabitant, Dancer):
    def dance(self) -> None:
        print("Human going wild on the dance floor.")


class Hobbit(MiddleEarthInhabitant, Dancer):
    def dance(self) -> None:
        print("Look at those big Hobbit feet go.")


class Orc(MiddleEarthInhabitant):
    pass


class Party:
    def __init__(self, guests: List[Dancer]):
        self._guests: List[Dancer] = guests

    def que_music(self):
        for guest in self._guests:
            if not self.check_guest(guest):
                continue

            guest.dance()

    def check_guest(self, guest):
        if not isinstance(guest, Dancer):
            if hasattr(guest, "name"):
                print(f"You shall not pass, {guest.name}!")


if __name__ == "__main__":
    aragorn = Human("Aragorn")
    frodo = Hobbit("Frodo")
    azog = Orc("Azog")

    party = Party([aragorn, frodo, azog])

    party.que_music()