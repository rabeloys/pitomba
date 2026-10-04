palavras = ('Banana', 'Manga', 'Melancia', 'Abacaxi', 'Laranja', 'Mouse', 'Teclado', 'Garrafa')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    vogais_encontradas = ()
    for letra in palavra:
        if letra in vogais:
            vogais_encontradas += (letra,)
    print(f'Na palavra {palavra}, temos as seguintes vogais: {vogais_encontradas}')