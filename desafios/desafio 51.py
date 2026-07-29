a1 = int(input('Digite o primeiro termo de uma PA: '))
q = int(input('Digite a razão dessa PA: '))
for c in range(1, 11):
   a1 += q
   print(f'Os proximos termos serão: {a1}')