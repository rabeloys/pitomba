aluno_maior_nota = ''
maior_nota = 0
soma = 0
for n in range(1, 6):
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    nota = float(input('Digite a sua nota: '))
    if nota >= 11 or nota < 0:
        print('Nota invalida. Tente novamente com nota de 0 á 10')
        break
    if n == 1:
        maior_nota = nota
    if nota > maior_nota:
        maior_nota = nota
    if nota == maior_nota:
        if nota == maior_nota:
            aluno_maior_nota = nome
    soma += nota
media = soma / 5
print(f'O aluno que tirou a maior nota foi: {aluno_maior_nota}')
print(f'A maior nota tirada foi: {maior_nota}')
print(f'A média da turma foi: {media:.1f}')