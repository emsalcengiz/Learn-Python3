"""
Singleton(tek nesne) tasarım kalıbı, bir sınıfın tek bir örneğini almak için kullanılır.
Amaç oluşturulan nesneye global erişim noktası sağlamaktır.
Sistem çalıştığı sürece ikinci bir örnek oluşturulmaz, böylelikle istenen nesnenin tek bir defa oluşturulması garanti altına alınacaktır.
Singleton nesneler ilk çağırıldıklarında bir kere oluşturulurlar ve sonraki istekler bu nesne üzerinden karşılanır.
"""

from typing import Optional, cast


class IvoryTower:
    """Singleton class example"""

    _instance: Optional["IvoryTower"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance

        cls._instance = cast(
            "IvoryTower", super(IvoryTower, cls).__new__(cls, *args, **kwargs)
        )
        return cls._instance

    def __str__(self):
        return f"The id of this Ivory Tower is {id(self)}"


if __name__ == "__main__":
    tower_1 = IvoryTower()
    tower_2 = IvoryTower()

    print(tower_1)
    print(tower_2)