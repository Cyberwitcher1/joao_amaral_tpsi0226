"""
Exercícios 18: Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial.
6=3+2+1 .
"""

entrada = int(input("Digite: "))
divisores = 0


for i in range(entrada):
    i += 1 
    if entrada % i == 0:
        divisores = i
        print(f"{divisores} é um divisor de {entrada}")

