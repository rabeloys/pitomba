import time
estoque = ['Camisa', 'Shorts', 'Tênis', 'Tenis', 'Boné', 'Bone', 'Meias']
carrinho = []
menu = 0
preco = 0
while menu != 5:
    print('=' * 30)
    print(f'{"MERCADO DRV":^30}')
    print('=' * 30)
    menu = int(input('O que deseja fazer?\n[1] - Ver produtos em estoque\n[2] - Adicionar produto ao carrinho\n[3] - Ver carrinho\n[4] - Finalizar compra\n[5] - Sair\n'))
    if menu == 1:
        print(f'Produtos em estoque: {", ".join(estoque)}', end='.\n')
        time.sleep(3)
    elif menu == 2:
        produto = str(input('Digite o nome do produto que você quer adicionar ao carrinho: ')).strip().capitalize()
        if produto in estoque:
            carrinho.append(produto)
            if produto == 'Camisa':
                preco += 50
                print(f'O seguinte produto foi adicionado ao seu carrinho: {produto}! Valor do item: R$50,00\n')
            elif produto == 'Shorts':
                preco += 40
                print(f'O seguinte produto foi adicionado ao seu carrinho: {produto}! Valor do item: R$40,00\n')
            elif produto == 'Tênis' or produto == 'Tenis':
                preco += 100
                print(f'O seguinte produto foi adicionado ao seu carrinho: {produto}! Valor do item: R$100,00\n')
            elif produto == 'Boné' or produto == 'Bone':
                preco += 30
                print(f'O seguinte produto foi adicionado ao seu carrinho: {produto}! Valor do item: R$30,00\n')
            elif produto == 'Meias':
                preco += 10
                print(f'O seguinte produto foi adicionado ao seu carrinho: {produto}! Valor do item: R$10,00\n')
        else:
            print('Produto indisponivel')
        continuar = str(input('Deseja continuar a compra? [S/N] ')).strip().upper()
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar a compra? [S/N] ')).strip().upper()
    elif menu == 3:
         print(f'Produtos no carrinho: {", ".join(carrinho)}', end='.\n')
         time.sleep(3)
    elif menu == 4:
         if len(carrinho) == 0:
              print('Carrinho vazio, não é possível finalizar a compra.')
              time.sleep(3)
         else:
            if preco >= 200:
                desconto = preco * 0.2
                preco -= desconto
                print('\nVocê ganhou um desconto de 20% na sua compra!')
                print(f'O valor do desconto: R$ {desconto:.2f}\n')
            print(f'Produtos no carrinho: {", ".join(carrinho)}', end='.\n')
            print(f'O valor total da compra foi: R$ {preco:.2f}')
            break