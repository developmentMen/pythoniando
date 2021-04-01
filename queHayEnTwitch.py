import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://www.w3schools.com/python/')
soup = BeautifulSoup(pagina.content, "html.parser")

data = soup.find_all('a', target="_top") #find_all

print(data)