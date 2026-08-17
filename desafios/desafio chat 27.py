numero = int(input('Digite um número: '))
while numero != 10:
    print('Número incorreto\n')
    if numero > 10:
        diferenca = numero - 10
    else:
        diferenca = 10 - numero
    print(f'Errou por {diferenca:.0f}\n')
    numero = int(input('Digite um número: '))
print(f'{numero} está correto')