"""
8. Operação matemática
Recebe uma operação (em texto) e dois números.
Operações válidas: "soma", "subtrai", "multiplica", "divide".
Exemplo:
Entrada →
Operação: "divide"
Número 1: 20
Número 2: 4
Saída → 5
"""

operacao = (input("Qual operação queres?(Operações validas: soma, subtracao, multiplicacao, divisao) "))

primeiro = int(input("Escreva o primeiro número: "))
segundo = int(input("Escreva o segundo número: "))

soma = primeiro+segundo
subtracao = primeiro-segundo
multiplicacao = primeiro*segundo
divisao = primeiro / segundo


match operacao:
    case "soma":
        print(soma)
    case "subtracao":
        print(subtracao)
    case "multiplicacao":
        print(multiplicacao)
    case "divisao":
        print(divisao)
    case _:
        print("Operacao desconhecida!")