from bs4 import BeautifulSoup
from gtts import gTTS
from gtts import langs
# import mimic3_tts
import os
import pyttsx3
import requests

import text_preprocess

# Obtener el documento HTML
website = 'https://www.elle.com/es/gourmet/gastronomia/a42709633/como-ser-vegano-gloria-carrion/'
# website = 'https://www.marca.com/futbol/real-madrid/2023/03/07/640513a146163ff16e8b456c.html'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())


# Let's identify the box that contains the title and intro
box = soup.find('div', class_='content-header-inner')
title = box.find('h1').get_text()
intro = box.find('p').get_text(strip=True, separator=' ')

print(title)
print(intro)


# Let's identify the box that contains the autor
author_box = soup.find('div', class_='byline')
author = author_box.find('span').get_text(strip=True, separator=' ')

print(author)


# Let's get the actual article box
article_box = soup.find_all('p', class_='body-text')

print(article_box[0].text)


full_article = ''

full_article += text_preprocess.preprocess_text(title) + '\n'
full_article += text_preprocess.preprocess_text(intro) + '\n'

for paragraph in article_box:
    full_article += text_preprocess.preprocess_text(paragraph.text) + '\n'

# print(intro[276:301])

# tts = gTTS(full_article, lang="es", tld="es")
# tts.save('full_article.mp3')

engine = pyttsx3.init()

for voice in engine.getProperty('voices'):
    if 'ES-ES' in voice.id.split("\\")[-1]:
        my_voice_id = voice.id

engine.getProperty('rate')

engine.setProperty('rate', 150)
engine.setProperty('voice', my_voice_id)
engine.setProperty('volume', 1)
# engine.say('Hola amigo mío, o debería decir "amigo" mío')
engine.save_to_file(full_article, 'full_article.mp3')
engine.runAndWait()

print(full_article[:300])

# help(mimic3_tts.tts)

# engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# pyttsx3.voice.Voice(id=1, name=None, languages=['es'])
#
# engine.say('The quick brown fox jumped over the lazy dog.')
#
# engine.say('Hola amigo mío')
# engine.runAndWait()

# article_box[0].text


# intro = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# Exportar data en un archivo txt con el nombre de la variable titulo (title)
# with open(f'{title}.txt', 'w') as file:
#     file.write(transcript)

# <div class="content-dek standard-dek" style=""><p>Hablamos con la divulgadora Gloria Carrión, que acaba de lanzar ‘La Biblia de la Cocina Vegana’, de esas recetas que, sorprendentemente, están triunfando también entre el público no vegano. Y para comprobar que se puede estar comprometido con la causa sin tener que renunciar al sabor y a la diversión, hacemos una parada en el madrileño Levél Veggie Bistro, que gracias a platos como la lasagna o las brochetas de champiñón,  aprueba con nota.</p></div>
#
# < div class ="content-header-inner" >
#
# < div class ="content-container standard-container" >

# ord(chr(8217))