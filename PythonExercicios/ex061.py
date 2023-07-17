prim = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
c = 0
while c < 10:
    print('{} ->'.format(prim), end=' ')
    prim += raz
    c += 1
print('FIM.')
