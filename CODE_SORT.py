import random

print("Jogo de Adivinhação de Número")

# gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# solicita ao usuário que adivinhe o número
tentativas = 0
while True:
    tentativa = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou o número em", tentativas, "tentativa(s).")
        break
    elif tentativa < numero_secreto:
        print("O número é maior. Tente novamente.")
    else:
        print("O número é menor. Tente novamente.")
