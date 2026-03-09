"""
Exercício 3: Mostrar Números em Ordem Crescente e Decrescente
Enunciado:
 Crie 2 variáveis (num1 e num2) e leia o valor para cada uma delas. Mostre os valores de forma crescente e decrescente.
Exemplo:
 Entrada: num1 = 7, num2 = 2
 Saída esperada:
 Crescente: 2, 7
 Decrescente: 7, 2
"""

num1=7;
num2=2;

numeros=(num1,num2)

crescente=sorted(numeros);
decrescente=sorted(numeros, reverse=True);

print(crescente);
print(decrescente);