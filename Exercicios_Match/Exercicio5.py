"""
5. Análise de mensagem
Recebe uma mensagem e retorna:
•	“Saudação” se for “olá” ou “bom dia”
•	“Pergunta” se terminar com “?”
•	“Despedida” se contiver “tchau” ou “adeus”
•	“Mensagem genérica” caso contrário
Exemplo:
Entrada → “Tudo bem?”
Saída → Pergunta
"""

mensagem = input("Escreva uma mensagem: ")

match mensagem:
    case "olá" | "bom dia":
        print("Saudação")
    case "tchau" | "adeus":
        print("Despedida")
    case _ if mensagem[-1] == "?":
        print("Pergunta")
    case _:
        print("Mensagem genérica")