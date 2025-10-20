n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
md = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno  é {md}')
if md >= 7:
    print('O aluno está APROVADO.')
elif 5 <= md < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')
