import requests
from Tools.scripts.findlinksto import visit

import dryscrape

url = "http://avi.im/stuff/js-or-no-js.html"

r = requests.get(url)
print(r.status_code)
print(r.content)

s = dryscrape.Session()
s = visit()
s = body()

# dryscrape windows os de  çalımıyormuş :(