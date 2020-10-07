# mylist = ['g','ö','k','s','e','l','e','s','l']
# mylist = list(dict.fromkeys(mylist))
#
# print(mylist)


def my_function(x):
    return list(dict.fromkeys(x))

mylist = my_function(['e','m','s','q','l','a','a','l'])
print(mylist)