'''
Desafio 048 
Faça um programa que calcule
a soma entre os numeros ímpares
que são multiplos de três e que se 
encontram no intervalo de 1 a 500. 
'''
soma = 0
cont=0
for i in range(1, 501, 2):
    if i % 3 == 0: # numeros que são multiplos i % 3 == 0
        soma+= i
        cont+= 1
print(f' a soma de todos os {cont} valores solicitados é {soma}')

