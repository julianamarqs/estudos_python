# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
print('-=' * 20)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('-=' * 20)
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou! O número era {computador}. Você precisou de {tentativas} tentativas para acertar.')