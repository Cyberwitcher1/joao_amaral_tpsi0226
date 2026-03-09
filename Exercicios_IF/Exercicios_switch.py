"""
Exercício Switch: Exibir Nome do Mês
Enunciado:
Leia um número inteiro de 1 a 12 e mostre o nome do mês correspondente. Caso o número não seja válido, mostre uma mensagem de erro.
Exemplo:
 Entrada: 5
 Saída esperada: Maio
"""

mes=int(input("Insira um número inteiro de 0 a 12: "))

if mes == int(1):
    print("O mês é Janeiro")
elif mes == int(2):
    print("O mês é Feveiro")
elif mes == int(3):
    print("O mês é Março")
elif mes == int(4):
    print("O mês é Abril")
elif mes == int(5):
    print("O mês é Maio")
elif mes == int(6):
    print("O mês é Junho")
elif mes == int(7):
    print("O mês é Julho")
elif mes == int(8):
    print("O mês é Agosto")
elif mes == int(9):
    print("O mês é Setembro")
elif mes == int(10):
    print("O mês é Outubro")
elif mes == int(11):
    print("O mês é Novembro")
elif mes == int(12):
    print("O mês é Dezembro")
else:
    print("Colocou um número errado!")


