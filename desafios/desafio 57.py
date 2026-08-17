sexo = ' '
while sexo not in 'M' and sexo not in 'F':
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()
if sexo == 'M':
    print('\nSeu sexo é: Masculino')
else:
    print('\nSeu sexo é: Feminino')