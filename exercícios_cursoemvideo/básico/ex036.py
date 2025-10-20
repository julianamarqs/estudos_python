# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Em quantos anos ele vai pagar? '))
prestacao = casa / (anos * 12) # o valor da prestação mensal resulta da divisão do valor da casa pelo número total de meses (anos * 12)
minimo_mensal = salario * 0.3 # 30% do salário do comprador
print(f'Para pagar uma casa no valor de R$ {casa:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f}.')
if prestacao <= minimo_mensal:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
