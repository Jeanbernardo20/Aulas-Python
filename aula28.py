"""
Exercício
Peça ao usuário para digitar seu nome ok 
Peça ao usuário para digitar sua idade ok 
Se nome e idade forem digitados: ok
    Exiba:
        Seu nome é {nome} ok
        Seu nome invertido é {nome invertido} ok
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras ok
        A primeira letra do seu nome é {letra} ok
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = str(input('Digite o seu nome: ')).upper()
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")

