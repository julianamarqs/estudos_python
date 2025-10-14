import random

aluno01 = input('Primeiro aluno: ')
aluno02 = input('Segundo aluno: ')
aluno03 = input('Terceiro aluno: ')
aluno04 = input('Quarto aluno: ')
lista = [aluno01, aluno02, aluno03, aluno04]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))