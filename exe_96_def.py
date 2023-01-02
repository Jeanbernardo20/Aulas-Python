'''
Faça um programa que tenha uma função chamada área(), que recebe as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
# função
def area(larg, comp):
    a= larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m2.')
 
  
# programa principal
print('Controle de terreno')   
print('-='*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
    
area(l, c)      
