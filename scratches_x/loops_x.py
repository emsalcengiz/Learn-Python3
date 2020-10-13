for i in range(20):
          if i == 10:
               break
print("test")

"""
Break .... i değeri 10 olduğu zaman i yi saymayı bırakıp ekrana "test" yazacak
"""


for i in range(20):
    if i == 15:
        continue

print(i)

"""
Ekrana 12345678910111213141617181920 yazacatır. Dikkat etmeniz gereken r değeri 15 olduğu zaman print işlemi işletilmeyecektir. Yani ekrana yazmayacaktır.
"""
def fonksiyon():
    pass

fonksiyon()

"""Eğer bir fonksiyona ya da kod bloğuna ihtiyacınız varsa ama içinde bir işlem olmaması gerekiyorsa kullanılır. Benim denk geldiğim plsql de null olarak kullanılıyor, python da pass olarak kullanılıyor."""
