'''
Desafio 52
Faça om programa que leia um numero inteiro e diga se ele e ou não numero primo
'''
num = int(input('Digite um numero para saber se ele e primo? '))
tot = 0

for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1 
    else:
      print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[m0 número {num} foi divisivel {tot} vezes')
if tot == 2:
    print(f'e por isso que ele é PRIMO')
else:
    print(f'e por isso que ele não e PRIMO')



