# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
n = random.randint(0, 5) # Faz o computador "pensar" em um número entre 0 e 5
print('Adivinhe o número que eu pensei entre 0 e 5...')
num = int(input('Em que número eu pensei? ')) 
if num == n:
    print('Parabéns! Você me venceu!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(n, num))
# Obs: usei o randint que inclui o 5, diferente do randrange que não inclui o 5.