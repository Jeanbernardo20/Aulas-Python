# a tupla vem dentro de parenteses ()
# tuplas são imutáveis
# count conta quantos elemento iguais aparacem na tupla
# index fala a posição
''' sinal de + junta as duas tupla criando um terceira tupla
exemplos:
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
será printando (1, 2, 3, 4, 5, 6)
'''


# formas de usar tuplas
lanche = ('hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frito' )

# modo tradicional
#for comida in lanche:
    #print(f'Eu vou comer {comida}')

# modo para saber a posição 
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche [cont]} na posição {cont}')

# outro modo para saber a posição 
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('comi pra caramba')
    



