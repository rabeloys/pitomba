maior = 0
menor = 0
for c in range(1, 9):
    idade = int(input('Digite a sua idade: '))
    if c == 1:
        maior = idade
        menor = idade
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade
diferenca = maior - menor
print(f'A maior idade é {maior} e a menor idade é {menor} e a diferença de idade é: {diferenca}')