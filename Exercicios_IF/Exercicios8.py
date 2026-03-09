"""
Exercício 8: Calcular a Média de 10 Notas e informar notas iguais ou acima da media 
Enunciado:
Crie um programa que leia a nota de 10 alunos (notas de 0 a 20), calcule a média das notas e mostre a média. Além disso, informe quantos alunos ficaram com a nota igual ou acima da média. 
"""


aluno1=("Rui")
nota1=float(input("Insira a nota do primeiro aluno: "))

aluno2=("Pedro")
nota2=float(input("Insira a nota do segundo aluno: "))

aluno3=("João")
nota3=float(input("Insira a nota do terceiro aluno: "))

aluno4=("Ricardo")
nota4=float(input("Insira a nota do quarto aluno: "))

aluno5=("Luís")
nota5=float(input("Insira a nota do quinto aluno: "))

aluno6=("João")
nota6=float(input("Insira a nota do sexto aluno: "))

aluno7=("Maria")
nota7=float(input("Insira a nota setimo aluno: "))

aluno8=("Luísa")
nota8=float(input("Insira a nota do oitavo aluno: "))

aluno9=("Ana")
nota9=float(input("Insira a nota do nono aluno: "))

aluno10=("Afonso")
nota10=float(input("Insira a nota do decimo aluno: "))



media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10) / 10



"""if nota1 or nota2 or nota3 or nota4 or nota5 or nota6 or nota7 or nota7 or nota8 or nota9 or nota10 >= media:
    print(f"Alunos que estão acima da média: {aluno1} + {aluno2} + {aluno3} + {aluno4} + {aluno5} + {aluno6} + {aluno7} + {aluno8} + {aluno9} + {aluno10} ")"""

print()
print("Os alunos que aprovaram foram:")
if nota1 >= media:
    print(aluno1)
if nota2 >= media:
    print(aluno2)
if nota3 >= media:
    print(aluno3)
if nota4 >= media:
    print(aluno4)
if nota5 >= media:
    print(aluno5)
if nota6 >= media:
    print(aluno6)
if nota7 >= media:
    print(aluno7)
if nota8 >= media:
    print(aluno8)
if nota9 >= media:
    print(aluno9)
if nota10 >= media:
    print(aluno10)


print()
print(f"Media: {media:.1f}")