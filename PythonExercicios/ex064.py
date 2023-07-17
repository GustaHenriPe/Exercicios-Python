num = int(input('Digite um número inteiro [999 para parar]: '))
soma = 0
cont = 1
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite outro número inteiro [999 para parar]: '))
print('Você digitou {} números, e a soma entre eles é {}.'.format(cont, soma))
