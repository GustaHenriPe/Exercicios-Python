from random import randint
from time import sleep
alea = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-'*20)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if  alea == num:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Você perdeu! Pensei no número {} e não no {}'.format(alea, num))

