um_e_oitenta = 0
maior = 0
menor = 0
for a in range(1, 7):
    altura = float(input('Digite sua altura[M]: '))
    if a == 1:
        maior = altura
        menor = altura
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura
    if altura > 1.80:
        um_e_oitenta += 1
print(f'Tem {um_e_oitenta:.0f} pessoas com mais de 1.80m.')
print(f'A maior altura é: {maior:.2f}')
print(f'A menor altura é: {menor:.2f}')