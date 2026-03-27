"""
Exercícios 16: Elabore um programa que constitua a média de 30 números pares que sejam introduzidos. Validando a entrada de números inteiros entre 1 e 50.
"""


contador = 0
numeros = 0

while contador < 30:
    i = int(input("Escreva um número: "))
    if i >= 1 and i <= 50:
            contador = contador + 1
            numeros = numeros + i
            print(numeros)

    else:
          print("Tem que ser entre 1 e 50!")
          print("Tenta outravez!")
          break
          

media = numeros/30
print(f"A media é {media}")


    