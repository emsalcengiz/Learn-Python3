import requests

# url = requests.get("https://dfb16bd5b7fcb6c1e064e8bb5e610b4f.m.pipedream.net")
# print(url)

# print(type(url))

# r = requests.get("https://dfb16bd5b7fcb6c1e064e8bb5e610b4f.m.pipedream.net")
# print(r.status_code)
# print(r.ok)

url = "https://dfb16bd5b7fcb6c1e064e8bb5e610b4f.m.pipedream.net"
r = requests.get(url, params={"kategori":"telefon","marka":"apple"})

print(r.status_code)
print(r.ok)
print(r.url)

x = requests.post(url)
print(x.status_code)
print(x.url)

y = requests.post(url, data={"username":"emsal","password":"göksel"})
print(y.status_code)
print(y.url)

z = requests.post(url, data={"username":"emsal","password":"göksel"}, headers={"User-Agent":"Emsal Cengiz-Chrome", "Referer":"emsalcengiz.com"})
print(z.status_code)
print(z.url)

v = requests.get("https://github.com/emsalcengiz")
print(v.encoding)
print(v.headers)
# print(v.text)

print(v.request) #atılan son isteği döner






