from gtts import gTTS
from gtts import langs

def say_hello():
    # tts = gTTS('Hello again, my dear friend')
    # tts = gTTS(lang="en", "Hello my potatoe!")
    tts = gTTS("Hola mi patata", lang="es", tld="es")
    tts.save('hello.mp3')