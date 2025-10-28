#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
soma_idade = 0
media_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
num_mulheres_menos_20 = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
#- Qual é o nome do homem mais velho
    if c == 1 and sexo == 'M':
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
#- Quantas mulheres têm menos de 20 anos
    if sexo == 'F' and idade < 20:
        num_mulheres_menos_20 += 1

#- A média de idade do grupo 
media_idade = soma_idade / 4
print('----- RESULTADOS -----')
print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos.')
print(f'Ao todo são {num_mulheres_menos_20} mulheres com menos de 20 anos.')
