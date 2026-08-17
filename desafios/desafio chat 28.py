import random
tentativas = 1
numero = int(input('Escolha um número entre 1 - 100: '))
numeros = random.randint(1, 100)
while numeros != numero:
    if numero > numeros:
        diferenca = numero - numeros
        print('O número é menor\n')
    else:
        diferenca = numeros - numero
        print('O número é maior\n')
    tentativas += 1
    print(f'Você errou por {diferenca}\n')
    numero = int(input('Escolha um número entre 1 - 100: \n'))
    print()
print(f'Parabéns você acertou em {tentativas} tentativas')