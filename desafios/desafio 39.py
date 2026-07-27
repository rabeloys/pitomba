print('=' * 30)
print(f"{'ALISTAMENTO MILITAR':^30}")
print('=' * 30)
idade = int(input('Digite sua idade: '))
tempo_alistamento_falta = 18 - idade
tempo_alistamento_passou = idade - 18
if idade == 18:
    print('Já tá na hora de se alistar!')
elif idade > 18:
    print('Já passou da hora de se alistar!')
    print()
    print(f'Já passou {tempo_alistamento_passou} anos que era pra você ter se alistado!')
else:
    print('Ainda não está na hora de se alistar!')
    print()
    print(f'Ainda falta {tempo_alistamento_falta} anos para se alistar!')