import random

isimler = ["Emsal 🤬 ","Göksel 😎 "]
taraf = ["sağ", "sol"]

print(str(isimler[random.getrandbits(1)]) + " " + str(taraf[random.getrandbits(1)]) + "daki kahveyi içer. ☕️")