'''
valore digitados são 9, 3, 2, 9
index para achar a posição em uma tupla
'''
num = (int(input('Digite um numero: ')),
     int(input('Digite um numero: ')),
     int(input('Digite um numero: ')),
     int(input('Digite um numero: ')))
print(f'Você digitou os Valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
   print(f'O numero 3 paraceu na {num.index(3) + 1}º posição ')
else:
    print('O numero 3 não foi digitado em nunhuma posição')
print('Os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

