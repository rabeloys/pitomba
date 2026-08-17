n = 1
numeros = []
while n:
    n = int(input('Digite um número: '))
    if n != 0:
        numeros.append(n)
    elif n == 0:
        continua = str(input('\nVocê quer digitar mais números? [Y/N] ')).strip().upper()
        if continua == 'Y':
            n = int(input('Digite um número: '))
sum(numeros)
len(numeros)
media = sum(numeros) / len(numeros)
print(f'\nA média dos números é {media:.2f}')
print(f'O maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')