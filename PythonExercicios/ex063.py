print('Sequencia de Fibonacci')
n = int(input('Quantos números você quer mostrar: '))
t1 = 0
t2 = 1
print('__'*30)
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' -> FIM')