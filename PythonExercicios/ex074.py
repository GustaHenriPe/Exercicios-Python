from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0,  100))
print('Os números são: ', end='')

menor = maior = numeros[0]
for c in numeros:
    print(f'{c} ', end='')
    if c > maior:
        maior = c
    elif c < menor:
        menor = c
print(f'\nO menor número foi o {menor}')
print(f'O maior número foi o {maior}')
#print(f'\nO menor número foi o {min(numeros)}')
#print(f'O maior número foi o {max(numeros)}')



