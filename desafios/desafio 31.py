distancia = float(input('Qual a distância da viagem?(km): '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O valor da sua passagem será de: R$\033[92m{preco:.2f}\033[m')