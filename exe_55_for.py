'''
Desafio 55

Faça um programa que leia o peso de 5 pessoas. no final, mostre qual maior e o menor peso lidos 
'''
maior = 0
menor = 0
for p in range(1, 6 ):
    peso = float(input(f'Peso da {p}º pessoa? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior} kg')
print(f'O menor peso lido foi de {menor} kg')



