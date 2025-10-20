# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_atual = date.today().year
print('=== ALISTAMENTO MILITAR ===')
ano_nascimento = int(input('Digite o ano de nascimento: '))
print('''Informe o seu sexo:
      [1] Masculino
      [2] Feminino''')
sexo = int(input('Escolha uma opção: '))
print('---' * 10)
if sexo == 2:
    print('O alistamento militar é obrigatório apenas para homens.')
    exit()
elif sexo == 1:
    idade = ano_atual - ano_nascimento
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')
    if idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o alistamento.')
        print(f'Seu alistamento será em {ano_atual + saldo}.')
    elif idade == 18:
        print(f'Está na hora de se alistar ao serviço militar!')
    else:
        saldo = idade - 18
        print(f'Já passou {saldo} anos do prazo de alistamento.')
        print(f'Seu alistamento foi em {ano_atual - saldo}.')
