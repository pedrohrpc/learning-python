
class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self, likes = 1):
        self._likes += likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.likes} Likes'
    

class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.duracao} minutos - {self.ano} - {self.likes} Likes'

class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.temporadas} temporadas - {self.ano} - {self.likes} Likes'
    
class Playlist():
    
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #Define a classe como iterável, passando os programas como itens
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)
vingadores.dar_like(5)
atlanta.dar_like(3)
tmep.dar_like()
demolidor.dar_like(4)


filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas               #IF-ELSE em uma linha
    #print(f'{programa.nome} - {detalhes} - {programa.likes}')              #Formatação do print
    print(programa)

print(f'\n{playlist_fim_de_semana[0]}')
