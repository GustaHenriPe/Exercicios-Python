contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezeseis', 'dezesete', 'dezoito',
            'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20 e veja ele por extenso: '))
    while True:
        if 0 <= num <= 20:
            break
        else:
            num = int(input('Tente novamente. Digite um número de 0 a 20 e veja ele por extenso: '))
    print(contagem[num])
    esc = str(input('Quer ver outro número? [S/N] ')).upper().strip()
    while True:
        if esc in 'SN':
            break
        else:
            esc = str(input('Digite novamente. Quer ver outro número? [S/N] ')).upper().strip()
    if esc == 'N':
        break
print('Programa encerrado.')
