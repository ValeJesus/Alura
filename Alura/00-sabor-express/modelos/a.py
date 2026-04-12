class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao): 
        self.nome = nome
        self.artista = artista 
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def __str__(self):
        return f'{self.nome} \n {self.artista} \n {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} \n {musica.artista} \n {musica.duracao}')

musicas_alee = Musica('Segredo', 'Alee feat. Brandao085', '2:31')

musicas = [musicas_alee]

Musica.listar_musicas()
