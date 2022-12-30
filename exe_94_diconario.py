# criar um dicionario vazio 
galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)

print(f' A) Ao todo temos {len(galera)} pessoas cadastradas') 
media = soma / len(galera) 
print(f' B) A média de idade é de {media:5.2f} anos. ')
print(' C) As mulheres cadastradas foram', end='')
print()
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print(f' D) Listas das pesoas que estão acima da média: ')
for p in galera:
    if p['idade']>= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<< ENCERRADO >>')
