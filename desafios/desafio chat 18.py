print('=' * 30)
print(f'{"BATERIA DO CONTROLE":^30}')
print('=' * 30)
bateria = int(input('Digite a porcentagem de bateria do seu controle: '))
if bateria < 0 or bateria > 100:
    print()
    print('-' * 30)
    print('Valor invalido')
    print('-' * 30)
elif bateria >= 0 and bateria <= 20:
    print()
    print('-' * 30)
    print('O controle precisa descansar um pouco 🪫')
    print('-' * 30)
elif bateria >= 21 and bateria <= 50:
    print()
    print('-' * 30)
    print('Daqui a pouco ele desliga, coloca pra carregar um pouco 😴')
    print('-' * 30)
elif bateria >= 51 and bateria <= 80:
    print()
    print('-' * 30)
    print('O controle ta bom pra jogar 😀')
    print('-' * 30)
else:
    print()
    print('-' * 30)
    print('Tá recarregado, aproveita 🔋')
    print('-' * 30)