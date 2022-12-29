# criar um dicionario vazio 
galera = list()
pessoa = dict()

while True:
    galera.clear()
    pessoa['nome'] = str(input('Qual seu Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F')
    pessoa['idade'] = int(input('idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!, responda S ou N')
    if resp == 'N':
        break
print('-='*30)

print(f' Ao todo temos {len(galera)} cadastrado')  