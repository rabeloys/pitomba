soma = 0
maior = 0
menor = 0
nome_homem = ''
for informacao in range(1, 5):
    nome = str(input('Digite seu nome: ')).lower().strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()
    soma += idade

    if sexo == 'M':
        if idade > maior:
            maior = idade
            nome_homem = nome
    if sexo == 'F' and idade < 20:
        menor += 1
media_idade = soma / 4
print(f'Mulheres abaixo de 20 anos tem: {menor}')
print(f'O homem mais velho, {nome_homem}, tem: {maior} anos')
print(f'A média de idade dos participantes é: {media_idade:.1f}')