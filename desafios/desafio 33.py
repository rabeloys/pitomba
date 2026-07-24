numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o terceiro numero: '))
if numero1 > numero2 and numero1 > numero3:
    print(f'O \033[32m{numero1}\033[m é o maior')
if numero2 > numero1 and numero2 > numero3:
    print(f'O \033[32m{numero2}\033[m é o maior')
if numero3 > numero1 and numero3 > numero2:
    print(f'O \033[32m{numero3}\033[m é o maior')
if numero1 < numero2 and numero1 < numero3:
    print(f'O \033[31m{numero1}\033[m é o menor')
if numero2 < numero1 and numero2 < numero3:
    print(f'O \033[31m{numero2}\033[m é o menor')
if numero3 < numero1 and numero3 < numero2:
    print(f'O \033[31m{numero3}\033[m é o menor')