reta1 = float(input('informe o comprimento da primeira reta: '))
reta2 = float(input('informe o comprimento da segunda reta: '))
reta3 = float(input('informe o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print()
    print('\033[1;92mPode formar um triangulo ✅\033[m')
else:
    print()
    print('\033[1;91mNão pode formar um triangulo ❌\033[m')