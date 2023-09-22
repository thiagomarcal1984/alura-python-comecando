print("*******************************")
print("Bem vindo ao jogo de avinhação!")
print("*******************************")

numero_secreto = 43

chute_str = input("Digite o seu número: ")

print("Você digitou", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou.")
else:
    print("Você errou.")

print("Fim do jogo.")
