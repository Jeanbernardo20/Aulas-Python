'''
Desafio 68 
faça um programa que jogue par ou impar com o computador. jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele consquistou no final do jogo
'''
from random import randint
v = 0
while True:
    jogador = int(input('digite um valor? '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total de {total}, ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')




    