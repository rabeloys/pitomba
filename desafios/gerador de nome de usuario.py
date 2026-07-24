import random
import string
caracteres = string.ascii_lowercase + string.digits
caracteres1 = random.choice(caracteres).upper()
caracteres2 = random.choice(caracteres).lower()
caracteres3 = random.choice(caracteres).lower()
caracteres4 = random.choice(caracteres).upper()
caracteres5 = random.choice(caracteres).lower()
caracteres6 = random.choice(caracteres).lower()
caracteres7 = random.choice(caracteres).upper()
caracteres8 = random.choice(caracteres).lower()
senha = caracteres1 + caracteres2 + caracteres3 + caracteres4 + caracteres5 + caracteres6 + caracteres7 + caracteres8
nome = input('Digite seu nome: ').strip()
sobrenome = input('Digite seu sobrenome: ').strip()
ano_nasceu = int(input('Digite o ano que você nasceu: '))
anousuario = str(ano_nasceu)
usuario = nome.lower() + '.' + sobrenome.lower() + anousuario
print('Usuario criado com sucesso!')
print()
print(f'O seu nome de usuario será {usuario}')
print(f'A sua senha é essa: {senha}. Não compartilhe com ninguem 🤫')