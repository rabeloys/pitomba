frase = str(input('Digite uma frase: ')).strip().lower()
if frase == frase[::-1]:
    print('É um palindromo')
else:
    print('Não é')