preco = float(input('Digite o valor do produto: R$'))
desconto = preco * 0.05 # preço * 5 / 100
novo = preco - desconto
print('O valor do produto é R${:.2f} e com desconto ficará R${:.2f}'.format(preco, novo))
