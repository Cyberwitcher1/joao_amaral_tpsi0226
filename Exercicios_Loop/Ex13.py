"""
Exercício 13: Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10)
"""

numero = int(input("Escreva um número para a tabuada: "))

print(f"A tabuada de {numero} ")
for i in range(1, 11):
    resultado =numero*i
    print(f"{numero} x {i} = {resultado}")
