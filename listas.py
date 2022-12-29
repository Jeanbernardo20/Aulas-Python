'''
num = [2, 5, 9, 1] # É uma lista 
num[2] = 3
num.append(7) # Adiciona um novo elemento a lista
num.sort(reverse=True) # Coloca em ordem a lista 
num.insert(2, 2) # Insere um elemento na posição desejada
if 5 in num:
    num.remove(5)
else:
    print('Não encontrei o numero 5')
print(num)
print(f'Essa lista tem {len(num)} elementos. ')

# Outro exemplo
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('cheguei ao final da lista')
'''
# Outro exemplo
a = [2, 3, 4, 7]
b = a[:] # faz uma copia da lista a
b[2] = 8
print(f'Lista A:{a}')
print(f'Lista B: {b}')