"""
4. Ordenar uma lista de palavras pela quantidade de letras minúsculas
 Objetivo: Contar quantas letras minúsculas há em cada palavra e ordená-las do menor para o maior número.
Exemplo:
["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
Resultado esperado:
["CÓDIGO", "intELIGENTE", "PYthon", "dados", "banana"]
Como fazer:
•	Conta, para cada palavra, quantos caracteres estão entre 'a' e 'z'.
•	Usa esse número como "peso" para ordenar.
•	Palavras com mais minúsculas vão para o fim da lista.
"""



palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]



def contar_minusculas(palavra):
    soma = 0
    for letra in palavra:
        if letra.islower():
            soma += 1
    return soma

palavras_ordenadas = sorted(palavras, key=contar_minusculas)

print(palavras_ordenadas)



"""
palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
palavras_org = []

for palavra in palavras:
    print(palavra)
    quant_caracteres = 0
    

    for caracteres in palavra:
        if caracteres.islower():
            quant_caracteres = quant_caracteres + 1
            print(f"Encontrei uma minúscula: {caracteres}")
            print(quant_caracteres)
        
print(quant_caracteres)

"""
            





