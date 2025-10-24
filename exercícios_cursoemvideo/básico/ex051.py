# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 -1) * razão
print('Os 10 primeiros termos da PA são: ')
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end=' → ')
print('ACABOU')
