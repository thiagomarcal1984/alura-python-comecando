print("*******************************")
print("Bem vindo ao jogo de avinhação!")
print("*******************************")

numero_secreto = 43
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
    # Interpolação da string com a função .format(...)
    print ('Tentativa {} de {}'.format(rodada, total_tentativas))
    # print (f'Tentativa {rodada} de {total_tentativas}') # Usando as f-strings.
    chute_str = input("Digite o seu número: ")
    if (chute_str == 'FIM'):
        exit()

    print("Você digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou.")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1
    
print("Fim do jogo.")
