'''
Crie um programa que leia varios números pelo teclado. o programa só vai parar quando o usuario digitar 999.  que é a condição de parada. No final. mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)
'''
soma = cont = 0 
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont+=1 
print(f'Você digitou {cont} números soma os numeros é {soma}')