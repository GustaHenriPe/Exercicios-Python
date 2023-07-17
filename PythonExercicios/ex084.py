dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    esc = input('Quer continuar? [S] [N] ').upper()
    if esc not in 'SN':
        print('VALOR INVÁLIDO! Digite novamente.')
        esc = input('Quer continuar? [S/N] ').upper()
    if esc in 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
