"""
3. Ordenar os caracteres de uma palavra por ordem alfabética
Objetivo: Pega numa palavra e reorganiza as suas letras da mais "baixa" para a mais "alta", segundo o valor ASCII.
Exemplo:
"algoritmo"
Resultado esperado:
"agilmootr"
Como fazer:
•	Divide a palavra em caracteres.
•	Ordena os caracteres com base no valor de ord().
•	Junta novamente numa string.
Este exercício é útil para aprender como a ordenação funciona mesmo a nível de caracteres, não só de palavras inteiras.
"""

palavra = "Algoritmo"
caracteres_org = []
transformado = ""

""" Transformar string para valores númericos """

for caracter in palavra:
    caracteres = ord(caracter)
    caracteres_org.append(caracteres)

caracteres_org.sort()


for numero in caracteres_org:
    numeros = chr(numero)
    transformado += numeros


print(transformado)









"""
for i in range(len(palavra)):
    for j in range(0, len(palavra) - i - 1):
        
        if palavra[j].upper() < palavra[j + 1].upper():
            
            palavra[j], palavra[j + 1] = palavra[j + 1], palavra[j]"""


