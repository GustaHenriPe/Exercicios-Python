prim = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
term = 10
cont = 0
while term != 0:
    c = 0
    while c < term:
        print('{} ->'.format(prim), end=' ')
        prim += raz
        cont += 1
        c += 1
    print('PAUSA')
    term = int(input('\nVocê quer mostrar mais quantos termos? '))
print('A progressão foi finalizada com {} termos mostrados'.format(cont))
print('FIM.')
