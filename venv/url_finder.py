import json
import os
import pandas as pd
import requests
import urllib
import urllib2
import urllib3

# import urllib.request

site = 'https://www.elle.com/es/'
url = 'www.elle.com/es/'


# url = 'http://maps.googleapis.com/maps/api/directions/json'

# params = dict(
#     origin='Chicago,IL',
#     destination='Los+Angeles,CA',
#     waypoints='Joplin,MO|Oklahoma+City,OK',
#     sensor='false'
# )

resp = requests.get(url=site)
data = resp.json() # Check the JSON Response Content documentation below


with line in response:
   print_line


import http.client
conn = http.client.HTTPSConnection(url)
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
200 OK
data1 = r1.read()  # This will return entire content.


response = urllib.request.urlopen(site)
data = json.load(response)

response.read()

for line in response:
   print(line)

response = urllib.request.urlopen(site)
response.read()

print(response)

data = json.load(response.read())
print(response)


# import urllib.request

site = 'https://www.elle.com/es/'

with urllib.request.urlopen(site) as response:
   # html = response.read()
   # get_headers = response.getheaders()
   headers = response.headers

len(headers)
html[:100]

type(html)

for line in headers:
   print(line)

url_root = 'https://www.elle.com'
other_site = '/es/living/viajes/a42120894/ciudades-mas-bonitas-segun-la-ciencia/'

print(url_root + other_site)


with urllib.request.urlopen(url_root + other_site) as response:
   html = response.read()

html

