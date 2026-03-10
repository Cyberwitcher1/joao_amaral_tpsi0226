# operadores aritemeticos

# soma + sub -, div /, Mult *, mode % (resto da div), ** exponential

total=0
num=0
num=0

#input
num1=int(input("Insira número 1"))
num2=int(input("Insira número 2"))
num3=int(input("Insira número 3"))

total=num1+num2
print(f"soma : {total}")

total=num1-num2
print(f"sub : ",total," .")

total=num1/num2
print(f"div : {total}")

total=num1*num2
print("Mult : ",total," .")

# operadores de decisao

# == igualdade, != diferente, > maior que, < menor que
# >= maior ou igual e <=menor ou igual

# expressao 
# Val1 == Val2 = True/False

# operadores lógicos

# and e o or

# expressao
# val1 > val2 and val2 > val3 = true/false

#Exercicio encontra o maior e o menor
# If
val1=2
val2=3
val3=4

if val1>val2 and val2>val3:
    print("valor 1 é o maior, valor 3 é o menor")
elif val1>val3 and val3>val2:
    print("valor 1 é o maior, valor 2 é o menor")
elif val2>val1 and val1>val3:
    print("valor 2 é o maior, valor 3 é o menor")
elif val2>val3 and val1>val2:
    print("valor 2 é o maior, valor 2 o menor")
elif val3>val1 and val1>val2:
    print("valor 3 é o maior,valor 2 é o menor")
elif val3>val2 and val2>val3:
    print("valor 3 é o maior,valor 3 é o menor")


#match case (3,10 up)    
opc=int(input(0))

print("Prima 1 para bom dia")
print("Prima 2 para boa tarde")
print("Prima 3 para sair")

match opc:
    case "1":
        print("Bom dia")
    case "2":
        print("Boa noite")
    case "3":
        print("Sair do programa")
    case _:
        print("Errou opção")
