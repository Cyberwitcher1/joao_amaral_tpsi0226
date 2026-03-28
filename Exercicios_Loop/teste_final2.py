"""
Teste Final: Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1 (se é número Primo, Quantos divisores e números perfeitos) o Programa deve validar entradas entre 1 e 30.000, e parar de 10 em 10 valores com instrução para parar ou continuar. 

No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada. Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo introduzido) deve parar de 20 em 20 valores
"""


for i in range(30000, 0, -1):

    a = i
    divisores_p = 0

    for p in range(1, a + 1):
        if a % p == 0:
            divisores_p += 1

    if divisores_p == 2:
        print(i)
        print("É primo")
    else:
        print(i)
        print("Não é um número primo")


    entrada = i
    divisores_c = 0


    for c in range(entrada):
        c += 1 
        if entrada % c == 0:
            divisores = c
            print(f"{divisores} é um divisor de {entrada}")



    valor = i
    divisores = 0
    valor_inicial = valor 

    while valor_inicial > 0:
        if valor % valor_inicial == 0: 
            divisores += 1
        valor_inicial -= 1 
    print(f"A quantidade de divisores é: {divisores}\n")   




    if i % 10 == 0:
        cont = input("Deseja continuar? (s/n): ")
        if cont.lower() != 's':
            break

menu = True

while menu:
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair\n")
    entrada_2 = int(input("Escolha de 1 a 5: "))
    match entrada_2:
        case 1:
            numero = 0
            contador = 1
            numero_final = int(input("\nEscreva um número para a tabuada do +: "))
            if numero_final > 1 and numero_final < 1000:
                for j in range(1, numero_final+1):
                    print()
                    contador += 1
                    numero += 1

                    if (j-1) % 20 == 0:
                        cont = input("Deseja continuar? (s/n): ")
                        if cont.lower() != 's':
                            break

                    print(f"A tabuada de {numero} ")
                    for i in range(1, 11):
                        resultado=numero+i
                        print(f"{numero} + {i} = {resultado}")
            else:
                print("Tem que ser entre 1 e 1000!")
                continue



        case 2:
            numero = 0
            contador = 1
            numero_final = int(input("\nEscreva um número para a tabuada do -: "))
            if numero_final > 1 and numero_final < 1000:
                for j in range(1, numero_final+1):
                    print()
                    contador += 1
                    numero += 1

                    if (j-1) % 20 == 0:
                        cont = input("Deseja continuar? (s/n): ")
                        if cont.lower() != 's':
                            break


                    print(f"A tabuada de {numero} ")
                    for i in range(1, 11):
                        resultado=numero-i
                        print(f"{numero} - {i} = {resultado}")
            else:
                print("Tem que ser entre 1 e 1000!")
                continue

        case 3:
            numero = 0
            contador = 1
            numero_final = int(input("\nEscreva um número para a tabuada da multiplicação: "))
            if numero_final > 1 and numero_final < 1000:
                for j in range(1, numero_final+1):
                    print()
                    contador += 1
                    numero += 1

                    if (j-1) % 20 == 0:
                        cont = input("Deseja continuar? (s/n): ")
                        if cont.lower() != 's':
                            break


                    print(f"A tabuada de {numero} ")
                    for i in range(1, 11):
                        resultado=numero*i
                        print(f"{numero} * {i} = {resultado}")      
                else:
                    print("Tem que ser entre 1 e 1000!")
                    continue
            else:
                print("Tem que ser entre 1 e 1000!")
                continue


        case 4:
            numero = 0
            contador = 1
            numero_final = int(input("\nEscreva um número para a tabuada da divisão: "))
            if numero_final > 1 and numero_final < 1000: 
                for j in range(1, numero_final+1):
                    print()
                    contador += 1
                    numero += 1

                    if (j-1) % 20 == 0:
                        cont = input("Deseja continuar? (s/n): ")
                        if cont.lower() != 's':
                            break

                        
                    print(f"A tabuada de {numero} ")
                    for i in range(1, 11):
                        resultado=numero/i
                        print(f"{numero} / {i} = {resultado}")
            else:
                print("Tem que ser entre 1 e 1000!")
                continue
        case 5:
            print("Saiste...")
            break
        case _:
            print("Escreste um número errado!")


    

