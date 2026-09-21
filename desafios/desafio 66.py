n = 0
soma = 0
while n != 999:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    n += 1
print(f'A soma dos {n} valores foi {soma}.')