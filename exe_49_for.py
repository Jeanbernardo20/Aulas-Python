'''
Desafio 049

Refaça o desafio 009, mostrando a tabuada de um numero que o usuário escolher,
só que agora utilizando um laço for  

'''
num = int(input('Digite um numero para ver a tabuada? '))
for c in range(1,11):
    tabuada = num * c
    print(f'{num} x {c} = {tabuada}')


