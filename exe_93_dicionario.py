'''
Crie um Programa que gerencie o aproveitamento e um jogador de futebol.
o programa vai ler o nome do jogador e quantos partida ele jogou. ok

Depois vai ler a quantidadde e gols que ele fez na partida. ok

No final. tudo isso será guardado em um dicionário. ok
Incluindo total de gols feitos durante o campeonato. ok
'''
# criar um dicionario vazio 
jogador = dict()
partidas = list()

# variavel de total e gols


# informar o nome e as quantidades de partida do jogador
jogador['nome'] = str(input('Nome do jogador: '))

tot = int(input('número de partidas: '))

# Lendo a quantidade de gols feitos na partida atual e adicionando ao total de gols
for c in range (0, tot):
    partidas.append(int(input(f'   Quanto gols na partida {c + 1 }º: ')))
    jogador['gols'] = partidas
    jogador['total'] = sum(partidas)
print(jogador)

print('-='*30)
for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas. ")


for i, v in enumerate(jogador['gols']):
     print(f'  =>  na partida {i + 1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')

