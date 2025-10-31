# Opção 1 - Usando a biblioteca math
'''from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Informe um número: '))
cont = num
factorial = 1
print('-=-' * 10)
print(f'Calculando {num}!')
while cont > 0:
    print(f'{cont}', end='')
    print(f' x ' if cont > 1 else ' = ', end='') # se for verdadeiro imprimi ' x ' se não for imprimi ' = '
    factorial *= cont
    cont -= 1
print(factorial)
print('-=-' * 10)
