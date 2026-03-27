"""
Exercício 1: Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.
"""
"""
for i in range(1, 31):
    print(i)
"""

p = 0
print("Pares: ")
while p < 61:  
    print(p)


    p += 2  

i = 1
print("Impares: ")
while i < 63:  
    print(i)


    i += 2  

"""
OUTRA MANEIRA MEMNOS "PREGUIÇOSA"
"""

print()
print()
print("Pares: ")

for pares in range(62):
    if pares % 2 == 0:
        print(pares)


print()
print()
print("Impares: ")
for impares in range(63):
    if impares % 2 != 0:
        print(impares)


