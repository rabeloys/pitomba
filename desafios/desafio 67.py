n = 0
while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        print('\nNúmero inválido!\n')
        break
    for n in range(1, 11):
        print(f'{numero} x {n} = {numero * n}')