maior = 0
menor = 0
for n in range(1, 7):
    numero = int(input('Digite um número inteiro: '))
    if n == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'O maior número é {maior}, e o menor numero é {menor}. A diferença entre eles é {maior - menor}')