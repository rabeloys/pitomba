print('=' * 35)
print(f'{"BOLETIM ESCOLAR":^40}')
print('=' * 35)
nota = float(input('Nota: '))
if nota >= 7:
    print()
    print('-' * 30)
    print('Situação: Aprovado 🤩')
    print('-' * 30)
else:
    print()
    print('-' * 30)
    print('Situação: Reprovado 😭')
    print('-' * 30)