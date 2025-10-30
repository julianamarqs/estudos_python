# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
cont = 1
soma = 0
while True:
    num = int(input('Informe um número: '))
    if num == 999:
        cont -= 1
        break
    else:
        cont += 1
        soma += num
print(f'Foram digitados {cont} números até a parada e a soma entre eles é {soma}')
