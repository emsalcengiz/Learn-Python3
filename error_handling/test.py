# def funct(sayi):
#     return sayi/0


# sayi = int(input("sayi giriniz.."))
# sayi = sayi*sayi
# print(sayi)
# try:
#     sayi = funct(sayi)
#     print(sayi)


# except IndexError as e:
#     print("1.hata")
#     print(e)


# sayi = sayi/sayi
# print(sayi)

# x = 10
# if x > 5:
#     raise Exception('x 5 i geçmemelidr. x in değeri: {}'.format(x))

import sys
# assert ('linux' in sys.platform), "Bu kod yalnızca Linux'ta çalışır."



def linux_interaction():
    assert ('linux' in sys.platform), "Bu kod yalnızca Linux'ta çalışır."
    
try:
    linux_interaction()
except:
    pass
#2...
try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('Linux linux_interaction() function was not executed')


#3....
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')