"""
Exercício 1: Criar um dicionário simples
Cria um dicionário chamado alunos que receba nome, idade e curso de cada aluno:
1-	Inserir
2-	Listar
O mesmo deve imprimir cada elemento do dicionário no seguinte formato por cada aluno:
Exemplo:
nome: Maria
idade: 20
curso: Engenharia
"""
base_dados = []

alunos = {
}

menu = 1

while (menu==1):
    escolha = int(input("Selecione uma das opções(1 - Inserir, 2 - Listar, 3 - sair): \n"))
    if escolha == 1:
        nome_input = input("Nome: ")
        idade_input = input("Idade: ")
        curso_input = input("Curso: ")
        base_dados.append({
            'nome': nome_input, 
            'idade': idade_input,
            'curso': curso_input
        })

    
    if escolha == 2:
            print()
            print(base_dados)
            print()
    if escolha == 3:
         menu = 0



