"""
Exercício 7: Inverter chaves e valores
Tens o seguinte dicionário:
d = {'a': 1, 'b': 2, 'c': 3}
Cria um novo dicionário que tenha os valores como chaves e as chaves como valores. Resultado esperado:
{1: 'a', 2: 'b', 3: 'c'}
"""

dados = {'a': 1, 'b': 2, 'c': 3}

novos_dados = {}

for chave, valor in dados.items():

    nova_chave = valor
    novo_valor = chave

    novos_dados[nova_chave] = novo_valor


print(novos_dados)


"""valor: chave for chave, valor in d.items()}
print(novoDicionario)"""
