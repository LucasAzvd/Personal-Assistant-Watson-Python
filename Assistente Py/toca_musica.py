import webbrowser as browser

class Playlist():
    def __init__(self, playlist):
        self.playlist = playlist

    def toca_musica(self, estilo): 
        if estilo == 'rock':
            browser.open('https://open.spotify.com/track/7JQet6yCd8rZX3oeVGqAyx')
        elif estilo == 'reggae':
            browser.open('https://open.spotify.com/track/6IISVH5YBVy9ZohIlSaHm8')

