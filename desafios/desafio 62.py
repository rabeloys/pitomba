c = 0
contador = 0
a1 = int(input('Digite o primeiro termo de uma PA: '))
q = int(input('Digite a razão dessa PA: '))
while c < 10:
   a1 += q
   print(f'Os proximos termos serão: {a1}')
   c += 1
mais = int(input('Quantos termos mais você quer ver? '))
while mais != 0:
    contador = 0
    while contador < mais:
        a1 += q
        print(f'Os proximos termos serão: {a1}')
        contador += 1
    mais = int(input('Quantos termos mais você quer ver? '))