"""
Ne zaman ihtiyaç duyarız ?
" Eğer çok fazla parametre alan bir objeniz var ise bu objeyi oluştururken constructor’ında bir çok “null” parametre geçmeye başladıysanız."

"Eğer objenizi oluştururken birden çok constructor’ı varsa ve hangisini kullanacağınız konusu net değilse,
 bu objeyi oluşturmak için minimum hangi alanları doldurmanız gerektiği konusunda kafa karışıklığınız oluşuyorsa."

"Nesnenin oluşturulduktan sonra değişmez (immutable) olmasını istiyorsanız"

"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Armor(Enum):
    """Armors"""

    CLOTHES = "clothes"
    LEATHER = "leather"
    CHAIN_MAIL = "chain mail"
    PLATE_MAIL = "plate mail"


class HairColor(Enum):
    """Hair colors"""

    WHITE = "white"
    BLOND = "blond"
    RED = "red"
    BROWN = "brown"
    BLACK = "black"


class HairType(Enum):
    """Hair types"""

    BALD = "bald"
    SHORT = "short"
    CURLY = "curly"
    LONG_STRAIGHT = "long straight"
    LONG_CURLY = "long curly"


class Profession(Enum):
    """Professions"""

    WARRIOR = "warrior"
    THIEF = "thief"
    MAGE = "mage"
    PRIEST = "priest"


class Weapon(Enum):
    """Weapons"""

    DAGGER = "dagger"
    SWORD = "sword"
    AXE = "axe"
    WARHAMMER = "warhammer"
    BOW = "bow"


@dataclass
class Hero:
    name: str
    profession: Profession
    hair_type: Optional[HairType]
    hair_color: Optional[HairColor]
    weapon: Optional[Weapon]
    armor: Optional[Armor]

    def __repr__(self) -> str:
        """
        Why did I use a list instead of naively appending to a string: https://waymoot.org/home/python_string/
        """
        desc = [f"This is a {self.profession.value} named {self.name}"]

        if any([self.hair_type, self.hair_color]):
            desc.append("with")
        if self.hair_color:
            desc.append(self.hair_color.value)
        if self.hair_type:
            desc.append(self.hair_type.value)

            if self.hair_type == HairType.BALD:
                desc.append("head")
            else:
                desc.append("hair")
        if self.armor:
            desc.append(f"wearing {self.armor.value}")
        if self.weapon:
            desc.append(f"wielding {self.weapon.value}")

        return " ".join(desc)


class HeroBuilder:
    """Builder to create a new :class:`Hero`"""

    def __init__(self, name: str, profession: Profession):
        self._name: str = name
        self._profession: Profession = profession

        self._hair_type: Optional[HairType] = None
        self._hair_color: Optional[HairColor] = None
        self._armor: Optional[Armor] = None
        self._weapon: Optional[Weapon] = None

    def with_hair_type(self, hair_type: HairType) -> "HeroBuilder":
        self._hair_type = hair_type
        return self

    def with_hair_color(self, hair_color: HairColor) -> "HeroBuilder":
        self._hair_color = hair_color
        return self

    def with_armor(self, armor: Armor) -> "HeroBuilder":
        self._armor = armor
        return self

    def with_weapon(self, weapon: Weapon) -> "HeroBuilder":
        self._weapon = weapon
        return self

    def build(self) -> Hero:
        """Builds the :class:`Hero` using the given values"""
        return Hero(
            self._name,
            self._profession,
            self._hair_type,
            self._hair_color,
            self._weapon,
            self._armor,
        )


if __name__ == "__main__":
    hero = (
        HeroBuilder("Legolas", Profession.WARRIOR)
        .with_armor(Armor.CLOTHES)
        .with_hair_color(HairColor.BLOND)
        .with_hair_type(HairType.LONG_STRAIGHT)
        .with_weapon(Weapon.BOW)
        .build()
    )

    print(str(hero))

