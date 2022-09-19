import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação.")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))
    if(nivel == 1):
        total_de_tentativas = 20

    elif(nivel == 2):
        total_de_tentativas = 10

    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        chute_negativo = chute < 1
        chute_maior_cem = chute > 100
        if(chute_negativo or chute_maior_cem):
            print("Você deve escolher um número entre 1 e 100.")
            continue

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(chute_maior):
                print("Você errou! O chute foi alto demais!")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {} e você fez {} pontos.".format(numero_secreto, pontos))
            elif(chute_menor):
                print("Você errou! O chute foi baixo demais!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {} e você fez {} pontos.".format(numero_secreto, pontos))

    print("*********************************")
    print("Fim do jogo.")


if(__name__ == "__main__"):
    jogar()