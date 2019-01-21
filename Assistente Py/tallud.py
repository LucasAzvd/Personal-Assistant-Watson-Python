import speech_recognition as sr
import pyaudio
from playsound import playsound #windows
from requests import get
from bs4 import BeautifulSoup
from gtts import gTTS


### CONFIGS ###
hotword = 'clara'   #Bot name
with open('YOUR_ASSISTANT_CREDENCIALS.json') as credenciais_google:
    credenciais_google = credenciais_google.read()

###FUNÇÕES SUBSTITUTAS###
def monitora_audio():
    while True:
        microfone = sr.Recognizer()
        with sr.Microphone() as source:    
            print("Esperando o comando...") #Wait a command
            audio = microfone.listen(source)
            try:    #Try catch the message
                trigger = microfone.recognize_google(audio, language='pt-br')
                trigger = trigger.lower()
                print(trigger)
                if hotword in trigger:  
                    print('Comando: ' + trigger)
                    responde('feedback')
                    executa_comandos(trigger)
            except sr.UnknownValueError:    #No understand
                print("-> Não entendi o que você falou")
                pass
            except sr.RequestError as e:
                print("-> Could not request results from Google Speech Recognition service; {0}".format(e))
                pass
    return trigger

def responde(resposta):     #Play response
    playsound ('audios/'+ resposta +'.mp3')         #windows

def executa_comandos(trigger): #Execute commands
    if 'notícias' in trigger:
        ultimas_noticias()

### COMMAND FUNCTIONS ###

#Create audios to proram execute
def cria_audio(mensagem):
    tts = gTTS (mensagem, lang='pt-br')
    tts.save  ('audios/mensagem.mp3')
    playsound ('audios/mensagem.mp3')         #windows

def ultimas_noticias(): #The last br news
    mensagem = ''
    site = get('https://news.google.com/news/rss?ned=pt_br&BR&hl=pt')
    noticias= BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:3]:
        aux_mensagem = item.title.text + '.\n'
        mensagem += aux_mensagem
    print (mensagem)
    cria_audio(mensagem)

def main():
    monitora_audio()

main()





#USE THE ACTUAL API THE GOOGLE, BUT GENERATE ERRORS
"""
### FUNÇÕES PRINCIPAIS ###
def monitora_audio():
# obtem audio do microphone
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Esperando o comando...")
            audio = microfone.listen(source)
            try:
                trigger = microfone.recognize_google_cloud(audio, credentials_json=credenciais_google, language='pt-BR')
                print (trigger)
                trigger = trigger.lower()
                if hotword in trigger:
                    print('Comando: ' + trigger)
                    responde('feedback')
                    ### EXECUTAR COMANDO
                    break

            except sr.UnknownValueError:
                print("Google Cloud Speech could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Cloud Speech service; {0}".format(e))
    return trigger

"""
