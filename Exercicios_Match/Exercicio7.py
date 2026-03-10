"""
7. Classificação de produto
Recebe um dicionário com as chaves "categoria" e "preco".
Retorna:
•	“Produto de luxo” se categoria for “eletrônico” e preço acima de 1000
•	“Produto comum” se categoria for “eletrônico” e preço até 1000
•	“Produto alimentar” se categoria for “alimento”
•	“Categoria desconhecida” caso contrário
Exemplo:
Entrada → {"categoria": "eletrônico", "preco": 1500}
Saída → Produto de luxo
"""

categoria = input("Escreva a categoria(eletrônico/alimento): ")
if categoria == "alimento":
    print("Producto alimentar")
else:
    preco = int(input("Escreve o preco: "))
    mensagem = {"categoria": categoria, "preco": preco }

    match mensagem:
        case {"categoria": "eletrônico"} if preco > 1000:
            print("Produto de luxo")
        case {"categoria": "eletrônico"} if preco <= 1000:
            print("Produto comum")
        case {"categoria": "alimento"}:
            print("Produto alimentar")
        case _:
            print("Categoria desconhecida")
