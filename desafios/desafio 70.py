estoque = ['Bola', 'Balde', 'Bateria']
sacola = []
valor = 0
menor_preco = 400
mais_de_75 = 0
menor_preco_produto = ''
while True:
    escolha = int(input('Escolha um produto:' 
    '\n[1] Bola - 50,00' 
    '\n[2] Balde - 100,00' 
    '\n[3] Bateria - R$300,00\n'))
    if escolha >= 4 or escolha < 1:
         print('\nEscolha inválida! Tente novamente.\n')
         continue
    if escolha == 1:
        sacola.append(estoque[escolha - 1])
        valor += 50
        if 50 < menor_preco:
            menor_preco = 50
            menor_preco_produto = 'Bola'
    elif escolha == 2:
        sacola.append(estoque[escolha - 1])
        valor += 100
        mais_de_75 += 1
        if 100 < menor_preco:
                menor_preco = 100
                menor_preco_produto = 'Balde'
    elif escolha == 3:
        sacola.append(estoque[escolha - 1])
        valor += 300
        mais_de_75 += 1
        if 300 < menor_preco:
                menor_preco = 300
                menor_preco_produto = 'Bateria'
    continuar = str(input('\nDeseja continuar? [S/N] \n')).strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue
    if continuar != 'S' and continuar != 'N':
         print('\nEscolha invalida! Tente novamente.\n')
         str(input('\nDeseja continuar? [S/N] \n')).strip().upper()
print(f'\nVocê comprou {len(sacola)} produtos! O total gasto foi R${valor:.2f}')
print(f'\nO produto mais barato que você comprou foi {menor_preco_produto} que custou R${menor_preco:.2f}\n')
print(f'Você tem {mais_de_75} produtos que custam mais de R$75,00.\n')