"""
Exercício 3: Ler a nota de 10 alunos, calcular a media e mostrar essa média.
"""

media = 0

aluno = 0
soma_notas = 0

for aluno in range(1, 11):
    nota_atual = int(input(f"Escreva a nota do {aluno} aluno: "))
    soma_notas += nota_atual

media = soma_notas / 10
print(f"A soma das notas é: ", soma_notas)
print(f"A media das notas é: ", media)