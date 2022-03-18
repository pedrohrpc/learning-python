
import re

url = 'https://bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')


if not padrao_url.match(url):
    raise ValueError('URL não é válida')

print('URL válida')