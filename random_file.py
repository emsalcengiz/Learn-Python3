import random
import keyword

isimler = ["Göksel 🤬 ","Emsal 😎 "]
taraf = ["sağ", "sol"]

print(str(isimler[random.getrandbits(1)]) + " " + str(taraf[random.getrandbits(1)]) + "daki kahveyi içer. ☕️")

# @keyword.kwlist: bu listedeki hiç birşeyi değişken olarak kullanamazsın.
print(keyword.kwlist)
print(len(keyword.kwlist))