numeros = []
maior = 0
menor = 0
pares = 0
impares = 0
for n in range(1, 6):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
    elif numero % 2 == 1:
        impares += 1
    if n == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print(*numeros)
print(f'\nO maior número é: {maior}')
print(f'O menor número é: {menor}')
print(f'O primeiro número digitado foi {numeros[0]}')
print(f'O ultimo número digitado foi {numeros[-1]}')
print(f'Tem {pares} números pares')
print(f'Tem {impares} números impares')