primeiro_valor = int(input('digite o primeiro valor? '))
segundo_valor = int(input('digite o o segundo valor? '))

if primeiro_valor > segundo_valor:
    print(f'o primeiro valor {primeiro_valor} e maior que o segundo valor {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'os valor são iguais')
else:
    print(f'o segundo valor {segundo_valor} e maior que primeiro valor {primeiro_valor}')