salario = float(input('Qual o seu salario: '))
if salario <= 1250:
    aumento = salario * 15 / 100
else:
    aumento = salario * 10 / 100
salario_final = salario + aumento
print(f'O seu novo salario é de \033[92mR${salario_final:.2f}\033[m')