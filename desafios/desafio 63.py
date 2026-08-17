anterior = 0
atual = 1
proximo = 0
contador = 0
numero = int(input('Digite um número: '))
while contador < numero:
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    contador += 1
    if contador < numero:
        print(atual, end= ', ')
    else:
        print(atual, end='')