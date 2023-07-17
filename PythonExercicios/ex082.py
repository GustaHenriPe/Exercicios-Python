listanum = list()
listapar = list()
listaimpar = list()
while True:
    listanum.append(int(input('Digite um valor: ')))
    esc = input('Quer continuar? [S/N] ').upper()
    if esc not in 'SN':
        print('VALOR INVÁLIDO! Digite novamente.')
        esc = input('Quer continuar? [S/N] ').upper()
    if esc in 'N':
        break
for i, v in enumerate(listanum):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print('-='*30)
print(f'A lista completa é {listanum}')
print(f'A lista de  pares é {listapar}')
print(f'A lista de impares é {listaimpar}')
