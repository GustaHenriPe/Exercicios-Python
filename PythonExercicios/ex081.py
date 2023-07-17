lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    esc = input('Quer continuar? [S/N] ').upper()
    if esc not in 'SN':
        print('VALOR INVÁLIDO! Digite novamente.')
        esc = input('Quer continuar? [S/N] ').upper()
    if esc in 'N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse= True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista')
