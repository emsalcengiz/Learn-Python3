"""
map, zip, reduce ve filter fonksiyonları
"""
# numbers = [3, 2, 4, 5]
#
# def karesi(number):
#     return number ** 2
#
#
# sonuc = map(karesi,numbers)
# print(list(sonuc))

num1 = [3,5,6,7]
num2 = [9,4,7,8]

def kucuk(x,y):
    if x < y:
        return x
    else:
        return y


sonuc = map(kucuk, num1, num2)
print(list(sonuc))