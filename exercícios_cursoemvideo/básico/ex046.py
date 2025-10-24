# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for contagem in range(10, 0, -1): # se quiser contar até o zero, coloque -1 no lugar do 0
    print(contagem)
    sleep(1)
print('FELIZ ANO NOVO!!!')