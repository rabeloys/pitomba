s = 0
p = 0
for c in range(0, 6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        s += numero
        p += 1
print(f'Você digitou números pares {p} vezes')
print(f'A soma dos números pares é: {s}')