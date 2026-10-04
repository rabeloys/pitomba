aparece_9 = 0
pares = []
lugar_3 = []
for pos, n in enumerate(range(1, 5)):
    numero = int(input(f'Digite um número: '))
    if numero == 9:
        aparece_9 += 1
    if numero % 2 ==0:
        pares.append(numero)
    if numero == 3:
        lugar_3.append(pos)
print(f'Você digitou {aparece_9} vezes o número 9')
print(f'Os números pares são: {pares}')
print(f'O número 3 foi digitado na posição: {lugar_3[0] + 1}' if lugar_3 else 'O número 3 não foi digitado')