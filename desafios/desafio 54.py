maiores = 0
menores = 0
for c in range(1, 8):
    ano_nasc = int(input('Digite o ano do seu nascimento: '))
    idade = 2026 - ano_nasc
    if ano_nasc > 2026:
        print('McFly é você?')
    elif idade < 18:
        menores += 1
    else:
        maiores += 1
print(f'Tem {menores} menores de idade e {maiores} maiores de idade')