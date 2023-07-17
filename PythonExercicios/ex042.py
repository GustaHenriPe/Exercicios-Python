import math
ra = float(input('Digite o comprimento da primeira reta: '))
rb = float(input('Digite o comprimento da primeira reta: '))
rc = float(input('Digite o comprimento da primeira reta: '))
if ra < rb + rc and rb < ra + rc and rc < ra + rb:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if ra  == rb == rc:
        print('Equilátero')
    elif ra == rb or ra == rc or rb == rc:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Os segmentos acimos não podem formar um triângulo')
