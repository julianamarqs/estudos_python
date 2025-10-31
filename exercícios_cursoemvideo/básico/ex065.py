# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print('=-' * 20)
print(f'Você digitou {quant} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
