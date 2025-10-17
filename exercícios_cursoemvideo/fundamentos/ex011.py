altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print('A sua parede tem {}m² e será necessário {}l de tinta.'.format(area, tinta))
