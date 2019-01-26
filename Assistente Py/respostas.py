from playsound import playsound #windows
from gtts import gTTS


class Resposta():
    def __init__(self, resposta):
        self.resposta = resposta

    #Create audios to proram execute
    def cria_audio(self, mensagem):
        tts = gTTS (mensagem, lang='pt-br')
        tts.save('audios/mensagem.mp3')
        print ('Clara:\n    ' +mensagem)
        playsound ('audios/mensagem.mp3')   #windows

    
    def responde_simples(self, resposta):     #Play response
        playsound ('audios/'+ resposta +'.mp3')     #windows