reta1 = float(input('informe o comprimento da primeira reta: '))
reta2 = float(input('informe o comprimento da segunda reta: '))
reta3 = float(input('informe o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode formar um triangulo')
    if reta1 == reta2 and reta2 == reta3:
        print('É um triangulo equilatero')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('É um triangulo isosceles')
    elif reta1 != reta2 or reta2 != reta3 or reta3 != reta1:
        print('É um triangulo escaleno')
else:
    print('Não pode formar um triangulo')