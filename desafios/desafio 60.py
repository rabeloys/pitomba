f = 1
c = 1
c = int(input('Digite um número: '))
while c > 0:
    f *= c
    if c > 1:
        print(c, end= ' x ')
    else:
        print(c, end = ' = ')
    c -= 1
print(f)