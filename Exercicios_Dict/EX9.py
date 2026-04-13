"""
Exercício 9: Notas dos alunos
Cria um dicionário com o nome dos alunos e as suas respetivas listas de notas:
notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}
Calcula e imprime a média de cada aluno, com o seguinte formato:
João: 8.0
Maria: 9.0
Ana: 7.0
"""

alunos = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}
totalJoao = 0


for notas in alunos["João"]:
    totalJoao = totalJoao + notas  # Exemplo: somar 5 a cada idade

media = totalJoao/3
print("O total dos valores do João é: ", totalJoao)
print("A Média do João é:", media)

totalMaria = 0

for notas in alunos["Maria"]:
    totalMaria = totalMaria + notas  # Exemplo: somar 5 a cada idade

media = totalMaria/3
print("O total dos valores da Maria é: " , totalMaria)
print("A Média da Maria é:", media)

totalAna = 0

for notas in alunos["Ana"]:
    totalAna = totalAna + notas  # Exemplo: somar 5 a cada idade

media = totalAna/3
print("O total dos valores da Ana é: ", totalAna)
print("A Média da Ana é:", media)