"""
Exercícios 19:Escreva um programa que mostre os primeiros 60 números da serie bonatchi.
1, 1, 2, 3, 5, 8, 13, 21.
Como se constrói.

1+1=2
    1+2=3
        2+3=5
            3+5=8

a1+b1=c
    a2+b2=c
"""


"""
a_anterior = 1
a_atual = 1
a = a_anterior + a_atual 

b_anterior = 1
b_atual = 2
b = b_anterior + b_atual
"""

numero_anterior = 1
numero_atual = 1


for i in range(1, 60):
    numero_proximo = numero_anterior + numero_atual
    print(f"{numero_anterior} + {numero_atual} = {numero_proximo}")
    numero_anterior = numero_atual
    numero_atual = numero_proximo



