# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1: # primeira iteração
        maior = peso # inicializa o maior peso
        menor = peso # inicializa o menor peso
    else:
        if peso > maior: # atualiza o maior peso
            maior = peso
        if peso < menor: # atualiza o menor peso
            menor = peso
print(f'O maior peso lido foi {maior:.1f}kg.')
print(f'O menor peso lido foi {menor:.1f}kg.')
