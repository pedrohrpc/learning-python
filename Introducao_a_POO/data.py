
class Data():

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(str(self.dia) + "/" + str(self.mes) + "/" + str(self.ano))