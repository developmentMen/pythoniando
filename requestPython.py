import requests
from urllib

# REQUESTS
url = requests.get("https://www.google.com/")
url2 = requests.get("https://www.google.com/asgdefvtrwrq")
print(url.ok)

# URLLIB
a=urllib.request.urlopen('http://www.google.com/asdfsf')
a.getcode()
404
a=urllib.request.urlopen('http://www.google.com/')
a.getcode()

