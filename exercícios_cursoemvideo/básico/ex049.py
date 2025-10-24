# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Insira um número para ver a tabuada: '))
print('-=-' * 5)
for cont in range(1, 11):
    print(f'{num} x {cont:2} = {num*cont}')
print('-=-' * 5)