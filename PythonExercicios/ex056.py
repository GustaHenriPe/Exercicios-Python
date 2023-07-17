somaid = 0
somamu = 0
maioridhm = 0
nomevelho = ''
for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaid += idade
    if sexo == 'F' and idade < 20:
        somamu += 1
    somaid += idade
    if c == 1 and sexo == 'M':
        maioridhm = idade
        nomevelho = nome
    if idade > maioridhm and sexo == 'M':
        maioridhm = idade
        nomevelho = nome
md = somaid / 4
print('A média das idades é {:.1f}'.format(md))
print('Tem {} mulheres que tem menos de 20 anos '.format(somamu))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridhm, nomevelho))