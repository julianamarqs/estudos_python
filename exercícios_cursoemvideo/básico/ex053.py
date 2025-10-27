# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # Divide a frase em palavras
junto = ''.join(palavras) # Junta as palavras sem espaços
inverso = junto[::-1] # Inverte a string

'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]''' # Forma alternativa de inverter a string

print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO É UM PALÍNDROMO!')
