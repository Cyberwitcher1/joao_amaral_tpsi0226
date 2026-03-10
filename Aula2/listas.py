#Lista em inteiros

numeros=[1,5,8,3,9,23]

for numero in numeros:
    print(numero)

numeros[2]=6

for numero in numeros:
    print(numero)

#Lista de Strings

#ind d1  0       1        2
nomes=["João","Pedro","António"]
#ind d2 0123   01234   0123456

for nome in nomes:
    print(nome)

#print("ola," "mundo", end="\t", sep="
print("", end="\n\n\n\n")
print(nomes[0])

nomes[0]="Tiago"
print(nomes[0][2])
print(nomes)


#remover da lista
nomes.remove("Pedro")
print(nomes)
nomes.pop(0)
print(nomes)

nomes.append("Dario")
print(nomes)
print(nomes.count("Dario"))

print(nomes)
print(len(nomes))
nomes.index()