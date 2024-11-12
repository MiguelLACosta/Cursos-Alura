class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = int(duracao)
        Musica.musicas.append(self)
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica_eminem = Musica('Monster', 'Eminem', '180')
musica_adele = Musica('Skyfall', 'Adele','150')
musica_otonoke = Musica('Otonoke', 'kuabara', '185')

Musica.listar_musicas()



