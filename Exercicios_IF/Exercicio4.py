"""
Exercício 4: Verificar se o Cheque Pode Ser Descontado
Enunciado:
 Desenvolva um Programa que leia o saldo inicial de um cliente de banco e leia também o valor de um cheque. Analise se o cheque pode ser descontado. Se o cheque não puder ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo atualizado.
Exemplo:
 Entrada: Saldo = 500, Cheque = 300
 Saída esperada:
 Cheque descontado, saldo: 200
"""


entrada=int(input("Insira o saldo inicial do cliente: "))
cheque=int(input("Insira o valor do cheque: "))



while cheque>entrada:
    print("Não pode ser descontado!");
    print("Tente outro valor!")
    
    cheque=int(input("Insira o valor do cheque: "))

desconto=entrada-cheque;  
print(f"Cheque descontado... Saldo actual: {desconto}");
    
