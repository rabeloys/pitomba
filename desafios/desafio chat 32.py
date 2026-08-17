numeros = []
pares = []
for c in range(1, 6):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
print(f'Você digitou os seguintes números: {numeros}')
print(f'Sendo {pares} pares')