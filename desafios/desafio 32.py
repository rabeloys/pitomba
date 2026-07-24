ano = int(input('Escolha um ano e descubra se ele é bissexto: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} \033[1;32mé\033[m bissexto')
else:
    print(f'O ano {ano} \033[1;31mnão\033[m é bissexto')