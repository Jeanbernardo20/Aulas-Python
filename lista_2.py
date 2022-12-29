galera = list()
dado = list()
totmaio = totmen = 0
# esse bloco colhe os dados do usuario
for c in range(0, 3): # para p in galera faça
    dado.append(str(input('Digite seu Nome: ').capitalize().strip()))
    dado.append(int(input('Digite sua Idade: ')))
    galera.append(dado[:]) # importante [:] faz uma copia dos dados
    dado.clear() # limpa os dados a cada looping da variavel dado
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaio += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmaio} maiores e {totmen} menores de idade.')

