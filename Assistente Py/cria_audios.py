from gtts import gTTS
#from subprocess import call    #OSX e Linux
from playsound import playsound #windows

#Create audios to proram execute
def cria_audio(audio):
    tts = gTTS (audio, lang='pt-br')
    tts.save('audios/feedback.mp3')

    #call(['afplay' , 'audios/hello.mp3'])   #OSX
    #call(['aplay' , 'audios/hello.mp3'])    #Linux
    playsound ('audios/feedback.mp3')         #windows

cria_audio('Pera  aê')