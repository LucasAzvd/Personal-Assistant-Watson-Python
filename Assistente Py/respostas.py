from playsound import playsound #windows
from gtts import gTTS
import os
import random


class Resposta():
    def __init__(self, resposta):
        self.resposta = resposta

    #Create audios to proram execute
    def cria_audio(self, mensagem):
        try:
            tts = gTTS (mensagem, lang='pt-br')
            tts.save('audios/mensagem.mp3')
            print ('Tallud:\n    ' +mensagem)
            playsound ('audios/mensagem.mp3')   #windows
            os.remove('audios/mensagem.mp3')
            
        #Permission in Windows 10 is denied
        except PermissionError:
            numero = random.randint(0,1000000000000)
            tts = gTTS (mensagem, lang='pt-br')
            tts.save('audios/mensagem'+ str(numero) +'.mp3')
            print ('Tallud:\n    ' +mensagem)
            playsound ('audios/mensagem'+ str(numero) +'.mp3')   #windows
            os.remove('audios/mensagem'+ str(numero) +'.mp3')

    
    def responde_simples(self, resposta):     #Play response
        playsound ('audios/'+ resposta +'.mp3')     #windows
