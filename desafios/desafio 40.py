nota1 = float(input('Coloque a primeira nota: '))
nota2 = float(input('Coloque a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Sua média foi {media:.2f}')
if media < 5:
    print('\033[1;91mREPROVADO!\033[M')
elif media >= 5 and media <= 6.9:
    print('\033[1;93mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;92mAPROVADO!\033[m')