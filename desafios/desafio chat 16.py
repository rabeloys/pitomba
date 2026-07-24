print('=' * 30)
print(f'{"TERMÔMETRO":^30}')
print('=' * 30)
temperatura = int(input('Digite a temperatura: '))
if temperatura <= -30 or temperatura >= 50:
    print()
    print('-' * 30)
    print('Situação: Temperatura Invalida')
    print('-' * 30)
elif temperatura < 10:
    print()
    print('-' * 30)
    print('Situação: Tá frio hein, bota uma blusa ❄️')
    print('-' * 30)
elif temperatura >= 10 and temperatura <= 24:
    print()
    print('-' * 30)
    print('Situação: Temperatura ta boazinha')
    print('-' * 30)
elif temperatura >= 25 and temperatura <= 34:
    print()
    print('-' * 30)
    print('Situação: Demo do inferno PQP')
    print('-' * 30)
else:
    print()
    print('-' * 30)
    print('Situação: Achou o inferno PQP')
    print('-' * 30)