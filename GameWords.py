def jogo():
    import random

    print("Bem-vindo ao jogo!")
    nome = input("Por favor, digite o seu nome: ")
    
    print(f"Olá, {nome}! Vamos começar.")

    dificuldade = input("Escolha a dificuldade do jogo (fácil, médio, difícil): ")
    if dificuldade.lower() == 'fácil':
        tentativas = 10
        numero_secreto = random.randint(1, 10)
    elif dificuldade.lower() == 'médio':
        tentativas = 7
        numero_secreto = random.randint(1, 20)
    else:
        tentativas = 5
        numero_secreto = random.randint(1, 50)

    print(f"Você tem {tentativas} tentativas para adivinhar o número secreto.")

    for tentativa in range(tentativas):
        palpite = int(input("Digite o seu palpite: "))
        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número secreto.")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        else:
            print("O número secreto é menor. Tente novamente.")
        print(f"Você tem {tentativas - tentativa - 1} tentativas restantes.")

    print("Fim do jogo.")
    input(f"{nome}, pressione qualquer tecla para sair")

jogo()
