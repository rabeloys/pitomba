produto = input('Digite o nome do produto: ')
preco_produto = float(input('Digite o valor do produto: '))
if preco_produto < 100:
    preco_final = preco_produto
else:
    preco_desconto = preco_produto * 10 / 100
    preco_final = preco_produto - preco_desconto
print()
print(f'O novo preço de {produto} é R$\033[92m{preco_final}')