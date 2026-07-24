import random
numero_sortido = random.randint(0, 5)
adivinhacao = int(input('Tente adivinhar o número em que o computador está pensando (0-5): '))
if adivinhacao > 5 or adivinhacao < 0:
    print('Tente novamente com algum número entre 0 e 5')
elif adivinhacao == numero_sortido:
    print(f'\033[1;92mParabens você acertou, o número sorteado foi {numero_sortido}\033[m 🎉🎉🎉')
else:
    print(f'\033[1;91mQue pena, o número sorteado foi\033[m \033[1;96m{numero_sortido}')