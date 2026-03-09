"""
Exercício 5: Ler 3 Valores e Exibir em Ordem Crescente e Decrescente
Enunciado:
 Ler 3 valores inteiros e apresentar os valores dispostos em ordem crescente e decrescente.
Exemplo:
 Entrada: num1 = 4, num2 = 9, num3 = 2
 Saída esperada:
 Crescente: 2, 4, 9
 Decrescente: 9, 4, 2
"""



val1=int(input("Insira o primeiro valor: "))
val2=int(input("Insira o segundo valor: "))
val3=int(input("Insira o terceiro valor: "))

numeros=val1, val2, val3;

crescente=sorted(numeros);
decrescente=sorted(numeros, reverse=True);

print(f"Os valores em ordem crescente: {crescente}" );
print(f"Os valores em ordem descrescente: {decrescente}" );