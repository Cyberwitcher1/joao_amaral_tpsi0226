"""
6. Estado do servidor
Recebe um dicionário com as chaves "status" e "tempo_resposta".
Retorna:
•	“Servidor ativo” se o status for “ok”
•	“Servidor lento” se o status for “ok” e o tempo de resposta for maior que 200 ms
•	“Servidor indisponível” se o status for “erro”
•	“Estado desconhecido” caso contrário
Exemplo:
Entrada → {"status": "ok", "tempo_resposta": 350}
Saída → Servidor lento
"""

status = input("Escreva o status(ok/erro): ")
if status == ("erro"):
    print("Servidor indisponível")
else:
    tempo_resposta = int(input("Escreva o valor do tempo de resposta: "))

    mensagem = {"status": status, "tempo_resposta": tempo_resposta}

    match mensagem:
        case {"status": "ok"} if tempo_resposta >= 350:
            print("Servidor ativo")

        case {"status": "ok"} if tempo_resposta > 200 and tempo_resposta < 350:
            print("Servidor lento")
        case _:
            print("Estado desconhecido")


