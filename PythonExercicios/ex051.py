prim = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
for c in range(0, 10):
    print('{} ->'.format(prim),end=' ')
    prim += raz
print('FIM.')