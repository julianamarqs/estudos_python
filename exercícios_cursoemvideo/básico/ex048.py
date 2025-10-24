# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for num in range(1, 501, 2): # só números ímpares
    if num % 3 == 0:
        cont += 1
        soma += num
print(f'A soma dos {cont} números ímpares múltiplos de três entre 1 e 500 é de {soma}')
