import os

# print(os.name) #kullanılan işletim sisteminin değerini söyler, nt windows posix linux ---

# print(os.sep) #kullandığımız işletim sisteminin dosya ayracının ne olduğunu gösterir. Windows için \ veya \\ değeri dönerken Linux’ta / değeri

# liste = ['kahve', 'yumurta', 'peynir', 'bira']
# dizgi = os.sep.join(liste) #kahve\yumurta\peynir\bira
# print(dizgi)

# path = os.getcwd() #bulunduğumuz dosya yolunu döndürür
# print(path)

# folder = os.chdir('C:\\Users\\emsal.cengiz\\PycharmProjects') #bulunduğumuz dizinden başka bir dizine geçmemizi sağlar
# path = os.getcwd() 
# print(path)

# listem = os.listdir('C:\\Users\\emsal.cengiz\\PycharmProjects\\Learn-Python3')
# print(listem)
# #Bulunduğumuz dizindeki dosya ve altdizinleri bir döngü ile listeleyebiliriz
# print("--------------------------------------------------------------------")

# listem_two = os.listdir(r'C:\Users\emsal.cengiz\PycharmProjects\Learn-Python3')
# print(listem_two)


# listem_ex = os.listdir(".") #veya listdir(os.getcwd()) aynıdır.. bulundumuz klasörleri lstelemek için kullanılır
# for i in listem_ex:
#     print(i)




# #os.pardir() İşletim sistemine göre dosya yolunda geri gitmek için yani bir üst dizine gitmek için kullanılan karakter dizisini döndürür.

# see = os.curdir
# #İçinde bulunduğumuz dizini göstermek için kullanılan karakter dizisini döndürür
# print(see)


# os.startfile(r'C:\Users\emsal.cengiz\PycharmProjects\Learn-Python3') #sadece windows da çalışıyor..
# #Herhangi bir dizini, internet sitesini , bir dosyayı ilişkili olduğu programda açar

# # os.mkdir()
# # os.rename('eski dizin adı', 'yeni dizin adı')
# # os.rename('silinecek_file.doc')
# # os.rmdir('silinecek_folder') #içi boş folder siler
# # os.removedirs()#iç içe olan boş dizinleri tek seferde silmemizi sağlar
# # os.removedirs('yazılar\\biyografi') #yazıların içindeki biyografi silinecek

# # os.stat()
# #Dosyanın boyutu, oluşturulma tarihi, değiştirilme tarihi, son erişime tarihi gibi bilgileri bizlere obje olarak döndürür.


# from datetime import datetime

# # my_file = os.stat('göksel.txt')
# # print(my_file)


# os.walk()
# # dizinler içinde yürümemizi sağlar, Yani fonksiyonun içine yazdığımız dizin içerisindeki tüm altdizin ve dosyaları bize 3 öğeden oluşan bir demet olarak döndürür. Bu demetin sıfırıncı indeksi dizin yolunu , birinci indeksi altdizinleri , ikinci indeksi ise dosyaları


# for yol,dizin,dosya in os.walk(os.getcwd()):
#     for dosyalar in dosya:
#         print(dosyalar)



os.path.exists('göksel.txt')
#Dosya veya dizinin var olup olmadığını kontrol eder. True veya False değeri döndürür.

os.path.abspath('göksel.txt')
#Dosyanın yolunu döndürür.