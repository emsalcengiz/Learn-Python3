from functools import reduce

numbers = [11, 2 , 3 , 8]


# def find_max(a,b):
#     if a > b:
#         return a
#
#      return b

def carp(a,b):
    return a * b


sonuc = reduce(carp, numbers)
print(sonuc)

