import time
saldo = 0
movimentacoes_saldo = []
menu = 0
total_ganho = 0
total_gasto = 0
while menu != 5:
    print(f'{"=" * 30}')
    print(f'{"Banco DRV" :^30}')
    print(f'{"=" * 30}')
    menu = int(input('\nO que deseja fazer?\n[1] Adicionar saldo\n[2] Adicionar gasto\n[3] Ver saldo\n[4] Ver transações bancarias\n[5] Sair\n'))
    while menu > 5 or menu < 1:
        print('\n\033[1;91mOpção Invalida!\033[m')
        print()
        menu = int(input('O que deseja fazer?\n[1] Adicionar saldo\n[2] Adicionar gasto\n[3] Ver saldo\n[4] Ver transações bancarias\n[5] Sair\n'))
    if menu == 1:
        quantidade = float(input('Quanto deseja adicionar ao seu saldo? '))
        if quantidade < 0:
            print('Valor invalido! Tente a opção 2.')
            continue
        saldo += quantidade
        movimentacoes_saldo.append(quantidade)
        total_ganho += quantidade
    elif menu == 2:
        quantidade = float(input('Quanto você gastou? '))
        if quantidade < 0:
            print('Valor invalido! Tente a opção 1.')
            continue
        movimentacoes_saldo.append(quantidade * -1)
        saldo -= quantidade
        total_gasto += quantidade
    elif menu == 3:
        print(f'{"=" * 30}')
        print(f'{"Seu saldo":^30}')
        print(f'{"=" * 30}')
        print(f'R$ \033[92m{saldo:.2f}\033[m')
        time.sleep(3.5)
    elif menu == 4:
        print('=' * 30)
        print(f'{"Movimentações":^30}')
        print('=' * 30)
        for m in movimentacoes_saldo:
            if m > 0:
                print(f'+ {m:.2f}')
            else:
                print(f'- {m * -1:.2f}')
        time.sleep(3.5)
print(f'Total ganho: {total_ganho:.2f}')
print(f'Total gasto: {total_gasto:.2f}')
print(f'Saldo: {saldo:.2f}')