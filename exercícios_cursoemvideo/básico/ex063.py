# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#Exemplo: 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - ...
print('--' * 10)
print('Sequência de Fibonacci')
print('--' * 10)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
