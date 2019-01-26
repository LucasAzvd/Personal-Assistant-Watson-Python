import pyaudio
import speech_recognition as sr
from toca_musica import Playlist
from comandos_e_automatizacoes import Comandos
from respostas import Resposta


#3a5e2c93c0896fa3fa8dfec3fd8c9e5d

### CONFIGS ###
hotword = 'talu'   #Bot name
with open('YOUR GOOGLE ID.json') as credenciais_google:
    credenciais_google = credenciais_google.read()



class Monitora():

    def monitora_audio(self):
        while True:
            microfone = sr.Recognizer()

            with sr.Microphone() as source:    
                print("\nEsperando o comando...") #Wait a command
                audio = microfone.listen(source)

                try:    #Try catch the message
                    trigger = microfone.recognize_google(audio, language='pt-br')
                    trigger = trigger.lower()

                    #print(trigger)
                    #if hotword in trigger:  
                    print('Comando: ' + trigger.strip(hotword))

                    aux_resposta = Resposta('feedback')
                    aux_resposta.responde_simples('feedback')

                    auxilia_comandos = Comandos(trigger)
                    auxilia_comandos.executa_comandos(trigger)

                except sr.UnknownValueError:    #No understand
                    print("-> Não entendi o que você falou")
                    pass

                except sr.RequestError as e:
                    print("-> Could not request results from Google Speech Recognition service; {0}".format(e))
                    pass

        return trigger
