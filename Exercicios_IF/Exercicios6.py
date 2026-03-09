"""
Exercício 6: Desconto de Compra
Enunciado:
 Uma loja oferece descontos de acordo com o valor da compra:
10% para compras até 200,00€.
15% para compras entre 200,01€ e 500,00€.
20% para compras acima de 500,00€.
 Desenvolva um Programa que leia o nome do cliente e o valor da compra e mostre o valor do desconto e o valor total a pagar.
Exemplo:
 Entrada: Cliente: João, Compra: 350
 Saída esperada:
 Nome: João
 Compra: 350,00€
 Desconto: 52,50€
 Total a pagar: 297,50€
"""

nome=""
compra=0
desconto=0
total=0

nome=input("Insira o seu nome:")
compra=int(input("Insira o valor de compra: "))

if compra <= 200:
    percentagem = 0.10  # 10%
elif compra <= 500:
    percentagem = 0.15  # 15%
else:
    percentagem = 0.20  # 20%

desconto = compra * percentagem
total = compra - desconto

print(f"Nome: {nome}")
print(f"Compra: {compra:}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total a pagar: {total:.2f}€")