print('=' * 30)
print(f'{"\033[1;30mSE\033[m\033[1;92mMÁ\033[m\033[1;91mFO\033[m\033[1;93mRO\033[m":^70}')
print('=' * 30)
semaforo = input('Digite a cor do semáforo: ').strip().capitalize()
if semaforo not in ['Verde', 'Amarelo', 'Vermelho', 'Amarela', 'Vermelha']:
    print()
    print('-' * 30)
    print('\033[31mCor invalida ❌\033[m')
    print('-' * 30)
elif semaforo == 'Vermelho' or semaforo == 'Vermelha':
    print()
    print('-' * 30)
    print('\033[1;91mPare 🛑\033[m')
    print('-' * 30)
elif semaforo == 'Amarelo' or semaforo == 'Amarela':
    print()
    print('-' * 30)
    print('\033[1;93mAtenção ⚠️\033[m')
    print('-' * 30)
else:
    print()
    print('-' * 30)
    print('\033[1;92mPode passar 🚗\033[m')
    print('-' * 30)