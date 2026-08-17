numeros = []
numero = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        numeros.append(numero)
soma = sum(numeros)
print(f'\nForam digitados {len(numeros)} números')
print(f'\nA soma dos números digitados é: {soma}')