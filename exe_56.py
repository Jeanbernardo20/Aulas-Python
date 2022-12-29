'''
Desafio 56 - Analisador completo

Desenvolva um programa que leia o nome, idade e sexo de 4 passoas. no final do programa mostre:
-> A media de idade do grupo
-> Qual é o nome do homem mais velho
-> Quantas mulheres tem menos de 20 anos  
'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'-----{p}º PESSOA ----- ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip() 
    somaidade+= idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
    
media = somaidade/4
print(f'A medias das idades do grupo é de {media} anos')
print(f'O homem mais velho tem {maioridadehomem} anos é se chama {nomevelho}')
print(f'Ao todo são {totmulher20} com menos de 20 anos')
