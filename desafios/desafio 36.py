valor_casa = float(input('Digite o valor da casa: R$'))
salario_comprador = float(input('Digite qual o seu salário: R$'))
pagar_anos = int(input('Em quantos anos deseja pagar? '))
prestacao_mensal = valor_casa / pagar_anos / 12
print(f'A prestação será de R${prestacao_mensal:.2f}')
if prestacao_mensal > salario_comprador * 30 / 100:
    print('\033[1;91mEmpréstimo negado\033[m')
else:
    print('\033[1;92mParabens, tá de casa nova hein\033[m')