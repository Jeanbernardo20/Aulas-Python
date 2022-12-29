'''
Desenvolva um programa que leia seis numero interios e mostre a soma daqueles que forem pares, se o valor for impar desconsidere-o
'''
soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('digite um número? ')) # dentro do for repete o input
    if num % 2 == 0:
        soma+=num
        cont+=1
    
print(f'Você informou {cont} Pares e a soma foi {soma}')