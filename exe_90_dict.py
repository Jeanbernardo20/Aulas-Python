aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'A média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(aluno)



