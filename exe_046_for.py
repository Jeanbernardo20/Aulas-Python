'''
Desafio 046 contagem regressiva

faça um programa que mostre na tela uma 
contagem regressiva para o estouro de
fogos de artifícios, indo de 10 a 0, com
pausa de 1 segundo entre eles
'''
from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("Feliz ano novo")