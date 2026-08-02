import random
import time
vida = 100
xp = 0
dano = 0
multiplicador_xp = 1
multiplicador_moeda = 1
moedas = 0
bolso = 0
vitorias = 0
derrotas = 0
inimigos = ['Conquista', 'Cthulhu', 'Sócrates', 'Zumbi', 'Demiurgo', 'Higgs', 'Hades', 'Zagreu', 'Melinoe', 'Nuclear']
nome = str(input('Digite seu nome: ')).strip().capitalize()
escolha_classe = int(input('Escolha uma classe: [1] Mago(a), [2] Guerreiro(a), [3] Ladino(a): '))
print('=' * 30)
print(f'{"START FANTASY DE" + " " +nome.strip().upper():^30}')
print('=' * 30)
if escolha_classe == 1:
    print(f'{nome} você será um(a) \033[1;35mMago(a)\033[m')
elif escolha_classe == 2:
    print(f'{nome} você será um(a) \033[1;31mGuerreiro(a)\033[m')
elif escolha_classe == 3:
    print(f'{nome} você será um(a) \033[1;34mLadino(a)\033[m')
else:
    print('Classe ainda em desenvolvimento!')
    exit()
#vida extra
if escolha_classe == 1:
    vida += 50
elif escolha_classe == 2:
    vida += 100
elif escolha_classe == 3:
    vida += 75
#multiplicador xp
if escolha_classe == 1:
    multiplicador_xp += 0.5
elif escolha_classe == 2:
    multiplicador_xp = 1
elif escolha_classe == 3:
    multiplicador_xp += 0.1
#multiplicador moeda
if escolha_classe == 1:
    multiplicador_moeda = 1
elif escolha_classe == 2:
    multiplicador_moeda += 0.5
elif escolha_classe == 3:
    multiplicador_moeda += 1
