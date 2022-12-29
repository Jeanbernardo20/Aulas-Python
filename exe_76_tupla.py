listagem = ('Borracha', 1.75, 
            'Caderno', 25,
            'Boracha', 2, 
            'Apontador', 2.50, 
            'Lápis', 1.50, 
            'Caneta', 2,
            'Mochila', 120)

print(listagem)
print('-' *40)
print('LISTAGEM DE PREÇO')
print('-' *40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' *40)
  

