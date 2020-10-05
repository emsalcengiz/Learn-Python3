#!/usr/bin/python3
amount = int(input("Enter amount: "))

if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
elif amount < 5000:
    discount = amount * 0.10
    print("Discount", discount)
else:
    discount = amount * 0.15
    print("Discount", discount)

print("Net payable:", amount - discount)

# var = 100
# if ( var  == 100 ):
#     print ("Value of expression is 100")
#     print ("Good bye!")