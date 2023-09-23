import random

print("*******************************")
print("Bem vindo ao jogo de avinhação!")
print("*******************************")

numero_secreto = random.randrange(1, 101) # Exclui o número 100.
total_tentativas = 3
rodada = 1

for rodada in range(1, total_tentativas + 1):
    # Interpolação da string com a função .format(...)
    print ('Tentativa {} de {}'.format(rodada, total_tentativas))
    # print (f'Tentativa {rodada} de {total_tentativas}') # Usando as f-strings.
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou.")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
    
print("Fim do jogo.")
