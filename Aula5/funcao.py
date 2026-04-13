nomes=["da","fa","oi","da"]
#index   0    1    2   3
encontrado_list = []

def insert(nomesi:list):
    nomesi.append(input("insert um nome"))
 
def listar(nomesl:list, tipovalor:str):
    for nome in nomesl:
        print(tipovalor, " " , nome)
 
def delete(nomesd:list):
    nomesd.pop(int(input(" insert posiçao ")))

def procurar(nomesp:list, encontrado_list:list):
    encontrado_list.clear()
    nome=input("Insert nome de procura")
    for i in range(len(nomesp)):
        if nomesp[i] == nome:
            encontrado_list.append(i)
        """print("nome: ",nomesp[i] ," na posiçao ", i)"""

while True:
    print ("1 - inserir nome")
    print ("2 - listar nomes")
    print ("3 - delete nome")
    print ("4 - procurar nome")
    print ("5 - sair")
    opt=input("Escolha Opção")
    match opt :
        case "1":
            insert(nomes)
        case "2":
            listar(nomes)
            listar(encontrado_list)
        case "3":
            delete(nomes)
        case "4":
            procurar(nomes, encontrado_list)
            listar(encontrado_list)
            #print aqui os valores e posiçoes
        case "5":
            print("fim do programa")
            break
        case _:
            print("nao escolheu a opçao certa")