numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
numero3 = int(input('Digite outro número inteiro: '))
maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)
soma = numero1 + numero2 + numero3
media = soma / 3
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
print(f'A soma desses números é {soma}')
print(f'A média desses números é {media:.1f}')
