# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input('Informe um número: '))
c = num
factorial = 1
print('-=-' * 10)
while c >= 1:
    factorial *= c
    if c > 1:
        print(f'{c} x ', end='')
    else:
        print(f'{c} =', end=' ')
    c -= 1
print(factorial)
print('-=-' * 10)
