dist = float(input('Digite a distância da sua viagem: '))
if dist <= 200:
    preço = dist * 0.50
    print('O preço da passagem ficou {}'.format(preço))
else:
    preço = dist * 0.45
    print('O prdço da passagem ficou {}'.format(preço))