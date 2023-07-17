from random import randint
r = False
tent = 0
alea = randint(0, 10)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar...')
print('-=-'*20)
while not r:
    num = int(input('Em que número eu pensei? '))
    if alea == num:
        print('Parabéns! Você conseguiu me vencer!')
        r = True
    else:
        if num < alea:
            print('MAIS... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
    tent += 1
print('Você me venceu em {} tentativas'.format(tent))
