numero = int(input('Digite um número: '))
unidade = (numero // 1 % 10)
if unidade % 2 == 0:
    print('É um número \033[1;94mpar\033[m')
else:
    print('É um número \033[1;91mímpar\033[m')