import random
jokenpo = ['pedra', 'papel', 'tesoura']
escolha_pc = random.choice(jokenpo).capitalize()
escolha_jogador = input('Escolha entre pedra, papel e tesoura e tente ganhar da máquina: ').capitalize()
print()
print(f'Computador jogou {escolha_pc}')
print(f'Você jogou {escolha_jogador}')
if escolha_jogador == escolha_pc:
    print('\033[1;33mEmpate\033[m')
elif escolha_jogador == 'Pedra' and escolha_pc == 'Papel':
    print('\033[1;91mComputador ganhou')
elif escolha_jogador == 'Tesoura' and escolha_pc == 'Pedra':
    print('Computador ganhou')
elif escolha_jogador == 'Papel' and escolha_pc == 'Tesoura':
    print('Computador ganhou\033[m')
elif escolha_jogador == 'Pedra' and escolha_pc == 'Tesoura':
    print('\033[92mVocê ganhou')
elif escolha_jogador == 'Tesoura' and escolha_pc == 'Papel':
     print('Você ganhou')
elif escolha_jogador == 'Papel' and escolha_pc == 'Pedra':
    print('Você ganhou\033[m')