print('FORMAS DE PAGAMENTO')
print('[1] À vista dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
metodo_pagamento = int(input('Escolha um metodo de pagamento: '))
valor_produto = float(input('Insira o valor do produto: '))
if metodo_pagamento == 1:
    desconto_dinheiro = valor_produto * 0.1
    print(f'O valor final fica R${valor_produto - desconto_dinheiro:.2f}')
elif metodo_pagamento == 2:
    desconto_cartao = valor_produto * 0.05
    print(f'O valor final fica R${valor_produto - desconto_cartao:.2f}')
elif metodo_pagamento == 3:
    print(f'O valor final fica R${valor_produto:.2f}')
elif metodo_pagamento == 4:
    parcela_pergunta = int(input('Quantas parcelas? '))
    parcela = valor_produto + (valor_produto * 0.2)
    parcela_dividida = parcela / parcela_pergunta
    print(f'Sua compra será parcelada em {parcela_pergunta}x de R${parcela_dividida:.2f}')
else:
    print('Metodo de pagamento invalido')