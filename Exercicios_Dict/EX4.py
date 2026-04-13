"""
Exercício 4: Verificar se uma chave existe
Dado o dicionário:
utilizador = {'nome': 'Carlos', 'idade': 28}
Escreve um código que verifique se a chave email está presente no dicionário e imprima uma mensagem adequada, por exemplo: "Email não encontrado."
"""

utilizador = {'nome': 'Carlos', 'idade': 28, 'email': 'carlossantos@mail.com'}



for nome in utilizador.keys():
    if nome == 'email':
        print("Email encontrado")


