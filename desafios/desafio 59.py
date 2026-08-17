soma = 0
multiplicacao = 0
maior = 0
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
operacao = int(input('\nO que você deseja fazer com esses números? \n[1]Somar\n'
                     '[2]Multiplicar\n'
                     '[3]Maior\n'
                     '[4]Novos números\n'
                     '[5]Sair\n'))
while operacao != 5:
    if operacao == 1:
        soma = num1 + num2
        print(f'A soma é {soma}\n')
    elif operacao == 2:
        multiplicacao = num1 * num2
        print(f'O produto é {multiplicacao}\n')
    elif operacao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior número é {maior}\n')
    if operacao == 4:
        num1 = int(input('Digite um valor: \n'))
        num2 = int(input('Digite outro valor: \n'))
    operacao = int(input('O que você deseja fazer com esses números? \n[1]Somar\n'
                         '[2]Multiplicar\n'
                         '[3]Maior\n'
                         '[4]Novos números\n'
                         '[5]Sair\n'))
print('Até logo!')