from trata_audio import Monitora

#Execute Program
def main():
    while True:
        executa = Monitora()
        executa.monitora_audio()
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