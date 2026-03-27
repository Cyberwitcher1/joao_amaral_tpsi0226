"""
Exercício 10: Elabore um programa que lê um número e escreve quantos divisores ele possui.
"""
valor = int(input("Escreva um valor: "))
divisores = 0
valor_inicial = valor 

while valor_inicial > 0:
    if valor % valor_inicial == 0: 
        divisores += 1
    valor_inicial -= 1 
print(f"A quantidade de divisores é: {divisores}")