numeros = []
for n in range(1, 6):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
crescente = sorted(numeros)
print(*numeros)
print(*crescente)