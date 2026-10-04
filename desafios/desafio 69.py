mais_18 = 0
homens = 0
mulheres_menos_20 = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    continuar = str(input('Deseja continuar? (S/N) ')).strip().upper()
    if continuar == 'N':
        break
    else:
        continue
print(f'O total de pessoas com mais de 18 anos é de: {mais_18}')
print(f'O total de homens cadastrados é de: {homens}')
print(f'O total de mulheres com menos de 20 anos é de: {mulheres_menos_20}')