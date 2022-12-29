'''
Crie um programa que leia:
nome: ok
ano de nascimento: ok
carteira de trabalho: ok

Cadastre-os com idade em um dicionrio ok

acaso a CTPS for diferente de zero ok
o dicionario receberá tambem o ano de contratação e o salario. ok

Calcule e acrescente além da idade. com quantos anos a pessoas vai se aposentar

'''
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('nome: '))
nasc = int(input('Qual a data de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Qual o seu CTPS (0 não tem): '))

if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Qual o ano da contratação: '))
    dados['Salario'] = float(input('Qual o seu salario R$: '))
    dados['aposentadoria'] = dados['Idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('-='*30)
for k, v in dados.items(): # pasra imprimir as chaves e os valores
    print(f' - {k} tem valor {v}')











