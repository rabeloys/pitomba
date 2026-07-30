maior = 0
menor = 0
pares = 0
impares = 0
soma = 0
for n in range(1, 16):
    numero = int(input('Digite um número inteiro: '))
    if n == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    soma += numero
media = soma / 15
print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')
print(f'Tem {pares} números pares.')
print(f'Tem {impares} números impares.')
print(f'A média dos números é: {media:.2f}.')