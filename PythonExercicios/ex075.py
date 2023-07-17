numeros = (int(input('Digite o primeiro número: ')),
int(input('Digite o segundo número: ')),
int(input('Digite o terceiro número: ')),
int(input('Digite o quarto número: ')),)
print(f'Você digitou os valores: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número três a aparece primeiro na posição {numeros.index(3) + 1}.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ', end=' ')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')


