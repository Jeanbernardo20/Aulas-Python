'''
Desafio 67

Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. o programa será interrompido quando o valor for negativo  
'''

while True:
    print('-' * 30)
    num = int(input('Qual taboada você deseja ver? '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    
print('PROGRAMA ENCERRADO. volte sempre!')
