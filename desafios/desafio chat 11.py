import random
jokenpo = ['pedra', 'papel', 'tesoura']
escolha_pc = random.choice(jokenpo).capitalize()
print('=' * 20)
print('Bem-Vindo ao jokenpo')
print('=' * 20)
escolha_jogador = input('Escolha entre pedra, papel e tesoura e tente ganhar da máquina: ').capitalize()
if escolha_jogador not in ['Pedra', 'Papel', 'Tesoura']:
    print('Jogada invalida')
elif escolha_jogador == escolha_pc:
    print('Empate')
elif escolha_jogador == 'Pedra' and escolha_pc == 'Papel':
    print('Computador ganhou')
elif escolha_jogador == 'Tesoura' and escolha_pc == 'Pedra':
    print('Computador ganhou')
elif escolha_jogador == 'Papel' and escolha_pc == 'Tesoura':
    print('Computador ganhou')
elif escolha_jogador == 'Pedra' and escolha_pc == 'Tesoura':
    print('Você ganhou')
elif escolha_jogador == 'Tesoura' and escolha_pc == 'Papel':
     print('Você ganhou')
elif escolha_jogador == 'Papel' and escolha_pc == 'Pedra':
    print('Você ganhou')
print(f'Computador jogou {escolha_pc}')
print(f'Você jogou {escolha_jogador}')