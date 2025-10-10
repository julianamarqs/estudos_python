num = float(input('Valor na carteira: R$'))
dol = num / 5.38
print('Com R${:.2f} você pode comprar US${:.2f}'.format(num, dol))
