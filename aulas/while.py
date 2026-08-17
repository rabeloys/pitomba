pares = 0
impares = 0
n = 1
numeros = []
while n != 0 :
    n = int(input('Digite um numero: '))
    numeros.append(n)
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'\nTotal de números digitados: {len(numeros)}')
print(f'Total de pares: {pares}')
print(f'Total de ímpares: {impares}')
