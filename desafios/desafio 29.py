velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado e terá que pagar R$\033[91m{multa:.2f}\033[m')
else:
    print('\033[92mEstá livre da multa, pode ir\033[m')