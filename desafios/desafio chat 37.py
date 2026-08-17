nomes = ['Pucas', 'Zanderson', 'Kophia', 'Huis', 'Reticia']
copia = nomes.copy()
copia_decrescente = nomes.copy()
copia.sort()
copia_decrescente.sort(reverse=True)
print(*nomes)
print(*copia)
print(*copia_decrescente)