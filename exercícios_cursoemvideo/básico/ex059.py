# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
valor01 = int(input('Digite um valor: '))
valor02 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('-=-' * 10)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa''')
    opção = int(input('>>> Informe qual operação você deseja realizar: '))
    print('-=-' * 10)
    if opção == 1:
        soma = valor01 + valor02
        print(f'O valor da soma de {valor01} com {valor02} é de {soma}')
    elif opção == 2:
        produto = valor01 * valor02
        print(f'O valor da multiplicação dos valores {valor01} e {valor02} é de {produto}')
    elif opção == 3:
        if valor01 > valor02:
            maior = valor01
        else:
            menor = valor02
        print(f'O maior valor entre {valor01} e {valor02} é {maior}')
    elif opção == 4:
        print("Voltando para a entrada de novos números...")
        valor01 = int(input('Digite um valor: '))
        valor02 = int(input('Digite outro valor: '))
    elif opção == 5:
        print('Saindo...')
        break
    else:
        print('Opção inválida! Tente novamente.')
    print('-=-' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
