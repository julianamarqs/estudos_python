# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' Loja Luna '))
valor_produto = float(input('Informe o valor do produto: R$ '))
print('''Escolha a forma de pagamento: 
      [1] À vista dinheiro/cheque
      [2] À vista no cartão
      [3] Em até 2x no cartão
      [4] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = valor_produto - (valor_produto * 0.10)
    print(f'O valor a ser pago é de R${total:.2f} com 10% de desconto.')
elif opcao == 2:
    total = valor_produto - (valor_produto * 5 / 100)
    print(f'O valor a ser pago é de R${total:.2f} com 5% de desconto.')
elif opcao == 3:
    valor_parcelas = valor_produto / 2
    print(f'O valor a ser pago é de R${valor_produto:.2f} em 2x de R${valor_parcelas:.2f} no cartão, sem juros.')
elif opcao == 4:
    total = valor_produto + (valor_produto * 20 / 100)

    parcelas = int(input('Quantas parcelas? '))
    valor_parcelas = total / parcelas
    print(f'Sua compra será parcelado em {parcelas}x de R${valor_parcelas:.2f} com juros.')
    print(f'Sua compra é de R${valor_produto:.2f} e vai custar R${total:.2f} no final.')
else:
    print('Opção inválida. Tente novamente.')
