'''
aula sobre for para repetições
'''
# ele desconsidera o ultimo caractere ou seja de (1 a 5 somente)
'''for c in range(1,6): 
    print(c)
'''
i = int(input('Início? '))
f = int(input('Fim? '))
p = int(input('passo? '))

for c in range (i, f+1, p): #f+1 vai até o final do range
    print(c) 