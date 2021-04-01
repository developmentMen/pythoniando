#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

"""
soup = BeautifulSoup("<p>Hola<b>Mundo<i>HTML", 'html.parser')

print(soup.prettify())
"""
pagina = requests.get('https://es.wikipedia.org/wiki/Hola_mundo')
soup = BeautifulSoup(pagina.content, "html.parser")

data = soup.find('h1', class_="firstHeading") #find_all

print(data.text+" <--|From Wikipedia")
