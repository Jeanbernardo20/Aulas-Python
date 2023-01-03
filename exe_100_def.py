'''
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somapar(). A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valors PARES sortedos pela função anterior>

'''
from random import randint
from time import sleep
def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares {lista}, temos {soma}: ')

numeros = list()
sorteia(numeros)
somapar(numeros)