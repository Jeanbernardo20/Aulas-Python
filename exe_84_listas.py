# Criando as listas
temp = list()
princ = list ()
mai = men = 0


# Criando os loops e colha dos dados 
while True:
   temp.append(str(input('Digite seu Nome: ').capitalize()))
   temp.append(float(input('Digite seu Peso: ')))
   if len(princ) == 0:
      mai = men = temp[1]
   else:
      if temp[1] > mai:
         mai = temp[1]
      if temp[1] < men:
         men = temp[1]
   princ.append(temp[:])
   temp.clear()
   resp = str(input('Deseja Continuar? [S/N] '))
 
# Parando o looping:
   if resp in 'Nn':
      break
  
# imprimindo os dados
print(f'Ao todo você Cadastrou {len(princ)} Pessoas')
print(f'O maior peso foi de {mai} kg. de ', end=' ')
for p in princ:
   if p[1] == mai:
      print(f'[{p[0]}]', end=' ')
print()
print(f'O maior peso foi de {mai} kg. de ', end=' ')
for p in princ:
   if p[1] == men:
      print(f'[{p[0]}]', end=' ')
print()



   
   
