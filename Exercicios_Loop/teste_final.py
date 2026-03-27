"""
Teste Final: Elabore uma base de dados de clientes de uma fábrica de materiais. O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%, se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%. O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível busca direta por número de cliente.
"""
lista_clientes = []
proximo_id = 0

while True:
    print("1 - Inserir cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente por número")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nomCli = input("Nome do cliente: ")
        morada = input("Escreva a morada: ")
        tel = input("Escreva o número de telemóvel: ")
        nif = input("Escreva o nif do cliente: ")
        compra = int(input("Escreva o valor da compra: "))

        if 100 >= compra <= 200:
            desconto = compra * 0.05
        if 200 >= compra < 500:
            desconto = compra * 0.10
        else:
            desconto = compra * 0.15
        
        DivFin = compra - desconto

        proximo_id += 1

        novo_cliente = {
            "Id de cliente": proximo_id, 
            "Nome": nomCli,
            "Morada": morada,
            "Telemóvel": tel,
            "Nif": nif,
            "Compra": compra,
            "DivFin": DivFin
        }

        lista_clientes.append(novo_cliente)
    elif escolha == "2":
        print(lista_clientes)
        pass
    elif escolha == "3":
        id_escolhido = int(input("Escolha o id do cliente: \n"))

        for cliente in lista_clientes:
            if cliente["Id de cliente"] == id_escolhido:
                print(cliente)
                break
        else:
            print("Cliente não encontrado.")
    elif escolha == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")