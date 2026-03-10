"""
9. Processamento de requisição
Recebe um dicionário com as chaves "metodo" e "conteudo".
Retorna:
•	“Requisição GET recebida” se o método for “GET”
•	“Requisição POST com dados válidos” se o método for “POST” e o conteúdo não estiver vazio
•	“Requisição POST sem dados” se o método for “POST” e o conteúdo estiver vazio
•	“Método não suportado” caso contrário
Exemplo:
Entrada → {"metodo": "POST", "conteudo": ""}
Saída → Requisição POST sem dados
"""



metodo = input("Escreve o método pretendido: ")
conteudo = input("Escreve o conteudo dos dados: ")

mensagem = {"metodo": metodo, "conteudo": conteudo}


match mensagem:
    case {"metodo": "GET"}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c:
        print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": c} if not c:
        print("Requisição POST sem dados")
    case _:
        print("Metodo não suportado")