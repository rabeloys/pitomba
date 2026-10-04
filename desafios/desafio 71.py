# notas disponiveis: 1, 10, 20, 50
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0
while True:
    sacar = int(input('Digite o valor que deseja sacar: '))
    if sacar <= 0:
          print('Valor inválido! Tente novamente.')
          continue
    notas_50 = sacar // 50
    sacar %= 50
    notas_20 = sacar // 20
    sacar %= 20
    notas_10 = sacar // 10
    sacar %= 10
    notas_1 = sacar // 1
    print(f'Notas de 50: {notas_50}')
    print(f'Notas de 20: {notas_20}')
    print(f'Notas de 10: {notas_10}')
    print(f'Notas de 1: {notas_1}')
    continuar_saque = str(input('Deseja realizar outro saque? [S/N] ')).strip().upper()
    while continuar_saque != 'S' and continuar_saque != 'N':
                print('Escolha inválida! Tente novamente.')
                continuar_saque = str(input('Deseja realizar outro saque? [S/N] ')).strip().upper()
    if continuar_saque == 'N':
        break
    elif continuar_saque == 'S':
        continue