"""
Exercícios 15: Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255) e o código correspondente. Dispor de 20 em 20 com a condição de continuação ou saída do programa.
"""

for i in range(0, 256, 20):
    for j in range(i, min(i + 20, 256)):
        print(f"{j}: {chr(j)}")
    cont = input("Deseja continuar? (s/n): ")
    if cont.lower() != 's':
        break

