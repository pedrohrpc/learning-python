
url = "https://byteBank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

print(url)

url_base = url[0:27]
url_param = url[28:len(url)]

print(url_base)
print(url_param)