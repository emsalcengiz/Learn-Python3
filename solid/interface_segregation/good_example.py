from abc import ABC, abstractmethod


class ICanFly(ABC):
    @abstractmethod
    def fly(self) -> None:
        ...


class ICanEat(ABC):
    @abstractmethod
    def eat(self) -> None:
        ...


class ICanBreathFire(ABC):
    @abstractmethod
    def fly(self) -> None:
        ...


class Dragon(ICanFly, ICanEat, ICanBreathFire):
    def fly(self) -> None:
        print("Flying")

    def eat(self) -> None:
        print("Eating")

    def breath_fire(self) -> None:
        print("Breating fire")