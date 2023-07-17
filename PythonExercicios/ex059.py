from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
r = 0
while r != 5:
    r = 0

    while r != 1 and r != 2 and r != 3 and r != 4 and r != 5:
        print('''MENU
        [ 1 ] Somar 
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa''')
        r = int(input('Digite sua opção: '))
        if r == 1:
            soma = n1 + n2
            print('A soma de {} e {} é {}'.format(n1, n2, soma))
            print('-='*20)
            r = 0
            sleep(1)
        elif r == 2:
            mult = n1 * n2
            print('A multiplicação de {} e {} é {}'.format(n1, n2, mult))
            print('-='*20)
            r = 0
            sleep(1)
        elif r == 3:
            if n1 > n2:
                print('{} é maior que {}'.format(n1, n2))
                print('-=' * 20)
            elif n1 < n2:
                print('{} é maior que {}'.format(n2, n1))
                print('-=' * 20)
            else:
                print('Os números são iguais')
                print('-=' * 20)
            r = 0
            sleep(1)
        elif r == 4:
            print('Digite os números novamente')
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
        else:
            print('NÚMERO INVÀLIDO, DIGITE NOVAMENTE.')
            print('-=' * 20)
print('Muito obrigado por utilizar')