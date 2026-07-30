#Primeiro com mais de 50 linhas :)
mais_velho = 0
mais_nova = 0
mais_peso = 0
mais_leve = 0
nome_homem = ''
mulher_sem20 = 0
homen = 0
mulhe = 0
maior_idade = 0
menor_idade = 0
soma_idade = 0
maior_idade_homem = 0
for c in range(1, 8):
    nome = str(input('Digite seu nome: ')).capitalize().strip()
    idade = int(input('Digite sua idade: '))
    peso = float(input('Digite seu peso: '))
    sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()
    if c == 1:
        mais_velho = idade
        mais_nova = idade
    if idade > mais_velho:
        mais_velho = idade
    if idade < mais_nova:
        mais_nova = idade
    soma_idade += idade
    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem = nome
    if sexo == 'F' and idade < 20:
        mulher_sem20 += 1
    if c == 1:
        mais_peso = peso
        mais_leve = peso
    if peso > mais_peso:
        mais_peso = peso
    if peso < mais_leve:
        mais_leve = peso
    if sexo =='M':
        homen += 1
    if sexo == 'F':
        mulhe += 1
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
media_idade = soma_idade / 7
print(f'A média das idades é: {media_idade:.2f}')
print(f'A pessoa mais velha tem: {mais_velho} anos')
print(f'A pessoa mais nova tem: {mais_nova} anos')
print(f'A pessoa mais pesada tem: {mais_peso}KG')
print(f'A pessoa mais leve tem: {mais_leve}KG')
print(f'Tem {homen} homens')
print(f'Tem {mulhe} mulheres')
print(f'Tem {maior_idade} maiores de idade')
print(f'Tem {menor_idade} menores de idade')
print(f'Tem {mulher_sem20} mulheres com menos de 20 anos')
print(f'O homem mais velho se chama {nome_homem}')
