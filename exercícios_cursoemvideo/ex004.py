txt = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(txt)))
print('Só tem espaços? {}'.format(txt.isspace())) #
print('É um numero? {}'.format(txt.isnumeric())) # 2
print('É alfabético? {}'.format(txt.isalpha())) # py
print('É alfanumérico? {}'.format(txt.isalnum())) # py2
print('Está em maiúsculo? {}'.format(txt.isupper())) # python
print('Está em maiúsculo? {}'.format(txt.islower())) # PYTHON
print('Está capitalizada? {}'.format(txt.istitle())) #Python