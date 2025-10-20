# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão: 
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O número {num} em binário é {bin(num)[2:]}') # [2:] para remover o prefixo '0b'
elif opcao == 2:
    print(f'O número {num} em octal é {oct(num)[2:]}') # [2:] para remover o prefixo '0o'
elif opcao == 3:
    print(f'o número {num} em hexadecimal é {hex(num)[2:]}') # [2:] para remover o prefixo '0x'
else:
    print('Opção inválida! Escolha entre 1, 2 ou 3.')
 