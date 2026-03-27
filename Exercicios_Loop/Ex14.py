"""
Exercício 14: Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for).
"""


numero = 0
contador = 1


for j in range(1, 101):
    print()
    contador+= 1
    numero+= 1
    print(f"A tabuada de {numero} ")

    for i in range(1, 11):

        resultado=numero*i
        print(f"{numero} x {i} = {resultado}")

    
