"""
1.	Ordenar uma lista de palavras por ordem alfabética (A → Z)
Objetivo: Reordenar as palavras, comparando carácter por carácter, como se estivesses a fazer o papel da função sorted().
Exemplo:
["banana", "uva", "abacaxi", "laranja"]
Resultado esperado:
["abacaxi", "banana", "laranja", "uva"]
Como fazer:
•	Compara as palavras duas a duas.
•	Usa o código ASCII de cada letra para decidir qual vem antes.
•	Se duas palavras começarem pela mesma letra, continua a comparação na letra seguinte.
•	Se uma palavra for prefixo da outra (como "casa" e "casamento"), a mais curta deve vir primeiro.
"""

"""
palavras = ["banana", "uva", "abacaxi", "laranja"]
"""
palavras = ["abacaxi", "uva", "banana", "laranja"]

for i in range(len(palavras)):
    for j in range(0, len(palavras) - i - 1):
        
        if palavras[j] > palavras[j + 1]:
            
            palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

print(palavras)