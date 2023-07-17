print('=='*20)
print('TABUADA ')
print('=='*20)
num = int(input('Digite um número inteiro: '))
for c in range(1, 11):
    mult = num * c
    print('{} X {} = {}'.format(num, c, mult))
