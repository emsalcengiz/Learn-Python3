from abc import ABC, abstractmethod


class IDragon(ABC):
    @abstractmethod
    def fly(self) -> None:
        ...

    @abstractmethod
    def eat(self) -> None:
        ...

    @abstractmethod
    def breath_fire(self) -> None:
        ...


class Dragon(IDragon):
    def fly(self) -> None:
        print("Flying")

    def eat(self) -> None:
        print("Eating")

    def breath_fire(self) -> None:
        print("Breating fire")