# Crie um programa duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
nota01 = float(input('Primeira nota: '))
nota02 = float(input('Segunda nota: '))
media = (nota01 + nota02) / 2
print(f'Tirando {nota01:.1f} e {nota02:.1f}, a média do aluno é {media:.1f}')
if media < 5.0:
    print('O aluno está REPROVADO.')
elif media >= 5.0 and media <=6.9:
    print('O aluno está de RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')
