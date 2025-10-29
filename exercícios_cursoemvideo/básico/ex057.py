# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')