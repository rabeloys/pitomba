numeros = []
for n in range(1, 7):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
crescente = sorted(numeros)
decrescente = sorted(numeros, reverse=True)
print(*numeros)
print(*crescente)
print(*decrescente)