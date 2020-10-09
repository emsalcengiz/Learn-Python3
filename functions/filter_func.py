# name = ["emsal", "göksel","eda","uğur"]
# date = [2016,2017,2018,2020]
#
#
# sonuc1 = list(zip(name, date))
# # print(sonuc1[0][0])
#
# sonuc = filter(lambda x: x[1] > 2016, sonuc1)
# print(list(sonuc))


cumle = ["selam","istanbul","benim","en","sevdiğim","renk","siyah"]
sonuc = filter(lambda word: len(word)>=6, cumle )
print(list(sonuc))


sonuc2 = map(lambda word: len(word),  cumle)
print(list(sonuc2))