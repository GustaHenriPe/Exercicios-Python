from random import randint
vit = 0
while True:
    jogador = int(input('Digite um valor: '))
    esc = ' '
    while esc not in 'PI':
        esc = str(input('Par ou Ímpar [P/I]: ')).upper().strip().split()[0]
    print('--' * 20)
    computador = randint(0, 10)
    result = jogador + computador
    if result % 2 == 0:
        resp = 'PAR'
    else:
        resp = 'ÍMPAR'
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {result} deu {resp}')
    print('--' * 20)
    if esc == 'P' and resp == 'PAR' or esc == 'I' and resp == 'ÍMPAR':
        print('Você venceu!!')
        print('Vamos jogar de novo.')
        print('--'*20)
        vit += 1
    else:
        print('Você perdeu!!!')
        break
print(f'Você venceu {vit} vezes')