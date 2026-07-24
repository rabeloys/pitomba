produto = input('Digite o nome do produto: ').lower()
preco = float(input('Digite o valor do produto: '))
if preco > 200:
    desconto = preco * 0.2
    preco = preco - desconto
elif preco >= 100 and preco <= 200:
    desconto = preco * 0.1
    preco = preco - desconto
else:
    preco = preco
print(f'O valor de {produto} é R${preco:.2f}')