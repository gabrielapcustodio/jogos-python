import random

def jogar():

    imprime_boas_vindas()

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    nivel = pergunta_nivel_de_dificuldade()
    total_de_tentativas = calcula_tentativas(nivel)

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        checa_chute_invalido(chute)
        pontos = calcula_pontos(numero_secreto, chute, pontos)

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            calcula_erros(numero_secreto, chute, chute_maior, chute_menor, rodada, total_de_tentativas, pontos)

def imprime_boas_vindas():
    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação.")
    print("*********************************")

def pergunta_nivel_de_dificuldade():
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Define o nível: "))
    return nivel

def calcula_tentativas(nivel):
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    return total_de_tentativas

def calcula_pontos(numero_secreto, chute, pontos):
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos
    return pontos

def calcula_erros(numero_secreto, chute, chute_maior, chute_menor, rodada, total_de_tentativas, pontos):
    if (chute_maior):
        print("Você errou! O chute foi alto demais!")
        if (rodada == total_de_tentativas):
            print("O número secreto era {} e você fez {} pontos.".format(numero_secreto, pontos))
    elif (chute_menor):
        print("Você errou! O chute foi baixo demais!")
        if (rodada == total_de_tentativas):
            print("O número secreto era {} e você fez {} pontos.".format(numero_secreto, pontos))

def checa_chute_invalido(chute):
    chute_negativo = chute < 1
    chute_maior_cem = chute > 100

    if (chute_negativo or chute_maior_cem):
        print("Você deve escolher um número entre 1 e 100.")

if(__name__ == "__main__"):
    jogar()