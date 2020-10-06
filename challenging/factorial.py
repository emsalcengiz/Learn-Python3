def fact(number):
    if (number == 0):
        return 1
    return number * fact(number - 1)

number = int(input("what is the number:"))
print(fact(number))