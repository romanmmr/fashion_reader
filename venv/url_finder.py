import os
import pandas as pd
import urllib


# import urllib.request

site = 'https://www.elle.com/es/'

with urllib.request.urlopen(site) as response:
   html = response.read()

len(html)


url_root = 'https://www.elle.com'
other_site = '/es/living/viajes/a42120894/ciudades-mas-bonitas-segun-la-ciencia/'

print(url_root + other_site)


with urllib.request.urlopen(url_root + other_site) as response:
   html = response.read()

html

