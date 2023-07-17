print('Calculadora de fatorial')
num = int(input('Digite um número e veja seu fatorial: '))
print('Calculando {}! = '.format(num), end='')
result = 1
numfat = num
while numfat > 0:
    print('{} '.format(numfat), end='')
    print('X ' if numfat > 1 else '= ', end='')
    result *= numfat
    numfat -= 1
print('{}'.format(result))
