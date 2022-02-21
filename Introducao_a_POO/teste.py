

def cria_conta(numero, titular, saldo, limite):
    conta = {"Numero": numero, "Titular": titular, "Saldo": saldo, "Limite": limite}
    return conta

def deposita(conta, valor):
    conta["Saldo"] = conta["Saldo"] + valor

def saca(conta, valor):
    conta["Saldo"] = conta["Saldo"] - valor

def extrato(conta):
    print("Saldo: " + str(conta["Saldo"]))

