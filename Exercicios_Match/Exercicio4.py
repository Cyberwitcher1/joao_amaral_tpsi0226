"""
4. Tipo de dado
Analisa um valor e retorna o seu tipo:
•	Número inteiro
•	Número decimal
•	String numérica
•	String textual
•	Lista
•	Tipo desconhecido
Exemplo:
Entrada → [10, 20, 30]
Saída → Lista
"""

dados = "gandas cenas mê putz 123" 
numeros = "0123456789"

match dados:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case list():
        print("Lista")
    case str() if any(n in numeros for n in dados):
        print("String numérica")
    case str():
        print("String textual")
    case _:
        print("Tipo desconhecido")