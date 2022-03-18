import re


class ExtratorURL:

    def __init__(self, url) -> None:
        self.url = self.sanitizar(url)
        self.validar()

    def sanitizar(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def validar(self):
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        if not padrao_url.match(self.url):
            raise ValueError('URL não é válida')

    def get_base(self):
        posicao_interrogacao = self.url.find('?')
        return self.url[:posicao_interrogacao]

    def get_parametros(self):
        posicao_interrogacao = self.url.find('?')
        return self.url[posicao_interrogacao+1:]

    def get_valor_param(self, parametro):
        url_param = self.get_parametros()
        posicao_parametro = url_param.find(parametro)
        posicao_valor = posicao_parametro + len(parametro) + 1
        posicao_e_comercial = url_param.find('&', posicao_valor)
        valor =  url_param[posicao_valor:] if posicao_e_comercial == -1 else url_param[posicao_valor:posicao_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url



url = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
print(url.get_base())
print(url.get_parametros())
print(url.get_valor_param('moedaOrigem'))
print(url.get_valor_param('moedaDestino'))
print(url.get_valor_param('quantidade'))