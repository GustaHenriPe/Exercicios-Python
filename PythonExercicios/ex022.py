nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} ele tem {} letras'.format(separado[0], len(separado[0])))

