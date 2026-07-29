numero = int(input('Digite um número inteiro: '))
primo = True
for c in range(2, numero):
    if numero % c == 0:
        primo = False
if primo:
    print('É primo')
else:
    print('Não é primo')