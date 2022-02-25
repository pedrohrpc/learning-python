
class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    #Property serve para acessar o atributo atraves de um get, porém com sintaxe simplificada (cliente.nome) e mantendo o encapsulamento
    @property
    def nome(self):
        return self.__nome.title()

    #Também simplifica a sintaxe do set mantendo o encapsulamento (cliente.nome = nome)
    @nome.setter
    def nome(self, nome):
        self.__nome = nome