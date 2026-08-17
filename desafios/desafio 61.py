c = 0
a1 = int(input('Digite o primeiro termo de uma PA: '))
q = int(input('Digite a razão dessa PA: '))
while c < 10:
   a1 += q
   print(f'Os proximos termos serão: {a1}')
   c += 1