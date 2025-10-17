from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num))) # trunc() serve para mostrar apenas a parte inteira do número, sem arredondar.

# Outra forma de fazer sem importar nada:
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))