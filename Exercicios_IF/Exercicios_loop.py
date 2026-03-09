"""
Exercício Loop: Identificar Números Pares e Ímpares
Enunciado:
 Leia 10 números e determine quantos são pares e quantos são ímpares.
Exemplo:
 Entrada: 2, 3, 5, 6, 8, 9, 10, 12, 14, 15
 Saída esperada:
 Pares: 6
 Ímpares: 4
"""
pares=0
impares=0

for i in range(1, 11):
    numero = int(input(f"Insira o {i}º número: "))
    
    if numero % 2 == 0:
        pares += 1 
    else:
        impares += 1

print()
print()
print(f"Os números pares são: {pares}")
print(f"Os números impares são: {impares}")


