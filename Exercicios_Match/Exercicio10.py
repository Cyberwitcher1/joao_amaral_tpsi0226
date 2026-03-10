"""
10. Jogo: Pedra, Papel ou Tesoura
Cria um programa que receba duas jogadas:
•	Jogador 1
•	Jogador 2
Usa match para determinar o resultado:
•	Pedra ganha de Tesoura
•	Tesoura ganha de Papel
•	Papel ganha de Pedra
•	Se forem iguais, é Empate
Exemplo:
Entrada →
Jogador 1: pedra
Jogador 2: tesoura
Saída → Jogador 1 venceu
"""

jogador1 = input("Primeiro jogador -> Escolhe Pedra, Papel ou Tesoura: ")
jogador2 = input("Segundo jogador -> Escolhe Pedra, Papel ou Tesoura: ")


jogada = {"jogador1": jogador1, "jogador2": jogador2}

match jogada:
    case {"jogador1": "pedra","jogador2": "tesoura"}:
        print("O primeiro jogador ganhou!")
    case {"jogador1": "pedra","jogador2": "pedra"}:
        print("Empatou!")
    case {"jogador1": "pedra", "jogador2": "papel"}:
        print("O segundo jogador ganhou!")
    case {"jogador1": "tesoura", "jogador2": "papel"}:
        print("O primeiro jogador ganhou!")
    case {"jogador1": "tesoura", "jogador2": "tesoura"}:
        print("Empatou!")
    case {"jogador1": "tesoura", "jogador2": "pedra"}:
        print("O segundo jogador ganhou!")
    case {"jogador1": "papel", "jogador2": "pedra"}:
        print("O primeiro jogador ganhou!")
    case {"jogador1": "papel", "jogador2": "papel"}:
        print("Empatou!")
    case {"jogador1": "papel", "jogador2": "tesoura"}:
        print("O segundo jogador ganhou!")
    case _:
        print("Erro ao escrever a jogada!")