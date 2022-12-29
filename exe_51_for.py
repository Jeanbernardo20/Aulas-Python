'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostrar os 10 primeiros termos dessa progressão. 
'''
primeiro = int(input('primeiro termo? '))
razao = int(input('Digite a razão? '))
decimo = primeiro + (11-1) * razao

for c in range(primeiro, decimo, razao):
    print(f'{c}', end="-> ")

print('Acabou')