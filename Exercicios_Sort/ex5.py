"""
5. Agrupar palavras pela letra inicial e ordenar cada grupo por ordem alfabética (A → Z)
Objetivo: Reorganizar as palavras em grupos que comecem com a mesma letra, e depois ordenar cada grupo manualmente.
Exemplo:
["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
Resultado esperado:
{
  'b': ['banana', 'bola'],
  'a': ['abacaxi', 'arroz'],
  'u': ['urso', 'uva']
}
Como fazer:
•	Cria um dicionário onde cada chave é uma letra inicial.
•	Coloca cada palavra no grupo correspondente.
•	Ordena cada grupo individualmente usando comparação com ord().
Este é o exercício mais completo: vais precisar de organizar, comparar e ordenar em dois níveis.
"""


palavras = ["urso", "bola", "uva", "arroz", "abacaxi", "banana"]
dicionario_completo = {}



for palavra in palavras:
    letra = palavra[0]
    if letra not in dicionario_completo:
        dicionario_completo[letra] = []
    dicionario_completo[letra].append(palavra)

print(dicionario_completo)

#for letra in dicionario_completo:
    #print(letra)



def ordenar():
  for valor in dicionario_completo.values():
   if valor[0] > valor[1]:
    valor[1], valor[0] = valor[0], valor[1]
    #print("Trocou")

ordenar()

print(dicionario_completo)




