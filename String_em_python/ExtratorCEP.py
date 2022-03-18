

endereco = "Rua Maria Dirce Ribeiro 296, apartamento 301, Santa Monica, Uberlândia, MG, 38408194"

import re

# cep = 5 digitos + hífen (opcional) + 3 digitos

# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
# ? mostra que é opcional
# [0-9] indica quais valores podem ser (de 0 a 9)
# {N} indica a quantidade de vezes que se repete ({0,1} indica que pode ter 0 ou 1 ocorrencias)


padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)