for c in range(1, 13):
    inimigo = random.choice(inimigos)
    time.sleep(0.5)
    print('-' * 30)
    time.sleep(1)
    print(f'Um {inimigo} apareceu!')
    time.sleep(0.5)
    print('-' * 30)
    ganha = str(input('Você ganha a batalha? [Y/N] ').strip().upper())
    if ganha == 'Y':
        vitorias += 1
        if inimigo == 'Zumbi':
            xp += 9 * multiplicador_xp
            moedas += 5 * multiplicador_moeda
        elif inimigo == 'Conquista':
            xp += 25 * multiplicador_xp
            moedas += 45 * multiplicador_moeda
        elif inimigo == 'Cthulhu':
            xp += 40 * multiplicador_xp
            moedas += 30 * multiplicador_moeda
        elif inimigo == 'Sócrates':
            xp += 70 * multiplicador_xp
            moedas += 20 * multiplicador_moeda
        elif inimigo == 'Demiurgo':
            xp += 55 * multiplicador_xp
            moedas += 34 * multiplicador_moeda
        elif inimigo == 'Higgs':
            xp += 58 * multiplicador_xp
            moedas += 10 * multiplicador_moeda
        elif inimigo == 'Hades':
            xp += 90 * multiplicador_xp
            moedas += 120 * multiplicador_moeda
        elif inimigo == 'Zagreu':
            xp += 70 * multiplicador_xp
            moedas += 100 * multiplicador_moeda
        elif inimigo == 'Melinoe':
            xp += 60 * multiplicador_xp
            moedas += 75 * multiplicador_moeda
        elif inimigo == 'Nuclear':
            xp += 50 * multiplicador_xp
            moedas += 65 * multiplicador_moeda
        bolso += moedas
        time.sleep(0.25)
        print(f'\033[1;93mMoedas ganhas: {moedas:.0f}\033[m')
        time.sleep(0.25)
        print(f'\033[1;93mMoedas totais: {bolso:.0f}\033[m')
        time.sleep(0.5)
        print(f'\033[1;95mXP: {xp:.0f}\033[m')
    elif ganha == 'N':
        sequencia_y = 0
        if inimigo == 'Zumbi':
            dano = 5
        elif inimigo == 'Conquista':
            dano = 15
        elif inimigo == 'Cthulhu':
            dano = 25
        elif inimigo == 'Sócrates':
           dano = 20
        elif inimigo == 'Demiurgo':
            dano = 35
        elif inimigo == 'Higgs':
            dano = 18
        elif inimigo == 'Hades':
            dano = 24
        elif inimigo == 'Zagreu':
            dano = 27
        elif inimigo == 'Melinoe':
            dano = 30
        elif inimigo == 'Nuclear':
            dano = 10
        vida -= dano
        derrotas += 1
        if vida <= 0:
            print('-' * 30)
            print(f'Você perdeu com \033[1;93m{moedas} moedas\033[m, \033[1;95m{xp} de XP\033[m, \033[1;91m{derrotas} derrotas\033[m e \033[1;32m{vitorias} vitorias\033[m')
            print('-' * 30)
            exit()
        time.sleep(0.25)
        print(f'Dano Sofrido: \033[1;31m{dano:.0f}\033[m')
        print(f'Vida: \033[1;31m{vida}\033[m')
    else:
        if inimigo == 'Zumbi':
            dano = 5
        elif inimigo == 'Conquista':
            dano = 15
        elif inimigo == 'Cthulhu':
            dano = 25
        elif inimigo == 'Sócrates':
            dano = 20
        elif inimigo == 'Demiurgo':
            dano = 35
        elif inimigo == 'Higgs':
            dano = 18
        elif inimigo == 'Hades':
            dano = 24
        elif inimigo == 'Zagreu':
            dano = 27
        elif inimigo == 'Melinoe':
            dano = 30
        elif inimigo == 'Nuclear':
            dano = 10
        vida -= dano
        derrotas += 1
        print('Jogada Invalida')
        print(f'Dano Sofrido: \033[1;31m{dano:.0f}\033[m')
        print(f'Vida: \033[1;31m{vida}\033[m')
    if c % 4 == 0:
        print('=' * 30)
        print(f'{"LOJA":^30}')
        print('=' * 30)
        print(f'Você possui {bolso:.0f} moedas.')
        print('Pegue o que deseja: ')
        opcoes_loja = int(input('O que você deseja: [1] Poção - 50 moedas e + 50 vida [2] Sair '))
        preco_pocao = 50
        if opcoes_loja == 1:
            quantas_pocoes = int(input('Quantidade: '))
            pocoes_preco = preco_pocao * quantas_pocoes
            diferenca_pocoes = pocoes_preco - bolso
            if pocoes_preco > bolso:
                print(f'Pegue mais moedas. Falta apenas {diferenca_pocoes} moedas.')
            else:
                bolso -= pocoes_preco
                vida += 50 * quantas_pocoes
                print(f'Vida curada! Agora você tem \033[1;31m{vida}\033[m pontos de vida.')
if xp == 0:
    print(f'Você terminou com {xp} de XP! Você é Novato')
elif 50 <= xp <= 199:
    print(f'Você terminou com {xp} de XP! Você é Aventureiro')
elif 200 <= xp <= 399:
    print(f'Você terminou com {xp} de XP! Você é Guerreiro da Luz')
elif 400 <= xp <= 599:
    print(f'Você terminou com {xp} de XP! Você é Supremo da Luz')
else:
    print(f'Você terminou com {xp} de XP! Você é Deus da Luz')
if derrotas > vitorias:
    print(f'Você perdeu com \033[1;93m{moedas} moedas\033[m, \033[1;95m{xp} de XP\033[m, \033[1;91m{derrotas} derrotas\033[m e \033[1;32m{vitorias} vitorias\033[m')
elif vitorias > derrotas:
    print(f'Você ganhou com \033[1;93m{moedas} moedas\033[m, \033[1;32m{vitorias} vitorias\033[m e \033[1;91m{derrotas} derrotas\033[m')