nota1 = float(input('Coloque a primeira nota: '))
nota2 = float(input('Coloque a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'A sua média foi {media}. Aprovado!')
elif media >= 5 and media <= 6.9:
    print(f'A sua média foi {media}. Recuperação!')
else:
    print(f'A sua média foi {media}. Reprovado!')