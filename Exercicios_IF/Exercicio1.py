# Exercício 1: Converter Segundos em Horas, Minutos e Segundos 
# Enunciado:
#  Desenvolva um programa que assuma uma entrada em segundos e a converta para horas, minutos e segundos.
# Exemplo:
#  Entrada: 3665 segundos
#  Saída esperada: 1 hora, 1 minuto e 5 segundos.

# segundos=36665 # segundos
segundos=120
#input
minutos=(60 - segundos)
horas=(60 - minutos)


if segundos>=60:
    print(minutos)
elif minutos>=60:
    print(horas)
else:
    print(segundos)


