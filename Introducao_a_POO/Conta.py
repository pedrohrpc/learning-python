
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O extrato do " + self.__titular + " é de " + str(self.__saldo) + " reais")

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor):
        return valor<=(self.__saldo + self.__limite)

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor