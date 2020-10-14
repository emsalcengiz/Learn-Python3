"""
Facade Bir alt sistemin parçalarını oluşturan classları istemciden soyutlayarak kullanımı daha da kolaylaştırmak için tasarlanmış tasarım kalıbıdır.
Mimarisel açıdan ise, karmaşık ve detaylı bir sistemi organize eden ve bir bütün olarak clientlara(istemcilere) sunan yapıdır.

Karmaşık ve detaylı olarak nitelendirdiğimiz bu sistemi bir alt sistem olarak varsayarsak eğer bu sistemi kullanacak clientlara daha basit bir arayüz sağlamak ve alt sistemleri bu arayüze organize bir şekilde dahil etmek ve bu alt sistemlerin sağlıklı çalışabilmesi için bu arayüz çatısı altında işin algoritmasına uygun işlev sergilemek istersek Facade Design Pattern’i kullanmaktayız.
Burada bilmeniz gereken durum, alt sistem içerisinde bulunan sınıfların birbirlerinden bağımsız olmasıdır. Ayrıca Facade sınıfından da bağımsız bir şekilde çalışabilmektedirler.
Facade bizim classlarımızı içermek zorundadır ve operasyonu yaparken onlara ait fonksiyonellikleri kullanması gerekli.

"""