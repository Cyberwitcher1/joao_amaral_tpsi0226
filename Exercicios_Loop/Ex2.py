"""
Exercício 2: Ler 10 números, e determinar se o número par e número impar.
"""
pares = []
impares = []

for i in range(1, 11):
    numero = int(input(f"Escreva o {i}º número: "))
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Pares encontrados: {pares}")
print(f"Ímpares encontrados: {impares}")
