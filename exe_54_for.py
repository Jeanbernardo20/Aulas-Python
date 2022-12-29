'''
Desafio 054

crei um programa que leia o ano de nascimento e sete pessoas. No final. mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores. 
'''
from datetime import date
data_atual = date.today().year # buscar a data atual
tot_maior = 0 #saber q quantidade de maiores
tot_menor = 0 # saber a quantidade de menores
for c in range(1, 8):
    data_nasc = int(input(f'Em que ano a {c}º você nasceu? '))
    idade = data_atual - data_nasc
    if idade >= 21:
        tot_maior+= 1
        
    else:
        tot_menor+=1
        
print(f'Ao todo tivemos {tot_maior} pessoas maiores de idade')
print(f'E também tivemos {tot_menor} pessoas menores de idade')