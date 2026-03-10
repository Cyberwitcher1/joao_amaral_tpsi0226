"""
3. Tipo de pedido
Recebe um dicionário com as chaves "tipo" e "valor".
Exibe:
•	“Compra de X€” se tipo for “compra”
•	“Venda de X€” se tipo for “venda”
•	“Pedido desconhecido” caso contrário
Exemplo:
Entrada → {"tipo": "venda", "valor": 250}
Saída → Venda de 250€
"""

tipo_escolhido = input("Escolha um tipo (compra ou venda): ")

pedido = {"tipo": tipo_escolhido}
valor = 250

match pedido:
    case {"tipo": "compra"}:
        print(f"Compra de {valor}€")
    case {"tipo": "venda"}:
        print(f"Venda de {valor}€")
    case _:
        print("Pedido desconhecido")