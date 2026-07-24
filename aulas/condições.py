n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
media_arredondada = round(media * 2) / 2
print(f'A média foi: {media_arredondada:.1f}')
if media_arredondada >=6:
    print('Aprovado')
else:
    print('Reprovado')