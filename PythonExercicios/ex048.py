soma = 0
vezes = 0
for c in range(1, 501,):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
        vezes += 1
print('A soma dos {} valores é {}'.format(vezes, soma))

