c = 1
s = mil = 0
while True:
    prod = str(input(f'Digite o {c}° produto: '))
    preco = float(input(f'Digite o preço do {c}° produto: '))
    s += preco
    if preco > 1000:
        mil += 1
    if c == 1:
        barato = prod
        pbarato = preco
    if preco > pbarato:
        barato = prod
        pbarato = preco
    c += 1
    loop = ' '
    while loop not in 'SN':
        loop = str(input('Quer continuar? [S/N]')).upper().strip().split()[0]
    if loop == 'N':
        break
print(f'No total a compra fica R${s}.')
print(f'{mil} produtos custaram mais de R$1000')
print(f'O produto mais barato foi o/a {barato} que custa R${pbarato}')

