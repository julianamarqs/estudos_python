from math import hypot

coposto = float(input('Comprimento do cateto oposto: '))
cadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(coposto, cadjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

# Solução sem usar a biblioteca math
#hipotenusa = (coposto ** 2 + cadjacente ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))