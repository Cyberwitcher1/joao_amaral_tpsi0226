"""
Exercício 12: Elabore um programa que leia quantos números quer que se efetue a soma, subtrações, divisões, multiplicações e no fim por meio de um acumulador diga quantas operações foram efetuadas. Exemplo introduzindo o número 60 o programa deve apresentar 60 a somar, dividir multiplicar e subtrair por todos os números menores que ele.
"""
acumalador_operacoes = 0
numero_inicial = int(input("Introduza um número: "));
numero_final = 0


for i in range(1, numero_inicial):
    resultado_soma = numero_inicial + i
    resultado_subtracao = numero_inicial - i
    resultado_multiplicacao = numero_inicial * i
    resultado_divisao = numero_inicial / i
    acumalador_operacoes += 4
    print(f"{numero_inicial} + {i} = {resultado_soma}")
    print(f"{numero_inicial} - {i} = {resultado_subtracao}")
    print(f"{numero_inicial} x {i} = {resultado_multiplicacao}")
    print(f"{numero_inicial} / {i} = {resultado_divisao}\n")
print(f"A quantidade de operações efetuadas é: {acumalador_operacoes}")
