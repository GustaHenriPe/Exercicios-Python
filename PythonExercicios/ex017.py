from math import hypot
co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digiye a medida do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa é: {}'.format(hip))