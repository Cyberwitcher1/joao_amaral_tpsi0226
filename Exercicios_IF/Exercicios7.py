""" Exercício 7: Calcular a Média de Notas com Pesos
Enunciado:
 O sistema de avaliação de uma disciplina tem três provas com pesos diferentes. A primeira tem peso 2, a segunda tem peso 3, e a terceira tem peso 5. Crie um programa para calcular a média final de um aluno e mostrar se ele está APROVADO (nota >= 6) ou REPROVADO (nota < 6).
Exemplo:
 Entrada: Nota1 = 7, Nota2 = 6, Nota3 = 9
 Saída esperada:
 Média: 7.4
 Aprovado
 """


nota1=float(input("Insira a primeira nota: "))
nota2=float(input("Insira a segunda nota: "))
nota3=float(input("Insira a terceira nota: "))


media = (nota1*0.2)+(nota2*0.3)+(nota3*0.5)

"""
media = (nota1+nota2+nota3)/3
"""


if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

print(f"Nota 1: {nota1}, Nota 2: {nota2}, Nota 3: {nota3}")
print(f"Media: {media:.1f}")
