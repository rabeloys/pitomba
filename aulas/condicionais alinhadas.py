nome = str(input('Qual é o seu nome? ')).capitalize()
if nome == 'Diogo':
    print('Que nome bonito!')
elif nome == 'Hurmano' or nome == 'Chaves':
    print('Você talvez seja uma pessoa')
elif nome in 'Gabriel Orocinho Guanabara':
    print('Você é gay')
else:
    print(f'Vai se foder, {nome}')
print(f'Tenha um bom dia, {nome}')