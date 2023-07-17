num = int(input('Digite um número INTEIRO: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Comverter para Hexadecimal''')
esc = int(input('Sua opção: '))
if esc == 1:
    print('Em binário o número {} é {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('Em octal o número {} é {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('Em hexadecimal o número {} é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')