import requests

# a request to a web page
# The requests module allows you to send HTTP requests using Python
x = requests.get("https://github.com/emsalcengiz")

print(x.text)