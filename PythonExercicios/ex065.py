resp = 'S'
maior = 0
menor = 0
soma = 0
div = 0
fim = 1
while resp == 'S':
    while div < fim:
        num = int(input('Digite um número: '))
        soma += num
        div += 1
        if div == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    resp = str(input('Você quer ler mais números? [S/N] ')).upper()
    if resp == 'S':
        fim += 1
md = soma / div
print('A média entre os números digitados é {}'.format(md))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
