"""
Adaptör Tasarım deseni mevcut bir sınıfı veya arayüz sınıfını, eldeki farklı bir arayüz sınıfına uygun hale getirerek tekrar kullanmak amacıyla uygulanır.
Çoğu zaman işe yarayacağını düşündüğümüz mevcut bir sınıfı kendi sistemimizde tekrar kullanmak isteriz.
Fakat mevcut sınıf, tam beklediğimiz gibi olmayabilir.
Bu durumda araya bir tane adaptör yazarak, mevcut sınıfı kendi sistemimize uygun hale getirebiliriz.
Böylece adapte edilen nesnede kod değişikliği olmadan benzer bir arayüzü destekler hale getiririz.
Ayrıca adaptasyon işlemi sırasında, adapte edilen nesnenin desteklemediği özellikler de adaptör tarafından gerçekleştirilebilir.
Ayrıca adaptasyon işlemi sırasında, adapte edilen nesnenin desteklendiği özelliklerde Adaptör tarafında gerçekleştirilebilir.
Bir sınıfın arayüzünü müşterilerin istediği arayüze dönüştürülür.
Adaptör, sınıfların uyumsuz ara birimler nedeniyle aksi halde olmayan birlikte çalışmasına izin verir. mevcut bir sınıfı bir arayüzle sarar.

"""

from typing import Protocol


class RowingBoat(Protocol):
    def row(self):
        ...


class FishingBoat:
    """A boat to go fishing"""

    def sail(self):
        print("The fishing boat is sailing")


class Captain:
    def __init__(self, rowing_boat: RowingBoat):
        self.rowing_boat = rowing_boat

    def row(self):
        self.rowing_boat.row()


class FishingBoatAdapter(RowingBoat):
    def __init__(self):
        self.fishing_boat = FishingBoat()

    def row(self):
        self.fishing_boat.sail()


if __name__ == "__main__":
    captain = Captain(FishingBoatAdapter())

    captain.row()