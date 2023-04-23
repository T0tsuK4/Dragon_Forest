import random
from time import sleep

def jogar():
    print("Você está em uma floresta misteriosa e vê um dragão se aproximando de você.")
    sleep(2)
    print("O que você faz?")
    sleep(2)
    print("a) Tenta correr e se esconder")
    print("b) Enfrenta o dragão")

    escolha = input("Sua escolha: ")
    sleep(3)
    if escolha == "a":
        print("Você correu e se escondeu. O dragão não te achou e você conseguiu escapar!")
    elif escolha == "b":
        print("Você decidiu enfrentar o dragão. Escolha uma arma para lutar:")
        print("a) Espada")
        print("b) Arco e flecha")
        print("c) Machado")

        arma = input("Sua escolha: ")

        if arma in ["a", "b", "c"]:
            resultado = random.choice(["vitória", "derrota"])
            if resultado == "vitória":
                sleep(3)
                print("Você derrotou o dragão!")
            else:
                sleep(3)
                print("O dragão te derrotou. Melhor sorte na próxima vez!")
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            jogar()
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        jogar()

jogar()
