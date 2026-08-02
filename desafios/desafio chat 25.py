maior_idade = 0
menor_idade = 0
soma = 0
for c in range(1, 9):
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        maior_idade += 1
    if idade < 18:
        menor_idade += 1
    soma += idade
media = soma / 8
print(f'Tem {maior_idade} maiores de idade, e {menor_idade} menores de idade, e a média de idade entre eles é {media:.2f}')