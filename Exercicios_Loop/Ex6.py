"""
Exercício 6: Crie um algoritmo que mostre os 10 primeiros números primos.
"""


primos = []
numero_atual = 2  # Começamos no 2, pois o 1 não é primo

# O loop continua até a lista ter 10 números
while len(primos) < 10:
    divisores = 0
    
    # Verifica se o numero_atual é primo
    for i in range(1, numero_atual + 1):
        if numero_atual % i == 0:
            divisores += 1
            
    # Se for primo, guarda na lista
    if divisores == 2:
        primos.append(numero_atual)
        
    # Passa para o próximo número para testar na próxima volta
    numero_atual += 1

print(f"Os 10 primeiros números primos são: {primos}")