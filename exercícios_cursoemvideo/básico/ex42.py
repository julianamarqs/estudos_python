# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a = float (input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end=' ')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a == b and b != c or a == c and c != b or b == c and c != a:
        print('ISÓSCELES!')
    elif a != b and b != c and a != c:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')