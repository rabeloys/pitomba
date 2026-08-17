numeros = []
maior = 0
menor = 0
pares = 0
impares = 0
for n in range(1,9):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n == 1:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
crescente = sorted(numeros)
decrescente = sorted(numeros , reverse=True)
print(*numeros)
print(*crescente)
print(*decrescente)
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
print(f'Tem {pares} números pares')
print(f'Tem {impares} números ímpares')
print(f'Tem {len(numeros)} números')
print(f'O primeiro número é: {numeros[0]}')
print(f'O último número é: {numeros[-1]}')