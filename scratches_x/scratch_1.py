print("Aramak istediğniz kelimeyi girin:")
print(len("göksel"))

print("c#","python3")
print("www",".","ggogle",".","com")

# sep print fonksiyonun aldığı bir parametredir
print("www",".","ggogle",".","com", sep="")
print("T","C", sep=".")
print(1,2,3,sep=None)

# end print fonksiyonun aldığı bir parametredir
print("BU gün günlerden çarşambadır",end=".")
print("\n",1,2,3,end=None)

# file print fonksiyonun aldığı bir parametredir
dosya=open("deneme.txt", "w")
print("python programlama dilidir.",file=dosya)
dosya.close()
