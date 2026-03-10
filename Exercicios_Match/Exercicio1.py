"""
1. Tipo de dia
Cria um programa que receba o nome de um dia da semana e diga se é dia útil ou fim de semana.
Exemplo:
Entrada → domingo
Saída → Fim de semana
"""

dia=input("Insira o dia da semana: ")


match dia:
    case "Segunda-feira":
        print("Dia útil")
    case "Terca-feira":
        print("Dia útil")
    case "Quarta-feira":
        print("Dia útil")
    case "Quinta-feira":
        print("Dia útil")
    case "Sexta-feira":
        print("Dia útil")
    case "Sabádo":
        print("Fim de semana")
    case "Domingo":
        print("Fim de semana")
    case _:
        print("Opção errada")