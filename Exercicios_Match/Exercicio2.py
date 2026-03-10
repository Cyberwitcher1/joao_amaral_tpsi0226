"""
2. Classificação de nota
Lê uma nota (0–100) e retorna uma classificação:
•	90 ou mais → Excelente
•	70–89 → Bom
•	50–69 → Suficiente
•	Abaixo de 50 → Insuficiente
Exemplo:
Entrada → 70-89
Saída →  Bom
"""

"""
nota=(int(input("Insira uma nota: ")))


if nota >= 90:
    print("Excelente")
elif nota>=70 <= 89:
    print("Bom")
elif nota >= 50 <= 69:
    print("Suficiente")
else:
    print("Insuficiente")

"""

nota = int(input("Insira uma nota: "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if 70 <= n <= 89:
        print("Bom")
    case n if 50 <= n <= 69:
        print("Suficiente")
    case _:
        print("Insuficiente")

""" OUTRA SOLUÇÃO MAS COM IF

nota=(int(input("Insira uma nota: ")))


if nota >= 90:
    print("Excelente")
elif nota>=70 <= 89:
    print("Bom")
elif nota >= 50 <= 69:
    print("Suficiente")
else:
    print("Insuficiente")


"""