import pyaudio
import speech_recognition as sr
import watson_developer_cloud
from toca_musica import Playlist
from comandos_e_automatizacoes import Comandos
from respostas import Resposta
from watson_developer_cloud import AssistantV2


#3a5e2c93c0896fa3fa8dfec3fd8c9e5d

### CONFIGS ###
hotword = 'talu'   #Bot name
with open('{YOUR_GOOGLE_API}') as credenciais_google:
    credenciais_google = credenciais_google.read()



#Conect to Watson Assistant
service=watson_developer_cloud.AssistantV2(
    iam_apikey='{YOUR_API_KEY}',
    version='2018-11-08',
    url='https://gateway.watsonplatform.net/assistant/api'
)
assistant_id = '{YOUR_ASSISTANT_ID}'

response = service.create_session(
    assistant_id= assistant_id
).get_result()




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

                    
                    
                    watson_return = service.message(
                        assistant_id= assistant_id,
                        session_id=response['session_id'],
                        input={
                            'message_type': 'text',
                            'text': trigger
                        }
                    ).get_result()
                    
                    #Recived the response and send to commands
                    auxilia_comandos = Comandos(watson_return['output']['generic'][0]['text'])
                    auxilia_comandos.executa_comandos(watson_return['output']['generic'][0]['text'])

                except sr.UnknownValueError:    #No understand
                    print("-> Não entendi o que você falou")
                    pass

                except sr.RequestError as e:
                    print("-> Could not request results from Google Speech Recognition service; {0}".format(e))
                    pass

        return trigger