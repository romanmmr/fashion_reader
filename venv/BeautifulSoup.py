from bs4 import BeautifulSoup
import requests

# Obtener el documento HTML
website = 'https://www.elle.com/es/gourmet/gastronomia/a42709633/como-ser-vegano-gloria-carrion/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

# Localizar la caja (box) que contiene el titulo (title) y transcript
title_box = soup.find('h1', class_='content-hed standard-hed')
# title_box = title_box.find('span', class_='wait-font-load')
# print(title_box.get_text())
# Localizar el titulo (title) y transcript
title = title_box.find('span').get_text()
print(title_box)

box = soup.find('div', class_='content-header-inner')
title = box.find('h1').get_text()
intro = box.find('p').get_text(strip=True, separator=' ')

author_box = soup.find('div', class_='byline')
author = author_box.find('span').get_text(strip=True, separator=' ')

article_box = soup.find_all('p', class_='body-text')

print(article_box)

# intro = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# Exportar data en un archivo txt con el nombre de la variable titulo (title)
# with open(f'{title}.txt', 'w') as file:
#     file.write(transcript)

# <div class="content-dek standard-dek" style=""><p>Hablamos con la divulgadora Gloria Carrión, que acaba de lanzar ‘La Biblia de la Cocina Vegana’, de esas recetas que, sorprendentemente, están triunfando también entre el público no vegano. Y para comprobar que se puede estar comprometido con la causa sin tener que renunciar al sabor y a la diversión, hacemos una parada en el madrileño Levél Veggie Bistro, que gracias a platos como la lasagna o las brochetas de champiñón,  aprueba con nota.</p></div>
#
# < div class ="content-header-inner" >
#
# < div class ="content-container standard-container" >