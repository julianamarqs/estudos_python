# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('-=' * 20)
print('ANALISANDO OS VALORES...')
print('-=' * 20)

# Descobrindo o menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Descobrindo o maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
