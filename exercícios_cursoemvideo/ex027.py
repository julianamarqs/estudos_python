# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador= randint(0, 5) # Faz o computador "pensar" em um número entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) 
print('PROCESSANDO...')
sleep(2) # Pausa de 2 segundos para dar suspense
if jogador == computador:
    print('Parabéns! Você me venceu!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
# Obs: usei o randint que inclui o 5, diferente do randrange que não inclui o 5.