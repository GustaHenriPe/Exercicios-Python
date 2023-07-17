from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Opções:
 [ 1 ] Pedra 
 [ 2 ] Papel
 [ 3 ] Tesoura''')
jogador = int(input('Qua a sua jogada? ')) - 1
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-='*20)
print('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-='*20)
if computador == 0: #pedra
    if jogador == 0:
        print('Empate!!! Ninguém ganhou!!!')
    elif jogador == 1:
        print('GANHOU!!! O computador perdeu!!!')
    elif jogador == 2:
        print('PERDESTE!!! O computador ganhou!!!')
    else:
        print('Jogada Inválida!!')
elif computador == 1: #papel
    if jogador == 0:
        print('PERDESTE!!! O computador ganhou!!!')
    elif jogador == 1:
        print('Empate!!! Ninguém ganhou!!!')
    elif jogador == 2:
        print('GANHOU!!! O computador perdeu!!!')
    else:
        print('Jogada Inválida!!')
elif computador == 2: #tesoura
    if jogador == 0:
        print('GANHOU!!! O computador perdeu!!!')
    elif jogador == 1:
        print('PERDESTE!!! O computador ganhou!!!')
    elif jogador == 2:
        print('Empate!!! Ninguém ganhou!!!')
    else:
        print('Jogada Inválida!!')
