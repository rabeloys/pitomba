valor_compra = float(input('Digite o valor da compra: '))
if valor_compra <= 100:
    valor_desconto = 0
elif valor_compra > 100 and valor_compra <= 300:
    valor_desconto = valor_compra * 0.05
else:
    valor_desconto = valor_compra * 0.15
valor_final = valor_compra - valor_desconto
print(f'Seu desconto foi de R${valor_desconto:.2f}')
print(f'O valor da sua compra foi {valor_compra:.2f}, com os descontos ficam {valor_final:.2f}')