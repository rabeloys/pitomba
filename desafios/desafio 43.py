peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (pow(altura, 2))
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal')
elif 25 < imc <= 30:
    print('Você está sobrepeso')
elif 30 <= imc <= 40:
    print('Você é obeso')
else:
    print('Obesidade mórbida')