"""
Exercício 9: Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100.
 (Use o ciclo do ... while)
"""

valor = 0 

while True:
    valor = int(input("Escreva um valor entre 1 e 100: "))

    if valor >= 1 and valor <= 101:
        break

    print("Inseriste um numero errado...")

print("Inseriste um número certo...")
