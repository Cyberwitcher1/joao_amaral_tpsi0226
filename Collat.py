numero = int(input("Escreva um numero: "))

while numero != 1:
    
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = 3 * numero + 1
        
    print(numero)
    

print("Chegamos ao 1! Fim da sequencia.")
    