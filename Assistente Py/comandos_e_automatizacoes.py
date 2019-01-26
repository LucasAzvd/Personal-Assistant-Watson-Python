from requests import get
from bs4 import BeautifulSoup
from toca_musica import Playlist
from respostas import Resposta


gera_resposta = Resposta('loading')

class Comandos():
    def __init__(self, trigger):
        self.trigger = trigger

    def executa_comandos(self, trigger): #Execute commands
        aux = Automatizacoes()
        if 'notícias' in trigger or 'notícia' in trigger:
            aux.ultimas_noticias()

        elif 'toca' in trigger and 'rock' in trigger:
            musica = Playlist('rock')
            musica.toca_musica('rock')

        elif 'toca' in trigger and 'reggae' in trigger:
            musica = Playlist('reggae')
            musica.toca_musica('reggae')

        elif 'tempo' in trigger:
            aux.previsao_tempo()

        else:
            gera_resposta.responde_simples('nao_entendi')


class Automatizacoes():

    def ultimas_noticias(self): #The last br news
        mensagem = ''
        site = get('https://news.google.com/news/rss?ned=pt_br&BR&hl=pt')
        noticias= BeautifulSoup(site.text, 'html.parser')
        for item in noticias.findAll('item')[:3]:
            aux_mensagem = item.title.text + '.\n'
            mensagem += aux_mensagem
        gera_resposta.cria_audio(mensagem)

    def previsao_tempo(self):
        site = get('http://api.openweathermap.org/data/2.5/weather?q=Belo%20Horizonte,br&APPID=3a5e2c93c0896fa3fa8dfec3fd8c9e5d&units=metric&lang=pt')
        clima = site.json()
        temperatura=clima['main']['temp']
        minima=clima['main']['temp_min']
        maxima=clima['main']['temp_max']
        descricao=clima['weather'][0]['description']
        mensagem = ("A temperatura aonde tu tais é " + str(temperatura) + " Graus. A máxima é: " + str(maxima) +
                    " Graus . A mínima é: " + str(minima) + " Graus. E tá com: " + str(descricao))
        gera_resposta.cria_audio(mensagem)    
