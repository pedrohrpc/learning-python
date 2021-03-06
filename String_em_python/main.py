
#url = 'https://byteBank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
url = ' '

#print(url)

# Sanitização url
url = url.replace(' ', '') # Substitui uma string por outra ((nesse caso, remove os espaços))
url = url.strip() # Remove espaços e caracteres especiais de antes e depois da string


# Validação url
if url == '':
    raise ValueError('A url está vazia')

# Separa base de parametros
posicao_interrogacao = url.find('?')
url_base = url[:posicao_interrogacao]
url_param = url[posicao_interrogacao+1:]
print(url_base)
print(url_param)

# Busca valores
parametro = 'moedaOrigem'
posicao_parametro = url_param.find(parametro)
#print(posicao_parametro)
posicao_valor = posicao_parametro + len(parametro) + 1
#print(posicao_valor)
posicao_e_comercial = url_param.find('&', posicao_valor)  # Encontra o & a partir da posicao valor
#print(posicao_e_comercial)
valor = url_param[posicao_valor:] if posicao_e_comercial == -1 else url_param[posicao_valor:posicao_e_comercial]

print(valor)