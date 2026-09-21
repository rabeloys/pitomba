import random
rodadas = 1
vitorias = 0
while True:
    escolha = int(input('Escolha um valor: '))
    par_ou_impar = str(input('Par ou ímpar? (P/I): ')).strip().upper()
    escolha_pc = random.randint(0, 10)
    soma = escolha + escolha_pc
    if soma % 2 == 0:
        ganhador = 'P'
        print(f'Você jogou {escolha} e o computador {escolha_pc}. Deu  {soma}. PAR')
    else:
        ganhador = 'I'
        print(f'Você jogou {escolha} e o computador {escolha_pc}. Deu  {soma}. ÍMPAR')
    if par_ou_impar == ganhador:
        vitorias += 1
    else:
        break
    rodadas += 1
print(f'Você perdeu com {vitorias} vitórias seguidas. Porém durou {rodadas} rodadas.')