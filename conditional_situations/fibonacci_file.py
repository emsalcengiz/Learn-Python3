import sys

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a + b
f = fibonacci(5)

# yield deyimi, return deyimi gibi fonksiyonlarda kullanılır, ancak, fonksiyon bir generator döndürür.
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()