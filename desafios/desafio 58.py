import random
tentativas = []
adivinhacao = 0
numero_sortido = random.randint(0, 10)
while adivinhacao != numero_sortido:
    adivinhacao = int(input('Tente adivinhar o número em que o computador está pensando (0-10): \n'))
    tentativas.append(adivinhacao)
    if adivinhacao > 10 or adivinhacao < 0:
        print('\nTente novamente com algum número entre 0 e 10\n')
    elif adivinhacao == numero_sortido:
        print(f'\n\033[1;92mParabens você acertou, o número sorteado foi {numero_sortido}\033[m 🎉🎉🎉\n')
print(f'Você conseguiu depois de {len(tentativas)} tentativas')