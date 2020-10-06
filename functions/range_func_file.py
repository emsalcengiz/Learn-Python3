# liste = list(range(0,20)) # list fonksiyonuyla listeye dönüştürebilir.
# print(liste)
#
# print(*range(5,20,2)) # 5'ten 20'ye kadar olan sayıları 2 atlayarak oluşturur.
#
# print(*range(20,0,-1)) # 20'den geri gelen sayıları oluşturur.
#
# #
# # for sayı in range(0,10):
# #     print(sayı)
# #
#
# for sayı in range(1,20):
#     print("false" * sayı)

#such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200
lst=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        lst.append(str(i))

print(','.join(lst))