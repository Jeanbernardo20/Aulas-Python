'''
Faça um programa que tenha uma função chamada Escreva(), que recebe um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável
'''
# função
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# programa principal
escreva('Jean Bernardo')
escreva('Curso de Python no youtube')
escreva('Cev')

