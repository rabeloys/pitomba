hora = int(input('Que horas são? '))
minuto = int(input('Quantos minutos são? '))
if hora < 0 or hora > 23:
    print('Hora invalida')
elif minuto < 0 or minuto > 59:
    print('Minuto invalido')
elif hora >= 5 and hora <= 11:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
elif hora >= 18 and hora <=23:
    print('Boa noite')
else:
    print('Boa madrugada')