from collections import OrderedDict

# type() func
x = 10
print(type(x))

s = 'abc'
print(type(s))

od = OrderedDict()
print(type(od))


class Data:
    pass

d = Data()
print(type(d))

# len() func.
mylist = ["apple", "orange", "cherry"]
x = len(mylist)

print(x)

# pov() func.
x = 3
print(pow(x,3))