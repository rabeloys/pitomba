print('=' * 15)
print('Cadastro Civil')
print('=' * 15)
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print('Resultado:')
if idade >= 18:
    print(nome)
    print(idade)
    print('Maior de idade')
else:
    print(nome)
    print(idade)
    print('Menor de idade')