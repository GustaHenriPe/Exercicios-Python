r = ''
while r != 'M' and r != 'F':
    r = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
    if r != 'M' and r  != 'F':
        print('Comando incorreto, digite novamente.')
print('Sexo {} registrado com sucesso'.format(r))
