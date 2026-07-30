maior_salario = 0
maior_idade = 0
mais_velho = ''
ganha_3000 = 0
soma = 0
for s in range(1, 6):
    nome = str(input('Digite seu nome: ')).capitalize().strip()
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salario: '))
    if s == 1:
        maior_salario = salario
    if salario > maior_salario:
        maior_salario = salario
    if idade > maior_idade:
        maior_idade = idade
        mais_velho = nome
    if salario > 3000:
        ganha_3000 += 1
    soma += salario
media = soma / 5
print(f'A média dos salarios é: {media:.2f}')
print(f'O funcionario mais velho é: {mais_velho}')
print(f'O maior salario é: {maior_salario:.2f}')
print(f'{ganha_3000} ganham mais de 3000 no mês')