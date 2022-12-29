'''
Faça um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitrado e as suas respectivas posições
'''
valores = list()  # quando usar () colocar list antes.
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for p in enumerate(valores):
    print(f'Os maiores valores digitados foram: {max(valores)} na posição {p}')
    print(f'Os menores valores digitados foram: {min(valores)} na posição {p}')




